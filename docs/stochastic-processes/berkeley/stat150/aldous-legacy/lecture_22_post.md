---
title: Lecture 22 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_22_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_22_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 22 — post

**Source:** [`lecture_22_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_22_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 22 David Aldous


19 October 2015

David Aldous

Lecture 22


In continuous time 0 _≤ t < ∞_ we specify transition **rates**


or informally

P( _X_ ( _t_ + _dt_ ) = _j|X_ ( _t_ ) = _i_ ) = _qij dt_

but note these are defined only for _j̸_ = _i_ . The time- _t_ distribution _π_ ( _t_ ) evolves as


where **Q** is the matrix with off-diagonal entries ( _qij_ ) and with diagonal entries defined by


David Aldous Lecture 22


# **Birth-and-death chains.**

These have states _{_ 0 _,_ 1 _,_ 2 _, . . . , N}_ or _{_ 0 _,_ 1 _,_ 2 _, . . . . . .}_ and the only transitions are _i → i ±_ 1. Write


For these chains we can solve the detailed balance equations: [board]


So the stationary distribution is


provided (in the infinite-state case) _w < ∞_ .

**Example.** Take _λi_ = _λ, µi_ = _µi_ . Then [board] _π_ is the Poisson( _λ/µ_ ) distribution.

David Aldous Lecture 22


**Example.** Take _λi_ = _λ, µi_ = _µ, λ < µ_ . Then [board] _π_ is the shifted Geometric ( _p_ = 1 _− λ/µ_ ) distribution.

This is the M/M/1 queue model, as follows.


Customers arrive at times of a rate- _λ_ Poisson point process Service times are IID Exponential( _µ_ ). _X_ ( _t_ ) = number of customers at time _t_ ,

We can calculate many quantities associated with the stationary process [board]


Long-run proportion of time server is idle = 1 _− λ/µ_ .

Mean number of customers = _<u>λ</u> µ−λ_<sup>.</sup>

Mean waiting time (until starting service) for customer = _µ_<sup>_λ_</sup> _−_<sup>_<u>/µ</u>_</sup> _λ_<sup>.</sup> Mean total time (until ending service) for customer = _µ−_ <u>1</u> _λ_<sup>.</sup> Mean busy period for server = _µ−_ <u>1</u> _λ_<sup>.</sup>

David Aldous

Lecture 22


**More theory – similar to discrete-time setting.** [Assume chain is irreducible, and either finite-state or infinite state and positive-recurrent, so a unique stationary distribution _π_ exists.] For any initial distribution, P( _X_ ( _t_ ) = _i_ ) _→ πi_ as _t →∞_ . Writing _Ni_ ( _t_ ) = length of time chain spends in state _i_ during [0 _, t_ ], we have _Ni_ ( _t_ ) _/t → πi_ as _t →∞_ . E _i Ti_<sup>+</sup> = 1 _/_ ( _πi qi_ ), where _Ti_<sup>+</sup> is the first **return time** to _i_ (after leaving _i_ ).

Note we don’t need “aperiodic” in the first result. The third result can be seen by a general “cycle argument” [next slide and board].

David Aldous Lecture 22


**Example: repairman model** ([PK] Problem 6.4.3.)


- 5 machines – each is working or “failing” (not working) A working machine fails at rate _α_ = 0 _._ 2


- 1 repairman; a repair takes random Exponential(rate _β_ = 0 _._ 5) time Study _X_ ( _t_ ) =number of machines working at time _t_ .

[board]

David Aldous Lecture 22


Note that if the stationary distribution _π_ exists for an infinite-state birth-and-death process, then for the same process on states _{_ 0 _,_ 1 _,_ 2 _, . . . , N}_ the stationary distribution is


In other words, taking _π_ as the distribution of a RV _Z_ , _π_<sup>[</sup><sup>_N_]</sup> is the conditional distribution of _Z_ given _{Z ≤ N}_ .

David Aldous Lecture 22

---

[Up: contents](index.md)
