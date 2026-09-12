"""Apply the reviewed September FP editorial metadata delta, without publishing."""
import json
from pathlib import Path

from verify_fp_foundational_dependencies import FP_ORDER

ROOT = Path(__file__).resolve().parents[1]
VERSIONS = {2: 6, 3: 8, 4: 7, 5: 9, 6: 7}
DELTAS = {
    2: "Replaces the downstream q79 carrier claim by a locally checked tensor-factor example. Retains shared-circle dimension accounting and all joint-operator, existence and coherent-contraction gates. Cites FP I v7.",
    3: "Removes the reverse citation to the finite-mode calculation companion. Its calculations remain owned by that companion, which may cite FP III. The enhanced invariance principle and analytic statements are unchanged. Explicitly cites FP I v7 and FP II v6.",
    4: "Replaces the q79 repository authority by Narasimhan--Ramanan universal connections and local image-module, Schur-elimination and constrained-minimization arguments. Specifies the Hessian domain, complementary inverse and coercivity; adds a two-dimensional example. No ambient extension or physical endpoint is inferred.",
    5: "Removes misleading generic numerical-evidence boilerplate, explicitly cites earlier FP editions and preserves every covariance/correlation/exit theorem and proof. No later MTT research is a premise.",
    6: "Removes the downstream q79 progress ledger and carrier imports. Preserves the FP I--V synthesis, conditional interpretations and two causality propositions. Aligns bibliography to I v7, II v6, III v8, IV v7 and V v9.",
}
ABSTRACTS = {
    2: "We apply the Fixed Points I machinery to a ten-dimensional Riemannian control setting with one compact six-dimensional internal space. Three compatible vertical structures are represented by strongly commuting nonnegative self-adjoint operators. Overlap is allowed; nesting requires supplied inclusion maps and is not inferred from rank labels. Shared phase data can be represented by a common unitary line connection without adding another internal product dimension. We establish projected time-step fixed points through the earlier Schauder and Darbo gates and coherent uniqueness under base coercivity or strong monotonicity. A projected fixed point becomes a full equilibrium only under a strict Lyapunov identity. Fiber gaps damp the noncoherent complement and do not provide coherent contraction.",
    4: "We develop curvature coupling and structural transitions on the Fixed Points I--III framework. Curvature can shift a low spectral cluster, rotate its projector and create leakage into the old noncoherent sector. A bounded perturbation smaller than half the initial gap preserves a separated cluster. Intrinsic centroids are defined by Karcher means, and a first-order gradient parent flow yields a first-order modulation law. Interaction sign requires a separate hypothesis; energy-barrier exclusion and exit detection do not select a post-transition basin. Standard universal connections represent supplied bundle data, while image-module transport preserves the specified connection and Hessian. Local block-elimination and constrained-minimization arguments distinguish invariant restriction, Feshbach reduction and reduced-Green Hessians under explicit domain and coercivity conditions.",
    6: "We synthesize the Fixed Points I--V results without promoting their control parameter, projections or diagnostics into an unproved fundamental field theory. The analytic chain includes projected fixed-point existence, strict-Lyapunov equilibrium promotion, disturbance floors, curved spectral-cluster persistence and leakage, intrinsic first-order centroid modulation, frozen linear covariance and declared admissibility exits. Earlier results are stated as self-contained input-output contracts with their canonical sources, rather than duplicated theorem blocks. We distinguish inherited results, conditional model completions and physical interpretations. The two local causality propositions explain why an instantaneous bilocal interaction lacks the usual domain of dependence and how a hyperbolic local mediator supplies a causal retarded completion. The synthesis depends only on earlier Fixed Points installments and standard mathematical literature, not on later MTT research results.",
}


def main():
    review_path = ROOT / "catalog/expository-review-decisions.json"
    reviews = json.loads(review_path.read_text(encoding="utf-8-sig"))
    for number, version in VERSIONS.items():
        directory = ROOT / "papers" / FP_ORDER[number - 1]
        path = directory / "metadata.json"
        meta = json.loads(path.read_text(encoding="utf-8-sig"))
        assert meta["current_version"] in {f"v{version - 1}", f"v{version}"}, "unexpected concurrent version"
        meta["current_version"] = f"v{version}"
        meta["date"] = f"September 2026 Version {version}"
        meta["release_state"] = "current_revised_tex"
        meta["version_relation"] = "current_source_newer_than_release"
        if number in ABSTRACTS:
            meta["abstract"] = ABSTRACTS[number]
        path.write_text(json.dumps(meta, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
        audit = directory / "REVISION_AUDIT.md"
        marker = f"## Foundational dependency repair: version {version} (2026-09-12)"
        text = audit.read_text(encoding="utf-8-sig")
        if marker not in text:
            text += (f"\n{marker}\n\n{DELTAS[number]}\n\n"
                     "Only local arguments, earlier numbered FP installments and standard mathematics are proof sources. "
                     "Prior revision and validation entries above are historical, not current application-status assertions. "
                     "Original Zenodo release metadata is preserved; this is an unreleased authoring revision. "
                     "See FP_FOUNDATIONAL_DEPENDENCY_REPAIR_2026-09-12.md for the full review and verification record.\n")
            audit.write_text(text, encoding="utf-8")
        print(f"FP {number}: v{version}; release metadata retained")
        decision = reviews["papers"][FP_ORDER[number - 1]]
        decision["reviewed_on"] = "2026-09-12"
        decision["release_authorized"] = False
    review_path.write_text(json.dumps(reviews, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
