---
title: 8.2. Polarity of points, and windings
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8.2. Polarity of points, and windings

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

According to L´evy’s theorem,


with ( _Z_<sup>�</sup> ( _u_ ) _, u ≥_ 0) another planar BM started at 1, and _Xs_ the real part of _Zs_ . It follows immediately from (102) that _Z_<sup>�</sup> will never visit 0 almost surely. From this, it follows easily that for two arbitrary points _z_ 0 and _z_ 1 with _z_ 0 _̸_ = _z_ 1


_J. Pitman and M. Yor/Guide to Brownian motion_

51

In particular, the winding number process, that is a continuous determination ( _θt_<sup>(</sup><sup>_z_1)</sup> _, t ≥_ 0) of the argument of _Zt −z_ 1 along the path of _Z_ , is almost surely well defined for all _t ≥_ 0, and so is the corresponding complex logarithm of _Zt − z_ 1, according to the formula


for _t ≥_ 0, where, by another application of L´evy’s theorem, the process _Z_<sup>˜</sup> is a complex Brownian motion starting at 0. Moreover, from the trivial identity


considered as a linear integral equation in ( _Zu − z_ 1), we see that


Taking _z_ 1 = 0, this yields the _skew-product representation_ of the planar BM _Z_ started from _z_ 0 _̸_ = 0:


for _t ≥_ 0, where ( _γ_ ( _u_ ) _, u ≥_ 0) is a one dimensional BM, independent of the radial part ( _|Zt|, t ≥_ 0), which is by definition a 2-dimensional Bessel process. This skew-product representation reduces a number of problems involving a planar Brownian motion _Z_ to problems involving just its radial part.

---

[← 8.1. Conformal invariance](73-8-1-conformal-invariance.md) · [Up: contents](index.md) · [8.3. Asymptotic laws →](75-8-3-asymptotic-laws.md)
