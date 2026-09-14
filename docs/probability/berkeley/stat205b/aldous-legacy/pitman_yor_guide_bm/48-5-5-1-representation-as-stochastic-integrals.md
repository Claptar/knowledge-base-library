---
title: 5.5.1. Representation as stochastic integrals
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.5.1. Representation as stochastic integrals

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A (local) martingale relative to the natural filtration ( _Bt, t ≥_ 0) of a _d_ -dimensional Brownian motion


is called a _Brownian (local) martingale_ . According to an important result of Itˆoand Kunita- Watanabe [237], every Brownian local martingale admits a continuous version ( _Mt, t ≥_ 0) which may be written as


30

_J. Pitman and M. Yor/Guide to Brownian motion_

for some constant _c_ and some R<sup>_d_</sup> -valued predictable process ( _ms, s ≥_ 0) such that �0 _t_<sup>_|ms|_2</sup><sup>_ds < ∞_.</sup>

In particular, every _L_<sup>2</sup> ( _B∞_ ) random variable _Y_ may be represented as


for some R<sup>_d_</sup> -valued predictable process ( _ys, s ≥_ 0) such that


Such a representing process is unique in _L_<sup>2</sup> (Ω _×_ R+ _,_ P( _B_ ) _, d_ P _ds_ ). The ClarkOcone formula [82] [329] gives some general expression for ( _ys, s ≥_ 0) in terms of _Y_ . This expression plays an important role in Malliavin calculus. See references in Section 11.3.

A class of examples of particular interest arises when


for suitably regular Φ( _t, ω, x_ ). In particular, if Φ is of bounded variation in _t_ , and sufficiently smooth in _x_ , one of Kunita’s extensions of Itˆo’s formula gives


where _∇x_ is the gradient operator with respect to _x_ . So, with the notations (58) and (59), we get, for the _L_<sup>2</sup> -martingale _Mt_ = _E_ [ _Y | Bt_ ],


See [389, 157] for some interesting examples of such computations.

---

[← 5.5. Brownian martingales](47-5-5-brownian-martingales.md) · [Up: contents](index.md) · [5.5.2. Wiener chaos decomposition →](49-5-5-2-wiener-chaos-decomposition.md)
