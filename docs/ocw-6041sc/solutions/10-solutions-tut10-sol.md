---
title: 10 solutions tut10 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/10-solutions-tut10-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 solutions tut10 sol

**Source:** `solutions/10-solutions-tut10-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Tutorial 10 Solutions November 18/19, 2010

1. Note that n is deterministic and H is a random variable.

   - (a) Use X1, X2, . . . to denote the (random) measured heights.


- (b) We solve<sup>~~√~~</sup> <u>1.n5</u> < 0.01 for n to obtain n > 22500.

- (c) Apply the Chebyshev inequality to H with E[H] and var(H) from part (a):


To be “99% sure” we require the latter probability to be at least 0.99. Thus we solve


- (d) Intuitively, the variance of a random variable X that takes values in the range [0, b] is maximum when X takes the value 0 with probability 0.5 and the value b with probability 0.5, in which case the variance of X is b<sup>2</sup> /4 and its standard deviation is b/2.

   - More formally, since E[(X − c)<sup>2</sup> ] is minimized when c = E[X], we have for any random variable X taking values in [0, b],


since 0 ≤ X ≤ b ⇒ X(X − b) ≤ 0. Thus σX ≤ b/2. In our example, we have b = 3, so σX ≤ 3/2.

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

2. (a) Setting s = 1, we get t1 = 0 and


(b)


3. (a) K = 2 + X1 + X2, where X1 and X2 are independent exponential random variables with parameters 2/3 and 3/5.


(b)


Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
