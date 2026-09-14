---
title: 4.4.2. Bessel processes
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.4.2. Bessel processes

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let _Bt_ = ( _Bt_<sup>(</sup><sup>_i_)</sup><sup>_,_1</sup><sup>_≤i≤δ_)bea</sup><sup>_δ_-dimensionalBrownianmotionforsomefixed</sup> positive integer _δ_ . Let


be the radial part of ( _Bt_ ). If ( _Bt_ ) is started at _x ∈_ R<sup>_δ_</sup> , and _Ox,y_ is an orthogonal linear transformation of R<sup>_δ_</sup> which maps _x_ to _y_ , with _|Ox,y_ ( _z_ ) _|_ = _|z|_ for all _z ∈_ R<sup>_δ_</sup> , then ( _Ox,y_ ( _Bt_ )) is a Brownian motion starting at _y_ whose radial part is pathwise identical to the radial part of ( _Bt_ ). It follows immediately from this observation that ( _Rt_<sup>(</sup><sup>_δ_)</sup><sup>_, t ≥_0)given</sup><sup>_B_0with</sup><sup>_|B_0</sup><sup>_|_=</sup><sup>_r_definesaMarkovprocess,</sup> the _δ-dimensional Bessel process_ , with initial state _r_ and transition semigroup ( _Qt_ ) on [0 _, ∞_ ) which can be defined via (64) by integration of the Brownian transition density function over spheres in R<sup>_δ_</sup> . That gives an explicit formula for the transition density of the Bessel semigroup in terms of Bessel functions [370, p. 446]. Since the generator of _B_ acting on smooth functions is the half of the _δ_ -dimensional Laplacian


it is clear that the generator of the _δ_ -dimensional Bessel process, acting on smooth functions with domain [0 _, ∞_ ) which vanish in a neighbourhood of 0, must be half of the radial part of the Laplacian, that is


In dimensions _δ ≥_ 2, it is known [370, Ch. XI] that this action of the generator uniquely determines the Bessel semigroup ( _Qt_ ), essentially because when started away from 0 the Bessel process never reaches 0 in finite time, though in two dimensions it approaches 0 arbitrarily closely at large times.

In dimension one, the process ( _|Bt|, t ≥_ 0) is called _reflecting Brownian motion_ . It is obvious, and consistent with the vanishing drift term in formula (36) for _δ_ = 1, that the reflecting Brownian motion started at _x >_ 0 is indistinguishable from ordinary Brownian motion up until the random time _T_ 0 that the path

_J. Pitman and M. Yor/Guide to Brownian motion_

18

first hits 0. In dimension one, the expression (36) for the infinitesimal generator must be supplemented by a _boundary condition_ to distinguish the reflecting motion from various other motions with the same dynamics on (0 _, ∞_ ), but different behaviour once they hit 0. See Harrison [165] for further treatment of reflecting Brownian motion and its applications to stochastic flow systems. See also R. Williams [445] regarding semimartingale reflecting Brownian motions in an orthant, and Harrison [166] for a broader view of Brownian networks.

The theory of Bessel processes is often simplified by consideration of the _squared Bessel process of dimension δ_ which for _δ_ = 1 _,_ 2 _, . . ._ is simply the square of the norm of a _δ_ -dimensional Brownian motion:


This family of processes enjoys the key _additivity property_ that if _X_<sup>(</sup><sup>_δ_)</sup> and _X_<sup>(</sup><sup>_δ′_)</sup> are two independent squared Bessel processes of dimensions _δ_ and _δ_<sup>_′_</sup> , started at values _x, x_<sup>_′_</sup> _≥_ 0, then _X_<sup>(</sup><sup>_δ_)</sup> + _X_<sup>(</sup><sup>_δ′_)</sup> is a squared processes of dimension _δ_ + _δ_<sup>_′_</sup> , started at _x_ + _x_<sup>_′_</sup> . As shown by Shiga and Watanabe [387], this property can be used to extend the definition of the squared Bessel process to arbitrary non-negative real values of the parameter _δ_ . The resulting process is then a Markovian diffusion on [0 _, ∞_ ) with generator acting on smooth functions of _x >_ 0 according to


meaning that the process when at level _x_ behaves like a Brownian motion with drift _δ_ and variance parameter 4 _x_ . See [370] and [458, _§_ 3.2] for further details. For _δ_ = 0 this is the _Feller diffusion_ [126], which is the continuous state branching process obtained as a scaling limit of critical Galton-Watson branching processes in discrete time. Similarly, the squared Bessel process of dimension _δ ≥_ 0 may be interpreted as a continuous state branching process immigration rate _δ_ . See [212], [246], [245], [276]. See also [155] for a survey and some generalizations of Bessel processes, including the Cox-Ingersoll-Ross diffusions which are of interest in mathematical finance.

---

[← 4.4.1. Space transformations](27-4-4-1-space-transformations.md) · [Up: contents](index.md) · [4.4.3. The Ornstein-Uhlenbeck process →](29-4-4-3-the-ornstein-uhlenbeck-process.md)
