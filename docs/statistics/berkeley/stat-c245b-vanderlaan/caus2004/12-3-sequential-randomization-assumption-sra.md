---
title: (3) Sequential randomization assumption (SRA)
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# (3) Sequential randomization assumption (SRA)

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

At any time point t, treatment assignment is only dependent on the observed history of a given subject. It depends neither on future covariate or outcome measures, nor on unobserved counterfactual histories:


Note that this is an assumption on g0(·|X<sup>F ull</sup> ), the conditional distribution of A<sup>¯</sup> given X<sup>F ull</sup> :


We assume that, given the observed history of a subject, treatment assignment is independent of X<sup>F ull</sup> :


Suppose there exists an unmeasured confounder U that is associated with the outcome Y as well as with treatment assignment. Then this conditional independence assumption will not hold. Thus the observed history must contain any variables that are associated with treatment assignment. The SRA informs our study design in that it requires us to measure any variables that are associated with treatment assignment.

Example 3: Sequentially randomized trials meet this assumption. For simplicity, assume that treatment is binary, A(t) ∈{0, 1}. In order to decide if we assign a subject to treatment at any given time point t, we take into account the subject’s history (side effects, drug resistance, viral mutations etc.). We use a known function of this history to obtain a probability p, 0 < p < 1, with which we assign the subject to treatment. Note that treatment assignment is probabilistic rather than deterministic since the function does not return

7

values of zero or one.

---

[← (2) Consistency assumption (CA)](11-2-consistency-assumption-ca.md) · [Up: contents](index.md) · [(4) Experimental treatment assignment assumption (ETA) →](13-4-experimental-treatment-assignment-assumption-eta.md)
