---
title: 16 Law of iterated expectations
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/exams/02-exam-quiz02-revi.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 16 Law of iterated expectations

**Source:** `exams/02-exam-quiz02-revi.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Graphical Method:

- put the PMFs (or PDFs) on top of each other

- flip the PMF (or PDF) of Y

- shift the flipped PMF (or PDF) of Y by w

- cross-multiply and add (or evaluate the integral)

In particular, if X, Y are independent and normal, then W = X + Y is normal.

E[X|Y = y] = f (y) is a number. E[X|Y ] = f (Y ) is a random variable (the expectation is taken with respect to X). To compute E[X|Y ], first express E[X|Y = y] as a function of y. Law of iterated expectations: E[X] = E[E[X|Y ]] (equality between two real numbers)

19

20

---

[← 14 Derived distributions 15 Convolution](10-14-derived-distributions-15-convolution.md) · [Up: contents](index.md) · [17 Law of Total Variance →](12-17-law-of-total-variance.md)
