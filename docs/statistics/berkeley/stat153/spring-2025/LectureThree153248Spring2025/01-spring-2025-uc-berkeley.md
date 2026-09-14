---
title: Spring 2025, UC Berkeley
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureThree153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Spring 2025, UC Berkeley

**Source:** [`LectureThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureThree153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Aditya Guntuboyina

January 28, 2025

## **1 Bayesian Inference in Simple Linear Regression**

We observe data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ). In the linear regression model, it is assumed that _x_ 1 _, . . . , xn_ are fixed deterministic values, and that the response values _y_ 1 _, . . . , yn_ satisfy the model equation:


Another way of writing the model is:


There are three parameters in this model: _β_ 0 _, β_ 1 and _σ_<sup>2</sup> .

In Bayesian inference, the first step is to select a prior for the unknown parameters _β_ 0 _, β_ 1 _, σ_ . A reasonable prior reflecting ignorance is


for a large number _C_ (the exact value of _C_ will not matter in the following calculations). Note that as _σ_ is always positive, we have made the uniform assumption on log _σ_ (by the change of variable formula, the density of _σ_ would be given by _fσ_ ( _x_ ) = _f_ log _σ_ (log _x_ ) _x_<sup><u>1</u>=</sup> _I{−C<_ 2 _Cx_ log _x<C}_ =<sup>_I{e−C_</sup> 2<sup>_<x<e_</sup> _Cx_<sup>_C_</sup><sup>_<u>}</u>_</sup> .

The joint posterior for all the unknown parameters _β_ 0 _, β_ 1 _, σ_ is then given by (below we write the term “data” for _y_ 1 _, . . . , yn_ ):


The two terms on the right hand side above are the likelihood:


and the prior:


1

We thus obtain


The above is the joint posterior over _β_ 0 _, β_ 1 _, σ_ . The posterior over only the main parameters _β_ 0 _, β_ 1 can be obtained by integrating (or marginalizing) the parameter _σ_ .


When _C_ is large, the above integral can be evaluated from 0 to _∞_ which gives


The change of variable

allows us to write the integral as


The posterior density of ( _β_ 0 _, β_ 1) is thus


Using the notation

we write


In most regression problems, the least squares criterion _S_ ( _β_ 0 _, β_ 1) will take large values (for example, in the US population dataset, the smallest possible value of _S_ ( _β_ 0 _, β_ 1) is of the order of billions). This would mean that <u>1</u> would be very small for all values of _β_ 0 _, β_ 1 � _S_ ( _β_ 0 _,β_ 1) � _n/_ 2 (of course, the normalizing constant in front of (1) would then have to be quite large). In order to not deal with such small values, it makes sense to rewrite the posterior density as:


2

Note that (1) and (2) represent exactly the same density because the term ( _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1))<sup>_n/_2</sup> does not depend on _β_ 0 _, β_ 1 and is thus a constant.

Generally, the density (2) will be quite sharply concentrated around the least squares estimator ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1) especially when _n_ is large. This is because, when ( _β_ 0 _, β_ 1) is such that _S_ ( _β_ 0 _, β_ 1) is large compared to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1), the quantity


would be quite negligible because of the large power _n/_ 2. As a result, the posterior density _fβ_ 0 _,β_ 1 _|_ data( _β_ 0 _, β_ 1) will be concentrated around those values of ( _β_ 0 _, β_ 1) for which _S_ ( _β_ 0 _, β_ 1) is quite close to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). For example, suppose _n_ = 791 (as in the US population dataset), and that ( _β_ 0 _, β_ 1) is such that _S_ ( _β_ 0 _, β_ 1) = (1 _._ 1) _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). Then


Such ( _β_ 0 _, β_ 1) will thus get negligible posterior probability. Even for ( _β_ 0 _, β_ 1) such that _S_ ( _β_ 0 _, β_ 1) = (1 _._ 01) _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1), we have


and so such ( _β_ 0 _, β_ 1) will also get fairly small posterior probability.

To sum up, when _n_ is large, the posterior probability will be concentrated around those ( _β_ 0 _, β_ 1) for which _S_ ( _β_ 0 _, β_ 1) is very close to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). Generally, this would imply that ( _β_ 0 _, β_ 1) would itself have to be close to ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). For this reason, the indicator term in (2) has no effect when _C_ is large. From now on, we shall drop this indicator term and refer to the Bayesian posterior as simply


A more precise understanding of the posterior density can be obtained by noting its connection to the multivariate _t_ -density. Before looking at this connection, let us briefly recall _t_ -densities.

---

[Up: contents](index.md) · [1.1 t -densities →](02-1-1-t--densities.md)
