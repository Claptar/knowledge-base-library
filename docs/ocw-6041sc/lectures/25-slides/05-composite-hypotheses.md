---
title: Composite hypotheses
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
source_file: sources/ocw-6041sc/lectures/25-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Composite hypotheses

**Source:** `lectures/25-slides.pdf` from [ocw-6041sc](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Got _S_ = 472 heads in _n_ = 1000 tosses; is the coin fair?

- _H_ 0 : _p_ = 1 _/_ 2 versus _H_ 1 : _p_ = 1 _/_ 2

- Pick a **“statistic”** (e.g., _S_ )

- Pick shape of **rejection region** (e.g., _|S − n/_ 2 _| > ξ_ )

- Choose **significance level** (e.g., _α_ = 0 _._ 05)

- Pick **critical value** _ξ_ so that:

**P** (reject _H_ 0; _H_ 0) = _α_

Using the CLT:

   - **P** ( _|S −_ 500 _| ≤_ 31; _H_ 0) _≈_ 0 _._ 95; _ξ_ = 31

- In our example: _|S −_ 500 _|_ = 28 _< ξ H_ 0 **not rejected** (at the 5% level)

---

[← Example (test on normal variance)](04-example-test-on-normal-variance.md) · [Up: contents](index.md) · [Is my die fair? →](06-is-my-die-fair.md)
