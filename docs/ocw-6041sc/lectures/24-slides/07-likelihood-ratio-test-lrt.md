---
title: Likelihood ratio test (LRT)
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/24-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Likelihood ratio test (LRT)

**Source:** `lectures/24-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Bayesian case (MAP rule): choose _H_ 1 if: **P** ( _H_ 1 _| X_ = _x_ ) _>_ **P** ( _H_ 0 _| X_ = _x_ )

or


(likelihood ratio test)

      - Nonbayesian version: choose _H_ 1 if

- Types of errors:

- **Type I** ( **false rejection** , false alarm): _H_ 0 true, but rejected

   - _α_ ( _R_ ) = **P** ( _X ∈ R_ ; _H_ 0)

- **Type II** ( **false acceptance** , missed detection): _H_ 0 false, but accepted


   - threshold _ξ_ trades off the two types of error

   - choose _ξ_ so that **P** (reject _H_ 0; _H_ 0) = _α_ (e.g., _α_ = 0 _._ 05)

- _β_ ( _R_ ) = **P** ( _X ￿∈ R_ ; _H_ 1)

2

MIT OpenCourseWare http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Binary hypothesis testing](06-binary-hypothesis-testing.md) · [Up: contents](index.md)
