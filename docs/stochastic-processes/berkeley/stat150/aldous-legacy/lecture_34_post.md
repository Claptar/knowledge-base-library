---
title: Lecture 34 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_34_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_34_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 34 — post

**Source:** [`lecture_34_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_34_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 34


David Aldous

20 November 2015

David Aldous

Lecture 34


[from Lecture 22] Continuous-time **Birth-and-death chains.**

These have states _{_ 0 _,_ 1 _,_ 2 _, . . . , N}_ or _{_ 0 _,_ 1 _,_ 2 _, . . . . . .}_ and the only transitions are _i → i ±_ 1. Write


For these chains we can solve the detailed balance equations:


So the stationary distribution is


provided (in the infinite-state case) _w < ∞_ .

David Aldous Lecture 34


[from Lecture 22]

**Example.** Take _λi_ = _λ, µi_ = _µ, λ < µ_ . Then the stationary distribution _π_ is the shifted Geometric ( _p_ = 1 _− λ/µ_ ) distribution. This is the M/M/1 queue model, as follows.


Customers arrive at times of a rate- _λ_ Poisson point process Service times are IID Exponential( _µ_ ). _X_ ( _t_ ) = number of customers at time _t_ . 1 server.

We can calculate many quantities associated with the stationary process: Long-run proportion of time server is idle = 1 _− λ/µ_ . Mean number of customers = _<u>λ</u> µ−λ_<sup>.</sup>


Mean waiting time (until starting service) for customer = _µ_<sup>_λ_</sup> _−_<sup>_<u>/µ</u>_</sup> _λ_<sup>.</sup> Mean total time (until ending service) for customer = _µ−_ <u>1</u> _λ_<sup>.</sup>

Mean busy period for server = _µ−_ <u>1</u> _λ_<sup>.</sup>

David Aldous

Lecture 34


We implicitly assumed the rule for “order of service” is **first-in first-out – FIFO** but the results above do not depend on this rule. Changing the rule to “last-in first-out” would change other aspects such as “distribution of time in system”.

Many more complicated queue models have been studied – we will look at a few of them. First here is a

**General principle.** For a system in equilibrium (stationary distribution)

_L_ = _λW ,_ where

_λ_ = arrival rate = E (number of arriving customers per unit time). _W_ = average time in system per customer.

_L_ = average number of customers in the system.

[board]

David Aldous

Lecture 34


The M/M/s queue model has _s_ servers instead of 1 server. But with a single waiting line.


Customers arrive at times of a rate- _λ_ Poisson point process Service times are IID Exponential( _µ_ ). _X_ ( _t_ ) = number of customers at time _t_ .


_s_ servers.

Here _X_ ( _t_ ) is again a continuous-time Markov chain but with transition rates


Now the stationary distribution is [board]


provided _λ < sµ_ .

David Aldous

Lecture 34


**General principle.** In a queueing system, the **traffic intensity** _ρ_ is defined as (arrival rate) / (maximum service rate). So for M/M/s _ρ_ = _λ/_ ( _sµ_ )

A system will be stable (has a stationary distribution) if _ρ <_ 1, but unstable (length of queue _→∞_ ) if _ρ >_ 1.

David Aldous Lecture 34


We can calculate the same quantities for M/M/s as we did for M/M/1. A trick that makes the calculation simpler is to write the tail of the stationary distribution of _X_ (number of customers) as


where _G_ has shifted Geometric( _p_ = 1 _− µ_<sup>_<u>λ</u>_</sup> _s_<sup>)distribution.</sup>

Another trick is that the argument for our first general principle _L_ = _λW_ also shows


where

_W_ 0 = average **waiting** time per customer _L_ 0 = average number of customers **waiting** in the system.

[calculation on board]

David Aldous

Lecture 34


We get a formula for _W_ = average time in M/M/s system per customer.


Note we can calculate P( _X ≥ s_ ) in terms of _w_ or _π_ 0.

David Aldous Lecture 34

---

[Up: contents](index.md)
