---
title: What is missing? (5) Returning the actual path!
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# What is missing? (5) Returning the actual path!

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- We know how to compute the best score

      - Simply the number at the bottom right entry

   - But we need to remember where it came from

      - Pointer to the choice we made at each step

   - Retrace path through the matrix

      - Need to remember all the pointers

- x1 …………………………  xM


Time needed:  O(m*n) Space needed:  O(m*n)

44

---

[← Genome alignment in an excel spreadsheet](36-genome-alignment-in-an-excel-spreadsheet.md) · [Up: contents](index.md) · [Goal: Sequence Alignment / Dynamic Programming →](38-goal-sequence-alignment-dynamic-programming.md)
