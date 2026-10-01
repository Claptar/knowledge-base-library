---
title: "Hines et al. 2021 — Demystifying statistical learning based on efficient influence functions"
paper: "summary"
source: "https://arxiv.org/abs/2107.00681"
licence: "arXiv non-exclusive distribution licence — not reproduced"
written: "2026-10-02"
---

> **Summary of a paper.** Hines, O., Dukes, O., Diaz-Ordaz, K., & Vansteelandt, S. (2021). Demystifying statistical learning based on efficient influence functions. arXiv:2107.00681 [math.ST]. ([original](https://arxiv.org/abs/2107.00681)). Rights: arXiv non-exclusive distribution licence — not reproduced. This is a short account of it in our own words; the work itself is not reproduced here.

# Demystifying statistical learning based on efficient influence functions

## What this covers

A tutorial on deriving an estimand's *efficient influence function* and turning it into a root-$n$
consistent estimator compatible with machine-learning-based nuisance models, at the intersection of
semiparametric efficiency theory, causal inference, and the "targeted learning"/"debiased machine
learning" literature.

## The question

Standard practice fits a parametric model, extracts a coefficient, and reports a standard error
computed as though that model were fixed in advance — a fiction that breaks down once the model is
chosen adaptively (by variable selection or a learning algorithm), inducing bias and excess
variability that ordinary standard-error formulas do not capture. The alternative is to center the
analysis on a nonparametric estimand — a functional of the data-generating distribution defined
without reference to any model — and to base estimation and inference on that estimand's efficient
influence function. The authors say this route is treated as a "dark art": existing expositions lean on functional-analytic
machinery (Hilbert spaces, manipulating a score function into a canonical integral form) opaque to
most applied users, who then take a published influence function on faith. The paper's aim is to make
the derivation routine, using only the differentiation techniques of a basic calculus course.

## The approach

The authors adopt the "point-mass contamination," or Gâteaux-derivative, route formalised by
Ichimura and Newey, rather than the more usual canonical-gradient-via-score-function route. An
estimand $\Psi(\mathcal{P})$ is viewed as a functional of the whole data-generating distribution and
perturbed along a one-parameter path mixing $\mathcal{P}$ with a point mass at a single hypothetical
observation; differentiating $\Psi$ along that path, by ordinary chain and product rules, gives the
efficient influence function directly, without positing score functions or solving an integral
equation. The paper works this recipe through a sequence of estimands of increasing complexity —
the mean, a density, a covariance, potential-outcome and treatment-effect functionals, conditional
means — building reusable identities (for conditional expectations and for densities perturbed at a
point) that are then combined to handle more elaborate estimands: the average treatment effect,
average derivative effects, expected conditional covariance, mediation estimands, and incremental
propensity score interventions. It then shows how the influence function is put to use: a plug-in
estimator built from data-adaptively estimated nuisance functions carries a bias term (a "drift")
that need not vanish at the parametric rate; adding, subtracting, or solving for a correction based
on the influence function — the one-step estimator, the estimating-equations/AIPW estimator, or
targeted learning's retargeting of the nuisance estimator — removes this leading bias, leaving a
remainder term that can be controlled under conditions on how fast the nuisance estimators converge.

## What it found

Under conditions that make the remaining "empirical process" and remainder terms of the resulting
von Mises expansion vanish — chiefly, fast-converging nuisance estimators, with cross-fitting used
when the same data trains and evaluates them — all three correction strategies yield an estimator
that is asymptotically normal around the truth, with variance equal to the expected square of the
efficient influence function. That variance is the
nonparametric analogue of the Cramér–Rao bound, so these estimators are asymptotically efficient and
the sample variance of the influence function gives a valid standard error, without having to
separately account for uncertainty in the fitted nuisance models. The paper also shows how estimands can fail to admit this treatment: a density at a single continuous
point, and a conditional mean at a continuous covariate value, both have influence functions with
infinite variance, so no root-$n$-consistent estimator of either exists. The worked examples are offered to show that a
handful of techniques — the chain rule, the quotient rule, and two reusable identities for perturbed
conditional expectations and densities — reproduce results that, in the original research papers
cited, required more elaborate, model-specific arguments.

## Limits and context

The authors are explicit that their method is a derivation technique, not a new theory: the
asymptotic justification of the von Mises expansion still rests on results from functional analysis
(the Riesz representation theorem, regularity and convergence-rate conditions on the nuisance
estimators) that the paper relegates to an appendix rather than dispensing with. Proceeding fully
nonparametrically is not always possible either — inference on the mean, for instance, is impossible
without restrictions on the tails of the outcome distribution, and several of the paper's own
examples still rely on working models for nuisance functions that must be at least somewhat smooth
or low-dimensional for fast convergence. The paper positions itself against parametric-model-first
statistical education and practice, which it argues produces model-dependent, poorly understood
inference once models are chosen adaptively from data; and against the idea that efficiency gains
should be "extracted" from strong modelling assumptions, arguing instead that such gains belong only
to special cases where restrictions are known to hold by design or strong prior knowledge. It does
not address how to choose an estimand in the first place, and it does not supply new convergence-rate
results for machine-learning estimators of nuisance functions, treating those as a separate, cited
literature.

## Citation

Hines, O., Dukes, O., Diaz-Ordaz, K., & Vansteelandt, S. (2021). Demystifying statistical learning
based on efficient influence functions. arXiv:2107.00681 [math.ST]. Available at
https://arxiv.org/abs/2107.00681 (the paper text gives no separate journal venue; this is the arXiv
preprint, v3, dated 1 December 2021).
