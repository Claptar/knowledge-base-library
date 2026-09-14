---
title: 1 Bayesian Inference for Simple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFour153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Bayesian Inference for Simple Linear Regression

**Source:** [`LectureFour153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFour153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We use the prior


for a large number _C_ (the exact value of _C_ will not matter in the following calculations). Note that as _σ_ is always positive, we have made the uniform assumption on log _σ_ (by the change of variable formula, the density of _σ_ would be given by _fσ_ ( _x_ ) = _f_ log _σ_ (log _x_ ) _x_<sup><u>1</u>=</sup> _I{−C<_ 2 _Cx_ log _x<C}_ =<sup>_I{e−C_</sup> 2<sup>_<x<e_</sup> _Cx_<sup>_C_</sup><sup>_<u>}</u>_</sup> .

The joint posterior for all the unknown parameters _β_ 0 _, β_ 1 _, σ_ is then given by (below we write the term “data” for _y_ 1 _, . . . , yn_ ):


The two terms on the right hand side above are the likelihood:


and the prior:


Recall that _S_ ( _β_ 0 _, β_ 1) denotes the sum of squares:


We thus obtain


1

The above is the joint posterior over _β_ 0 _, β_ 1 _, σ_ . The posterior over only the main parameters _β_ 0 _, β_ 1 can be obtained by integrating (or marginalizing) the parameter _σ_ .


When _C_ is large, the above integral can be evaluated from 0 to _∞_ which gives


The change of variable

allows us to write the integral as


where, we are using the fact that �0 _∞_<sup>_s−n−_1 exp(</sup><sup>_−_1</sup><sup>_/_(2</sup><sup>_s_2))</sup><sup>_ds_isaconstant(inthesensethat</sup> it does not depend on _β_ 0 and _β_ 1).

The posterior density of ( _β_ 0 _, β_ 1) is thus


In words, the posterior density is inversely proportional to _S_ ( _β_ 0 _, β_ 1)<sup>_n/_2</sup> . This implies that the posterior mode is just the least squares estimator ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). It is nicer to write the posterior in the following equivalent form:


Note that (1) and (2) represent exactly the same density because the term ( _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1))<sup>_n/_2</sup> does not depend on _β_ 0 _, β_ 1 and is thus a constant.

Generally, the density (2) will be quite sharply concentrated around the least squares estimator ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1) especially when _n_ is large. This is because, when ( _β_ 0 _, β_ 1) is such that _S_ ( _β_ 0 _, β_ 1) is large compared to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1), the quantity


would be quite negligible because of the large power _n/_ 2. As a result, the posterior density _fβ_ 0 _,β_ 1 _|_ data( _β_ 0 _, β_ 1) will be concentrated around those values of ( _β_ 0 _, β_ 1) for which _S_ ( _β_ 0 _, β_ 1)

2

is quite close to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). For example, suppose _n_ = 791, and that ( _β_ 0 _, β_ 1) is such that _S_ ( _β_ 0 _, β_ 1) = (1 _._ 1) _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). Then


Such ( _β_ 0 _, β_ 1) will thus get negligible posterior probability. Even for ( _β_ 0 _, β_ 1) such that _S_ ( _β_ 0 _, β_ 1) = (1 _._ 01) _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1), we have


and so such ( _β_ 0 _, β_ 1) will also get fairly small posterior probability.

To sum up, when _n_ is large, the posterior probability will be concentrated around those ( _β_ 0 _, β_ 1) for which _S_ ( _β_ 0 _, β_ 1) is very close to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). Generally, this would imply that ( _β_ 0 _, β_ 1) would itself have to be close to ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). For this reason, the indicator term in (2) has no effect when _C_ is large. From now on, we shall drop this indicator term and refer to the Bayesian posterior as simply


It turns out that this represents a multivariate _t_ -density, as well shall soon. Before that, let us first note that we have essentially the same formula in multiple linear regression as well.

---

[Up: contents](index.md) · [2 Multiple Linear Regression →](02-2-multiple-linear-regression.md)
