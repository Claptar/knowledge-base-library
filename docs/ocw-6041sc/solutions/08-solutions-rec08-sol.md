---
title: 08 solutions rec08 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/08-solutions-rec08-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 08 solutions rec08 sol

**Source:** `solutions/08-solutions-rec08-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

# Recitation 8 Solutions October 5, 2010

1. (a) We know that the PDF must integrate to 1. Therefore we have


From this we conclude γ = 1/6.

(b) To find the CDF, we integrate:


2. See textbook, Problem 3.9, page 187.

3. (a) For x ≥ 0,


(b) The key step in the following computation uses integration by parts, whereby

(c) Integrating by parts with u = x<sup>2</sup> and v = −e<sup>−λx</sup> in the second line below gives


Combining with the previous computation, we obtain


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis

(Fall 2010)

- (d) The maximum of a set is upper bounded by z when each element of the set is upper bounded by z. Thus for any positive z,


where the third equality uses the independence of X1, X2, and X3. Thus,


Differentiating the CDF gives the desired PDF:

- (e) The minimum of a set is lower bounded by w when each element of the set is lower bounded by w. Thus for any positive w,


where the third equality uses the independence of X1 and X2. Thus,


We can recognize this as the CDF of an exponential random variable with parameter 2λ. The PDF is


Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
