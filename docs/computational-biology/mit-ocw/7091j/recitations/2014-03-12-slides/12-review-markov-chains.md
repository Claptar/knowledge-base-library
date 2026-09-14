---
title: 'Review: Markov Chains'
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-03-12-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Review: Markov Chains

**Source:** `recitations/2014-03-12-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Defined by a set of _n_ possible states s1, ..., sn at each timepoint

- Markov models follow the **Markov Property** :  Transition from state _i_ to _j_ (with probability P _i,j_ ) depends _only_ on the previous state, not any states before that. In other words, the future is conditionally independent of the past given the present:


**Example** :  if we know individual 3’s genotype, there’s no additional information that individuals 1 and 2 can give us about 5’s genotype.  So current state (individual 5's genotype) depends only on previous state (individuals 3 and 4).

14

---

[← Gibbs Sampler](11-gibbs-sampler.md) · [Up: contents](index.md) · [Hidden Markov Models →](13-hidden-markov-models.md)
