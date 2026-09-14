---
title: DNA Sequence Alignment IV
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DNA Sequence Alignment IV

**Source:** `lectures/02-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

What scoring matrix to use for DNA? Usually use simple match-mismatch matrices:


<!-- Start of picture text -->
i        j:     A  C  G  T<br>A  1   m   m   m<br>s<br>i,j  :<br>C   m    1   m   m<br>G   m   m    1   m<br>T   m   m   m    1<br><!-- End of picture text -->

m = “mismatch penalty” (must be negative)

When would you use a mismatch penalty of:    -1    -3   -5  ?

23

---

[← DNA Sequence Alignment III](12-dna-sequence-alignment-iii.md) · [Up: contents](index.md) · [DNA Sequence Alignment V →](14-dna-sequence-alignment-v.md)
