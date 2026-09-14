---
title: 3.4. Brownian bridges
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.4. Brownian bridges

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

It is useful to define, as explicitly as possible, a family of _Brownian bridges {_ ( _Bu_<sup>_x,y,T_</sup> _,_ 0 _≤ u ≤ T_ ) _, x, y ∈_ R _}_ distributed like a Brownian motion ( _Bu,_ 0 _≤ u ≤ T_ ) conditioned on _B_ 0 = _x_ and _BT_ = _y_ . To see how to do this, assume first that _x_ = 0, and write


Observe that each of the random variables _Bu −_ ( _u/T_ ) _BT_ is orthogonal to _BT_ , and hence the process ( _Bu −_ ( _u/T_ ) _BT ,_ 0 _≤ u ≤ T_ ) is independent of _BT_ . It follows that the desired family of bridges can be constructed from an unconditioned Brownian Motion _B_ with _B_ 0 = 0 as

_Bu_<sup>_x,y,T_</sup> = _x_ + _Bu −_ ( _u/T_ ) _BT_ + ( _u/T_ )( _y − x_ ) = _x_ + _u_ ( _y − x_ ) + _√TB_<sup>br</sup> ( _u/T_ ) for 0 _≤ u ≤ T, x, y ∈_ R, where _B_<sup>br</sup> is the _standard Brownian bridge_ as in (4).

---

[← 3.3. Paley-Wiener integrals](12-3-3-paley-wiener-integrals.md) · [Up: contents](index.md) · [3.5. Fine structure of Brownian paths →](14-3-5-fine-structure-of-brownian-paths.md)
