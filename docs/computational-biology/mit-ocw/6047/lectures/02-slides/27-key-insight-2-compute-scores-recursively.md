---
title: 'Key insight #2: compute scores recursively'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Key insight #2: compute scores recursively

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
S1<br>A  C  G  T  C  A  T  C  A<br>S2<br>T  A  G  T  G  T  C  A<br>S1<br>A  C  G  T  C  A  T  C  A<br>S2<br>T  A  G  T  G  T  C  A<br>S1<br>A  C  G  T<br>S2<br>T  A  G  T  G<br><!-- End of picture text -->

 Compute alignment of CGT vs. TG exactly once

30

---

[← Key insight #1: Score is additive, smaller to larger](26-key-insight-1-score-is-additive-smaller-to-larger.md) · [Up: contents](index.md) · [Key insight #3: sub-problems are repeated  reuse! →](28-key-insight-3-sub-problems-are-repeated-reuse.md)
