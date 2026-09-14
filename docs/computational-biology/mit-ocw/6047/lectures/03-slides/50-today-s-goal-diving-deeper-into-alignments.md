---
title: 'Today’s Goal: Diving deeper into alignments'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Today’s Goal: Diving deeper into alignments

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### **1. Global alignment vs. Local alignment**

   - Needleman-Wunsch and Smith-Waterman

   - Varying gap penalties and algorithmic speedups

**2. Linear-time exact string matching (expected)**

   - Karp-Rabin algorithm and semi-numerical methods

   - Hash functions and randomized algorithms

**3. The BLAST algorithm and inexact matching**

   - Hashing with neighborhood search

   - Two-hit blast and hashing with combs

**4. Deterministic linear-time exact string matching**

   - Key insight: gather more info from each comparison

   - Pre-processing, Z-algorithm, Boyer-More, KMP

55

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← The Z algorithm](49-the-z-algorithm.md) · [Up: contents](index.md)
