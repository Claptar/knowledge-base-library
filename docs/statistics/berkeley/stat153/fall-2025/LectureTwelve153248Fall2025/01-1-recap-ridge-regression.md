---
title: '1 Recap: Ridge Regression'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwelve153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Recap: Ridge Regression

**Source:** [`LectureTwelve153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwelve153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Our model from the last two lectures is given by:

_yt_ = _β_ 0 + _β_ 1( _t −_ 1) + _β_ 2ReLU( _t −_ 2) + _· · ·_ + _βn−_ 1ReLU( _t −_ ( _n −_ 1)) + _ϵt_ (1) i.i.d where, as always, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). Here ReLU( _t − c_ ) = ( _t − c_ )+ equals 0 if _t ≤ c_ and equals ( _t − c_ ) if _t > c_ .

The unknown parameters in this model are _β_ 0 _, β_ 1 _, . . . , βn−_ 1 as well as _σ_ .

Alternatively, (1) can be written as:


where


The ridge regression estimator _β_<sup>ˆridge</sup> ( _λ_ ) for _β_ is given by the minimizer of:


The objective function above can also be written as


1

It turns out that _β_<sup>ˆridge</sup> ( _λ_ ) can be written in closed form using matrix notation. To see this, note first that the gradient of the above objective function with respect to _β_ is given by


Let _J_ denote the _n × n_ diagonal matrix whose diagonal entries are 0 _,_ 0 _,_ 1 _, . . . ,_ 1. In other words, the first two diagonal entries of _J_ are 0 and the rest of the diagonal entries equal 1:


With this matrix, we can write


Setting this gradient equal to zero, we get


which gives

_β_ ˆ<sup>ridge</sup> ( _λ_ ) = ( _X_<sup>_T_</sup> _X_ + _λJ_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _y._ (4)

This looks very similar to the usual linear regression least squares formula ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _y_ with the only difference being the presence of the _λJ_ term.

---

[Up: contents](index.md) · [2 Bayesian Regularization →](02-2-bayesian-regularization.md)
