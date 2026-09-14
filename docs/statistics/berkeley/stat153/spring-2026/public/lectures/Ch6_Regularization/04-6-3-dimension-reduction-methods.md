---
title: 6.3 Dimension Reduction Methods
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Ch6_Regularization.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Ch6_Regularization.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6.3 Dimension Reduction Methods

**Source:** [`public/lectures/Ch6_Regularization.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Ch6_Regularization.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The methods that we have discussed so far in this chapter have controlled variance in two different ways, either by using a subset of the original variables, or by shrinking their coefficients toward zero. All of these methods are defined using the original predictors, _X_ 1 _, X_ 2 _, . . . , Xp_ . We now explore a class of approaches that _transform_ the predictors and then fit a least squares model using the transformed variables. We will refer to these techniques as _dimension reduction_ methods.


Let _Z_ 1 _, Z_ 2 _, . . . , ZM_ represent _M < p linear combinations_ of our original _p_ predictors. That is,

for some constants _φ_ 1 _m, φ_ 2 _m . . . , φpm, m_ = 1 _, . . . , M_ . We can then fit the linear regression model


using least squares. Note that in (6.17), the regression coefficients are given by _θ_ 0 _, θ_ 1 _, . . . , θM_ . If the constants _φ_ 1 _m, φ_ 2 _m, . . . , φpm_ are chosen wisely, then such dimension reduction approaches can often outperform least squares regression. In other words, fitting (6.17) using least squares can lead to better results than fitting (6.1) using least squares.

The term _dimension reduction_ comes from the fact that this approach reduces the problem of estimating the _p_ +1 coefficients _β_ 0 _, β_ 1 _, . . . , βp_ to the

---

[← 6.2 Shrinkage Methods](03-6-2-shrinkage-methods.md) · [Up: contents](index.md)
