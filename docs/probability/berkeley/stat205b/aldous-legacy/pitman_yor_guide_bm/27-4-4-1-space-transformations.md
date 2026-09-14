---
title: 4.4.1. Space transformations
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.4.1. Space transformations

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The simplest means of transformation of a Markov process _X_ with state space ( _E, E_ ) is to consider the distribution of the process (Φ( _Xt_ ) _, t ≥_ 0) for a suitable measurable Φ : _E → E_<sup>_′_</sup> for some ( _E_<sup>_′_</sup> _, E_<sup>_′_</sup> ). Typically, such a transformation destroys the Markov property, unless Φ respects some symmetry in the dynamics of _X_ , as follows [372, I (14.1)]. Suppose that Φ maps _E_ onto _E_<sup>_′_</sup> , and that for each _x ∈E_ the _Pt_ ( _x, ·_ ) distribution of Φ depends only on Φ( _x_ ), so that


for some family of Markov kernels ( _Qt, t ≥_ 0) on ( _E_<sup>_′_</sup> _, E_<sup>_′_</sup> ). Assuming for simplicity that _X_ has continuous paths, that Φ is continuous, and that P<sup>_x_</sup> governs _X_ with

_J. Pitman and M. Yor/Guide to Brownian motion_

17

semigroup ( _Pt_ ) with _X_ 0 = _x_ . Then the P<sup>_x_</sup> distribution of (Φ( _Xt_ ) _, t ≥_ 0) is that of a Markov process with semigroup ( _Qt_ ) and initial state Φ( _x_ ). Refer to Dynkin [110], Rogers-Williams [372], Rogers and Pitman [371] Glove and Mitro [154]. Let Q<sup>_y_</sup> for _y ∈E_<sup>_′_</sup> denote the common distribution of this process on _C_ ([0 _, ∞_ ) _, E_<sup>_′_</sup> ) for all _x_ with Φ( _x_ ) = _y_ . Then (Q<sup>_y_</sup> _, y ∈ E_<sup>_′_</sup> ) defines the collection of laws on _C_ ([0 _, ∞_ ) _, E_<sup>_′_</sup> ) of the canonical Markov process with semigroup ( _Qt, t ≥_ 0). Following is a well known example.

---

[← 4.4. Transformations](26-4-4-transformations.md) · [Up: contents](index.md) · [4.4.2. Bessel processes →](28-4-4-2-bessel-processes.md)
