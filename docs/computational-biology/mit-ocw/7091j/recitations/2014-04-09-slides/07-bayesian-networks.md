---
title: Bayesian Networks
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-04-09-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Bayesian Networks

**Source:** `recitations/2014-04-09-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- If we have 3 binary variables A, B, C that we can observe, how many variables do we need to fully specify joint probabilit P(A=a,B=b,C=c)   in the following situtaPons:

   - A,B,C   are all independent of each other?

      - P(A=a,B=b,C=c)   = PA(a) PB(b)PC(c) 3 parameters (more generally, _n_ for _n_ binary variables since 1 probability (prob. of ON)   needed for each)

   - Cannot assume any independencies?

      - Need   all possible combinaPons of A,B,C   = 2<sup>3</sup> -­‐1 (= 2<sup>_n_</sup> -­‐1 for _n_ binary variables since there are 2<sup>_n_</sup> combinaPons, but last one is determined since all probabiliPes must sum to 1)

   - The Bayesian network tells us about independencies between variables, and allows us to factor the joint probability accordingl

- A Bayesian networks is a way of represenPng a set of random variables and their condiPonal dependencies. Consists of:

   1. Directed (acyclic) graph over the variables

   2. Associated probability distribuPons:

      - Prior probabiliPes of all root nodes and

      - CondiPonal probabiliPes of all child nodes given their parents

8

---

[← Yeast Two-­‐Hybrid (Y2H)](06-yeast-two--hybrid-y2h.md) · [Up: contents](index.md) · [Bayesian Networks →](08-bayesian-networks.md)
