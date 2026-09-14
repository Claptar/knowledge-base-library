---
title: Knuth-Morris-Pratt algorithm
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Knuth-Morris-Pratt algorithm

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

T=


<!-- Start of picture text -->
P=  a b c  f  a b c  d  e<br>a b c  f  a b c d e<br><!-- End of picture text -->

- Pre-processing:

– Spi(P) = length of longest proper suffix of P[1..i] that matches a prefix of P


<!-- Start of picture text -->
P=  a b c  f  a b c  d  e<br>a b c  a b c<br><!-- End of picture text -->

- No other than the right-hand-side of the Z-boxes

51

---

[← Back to string matching](45-back-to-string-matching.md) · [Up: contents](index.md) · [Knuth-Morris-Pratt running time →](47-knuth-morris-pratt-running-time.md)
