---
title: 5 Ridge vs LASSO
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEleven153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Ridge vs LASSO

**Source:** [`LectureEleven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEleven153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The LASSO estimator _β_<sup>ˆlasso</sup> ( _λ_ ) is usually sparse which means that most of _β_<sup>ˆ</sup> 2<sup>lasso</sup> ( _λ_ ) _, . . . , β_<sup>ˆ</sup> _n_<sup>lasso</sup> _−_ 1<sup>(</sup><sup>_λ_)</sup> are exactly (up to numerical precision) equal to zero. This implies that _µ_ ˆ<sup>lasso</sup> _t_ ( _λ_ ) is piecewise linear. On the other hand, _β_<sup>ˆridge</sup> ( _λ_ ) will not be sparse in that all the terms _β_<sup>ˆ</sup> 2<sup>ridge</sup> ( _λ_ ) _, . . . , β_<sup>ˆ</sup> _n_<sup>ridge</sup> _−_ 1<sup>(</sup><sup>_λ_)</sup> will be nonzero (even though they may be small). This gives a smooth appearance to _β_ ˆ<sup>ridge</sup> ( _λ_ ).

Some insight into the tendency of the LASSO regularization to yield exact zeroes in contrast to ridge regularization can be gained from the following two simple facts.

**Fact 5.1** (Simple Ridge) **.** _Suppose y is a real number and λ >_ 0 _. Then the minimizer of_


_is given by_


_Proof._ We just need to differentiate _f_ and set the derivative to zero:


3

**Fact 5.2** (Simple LASSO) **.** _Suppose y is a real number and λ >_ 0 _. Then the minimizer of_


_is given by_


_Proof._ The derivative of _f_ is given by:


At _β_ = 0, the function _|β|_ is not differentiable. We now need to set the derivative to zero. Setting to zero the expression for _f_<sup>_′_</sup> ( _β_ ) for _β >_ 0, we get


Since this expression for _f_<sup>_′_</sup> ( _β_ ) is only valid when _β >_ 0, we need to assume that _y > λ/_ 2.

Similarly setting to zero the expression for _f_<sup>_′_</sup> ( _β_ ) when _β <_ 0, we get


which is valid when _y_ + _λ/_ 2 _<_ 0 or _y < −λ/_ 2.

The above calculations show that _β_<sup>ˆ</sup> equals _y − λ/_ 2 when _y > λ/_ 2, and that _β_<sup>ˆ</sup> equals _y_ + _λ/_ 2 when _y < −λ/_ 2. In the intermediate range _−λ/_ 2 _≤ y ≤ λ/_ 2, check that _f_<sup>_′_</sup> ( _β_ ) _<_ 0 for _β <_ 0 and _f_<sup>_′_</sup> ( _β_ ) _>_ 0 for _β >_ 0. This means that _f_ is decreasing on ( _−∞,_ 0) and then increasing on (0 _, ∞_ ) which implies that the minimum of _f_ has to be achieved at 0.

From these facts, it is clear that when _y̸_ = 0, the ridge minimizer will never be zero, while the lasso minimizer will equal exactly zero for all _y_ -values in the range [ _−λ/_ 2 _, λ/_ 2]. The LASSO penalty therefore has a tendency to produce exact zeros unlike the ridge penalty.

---

[← 4 Regularized Estimates](04-4-regularized-estimates.md) · [Up: contents](index.md) · [6 Cross-validation for selecting λ →](06-6-cross-validation-for-selecting-λ.md)
