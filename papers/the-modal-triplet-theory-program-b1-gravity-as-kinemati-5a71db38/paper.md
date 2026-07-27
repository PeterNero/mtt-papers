---
abstract: |
  We determine exactly what follows from circle-type return memory in a typed encoding atlas. A composable family of invertible comparison maps defines a transport functor and a holonomy group. A carrier value descends to a path-independent global value precisely when it is fixed by that holonomy group. Nontrivial holonomy therefore need not be an inconsistency: one may retain the transport data, restrict to the fixed sector, or pass to a declared quotient. It obstructs only an endpoint-only trivialization. Under standard smoothness and locality hypotheses, transport on a supplied principal bundle is represented by a connection, but the circle profile alone selects neither the bundle, structure group, representation, nor connection. Flat connections can have nontrivial global holonomy, so return memory does not imply curvature.

  Gravity is a canonical realization only after additional physical data are supplied: a smooth base, a Lorentzian metric or equivalent physical principal symbol, and the tangent, frame, coframe, or spin carrier. The metric then has a unique torsion-free compatible Levi–Civita connection. Causal cones come from the principal symbol of a selected local hyperbolic equation, and Einstein dynamics follows only after an Einstein–Hilbert or equivalent local action is selected. Thus Program B1 establishes a precise loop-transport bridge and a conditional gravity realization, not the inevitability or uniqueness of gravity from obstruction taxonomy alone.
author:
- Peter Nero
current_version: v2
date: July 2026
generated_from_main_tex_sha256: b8c33c9d49d333c32693bf87e583adf8418d6e627c7ecf533ed7c3566354d81c
paper_id: the-modal-triplet-theory-program-b1-gravity-as-kinemati-5a71db38
release_state: zenodo_released
released_version: v1.0
title: |
  The Modal Triplet Theory Program B1:  
  Loop-Transport Consistency and the Conditional Gravity Realization
zenodo_doi: 10.5281/zenodo.18355020
zenodo_record_id: 18355020
zenodo_url: "https://zenodo.org/records/18355020"
---

# Revision note for version 2

<div class="description">

Version 1 of Program B1.

The first version identified every circle obstruction with a unique gravity encoding, treated nontrivial holonomy as curvature, and promoted encoding-level path dependence to causal cones, horizons, and gravitational dynamics without a physical metric, principal symbol, or action.

Version 2 replaces those claims by a transport-groupoid theorem, a holonomy-fixed descent criterion, an endpoint-trivialization obstruction, and a conditional connection realization. It separates loop transport, Lorentzian causal geometry, and Einstein dynamics.

Loop-dependent comparison requires explicit bookkeeping; smooth connections are natural realizations of such bookkeeping; and a common frame connection can act on every associated carrier in a declared gravitational model.

No theorem here selects the physical base, Lorentzian metric, frame carrier, Einstein–Hilbert action, Newton constant, cosmological constant, matter stress tensor, or a unique gravity theory from the circle profile.

</div>

# Scope and Imported Data

Program A0 supplies typed reductions, autonomous descent, recovery, admissible domains, and exact re-encoding criteria . Program A1 supplies encoding-level trajectories and proves that physical motion and causality require a separate local hyperbolic bridge . Program B0 defines a *circle profile* as nontrivial return transport around a composable loop; it also proves that such return transport may be flat and one-dimensional .

This paper addresses the next typed question:

> What additional structure is required to compare carrier values consistently when admissible continuation has nontrivial return transport, and under which extra hypotheses may that structure be interpreted as gravity?

Four levels must remain separate:

1.  *encoding transport*: comparison of local carrier values;

2.  *smooth geometric realization*: a bundle and connection;

3.  *physical causal geometry*: a local hyperbolic equation and its principal symbol;

4.  *gravitational dynamics*: a selected action or field equation.

An implication within one level does not supply the data required by the next level.

The word “gravity” will therefore be used only for a declared tangent, frame, coframe, spin, or metric-affine realization. An internal $`U(1)`$ connection, a Berry connection, and a spacetime frame connection can all carry holonomy, but they are not the same physical object.

