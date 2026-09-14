---
title: 5. BM as a martingale
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5. BM as a martingale

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let ( _Ft, t ≥_ 0) be a filtration in a probability space (Ω _, F,_ P). A process _M_ = ( _Mt_ ) is called an ( _Ft_ ) _martingale_ if

1. _Mt_ is _Ft_ measurable for each _t ≥_ 0 _._

2. E( _Mt|Fs_ ) = _Ms_ for all 0 _≤ s ≤ t_ .

Implicitly here, to make sense of the conditional expectation, it is assumed that E _|Mt| < ∞_ . It is known that if the filtration ( _Ft_ ) is right continuous, i.e. _Ft_<sup>+</sup> = _Ft_ up to null sets, then every martingale has a version which has right continuous paths (even with left limits). See [370].

_J. Pitman and M. Yor/Guide to Brownian motion_

21

If _B_ is a standard Brownian motion relative for a filtration ( _Ft, t ≥_ 0), meaning that _Bt_ + _s − Bt_ is independent of _Ft_ with Gaussian distribution with mean 0 and variance _s_ , for each _s, t ≥_ 0, then both ( _Bt_ ) and ( _Bt_<sup>2</sup><sup>_−t_)are(</sup><sup>_Ft_)</sup> martingales. So too is


for each _θ_ real or complex, where a process with values in the complex plane, or in R<sup>_d_</sup> for _d ≥_ 2, is called a martingale if each of its one-dimensional components is a martingale.

**Optional Stopping Theorem** If ( _Mt_ ) is a right continuous martingale relative to a right continuous filtration ( _Ft_ ), and _T_ is a stopping time for ( _Ft_ ), meaning ( _T ≤ t_ ) _∈Ft_ for each _t ≥_ 0, and _T_ is bounded, i.e., _T ≤ C < ∞_ for some constant _C_ , then


Moreover, if an ( _Ft_ ) adapted process _M_ has this property for all bounded ( _Ft_ ) stopping times _T_ , then _M_ is an ( _Ft_ ) martingale. Variations or corollaries with same setup: If _T_ is a stopping time (no bound now), then


so ( _MT ∧t, t ≥_ 0) is an ( _Ft_ )-martingale. If _T_ is a stopping time of Brownian motion _B_ with E( _T_ ) _< ∞_ , then

---

[← 4.6. References for Markov processes](37-4-6-references-for-markov-processes.md) · [Up: contents](index.md) · [5.1. L´evy’s characterization →](39-5-1-l-evy-s-characterization.md)
