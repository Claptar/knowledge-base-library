---
title: Fundamental pre-processing
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Fundamental pre-processing

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
• Learning the redundancy structure of a string S<br>1  2  3  4  5  6  7  8  9  10  11<br>S =  a a b c a a b x  a a a<br>Z =  0  1  0  0  3  1  0  0  2  2  1<br>a a<br>a a b  a a b<br>a  a<br>a a  a a<br>a a  a a<br><!-- End of picture text -->

- Zi = length of longest prefix in common for S[i..] and S (Length of the longest prefix of S[i..] that’s also a prefix of S)

42

---

[← Key insight: make bigger shifts!](36-key-insight-make-bigger-shifts.md) · [Up: contents](index.md) · [Fundamental pre-processing →](38-fundamental-pre-processing.md)
