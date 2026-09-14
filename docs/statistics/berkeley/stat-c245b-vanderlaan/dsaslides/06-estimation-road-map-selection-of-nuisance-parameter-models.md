---
title: 'Estimation Road Map: Selection of nuisance parameter models'
source: https://vanderlaan-lab.org/teach-files/dsaslides.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/dsaslides.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Estimation Road Map: Selection of nuisance parameter models

**Source:** [`dsaslides.pdf`](https://vanderlaan-lab.org/teach-files/dsaslides.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Selecting the nuisance parameter models with CV/DSA algorithm

      - υ = {g(A|V ), g(A|W ), Q(Y |A, W ), Q(Y<sup>2</sup> |A, W )}

   - Since these nuisance parameters are either observed data densities or regressions, we can estimate them with the loss-based estimation approach based on either the squared error loss function, or the minus log loss function.

Nov. 8, 2004

16

---

[← Estimation Road Map: D/S/A algorithm for computing the optimal index set](05-estimation-road-map-d-s-a-algorithm-for-computing-the-optima.md) · [Up: contents](index.md) · [R-package cvDSA →](07-r-package-cvdsa.md)
