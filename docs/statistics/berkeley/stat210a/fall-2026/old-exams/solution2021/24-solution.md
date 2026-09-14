---
title: Solution
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2021.pdf
source_file: sources/berkeley-stat210a/fall-2026/old-exams/solution2021.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Solution

**Source:** [`old-exams/solution2021.pdf`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/old-exams/solution2021.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

First, we consider how to implement a Gibbs step where _k_ is held fixed and _γ_ 0 or _γ_ 1 is updated; this follows from part (b) where we showed


To update _k_ , we need to first calculate


15

Then, we have


Thus, to update _k_ we calculate ( _ω_ 4 _, ω_ 5 _, ω_ 6) and sample _k_ from a distribution proportional to that distribution. To sum up the algorithm, we can initialize _k_<sup>(0)</sup> and then take


16

---

[← Solution](23-solution.md) · [Up: contents](index.md)
