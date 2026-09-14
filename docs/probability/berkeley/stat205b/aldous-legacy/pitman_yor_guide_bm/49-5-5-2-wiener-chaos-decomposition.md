---
title: 5.5.2. Wiener chaos decomposition
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.5.2. Wiener chaos decomposition

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

These representation results (58) and (59) may also be regarded as corollaries of the _Wiener chaos decomposition_ of _L_<sup>2</sup> ( _B∞_ ) as


where _Cn_ is the subspace of _L_<sup>2</sup> ( _B∞_ ) spanned by _n_ th order multiple integrals of the form


for _fn_ subject to


31

_J. Pitman and M. Yor/Guide to Brownian motion_

and 1 _≤ ij ≤ d_ for 1 _≤ j ≤ n_ . This space _Cn_ , consisting of iterated integrals obtained from _deterministic_ functions _fn_ , is called the _n_ th Wiener chaos.

To prove the martingale representation (58)-(59), it suffices to establish (59) for the random variable


for _f ∈ L_<sup>2</sup> (R+ _→_ R<sup>_d_</sup> ; _du_ ). The formula (59) now follows from Itˆo’s formula, with


Similarly, the Wiener chaos representation (63) follows by consideration of the generating function


of the Hermite polynomials _Hn_ ( _x, u_ ), using the consequence of Itˆo’s formula and ( _∂/∂x_ ) _Hn_ = _Hn−_ 1 that


We discuss in Section 6.4 some techniques for identifying the distribution of Brownian functionals in _C_ 0 � _C_ 2. It is known that if _X ∈_<sup>�</sup><sup>_n_</sup> _k_ =0<sup>_Ck_thenthereexists</sup><sup>_α >_0suchthat</sup>


and also some _α_ 0 such that for any _β > α_ 0


assuming that _X_ = _X_ 0 + _· · ·_ + _Xn_ with _Xi ∈ Ci_ and _Xn̸_ = 0. This gives some indication of the tail behaviour of distributions of various Brownian functionals Such results may be found in the book of Ledoux and Talagrand [266]. We do not know of any exact computation of the law of a non-degenerate element of _C_ 3, or of _C_ 0 � _C_ 1 � _C_ 2 � _C_ 3. We regard as “degenerate” a variable such as (�0 _∞ f_ ( _s_ ) _dBs_ )<sup>3</sup> , whose law can be found by simple transformation of the law of some element of _C_ 0 � _C_ 1 � _C_ 2.

---

[← 5.5.1. Representation as stochastic integrals](48-5-5-1-representation-as-stochastic-integrals.md) · [Up: contents](index.md) · [5.6. Transformations of Brownian motion →](50-5-6-transformations-of-brownian-motion.md)
