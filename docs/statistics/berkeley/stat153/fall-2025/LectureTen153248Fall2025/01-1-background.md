---
title: 1 Background
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Background

**Source:** [`LectureTen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We will now start our third main topic: High-dimensional linear regression. We shall motivate our basic high-dimensional linear regression model starting from the change of slope (or broken stick regression) model that we previously considered.

The change of slope (or broken stick regression) model is given by:


Recall that ( _t − c_ )+ equals 0 if _t ≤ c_ and _t − c_ if _t ≥ c_ . We shall also sometimes write ( _t − c_ )+ = ReLU( _t − c_ ). The model (1) says that for times _t ≤ c_ , the slope of the regression line is _β_ 1 while for _t > c_ , the slope changes to _β_ 1 + _β_ 2. Note _β_ 2 represents the change in slopes (after _t_ = _c_ and before _t_ = _c_ ).

Generalizations of model (1) can be obtained by having _k_ points of change of slope (instead of just one):


We use least squares to estimate the unknown parameters _c_ 1 _, . . . , ck, β_ 0 _, β_ 1 _, . . . , βk_ +1 in this model. In the previous lectures, we recommended the method where we first compute the function:


and then attempt to minimize _RSS_ ( _c_ 1 _, . . . , ck_ ) by some grid-based search jointly over _c_ 1 _, . . . , ck_ to estimate _c_ 1 _, . . . , ck_ . Once _c_ 1 _, . . . , ck_ are estimated by _c_ ˆ1 _, . . . ,_ ˆ _ck_ , we estimate the remaining parameters _β_ 0 _, . . . , βk_ +1 by least squares in the linear regression model obtained by fixing each _cj_ by _c_ ˆ _j_ .

This method is computationally inefficient especially when _k_ is not small (even when _k ≥_ 3). An alternative method of obtaining the least squares estimates is to directly minimize the least squares objective with respect to all parameters:


1

This is a non-trivial optimization problem but several optimization libraries provide functions which can be employed for solving this. One option is the PyTorch library in Python which uses first order optimization algorithms (gradient descent and related methods). These methods require a good initialization for the parameters (for _c_ 1 _, . . . , ck_ , a natural initialization is to take equally spaced quantiles of _t_ ; once _cj_ ’s are chosen, initial values for _β_ 0 _, . . . βk_ +1 can be obtained by running a linear regression with those fixed _cj_ ’s).

When _k_ is not small, the least squares estimates (3) can lead to fitted values which overfit the data. In such cases, we need to add a regularization term to the objective function to prevent overfitting. We shall see how to do this in the case of the high-dimensional model which uses all possible _cj_ ’s.

---

[Up: contents](index.md) · [2 High-dimensional Version of (2) →](02-2-high-dimensional-version-of-2.md)
