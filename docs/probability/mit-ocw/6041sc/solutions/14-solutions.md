---
title: 14 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/14-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 solutions

**Source:** `solutions/14-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 14 Solutions October 26, 2010

1. (a) Let X = (time between successive mosquito bites) = (time until the next mosquito bite).

The mosquito bites occur according to a Bernoulli process with parameter p = 0.5·0.2 = 0.1. X is a geometric random variable, so, E[X] = 1p = 01.1<sup>= 10.</sup>


- (b) Mosquito bites occur according to a Bernoulli process with parameter p = 0.1. Tick bites occur according to another independent Bernoulli process with parameter q = 0.1 · 0.7 = 0.07. Bug bites (mosquito or tick) occur according to a merged Bernoulli process from the mosquito and tick processes. Therefore, the probability of success at any time point for the merged Bernoulli process is r = p + q − pq = 0.1 + 0.07 − 0.1 · 0.07 = 0.163. Let Y be the time between successive bug bites. As before, Y is a geometric random variable, so E[Y ] =<sup>1</sup> r = 0.1631 ≈ 6.135.


2. (a) In this case, since the trials are independent, the given information is irrelevant. P(next 2 trials result in 3 tails) = (<sup>1</sup> 8 )<sup>2</sup> = 641 .

   - (b) i. The second order Pascal PMF for random variable N , as defined in the text, is the probability of the second success comes on the n<sup>th</sup> trial. Thus, the random variable, K, is a shifted version of the second order Pascal PMF, i.e. K = N − 1. So, the probability that 1 success comes in the first k trials, where the next trial will result in the second success, can be expressed as:


ii. The number of tails before the first success, M , can be written as a random sum:


where Xi is the number of tails that occur on (unsuccessful) trial i, and N is the number of unsuccessful trials (i.e. trials before the first success). We notice that X is equally likely to be either 1 or 2, and that N is a shifted geometric: N = R − 1, where R is a geometric random variable with parameter<sup>1</sup> 4<sup>. Now we can apply our random sum</sup> formulae.


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (c) N , the number of trials in Bob’s experiment, can be expressed as the sum of 3 independent random variables, X, Y , and Z. X is the number of trials until Bob removes the first coin, Y the number of additional trials until he removes the second coin, and Z the additional number until he removes the third coin. We see that X is a geometric random variable with parameter<sup>1</sup> 8<sup>,Yis geometric with parameter</sup> 4<sup>1, andZgeometric with parameter1</sup> 2<sup>. Hence,</sup>

E[N ] = E[X] + E[Y ] + E[Z] = 8 + 4 + 2 = 14.

3. Let M be the total number of draws you make until you have signed all n papers. Let Ti be the number of draws you make until drawing the next unsigned paper after having signed i papers. Then M = T0 + · · · + Tn `−` 1.

We can view the process of selecting the next unsigned paper after having signed i papers as a sequence of independent Bernoulli trials with probability of success pi =<sup>n</sup> n `−` i , since there are n − i unsigned papers out of a total of n papers and receiving any paper is equally likely in a particular draw. The PMF governing the number of attempts we make until we succeed in drawing the next unsigned paper after having signed i papers is geometric. More concretely, the probability that it takes k tries to draw the next unsigned paper after having signed i papers is


With this model, the expected value of M , the number of draws you make until you sign all n papers is:


For large n, this is on the order of: n � 1n x1 dx = n log n.

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
