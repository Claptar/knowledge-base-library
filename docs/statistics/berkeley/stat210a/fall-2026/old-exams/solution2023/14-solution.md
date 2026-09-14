---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _Z_ = _Y/√_ 2 so it has an identity covariance. We want to use a James-Stein estimator for the mean of _Z_ (which will be 0 if we’re lucky) and the MLE for the mean of _W_ = ( _X_<sup>(1)</sup> + _X_<sup>(2)</sup> ) _/√_ 2 _∼ Nd_ ( _θ_<sup>(1)</sup> + _θ_<sup>(2)</sup> _, Id_ ). Note _Z_ and _W_ are independent, which we can verify by noting that they represent two orthogonal projections of ( _X_<sup>(1)</sup> _, X_<sup>(2)</sup> ). Let _µ_ denote the mean of _Z_ , and _ν_ the mean of _W_ . Then _ν_ ˆ = _W_ and


The MSE for estimating ( _θ_<sup>(1)</sup> _, θ_<sup>(2)</sup> ) is the sum of the MSEs for the two estimators _µ_ ˆ and ˆ _ν_ . The second has MSE _d_ and the first has MSE strictly less than _d_ , equaling 2 if _µ_ = 0.

8

---

[← Solution](13-solution.md) · [Up: contents](index.md) · [3. Nonparametric two-sample problem (20 points, 5 points / part). →](15-3-nonparametric-two-sample-problem-20-points-5-points-part.md)
