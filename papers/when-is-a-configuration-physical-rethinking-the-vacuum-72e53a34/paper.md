---
abstract: |
  Despite decades of progress in quantum gravity, string theory, cosmology, and effective field theory, no consensus has emerged on how to select a unique or sharply constrained vacuum describing observed physics. This persistent difficulty is commonly framed as a problem of combinatorics, statistics, or anthropic weighting over a large landscape of vacua. In this work we argue that the difficulty may instead reflect a mis-posed question: the assumption that physics is defined throughout configuration space. We observe that core physical notions—Hilbert spaces, probability, effective field theory, and renormalization group flow—already presuppose stability, boundedness, and spectral separation, none of which are guaranteed globally. As a consequence, selection cannot meaningfully act pointwise on vacua but must instead operate on admissible regions defined by dynamical and spectral inequalities. These regions need not be connected or accessible by continuous deformation, rendering standard landscape searches ineffective by construction. The goal of this paper is not to propose a new fundamental theory, but to clarify the conceptual structure underlying vacuum selection and to explain why existing approaches have struggled to converge.
author:
- Peter Nero
current_version: v1.0
date: January, 2026
generated_from_main_tex_sha256: 8bd1d842881d1cf59f64b4333159bd3ba8318667d783ffd1cc650ba1a0138b68
paper_id: when-is-a-configuration-physical-rethinking-the-vacuum-72e53a34
release_state: zenodo_released
released_version: v1.0
title: |
  When Is a Configuration Physical?  
  Rethinking the Vacuum Selection Problem
zenodo_doi: 10.5281/zenodo.18255208
zenodo_record_id: 18255208
zenodo_url: "https://zenodo.org/records/18255208"
---

# Introduction

The problem of vacuum selection has remained unresolved across multiple approaches to fundamental physics. In string theory, the existence of a vast space of formally consistent backgrounds has led to the notion of a “landscape” of vacua, with selection often deferred to statistical, cosmological, or anthropic arguments. Related difficulties appear in other frameworks: renormalization group flows depend on truncations whose domains of validity are not always controlled; cosmological measures presuppose probabilities in regimes where observers and effective descriptions may not exist; and effective field theory arguments are frequently extrapolated beyond the conditions under which they are known to apply. Despite substantial technical progress, no consensus has emerged on how a unique or even sharply constrained physical vacuum should be identified.

A common feature of these approaches is an implicit assumption that physics is defined throughout configuration space. That assumption is rarely stated explicitly, yet it underlies much of the standard reasoning: vacua are compared pointwise, probabilities are assigned globally, and flows are assumed to exist between nearby configurations. However, core physical structures—Hilbert spaces, probability measures, effective field theories, and renormalization group trajectories—are themselves conditional. They presuppose stability, boundedness, and spectral separation, none of which are guaranteed *a priori*. When these conditions fail, the usual language of physics ceases to apply.

In this work we argue that the persistent difficulty of vacuum selection may reflect a mis-posed question. Rather than selecting individual vacua within a landscape, one should first ask where physics is well defined at all. We suggest that selection, if it exists, must operate on admissible regions of configuration space characterized by dynamical and spectral inequalities, not on isolated points. Such regions need not be connected, nor accessible by continuous deformation, and may be invisible to standard scanning or perturbative methods. From this perspective, the absence of convergence in landscape-based approaches is not surprising but expected.

# The Implicit Assumption Behind Landscape Reasoning

Landscape-based reasoning presupposes that configuration space is uniformly physical: that for every formally consistent background, a well-defined physical description exists. This assumption manifests in several ways. Vacua are treated as points that can be compared energetically. Measures are defined globally. Probabilities are assigned across wide classes of configurations. Renormalization group flows are assumed to interpolate between nearby descriptions.

None of these operations is innocent. Each relies on the existence of a stable physical structure supporting observables, probabilities, and controlled approximations. Formal consistency—such as anomaly cancellation or the existence of classical equations of motion—is not sufficient to guarantee this structure. A configuration may satisfy algebraic or geometric constraints and yet fail to support a meaningful physical description.

The assumption that physics is defined everywhere is therefore not a neutral starting point but a strong hypothesis. If it fails, then the entire framing of vacuum selection as a problem of choosing among vacua must be reconsidered.

# Physical Structures Are Conditional, Not Automatic

Core elements of physical reasoning are conditional constructions. A Hilbert space description requires control over operator domains, norms, and spectral properties. Probability theory requires stable measures and expectation values. Effective field theory depends on the existence of a separation of scales allowing truncation with controlled error. Renormalization group flow presupposes that effective descriptions exist along the trajectory and that singularities or instabilities are not encountered prematurely.

These conditions are not guaranteed globally. When spectral gaps close, when operators become unbounded, or when small perturbations lead to uncontrolled growth, the usual physical structures fail. In such regimes, it is not merely that the physics is unfamiliar; rather, the basic language of states, observables, and probabilities ceases to be well defined. By “ceases to apply” we mean that standard operational structures (e.g. Hilbert-space states, controlled observables, and probability measures) are not well-defined, not that one cannot write down formal mathematical data outside the admissible domain.

