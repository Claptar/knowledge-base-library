---
title: 'Key insight #1: Score is additive, smaller to larger'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Key insight #1: Score is additive, smaller to larger

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_i_ S1 <mark>A C G T C A T C A</mark> S2 <mark>T A G T G T C A</mark> _j_

- Compute best alignment recursively – For a given aligned pair _(_ **_i, j_** _)_ , the best alignment is: •    Best alignment of S1[1..i]     and S2[1..j]

   - +  Best alignment of S1[    i..n] and S2[    j..m]

   - – Proof:  cut-and-paste argument (see 6.046)

_i i_ S1 <mark>A C G T C A T C A</mark> S2 <mark>T A G T G T C A</mark> _j j_ This allows a single recursion (top-left to bottom-right) instead of two recursions (middle-to-outside top-down)

29

---

[← (3) How do we apply dynamic programming to sequence alignment ?](25-3-how-do-we-apply-dynamic-programming-to-sequence-alignment.md) · [Up: contents](index.md) · [Key insight #2: compute scores recursively →](27-key-insight-2-compute-scores-recursively.md)
