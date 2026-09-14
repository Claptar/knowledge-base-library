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

We can define the variable _Y_ = _X_<sup>(2)</sup> _− X_<sup>(1)</sup> _∼ Nd_ ( _θj_<sup>(2)</sup> _− θj_<sup>(1)</sup><sup>_,_2</sup><sup>_σ_2</sup><sup>_Id_).Under</sup> the null hypothesis, 2 _σ_ <u>1</u><sup>2</sup><sup>_∥Y ∥_2</sup><sup>_∼χ_</sup> _d_<sup>2,sowecanrejectwhenthisstatisticis</sup> above the upper- _α_ quantile of that distribution.

- (b) Now drop the assumption that _σ_<sup>2</sup> is known (i.e. now it is **unknown** ), and assume (for this and the next part **only** ) that _θj_<sup>(2)</sup> = _θj_<sup>(1)</sup> + _δ_ , for some _δ ∈_ R (i.e. every coordinate is shifted by the same amount _δ_ ), but apart from this assumption, both _θ_<sup>(1)</sup> and _θ_<sup>(2)</sup> are unknown. Propose a finite-sample test of _H_ 0 : _δ_ = 0 against the two-sided alternative _H_ 1 : _δ̸_ = 0. Give a test statistic and cutoffs in terms of a quantile of a specific distribution.

**Note:** You do _not_ need to prove any optimality properties for your test, but you won’t receive full credit if you trivialize the problem by giving an inefficient test, even if the test is valid in the Type I error sense.

---

[← 2. Multivariate normal means (20 points, 5 points / part).](10-2-multivariate-normal-means-20-points-5-points-part.md) · [Up: contents](index.md) · [Solution →](12-solution.md)
