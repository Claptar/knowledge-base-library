---
title: 13 solutions
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/13-solutions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 13 solutions

**Source:** `solutions/13-solutions.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 13 Solutions October 21, 2010

1. (a) We begin by writing the definition for E[Z | X, Y ]


Since E[Z | X, Y ] is a function of the random variables X and Y , and is equal to E[Z | X = x, Y = y] whenever X = x and Y = y, which happens with probability pX,Y (x, y), using the expected value rule, we have


- (b) We start with the definition for E[Z | X, Y ] which is a function of the random variables X and Y , and is equal to E[Z | X = x, Y = y] whenever X = x and Y = y, so


Proceeding as above, but conditioning on the event X = x, we have


Since this is true for all possible values of x, we have E�E[Z | Y, X] | X� = E[Z | X].

(c) We take expectations of both sides of the formula in part (b) to obtain


By the law of iterated expectations, the left-hand side above is E[Z], which establishes the desired result.

2. Let Y be the length of the piece after we break for the first time. Let X be the length after we break for the second time.

Page 1 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

(a) The law of iterated expectations states:


(b) We use the Law of Total Variance to find var(X):


Recall that the variance of a uniform random variable distributed over [a, b] is (b − a)<sup>2</sup> /12. Since Y is uniformly distributed over [0, ℓ], we have


We know that E[X | Y ] = Y/2, and so

Also,


Combining these results, we obtain


3. Let Xi denote the number of widgets in the i<sup>th</sup> box. Then T =<sup>�N</sup> i=1<sup>Xi.</sup>


Page 2 of 3

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

and,


Page 3 of 3

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
