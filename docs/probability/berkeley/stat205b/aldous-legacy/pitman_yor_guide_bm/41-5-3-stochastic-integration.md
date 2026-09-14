---
title: 5.3. Stochastic integration
source: https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/pitman_yor_guide_bm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5.3. Stochastic integration

**Source:** [`pitman_yor_guide_bm.pdf`](https://www.stat.berkeley.edu/~aldous/205B/pitman_yor_guide_bm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The theory of stochastic integration defines integration of suitable random integrands _f_ ( _t, ω_ ) with respect to random “measures” _dXt_ ( _ω_ ) derived from suitable

_J. Pitman and M. Yor/Guide to Brownian motion_

24

stochastic processes ( _Xt_ ). The principal definitions in this theory, of _local martingales_ and _semimartingales_ , are motivated by a powerful calculus, known as _stochastic_ or _Itˆo_ calculus, which allows the representation of various functionals of such processes as stochastic integrals. For instance, the formula (48) can be justified for _f_ ( _x_ ) = _x_<sup>2</sup> to identify the martingale _Bt_<sup>2</sup><sup>_−t_as a stochastic integral:</sup>


Similarly, the previous derivation of formula (43) is easily extended to a Brownian motion _B_ in R<sup>_δ_</sup> for _δ_ = 1 _,_ 2 _,_ 3 _, . . ._ to show that for _f ∈ C_<sup>2</sup> (R<sup>_δ_</sup> )


with _∇_ the gradient operator and ∆the Laplacian. Again, the stochastic integral is obtained as a limit in probability of Riemann sums, along with the Itˆo formula, and the stochastic integral is a martingale in _t_ .

It is instructive to study carefully what happens in Itˆo’s formula (48) for _δ ≥_ 2 if we take _f_ to be a radial harmonic function with a pole at 0, say


and


these functions being solutions on R<sup>_δ_</sup> _−{_ 0 _}_ of _Laplace’s equation_ ∆ _f_ = 0, so the last term in (48) vanishes. Provided _B_ 0 = _x̸_ = 0 the remaining stochastic integral is a well-defined almost sure limit of Riemann sums, and moreover _f_ ( _Bt_ ) is integrable, and even square integrable for _δ ≥_ 3. It is tempting to jump to the conclusion that ( _f_ ( _Bt_ ) _, t ≥_ 0) is a martingale. But this is not the case. Indeed, it is quite easy to compute E<sup>_x_</sup> _f_ ( _Bt_ ) in these examples, and to check for example that this function of _t_ is strictly decreasing for _δ ≥_ 3. For _δ_ = 3, according to a relation discussed further in Section 7.1, E<sup>_x_</sup> (1 _/|Bt|_ ) equals the probability that a one-dimensional Brownian motion started at _|x|_ has not visited 0 before time _t_ . The process ( _f_ ( _Bt_ ) _, t ≥_ 0) in these examples is not a martingale but rather a _local martingale_ .

Let _X_ be a real-valued process, and assume for simplicity that _X_ has continous paths and _X_ 0 = _x_ 0 for some fixed _x_ 0. Such a process _X_ is called a _local martingale_ relative to a filtration ( _Ft_ ) if for each _n_ = 1 _,_ 2 _, . . ._ , the stopped process


for some sequence of stopping times _Tn_ increasing to _∞_ , which can be taken without loss of generality to be _Tn_ := inf _{t_ : _|Xt| > n}._ For any of the processes ( _f_ ( _Bt_ ) _, t ≥_ 0) considered above for a harmonic function _f_ with a pole at 0, these processes stopped when they first hit _±n_ are martingales, by consideration of Itˆo’s formula (48) for a _C_<sup>2</sup> function _f_<sup>ˆ</sup> which agrees with _f_ where _f_ has values

_J. Pitman and M. Yor/Guide to Brownian motion_

25

in [ _−n, n_ ], and is modified elsewhere to be _C_<sup>2</sup> on all of R<sup>_δ_</sup> . Consideration of these martingales obtained by stopping processes is very useful, because by application of the optional sampling theorem they immediately yield formulae for hitting probabilities of the radial part of _B_ in R<sup>_δ_</sup> , as discussed in [372, I.18]. A _continuous semimartingale X_ is the sum of a continuous local martingale and a process with continous paths of locally bounded variation.

Given a filtration ( _Ft_ ), a process _H_ of the form


for an increasing sequence of stopping times _Ti_ , and _Hi_ an _FTi_ measurable random variable, is called an _elementary predictable process_ . If _B_ is an ( _Ft_ ) Brownian motion, and _H_ is such an elementary predictable process, one can define


and check the identity


which allows the definition (49) to be extended by completion in _L_<sup>2</sup> to any pointwise limit _H_ of elementary predictable processes such that


for each _t >_ 0, and the identity (50) then holds for such a limit process _H_ . Replacing _H_ ( _s, ω_ ) by _H_ ( _s, ω_ )1( _s ≤ T_ ( _ω_ )), it follows that both


define ( _Ft_ ) martingales.

A similar stochastic integral, with _B_ replaced by an ( _Ft_ ) martingale or even a local martingale _M_ , is obtained hand in hand with the existence of an increasing process _⟨M ⟩_ such that


and the above discussion (49) -(50) -(51) -(52) generalizes straightforwardly with _dMs_ instead of _dBs_ and _d⟨M ⟩s_ instead of _ds_ . In particular, there is then the formula


_J. Pitman and M. Yor/Guide to Brownian motion_

26

of which (53) is the special case for _M_ = _B_ . See e.g. Yor [450] and Lenglart [268] for details of this approach to Itˆo’s formula for continuous semimartingales.

Let _M_ be a continuous ( _Ft_ ) local martingale and _A_ an ( _Ft_ ) adapted continuous process of locally bounded variation. Then for suitably regular functions _f_ = _f_ ( _m, a_ ) there is the following form of Itˆo’s formula for semimartingales:


where


Note that the first integral on the right side of (53) defines a local martingale, and that the sum of the second and third integrals is a process of locally bounded variation. It is the third integral, involving the second derivative _fm,m_ , which is the special feature of Itˆo calculus.

More generally, for a vector of _d_ local martingales _M_ = ( _M_<sup>(</sup><sup>_i_)</sup> _,_ 1 _≤ i ≤ d_ ), and a process _A_ of locally bounded variation, Itˆo’s formula reads


where for two local martingales _M_<sup>(</sup><sup>_i_)</sup> and _M_<sup>(</sup><sup>_j_)</sup> , their _bracket ⟨M_<sup>(</sup><sup>_i_)</sup> _, M_<sup>(</sup><sup>_j_)</sup> _⟩_ is the unique continuous process _C_ with bounded variation such that _Mt_<sup>(</sup><sup>_i_)</sup><sup>_M_(</sup> _t_<sup>_j_)</sup> _− Ct_ is a local martingale. See Section 12.1 for connections between Itˆo’s formula and various second order partial differential equations.

---

[← 5.2. Itˆo’s formula](40-5-2-itˆo-s-formula.md) · [Up: contents](index.md) · [5.4. Construction of Markov processes →](42-5-4-construction-of-markov-processes.md)
