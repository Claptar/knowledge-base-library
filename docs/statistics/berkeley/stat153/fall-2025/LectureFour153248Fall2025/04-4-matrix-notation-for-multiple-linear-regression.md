---
title: 4 Matrix Notation for Multiple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Matrix Notation for Multiple Linear Regression

**Source:** [`LectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This notation is used not just to write formulae for linear regression, but also in code. For example, the OLS function in `statsmodels` uses the syntax `sm.OLS(y, X).fit()` to fit the linear regression model, where _y_ ( _n ×_ 1 vector) and _X_ ( _n ×_ ( _m_ +1) matrix) are defined above.

With this notation, one can write the sum of squares _S_ ( _β_ 0 _, . . . , βm_ ) as:


There are two important facts about _S_ ( _β_ ):

1. **Fact 1** : the least squares estimator _β_<sup>ˆ</sup> is given by the formula:


The proof of (7) is as follows. The gradient of _S_ ( _β_ ) is given by


5

Because _β_<sup>ˆ</sup> minimizes _S_ ( _β_ ), the gradient should equal zero when _β_ = _β_<sup>ˆ</sup> , and this leads to


2. **Fact 2** : The following Pythagorean identity holds:


To prove (9), write


The cross product is zero (leading to (9)) because:

where we used (8).

Using (9), we can write the posterior density (2) as


The above formula is a special case of (6) with


or equivalently


We thus have

With the posterior density (11), one can do uncertainty quantification about the parameters _β_ 0 _, β_ 1 _, . . . , βm_ . One can generate multiple samples from _tm_ +1( _β,_<sup>ˆ</sup> ( _S_ ( _β_<sup>ˆ</sup> ) _/_ ( _n − m −_ 1))( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _, n − m −_ 1) and plot the resulting fitted values to visualize the uncertainty in the coefficients.

6

---

[← 3 Why is (5) a t -density?](03-3-why-is-5-a-t--density.md) · [Up: contents](index.md)