# Typed Loop Transport

## Transport groupoid

<div id="def:transport" class="definition">

**Definition 1** (Typed transport system). Let $`\mathcal P`$ be a connected groupoid whose objects are admissible carrier locations $`x`$ and whose arrows are declared composable continuation paths. For every object let $`E_x`$ be a carrier. A *typed transport system* is a functor
``` math
T:\mathcal P\longrightarrow \mathsf{Iso},
```
where $`T_\gamma:E_x\to E_y`$ is an isomorphism for every arrow $`\gamma:x\to y`$, and
``` math
T_{\operatorname{id}_x}=\operatorname{id}_{E_x},\qquad
 T_{\gamma_2\circ\gamma_1}=T_{\gamma_2}T_{\gamma_1},\qquad
 T_{\gamma^{-1}}=T_\gamma^{-1}.
```

</div>

The groupoid may be the path groupoid of a smooth base, the groupoid generated by a chart-overlap nerve, or a finite transition groupoid. These cases must not be conflated. In particular, an overlap chain becomes a physical path only after a bridge identifying its arrows with physical transport.

<div id="def:holonomy" class="definition">

**Definition 2** (Holonomy group and circle profile). Fix an object $`x_0`$. The holonomy group of $`T`$ at $`x_0`$ is
``` math
\operatorname{Hol}_{x_0}(T)
 :=\{T_\gamma:\gamma:x_0\to x_0\}.
```
The transport system has a circle profile at $`x_0`$ when this group contains an element other than the identity, modulo the declared equivalence of carrier representatives.

</div>

This definition records return memory. It does not yet say that the return map is erroneous, that it must be cancelled, or that it is gravitational.

## The exact descent criterion

<div class="definition">

**Definition 3** (Parallel global value). A *parallel global value* for $`T`$ is a family $`s=(s_x)`$ with $`s_x\in E_x`$ such that
``` math
T_\gamma s_x=s_y
```
for every declared arrow $`\gamma:x\to y`$.

</div>

<div id="thm:fixed-descent" class="theorem">

**Theorem 4** (Holonomy-fixed descent). *Fix $`x_0`$ and $`v\in E_{x_0}`$. A parallel global value satisfying $`s_{x_0}=v`$ exists if and only if
``` math
h v=v\qquad\text{for every }h\in\operatorname{Hol}_{x_0}(T).
```
When it exists, it is unique.*

</div>

<div class="proof">

*Proof.* If $`s`$ is parallel and $`\gamma`$ is a loop at $`x_0`$, then $`T_\gamma v=T_\gamma s_{x_0}=s_{x_0}=v`$.

Conversely, choose for every $`y`$ an arrow $`\gamma_y:x_0\to y`$ and define $`s_y=T_{\gamma_y}v`$. If $`\gamma_y'`$ is another such arrow, then $`(\gamma_y')^{-1}\circ\gamma_y`$ is a loop at $`x_0`$. The fixed-point hypothesis gives
``` math
T_{\gamma_y}v
 =T_{\gamma_y'}T_{(\gamma_y')^{-1}\circ\gamma_y}v
 =T_{\gamma_y'}v.
```
Thus $`s_y`$ is path independent. Functoriality proves $`T_\eta s_y=s_z`$ for every $`\eta:y\to z`$. Connectedness and the fixed value at $`x_0`$ give uniqueness. ◻

</div>

<div id="cor:not-inconsistent" class="corollary">

**Corollary 5** (Nontrivial holonomy is not automatically inconsistency). *A transport system with nontrivial holonomy may still possess nonzero parallel global values. The descending sector at $`x_0`$ is exactly
``` math
E_{x_0}^{\operatorname{Hol}}
 :=\{v\in E_{x_0}:hv=v\text{ for all }h\in\operatorname{Hol}_{x_0}(T)\}.
```*

</div>

Accordingly, a circle profile admits several lawful responses:

- retain the path and transport data;

- restrict to the holonomy-fixed sector;

