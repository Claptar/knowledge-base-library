---
title: Ideas used in Lecture 9.
source: https://www.stat.berkeley.edu/~aldous/150/lecture_10_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_10_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Ideas used in Lecture 9.

**Source:** [`lecture_10_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_10_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

If _µ_ ( _t_ ) (the distribution of _X_ ( _t_ )) converges to a limit distribution _π_ , then the limit _π_ must be a stationary distribution and (mean proportion of time at _i_ before _t_ ) _→ πi_ .


Theorem about existence and formula for stationary distribution. Current material treated in sections 4.3, 4.4 of [PK].

Before continuing, some reminders about the distinction between random variables and probability distributions, and the difference between convergence of random variables and convergence of probability distributions.

David Aldous

Lecture 10


Given a random variable _X_ , its distribution describes the probabilities of the possible values;


_X_ die throw; _π_ 1 = 1 _/_ 6 _, π_ 2 = 1 _/_ 6 _, . . . , π_ 6 = 1 _/_ 6


_Z_ standard Normal(0 _,_ 1): density function _φ_ ( _z_ ) or distribution function Φ( _z_ ).

If _X_ 1 and _X_ 2 are independent dice throws then they have the same distribution. But P( _X_ 1 = _X_ 2) = 1 _/_ 6, so they are not the same random variable.


Two random variables _X_ and _Y_ are regarded as “the same” if P( _X_ = _Y_ ) = 1.

David Aldous

Lecture 10


“Convergence in distribution” of random variables means “convergence of their distributions”. For real-valued random variables this is illustrated by the central limit theorem.

For i.i.d. ( _ξi_ ) with mean _θ_ and variance _σ_<sup>2</sup> ,


for standard Normal _Z_ .. The “convergence in distribution” symbol _→d_ here means

P( _S_<sup>¯</sup> _n ≤ z_ ) _→_ P( _Z ≤ z_ ) = Φ( _z_ ) for each _−∞ < z < ∞._

David Aldous Lecture 10


In a more advanced course there are several related notions of “convergence of random variables”. Given ( _X_ 1 _, X_ 2 _, . . ._ ) and also _X∞_ then (going back to the formal math set-up, where a RV is a function from a sample space Ωto a range space, here R) there is an event


which has some probability. We say


to mean P( _Xn → X∞_ as _n →∞_ ) = 1. Here ”a.s.” is an abbreviation for ”almost surely”. Note that _X∞_ might be a constant. As a basic example, the “law of averages” can be formalized as the **strong law of large numbers** : _For i.i.d._ ( _ξi_ ) _with mean θ,_


David Aldous Lecture 10


Recall _Ti_ = min _{t ≥_ 0 : _Xt_ = _i}_ and define also the **return time**


Fix a reference state _b_ .

Theorem _Suppose irreducible. (a) If state space is finite then_ E _bTb_<sup>+</sup><sup>_< ∞._</sup> _(b) Suppose_ E _bTb_<sup>+</sup><sup>_< ∞.Define_</sup> _Tb_<sup>+</sup> _a_ ( _b, i_ ) = E _b_ � **1** ( _X_ ( _s_ )= _i_ ) _s_ =1 = _mean number of visits to i before returning to b. So a_ ( _b, b_ ) = 1 _. Then πi_ =<sup>_a_</sup><sup><u>(</u></sup><sup>_b, i_</sup><sup><u>)</u></sup> E _bTb_<sup>+</sup>


_is a stationary distribution, and is the_ **only** _stationary distribution._


David Aldous Lecture 10

---

[Up: contents](index.md) · [Discussion. →](02-discussion.md)
