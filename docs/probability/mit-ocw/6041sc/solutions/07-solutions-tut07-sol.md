---
title: 07 solutions tut07 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/07-solutions-tut07-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 07 solutions tut07 sol

**Source:** `solutions/07-solutions-tut07-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Tutorial 7: Solutions

1. (a) For each round, the probability that both Alice and Bob have a loss is 13<sup>·1</sup> 3<sup>=1</sup> 9<sup>. Let random</sup> variable X represent the total number of rounds played until the first time where they both have a loss. Then X is a geometric random variable with parameter p = 1/9 and has the following PMF.


- (b) First, consider the number of games, K3 Bob played until his third loss. Random variable K3 is a Pascal random variable and has the following PMF.


In this question, we are interested in another random variable Z defined as the time at which Bob has his third loss. Note that Z = 2K3. By changing variables, we obtain


- (c) Let A be the event that Alice wins, and Let B be the event that Bob wins. The event A ∪ B is then the event that either A wins or B wins or both A and B win, and the event A ∩ B is the event that both A and B win. Suppose we observe this gambling process, and let U be a random variable indicating the number of rounds we see until at least one of them wins. Random variable U is a geometric random variable with parameter p = P (A∪ B) = 1−<sup>1</sup> 3<sup>·</sup> 3<sup>1.</sup>

Consider another random variable V representing the number of additional rounds we have to observe until the other wins. If both Alice and Bob win at the U th round, then V = 0. 2 2 3 This occurs with probability P (A ∩ B|A ∪ B) = 38 . If Alice wins the U th round, then the 9 time V until Bob wins is a geometric random variable with parameter p = 1/2 + 1/6 = 2/3. 1 2 This occurs with probability P (A ∩ B<sup>c</sup> |A ∪ B) = 383 . Likewise, if Bob wins the U th 9 round, then the time V until Alice wins is a geometric random variable with parameter 1 2 3 p = 1/2 + 1/6 = 2/3. This occurs with probability P (B ∩ A<sup>c</sup> |A ∪ B) = 38 .The number of 9 rounds until each one of them has won at least once, N is

N = U + V

The expectation of N is then:


Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

There is another approach to this problem. Consider the following partition.

A1: both win first round

A2:Only Alice wins first round

A3: Only Bob wins first round

A4: both lose first round

Event A1 occurs with probability<sup>2</sup> 3<sup>·</sup> 23 . Event A2 occurs with probability 23<sup>·</sup> 13 . Event A3 occurs with probability 31 · 32 . Event A4 occurs with probability 31 · 13 . When event A2 (A3) occurs, the distribution on the time until Bob (Alice) wins is a geometric random variable with mean 12 . When event A4 occurs, the additional time until Alice and Bob 3 win is distributed identically to that at time 0 by the fresh-start property. By the total expectation theorem,


2. Problem 6.6, page 328 in text. See text for solutions.

3. (a) The number of trains arriving on days 1, 2, and 3 is independent of the number of trains arriving on day 0. Let N denote the total number of trains that arrive on days 1, 2, and 3. Then N is a Poisson random variable with parameter 3λ = 9, and we have

P (no train on days 1,2,3 | one train on day 1) = P (no train on days 1,2,3)


- (b) The event that the next arrival is more than three days after the train arrival on day 0 is the same as the event that there are zero arrivals in the three days after the train arrival on day 0. Therefore the required probability is the same as that found in part (a), namely, `−` 9

- e .

- (c) The number of trains arriving in the first 2 days is independent of the number of trains arriving on day 4. Therefore, we have


Page 2 of 3

(Fall 2010)

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

- (d) The event that it takes more than 2 days for the 5th arrival is equivalent to the event that there are at most 4 arrivals in the first 2 days. Therefore the required probability is equal to


Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