- pass to a declared orbit, coinvariant, or quotient carrier, provided the relevant maps descend; or

- seek a trivialization, if the holonomy permits one.

None of these choices is selected by the word “circle” alone.

## What compensation can and cannot do

The first version spoke of a compensator that erased path dependence. The following result identifies the exact obstruction.

<div id="thm:trivialization" class="theorem">

**Theorem 6** (Endpoint-only trivialization criterion). *Suppose all carriers are isomorphic to one model carrier $`V`$. There exist isomorphisms $`q_x:E_x\to V`$ satisfying
``` math
q_yT_\gamma=q_x
 \qquad\text{for every }\gamma:x\to y
```
if and only if $`\operatorname{Hol}_{x_0}(T)`$ is trivial.*

</div>

<div class="proof">

*Proof.* If such $`q_x`$ exist and $`\gamma`$ is a loop at $`x_0`$, then $`q_{x_0}T_\gamma=q_{x_0}`$, hence $`T_\gamma=\operatorname{id}`$.

Conversely, assume the holonomy is trivial. Choose one isomorphism $`q_{x_0}:E_{x_0}\to V`$ and an arrow $`\gamma_x:x_0\to x`$ for every $`x`$. Set $`q_x=q_{x_0}T_{\gamma_x}^{-1}`$. Trivial holonomy makes this independent of the chosen arrow, and the displayed compatibility follows by functoriality. ◻

</div>

A path-dependent inverse $`T_\gamma^{-1}`$ always reverses a known transport, but it retains the entire path label and does not furnish the endpoint-only trivialization in Theorem <a href="#thm:trivialization" data-reference-type="ref" data-reference="thm:trivialization">6</a>. Additional bookkeeping can therefore *represent* nontrivial holonomy without erasing it.

# Smooth Bundle and Connection Realizations

## From overlap data to a bundle

Let $`Y`$ be a supplied smooth manifold, let $`\{U_\alpha\}`$ be an open cover, and let $`G`$ be a supplied Lie group. Smooth transition functions
``` math
g_{\beta\alpha}:U_\alpha\cap U_\beta\longrightarrow G
```
define a principal $`G`$-bundle when
``` math
g_{\alpha\alpha}=e,\qquad
 g_{\alpha\beta}=g_{\beta\alpha}^{-1},\qquad
 g_{\gamma\beta}g_{\beta\alpha}=g_{\gamma\alpha}
```
on the relevant overlaps. This is a bundle-descent theorem, not a selection of $`G`$, $`Y`$, or a physical interpretation.

<div id="prop:bundle-section" class="proposition">

**Proposition 7** (Bundle consistency versus parallel-section consistency). *A nontrivial principal bundle can satisfy its transition cocycle exactly even when a chosen associated carrier has no nonzero global parallel section. Bundle consistency is therefore weaker than trivial holonomy and different from the state-level descent condition of Theorem <a href="#thm:fixed-descent" data-reference-type="ref" data-reference="thm:fixed-descent">4</a>.*

</div>

<div class="proof">

*Proof.* The cocycle equations glue the local products $`U_\alpha\times G`$ into a principal bundle. A parallel section in an associated bundle additionally requires its base value to be fixed by the connection holonomy. The latter condition can fail while the bundle cocycle remains exact. ◻

</div>

## Connections represent smooth local transport

<div class="definition">

**Definition 8** (Smooth local parallel transport). On a supplied principal $`G`$-bundle $`P\to Y`$, a smooth local parallel-transport system assigns a $`G`$-equivariant map between endpoint fibers to each piecewise-smooth path, respects identity, reversal, and concatenation, depends smoothly on smooth path families, and is invariant under orientation-preserving reparametrization and thin homotopy.

</div>

<div id="thm:connection-transport" class="theorem">

**Theorem 9** (Connection–transport correspondence). *On a fixed smooth principal bundle $`P\to Y`$, principal connections are in one-to-one correspondence with smooth local parallel-transport systems in the preceding sense.*

</div>

<div class="proof">