Crucially, the conditions under which physical structure exists are expressed as inequalities rather than equalities. They bound growth, spectra, and fluctuations rather than fixing precise parameter values. As a result, the domain of physics is generically a subset of configuration space defined by stability constraints, not the full space of formally consistent configurations.

This observation already suggests that the image of a landscape populated everywhere by physical vacua is misleading. Many formally allowed configurations may simply lie outside the domain where physics can be formulated at all.

# Why Selection Cannot Be Pointwise

If physical structure exists only where stability and boundedness conditions are satisfied, then selection cannot meaningfully operate on individual points in configuration space. Pointwise selection presumes that nearby configurations are physically comparable, that observables vary smoothly under deformation, and that probabilities can be assigned globally. None of these assumptions holds once admissibility conditions are taken seriously.

Selection governed by inequalities naturally acts on extended regions rather than isolated points. In particular, inadmissibility here is stronger than dynamical instability within an already well-defined physical theory: it refers to failure of the conditions required to define the effective physical description in the first place. An admissible configuration is not characterized by exact values of moduli or couplings, but by remaining within a domain where spectral gaps persist, projections remain bounded, and effective descriptions are stable. These domains define regions of configuration space within which physics is well defined, rather than single distinguished vacua.

There is no reason for such admissible regions to be connected. They may be separated by domains in which stability conditions fail and physical descriptions break down entirely. In those intervening regions, there is no meaningful notion of renormalization group flow, effective field theory, or probabilistic measure. As a consequence, standard tools that rely on continuous deformation—moduli scanning, perturbative expansion, or statistical sampling—cannot be expected to locate or relate admissible regions reliably.

This perspective explains why decades of landscape-based searches have not converged. The absence of convergence is not evidence that the correct vacuum is extraordinarily rare within a dense landscape, but rather that the underlying assumption of a landscape populated everywhere by physical vacua is itself flawed.

# Consequences for Existing Approaches

Reframing vacuum selection as a problem of admissibility rather than pointwise choice has direct implications for several established approaches. These implications are not criticisms of particular programs, but observations about the kinds of questions those programs are structurally equipped to answer.

## String theory and formal consistency

String theory has achieved remarkable success in cataloguing large classes of mathematically consistent backgrounds. Anomalies cancel, quantum consistency conditions are satisfied, and low-energy effective descriptions can often be constructed. However, formal consistency alone does not guarantee that a background supports the full set of structures required for physics as observed—stable observables, controlled truncations, and well-defined probabilities.

From an admissibility-first perspective, the string “landscape” should be understood as a space of formally consistent configurations, only a subset of which may admit stable physical descriptions. Standard landscape reasoning implicitly assumes that physics is defined throughout this space and that vacua can be compared pointwise using energies, measures, or statistical weights. If admissibility conditions fail over large portions of configuration space, then such comparisons are ill defined from the outset. In that case, the absence of a convergent vacuum selection principle is not surprising, and the relevant question shifts from counting vacua to identifying admissible regions.

## Renormalization group approaches and asymptotic safety

Renormalization group methods, including asymptotic safety scenarios, rely on the existence of well-defined flows between ultraviolet and infrared descriptions. These flows presuppose that effective field theory remains valid along the trajectory and that truncations can be controlled. When these assumptions hold, RG techniques provide powerful insights into universality and scaling behavior.

Admissibility constraints introduce the possibility that RG flows exist only within restricted domains. If stability or boundedness conditions fail before a flow reaches the infrared, then the notion of a complete RG trajectory becomes ill defined. From this perspective, difficulties associated with truncation dependence or non-convergence may reflect not technical shortcomings but the breakdown of effective descriptions outside admissible regions.

## Cosmology and probabilistic measures

Cosmological approaches to vacuum selection often rely on probabilistic reasoning, whether through eternal inflation, multiverse measures, or ensembles of initial conditions. Such arguments presuppose that probabilities are well defined globally and that observers can be meaningfully counted across vast regions of configuration space.

If probabilistic structure itself requires admissibility—stability of observables, bounded fluctuations, and well-defined time evolution—then the assignment of probabilities outside those regimes is not justified. From this standpoint, measure problems in cosmology are not merely technical obstacles but signals that probability is being invoked beyond its domain of validity.

## Effective field theory and bottom-up reasoning

Effective field theory has proven extraordinarily successful within its domain of applicability. Its logic depends on scale separation, controlled truncation, and insensitivity to ultraviolet details. Yet these properties are not universal; they must be established rather than assumed.

An admissibility-first view emphasizes that EFT reasoning applies only where such control exists. Attempting to extrapolate EFT arguments into regions where spectral gaps close or truncations fail can produce apparent paradoxes or uncontrolled ambiguities. In this sense, failures of bottom-up reasoning to identify a unique vacuum may reflect the limits of EFT applicability rather than the absence of a fundamental selection principle.

