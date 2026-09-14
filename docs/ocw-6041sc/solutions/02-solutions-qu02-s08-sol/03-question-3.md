---
title: Question 3
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-qu02-s08-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 3

**Source:** `solutions/02-solutions-qu02-s08-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Saif is a well intentioned though slightly indecisive fellow. Every morning he flips a coin to decide where to go. If the coin is heads he drives to the mall, if it comes up tails he volunteers at the local shelter. Saif’s coin is not necessarily fair, rather it possesses a probability of heads equal to _q_ . We do not know _q_ , but we do know it is well-modeled by a random variable _Q_ where the density of _Q_ is


Assume conditioned on _Q_ each coin flip is independent. Note parts a, b, c, and _{d, e}_ may be answered independent of each other.

6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 2 Solutions | Spring 2008)

a. (4 pts) What’s the probability that Saif goes to the local shelter if he flips the coin once? **Solution**

Let _Xi_ be the outcome of a coin toss on the _i_<sup>th</sup> trial, where _Xi_ = 1 if the coin lands ‘heads’, and _Xi_ = 0 if the coin lands ‘tails.’ By the total probability theorem:


In an attempt to promote virtuous behavior, Saif’s father offers to pay him $4 every day he volunteers at the local shelter. Define _X_ as Saif’s payout if he flips the coin every morning for the next 30 days.

b. Find var( _X_ )

**Solution** Let _Yi_ be a Bernoulli random variable describing the outcome of a coin tossed on morning _i._ Then, _Yi_ = 1 corresponds to the event that on morning _i_ , Saif goes to the local shelter; _Yi_ = 0 corresponds to the event that on morning _i_ , Saif goes to the mall. Assuming that the coin lands heads with probability _q_ , i.e. that _Q_ = _q_ , we have that _P_ ( _Yi_ = 1) = _q_ , and _P_ ( _Yi_ = 0) = 1 _− q_ for _i_ = 1 _, . . . ,_ 30.

Saif’s payout for next 30 days is described by random variable _X_ = 4( _Y_ 1 + _Y_ 2 + _· · ·_ + _Y_ 30) _._


since **E** [ _Q_ ] = �01 2 _q_ 2 _dq_ = 2 _/_ 3 and **E** [ _Q_ 2] = �01 2 _q_ 3 _dq_ = 1 _/_ 2.

7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 2 Solutions | Spring 2008)

Let event _B_ be that Saif goes to the local shelter at least once in _k_ days.

c. Find the conditional density of _Q_ given _B_ , _fQ B|_ ( _q_ )

**Solution** By Bayes Rule:


While shopping at the mall, Saif gets a call from his sister Mais. They agree to meet at the Coco Cabana Court yard at exactly 1:30PM. Unfortunately Mais arrives _Z_ minutes late, where _Z_ is a continuous uniform random variable from zero to 10 minutes. Saif is furious that Mais has kept him waiting, and demands Mais pay him _R_ dollars, where _R_ = exp( _Z_ + 2).

e. Find Saif’s expected payout, **E** [ _R_ ].

**Solution**


- f. Find the density of Saif’s payout, _fR_ ( _r_ ). **Solution**


8

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Question 2](02-question-2.md) · [Up: contents](index.md)
