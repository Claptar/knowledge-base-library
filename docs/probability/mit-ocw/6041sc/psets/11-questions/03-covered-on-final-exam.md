---
title: Covered on Final Exam
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/psets/11-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Covered on Final Exam

**Source:** `psets/11-questions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. Problem 7, page 509 in textbook

   - Derive the ML estimator of the parameter of a Poisson random variable based of i.i.d. observa­ tions X1, . . . , Xn. Is the estimator unbiased and consistent?

2. Caleb builds a particle detector and uses it to measure radiation from far stars. On any given day, the number of particles Y that hit the detector is conditionally distributed according to a Poisson distribution conditioned on parameter x. The parameter x is unknown and is modeled as the value of a random variable X, exponentially distributed with parameter µ as follows.


Then, the conditional PDF of the number of particles hitting the detector is,

- (a) Find the MAP estimate of X from the observed particle count y.

- (b) Our goal is to find the conditional expectation estimator for X from the observed particle count y.

   - i. Show that the posterior probability distribution for X given Y is of the form


and find the parameter λ. You may find the following equality useful (it is obviously true if the equation above describes a true PDF):


      - ii. Find the conditional expectation estimate of X from the observed particle count y. Hint: you might want to express xfX|Y (x | y) in terms of fX|Y (x | y + 1).

   - (c) Compare the two estimators you constructed in part (a) and part (b).

3. Consider a Bernoulli process X1, X2, X3, . . . with unknown probability of success q. Define the kth inter-arrival time Tk as


where Yk is the time of the kth success. This problem explores estimation of q from observed inter-arrival times {t1, t2, t3, . . .}. In problem set 10, we solved the problem using Bayesian inference. Our focus here will be on classical estimation.

Page 1 of 3

Textbook problems are courtesy of Athena Scientific, and are used with permission.

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

We assume that q is an unknown parameter in the interval (0, 1]. Denote the true parameter by q<sup>∗</sup> . Denote by Q<sup>�</sup> k the maximum likelihood estimate (MLE) of q given k recordings, T1 = t1, . . . , Tk = tk.

- (a) Compute Q<sup>�</sup> k. Is this different from the MAP estimate you found in problem set 10?

- (b) Show that for all ǫ > 0


- (c) Assume q<sup>∗</sup> ≥ 0.5. Give a lower bound on k such that


4. A body at temperature θ radiates photons at a given wavelength. This problem will have you estimate θ, which is fixed but unknown. The PMF for the number of photons K in a given wavelength range and a fixed time interval of one second is given by,


Z(θ) is a normalization factor for the probability distribution (the physicists call it the partition function). You are given the task of determining the temperature of the body to two significant digits by photon counting in non-overlapping time intervals of duration one second. The photon emissions in non-overlapping time intervals are statistically independent from each other.

- (a) Determine the normalization factor Z(θ).

- (b) Compute the expected value of the photon number measured in any 1 second time interval, µK = Eθ[K], and its variance, varθ(K) = σK<sup>2.</sup>

- (c) You count the number ki of photons detected in n non-overlapping 1 second time intervals. Find the maximum likelihood estimator, Θ<sup>ˆ</sup> n, for temperature Θ. Note, it might be useful to introduce the average photon number sn = n 1<sup>�</sup> ni=1<sup>ki. In order to keep the analysis simple</sup> we assume that the body is hot, i.e. θ ≫ 1. You may use the approximation: <u>11</u> ≈ θ for θ ≫ 1. e θ −1

In the following questions we wish to estimate the mean of the photon count in a one second time interval using the estimator K<sup>ˆ</sup> , which is given by,


   - (d) Find the number of samples n for which the noise to signal ratio for K<sup>ˆ</sup> , (i.e., µ<sup>σ</sup> <u>KK</u><sup>ˆ</sup> ˆ ), is 0.01.

   - (e) Find the 95% confidence interval for the mean photon count estimate for the situation in part (d). (You may use the central limit theorem.)

5. The RandomView window factory produces window panes. After manufacturing, 1000 panes were loaded onto a truck. The weight Wi of the i-th pane (in pounds) on the truck is modeled as a random variable, with the assumption that the Wi’s are independent and identically distributed.

Page 2 of 3

Textbook problems are courtesy of Athena Scientific, and are used with permission.

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

- (a) Assume that the measured weight of the load on the truck was 2340 pounds, and that var(Wi) ≤ 4. Find an approximate 95 percent confidence interval for µ = E[Wi], using the Central Limit Theorem.

- (b) Now assume instead that the random variables Wi are i.i.d., with an exponential distribution with parameter θ > 0, i.e., a distribution with PDF


What is the maximum likelihood estimate of θ, given that the truckload has weight 2340 pounds?

6. Given the five data pairs (xi,yi) in the table below,


we want to construct a model relating x and y. We consider a linear model


and a quadratic model


where Wi and Vi represent additive noise terms, modeled by independent normal random variables with mean zero and variance σ12 and σ22, respectively.

- (a) Find the ML estimates of the linear model parameters.

- (b) Find the ML estimates of the quadratic model parameters.

Note: You may use the regression formulas and the connection with ML described in pages 478-479 of the text. However, the regression material is outside the scope of the final.

Page 3 of 3

Textbook problems are courtesy of Athena Scientific, and are used with permission.

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2010

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Never Due](02-never-due.md) · [Up: contents](index.md)
