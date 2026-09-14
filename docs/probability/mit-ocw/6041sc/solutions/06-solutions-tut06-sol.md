---
title: 06 solutions tut06 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/06-solutions-tut06-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 solutions tut06 sol

**Source:** `solutions/06-solutions-tut06-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Fall</u> 2010)

# **Tutorial 6: Solutions**

1. Let _Z_ = _X_ + _Y_ . Using the 2 step CDF method,


Using the Total Probability Theorem, we have


Differentiating both sides with respect to _z_ , we obtain


2. We will condition on _X_ and use the law of total variance


Given a value _x_ of _X_ , the random variable _Y_ is uniformly distributed in the interval [ _x, x_ + 1], and the random variable _X_ + _Y_ is uniformly distributed in the interval [2 _x,_ 2 _x_ + 1]. Therefore, **E** [ _X_ + _Y |X_ ] = 0 _._ 5 + 2 _X_ and var( _X_ + _Y |X_ ) = 1 _/_ 12. Thus,


3. (a) Let _Xi_ be independent Bernoulli random variables that are equal to 1 if the _i_ th flip results in heads. Let _N_ be the number of coin flips. We have **E** [ _Xi_ ] = 1 _/_ 2, var( _Xi_ ) = 1 _/_ 4, **E** [ _N_ ] = 7 _/_ 2, and var( _N_ ) = 35 _/_ 12. (The last equality is obtained from the formula for the variance of a discrete uniform random variable.) Therefore, the expected number of heads is


and the variance is


- (b) The experiment in part (b) can be viewed as consisting of two independent repetitions fo the experiment in part (a). Thus, both the mean and the variance are doubled and become 7 _/_ 2 and 77 _/_ 24, respectively.

Page 1 of 1

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
