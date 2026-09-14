---
title: Dimensionless variables
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/15-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Dimensionless variables

**Source:** `lecture-outlines/15-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

First we will introduce dimensionless variables to make the algebra simpler. Time will be normalized to (γa)<sup>-1</sup> and the spatial coordinate x will be measured in terms of the distance that the activator will diffuse in time (γa)<sup>-1</sup> :


**[VIII.3]**

Substituting this in [VIII.1] yields:


**[VIII.4]**

We still have the freedom to the normalize a and i:


**[VIII.5]**

Substituting this in [VIII.4] gives:


**[VIII.6]**

By choosing


**[VIII.7]**

[VIII.6] finally reduces to:


**[VIII.8]**

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

44

where


P and Q are a measure of the diffusion coefficient and decay rate relative to the activator properties. R is the ratio of the autocatalytic activator synthesis (ka) and the constant synthesis (‘leakyness’, ra).

---

[← VIII Local excitation, global inhibition model](01-viii-local-excitation-global-inhibition-model.md) · [Up: contents](index.md) · [Spatially homogeneous solutions →](03-spatially-homogeneous-solutions.md)