*Proof sketch.* A connection supplies horizontal lifts; their endpoints define parallel transport with the listed properties. Conversely, the derivative of transport along infinitesimal path germs defines the horizontal subspace at each point of $`P`$. Smoothness, thin-homotopy locality, composition, and $`G`$-equivariance give a smooth principal connection. The two constructions are inverse. This is the standard reconstruction of a connection from parallel transport . ◻

</div>

The locality and thin-homotopy clauses matter. An arbitrary assignment to finite chart loops need not come from a smooth connection.

<div id="prop:no-unique-connection" class="proposition">

**Proposition 10** (No unique connection from a circle profile). *A circle profile does not determine a unique smooth geometric realization. It does not select $`Y`$, $`G`$, $`P`$, a representation, or a connection. Even after $`P`$ is fixed, its connections form an affine space modeled on
``` math
\Omega^1(Y,\operatorname{Ad}P).
```*

</div>

<div class="proof">

*Proof.* If $`\omega`$ is one principal connection and $`a\in\Omega^1(Y,\operatorname{Ad}P)`$, then $`\omega+a`$ is another principal connection. Moreover, internal line bundles, frame bundles, and flat local systems provide inequivalent realization categories with nontrivial return transport. The coarse predicate “some return map is nonidentity” contains none of the data needed to choose among them. ◻

</div>

# Holonomy Is Not Curvature

Let $`S^1=\mathbb R/2\pi\mathbb Z`$ with angular coordinate $`\theta`$. On the trivial complex line consider
``` math
\nabla=d+ia\,d\theta,\qquad a\in\mathbb R\setminus\mathbb Z.
```
Its curvature is
``` math
F_\nabla=d(ia\,d\theta)=0,
```
while its holonomy around the positive generator is
``` math
\operatorname{Hol}_\nabla(S^1)=\exp(-2\pi ia)\ne1.
```

<div id="thm:flat-holonomy" class="theorem">

**Theorem 11** (Local curvature and global return memory). *Curvature controls infinitesimal and restricted holonomy. On a simply connected contractible domain, a flat connection is gauge-equivalent to a trivial connection and its parallel transport is path independent. On a non-simply-connected domain, a flat connection may retain a nontrivial monodromy representation
``` math
\pi_1(Y,x_0)\longrightarrow G.
```
Consequently a global circle profile does not imply nonzero curvature.*

</div>

<div class="proof">

*Proof.* The local statement is the standard flat-connection trivialization on a contractible domain. Global flat transport factors through the fundamental group, as the displayed $`S^1`$ example shows. The relation between curvature and the restricted holonomy group is formalized by the Ambrose–Singer theorem . ◻

</div>

This corrects the biconditional “curvature vanishes if and only if no circle obstruction.” It is valid only after “circle” is restricted to contractible infinitesimal loops in a fixed smooth connection realization.

# The Conditional Gravity Realization

## The additional physical data

<div id="ass:gravity" class="assumption">

**Assumption 12** (Gravitational carrier). For the remainder of this section, supply:

1.  a smooth $`d`$-dimensional base $`Y`$;

2.  a Lorentzian metric $`g`$ or an equivalent selected metric principal symbol;

3.  the tangent, frame, coframe, or spin carrier over $`Y`$; and

4.  a declaration that the relevant transport acts on that carrier.

</div>

These data do not follow from Definition <a href="#def:holonomy" data-reference-type="ref" data-reference="def:holonomy">2</a>. In the canonical MTT physical realization one takes $`d=4`$, but neither $`d=4`$ nor Lorentzian signature is selected by B1.

<div id="thm:levi-civita" class="theorem">

**Theorem 13** (Canonical Levi–Civita realization). *Under Assumption <a href="#ass:gravity" data-reference-type="ref" data-reference="ass:gravity">12</a>, there is a unique affine connection $`\nabla^g`$ on $`TY`$ satisfying
``` math
\nabla^g g=0,\qquad
 \operatorname{Tor}(\nabla^g)=0.
```
In a coordinate chart its coefficients are
``` math
\Gamma^\rho_{\mu\nu}
 =\frac12 g^{\rho\sigma}
 \left(
 \partial_\mu g_{\sigma\nu}
 +\partial_\nu g_{\sigma\mu}
 -\partial_\sigma g_{\mu\nu}
 \right).
```
Its return transport is a genuine gravitational holonomy realization.*

