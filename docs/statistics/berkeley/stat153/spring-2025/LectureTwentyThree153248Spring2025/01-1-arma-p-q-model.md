---
title: 1 ARMA( p , q ) Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyThree153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 ARMA( p , q ) Model

**Source:** [`LectureTwentyThree153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyThree153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The ARMA( _p_ , _q_ ) model is given by the equation:


i.i.d where, as usual, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). In backshift notation, this equation becomes


where _φ_ ( _B_ ) and _θ_ ( _B_ ) are the AR and MA polynomials:


applied to the backshift operator _B_ . Another way of writing (1) is:


where we now write the intercept term _δ_ explicitly on the right hand side.

We can write the solution to (1) as


To make sense of the right hand side above, we can factorize _φ_ ( _z_ ) as:


Here 1 _/a_ 1 _, . . . ,_ 1 _/ap_ are the roots of _φ_ ( _z_ ). This gives


Each term (1 _− akB_ )<sup>_−_1</sup> can be expanded via one of the following two formulae:


1

depending on whether _|ak| <_ 1 or _|ak| >_ 1. This allows us to write _yt − µ_ in terms of _{ϵt}_ . If _|ak| <_ 1 for every _k_ , we can write


for some _ψ_ 0 _, ψ_ 1 _, ψ_ 2 _, . . ._ . This is a causal stationary process. We shall only work with ARMA( _p_ , _q_ ) models in the causal stationary regime (which corresponds to _φ_ ( _z_ ) having all roots of modulus strictly larger than 1).

ARMA( _p_ , _q_ ) is a more sophisticated model compared to pure AR( _p_ ) and MA( _q_ ). For AR( _p_ ), the theoretical PACF becomes zero for lags _h > p_ . For MA( _q_ ), the theoretical ACF becomes zero for lags _h > q_ . For ARMA( _p_ , _q_ ) with both _p_ and _q_ at least one, one of these is true about the ACF and PACF. It is therefore to determine an appropriate choice for _p_ and _q_ for fitting an ARMA( _p_ , _q_ ) model looking at the ACF and PACF. In practice, one usually searches over a range of _p_ and _q_ values using a model selection criterion such as AIC, BIC or Cross-Validation.

---

[Up: contents](index.md) · [2 The Box-Jenkins Time Series Modeling Strategy →](02-2-the-box-jenkins-time-series-modeling-strategy.md)
