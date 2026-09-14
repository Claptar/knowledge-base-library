---
title: DNA Sequence Alignment III
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DNA Sequence Alignment III

**Source:** `lectures/02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

How is λ related to the score matrix?

λ is the unique positive solution to the equation*:

= 1 pre<sup>λsij</sup> i j<sup>∑</sup> i,j

pi = freq. of nt i in query, rj = freq. of nt j in subject sij = score for aligning an i,j pair

What kind of an equation is this? What would happen to λ if we doubled all the scores? What does this tell us about the nature of λ?

(transcendental) (reduced by half) (scaling factor)

*Karlin & Altschul, 1990

22

---

[← DNA Sequence Alignment II](11-dna-sequence-alignment-ii.md) · [Up: contents](index.md) · [DNA Sequence Alignment IV →](13-dna-sequence-alignment-iv.md)
