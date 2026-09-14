---
title: 1 ARMA( p , q ) models
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwentyTwo153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 ARMA( p , q ) models

**Source:** [`LectureTwentyTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwentyTwo153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The ARMA( _p_ , _q_ ) model is defined by the equation:


i.i.d where, as usual, _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ). The unknown parameters in this model are _µ, φ_ 1 _, . . . , φp, θ_ 1 _, . . . , θq_ and the noise standard deviation _σ_ .

An equivalent way of writing (1) is by moving the _µ_ terms to the right hand side. This gives:


In other words,


where _φ_ 0 = _µ_ (1 _− φ_ 1 _−· · · − φp_ ) and _ηt_ = _ϵt_ + _θ_ 1 _ϵt−_ 1 + _· · ·_ + _θqϵt−q_ . In this sense, ARMA( _p_ , _q_ ) can be seen as an AR( _p_ ) model where the error terms are modeled as MA( _q_ ) instead of i.i.d Gaussian _N_ (0 _, σ_<sup>2</sup> ).

AR( _p_ ) and MA( _q_ ) models are special cases of ARMA( _p_ , _q_ ) because:

1. When _p_ = 0, the equation (1) becomes:


which is the MA( _q_ ) model. So ARMA(0, _q_ ) = MA( _q_ ).

2. When _q_ = 0, the equation (2) becomes:


which is the AR( _p_ ) equation with _φ_ 0 = _µ_ (1 _− φ_ 1 _−· · · − φp_ ). Thus ARMA( _p_ , 0) = AR( _p_ ).

In Backshift notation, we can write


1

where _φ_ ( _B_ ) and _θ_ ( _B_ ) are the AR and MA polynomials:


applied to the Backshift operator _B_ .

We can rewrite (4) as


To make sense of the right hand side above, we can factorize _φ_ ( _z_ ) as:


Here 1 _/a_ 1 _, . . . ,_ 1 _/ap_ are the roots of _φ_ ( _z_ ). This gives


Suppose each _|ak| <_ 1 (in other words, every root of _φ_ ( _z_ ) has modulus strictly larger than 1), then each term (1 _− akB_ )<sup>_−_1</sup> can be expanded as follows:


This allows us to write _yt − µ_ in terms of _{ϵt}_ :


for some _ψ_ 0 _, ψ_ 1 _, ψ_ 2 _, . . ._ . This is a causal stationary process. We shall only work with ARMA( _p_ , _q_ ) models in the causal stationary regime (which corresponds to _φ_ ( _z_ ) having all roots of modulus strictly larger than 1).

Therefor if the AR polynomial _φ_ ( _z_ ) has all roots with modulus strictly larger than 1, then the ARMA( _p_ , _q_ ) difference equation has a stationary and causal solution:


These coefficients _{ψj}_ can be explicitly determined in terms of _φ_ 1 _, . . . , φp_ and _θ_ 1 _, . . . , θq_ by solving the equation: _ψ_ ( _z_ ) = _θ_ ( _z_ ) _/φ_ ( _z_ ) (here _ψ_ ( _z_ ) := _ψ_ 0 + _ψ_ 1 _z_ + _ψ_ 2 _z_<sup>2</sup> + _. . ._ ) which can be done by writing

_θ_ ( _z_ ) = 1 + _θ_ 1 _z_ + _· · ·_ + _θqz_<sup>_q_</sup> = _φ_ ( _z_ ) _× ψ_ ( _z_ ) = (1 _− φ_ 1 _z −· · · − φpz_<sup>_p_</sup> ) � _ψ_ 0 + _ψ_ 1 _z_ + _ψ_ 2 _z_<sup>2</sup> + _. . ._ �

and then equating the coefficients of _z_<sup>_j_</sup> on both sides for _j_ = 0 _,_ 1 _, . . ._ to get


Note that the condition for ARMA( _p_ , _q_ ) to have a causal stationary solution is identical to the condition for AR( _p_ ) to have a causal stationary solution (namely, every root of the polynomial _φ_ ( _z_ ) should have modulus strictly larger than 1).

2

---

[Up: contents](index.md) · [2 ACF and PACF of ARMA( p , q ) models →](02-2-acf-and-pacf-of-arma-p-q-models.md)
