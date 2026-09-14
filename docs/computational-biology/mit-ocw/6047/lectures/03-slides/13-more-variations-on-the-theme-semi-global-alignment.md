---
title: 'More variations on the theme: semi-global alignment'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# More variations on the theme: semi-global alignment

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### • Sequence alignment variations Global Local


###### Complete alignment

Stretches of similarity

###### Semi-global


No end-gap penalty

Initialization

Iteration:max

Termination

Top row or Top left Top row/left col. left column 0 F(i – 1, j) – d F(i – 1, j) – d F(i – 1, j) – d F(i, j – 1) – d F(i, j – 1) – d F(i, j – 1) – d F(i – 1, j – 1) + s(xi, yj) F(i – 1, j – 1) + s(xi, yj) F(i – 1, j – 1) + s(xi, yj) Bottom row Bottom right Anywhere or right column

Bottom row or right column

15

---

[← vs. Local alignment](12-vs-local-alignment.md) · [Up: contents](index.md) · [Sequence alignment with generalized gap penalties →](14-sequence-alignment-with-generalized-gap-penalties.md)
