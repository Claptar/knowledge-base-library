---
title: 8.4. Self-intersections
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8.4. Self-intersections

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In a series of remarkable papers in the 1950’s, Dvoretsky, Erd˝os, Kakutani and Taylor established among other things the existence of multiple points of arbitary (even infinite) order in planar Brownian paths. It was not until the 1970’s that any attempt was made to quantify the extent of self-intersection of Brownian paths by consideration of the occupation measure of Brownian increments


for a planar Brownian motion _B_ , and _x ∈_ R<sup>2</sup> . Wolpert [447] and Rosen [374] showed that this random measure is almost surely absolutely continuous with respect to Lebsesgue measure on R<sup>2</sup> , with a density


which can be chosen to be jointly continuous in ( _x, s, t_ ). For fixed _x_ this process in _s, t_ is called the the process of _intersection local times at x_ . However,

_x_ lim _→_ 0<sup>_α_˜(</sup><sup>_x_;</sup><sup>_s, t_) =</sup><sup>_∞_almostsurely</sup>

_J. Pitman and M. Yor/Guide to Brownian motion_

53

reflecting the accumulation of immediate intersections of the Brownian path with itself coming from times _u, v_ in (105) with _u_ close to _v_ . A measure of the extent of such self-intersections is obtained by consideration of


as _n →∞_ with _fn_ ( _x_ ) := _n_<sup>2</sup> _f_ ( _nx_ ) for a continuous non-negative function _f_ with compact support and planar Lebesgue integral equal to 1. Varadhan [422] showed that


in every _L_<sup>_p_</sup> space for some limit _γs,t_ which is independent of _f_ . Indeed,


in _L_<sup>2</sup> . The limit process ( _γs,t, s, t ≥_ 0) is known to admit a continuous version in ( _s, t_ ), called the _renormalized self-intersection local time_ of planar Brownian motion. Rosen [375] obtained variants of Tanaka’s formula for these local times of intersection.

These results have been extended in a number of ways. In particular, for each _k >_ 2 the occupation measure of Brownian increments of order _k −_ 1


is absolutely continuous with respect to the Lebesgue measure _dx_ 2 _· · · dxk_ , and Varadhan’s renormalization result extends as follows: the multiple integrals


where _X_ := _X −_ E( _X_ ), converge in _L_<sup>_p_</sup> for every _p ≥_ 1 as _n →∞_ , to define a _k_ th order renormalized intersection local time. Amongst a number of deep applications of these intersection local times, we mention the asymptotic series expansion of the area of the _Wiener sausage_


according to which for each fixed _n_ = 1 _,_ 2 _, . . ._ , as _ϵ →_ 0


where _γk_ ( _t_ ) is the _k_ th order normalized intersection local time. These results, and much more in the same vein, can be found in the course of Le Gall [263]. Subsequent open problems were collected in [102].

_J. Pitman and M. Yor/Guide to Brownian motion_

54

Questions about self-intersection of planar Brownian paths are closely related to questions about intersections of two or more independent Brownian paths. Such questions are easier, because a process _L_<sup>(1</sup> _t,s_<sup>_,_2)</sup> of local time of intersection at 0 between two independent Brownian paths ( _Bu_<sup>(1)</sup><sup>_,_0</sup><sup>_≤u ≤t_)and(</sup><sup>_B_</sup> _v_<sup>(2)</sup><sup>_,_0</sup><sup>_≤_</sup> _v ≤ s_ ) is well-defined and finite. Le Gall’s proof of Varadhan’s renormalization uses the convergence of a centered sequence of such local times of intersection _L_<sup>(1</sup><sup>_,_2)</sup> .

---

[← The Kallianpur-Robbins law [203]](77-the-kallianpur-robbins-law-203.md) · [Up: contents](index.md) · [8.5. Exponents of non-intersection →](79-8-5-exponents-of-non-intersection.md)
