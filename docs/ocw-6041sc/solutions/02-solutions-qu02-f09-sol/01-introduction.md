---
title: Introduction
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/solutions/02-solutions-qu02-f09-sol.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** `solutions/02-solutions-qu02-f09-sol.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Massachusetts Institute of Technology Department of Electrical Engineering & Computer Science **6.041/6.431: Probabilistic Systems Analysis** <u>(Quiz 2 Solutions | Fall 2009)</u>

### (e) (7 points)

In the new universe in which _X_ = 2, we are asked to compute the conditional PDF of _Y_ given the event _Y ≥_ 3.


We first calculate the **P** ( _Y ≥_ 3 _| X_ = 2).


where _FY |X_ (3 2) _|_ is the CDF of an exponential random variable with _λ_ = 2 evaluated at _y_ = 3. Substituting the values of _fY |X_ ( _y |_ 2) and **P** ( _Y ≥_ 3 _| X_ = 2) yields


Alternatively, _fY |X_ ( _y |_ 2) is an exponential random variable with _λ_ = 2. To compute the conditional PMF _fY |X,Y ≥_ 3<sup>(</sup><sup>_y|_2), we can apply the memorylessness property of an exponential</sup> variable. Therefore, this conditional PMF is also an exponential random variable with _λ_ = 2, but it is shifted by 3.

- (f) (7 points)

Let’s define _Z_ = _e_<sup>2</sup><sup>_X_</sup> . Since _X_ is an exponential random variable that takes on non-negative values ( _X ≥_ 0) _, Z ≥_ 1. We find the PDF of _Z_ by first computing its CDF.


The CDF of Z is:


1

---

[Up: contents](index.md) · [02 solutions qu02 f09 sol Part 02 — →](02-02-solutions-qu02-f09-sol-part-02.md)
