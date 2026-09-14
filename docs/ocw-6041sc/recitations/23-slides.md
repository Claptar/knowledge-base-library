---
title: 23 slides
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/recitations/23-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 23 slides

**Source:** `recitations/23-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science 6.041/6.431: Probabilistic Systems Analysis <u>(Fall</u> 2010)

Recitation 23 December 2, 2010

1. Example 9.1, page 463 in textbook

   - Romeo and Juliet start dating, but Juliet will be late on any date by a random amount X, uniformly distributed over the interval [0, θ]. The parameter θ is unknown. Assuming that Juliet was late by an amount x on their first date, find the ML estimate of θ based on the observation X = x.

2. Example 9.4, page 464 in textbook

   - Estimate the mean µ and variance v of a normal distribution using n independent observations X1, . . . , Xn.

3. Example 9.8, page 474 of textbook

   - We would like to estimate the fraction of voters supporting a particular candidate for office. We collect n independent sample voter responses X1, . . . , Xn, where Xi is viewed as a Bernoulli random variable, with Xi = 1 if the ith voter supports the candidate. We conducted a poll of 1200 people in North Carolina, and found that 684 were supporting the candidate. We would like to construct a 95% confidence interval for θ, the proportion of people who support the candidate. As we saw in lecture, using the central limit theorem, an (approximate) 95% confidence interval can be defined as


where v = Var(Xi), and Θ<sup>ˆ</sup> n = (X1 + . . . + Xn)/n. Unfortunately, we don’t know the value for v. Construct confidence intervals for θ using the following three ways of estimating or bounding the value for v (in each case simply assume that v is equal to the given estimate; note that this is a further approximation in cases (a) and (b)).

(a)


(b)


(c) The most conservative upper bound for the variance.

Textbook problems are courtesy of Athena Scientific, and are used with permission.��

Page 1 of 1

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
