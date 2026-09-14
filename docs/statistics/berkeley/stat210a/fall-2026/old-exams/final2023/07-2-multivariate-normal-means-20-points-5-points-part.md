---
title: 2. Multivariate normal means (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2023.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/final2023.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2. Multivariate normal means (20 points, 5 points / part).

**Source:** [`old-exams/final2023.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/final2023.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Suppose that we observe two multivariate normal random vectors in R<sup>_d_</sup> , for _d ≥_ 3:


where _θ_<sup>(1)</sup> _, θ_<sup>(2)</sup> _∈_ R<sup>_d_</sup> and _σ_<sup>2</sup> _>_ 0, and _Id_ is the _d × d_ identity matrix.

For all parts below, if you refer to quantiles of a _t_ , _χ_<sup>2</sup> , or _F_ distribution, you will need to **give the relevant degrees of freedom** in order to receive full credit.

- (a) Assume (for this part **only** ) that _σ_<sup>2</sup> is known but _θ_<sup>(1)</sup> _, θ_<sup>(2)</sup> are unknown, and suggest a test of the hypothesis _H_ 0 : _θ_<sup>(1)</sup> = _θ_<sup>(2)</sup> (that _θj_<sup>(1)</sup> = _θj_<sup>(2)</sup> for _every j_ = 1 _, . . . , d_ ) against the hypothesis that _θ_<sup>(1)</sup><sup>_̸_</sup> = _θ_<sup>(2)</sup> (that _θj_<sup>(1)</sup> = _θj_<sup>(2)</sup> for _at least one j_ = 1 _, . . . , d_ ). Give your test statistic and a rejection cutoff in terms of a quantile of a _χ_<sup>2</sup> distribution.

- (b) Now drop the assumption that _σ_<sup>2</sup> is known (i.e. now it is **unknown** ), and assume (for this and the next part **only** ) that _θj_<sup>(2)</sup> = _θj_<sup>(1)</sup> + _δ_ , for some _δ ∈_ R (i.e. every coordinate is shifted by the same amount _δ_ ), but apart from this assumption, both _θ_<sup>(1)</sup> and _θ_<sup>(2)</sup> are unknown. Propose a finite-sample test of _H_ 0 : _δ_ = 0 against the two-sided alternative _H_ 1 : _δ̸_ = 0. Give a test statistic and cutoffs in terms of a quantile of a specific distribution.

**Note:** You do _not_ need to prove any optimality properties for your test, but you won’t receive full credit if you trivialize the problem by giving an inefficient test, even if the test is valid in the Type I error sense.

- (c) Under the same assumptions as in part (b), propose a confidence interval for _δ_ . If you didn’t solve part (b), or if you are not confident in your answer, you may assume that there is a valid test statistic from part (b) of the form _T_ ( _X_<sup>(1)</sup> _, X_<sup>(2)</sup> ), and (non-data-dependent) cutoff values _c_ 1( _α_ ) and _c_ 2( _α_ ) (so the test rejects if _T < c_ 1 or _T > c_ 2), and give your answer in terms of these.

- (d) (*) Now, drop the assumption about _δ_ from the previous parts, so _θ_<sup>(1)</sup> and _θ_<sup>(2)</sup> are again completely unknown. And now assume (for this part **only** ) that _σ_<sup>2</sup> = 1. Also, suppose that we believe _θ_<sup>(1)</sup> _≈ θ_<sup>(2)</sup> as vectors in R<sup>_d_</sup> , but we do not have any other strong priors about it. Suggest an estimator that will have MSE less than 2 _d_ for all values of _θ_<sup>(1)</sup> _, θ_<sup>(2)</sup> , but which will have MSE _d_ + 2 whenever _θ_<sup>(1)</sup> = _θ_<sup>(2)</sup> .

**Note:** You do not need to prove that your estimator has these properties, it is sufficient to give a correct functional form for the estimator.

7

---

[← Problem 1 answers continued (3)](06-problem-1-answers-continued-3.md) · [Up: contents](index.md) · [Problem 2 answers continued (1) →](08-problem-2-answers-continued-1.md)
