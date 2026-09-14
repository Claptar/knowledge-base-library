---
title: Lecture 36 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_36_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_36_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 36 — post

**Source:** [`lecture_36_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_36_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 36


David Aldous

30 November 2015

David Aldous

Lecture 36


The M/G/1 queue model is


Customers arrive at times of a rate- _λ_ Poisson point process Service times _Y_ 1 _, Y_ 2 _, . . ._ are IID.


Write _ν_ = E _Y_ and note that 1 _/ν_ is “service rate”. _X_ ( _t_ ) = number of customers at time _t_ .


1 server.

Here ( _X_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) is **not** a continuous-time Markov chain. But we can do some calculations.

David Aldous Lecture 36


Here is a third method which calculates something different. There is a **discrete-time** Markov chain associated with the M/G/1 queue: _Xn_ = number of customers just after the departure of the _n_ ’th customer. Here [board] _Xn_ +1 = max( _Xn −_ 1 _,_ 0) + _An_

_An_ = number of arrivals during next service period

and the _An_ are IID.

As a special property of the M/G/1 queue, the stationary distribution of ( _Xn_ ) is the same as the equilibrium distribution of “number of customers” in the original queue process. Using this fact we can calculate the expectation of “number of customers”.

[calculation on board – follows [PK] sec. 9.3.1].

David Aldous

Lecture 36


The M/G/ _∞_ queue model is


Customers arrive at times of a rate- _λ_ Poisson point process Service times _Y_ 1 _, Y_ 2 _, . . ._ are IID. Service starts immediately (infinite number of available servers) _X_ ( _t_ ) = number of customers at time _t_ .

Easy to analyze as follows. Customer _i_ arrives at some time _Ti_ and has some service time _Yi_ ; we can represent ( _Ti , Yi_ ) as a Poisson process in R<sup>2</sup> with rate

_λ_ ( _t, y_ ) = _λf_ ( _y_ ); _f_ ( _y_ ) is density of _Y ._

[board] Starting empty, distribution of _X_ ( _t_ ) is Poisson with mean _λ_ �0 _t_<sup>P(</sup><sup>_Y≥s_)</sup><sup>_ds_.Soin</sup><sup>_t→∞_limitthemeanis</sup><sup>_λ_E</sup><sup>_Y_.</sup>

David Aldous

Lecture 36


**Example: airport parking lot.** [not in text]

Cars arrive at (large) rate _λ_ and remain for Exponential(1) times. The numbers of parked cars form a _M/M/∞_ queue and the stationary distribution is Poisson( _λ_ ). But there is also a “spatial” aspect; imagine parking spaces numbered 1 _,_ 2 _,_ 3 _, . . ._ and each arriving car parks in the lowest-numbered empty space.

**Question:** when “you” arrive, you park in some space _U_ : what is the distribution of _U_ ?

**Answer.** Fix 0 _< u <_ 1 and consider

_Nu_ = number of empty spaces among spaces [1 _, uλ_ ] _._

This “number of empty spaces” process is approximately a _M/M/_ 1 queue with “arrival” rate _uλ_ and “service” rate _λ_ . So at stationarity


P( _U ≤ uλ_ ) = P( _Nu ≥_ 1) _≈ u,_ 0 _< u <_ 1 _._

David Aldous Lecture 36

---

[Up: contents](index.md)
