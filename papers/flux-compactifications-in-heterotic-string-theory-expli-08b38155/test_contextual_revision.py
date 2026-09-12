"""Bounded editorial checks; no scientific source calculation is rerun."""

import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
import unittest

import sympy as sp


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULTS = ROOT.parent / "TEXPAPERS/mtt-results-repro/release/results"


def clean(form):
    return {key: sp.expand(value) for key, value in form.items() if sp.expand(value) != 0}


def add(*forms):
    result = {}
    for form in forms:
        for key, value in form.items():
            result[key] = result.get(key, 0) + value
    return clean(result)


def scale(c, form):
    return clean({key: c * value for key, value in form.items()})


def wedge(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            if set(a) & set(b):
                continue
            sign = (-1) ** sum(i > j for i in a for j in b)
            key = tuple(sorted(a + b))
            result[key] = result.get(key, 0) + sign * x * y
    return clean(result)


def basis(*indices):
    return {tuple(indices): sp.Integer(1)}


def exterior_d(form, structure):
    result = {}
    for indices, coefficient in form.items():
        for position, index in enumerate(indices):
            term = wedge(basis(*indices[:position]), structure.get(index, {}))
            term = wedge(term, basis(*indices[position + 1:]))
            result = add(result, scale(coefficient * (-1) ** position, term))
    return result


class ContextualRevisionTests(unittest.TestCase):
    def test_iwasawa_torsion_sign(self):
        # Ordered basis: w1,w2,w3,bar(w1),bar(w2),bar(w3).
        structure = {3: basis(1, 2), 6: basis(4, 5)}
        omega = scale(sp.I / 2, add(basis(1, 4), basis(2, 5), basis(3, 6)))
        derivative = exterior_d(omega, structure)
        self.assertEqual(derivative[(3, 4, 5)], -sp.I / 2)
        H = scale(sp.Rational(1, 2), add(basis(3, 4, 5), basis(1, 2, 6)))
        self.assertEqual(exterior_d(H, structure), basis(1, 2, 4, 5))
        ab = wedge(scale(sp.I / 2, basis(1, 4)), scale(sp.I / 2, basis(2, 5)))
        self.assertEqual(exterior_d(H, structure), scale(4, ab))
        self.assertEqual(exterior_d(wedge(omega, omega), structure), {})

    def test_lens_nil_forms(self):
        a, b, c = sp.symbols("a b c")
        structure = {1: basis(2, 3), 2: scale(-1, basis(1, 3)),
                     3: basis(1, 2), 6: basis(4, 5)}
        J = add(scale(a, basis(1, 2)), scale(b, basis(3, 6)), scale(c, basis(4, 5)))
        omega = wedge(wedge(add(basis(1), scale(sp.I, basis(2))),
                            add(basis(3), scale(sp.I, basis(4)))),
                      add(basis(6), scale(sp.I, basis(5))))
        self.assertEqual(exterior_d(wedge(J, J), structure),
                         {(1, 2, 3, 4, 5): -2*a*b, (1, 2, 4, 5, 6): 2*b*c})
        self.assertEqual(wedge(J, omega),
                         clean({(1, 3, 4, 5, 6): c-b, (2, 3, 4, 5, 6): sp.I*(c-b)}))
        # In the theta-coframe, e4=(theta2-bar2)/(2i), e5=(theta3-bar3)/(2i).
        dtheta3 = wedge(scale(1/(2*sp.I), add(basis(2), scale(-1, basis(5)))),
                        scale(1/(2*sp.I), add(basis(3), scale(-1, basis(6)))))
        self.assertEqual(dtheta3[(5, 6)], -sp.Rational(1, 4))

    def test_full_maurer_cartan(self):
        def unit(i, j):
            M = sp.zeros(3)
            M[i-1, j-1] = 1
            return M
        comm = lambda A, B: A*B-B*A
        B1, B2, B3 = unit(1, 3), -unit(3, 2), unit(1, 2)
        self.assertEqual(B3+comm(B1, B2), sp.zeros(3))
        self.assertEqual(comm(B1, B3), sp.zeros(3))
        self.assertEqual(comm(B2, B3), sp.zeros(3))
        # The first equation alone is insufficient for general constant matrices.
        C1, C2 = unit(1, 2), unit(2, 1)
        C3 = -comm(C1, C2)
        self.assertNotEqual(comm(C1, C3), sp.zeros(3))

    def test_crt_and_primitive_lag(self):
        self.assertEqual([q for q in range(448) if q % 64 == 15 and q % 7 == 2], [79])
        self.assertEqual(sp.gcd(64, 63), 1)

    def test_integral_relation_and_discriminant(self):
        A = sp.Matrix([[-2, 1], [1, -2], [-1, -1]])
        d = sp.Matrix([1, 0, 1])
        self.assertEqual((sp.Matrix([[1, 1, -1]])*d)[0], 0)
        self.assertEqual(A*sp.Matrix([-sp.Rational(2, 3), -sp.Rational(1, 3)]), d)
        self.assertEqual(A*sp.Matrix([2, -1]), sp.Matrix([-5, 4, -1]))
        self.assertEqual(3**22*54, 1694577218886)

    def test_pairing_one_and_factorial(self):
        self.assertEqual(2*4-7, 1)
        self.assertEqual(pow(6, -1, 11), 2)
        for a in range(-19, 20, 2):
            y = 1 if a % 4 == 1 else -1
            x = (1-a*y)//4
            self.assertEqual(4*x+a*y, 1)

    def test_frozen_hashes_and_full_json_parse(self):
        rows = json.loads((ROOT / "catalog/research-ownership.json").read_text(encoding="utf-8"))["results"]
        assigned = [r for r in rows if r["integration_owner"] == HERE.name]
        self.assertEqual(len(assigned), 56)
        for row in assigned:
            path = RESULTS / row["result_id"] / row["artifact_url"].rsplit("/", 1)[1]
            raw = path.read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"], row["result_id"])
            if path.suffix == ".json":
                json.loads(raw)

    def test_complete_frontier_partitions(self):
        packet = json.loads((RESULTS / "eta9_three_cycle_frontier_merge/artifact.json").read_bytes())
        self.assertEqual(len(packet["sources"]), 81)
        self.assertEqual(len(packet["faces"]), 3)
        for face in packet["faces"].values():
            codes = sorted(face["completed_leaf_codes"])
            self.assertEqual(len(codes), len(set(codes)))
            self.assertTrue(all(not b.startswith(a) for a, b in zip(codes, codes[1:])))
            self.assertEqual(sum(Fraction(1, 2**len(c)) for c in codes), 1)
            self.assertEqual(face["residual_leaf_codes"], [])

    def test_all_endpoint_records(self):
        packet = json.loads((RESULTS / "eta9_three_cycle_endpoint_projection/artifact.json").read_bytes())
        cycles = packet["cycle_projections"]
        self.assertEqual([len(c["cells"]) for c in cycles], [1798, 1517, 936])
        self.assertEqual(sum(len(c["cells"]) for c in cycles), 4251)
        for cycle in cycles:
            self.assertEqual(sum(cycle["face_cell_counts"].values()), len(cycle["cells"]))
            for cell in cycle["cells"]:
                self.assertEqual(len(cell["endpoint_box"]), 10)
                for key in ("packet_sha256", "mathematical_certificate_sha256"):
                    self.assertRegex(cell[key], r"^[a-f0-9]{64}$")
                for interval in cell["endpoint_box"]:
                    match = re.fullmatch(r"\[(?:([^ ]+) )?\+/- ([^ ]+)\]", interval)
                    self.assertIsNotNone(match)
                    Fraction(match[1] or "0")
                    self.assertGreaterEqual(Fraction(match[2]), 0)
        self.assertEqual(sp.det(-2*sp.eye(3)), -8)

    def test_response_dimensions(self):
        self.assertEqual(249-126-1, 122)
        self.assertEqual(122-70, 52)
        self.assertEqual(82-70, 12)
        self.assertEqual(196-126, 70)
        self.assertEqual(3*82, 246)

    def test_theta_consumer_corrections(self):
        r, gy, g2 = sp.symbols("r gy g2", positive=True)
        angle = 3*r/(5+3*r)
        self.assertEqual(sp.simplify(angle.subs(r, sp.Rational(5, 3)*gy**2/g2**2)
                                    - gy**2/(gy**2+g2**2)), 0)
        self.assertEqual(sp.simplify(sp.diff(angle, r) - 15/(5+3*r)**2), 0)
        torus = 4*sp.pi**2
        landau_at_one = 2*sp.pi + 4*sp.pi**2
        self.assertEqual(sp.simplify(landau_at_one-torus), 2*sp.pi)
        self.assertLess(float(torus), float(landau_at_one))
        cap = sp.Rational(1989699, 1000000)
        floor = min(float(torus), float(2*sp.pi+4*sp.pi**2/cap**2))
        self.assertGreater(floor, 16.25)
        self.assertLess(floor, 16.26)


if __name__ == "__main__":
    unittest.main(verbosity=2)
