---
title: Lecture 16 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_16_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_16_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 16 — post

**Source:** [`lecture_16_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_16_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 16


David Aldous

5 October 2015

David Aldous

Lecture 16


Notation for studying random times (of events) over 0 _≤ t < ∞_ . Cannot have two events at the same time.


_Wk_ = time at which _k_ ’th event occurs ( _W_ 0 = 0). _Sk_ = _Wk − Wk−_ 1 is the time between successive events.


_N_ ( _t_ ) = number of events during time [0 _, t_ ]. _N_ ( _s, t_ ) = _N_ ( _t_ ) _− N_ ( _s_ ) = number of events during ( _s, t_ ].

Note that the event _{Wn ≤ t}_ is the same as the event _{N_ ( _t_ ) _≥ n}_ . So, regardless of the probability model,


We will study the mathematically simplest probability model. Fix a parameter 0 _< λ < ∞_ .

David Aldous

Lecture 16


David Aldous Lecture 16


**Poisson point process (PPP) of rate** _λ_ **.**

This process is defined by the properties (a) _N_ ( _s, t_ ) has Poisson( _λ_ ( _t − s_ )) distribution. (b) For disjoint intervals ( _s_ 1 _, t_ 1) _,_ ( _s_ 2 _, t_ 2) _, . . . ,_ ( _sk , tk_ ) the random variables _N_ ( _s_ 1 _, t_ 1) _, N_ ( _s_ 2 _, t_ 2) _, . . . , N_ ( _sk , tk_ ) are independent. Why does such a process exist? Consider large _M_ , and suppose events could only happen at times _M_ <u>1</u><sup>_,_</sup> _M_<sup><u>2</u></sup><sup>_,_</sup> _M_<sup><u>3</u></sup><sup>_, . . ._,independentlywithprobability</sup> _λ/M_ . Then the number of events during ( _s, t_ ) is almost Binomial( _M_ ( _t − s_ ) _, λ/M_ ). We picture the PPP as the _M →∞_ limit, and the Poisson distribution arises as limit of Binomials.

A more informal description in terms of infinitesimal intervals is (a’) P( event during [ _t, t_ + _dt_ ]) = _λ dt_ (b’) What happens in disjoint time intervals is independent. **Conceptual point;** “Poisson” is not an arbitrary assumption, but instead arises automatically from (a’,b’). Also _λ_ is a “rate”: the mean number of events per unit time.

David Aldous Lecture 16


The PPP is used as an over-simplified model for events that occur at “completely random” times


accidents


coincidences


start of phone calls (from phone company viewpoint)


customer joining supermarket checkout line (from the supermarket viewpoint)


earthquakes


murders

For many of these examples we know that in fact the rates vary with time. But we can adapt the model to allow a time-varying rate function _λ_ ( _t_ ).

David Aldous

Lecture 16


# **The PPP with rate function** _λ_ ( _t_ ) **.**

- Start with the informal description in terms of infinitesimal intervals: (a’) P( event during [ _t, t_ + _dt_ ]) = _λ_ ( _t_ ) _dt_

- (b’) What happens in disjoint time intervals is independent.

We can then deduce the other description. Write Λ( _t_ ) = �0 _t_<sup>_λ_(</sup><sup>_u_)</sup><sup>_du_.</sup>

(a) _N_ ( _s, t_ ) has Poisson(Λ( _t_ ) _−_ Λ( _s_ )) distribution. (b) For disjoint intervals ( _s_ 1 _, t_ 1) _,_ ( _s_ 2 _, t_ 2) _, . . . ,_ ( _sk , tk_ ) the random variables _N_ ( _s_ 1 _, t_ 1) _, N_ ( _s_ 2 _, t_ 2) _, . . . , N_ ( _sk , tk_ ) are independent. We will see details later. For now, the **mathematical** point is that we can deduce results for the “rate function _λ_ ( _t_ )” case from results for the “constant rate _λ_ ” case, so we can set up theory in the constant rate case. A **modeling** point is that any process of random events has some mean rate function _λ_ ( _t_ ) – what is special about the Poisson process is the independence property. Is this approximately true in a given example?

David Aldous Lecture 16


**Poisson point process (PPP) of rate** _λ_ defined by the properties (a) _N_ ( _s, t_ ) has Poisson( _λ_ ( _t − s_ )) distribution. (b) For disjoint intervals ( _s_ 1 _, t_ 1) _,_ ( _s_ 2 _, t_ 2) _, . . . ,_ ( _sk , tk_ ) the random variables _N_ ( _s_ 1 _, t_ 1) _, N_ ( _s_ 2 _, t_ 2) _, . . . , N_ ( _sk , tk_ ) are independent. In this model we will consider _Wk_ = time at which _k_ ’th event occurs ( _W_ 0 = 0). _Sk_ = _Wk − Wk−_ 1 is the time between successive events.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

The first results are [board] _W_ 1 has Exponential( _λ_ ) distribution _Wk_ has Gamma( _λ, k_ ) distribution:


_S_ 1 _, S_ 2 _, S_ 3 _, . . ._ are IID Exponential( _λ_ ).

David Aldous Lecture 16


Note that we can use the fact

_S_ 1 _, S_ 2 _, S_ 3 _, . . ._ are IID Exponential( _λ_ )

as a (mathematical) construction of the PPP, or as an easy way to simulate the process.

Here is the next result.

Theorem


_Fix t >_ 0 _and k ≥_ 1 _. Conditional on {N_ ( _t_ ) = _k} the times_ ( _W_ 1 _, W_ 2 _, . . . , Wk_ ) _of events in the PPP are distributed as the order statistics of k IID Uniform_ (0 _, t_ ) _random variables._


[board]

The same result holds if instead we condition on _{Wk_ +1 = _t}_ .

David Aldous Lecture 16

---

[Up: contents](index.md)
