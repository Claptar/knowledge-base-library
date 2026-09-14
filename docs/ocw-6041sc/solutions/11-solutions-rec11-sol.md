---
title: 11 solutions rec11 sol
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/11-solutions-rec11-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 solutions rec11 sol

**Source:** `solutions/11-solutions-rec11-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

# Recitation 11 Solutions October 14, 2010

1. We need to apply the version of Bayes rule for a discrete random variable conditioned on a continuous random variable:


Specifically,


The final manipulations are to ease interpretations for p → 0<sup>+</sup> , p → 1<sup>−</sup> , λ → 0<sup>+</sup> , and λ →∞. Easily


these make sense because the observation z should become unimportant when value of X becomes certain without it. Next,


this makes sense because λ →∞ makes the Y negligible.

2. We need to apply the version of Bayes rule for a continuous random variable conditioned on a discrete random variable:


For x = 0 and q ∈ [0, 1],


Page 1 of 2

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis (Fall 2010)

For x = 1 and q ∈ [0, 1],


The distributions fQ(q), fQ|X(q | 0), and fQ|X(q | 1) are all in the family of beta distributions, which arise again in Chapter 8.

3. Because of the definition of g, the random variable Y takes on only nonnegative values. Thus fY (y) = 0 for any negative y. For y > 0,


Taking the derivative of FY (y) (and using the chain rule),

Page 2 of 2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
