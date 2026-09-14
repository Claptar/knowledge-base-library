---
title: Final s09 exam
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/final-s09-exam.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Final s09 exam

**Source:** `exams/final-s09-exam.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

## (Final Exam | Spring 2009)

Problem 1: True or False (2pts. each, 18 pts. total)

No partial credit will be given for individual questions in this part of the quiz.

- a. Let {Xn} be a sequence of i.i.d random variables taking values in the interval [0, 0.5]. Consider the following statements:

   - (A) If E[Xn2] converges to 0 as n →∞ then Xn converges to 0 in probability.

   - (B) If all Xn have E[Xn] = 0.2 and var (Xn) converges to 0 as n →∞ then Xn converges to 0.2 in probability.

   - (C) The sequence of random variables Zn, defined by Zn = X1 · X2 · · · Xn, converges to 0 in probability as n →∞.

Which of these statements are always true? Write True or False in each of the boxes below.

A: B: C:

- b. Let Xi (i = 1, 2, . . . ) be i.i.d. random variables with mean 0 and variance 2; Yi (i = 1, 2, . . . ) be i.i.d. random variables with mean 2. Assume that all variables Xi, Yj are independent. Consider the following statements:

   - (A) X1+···n +Xn converges to 0 in probability as n →∞. (B) X1<sup>2</sup> +···n +Xn<sup>2</sup> converges to 2 in probability as n →∞.

   - (C) X1Y1+···n +XnYn converges to 0 in probability as n →∞.

Which of these statements are always true? Write True or False in each of the boxes below.

A: B: C:

- c. We have i.i.d. random variables X1 . . . Xn with an unknown distribution, and with µ = E[Xi]. We define Mn = (X1 + . . . + Xn)/n. Consider the following statements:

   - (A) Mn is a maximum-likelihood estimator for µ, irrespective of the distribution of the Xi’s.

   - (B) Mn is a consistent estimator for µ, irrespective of the distribution of the Xi’s.

   - (C) Mn is an asymptotically unbiased estimator for µ, irrespective of the distribution of the Xi’s.

Which of these statements are always true? Write True or False in each of the boxes below.

|A:<br>B:<br>C:|
|---|


1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

Problem 2: Multiple Choice (4 pts. each, 24 pts. total)

Clearly circle the appropriate choice. No partial credit will be given for individual questions in this part of the quiz.

- a. Earthquakes in Sumatra occur according to a Poisson process of rate λ = 2/year. Conditioned on the event that exactly two earthquakes take place in a year, what is the probability that both earthquakes occur in the first three months of the year? (for simplicity, assume all months have 30 days, and each year has 12 months, i.e., 360 days).

(i) 1/12

- (ii) 1/16

- (iii) 64/225

(iv) 4e<sup>−4</sup>

   - (v) There is not enough information to determine the required probability.

   - (vi) None of the above.

- b. Consider a continuous-time Markov chain with three states i ∈{1, 2, 3}, with dwelling time in each visit to state i being an exponential random variable with parameter νi = i, and transition probabilities pij defined by the graph


What is the long-term expected fraction of time spent in state 2?

(i) 1/2 (ii) 1/4 (iii) 2/5 (iv) 3/7 (v) None of the above.

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Final Exam | Spring 2009)

- c. Consider the following Markov chain:


Starting in state 3, what is the steady-state probability of being in state 1?

(i) 1/3

(ii) 1/4

(iii) 1

(iv) 0

   - (v) None of the above.

- d. Random variables X and Y are such that the pair (X, Y ) is uniformly distributed over the trapezoid A with corners (0, 0), (1, 2), (3, 2), and (4, 0) shown in Fig. 1:


<!-- Start of picture text -->
X<br>2<br>Y<br>1 3 4<br><!-- End of picture text -->

Figure 1: fX,Y (x, y) is constant over the shaded area, zero otherwise.

i.e.


We observe Y and use it to estimate X. Let X<sup>ˆ</sup> be the least mean squared error estimator of X given Y . What is the value of var( X<sup>ˆ</sup> − X|Y = 1)?

(i) 1/6 (ii) 3/2

(iii) 1/3

- (iv) The information is not sufficient to compute this value.

- (v) None of the above.

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Final Exam | Spring 2009)

- e. X1 . . . Xn are i.i.d. normal random variables with mean value µ and variance v. Both µ and v are unknown. We define Mn = (X1 + . . . + Xn)/n and


We also define Φ(x) to be the CDF for the standard normal distribution, and Ψn−1(x) to be the CDF for the t-distribution with n − 1 degrees of freedom. Which of the following choices gives an exact 99% confidence interval for µ for all n > 1?


   - (v) None of the above.

- f. We have i.i.d. random variables X1, X2 which have an exponential distribution with unknown parameter θ. Under hypothesis H0, θ = 1. Under hypothesis H1, θ = 2. Under a likelihood-ratio test, the rejection region takes which of the following forms?

   - (i) R = {(x1, x2) : x1 + x2 > ξ} for some value ξ.

   - (ii) R = {(x1, x2) : x1 + x2 < ξ} for some value ξ.

   - (iii) R = {(x1, x2) : e<sup>x1</sup> + e<sup>x2</sup> > ξ} for some value ξ.

   - (iv) R = {(x1, x2) : e<sup>x1</sup> + e<sup>x2</sup> < ξ} for some value ξ.

   - (v) None of the above.

4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

Problem 3 (12 pts. total)

Aliens of two races (blue and green) are arriving on Earth independently according to Poisson process distributions with parameters λb and λa respectively. The Alien Arrival Registration Service Authority (AARSA) will begin registering alien arrivals soon.

Let T1 denote the time AARSA will function until it registers its first alien. Let G be the event that the first alien to be registered is a green one. Let T2 be the time AARSA will function until at least one alien of both races is registered.

- (a) (4 points.) Express µ1 = E[T1] in terms of λg and λb. Show your work.

- (b) (4 points.) Express p = P(G) in terms of λg and λb. Show your work.

5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

- (c) (4 points.) Express µ2 = E[T2] in terms of λg and λb. Show your work.

6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

Problem 4 (18 pts. total)

Researcher Jill is interested in studying employment in technology firms in Dilicon Valley. She denotes by Xi the number of employees in technology firm i and assumes that Xi are independent and identically distributed with mean p. To estimate p, Jill randomly interviews n technology firms and observes the number of employees in these firms.

(a) (6 points.) Jill uses


as an estimator for p. Find the limit of P(Mn ≤ x) as n →∞ for x < p. Find the limit of P(Mn ≤ x) as n →∞ for x > p. Show your work.

- (b) (6 points.) Find the smallest n, the number of technology firms Jill must sample, for which the Chebyshev inequality yields a guarantee


Assume that var (Xi) = v for some constant v. State your solution as a function of v. Show your work.

7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

- (c) (6 points.) Assume now that the researcher samples n = 5000 firms. Find an approximate value for the probability

   - P(|M5000 − p| ≥ 0.5)

using the Central Limit Theorem. Assume again that var (Xi) = v for some constant v. Give your answer in terms of v, and the standard normal CDF Φ. Show your work.

8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

Problem 5 (12 pts. total)

The RandomView window factory produces window panes. After manufacturing, 1000 panes were loaded onto a truck. The weight Wi of the i-th pane (in pounds) on the truck is modeled as a random variable, with the assumption that the Wi’s are independent and identically distributed.

- (a) (6 points.) Assume that the measured weight of the load on the truck was 2340 pounds, and that var (Wi) ≤ 4. Find an approximate 95 percent confidence interval for µ = E[Wi], using the Central Limit Theorem (you may use the standard normal table which was handed out with this quiz). Show your work.

- (b) (6 points.) Now assume instead that the random variables Wi are i.i.d, with an exponential distribution with parameter θ > 0, i.e., a distribution with PDF


What is the maximum likelihood estimate of θ, given that the truckload has weight 2340 pounds? Show your work.

9

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

Problem 6 (21 pts. total)

In Alice’s Wonderland, there are six different seasons: Fall (F), Winter (W), Spring (Sp), Summer (Su), Bitter Cold (B), and Golden Sunshine (G). The seasons do not follow any particular order, instead, at the beginning of each day the Head Wizard assigns the season for the day, according to the following Markov chain model:


Thus, for example, if it is Fall one day then there is 1/6 probability that it will be Winter the next day (note that it is possible to have the same season again the next day).

- (a) (4 points.) For each state in the above chain, identify whether it is recurrent or transient. Show your work.

- (b) (4 points.) If it is Fall on Monday, what is the probability that it will be Summer on Thursday of the same week? Show your work.

10

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

- (c) (4 points.) If it is Spring today, will the chain converge to steady-state probabilities? If so, compute the steady-state probability for each state. If not, explain why these probabilities do not exist. Show your work.

- (d) (5 points.) If it is Fall today, what is the probability that Bitter Cold will never arrive in the future? Show your work.

11

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

- (e) (5 points.) If it is Fall today, what is the expected number of days till either Summer or Golden Sunshine arrives for the first time? Show your work.

12

# Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Final Exam | Spring 2009)

Problem 7 (12 pts. total)

A newscast covering the final baseball game between Sed Rox and Y Nakee becomes noisy at the crucial moment when the viewers are informed whether Y Nakee won the game.

Let a be the parameter describing the actual outcome: a = 1 if Y Nakee won, a = −1 otherwise. There were n viewers listening to the telecast. Let Yi be the information received by viewer i (1 ≤ i ≤ n). Under the noisy telecast, Yi = a with probability p, and Yi = −a with probability 1 − p. Assume that the random variables Yi are independent of each other.

The viewers as a group come up with a joint estimator


(a) (6 points.)

Find limn→∞ P(Zn = a) assuming that p > 0.5 and a = 1. Show your work.

(b) (6 points.) Find limn→∞ P(Zn = a), assuming that p = 0.5 and a = 1. Show your work.

13

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
