---
title: 5.6.1. Change of probability
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.6.1. Change of probability

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The assumption is that the underlying probability P is replaced by Q defined on by


meaning that every non negative _Ft_ -measurable trandom variable _Xt_ has Q- expectation


This definition is consistent as _t_ -varies, and defines a probability distribution on the entire path space, if and only if ( _Dt, t ≥_ 0) is an ( _Ft,_ P) martingale. Then, Girsanov’s theorem [370, Ch. VIII] states that


with ( _B_<sup>˜</sup> _t_ ) an (( _Ft_ ) _,_ Q) Brownian motion. In the first instance, ( _B_<sup>˜</sup> _t_ ) is just identified as an (( _Ft_ ) _,_ Q) local martingale. But _⟨B_<sup>˜</sup> _⟩_ = _⟨B⟩t_ = _t_ , and hence ( _B_<sup>˜</sup> _t_ ) is an (( _Ft_ ) _,_ Q) Brownian motion, by L´evy’s theorem.

This application of Girsanov’s theorem has a number of important consequences for Brownian motion. In particular, for each _f ∈ L_<sup>2</sup> loc<sup>(R+</sup><sup>_, ds_)thelaw</sup> Q<sup>(</sup><sup>_f_)</sup> of the process


is locally equivalent to the law P of BM, with the density relation


_J. Pitman and M. Yor/Guide to Brownian motion_

33

where the density factor is


In other words, the Wiener measure _P_ is quasi-invariant under translations by functions _F_ in the _Cameron-Martin space_ , that is


As a typical application of the general Girsanov formula (65), the law P<sup>_λ_</sup> _x_<sup>ofthe</sup> Ornstein-Uhlenbeck process of Section **??** is found to satisfy


where the formula<sup><u>1</u></sup> 2<sup>(</sup><sup>_B_</sup> _t_<sup>2</sup><sup>_−x_2) =</sup> �0 _t_<sup>_BsdBs_hasbeenused.</sup> Girsanov’s formula can also be applied to study the bridge of length _T_ defined by starting a diffusion process _X_ started at some point _x_ at time 0, and conditioning on arrival at _y_ at time _T_ . Then, more or less by definition [132], for 0 _< s < T_


where _pt_ ( _x, y_ ) is the transition density for the diffusion. In particular, for _X_ a Brownian bridge of length _T_ from (0 _, x_ ) to ( _T, y_ ) we learn from Girsanov’s formula that


This discussion generalizes easily to a _d_ -dimensional Brownian motion, and to other Markov processes. See e.g. [410, _§_ 6.2.2].

---

[← 5.6. Transformations of Brownian motion](50-5-6-transformations-of-brownian-motion.md) · [Up: contents](index.md) · [5.6.2. Change of filtration →](52-5-6-2-change-of-filtration.md)
