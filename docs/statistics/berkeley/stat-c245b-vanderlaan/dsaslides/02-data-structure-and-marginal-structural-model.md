---
title: Data structure and Marginal Structural Model
source: https://vanderlaan-lab.org/teach-files/dsaslides.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/dsaslides.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data structure and Marginal Structural Model

**Source:** [`dsaslides.pdf`](https://vanderlaan-lab.org/teach-files/dsaslides.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Full data structure.

X = ((Ya, a ∈A), W ) ∼ FX,0

Ya is the counterfactual outcome, a represents treatment, W represents the baseline covariates.

- Observed data structure.

O = (A, YA, W ) ∼ P0 = PFX,0,g0

A is a random variable denoting which treatment is assigned, YA is the outcome under treatment A.

- Marginal Structural Model (MSM).

Estimate treatment specific mean E(Ya|V ) as a function of a and V , where V ⊂ W .

Randomization assumption (RA): treatment is randomly

Nov. 8, 2004

3

- assigned within strata of W , g0(a|X) = g0(a|W ) for all a ∈A.

- ▶ Defining the parameter of interest in terms of a loss function.

Let ψ(a, v) = E(Ya|V ) be the parameter of interest. The true parameter value ψ0 is the one maps the true data population, ψ0 ≡ ψ(FX,0). It is defined in terms of a loss function, L(X, ψ), as the minimizer of the expected loss, or risk. That is, ψ0 is

= ψ0 arg min E(L(X, ψ)) ψ∈Ψ

- Full data loss function.

L(X, ψ) = � (Ya − ψ(a, v))<sup>2</sup> a∈A

The true model ψ0 is the minimizer of the expectation of the loss function.

Nov. 8, 2004

4

---

[← Outlines](01-outlines.md) · [Up: contents](index.md) · [Estimation Road Map: Choices of loss function →](03-estimation-road-map-choices-of-loss-function.md)
