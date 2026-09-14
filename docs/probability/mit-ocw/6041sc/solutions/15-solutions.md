---
title: 15 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/15-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 15 solutions

**Source:** `solutions/15-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 15 Solutions October 28, 2010

1. (a) Let X be the time until the first bulb failure. Let A (respectively, B) be the event that the frist bulb is of type A (respectively, B). Since the two bulb types are equally likely, the total expectation theorem yields


- (b) Let D be the event of no bulb failures before time t. Using the total probability theorem, and the exponential distributions for bulbs of the two types, we obtain


- (c) We have


- (d) The lifetime of the first type-A bulb is XA, with PDF given by:


Let Y be the total lifetime of two type-B bulbs. Because the lifetime of each type-B bulb is exponential with λ = 3, the sum Y has an Erlang distribution of order 2 with λ = 3. Its PDF is:


A simpler solution involving no integrals is as follows:

The bulb failure times of interest (1st type-A, 2nd type-B) may be thought of as the arrival

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

times of two independent Poisson processes of rate λA = 1 and λB = 3. We may imagine that these two processes were split from a joint Poisson process of rate λA + λB, where the splitting probabilities for each arrival are P (A) = λAλ+AλB<sup>=1/4 to processAand</sup> λB P (B) = λA+λB<sup>= 3/4 toprocessB. Now we mayjust focus on whether arrivalstothejoint</sup> process go to process A or to process B. Each arrival to the joint process corresponds to an independent trial. There are two possible outcomes: the arrival is handed to process A with probability P (A) or the arrival is handed to process B with probability P (B). Then our event of interest occurs when either the first arrival goes to A, or the first arrival goes to B followed by the second going to A. So the corresponding probability is


- (e) Let V be the total period of illumination provided by type-B bulbs while the process is in operation. Let N be the number of light bulbs, out of the first 12, that are of type-B. Let Xi be the period of illumination from the ith type-B bulb. We then have V = Y1 + · · · YN . Note that N is a binomial random variable, with parameters n = 12 and p = 1/2, so that


Furthermore, E[Xi] = 1/3 and var(Xi) = 1/9. Using the formulas for the mean and variance of the sum of a random number of random variables, we obtain


and


- (f) Using the notation in parts (a)-(c), and the result of part (c), we have


2. (a) The total arrival process corresponds to the merging of two independent Poisson processes, and is therefore Poisson with rate λ = λA + λB = 7. Thus, the number N of jobs that arrive in a given three-minute interval is a Poisson random variable, with E[N ] = 3λ = 21, var(N ) = 21, and PMF


- (b) Each of these 10 jobs has probability λA/(λA + λB) = 3/7 of being type A, independently of the others. Thus, the binomial PMF applies and the desired probability is equal to


Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (c) Each future arrival is of type A with probability λA/(λA + λB) = 3/7 of being type A, independently of the others. Thus, the number K of arrivals until the first type A arrival is geometric with parameter 3/7. The number of type B arrivals before the first type A arrival is equal to K − 1, and its PMF is similar to a geometric, except that it is shifted by one unit to the left. In particular,


3. The event {X < Y < Z} can be expressed as {X < min{Y, Z}} ∩{Y < Z}. Let Y and Z be the 1st arrival times of two independent Poisson processes with rates µ and ν. By merging the two processes, it should be clear that Y < Z if and only if the first arrival of the merged process comes from the original process with rate µ, and thus


Let X be the 1st arrival time of a third independent Poisson process with rate λ. Now {X < min{Y, Z}} if and only if the first arrival of the Poisson process obtained by merging the two processes with rates λ and µ + ν comes from the original process with rate λ, and thus


Note that the event {X < min{Y, Z}} is independent of the event {Y < Z}, as the time of the first arrival of the merged process with rate µ + ν is independent of whether that first arrival comes from the process with rate µ or the process with rate ν. Hence,


Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
