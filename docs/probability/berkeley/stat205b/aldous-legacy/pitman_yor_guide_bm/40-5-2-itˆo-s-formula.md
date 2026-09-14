---
title: 5.2. Itˆo’s formula
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.2. Itˆo’s formula

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

It is a key observation that if _X_ is a Markov process with semigroup ( _Pt_ ), and _f_ and _g_ are bounded Borel functions with _Gf_ = _g_ , then the equality between the first and last expressions in the Chapman-Kolmogorov equation (30) can be recast as


Equivalently, by application of the Markov property,


for all _x ∈ E_ . The optional stopping theorem applied to this martingale yields _Dynkin’s formula_ , [372, _§_ 10], according to which (38) holds also for ( _Ft_ ) stopping times _T_ with E<sup>_x_</sup> ( _T_ ) _< ∞_ . If _X_ = _B_ is a one-dimensional Brownian motion, and _f ∈ Cb_<sup>2,meaningthat</sup><sup>_f_,</sup><sup>_f ′_and</sup><sup>_f ′′_areallboundedandcontinuous,then</sup> _Gf_ =<sup><u>1</u></sup> 2<sup>_f ′′_and(39)reads</sup>


To identify more explicitly the martingale _Mt_<sup>_f_appearinghere,considerasub-</sup> division of [0 _, t_ ] say


with mesh


By a second order Taylor expansion,


_J. Pitman and M. Yor/Guide to Brownian motion_

23

for some Θ _n,i_ between _Btn,i_ and _Btn,i_ +1. Since Θ _n,i_ is bounded and ( _Btn,i_ +1 _− Btn,i_ )<sup>2</sup> has mean _tn,i_ +1 _− tn,i_ and variance a constant times ( _tn,i_ +1 _− tn,i_ )<sup>2</sup> , it is easily verified that as _n →∞_ there is the following easy extension of the fact (15) that the quadratic variation of _B_ on [0 _, t_ ] equals _t_ :


while the second sum in (42) is a Riemann sum which approximates �0 _t_<sup>_f ′′_(</sup><sup>_Bs_)</sup><sup>_ds_</sup> almost surely. Consequently, the first sum must converge to the same limit in _L_<sup>2</sup> , and we learn from (41) that the martingale _Mt_<sup>_f_in(40)is</sup>


where the limit exists in the sense of convergence in probability. Thus we obtain a first version of _Itˆo’s formula_ : for _f_ which is bounded with two bounded continuous derivatives:


where the _stochastic integral_ (�0 _t_<sup>_f ′_(</sup><sup>_Bs_)</sup><sup>_dBs, t≥_0)isan(</sup><sup>_Ft_)-martingaleif</sup><sup>_B_</sup> is an ( _Ft_ )-Brownian motion. Itˆo’s formula (48), along with an accompanying theory of stochastic integration with respect to Brownian increments _dBs_ , has been extensively generalized to a theory of stochastic integration with respect to semi-martingales [370]. The closely related theory of _Stratonovich stochastic integrals_ is obtained by defining for instance


This construction has the advantage that it is better connected to geometric notions of integration, such as integration of a differential form along a continuous path [176][177][302]and there is the simple formula


However, the important martingale property of Itˆo integrals is hidden by the Stratonovich construction. See [336, Chapter 3] and [410, Chapter 8] for further comparison of Itˆo and Stratonovich integrals.

---

[← 5.1. L´evy’s characterization](39-5-1-l-evy-s-characterization.md) · [Up: contents](index.md) · [5.3. Stochastic integration →](41-5-3-stochastic-integration.md)
