---
title: 07 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/tutorials/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 07 slides

**Source:** `tutorials/07-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

# Tutorial 7 October 28/29, 2010

1. Alice and Bob alternate playing at the casino table. (Alice starts and plays at odd times i = 1, 3, . . .; Bob plays at even times i = 2, 4, . . ..) At each time i, the net gain of whoever is playing is a random variable Gi with the following PMF:


Assume that the net gains at different times are independent. We refer to an outcome of −2 as a “loss.”

   - (a) They keep gambling until the first time where a loss by Bob immediately follows a loss by Alice. Write down the PMF of the total number of rounds played. (A round consists of two plays, one by Alice and then one by Bob.)

   - (b) Write down the PMF for Z, defined as the time at which Bob has his third loss.

   - (c) Let N be the number of rounds until each one of them has won at least once. Find E[N ].

2. Problem 6.6, page 328 in text.

Sum of a geometric number of independent geometric random variables

Let Y = X1 + · · · + XN , where the random variable Xi are geometric with parameter p, and N is geometric with parameter q. Assume that the random variables N, X1, X2, · · · are independent. Show that Y is geometric with parameter pq. Hint: Interpret the various random variables in terms of a split Bernoulli process.

3. A train bridge is constructed across a wide river. Trains arrive at the bridge according to a Poisson process of rate λ = 3 per day.

   - (a) If a train arrives on day 0, find the probability that there will be no trains on days 1, 2, and 3.

   - (b) Find the probability that the next train to arrive after the first train on day 0, takes more than 3 days to arrive.

   - (c) Find the probability that no trains arrive in the first 2 days, but 4 trains arrive on the 4<sup>th</sup> day.

   - (d) Find the probability that it takes more than 2 days for the 5<sup>th</sup> train to arrive at the bridge.

Textbook problems are courtesy of Athena Scientific, and are used with permission.

Page 1 of 1

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
