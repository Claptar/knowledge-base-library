---
title: Markov Models (Chains)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Markov Models (Chains)

**Source:** `recitations/2014-02-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Defined by a set of n possible states s1, ..., sn at each timepoint.

- **Markov property:** Transition from state _i_ to _j_ (with probability P _i,j_ ) depends _only_ on the previous state, not any states before that. In other words, the future is conditionally independent of the past given the present:


- If at time _t_ the probability distribution over the _n_ states is


what is the probability of being in state _i_ at time _t_ +1?


8

---

[← Markov Models (Chains)](04-markov-models-chains.md) · [Up: contents](index.md) · [Markov Chains →](06-markov-chains.md)
