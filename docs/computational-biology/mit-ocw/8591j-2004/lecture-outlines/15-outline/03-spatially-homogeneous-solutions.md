---
title: Spatially homogeneous solutions
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/15-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Spatially homogeneous solutions

**Source:** `lecture-outlines/15-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Version [VIII.8] only contain three parameters (P,Q,R) whereas [VIII.1] contained 9 parameters. For now let’s try to find a solution to [VIII.8] that is spatially homogeneous ( ∂ / ∂ _s_ = 0 ). In this case, the steady state solution is:


Is this solution stable? The stability matrix evaluated at the fixed point is:


Therefore [VIII.10] represents a stable solution when the trace of this matrix is negative and the determinant is positive:


As Q is positive by definition [VIII.9] the first inequality characterizes a unique constant solution that is stable against small spatially homogeneous perturbations.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

45

---

[← Dimensionless variables](02-dimensionless-variables.md) · [Up: contents](index.md) · [Spatially inhomogeneous solutions →](04-spatially-inhomogeneous-solutions.md)
