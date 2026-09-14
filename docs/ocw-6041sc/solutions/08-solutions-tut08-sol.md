---
title: 08 solutions tut08 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/08-solutions-tut08-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 08 solutions tut08 sol

**Source:** `solutions/08-solutions-tut08-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

# Tutorial 8: Solutions

1. (a) Let A = {An arriving item is of type A}.

The 3 independent Poisson processes can be merged into one Poisson process with an arrival rate of a + b + c items per minute. If δ is a short time interval, then


The probability that the first item is type A and exactly one of the next 9 items is type A is


- (b) Let B = {An arriving item is of type B}. Let C = {An arriving item is of type C}.

In order for there to be 5 times as many type A items as type B items, there can be either 5 type A items, 1 type B item, and 4 type C items, or 0 type A items, 0 type B item and 10 type C items. The probability of this event is the sum of the probabilities of the two cases:

10!


where P(A) = a+a b+c<sup>,P(B) =</sup> a+b b+c<sup>, andP(C) =</sup> a+c b+c<sup>.</sup>

- (c) The total time between consecutive discharges is an Erlang random variable of order 10 and parameter a + b + c, with PDF


(d) Let X = {Exactly two items from A arrive in 5 minutes}. Let Y = {Exactly two items from B arrive in 5 minutes}. Let Z = {Exactly two items from C arrive in 5 minutes}.

Because X, Y , Z are independent events, we know that

P({Exactly two of each of the three types arrive in 5 minutes})


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

2. (a) Since a given potential customer becomes an actual customer with probability p, we are dealing with a binomial probability, and �53�p3(1 − p)2 is the probability of exactly 3 of the first 5 potential customers being actual customers.

   - (b) Potential customers become actual customers independently of each other. Thus, P(the fifth customer is the third actual customer)

      - = P(any 2 of the first 4 customers become actual customer)

      - ·P(the fifth customer becomes an actual customer)

      - = [ �42<sup>�</sup> p2(1 − p)2][p] = �42<sup>�</sup> p3(1 − p)2.

   - (c) The process of incoming customers is being randomly split into two independent Poisson processes: the process for the arrival of actual customers, with rate pλ, and the process for the arrival of potential customers who do not become actual customers, with rate (1 − p)λ. The store will close when 10 actual customers have arrived. Thus, the store closes when we have 10 arrivals from the Poisson process of actual customers, which has rate pλ. Thus, L = T1 + T2 + ... + T10, where Ti is the interarrival time with an exponential distribution and parameter pλ. The distribution of L is the 10th order Erlang PDF, fL(l) =<sup>(pλ)10l</sup> 9!<sup>9e</sup><sup>`−`(pλ)l</sup> ,l ≥ 0. It follows that expected value of L is pλ<sup>10</sup> .

   - (d) Since five potential customers have arrived, three of which are actual customers, we are interested in the time for the next seven actual customers to arrive. Following from part (c), the expected time for the next seven actual customers to arrive is pλ7 . Adding the expected time for the first five potential customers to arrive, we get that the conditional expectation for the total time the store is open is λ 5 + pλ7 .

   - (e) The probability of no two actual customers arriving within τ time units of each other is equivalent to the probability of all nine independent interarrival times, seperating the ten actual customers, being at least τ time units apart. Thus,

      - P(no two actual customers arriving within τ time units of each other) = P([T1 ≥ τ ]<sup>9</sup> ) = e<sup>`−`9pλτ</sup> .

3. See problem 6.24, page 334 in the textbook.

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