</div>

<div class="proof">

*Proof.* This is the fundamental theorem of pseudo-Riemannian geometry . The final sentence is a typing statement: because the connection acts on the tangent or orthonormal-frame carrier, its holonomy is gravitational in the declared model. ◻

</div>

The word “canonical” is conditional on the metric, tangent carrier, torsion-free condition, and metric compatibility. Relaxing these assumptions admits metric-affine, Einstein–Cartan, and teleparallel realizations. Thus Levi–Civita uniqueness does not imply that the circle profile uniquely selects general relativity.

## Common-carrier coupling

<div id="prop:associated" class="proposition">

**Proposition 14** (Associated-bundle universality). *Let $`P\to Y`$ be one principal $`G`$-bundle with connection $`\omega`$, and let $`E_i=P\times_{\rho_i}V_i`$ be associated bundles. Then every $`E_i`$ inherits a covariant derivative
``` math
\nabla^{(i)}=d+\rho_{i*}(\omega)
```
from the same $`\omega`$. Parallel transport on every associated carrier is therefore functorially linked to the common principal transport.*

</div>

<div class="proof">

*Proof.* The connection defines a horizontal distribution on $`P`$. Passing through each representation $`\rho_i`$ gives the displayed associated covariant derivative and compatible parallel transport. ◻

</div>

This proposition explains a precise sense in which a declared common frame or spin connection acts on all associated sectors. It does not derive the equivalence principle, the matter action, equality of inertial and gravitational mass, or a universal numerical coupling from a circle profile.

# Causal Geometry Comes from a Principal Symbol

## Local physical equations

Let $`E\to(Y,g)`$ be a vector bundle with connection $`\nabla`$. A normally hyperbolic operator has the local form
``` math
L
 =-g^{\mu\nu}\nabla_\mu\nabla_\nu
 +A^\mu\nabla_\mu+B.
```
Its principal symbol is
``` math
\sigma_{\rm pr}(L)(x,\xi)
 =g^{\mu\nu}(x)\xi_\mu\xi_\nu\,\operatorname{id}_{E_x},
```
up to the chosen overall sign convention.

<div id="thm:principal" class="theorem">

**Theorem 15** (Connection data do not select the causal cone). *For the operator above, the characteristic covectors are determined by
``` math
g^{\mu\nu}\xi_\mu\xi_\nu=0.
```
The connection coefficients, holonomy, $`A^\mu`$, and $`B`$ contribute only lower-order terms and do not determine this principal cone.*

</div>

<div class="proof">

*Proof.* In a local trivialization, $`\nabla_\mu=\partial_\mu+\omega_\mu`$. Expanding $`g^{\mu\nu}\nabla_\mu\nabla_\nu`$ shows that only $`g^{\mu\nu}\partial_\mu\partial_\nu`$ contains two derivatives of the unknown section. Every term containing $`\omega_\mu`$, its derivative, $`A^\mu`$, or $`B`$ has differential order at most one. ◻

</div>

Thus loop bookkeeping cannot by itself stabilize a causal cone. The cone must already be present in a selected local physical equation or be selected by a separate principal-symbol theorem.

## Coherent principal-symbol descent

<div id="thm:compression" class="theorem">

**Theorem 16** (Conditional coherent-cone descent). *Let $`P_x:E_x\to E_x`$ be a smooth fiberwise projector and assume:*

1.  *$`L`$ is local and normally hyperbolic with scalar internal principal coefficient as above;*

2.  *the compressed operator $`PLP`$ is considered on $`\mathrm{Ran}P`$; and*

3.  *no nonlocal projection or additional mixed highest-order term is introduced.*

