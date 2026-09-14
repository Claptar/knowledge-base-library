---
title: 5.1. L´evy’s characterization
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.1. L´evy’s characterization

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let


denote a _d_ -dimensional process, and let


denote its filtration. It follows immediately from the property of stationary independent increments that if ( _Bt_ ) is a Brownian motion, then

(i) ( _Bt_<sup>(</sup><sup>_i_))isan(</sup><sup>_Ft_)martingalewithcontinuouspaths,foreach</sup><sup>_i_;</sup> (ii) ( _Bt_<sup>(</sup><sup>_i_)</sup><sup>_B_</sup> _t_<sup>(</sup><sup>_j_))isan(</sup><sup>_Ft_)martingalefor1</sup><sup>_≤i < j≤d_;</sup> (iii) (( _Bt_<sup>(</sup><sup>_i_))2</sup><sup>_−t_))isan(</sup><sup>_Ft_)martingaleforeach1</sup><sup>_≤i ≤d_</sup>

It is an important result, due to L´evy, that if a _d_ -dimensional process ( _Bt_ ) has these three properties relative to the filtration ( _Ft_ ) that it generates, then ( _Bt_ ) is a Brownian motion. Note how a strong conclusion regarding the distribution of the process is deduced from what appears to be a much weaker collection of martingale properties. Note also that continuity of paths is essential: if ( _Bt_ ) is

_J. Pitman and M. Yor/Guide to Brownian motion_

22

any process with stationary independent increments such that E( _B_ 1) = 0 and E( _B_ 1<sup>2) = 1,forinstance</sup><sup>_Bt_:=</sup><sup>_Nt−t_where</sup><sup>_N_isaPoissonprocesswithrate1,</sup> then both ( _Bt_ ) and ( _Bt_<sup>2</sup><sup>_−t_)aremartingales.</sup>

More generally, if a process ( _Bt_ ) has the above three properties relative to some filtration ( _Ft_ ) with


then it can be concluded that ( _Bt_ ) is an ( _Ft_ ) _Brownian motion_ , meaning that ( _Bt_ ) is a Brownian motion and that for all 0 _≤ s ≤ t_ the increment _Bt − Bs_ is independent of _Fs_ .

---

[← 5. BM as a martingale](38-5-bm-as-a-martingale.md) · [Up: contents](index.md) · [5.2. Itˆo’s formula →](40-5-2-itˆo-s-formula.md)
