---
title: Knuth-Morris-Pratt running time
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Knuth-Morris-Pratt running time

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

T=


<!-- Start of picture text -->
P=  a b c  f  a b c  d  e<br>a b c  f  a b c d e<br><!-- End of picture text -->

- Number of comparisons bounded by characters in T

   - Every comparison starts at text position where last comparison ended

   - Every shift results in at most one extra comparison

   - – At most |T| shifts  Running time bounded by 2*|T|

52

---

[← Knuth-Morris-Pratt algorithm](46-knuth-morris-pratt-algorithm.md) · [Up: contents](index.md) · [Boyer-Moore algorithm →](48-boyer-moore-algorithm.md)
