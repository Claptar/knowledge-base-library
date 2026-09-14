---
title: Introduction
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/finl-s09-sol-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `solutions/finl-s09-sol-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

Problem 1: True or False (2pts. each, 18 pts. total)

No partial credit will be given for individual questions in this part of the quiz.

- a. Let {Xn} be a sequence of i.i.d random variables taking values in the interval [0, 0.5]. Consider the following statements:

   - (A) If E[Xn<sup>2</sup> ] converges to 0 as n →∞ then Xn converges to 0 in probability.

   - (B) If all Xn have E[Xn] = 0.2 and var (Xn) converges to 0 as n →∞ then Xn converges to 0.2 in probability.

   - (C) The sequence of random variables Zn, defined by Zn = X1 · X2 · · · Xn, converges to 0 in probability as n →∞.

Which of these statements are always true? Write True or False in each of the boxes below.

A: True B: True C: True

## Solution:

- (A) True. The fact that limn→∞ E[Xn<sup>2</sup> ] = 0 implies limn→∞ E[Xn] = 0 and limn→∞ var(Xn) = 0. Hence, one has

   - P (|Xn − 0| ≥ ǫ) ≤ P (|Xn − E[Xn]| ≥ ǫ/2) + P (|E[Xn] − 0| ≥ ǫ/2) var(Xn)

   - ≤ (ǫ/2)<sup>2+P(|E[Xn] −0| ≥ǫ/2)→0,</sup>

where we have applied Chebyshev inequality.

- (B) True. Applying Chebyshev inequality gives


Hence Xn converges to E[Xn] = 0.2 in probability.

   - (C) True. For all ǫ > 0, since Zn ≤ (1/2)<sup>n</sup> ⇒ P (|Zn − 0| ≥ ǫ) = 0 for n > − log ǫ/ log 2.

- b. Let Xi (i = 1, 2, . . . ) be i.i.d. random variables with mean 0 and variance 2; Yi (i = 1, 2, . . . ) be i.i.d. random variables with mean 2. Assume that all variables Xi, Yj are independent. Consider the following statements:

   - (A) X1+···n +Xn converges to 0 in probability as n →∞.

   - (B) X1<sup>2</sup> +<sup>···</sup> n +Xn<sup>2</sup> converges to 2 in probability as n →∞.

   - (C) X1Y1+···n +XnYn converges to 0 in probability as n →∞.

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Final Exam Solutions | Spring 2009)

Which of these statements are always true? Write True or False in each of the boxes below.

A: True B: True C: True

## Solution:

   - (A) True. Note that E[<sup>X1+···</sup> n<sup>+Xn</sup> ] = 0 and var(<sup>X1+···</sup> n<sup>+Xn</sup> ) =<sup>n</sup> n<sup>·22</sup> = n2 . One can see X1+···n +Xn converges to 0 in probability.

   - (B) True. Let Zi = Xi 2 and E[Zi] = 2. Note Zi are i.i.d. since Xi are i.i.d., and hence one has that<sup>Z1+···</sup> n<sup>+Zn</sup> converges to E[Zi] = 2 in probability by the WLLN.

   - (C) True. Let Wi = XiYi and E[Wi] = E[Xi]E[Yi] = 0. Note Wi are i.i.d. since Xi and Yi are respectively i.i.d., and hence one has that<sup>W1+···</sup> n<sup>+Wn</sup> converges to E[Wi] = 0 in probability by the WLLN.

- c. We have i.i.d. random variables X1 . . . Xn with an unknown distribution, and with µ = E[Xi]. We define Mn = (X1 + . . . + Xn)/n. Consider the following statements:

   - (A) Mn is a maximum-likelihood estimator for µ, irrespective of the distribution of the Xi’s.

   - (B) Mn is a consistent estimator for µ, irrespective of the distribution of the Xi’s.

   - (C) Mn is an asymptotically unbiased estimator for µ, irrespective of the distribution of the Xi’s.

Which of these statements are always true? Write True or False in each of the boxes below.

|A: False|B: True|C: True|
|---|---|---|


## Solution:

- 1

- (A) False. Consider Xi follow a uniform distribution U [µ −<sup>1</sup> 2 , µ + 2 ]. The ML estimator for µ 1 1

- is any value between max(X1, · · · , Xn) − 2 and min(X1, · · · , Xn) + 2 , instead of Mn.

- (B) True. By the WLLN, Mn converges to µ in probability and hence it is a consistent estimator.

- (C) True. Since E[Mn] = E[Xi] = µ, Mn is unbiased estimator for µ and hence asymptotically unbiased.

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

Problem 2: Multiple Choice (4 pts. each, 24 pts. total)

Clearly circle the appropriate choice. No partial credit will be given for individual questions in this part of the quiz.

- a. Earthquakes in Sumatra occur according to a Poisson process of rate λ = 2/year. Conditioned on the event that exactly two earthquakes take place in a year, what is the probability that both earthquakes occur in the first three months of the year? (for simplicity, assume all months have 30 days, and each year has 12 months, i.e., 360 days).

(i) 1/12

(ii) 1/16

(iii) 64/225

- (iv) 4e<sup>−4</sup>

- (v) There is not enough information to determine the required probability.

- (vi) None of the above.

Solution: Consider the interval of a year be [0, 1].


(alternative explanation) Given that exactly two earthquakes happened in 12 months, each earth­ quake is equally likely to happen in any month of the 12, the probability that it happens in the first 3 months is 3/12 = 1/4. The probability that both happen in the first 3 months is (1/4)<sup>2</sup> .

- b. Consider a continuous-time Markov chain with three states i ∈{1, 2, 3}, with dwelling time in each visit to state i being an exponential random variable with parameter νi = i, and transition probabilities pij defined by the graph


What is the long-term expected fraction of time spent in state 2?

(i) 1/2

(ii) 1/4 (iii) 2/5

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

(iv) 3/7

(v) None of the above.

Solution: First, we calculate the qij = νipij, i.e., q12 = q21 = q23 = 1 and q32 = 3. The balance and normalization equations of this birth-death markov chain can be expressed as, π1 = π2, π2 = 3π3 and π1 + π2 + π3 = 1, yielding π2 = 3/7.

4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

- c. Consider the following Markov chain:


Starting in state 3, what is the steady-state probability of being in state 1?


- (v) None of the above.

Solution: State 1 is transient.

- d. Random variables X and Y are such that the pair (X, Y ) is uniformly distributed over the trapezoid A with corners (0, 0), (1, 2), (3, 2), and (4, 0) shown in Fig. 1:


<!-- Start of picture text -->
X<br>2<br>Y<br>1  3 4<br><!-- End of picture text -->

Figure 1: fX,Y (x, y) is constant over the shaded area, zero otherwise.

i.e.


We observe Y and use it to estimate X. Let X<sup>ˆ</sup> be the least mean squared error estimator of X given Y . What is the value of var( X<sup>ˆ</sup> − X|Y = 1)?


(iv) The information is not sufficient to compute this value.

5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

(v) None of the above.

Solution: fX|Y =1(x) is uniform on [0, 2] therefore X<sup>ˆ</sup> = E[X|Y = 1] = 1 and var( X<sup>ˆ</sup> − X|Y = 1) = var(X|Y = 1) = (2 − 0)<sup>2</sup> /12 = 1/3.

- e. X1 . . . Xn are i.i.d. normal random variables with mean value µ and variance v. Both µ and v are unknown. We define Mn = (X1 + . . . + Xn)/n and


We also define Φ(x) to be the CDF for the standard normal distribution, and Ψn−1(x) to be the CDF for the t-distribution with n − 1 degrees of freedom. Which of the following choices gives an exact 99% confidence interval for µ for all n > 1?


- (v) None of the above.

Solution: See Lecture 23, slides 10-12.

- f. We have i.i.d. random variables X1, X2 which have an exponential distribution with unknown parameter θ. Under hypothesis H0, θ = 1. Under hypothesis H1, θ = 2. Under a likelihood-ratio test, the rejection region takes which of the following forms?

   - (i) R = {(x1, x2) : x1 + x2 > ξ} for some value ξ.


- (v) None of the above.

Solution: We defined R = {x = (x1, x2)|L(x) > c} where


So R = {(x1, x2)|x1 + x2 < − log (c/4)}

6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

Problem 3 (12 pts. total)

Aliens of two races (blue and green) are arriving on Earth independently according to Poisson process distributions with parameters λb and λg respectively. The Alien Arrival Registration Service Authority (AARSA) will begin registering alien arrivals soon.

Let T1 denote the time AARSA will function until it registers its first alien. Let G be the event that the first alien to be registered is a green one. Let T2 be the time AARSA will function until at least one alien of both races is registered.

- (a) (4 points.) Express µ1 = E[T1] in terms of λg and λb. Show your work.


Solution: We consider the process of arrivals of both types of Aliens. This is a merged Poisson process with arrival rate λg+λb. T1 is the time until the first arrival, and therefore is exponentially 1 distributed with parameter λg + λb. Therefore µ1 = E[T1] = λg+λb<sup>.</sup>

One can also go about this using derived distributions, since T1 = min(T1g, T1b) where T1g and T1b are the first arrival times of green and blue Aliens respectively (i.e., T1g and T1b are exponentially distributed with parameters λg and λb, respectively. )

- (b) (4 points.) Express p = P(G) in terms of λg and λb. Show your work.


Solution: We consider the same merged Poisson process as before, with arrival rate λg +λb. Any λg particular arrival of the merged process has probability λg +λb<sup>of corresponding to a green Alien</sup> λb λg and probability λg +λb<sup>of corresponding to a blue Alien. The question asks forP(G) =</sup> λg +λb<sup>.</sup>

7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Final Exam Solutions | Spring 2009)

- (c) (4 points.) Express µ2 = E[T2] in terms of λg and λb. Show your work.


Solution: The time T2 until at least one green and one red Aliens have arrived can be expressed as T2 = max(T1g, T1b), where T1g and T1b are the first arrival times of green and blue Aliens respectively (i.e., T1g and T1b are exponentially distributed with parameters λg and λb, respectively.)

1 The expected time till the 1st Alien arrives was calculated in (a), µ1 = E[T1] = . To λg +λb compute the remaining time we simply condition on the 1st Alien being green(e.g. event G) or blue(event G<sup>c</sup> ), and use the memoryless property of Poisson, i.e.,


8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

Problem 4 (18 pts. total)

Researcher Jill is interested in studying employment in technology firms in Dilicon Valley. She denotes by Xi the number of employees in technology firm i and assumes that Xi are independent and identically distributed with mean p. To estimate p, Jill randomly interviews n technology firms and observes the number of employees in these firms.

(a) (6 points.) Jill uses


as an estimator for p. Find the limit of P(Mn ≤ x) as n →∞ for x < p. Find the limit of P(Mn ≤ x) as n →∞ for x > p. Show your work.

Solution: Since Xi is i.i.d., Mn converges to p in probability, i.e., limn→∞ P(|Mn − p| > ǫ) = 0, implying limn→∞ P(Mn < p − ǫ) = 0 and limn→∞ P(Mn > p + ǫ) = 0, for all ǫ > 0. Hence


- (b) (6 points.) Find the smallest n, the number of technology firms Jill must sample, for which the Chebyshev inequality yields a guarantee


Assume that var (Xi) = v for some constant v. State your solution as a function of v. Show your work.

n Solution: Since Mn converges to p in probability and var(Mn) = n2 ·<sup>var(X</sup> i<sup>) =v/n, Chebyshev</sup> inequality gives


9

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

- (c) (6 points.) Assume now that the researcher samples n = 5000 firms. Find an approximate value for the probability


using the Central Limit Theorem. Assume again that var (Xi) = v for some constant v. Give your answer in terms of v, and the standard normal CDF Φ. Show your work.

Solution: By CLT, we can approximate by a standard normal distribution


when n is large, and hence,

where n = 5000.

10

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam Solutions | Spring 2009)

Problem 5 (12 pts. total)

The RandomView window factory produces window panes. After manufacturing, 1000 panes were loaded onto a truck. The weight Wi of the i-th pane (in pounds) on the truck is modeled as a random variable, with the assumption that the Wi’s are independent and identically distributed.

- (a) (6 points.) Assume that the measured weight of the load on the truck was 2340 pounds, and that var (Wi) ≤ 4. Find an approximate 95 percent confidence interval for µ = E[Wi], using the Central Limit Theorem (you may use the standard normal table which was handed out with this quiz). Show your work.


Solution: The sample mean estimator Θ<sup>ˆ</sup> n =<sup>W1+···</sup> n<sup>+Wn</sup> in this case is


Using the CDF Φ(z) of the standard normal available in the normal tables, we have Φ(1.96) = 0.975, so we obtain


Because the variance is less than 4, we have


and letting the right-hand side of the above equation ≈ 0.95 gives a 95% confidence, i.e.,


11

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Final Exam Solutions | Spring 2009)

- (b) (6 points.) Now assume instead that the random variables Wi are i.i.d, with an exponential distribution with parameter θ > 0, i.e., a distribution with PDF


What is the maximum likelihood estimate of θ, given that the truckload has weight 2340 pounds? Show your work.


Solution: The likelihood function is


And the log-likelihood function is


The derivative with respect to θ is<sup>n</sup> θ<sup>−</sup> �n i=1<sup>wi,, and by setting it to zero, we see that the</sup> maximum of log fW (w; θ) over θ ≥ 0 is attained at θ<sup>ˆ</sup> n =<sup>�</sup> ni=1n<sup>wi</sup> . The resulting estimator is


In our case,


12

---

[Up: contents](index.md) · [Finl s09 sol solutions Part 02 — →](02-finl-s09-sol-solutions-part-02.md)
