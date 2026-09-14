---
title: 12 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/12-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 12 solutions

**Source:** `solutions/12-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041SC Probabilistic Systems Analysis and Applied Probability Lecture 12 Bonus Video Solution

**Problem 27.*** We toss _n_ times a biased coin whose probability of heads, denoted by _q_ , is the value of a random variable _Q_ with given mean _µ_ and positive variance _σ_<sup>2</sup> . Let _Xi_ be a Bernoulli random variable that models the outcome of the _i_ th toss (i.e., _Xi_ = 1 if the _i_ th toss is a head). We assume that _X_ 1 _, . . . , Xn_ are conditionally independent, given _Q_ = _q_ . Let _X_ be the number of heads obtained in the _n_ tosses.

(a) Use the law of iterated expectations to find **E** [ _Xi_ ] and **E** [ _X_ ].

- (b) Find cov( _Xi, Xj_ ). Are _X_ 1 _, . . . , Xn_ independent?

- (c) Use the law of total variance to find var( _X_ ). Verify your answer using the co­ variance result of part (b).

_Solution._ (a) We have, from the law of iterated expectations and the fact **E** [ _Xi | Q_ ] = _Q_ ,


Since _X_ = _X_ 1 + _· · ·_ + _Xn,_ it follows that


(b) We have, for _i_ = _j_ , using the conditional independence assumption,


and


Thus,

cov( _Xi, Xj_ ) = **E** [ _XiXj_ ] _−_ **E** [ _Xi_ ] **E** [ _Xj_ ] = **E** [ _Q_<sup>2</sup> ] _− µ_<sup>2</sup> = _σ_<sup>2</sup> _._

Since cov( _Xi, Xj_ ) _>_ 0, _X_ 1 _, . . . , Xn_ are not independent. Also, for _i_ = _j_ , using the observation that _Xi_ 2 = _Xi_ ,


1

_Further Topics on Random Variables Chap. 4_

(c) Using the law of total variance, and the conditional independence of _X_ 1 _, . . . , Xn_ , we have


To verify the result using the covariance formulas of part (b), we write


2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
