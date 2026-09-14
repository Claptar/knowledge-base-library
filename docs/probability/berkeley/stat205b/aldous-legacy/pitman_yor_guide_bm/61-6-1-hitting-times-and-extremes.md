---
title: 6.1. Hitting times and extremes
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6.1. Hitting times and extremes

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

For _x ∈_ R, let _Tx_ := inf _{t_ : _t ≥_ 0 _, Bt_ = _x}_ . Then for _a, b >_ 0, by optional sampling,


and hence


Let


and notice that ( _Tx, x ≥_ 0) is the left continuous inverse for ( _Mt, t ≥_ 0). Since ( _Mt ≥ x_ ) = ( _Tx ≤ t_ ), if we know the distribution of _Mt_ for all _t >_ 0 then we know the distribution of _Tx_ for all _x >_ 0. Define the reflected path,


39

_J. Pitman and M. Yor/Guide to Brownian motion_

By the Strong Markov Property and the fact that _B_ and _−B_ are equal in distribution we can deduce the _reflection principle_ that _B_<sup>ˆ</sup> and _B_ are equal in distribution: _B_<sup>ˆ</sup> = _d B_ . Rigorous proof of this involves some measurability issues: see e.g. Freedman [139, _§_ 1.3] Durrett [106] for details. Observe that for _x, y >_ 0,


so


Taking _y_ = 0 in the previous expression we have


But ( _Bt > x_ ) _⊂_ ( _Mt ≥ x_ ), so


by continuity of the distribution. Adding these two results we find that


So the distributions of _Mt_ and _|Bt|_ are the same: _Mt_ = _d |Bt|_ . Now recall that P<sup>0</sup> ( _Mt ≥ x_ ) = P<sup>0</sup> ( _Tx ≤ t_ ) so


So _Tx_ = _d Bx_<sup>2</sup> 1<sup>2. As a check, this implies</sup><sup>_Tx_</sup> = _d x_ 2 _T_ 1, which is explained by Brownian scaling.

The joint distribution of the minimum, maximum and final value of _B_ on an interval can be obtained by repeated reflections. See e.g. [46] and [40, _§_ 4.1] for related results involving the extremes of Brownian bridge and excursion. See also [57] for corresponding results up to various random times.

---

[← 6. Brownian functionals](60-6-brownian-functionals.md) · [Up: contents](index.md) · [6.2. Occupation times and local times →](62-6-2-occupation-times-and-local-times.md)
