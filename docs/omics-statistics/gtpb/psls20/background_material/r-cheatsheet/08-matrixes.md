---
title: Matrixes
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/r-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Matrixes

**Source:** [`background_material/r-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

`m <- matrix(x, nrow = 3, ncol = 3)` Create a matrix from x.

`t(m) m[2,  ]` - Select a row Transpose `m %*% n m[ , 1]` - Select a  column Matrix Multiplication `solve(m, n) m[2, 3]` -  Select an element Find x in: m * x = n

---

[← The Environment](07-the-environment.md) · [Up: contents](index.md) · [Lists →](09-lists.md)