*Then
``` math
\sigma_{\rm pr}(PLP)(x,\xi)\big|_{\mathrm{Ran}P_x}
 =g^{\mu\nu}(x)\xi_\mu\xi_\nu\,
 \operatorname{id}_{\mathrm{Ran}P_x}.
```
The coherent sector inherits the supplied causal cone.*

</div>

<div class="proof">

*Proof.* The two-derivative term in $`L(Pu)`$ is $`-g^{\mu\nu}P\,\partial_\mu\partial_\nu u`$; derivatives of $`P`$ have order at most one in $`u`$. Applying the outer $`P`$ and restricting to $`\mathrm{Ran}P`$ gives $`P^2=P`$, hence the displayed symbol. This is the corrected fixed-point principal-symbol descent used by Program A1 and the signature-stability paper . ◻

</div>

The theorem proves preservation, not emergence, of Lorentzian geometry. Spatially nonlocal kernels may leave a formal differential symbol unchanged while violating local domain of dependence; a causal physical completion must therefore use a local parent action or a separately controlled retarded operator .

## Three different boundaries

The following notions are not interchangeable:

Encoding boundary.  
The boundary of a declared admissible chart or decoder domain.

Characteristic boundary.  
A hypersurface characteristic for the principal symbol of a local physical equation.

Gravitational horizon.  
A global causal boundary in a specified spacetime solution, such as an event, Cauchy, trapping, or Killing horizon, with its own hypotheses.

An encoding boundary may correspond to a physical horizon only after an explicit bridge proves that the encoding loss tracks the relevant causal boundary. Loop transport alone supplies no such bridge.

# Einstein Dynamics Requires a Local Action

## Conditional Einstein realization

Assume a four-dimensional Lorentzian base for illustration and supply the local action
``` math
S[g,\psi]
 =\frac{1}{2\kappa}
   \int_Y (R(g)-2\Lambda)\,d\operatorname{vol}_g
 +S_{\rm m}[g,\psi]
 +S_{\partial},
```
where $`S_{\partial}`$ is the boundary term required by the chosen variational problem. Define
``` math
T_{\mu\nu}
 :=-\frac{2}{\sqrt{|g|}}
 \frac{\delta S_{\rm m}}{\delta g^{\mu\nu}}.
```

<div id="thm:einstein" class="theorem">

**Theorem 17** (Action-to-Einstein bridge). *If the fields and boundary conditions make the displayed action differentiable, stationarity under compactly supported metric variations gives
``` math
G_{\mu\nu}+\Lambda g_{\mu\nu}
 =\kappa T_{\mu\nu}.
```*

</div>

<div class="proof">

*Proof.* The first variation of the Einstein–Hilbert term is
``` math
\delta S_{\rm EH}
 =\frac{1}{2\kappa}\int_Y
 (G_{\mu\nu}+\Lambda g_{\mu\nu})
 \,\delta g^{\mu\nu}\,d\operatorname{vol}_g
```
after the selected boundary contribution is cancelled. The definition of $`T_{\mu\nu}`$ gives
``` math
\delta S_{\rm m}
 =-\frac12\int_Y T_{\mu\nu}\,
 \delta g^{\mu\nu}\,d\operatorname{vol}_g.
```
Arbitrariness of the interior variation yields the equation. ◻

</div>

This theorem is intentionally conditional. It explains how Einstein dynamics follows from a selected local action; it does not derive that action from the circle profile.

## Structural underdetermination

<div id="thm:no-einstein" class="theorem">

**Theorem 18** (No Einstein equation from obstruction taxonomy alone). *Typed loop-transport data and its circle profile do not determine a unique metric action or field equation.*

</div>

<div class="proof">