# A Minimal Admissibility-First Framework

The preceding analysis motivates a minimal, theory-agnostic reformulation of vacuum selection in which admissibility precedes choice. The purpose of this section is not to propose a new fundamental theory, but to isolate the structural ingredients required for physics to be well defined.

## Admissibility as a prerequisite

We define an admissible region of configuration space as a domain in which the basic structures required for physical description exist and remain stable. These structures include well-defined observables with controlled norms, bounded evolution under perturbations, and the ability to construct effective descriptions with controlled error.

Admissibility is therefore not a statement about which configuration is realized, but about whether a configuration supports the conditions under which physics can be meaningfully formulated. Outside admissible regions, notions such as particles, fields, probabilities, and even time evolution may fail to exist in a coherent sense.

## Selection as exclusion

Within this framework, selection is not an independent principle acting on an already physical landscape. It is a consequence of admissibility itself. Only configurations lying within admissible regions can support observers, measurements, or effective dynamics; configurations outside those regions are not alternative physical worlds, but non-physical configurations to which physical reasoning does not apply.

Selection therefore operates by exclusion rather than weighting. Unlike anthropic or measure-based reasoning, admissibility does not assign relative likelihoods to configurations; it excludes non-physical configurations outright and only then permits meaningful physical questions to be posed within the remaining domain. It does not require probabilities or measures defined over the entire configuration space. The remaining admissible regions define the domain within which further physical questions can be meaningfully posed.

## Disconnected admissible regions

There is no requirement that admissible regions form a connected set. Because admissibility depends on global stability conditions, admissible regions may be isolated from one another by domains in which physical structure breaks down entirely. Between such regions, continuous deformation is not physically meaningful.

This has two important consequences. First, the space of physically admissible configurations may be far smaller than the space of formally consistent ones. Second, exploratory tools that rely on continuity—perturbative expansion, moduli scanning, or statistical sampling—may be structurally incapable of discovering admissible regions if they traverse non-physical domains.

## Implications for predictivity

Predictivity in an admissibility-first framework arises not from enumerating possibilities but from understanding constraints. When admissibility severely restricts the allowed regions, the resulting framework may exhibit strong explanatory compression even before producing precise numerical predictions. In such cases, progress consists in narrowing the domain of viable physics rather than immediately fitting data.

# Conclusion and Outlook

The persistent difficulty of vacuum selection across quantum gravity, string theory, cosmology, and effective field theory has often been interpreted as evidence for vast landscapes, anthropic reasoning, or fundamental indeterminacy. In this work we have argued for a different diagnosis. The failure to converge may reflect a mis-posed question—one that assumes physics is defined throughout configuration space and that selection can act pointwise on vacua.

We have emphasized that central ingredients of physical reasoning—Hilbert spaces, probability measures, effective field theories, and renormalization group flows—are conditional constructions. They presuppose stability, boundedness, and spectral separation. Where these conditions fail, the language of physics ceases to apply. From this perspective, the relevant problem is not which vacuum is realized, but where physics is well defined at all.

Recasting vacuum selection as a problem of admissibility offers a coherent explanation for why existing approaches have struggled to converge. It suggests a shift in emphasis from cataloguing possibilities to identifying constraints, from scanning configurations to understanding stability, and from anthropic weighting to physical exclusion. Whether this perspective ultimately yields a unique description of observed physics remains an open question, but it provides a clear diagnostic framework for understanding past difficulties and guiding future work.

# Note on Concrete Realizations

While the present work has been intentionally theory-agnostic, it is worth noting that explicit realizations of admissibility-based selection frameworks already exist in the literature. In these constructions, physical observables, effective dynamics, and probabilistic descriptions are defined only on stability-selected sectors of a larger formal configuration space, and fail outside those sectors. Admissibility is enforced through boundedness, spectral separation, and dynamical stability conditions, with non-admissible configurations treated not as alternative vacua but as non-physical. Such frameworks provide concrete existence proofs that the admissibility-first perspective outlined in this paper is mathematically consistent and physically viable, without requiring vacuum selection, anthropic weighting, or global probabilistic measures. Detailed developments of these ideas may be found in the context of Modal Triplet Theory and related work, cited here solely to demonstrate feasibility rather than to advocate a particular foundational model.

<div class="thebibliography">

99

R. Bousso and J. Polchinski, “Quantization of Four-Form Fluxes and Dynamical Neutralization of the Cosmological Constant,” *JHEP* **0006** (2000) 006.

S. Weinberg, “Effective Field Theory, Past and Future,” *PoS* **CD09** (2009) 001.

K. G. Wilson and J. Kogut, “The Renormalization Group and the $`\epsilon`$ Expansion,” *Phys. Rept.* **12** (1974) 75.

P. Nero, “Modal Triplet Theory,” Zenodo Collection, 2023–2025.

</div>
