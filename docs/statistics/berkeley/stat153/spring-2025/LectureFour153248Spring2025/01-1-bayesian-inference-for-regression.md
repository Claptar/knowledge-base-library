---
title: 1 Bayesian Inference for Regression
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFour153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Bayesian Inference for Regression

**Source:** [`LectureFour153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFour153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We observe a time series _y_ 1 _, . . . , yn_ . We can fit a line to this data using the model:


We can fit a more complicated trend function such as the cubic function to the data using the model:

i.i.d _yt_ = _β_ 0 + _β_ 1 _t_ + _β_ 2 _t_<sup>2</sup> + _β_ 3 _t_<sup>3</sup> + _ϵt_ with _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) _._ (2)

(1) and (2) are both examples of the multiple linear regression model. More generally, the multiple linear regression model is given by:


There are _m_ covariates here and _xij_ is the _i_<sup>_th_</sup> value of the _j_<sup>_th_</sup> covariate. (1) is a special case of (3) with _m_ = 1 and _xi_ 1 = _i_ for _i_ = 1 _, . . . , n_ . (2) is a special case of (3) with _m_ = 3 and _xi_ 1 = _i, xi_ 2 = _i_<sup>2</sup> _, xi_ 3 = _i_<sup>3</sup> . We shall assume that _n_ is much larger than _m_ (the case where _n_ is comparable or even smaller to _m_ is known as high-dimensional linear regression and we shall look at this later).

In Bayesian inference for (3), we work with the prior


for a very large positive _C_ . The joint posterior density of _β_ 0 _, . . . , βm, σ_ is then given by

_fβ_ 0 _,β_ 1 _,σ|_ data( _β_ 0 _, β_ 1 _, . . . , βm, σ_ )


The above is the joint posterior over _β_ 0 _, β_ 1 _, . . . , βmσ_ . The posterior over only the coefficient

1

parameters _β_ 0 _, β_ 1 can be obtained by integrating (or marginalizing) the parameter _σ_ .


Using the notation


we can write


The mode of the above posterior is the least squares estimates _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ which minimize _S_ ( _β_ 0 _, . . . , βm_ ) over all values of _β_ 0 _, . . . , βm_ . (4) is equivalent to


Note that (4) and (5) represent exactly the same density because the term ( _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, . . . , β_<sup>ˆ</sup> _m_ )<sup>_n/_2</sup> does not depend on _β_ 0 _, β_ 1 _, . . . , βm_ and is thus a constant.

The density (5) represents a multivariate _t_ -distribution (see `https://en.wikipedia.org/ wiki/Multivariate_t-distribution` ). We demonstrate this below. It will be convenient to use the following vector-matrix notation here:


With this notation, one can check that

_S_ ( _β_ ) = _S_ ( _β_ 0 _, . . . , βm_ ) = _∥y − Xβ∥_<sup>2</sup> _._

The following facts will be important:

2

1. **Fact 1** : the least squares estimator _β_<sup>ˆ</sup> is given by the formula:


The proof of (6) is as follows. The gradient of _S_ ( _β_ ) is given by


Because _β_<sup>ˆ</sup> minimizes _S_ ( _β_ ), the gradient should equal zero when _β_ = _β_<sup>ˆ</sup> , and this leads to


2. **Fact 2** : The following Pythagorean identity holds:


To prove (8), write


The cross product is zero (leading to (8)) because:

where we used (7).

Using (8), we can write the posterior density (5) as


The formula for the multivariate _t_ -distribution will be reviewed next which will make clear that the above is an instance of the _t_ -density.

---

[Up: contents](index.md) · [2 Multivariate t -density →](02-2-multivariate-t--density.md)
