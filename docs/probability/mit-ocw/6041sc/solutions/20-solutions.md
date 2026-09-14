---
title: 20 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/20-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 20 solutions

**Source:** `solutions/20-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Recitation 20 Solutions: November 18, 2010

1. (a) Let Xi be a random variable indicating the quality of the ith bulb (“1” for good bulbs, “0” for bad ones). Xi’s are independent Bernoulli random variables. Let Zn be


where σ<sup>2</sup> is the variance of Xi.

Applying Chebyshev’s inequality yields,


<u>σ</u><sup>2</sup> As n →∞, nǫ2 → 0 and P (|Zn − p| ≥ ǫ) → 0. Hence, Zn converges to p in probability.

(b) By Chebychev’s inequality,


Since Xi is a Bernoulli random variable, its variance σ<sup>2</sup> is p(1 − p), which is less than or equal to<sup><u>1</u></sup> 4<sup>. Thus,</sup>


- (c) By Chebychev’s inequality,


To guarantee a probability 0.95 of falling in the desired range,


which yields n ≥ 500. Note that n ≥ 500 guarantees the accuracy specification even for the highest variance, namely 1/4. For smaller variances, we need smaller values of n to guarantee the desired accuracy. For example, if σ<sup>2</sup> = 1/16, n ≥ 125 would suffice.


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

- (b) Using Chebyshev’s inequality, we have


It follows that Xn converges to 0 in probability. For Yn, Chebyshev suggests that,


Thus, we cannot conclude anything about the convergence of Yn through Chebychev’s in­ equality.

- (c) For every ǫ > 0,


Thus, Yn converges to zero in probability.

- (d) The statement is false. A counter example is Yn. It converges in probability to 0 yet its expected value is 1 for all n.

- (e) Using the Markov bound, we have


Taking the limit as n →∞, we obtain


which establishes convergence in probability.

- (f) A counter example is Yn. Yn converges to 0 in probability, but

Thus,

and Yn does not converge to 0 in the mean square.

3. (a) No. Since Xi for any i ≥ 1 is uniformly distributed between -1.0 and 1.0.

   - (b) Yes, to 0. Since for ǫ > 0,


(c) Yes, to 0. Since for ǫ > 0,

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
