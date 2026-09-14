---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`units/old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A natural idea is to condition on the value of _T_ ( _X_ ), which is a sufficient statistic for the null submodel. Then, we can calculate the same statistic from the previous part, plugging in _θ_<sup>ˆ</sup> 0 = _T/n_ for _θ_ 0:


Then we can reject for large values of _W_ , which is equivalent up to an affine transformation to rejecting for small values of<sup>�</sup> _i_<sup>_i|Xi|/T_.</sup>

The statistic _W_ may have smaller than unit variance but it doesn’t really matter since we can just calculate its conditional distribution by Monte Carlo or other numerical integration techniques, and reject when _W_ is larger than some quantile. In fact we can simulate directly fron the conditional distribution of _W_ , or of<sup>�</sup> _i_<sup>_i|Xi|/T_, by simulating</sup><sup>_D_= (</sup><sup>_|X_1</sup><sup>_|, . . . , |Xn|_)</sup><sup>_/T_from the Dirichlet(1</sup><sup>_n_)</sup> distribution, but this is not necessary to get full credit.

**Alternative solution:** A natural idea is to condition on the value of _T_ ( _X_ ), which is a sufficient statistic for the null submodel. Rejecting for large _Z_ is equivalent to rejecting for small values of<sup>�</sup> _i_<sup>_i|Xi|_,sowecanjustsimulate</sup> from the conditional distribution given _T_ ( _X_ ) and reject when the statistic is above its conditional upper _α_ quantile. It so happens this is equivalent to the first approach because _D_ is independent of _T_ , so the conditional distribution of ( _|X_ 1 _|, . . . , |Xn|_ ) given _T_ = _t_ is just _t · D_ .

5

---

[← Solution](08-solution.md) · [Up: contents](index.md) · [2. Multivariate normal means (20 points, 5 points / part). →](10-2-multivariate-normal-means-20-points-5-points-part.md)
