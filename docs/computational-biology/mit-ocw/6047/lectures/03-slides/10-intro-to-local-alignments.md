---
title: Intro to Local Alignments
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Intro to Local Alignments

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Statement of the problem

   - A _local alignment_ of strings _s_ and _t_ is an alignment of a substring of _s_


_s_

with a substring of _t_

- Why local alignments?

   - Small domains of a gene may be only conserved portions

   - Looking for a small gene in a large chromosome (search)

   - Large segments often undergo rearrangements

```
AGTGCCCTGGAACCCTGACGGTGGGTCACAAAACTTCTGGA
```


<!-- Start of picture text -->
A  B  C  D<br>AGTGCCCTGGAACCCTGACGGTGGGTCACAAAACTTCTGGA<br>B<br>D<br>A<br>C<br>AGTGACCTGGGAAGACCCTGACCCTGGGTCACAAAACTC<br><!-- End of picture text -->

A B C D B D A C

Global alignment

Local alignment

13

---

[← Today’s Goal: Diving deeper into alignments](09-today-s-goal-diving-deeper-into-alignments.md) · [Up: contents](index.md) · [Global Alignment →](11-global-alignment.md)
