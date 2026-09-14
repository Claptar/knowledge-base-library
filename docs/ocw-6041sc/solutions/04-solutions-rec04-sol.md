---
title: 04 solutions rec04 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/04-solutions-rec04-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 04 solutions rec04 sol

**Source:** `solutions/04-solutions-rec04-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 4 Solutions September 21, 2010

1. The sample space consists of all possible choices for the birthday of each person. Since there are n persons, and each has 365 choices for their birthday, the sample space has 365<sup>n</sup> elements. Let us now consider those choices of birthdays for which no two persons have the same birthday. Assuming that n ≤ 365, there are 365 choices for the first person, 364 for the second, etc., for a total of 365 · 364 · · · (365 − n + 1). Thus,


It is interesting to note that for n as small as 23, the probability that there are two persons with the same birthday is larger than 1/2.


<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>0 20 40 60 80<br>n<br>10 0<br>10 -1<br>10 -2<br>10 -3<br>10 -4<br>10 -5<br>10 -6<br>10 -7<br>10 -8<br>10 -9<br>10 -10<br>0 20 40 60 80 100 120 140<br>n<br>Image by MIT OpenCourseWare.<br>P(n)<br>P(n)<br><!-- End of picture text -->

2. As we have done before, we will count the number of favorable positions in which we can safely place 8 rooks, and then divide this by the total number of positions for 8 rooks on a 8 × 8 chessboard. First we count the number of favorable positions for the rooks. We will place the

Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

rooks one by one. For the first rook, there are no constraints, so we have 64 choices. Placing this rook, however, eliminates one row and one column. Thus for our second rook, we can imagine that the illegal column and row have been removed, thus leaving us with a 7 × 7 chessboard, and thus with 49 choices. Similarly, for the third rook we have 36 choices, for the fourth 25, etc... There are 64 · 63 · · · 57 total ways we can place 8 rooks without any restrictions, and therefore the probability we are after is:


3. See textbook, Problem 1.61, page 69.

4. The group of n slots is divided into segments of length n1, . . . , nr slots. The n items can be arranged in n! ways, where each arrangement corresponds to a partition into the r segments. But all arrangements within a single segment lead to the same partition, where there are ni! ways to arrange the items within ith segment. Thus, for each segment we must divide by the number of ways to arrange the items within that segment. The solution is then:


5. The probability of drawing a particular sequence of balls containing exactly ni of color i balls is pn1 1<sup>· · · p</sup> r<sup>n</sup> r<sup>.The number of possible sequences containing</sup> ni<sup>of color</sup> i<sup>balls is the number of ways</sup> to form a partition of n distinct slots into subsets of cardinality n1, . . . , nr which is �n1,...,nn r�<sup>.</sup> Therefore, the probability of obtaining exactly ni balls of color i is:


Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
