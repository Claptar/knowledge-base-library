---
title: Takis exercises Part 26 —
source: https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf
source_file: sources/berkeley-stat150/aldous-legacy/takis_exercises.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Takis exercises Part 26 —

**Source:** [`takis_exercises.pdf`](https://www.stat.berkeley.edu/~aldous/150/takis_exercises.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Show that the stationary distribution on any (undirected) graph whose vertices have all the same degree is uniform.

Solution. We know that


where d(i) is the degree of i, and c some constant. Indeed, the detailed balance equations

π(i)p(i, j) = π(j)p(j, i), i̸ = j

are trivially satisfied because p(i, j) = 1/d(i), p(j, i) = 1/d(i), by definition. So when d(i) = d = constant, the distribution π is uniform.

---

[← Takis exercises Part 25 —](25-takis-exercises-part-25.md) · [Up: contents](index.md) · [Takis exercises Part 27 — →](27-takis-exercises-part-27.md)
