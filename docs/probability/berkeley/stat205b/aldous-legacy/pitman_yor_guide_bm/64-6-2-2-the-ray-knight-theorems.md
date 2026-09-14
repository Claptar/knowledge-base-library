---
title: 6.2.2. The Ray-Knight theorems
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6.2.2. The Ray-Knight theorems

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This subsection is an abbreviated form the account of the Ray-Knight theorems in [349, _§_ 8]. Throughout this section let _R_ denote a reflecting Brownian motion on [0 _, ∞_ ), which according to L´evy’s theorem (78) may be constructed from a standard Brownian motion _B_ either as _R_ = _|B|_ , or as _R_ = _B −_ _<u>B</u>_ <u>.</u> Note that if _R_ = _|B|_ then for _v ≥_ 0 the occupation density of _R_ at level _v_ up to time _t_ is


For 0 _≤ v < w_ let

_D_ ( _v, w, t_ ) := number of downcrossings of [ _v, w_ ] by _R_ before _t_

Then there is the following basic description of the process counting downcrossings of intervals up to an inverse local time [321]. See also [426] for more about Brownian downcrossings and their relation to the Ray-Knight theorems.

The process


is a time-homogeneous Markovian birth and death process on _{_ 0 _,_ 1 _,_ 2 _. . .}_ , with state 0 absorbing, transition rates


for _n_ = 1 _,_ 2 _, . . ._ , and initial state _D_ (0 _, ε, τℓ_ ) which has Poisson( _ℓ/_ (2 _ε_ )) distribution.

In more detail, the number _D_ ( _v, v_ + _ε, τℓ_ ) is the number of branches at level _v_ in a critical binary (0 _, ε_ ) branching process started with a Poisson( _ℓ/_ (2 _ε_ ))

42

_J. Pitman and M. Yor/Guide to Brownian motion_

number of initial individuals. From the Poisson distribution of _D_ (0 _, ε, τℓ_ ), and the law of large numbers,


and similarly, for each _v >_ 0 and _ℓ>_ 0, by consideration of excursions of _R_ away from level _v_


This process (2 _εD_ ( _v, v_ + _ε, τℓ_ ) _, v ≥_ 0), which serves as an approximation to ( _L_<sup>_v_</sup> _τℓ_<sup>(</sup><sup>_R_)</sup><sup>_, v≥_0),isaMarkovchainwhosestatespaceisthesetofintegermulti-</sup> ples of 2 _ε_ , with transition rates


for _x_ = 2 _εn >_ 0. The generator _Gε_ of this Markov chain acts on smooth functions _f_ on (0 _, ∞_ ) according to


Hence, appealing to a suitable approximation of diffusions by Markov chains [239, 238], we obtain the following _Ray-Knight theorem_ (Ray [365], Knight [220]): For each fixed _ℓ>_ 0, and _τℓ_ := inf _{t_ : _L_<sup>0</sup> _t_<sup>(</sup><sup>_R_)</sup><sup>_> ℓ}_,where</sup><sup>_R_=</sup><sup>_|B|_,</sup>


where ( _Xℓ,v_<sup>(</sup><sup>_δ_)</sup><sup>_, v≥_0)for</sup><sup>_δ≥_0denotesasquaredBesselprocessofdimension</sup> _δ_ started at _ℓ ≥_ 0, as in Section 4.4.2. Moreover, if _Tℓ_ := _τ_ 2 _ℓ_ := inf _{t >_ 0 : _L_<sup>0</sup> _t_<sup>(</sup><sup>_B_)=</sup><sup>_ℓ}_,thetheprocesses(</sup><sup>_Lv_</sup> _Tℓ_<sup>(</sup><sup>_B_)</sup><sup>_, v≥_0)and(</sup><sup>_L−_</sup> _Tℓ_<sup>_v_(</sup><sup>_B_)</sup><sup>_, v≥_0)aretwo</sup> independent copies of ( _Xℓ,v_<sup>(0)</sup><sup>_, v≥_0).ThesquaredBesselprocessesandtheir</sup> bridges, especially for _δ_ = 0 _,_ 2 _,_ 4, are involved in the description of the local time processes of numerous Brownian path fragments [220, 365, 437, 350]. For instance, if _T_ 1 := inf _{t_ : _Bt_ = 1 _}_ , then according to Ray and Knight


Many proofs, variations and extensions of these basic Ray-Knight theorems can be found in the literature. See for instance [212, 370, 348, 426, 190] and papers cited there. The appearance of squared Bessel processes processes embedded in

_J. Pitman and M. Yor/Guide to Brownian motion_

43

the local times of Brownian motion is best understood in terms of the construction of these processes as weak limits of Galton-Watson branching processes with immigration, and their consequent interpretation as continuous state branching processes with immigration [212]. For instance, there is the following expression of the L´evy-Itˆo representation of squared Bessel processes, and its interpretation in terms of Brownian excursions [350], due to Le Gall-Yor [257]: For _R_ a reflecting Brownian motion on [0 _, ∞_ ), with _R_ 0 = 0, let


Then for _δ >_ 0 the process of ultimate local times of _Y_<sup>(</sup><sup>_δ_)</sup> is a squared Bessel process of dimension _δ_ started at 0:


See [349, _§_ 8] for further discussion of these results and their explanation in terms of random trees embedded in Brownian excursions.

---

[← 6.2.1. Reflecting Brownian motion](63-6-2-1-reflecting-brownian-motion.md) · [Up: contents](index.md) · [6.3. Additive functionals →](65-6-3-additive-functionals.md)
