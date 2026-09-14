---
title: 3 ARMA( p , q ) models
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyTwo153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyTwo153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 ARMA( p , q ) models

**Source:** [`LectureTwentyTwo153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyTwo153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The combination of ideas behind the AR and MA models are generalized to obtain ARMA models. The ARMA(p, q) model is defined by the equation:


i.i.d where, as usual, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). The unknown parameters in this model are _µ, ϕ_ 1 _, . . . , ϕp, θ_ 1 _, . . . , θq_ and the noise standard deviation _σ_ . In Backshift notation, we can write


where _ϕ_ ( _B_ ) and _θ_ ( _B_ ) are the AR and MA polynomials:


applied to the Backshift operator _B_ .

It can be shown that if the AR polynomial _ϕ_ ( _z_ ) has all roots with modulus strictly larger than 1, then the ARMA(p, q) difference equation has a stationary and causal solution. This solution can be written in the form:


These coefficients _{ψj}_ can be explicitly determined in terms of _ϕ_ 1 _, . . . , ϕp_ and _θ_ 1 _, . . . , θq_ by solving the equation: _ψ_ ( _z_ ) = _θ_ ( _z_ ) _/ϕ_ ( _z_ ) (here _ψ_ ( _z_ ) := _ψ_ 0 + _ψ_ 1 _z_ + _ψ_ 2 _z_<sup>2</sup> + _. . ._ ) which can be done by writing


and then equating the coefficients of _z_<sup>_j_</sup> on both sides for _j_ = 0 _,_ 1 _, . . ._ to get


5

ARMA(p, q) models generalize both AR(p) and MA(q) models. When _p_ = _q_ = 0 (i.e., when _ϕ_ ( _z_ ) = 1 and _θ_ ( _z_ ) = 1), we obtain the white noise model. When _p_ = 0 (i.e., when _ϕ_ ( _z_ ) = 1), we get the MA(q) model. When _q_ = 0 (i.e., when _θ_ ( _z_ ) = 1), we get the AR(p) model.

The ACF and PACF functions of causal stationary ARMA(p, q) models when both _p_ and _q_ are nonzero are more complicated compared to those of AR(p) and MA(q) models. In particular, neither the ACF nor the PACF cuts off after a certain lag for ARMA(p, q) models with both _p, q ≥_ 1.

---

[← 2 AR( p )](02-2-ar-p.md) · [Up: contents](index.md) · [4 Additional Optional Reading →](04-4-additional-optional-reading.md)
