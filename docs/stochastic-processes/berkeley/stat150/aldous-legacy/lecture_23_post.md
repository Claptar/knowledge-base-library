---
title: Lecture 23 — post
source: https://www.stat.berkeley.edu/~aldous/150/lecture_23_post.pdf
source_file: sources/berkeley-stat150/aldous-legacy/lecture_23_post.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Lecture 23 — post

**Source:** [`lecture_23_post.pdf`](https://www.stat.berkeley.edu/~aldous/150/lecture_23_post.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Lecture 23


David Aldous

21 October 2015

David Aldous

Lecture 23


**Renewal processes.** I will talk about only a very little of the material in [PK] Chapter 7.

Mental picture: light bulbs have random lifetime _X_ , and we replace at failure. So successive bulbs have IID lifetimes _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ and we can consider


_Wn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_=timeof</sup><sup>_i_’th</sup><sup>**renewal**</sup> _N_ ( _t_ ) = max _{n_ : _Wn ≤ t}_ = number of renewals before _t_ .

If _X_ has Exponential( _λ_ ) distribution then the renewals form a rate- _λ_ Poisson point process, but here we allow a general distribution for _X_ . Write _µ_ = E _X_ . The law of large numbers says that as _n →∞_


It is intuitively clear that we can rewrite this “upside down”: on average we must replace a bulb every _µ_ time units, that is at average rate 1 _/µ_ per unit time, so


David Aldous Lecture 23


We can rewrite this in terms of the **rate** of renewals at _t_ . That is, defining _λ_ ( _t_ ) _dt_ = P( some renewal in [ _t, t_ + _dt_ ]) we have _λ_ ( _t_ ) _→_ 1 _/µ_ as _t →∞_ .

Here is the first “interesting” result about renewal processes. The following are defined relative to a time _t_ [board] _δt_ = _t − WN_ ( _t_ ) = time since last renewal before _t γt_ = _WN_ ( _t_ )+1 _− t_ = time until first renewal after _t βt_ = _δt_ + _γt_ = length of inter-renewal interval containing _t_ . Recall _µ_ = E _X_ and write _F_ ( _x_ ) = P( _X ≤ x_ ) and _fX_ ( _x_ ) for its density function.

Theorem


_As t →∞ the joint distribution_ ( _δt, γt_ ) _converges to the distribution of_ ( _δ, γ_ ) _defined by the joint density_

_fδ,γ_ ( _a, c_ ) = _fX_ ( _a_ + _c_ ) _/µ._


David Aldous Lecture 23


As _t →∞_ the joint distribution ( _δt, γt_ ) converges to the distribution of ( _δ, γ_ ) defined by the joint density


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

From this we can work out the marginal density of _γ_


For _δ_ we get the same result


For _β_ we get


This is the “size-biased” distribution arising from _X_ , discussed in a different setting in Lecture 2. [next slide]

David Aldous Lecture 23


_X_ = number of children in a uniform random family _X_ � =number of children in the family of a uniform randomly picked child.


_N_ = number of families.

We calculate


Number of families with _i_ children = _N_ P( _X_ = _i_ )


Say _X_<sup>�</sup> has the **size-biased** distribution of _X_ .

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

In the light bulb (renewal theory) setting this is an explanation of the **inspection paradox;** the mean total lifetime E _β_ of the bulb in use at a given time is larger than the mean lifetime E _X_ of a typical bulb.

David Aldous Lecture 23


The **cycle trick** mentioned in previous lectures is part of renewal theory. Suppose there are IID rewards _Ri_ associated with renewals – precisely, the pairs ( _X_ 1 _, R_ 1) _,_ ( _X_ 2 _, R_ 2) _, . . ._ are IID. Then

long-run average reward per unit time = E _R/_ E _X_ .

**Example: scheduling replacements before failure.** In many examples other than light bulbs (e.g. car battery), the cost _C_ 1 of replacement before failure is less than the cost _C_ 2 of replacement at failure. So we can consider a policy:

_replace at (random) failure time X or at (fixed) time T, whichever comes first._

What is the optimal choice of _T_ ? Replace at time _X_<sup>_∗_</sup> = min( _X , T_ )


Incur cost _C_ = _C_ 2 if _X < T_ , or cost _C_ = _C_ 1 if _X > T_ .

Long-run average cost per unit time = E _C /_ E _X_<sup>_∗_</sup> .

David Aldous Lecture 23


Replace at time _X_<sup>_∗_</sup> = min( _X , T_ ) Incur cost _C_ = _C_ 2 if _X < T_ , or cost _C_ = _C_ 1 if _X > T_ . Long-run average cost per unit time = E _C /_ E _X_<sup>_∗_</sup> .

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

We need to write these quantities in terms of _F_ ( _x_ ) = P( _X ≤ x_ ) and the associated density function _f_ ( _x_ ).


We could now use calculus or numerics to find the value of _T_ which minimizes E _C /_ E _X_<sup>_∗_</sup> .

David Aldous Lecture 23


The IID central limit theorem (CLT) says


We expect a corresponding CLT for the renewal counting process _N_ ( _t_ ): for some “unknown” _q_


But the events _{Wn > t}_ and _{N_ ( _t_ ) _< n}_ are the same, and this enables us to calculate _q_ [board] by considering _n_ and _t_ related by


David Aldous Lecture 23


So we get

and then indeed


David Aldous Lecture 23

---

[Up: contents](index.md)
