---
title: 01 exam quiz01 f09
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/01-exam-quiz01-f09.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 01 exam quiz01 f09

**Source:** `exams/01-exam-quiz01-f09.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Quiz 1 | Fall 2009)

**Summary of Results for Special Random Variables Discrete Uniform over** [ _a, b_ ] **:**


**Bernoulli with Parameter** _p_ **:** (Describes the success or failure in a single trial.)


**Binomial with Parameters** _p_ **and** _n_ **:** (Describes the number of successes in _n_ independent Bernoulli trials.)


**Geometric with Parameter** _p_ **:** (Describes the number of trials until the first success, in a sequence of independent Bernoulli trials.)


1

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis**

(Quiz 1 | Fall 2009)

**Problem B:** (98 points) As a way to practice his probability skills, Bob goes apple picking. The orchard he goes to grows two varieties of apples: gala and honey crisp.

The **proportion of the gala apples** in the orchard is _p_ (0 _< p <_ 1), the **proportion of the honey crisp apples** is 1 _− p_ . The number of apples in the orchard is so large that you can assume that picking a few apples does not change the proportion of the two varieties.

Independent of all other apples, the probability that a randomly picked **gala apple is ripe** is _g_ and the probability that a randomly picked **honey crisp apple is ripe** is _h_ .

1. **(10 points)** Suppose that Bob picks an apple at random (uniformly) and eats it. Find the probability that it was a **ripe gala** apple.

**Note:** Parts 2 and 3 below can be done independently.

2. Suppose that Bob picks _n_ apples at random (independently and uniformly).

   - (a) **(10 points)** Find the probability that exactly _k_ of those are **gala apples.**

   - (b) Suppose that there are **exactly** _k_ **gala apples** among the _n_ apples Bob picked. Caleb comes by and gives Bob a **ripe gala** apple to add to his bounty. Bob then picks an apple at random from the _n_ + 1 apples and eats it.

      - (i) **(12 points)** What is the probability that it was a **ripe apple?**

      - (ii) **(12 points)** What is the probability that it was a **gala apple if it was ripe?**

   - (c) **(10 points)** Let _n_ = 20, and suppose that Bob picked exactly 10 gala apples. What is the probability that the first 10 apples that Bob picked were all gala?

3. Next, Bob tries a different strategy. He starts with a tree of the **gala** variety and picks apples at random from that tree. Once Bob picks an apple off the tree, he carefully examines it to make sure it is ripe. Once he comes across an apple that is not ripe, he moves to **another gala tree.** He does this until he encounters an unripe apple on that second tree. Assume that each tree has a very large, essentially infinite, number of apples.

   - (a) **(10 points)** Let _Xi_ be the **number of apples** Bob picks off the _i_ th tree, ( _i_ = 1 _,_ 2). Write down the PMF, expectation, and variance of _Xi_ .

   - (b) **(12 points)** For _i_ = 1 _,_ 2, let _Yi_ be the **total** number of **ripe apples** Bob picked from the first _i_ trees. Find the expectation and the variance of _Y_ 2. (Note that _Y_ 1 = _X_ 1 _−_ 1 and _Y_ 2 = ( _X_ 1 _−_ 1) + ( _X_ 2 _−_ 1).)

   - (c) **(12 points)** Find the joint PMF of _Y_ 1 and _Y_ 2.

   - (d) In the following, answer just “yes” or “no.” (Explanations will not be taken into account in grading.)

      - (i) **(5 points)** Are _X_ 1 and _Y_ 2 independent?

      - (ii) **(5 points)** Are _X_ 2 and _Y_ 1 independent?

Each question is repeated in the following pages. Please write your answer on the appropriate page.

2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2009)

1. **(10 points)** Suppose that Bob picks an apple at random (uniformly) and eats it. Find the probability that it was a **ripe gala** apple.

**Note:** Parts 2 and 3 can be done independently.

2. Suppose that Bob picks _n_ apples at random (independently and uniformly).

   - (a) **(10 points)** Find the probability that exactly _k_ of those are **gala apples.**

3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2009)

- (b) Suppose that there are **exactly** _k_ **gala apples** among the _n_ apples Bob picked. Caleb comes by and gives Bob a **ripe gala** apple to add to his bounty. Bob then picks an apple at random from the _n_ + 1 apples and eats it.

   - (i) **(12 points)** What is the probability that it was a **ripe apple?**

4

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2009)

(ii) **(12 points)** What is the probability that it was a **gala apple if it was ripe?**

5

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2009)

- (c) **(10 points)** Let _n_ = 20, and suppose that Bob picked exactly 10 gala apples. What is the probability that the first 10 apples that Bob picked were all gala?

6

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2009)

3. Next, Bob tries a different strategy. He starts with a tree of the **gala** variety and picks apples at random from that tree. Once Bob picks an apple off the tree, he carefully examines it to make sure it is ripe. Once he comes across an apple that is not ripe, he moves to **another gala tree.** He does this until he encounters an unripe apple on that second tree. Assume that each tree has a very large, essentially infinite, number of apples.

   - (a) **(10 points)** Let _Xi_ be the **number of apples** Bob picks off the _i_ th tree, ( _i_ = 1 _,_ 2). Write down the PMF, expectation, and variance of _Xi_ .

   - (b) **(12 points)** For _i_ = 1 _,_ 2, let _Yi_ be the **total** number of **ripe apples** Bob picked from the first _i_ trees. Find the expectation and the variance of _Y_ 2. (Note that _Y_ 1 = _X_ 1 _−_ 1 and _Y_ 2 = ( _X_ 1 _−_ 1) + ( _X_ 2 _−_ 1).)

7

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2009)

- (c) **(12 points)** Find the joint PMF of _Y_ 1 and _Y_ 2.

8

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** (Quiz 1 | Fall 2009)

- (d) In the following, answer just “yes” or “no.” (Explanations will not be taken into account in grading.)

   - (i) **(5 points)** Are _X_ 1 and _Y_ 2 independent?

   - (ii) **(5 points)** Are _X_ 2 and _Y_ 1 independent?

9

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