*Proof.* First, the flat $`U(1)`$ example of Theorem <a href="#thm:flat-holonomy" data-reference-type="ref" data-reference="thm:flat-holonomy">11</a> has nontrivial circle-profile holonomy but no spacetime metric dynamics. Second, even after a Lorentzian metric and its frame connection are supplied, the same structural atlas can be paired with distinct local actions, for example
``` math
S_\lambda
 =S_{\rm EH}
 +\lambda\int_Y R(g)^2\,d\operatorname{vol}_g.
```
For $`\lambda\ne0`$ the metric Euler–Lagrange equation differs from Einstein’s equation, while the coarse statement that the transport has a nonidentity return map is unchanged. Hence the obstruction predicate cannot determine the action. ◻

</div>

Known metric uniqueness results also import substantial hypotheses. In four dimensions, a Lovelock-type argument restricts second-order, local, diffeomorphism-covariant metric equations under its stated assumptions; those assumptions and the four-dimensional base are not consequences of CLN .

# Consequences for the MTT Program

## What survives from version 1

The following claims remain useful:

- nontrivial return transport requires explicit comparison data if path labels matter;

- the holonomy-fixed sector is the exact domain on which transported values descend globally;

- smooth local transport on a supplied bundle is represented by a connection;

- a common principal connection induces compatible transport on all associated carriers; and

- after the frame carrier and Lorentzian metric are supplied, the Levi–Civita connection is canonical.

## Claims withdrawn or moved downstream

The following do not follow at the B1 tier:

- every circle profile is gravitational;

- gravity is the unique response to every loop obstruction;

- nontrivial holonomy implies nonzero curvature;

- chart-order path dependence selects a Lorentzian metric or causal cone;

- encoding boundaries are automatically physical horizons;

- a connection determines the Einstein–Hilbert action; or

- the obstruction taxonomy implies Einstein’s equation.

Gauge connections and gravitational connections may both instantiate the transport formalism. Their physical distinction comes from the carrier, structure group, representation, action, and observable map. A later unified theory must preserve those types rather than identify the sectors merely because both use connections.

## Relation to the shared circle and q79 geometry

A common $`U(1)`$ line may carry phase or flat holonomy through several internal sectors. It is counted once and is not identified with noncompact physical time. Likewise, the selected q79 internal geometry can provide vertical bundles and operators only after a same-source bridge specifies how its connection data relates to the physical frame/spin connection. Internal HYM curvature does not by itself select the base Lorentzian metric or Einstein dynamics.

# Scoped B1 Theorem

<div id="thm:scoped" class="theorem">

**Theorem 19** (Loop consistency with conditional gravity realization). *For the typed data declared in this paper:*

1.  *a composable comparison system is a transport functor;*

2.  *its path-independent global values are exactly the holonomy-fixed values;*

3.  *an endpoint-only trivialization exists exactly when the holonomy is trivial;*

4.  *on a supplied smooth principal bundle, smooth local transport is equivalent to a connection;*

5.  *circle-profile data alone does not select the bundle, connection, curvature, metric, dimension, causal cone, or action;*

6.  *after a Lorentzian metric and tangent/frame carrier are supplied, the torsion-free metric-compatible connection is uniquely Levi–Civita;*

7.  *a local normally hyperbolic principal symbol supplies the causal cone, which descends through a smooth fiberwise coherent projector under Theorem <a href="#thm:compression" data-reference-type="ref" data-reference="thm:compression">16</a>; and*

8.  *Einstein’s equation follows from the selected local Einstein–Hilbert–matter action under Theorem <a href="#thm:einstein" data-reference-type="ref" data-reference="thm:einstein">17</a>, not from the obstruction taxonomy.*

</div>

<div class="proof">

