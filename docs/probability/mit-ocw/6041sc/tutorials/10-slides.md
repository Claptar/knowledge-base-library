---
title: 10 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/tutorials/10-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 slides

**Source:** `tutorials/10-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

# Tutorial 10 November 18/19, 2010

1. Define X as the height in meters of a randomly selected Canadian, where the selection probability is equal for each Canadian, and denote E[X] by h. Bo is interested in estimating h. Because he is sure that no Canadian is taller than 3 meters, Bo decides to use 1.5 meters as a conservative (large) value for the standard deviation of X. To estimate h, Bo averages the heights of n Canadians that he selects at random; he denotes this quantity by H.

   - (a) In terms of h and Bo’s 1.5 meter bound for the standard deviation of X, determine the expected value and standard deviation for H.

   - (b) Help Bo by calculating a minimum value of n (with n > 0) such that the standard deviation of Bo’s estimator, H, will be less than 0.01 meters.

   - (c) Bo would like to be 99% sure that his estimate is within 5 centimeters of the true average height of Canadians. Using the Chebyshev inequality, calculate the minimum value of n that will make Bo happy.

   - (d) If we agree that no Canadians are taller than three meters, why is it correct to use 1.5 meters as an upper bound on the standard deviation for X, the height of any Canadian selected at random?

2. On any given week while taking 6.041, a student can be either up-to-date on learning the material, or she may have fallen behind. If she is up-to-date in a given week, the probability that she will be up-to-date (or behind) in the next week is 0.8 (or 0.2, respectively). If she is behind in the given week, the probability that she will be up-to-date (or behind) in the next week is 0.6 (or 0.4, respectively). We assume that these probabilities do not depend on whether she was up-to-date or behind in previous weeks, so we can model the situation as a 2-state Markov chain where State 1 is the case when the student is up-to-date and State 2 is the case when the student is behind.

   - (a) Calculate the mean first passage time to State 1, starting from State 2.

   - (b) Calculate the mean recurrence time to State 1.

3. Consider the following Markov chain:


The steady-state probabilities for this process are:

Assume the process is in state 1 just before the first transition.

- (a) Determine the expected value and variance of K, the number of transitions up to and including the next transition on which the process returns to state 1.

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

<u>(Fall</u> 2010)

- (b) What is the probability that the state of the system resulting from transition 1000 is neither the same as the state resulting from transition 999 nor the same as the state resulting from transition 1001?

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
