---
title: 11 solutions tut11 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/11-solutions-tut11-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 solutions tut11 sol

**Source:** `solutions/11-solutions-tut11-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Tutorial 11 Solutions

1. (a) The LMS estimator is


(b) If x ∈ [0, 1], the conditional PDF of Y is uniform over the interval [0, x], and


Similarly, if x ∈ [1, 2], the conditional PDF of Y is uniform over [1 − x, x], and

- (c) The expectations E [( Y −g(X) �2� and E [var(Y |X)] are equal because by the law of iterated expectations,


Recall from part (b) that

It follows that


Note that

(d) The linear LMS estimator is


In order to calculate var(X) we first calculate E[X<sup>2</sup> ] and E[X]<sup>2</sup> .


Page 1 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


To determine cov(X, Y ) we need to evaluate E[XY ].


<u>61</u>

Therefore cov(X, Y ) = E[XY ] − E[X]E[Y ] = 32461 . Therefore,


- (e) The LMS estimator is the one that minimizes mean squared error (among all estimators of Y based on X). The linear LMS estimator, therefore, cannot perform better than the LMS estimator, i.e., we expect E[(Y − L(X))<sup>2</sup> ] ≥ E[(Y − g(X))<sup>2</sup> ]. In fact,


   - (f) For a single observation x of X, the MAP estimate is not unique since all possible values of Y for this x are equally likely. Therefore, the MAP estimator does not give meaningful results.

2. (a) X is a binomial random variable with parameters n = 3 and given the probability p that a single bit is flipped in a transmission over the noisy channel:


- (b) To derive the ML estimator for p based on X1, . . . , Xn, the numbers of bits flipped in the first n three-bit messages, we need to find the value of p that maximizes the likelihood function:


Since the Xi’s are independent, the likelihood function simplifies to:

Page 2 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)


The log-likelihood function is given by


We then maximize the log-likelihood function with respect to p:

This yields the ML estimator:


(c) The estimator is unbiased since:


(d) By the weak law of large numbers, n1 �ni=1<sup>Xiconverges in probability toEp[Xi] = 3p, and</sup> therefore P<sup>ˆ</sup> n = 31n �ni=1<sup>Xiconverges in probability top. ThusPˆnis consistent.</sup>

- (e) Sending 3 bit messages instead of 1 bit messages does not affect the ML estimate of p. To see this, let Yi be a Bernoulli RV which takes the value 1 if the ith bit is flipped (with probability p), and let m = 3n be the total number of bits sent over the channel. The ML estimate of p is then


Using the central limit theorem, P<sup>ˆ</sup> n is approximately a normal RV for large n. An approxi­ mate 95% confidence interval for p is then,


Page 3 of 4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

where v is the variance of Yi.

As suggested by the question, we estimate the unknown variance v by the convervative upper bound of 1/4. We are also give that n = 100 and the number of bits flipped is 20, yielding P<sup>ˆ</sup> n = 30<sup><u>2</u></sup> . Thus, an approximate 95% confidence interval is [0.01, 0.123].

- (f) Other estimates for the variance are the sample variance and the estimate P<sup>ˆ</sup> n(1 − P<sup>ˆ</sup> n). They potentially result in narrower confidence intervals than the conservative variance estimate used in part (e).

Page 4 of 4

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