*Proof.* Items 1–3 are Definitions <a href="#def:transport" data-reference-type="ref" data-reference="def:transport">1</a>–<a href="#def:holonomy" data-reference-type="ref" data-reference="def:holonomy">2</a> and Theorems <a href="#thm:fixed-descent" data-reference-type="ref" data-reference="thm:fixed-descent">4</a> and <a href="#thm:trivialization" data-reference-type="ref" data-reference="thm:trivialization">6</a>. Item 4 is Theorem <a href="#thm:connection-transport" data-reference-type="ref" data-reference="thm:connection-transport">9</a>. Item 5 follows from Proposition <a href="#prop:no-unique-connection" data-reference-type="ref" data-reference="prop:no-unique-connection">10</a>, Theorem <a href="#thm:flat-holonomy" data-reference-type="ref" data-reference="thm:flat-holonomy">11</a>, and Theorem <a href="#thm:no-einstein" data-reference-type="ref" data-reference="thm:no-einstein">18</a>. Item 6 is Theorem <a href="#thm:levi-civita" data-reference-type="ref" data-reference="thm:levi-civita">13</a>. Item 7 is Theorems <a href="#thm:principal" data-reference-type="ref" data-reference="thm:principal">15</a> and <a href="#thm:compression" data-reference-type="ref" data-reference="thm:compression">16</a>. Item 8 is Theorem <a href="#thm:einstein" data-reference-type="ref" data-reference="thm:einstein">17</a>. ◻

</div>

# Version Delta and Research Frontier

Relative to version 1, this revision:

- replaces “gravity is necessary and unique” by an exact holonomy-fixed descent theorem and a conditional gravity realization;

- distinguishes a consistent nontrivial bundle from a globally parallel carrier value;

- proves the exact criterion for endpoint-only compensation;

- separates flat global holonomy from local curvature;

- makes the structure group, bundle, representation, connection, metric, and dimension explicit inputs;

- identifies Levi–Civita uniqueness only after the Lorentzian metric and torsion-free metric-compatible category are fixed;

- moves causal cones to the principal symbol of a selected local physical equation;

- distinguishes encoding boundaries from physical horizons; and

- derives Einstein’s equation only from a declared local action.

The next frontier is a source theorem, not another reclassification. A full MTT gravity bridge must construct, from one selected upper source:

1.  the physical base and Lorentzian principal symbol;

2.  the frame or spin carrier and its connection;

3.  a local action with normalization and matter coupling;

4.  a commuting map from the upper transport/Hessian data to those physical objects; and

5.  a verifier showing that the descended equations, causal propagators, and observables match the declared gravity tier.

Until those data are supplied, B1 is a rigorous conditional reconstruction contract rather than a derivation of general relativity.

# Conclusion

Circle-type return memory has a clean mathematical meaning: it is holonomy of a typed transport system. Its exact state-level consequence is equally clean: only holonomy-fixed values descend path independently. Smooth connections are natural realizations, but they are not selected uniquely, and flat connections already show why holonomy cannot be identified with curvature.

Gravity enters when the transport acts on a physical tangent, frame, coframe, or spin carrier equipped with a supplied Lorentzian metric. The Levi–Civita connection is then canonical under its familiar hypotheses. Causal structure still comes from a local principal symbol, and Einstein dynamics still comes from an action. This separation preserves the strongest part of the original idea–gravity as common geometric transport–while removing claims that the obstruction taxonomy alone cannot prove.

<div class="thebibliography">

99

P. Nero, *The Modal Triplet Theory Program A0: A Structural Theory of Reduced Description*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program A1: Coherent Kinematics*, revised v2, 2026.

P. Nero, *The Modal Triplet Theory Program B0: Circle–Lens–Nil as an Obstruction Taxonomy and Its Minimal Curvature Realizations*, revised v2, 2026.

P. Nero, *Fixed Points VI: Formal Synthesis and Physical Interpretations*, revised v5, 2026.

P. Nero, *Lorentzian Base Compatibility and Signature Stability in the MTT Fixed-Point Realization*, revised v2, 2026.

S. Kobayashi and K. Nomizu, *Foundations of Differential Geometry*, volume I, Wiley, 1963.

U. Schreiber and K. Waldorf, “Parallel transport and functors,” *Journal of Homotopy and Related Structures* 4 (2009), 187–244.

B. O’Neill, *Semi-Riemannian Geometry with Applications to Relativity*, Academic Press, 1983.

R. M. Wald, *General Relativity*, University of Chicago Press, 1984.

D. Lovelock, “The Einstein tensor and its generalizations,” *Journal of Mathematical Physics* 12 (1971), 498–501.

</div>
