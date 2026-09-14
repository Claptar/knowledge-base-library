---
title: Introduction
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/fin-f09-sol-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `solutions/fin-f09-sol-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

�C���� 9��� {�������� � C��� �����

**Problem 3.** (25 points)

- (a) (5 points)

The recurrent states are _{_ 3,4 _}_ .

## (b) (5 points)

The 2-step transition probability from State 2 to State 4 can be found by enumerating all the possible sequences. They are _{_ 2 _→_ 1 _→_ 4 _}_ and _{_ 2 _→_ 4 _→_ 4 _}_ . Thus,


- (c) (5 points) Generally,


Since states 3 and 4 are absorbing states, this expression simplifies to


Alternatively,


- (d) (5 points)

The steady-state probabilities do not exist since there is more than one recurrent class. The long-term state probabilities would depend on the initial state.

## (e) (5 points)

To find the probability of being absorbed by state 4, we set up the absorption probabilities. Note that _a_ 4 = 1 and _a_ 3 = 0.


Solving these equations yields _a_ 1 = <u>38</u> .

1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** �C���� 9��� {�������� � C��� �����

## **Problem 4.** (30 points)

## (a) (5 points)

Given the problem statement, we can treat Al, Bonnie, and Clyde’s running as 3 independent Poisson processes, where the arrivals correspond to lap completions and the arrival rates indicate the number of laps completed per hour. Since the three processes are independent, we can merge them to create a new process that captures the lap completions of all three runners. This merged process will have arrival rate _λM_ = _λA_ + _λB_ + _λC_ = 68. The total number of completed laps, _L_ , over the first hour is then described by a Poisson PMF with _λM_ = 68 and _τ_ = 1:


## (b) (5 points)

Let _L_ be the total number of completed laps over the first hour, and let _Ci_ be the number of cups of water consumed at the end of the _i_ th lap. Then, the total number of cups of water consumed is


which is a sum of a random number of i.i.d. random variables. Thus, we can use the law of iterated expectations to find


## (c) (5 points)

Let _X_ be the number of laps (out of 72) after which Al drank 2 cups of water. Then, in order for him to drink at least 130 cups, we must have


which implies that we need


Now, let _Xi_ be i.i.d. Bernoulli random variables that equal 1 if Al drank 2 cups of water following his _i_ th lap and 0 if he drank 1 cup. Then


_X_ is evidently a binomial random variable with _n_ = 72 and _p_ = 2 _/_ 3, and the probability we are looking for is


This expression is difficult to calculate, but since we’re dealing with the sum of a relatively large number of i.i.d. random variables, we can invoke the Central Limit Theorem to approx­ imate this probability using a normal distribution. In particular, we can approximate _X_ as

2

---

[Up: contents](index.md) · [Fin f09 sol solutions Part 02 — →](02-fin-f09-sol-solutions-part-02.md)
