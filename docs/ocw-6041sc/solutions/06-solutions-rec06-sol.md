---
title: 06 solutions rec06 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/06-solutions-rec06-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 solutions rec06 sol

**Source:** `solutions/06-solutions-rec06-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 6 Solutions September 28, 2010

1. (a) The first part can be completed without reference to anything other than the die roll:


<!-- Start of picture text -->
1/4<br>n<br>0  1  2  3<br><!-- End of picture text -->

- (b) When N = 0, the coin is not flipped at all, so K = 0. When N = n for n ∈{1, 2, 3}, the coin is flipped n times, resulting in K with a distribution that is conditionally binomial. The binomial probabilities are all multiplied by 1/4 because pN (n) = 1/4 for n ∈{0, 1, 2, 3}. The joint PMF pN,K(n, k) thus takes the following values and is zero otherwise:

||k = 0|k = 1|k = 2|k = 3|
|---|---|---|---|---|
|n = 0|1/4|0|0|0|
|n = 1|1/8|1/8|0|0|
|n = 2|1/16|1/8|1/16|0|
|n = 3|1/32|3/32|3/32|1/32|


- (c) Conditional on N = 2, K is a binomial random variable. So we immediately see that


This is a normalized row of the table in the previous part.


- (d) To get K = 2 heads, there must have been at least 3 coin tosses, so only N = 3 and N = 4 have positive conditional probability given K = 2.


Similarly, pN `|` K(3 | 2) = 3/5.

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)


<!-- Start of picture text -->
pN | K  ( n |2)<br>3/5<br>2/5<br>n<br>2 3<br><!-- End of picture text -->

2. (a) x = 0 maximizes E[Y | X = x] since


(b) y = 3 maximizes var(X | Y = y) since


(c)


(d) By traversing the points top to bottom and left to right, we obtain


Conditioning on A removes the point masses at (0, 1) and (0, 3). The conditional probability of each of the remaining point masses is thus 1/6, and


3. See the textbook, Example 2.17, pages 105–106.

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
