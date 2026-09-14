---
title: PIQ model of TF binding
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/18-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PIQ model of TF binding

**Source:** `lectures/18-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- The   genome   is   modeled   as   the   sum   of   smooth   terms   (λi) and   factor   specific   terms.

_ci_ ~ _Poisson_ (exp(λ _i_ +δ _j_ γ _i_ ))

λ ~ _MVN_ (µ0, Σ)

- γi is   the   factor   specific   profile,

- δj   is   a   binding   indicator.

- Each   factor’s   binding   is   calculated   as   a   log-­‐likelihood   ra'o amer   adjus'ng   for   effects   of   nearby   factor   profiles.

- • Profiles   are   es'mated   via   the   E-­‐M   algorithm.

Chroma'n   Structure

23

---

[← 18 slides Part 11 —](11-18-slides-part-11.md) · [Up: contents](index.md) · [Likelihood ra/o tes/ng for TF binding →](13-likelihood-ra-o-tes-ng-for-tf-binding.md)
