---
title: 1 The Sinusoidal Model
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 The Sinusoidal Model

**Source:** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

By the sinusoidal model, we refer to:


This is a simple model for time series data which show strong periodicity (like the sunspots data).

The unknown parameters in this model are _β_ 0 _, β_ 1 _, β_ 2 _, σ_ as well as the frequency parameter _f_ . If _f_ is assumed to be known, then clearly (1) is a multiple linear regression model:


with


When _f_ is unknown, this is a nonlinear regression model.

The function _t �→ β_ 0 + _β_ 1 cos(2 _πft_ ) + _β_ 2 sin(2 _πft_ ) is called a sinusoid. Before proceeding further, let us look at some basic properties and terminology related to sinusoids.

---

[Up: contents](index.md) · [2 The Sinusoid →](02-2-the-sinusoid.md)
