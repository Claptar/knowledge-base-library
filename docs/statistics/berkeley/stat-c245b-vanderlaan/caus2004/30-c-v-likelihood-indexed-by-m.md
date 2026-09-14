---
title: C.V. Likelihood indexed by m
source: https://vanderlaan-lab.org/teach-files/caus2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/caus2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# C.V. Likelihood indexed by m

**Source:** [`caus2004.pdf`](https://vanderlaan-lab.org/teach-files/caus2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here we compute likelihood over validation sample(s) using the likelihood from the training sample.


Let


Estimate f0 with f<sup>ˆ</sup> m(Pn). Estimate µ0 with estimator from above:


Why is this not the best method in this case?

This procedure uses the best trade-off of bias and variance. (m is small then you have a small variance and large bias, m is large then you have a large variance and small bias, as m −→∞ then we approach empirical) (If f0 is what you want then this is a good procedure)


Thus,


Averaging reduces the variability but not necessarily the bias. Bias should be converging at a rate < 1/<sup>√</sup> <u>n</u> to be as good as the estimator using the empirical. But here<sup>√</sup> <u>n(Bias) =</u><sup>√</sup> <u>nO(n</u><sup>−2/5</sup> = O(n<sup>1/10</sup> ) Thus, likelihood is not the best procedure here. (In literature this is referred to as the curse of dimensionality)

---

[← Yaz − Y0z ⊥ Z0 | W, for all a, z](29-yaz-y0z-z0-w-for-all-a-z.md) · [Up: contents](index.md) · [Estimating Function Approach →](31-estimating-function-approach.md)
