---
title: Cohort of children with asthma
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Cohort of children with asthma

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Treatment is use of steriod spray; Outcome is lung function(FEV) in two years. Based on history get assigned treatment, follow, at end observe outcomes.

Necessary Assumptions:

Sequential Randomization Assumption(SRA):

We can identify from the data what the treatment was (i.e. no unmeasured confounders)

Dynamic treatment regime means that the treatment is dependent on the past (covariates)

Consistancy Assumption:

For a given treatment rule W �→ d(W ) (function that maps history at baseline into treatment). Let Xd = (W, Yd), the treatment specific counterfactual, be the data we would have seen on the subject if they would have followed rule d.

Let X<sup>F ull</sup> = (Xd : d) = (W, (Yd : d ∈D)) where D = {w �→ dδ1,δ2 (w) : δ1, δ2} Assumption is O = (A, Xa) = (W, A, YA)

How to simulate?

Simulate baseline covariates. Simulate dynamic treatment specific outcomes. 1. Ydδ1 ,δ2 = Y0 + β0δ1 + β1δ2 + β2δ1δ2 (Draw Y0 from N(0,1) 2. Y0|W 1 and 2 gives us X<sup>F ull</sup> = (W, Yd : d ∈D) Then we simulate A|W ⇒ O = (A, W, YA) To generate counterfactuals: treat as missing data, apply G-Computation formula to observed data.

13

P (Yd = y, W = w) = P (W = w)P (Y = y|A = d(w), W = w) Can check if close to the truth.

Randomization Assumption:

A|(W, Yd : d) ∼ A|W

Y’s are random variables; The distributions for Y0, Y1, and Yd are different Y0 is the random variable observed if no one receives treatment Y1 is the random variable observed if everyone given static treatment Now:

Theorem: Distribution of Yd: P (Yd = y, W = w) = P (W = w)P (Y = y|A = d(w), W = w)

Given a rule d:

|δ1|δ2|ˆ<br>EYδ1,δ2|
|---|---|---|
|1|20|96|
|1|30|95|
|1|50|91|
|1|80|90|
|2|20|97|
|2|30|.|
|...|...|...|


For every combination of δ1, δ2 do a G-compuation to get EYˆ δ1,δ2 . Can see which combination of δ1, δ2 is the "best". Can bootstrap. Can Assume model.

ˆ e.g. EY δ1,δ2 = β0 + β1δ1 + β2δ2 + β3δ1δ2 lm(EY<sup>ˆ</sup> δ1,δ2 = δ1 + δ2 + δ1δ2)

Alternatively could have modeled:

EYˆδ1,δ2 |W = β0 + β1δ1

This is the analog of Marginal Structural Models, except for dynamic treatment regimes.

Inference for the Causal Effects of Dynamic Treatment Regimes in Point Treatment Studies 9/22/04

---

[← Example](19-example.md) · [Up: contents](index.md) · [Definitions →](21-definitions.md)
