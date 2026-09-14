---
title: 3. BM as a Gaussian process
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3. BM as a Gaussian process

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A _Gaussian process_ with index set _I_ is a collection of random variables ( _Xt, t ∈ I_ ), defined on a common probability space (Ω _, F,_ P), such that every finite linear combination of these variables<sup>�</sup> _i_<sup>_aiXt_</sup> _i_<sup>has a Gaussian distribution. The</sup> finite-dimensional distributions of a Gaussian process ( _Xt, t ∈ I_ ) are uniquely determined by the mean function _t →_ E( _Xt_ ), which can be arbitrary, and the covariance function ( _s, t_ ) _→_ E( _XsXt_ ) _−_ E( _Xs_ )E( _Xt_ ), which must be symmetric and non-negative definite. A Gaussian process is called _centered_ if E( _Xt_ ) _≡_ 0. Immediately from the definition of Brownian motion, there is the following characterization: a real valued process ( _Bt, t ≥_ 0) is a Brownian motion starting from 0 iff

(a) ( _Bt_ ) is a centered Gaussian process with covariance function


(b) with probability one, _t → Bt_ is continuous.

Note that for a centered process _B_ , formula (10) is equivalent to


The existence of Brownian motion can be deduced from Kolmogorov’s general criterion [372, Theorem (25.2)] for existence of a continuous version of a stochastic process. Specialized to a centered Gaussian process ( _Xt, t ∈_ R<sup>_n_</sup> ), this shows that a sufficient condition for existence of a continuous version is that E( _XsXt_ ) should be locally H¨older continuous [372, Corollary (25.6)].

_J. Pitman and M. Yor/Guide to Brownian motion_

8

---

[← 2. BM as a limit of random walks](08-2-bm-as-a-limit-of-random-walks.md) · [Up: contents](index.md) · [3.1. Elementary transformations →](10-3-1-elementary-transformations.md)
