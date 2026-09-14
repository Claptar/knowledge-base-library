---
title: 6.2. Occupation times and local times
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6.2. Occupation times and local times

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For _f_ ( _x_ ) = 1( _x ∈ A_ ) for a Borel set _A_ the integral


represents the amount of time that the Brownian path has spent in _A_ up to time _T_ , which might be either fixed or random. As _f_ varies, this integral functional defines a random measure on the range of the path of _B_ , the _random occupation measure_ of _B_ on [0 _, T_ ]. A basic technique for finding the distribution of the

_J. Pitman and M. Yor/Guide to Brownian motion_

40

integral functional (72) is provided by the method of Feynman-Kac, which is discussed in most textbooks on Brownian motion. Few explicit formulas are known, except in dimension one. A well known application of the Feynman-Kac formula is Kac’s derivation of L´evy ’s arcsine law for _B_ a BM(R), that is for all fixed times _T_


See for instance [313] for a recent account of this approach, and Watanabe [430] for various generalizations to one-dimensional diffusion processes and random walks. Other generalizations of L´evy’s arcsine law for occupation times were developed by Lamperti [247] and Barlow, Pitman and Yor [10], [354]. See also [67] [68]. See Bingham and Doney [48] and Desbois [96] regarding higherdimensional analogues of the arc-sine law, and Desbois [95] [18] for occupation times for Brownian motion on a graph.

It was shown by Trotter [418] that almost surely the random occupation measure induced by the sample path of a one dimensional Brownian motion _B_ = ( _Bt, t ≥_ 0) admits a jointly continuous local time process ( _L_<sup>_x_</sup> _t_<sup>(</sup><sup>_B_);</sup><sup>_x∈_</sup> R _, t ≥_ 0) satisfying the _occupation density formula_


See [295, 221, 370] for proofs of this. Immediately from (74) there is the almost sure approximation


which was used by L´evy to define the process ( _L_<sup>_x_</sup> _t_<sup>_, t ≥_0) for each fixed</sup><sup>_x_. Other</sup> such approximations, also due to L´evy, are


where _D_ [ _x, x_ + _ϵ, B, t_ ] is the number of downcrossings of the interval [ _x, x_ + _ϵ_ ] by _B_ up to time _t_ , and


where _N_ [ _x, ϵ, B, t_ ] is derived from the random closed level set _Zx_ := _{s_ : _Bs_ = _x}_ as the number component intervals of [0 _, t_ ] _\ Zx_ whose length exceeds _ϵ_ . See [370, Prop. XII.(2.9)]. According to Taylor and Wendel [416] and Perkins [341], the local time _L_<sup>_x_</sup> _t_<sup>isalsotherandomHausdorff</sup><sup>_ℓ_-measureof</sup><sup>_Zx∩_[0</sup><sup>_, t_]for</sup> _ℓ_ ( _v_ ) = (2 _v|_ log _|_ log _v||_ )<sup>1</sup><sup>_/_2</sup> .

_J. Pitman and M. Yor/Guide to Brownian motion_

41

---

[← 6.1. Hitting times and extremes](61-6-1-hitting-times-and-extremes.md) · [Up: contents](index.md) · [6.2.1. Reflecting Brownian motion →](63-6-2-1-reflecting-brownian-motion.md)
