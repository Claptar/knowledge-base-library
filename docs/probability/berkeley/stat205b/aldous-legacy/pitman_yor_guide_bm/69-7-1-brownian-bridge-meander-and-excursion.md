---
title: 7.1. Brownian bridge, meander and excursion
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.1. Brownian bridge, meander and excursion

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To facilitate description of the random path fragment of random length, the following notation is very convenient. For a process _X_ := ( _Xt, t ∈ J_ ) parameterized by an interval _J_ , and _I_ = [ _GI , DI_ ] a random subinterval of _J_ with length _λI_ := _DI − GI >_ 0, we denote by _X_ [ _I_ ] or _X_ [ _GI , DI_ ] the _fragment of X on I_ , that is the process


We denote by _X∗_ [ _I_ ] or _X∗_ [ _GI , DI_ ] the _standardized fragment of X on I_ , defined by the _Brownian scaling operation_


_J. Pitman and M. Yor/Guide to Brownian motion_

46

Note that the fundamental invariance of Brownian motion under Brownian scaling can be stated in this notation as


for each fixed time _T >_ 0. Let _GT_ := sup _{s_ : _s ≤ T, Bs_ = 0 _}_ be the last zero of _B_ before time _T_ and _DT_ := inf _{s_ : _s > T, Bs_ = 0 _}_ be the first zero of _B_ after time _T_ . Let _|B|_ := ( _|Bt|, t ≥_ 0), called _reflecting Brownian motion_ . It is well known [180, 76, 370] that there are the following identities in distribution derived by Brownian scaling: for each fixed _T >_ 0


where _B_<sup>br</sup> is a _standard Brownian bridge_ ,


where _B_<sup>me</sup> is a _standard Brownian meander_ , and


where _B_<sup>ex</sup> is a _standard Brownian excursion_ . These identities in distribution provide a convenient unified definition of the standard bridge, meander and excursion, which arise also as limits in distribution of conditioned random walks, as discussed in Section 2. It is also known that _B_<sup>br</sup> _, B_<sup>me</sup> and _B_<sup>ex</sup> can be constructed by various other operations on the paths of _B_ , and transformed from one to another by further operations [25].

**The excursion straddling a fixed time** For each fixed _T >_ 0, the path of _B_ on [0 _, T_ ] can be reconstructed in an obvious way from the four random elements


which are independent, the first with distribution


which is one of L´evy’s arc-sine laws, the next a standard bridge, the next a standard meander, and the last a uniform random sign _±_<sup><u>1</u></sup> 2<sup>.Similarly,thepath</sup> of _B_ on [0 _, DT_ ] can be reconstructed from the four random elements


which are independent, with the joint law of ( _GT , DT_ ) given by


_J. Pitman and M. Yor/Guide to Brownian motion_

47

with _B∗_ [0 _, GT_ ] a standard bridge, _|B|∗_ [ _GT , DT_ ] a standard excursion, and sign( _BT_ ) a uniform random sign _±_<sup><u>1</u></sup> 2<sup>.See[448,Chapter7].</sup>

For 0 _< t < ∞_ let _B_<sup>br</sup><sup>_,t_</sup> be a _Brownian bridge of length t_ , which may be regarded as a random element of _C_ [0 _, t_ ] or of _C_ [0 _, ∞_ ], as convenient:


Let _B_<sup>me</sup><sup>_,t_</sup> denote a _Brownian meander of length t_ , and _B_<sup>ex</sup><sup>_,t_</sup> be a _Brownian excursion of length t_ , defined similarly to (91) with _B_<sup>me</sup> or _B_<sup>ex</sup> instead of _B_<sup>br</sup> .

**Brownian excursions and the three-dimensional Bessel process** There is a close connection between Brownian excursions and a particular time-homogeneous diffusion process _R_ 3 on [0 _, ∞_ ), commonly known as the _three-dimensional Bessel process_ BES(3), due to the representation


where the _Bi_ are three independent standard Brownian motions. It should be understood however that this particular representation of _R_ 3 is a relatively unimportant coincidence in distribution. What is more important, and can be understood entirely in terms of the random walk approximations of Brownian motion and Brownian excursion (1) and (7), is that there exists a time-homogeneous diffusion process _R_ 3 on [0 _, ∞_ ) with _R_ 3(0) = 0, which has the same self-similarity property as _B_ , meaning invariance under Brownian scaling, and which can be characterized in various ways, including (92), but most importantly as a Doob _h_ -transform of Brownian motion.

For each fixed _t >_ 0, the Brownian excursion _B_<sup>ex</sup><sup>_,t_</sup> of length _t_ is the BES(3) bridge from 0 to 0 over time _t_ , meaning that


Moreover, as _t →∞_


and _R_ 3 can be characterized in two other ways as follows:

- (i) [294, 437] The process _R_ 3 is a Brownian motion on [0 _, ∞_ ) started at 0 and conditioned never to return to 0, as defined by the Doob _h_ -transform, for the harmonic function _h_ ( _x_ ) = _x_ of Brownian motion on [0 _, ∞_ ), with absorbtion at 0. That is, _R_ 3 has continuous paths starting at 0, and for each 0 _< a < b_ the stretch of _R_ 3 between when it first hits _a_ and first hits _b_ is distributed like _B_ with _B_ 0 = _a_ conditioned to hit _b_ before 0.

- (ii) [347] There is the identity


where _B_ is a standard Brownian motion with past minimum process


48


The identity in distribution (94) admits numerous variations and conditioned forms [347, 25, 31]. For instance, by application of L´evy’s identity (78)


where ( _Lt, t ≥_ 0) is the local time process of _B_ at 0.

---

[← 7. Path decompositions and excursion theory](68-7-path-decompositions-and-excursion-theory.md) · [Up: contents](index.md) · [7.2. The Brownian zero set →](70-7-2-the-brownian-zero-set.md)
