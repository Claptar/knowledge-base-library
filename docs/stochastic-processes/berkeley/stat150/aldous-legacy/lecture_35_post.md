---
title: Lecture 35 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_35_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_35_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 35 — post

**Source:** [`lecture_35_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_35_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 35


David Aldous

23 November 2015

David Aldous

Lecture 35


The M/G/1 queue model is


Customers arrive at times of a rate- _λ_ Poisson point process Service times _Y_ 1 _, Y_ 2 _, . . ._ are IID.


Write _ν_ = E _Y_ and note that 1 _/ν_ is “service rate”. _X_ ( _t_ ) = number of customers at time _t_ .


1 server.

Here ( _X_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) is **not** a continuous-time Markov chain. But we can do some calculations.

David Aldous Lecture 35


**Idle and busy periods.** The server alternates idle and busy periods – lengths _I_ 1 _, B_ 1 _, I_ 2 _, B_ 2 _, . . ._ . We know E _I_ 1 = 1 _/λ_ . How do we calculate E _B_ 1? **Method 1.** Recall the **cycle trick** . Write _T_ 1 _, T_ 2 _, . . ._ for the times between successive “renewals”, suppose there is a “reward” _Ri_ associated with the renewal interval _Ti_ , and suppose the sequence of pairs ( _Ti , Ri_ ) _, i_ = 1 _,_ 2 _, . . ._ is IID. Then

long-run average reward per unit time = E _R/_ E _T_ . To use this, write _Ti_ = _Ii_ + _Bi_ and _Ri_ = _Bi_ . So long-run average proportion of time server is busy = E _B_ 1 _/_ (E _I_ 1 + E _B_ 1). Demand for service per unit time = _λ ×_ E _Y_ = proportion of time server is busy. So


We solve to get


David Aldous Lecture 35


**Method 2.** Consider _N_<sup>_∗_</sup> = number of arrivals during a service period and argue [board]

E( _B_ 1 _|N_<sup>_∗_</sup> = _n_ ) = _ν_ + _n_ E _B_ 1 _._ Then [board] E _B_ 1 = _ν_ + (E _N_<sup>_∗_</sup> ) E _B_ 1 which we can solve to get


Then


and so


David Aldous Lecture 35


Here is a third method which calculates something different. There is a **discrete-time** Markov chain associated with the M/G/1 queue: _Xn_ = number of customers just after the departure of the _n_ ’th customer. Here [board] _Xn_ +1 = max( _Xn −_ 1 _,_ 0) + _An_

_An_ = number of arrivals during next service period

and the _An_ are IID.

As a special property of the M/G/1 queue, the stationary distribution of ( _Xn_ ) is the same as the equilibrium distribution of “number of customers” in the original queue process. Using this fact we can calculate the expectation of “number of customers”.

[calculation on board – follows [PK] sec. 9.3.1].

David Aldous

Lecture 35

---

[Up: contents](index.md)
