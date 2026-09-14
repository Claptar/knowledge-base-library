---
title: 22 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/22-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 22 slides

**Source:** `recitations/22-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Recitation 22 November 30, 2010

Examples 8.2, 8.7, 8.12, and 8.15 in the textbook

Romeo and Juliet start dating, but Juliet will be late on any date by a random amount X, uniformly distributed over the interval [0, θ]. The parameter θ is unknown and is modeled as the value of a random variable Θ, uniformly distributed between zero and one hour.

- (a) Assuming that Juliet was late by an amount x on their first date, how should Romeo use this information to update the distribution of Θ?

- (b) How should Romeo update the distribution of Θ if he observes that Juliet is late by x1, . . . , xn on the first n dates? Assume that Juliet is late by a random amount X1, . . . , Xn on the first n dates where, given θ, X1, . . . , Xn are uniformly distributed between zero and θ and are conditionally independent.

- (c) Find the MAP estimate of Θ based on the observation X = x.

- (d) Find the LMS estimate of Θ based on the observation X = x.

- (e) Calculate the conditional mean squared error for the MAP and the LMS estimates. Compare your results.

- (f) Derive the linear LMS estimator of Θ based on X.

- (g) Calculate the conditional mean squared error for the linear LMS estimate. Compare your answer to the results of part (e).

Page 1 of 1

Textbook problems are courtesy of Athena Scientific, and are used with permission.

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
