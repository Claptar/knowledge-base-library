---
title: 'Duality: seq. alignment  path through the matrix'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Duality: seq. alignment  path through the matrix

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
S1[1..i]  i  S1[i..n]<br>A  C  G  T  C  A  T  C  A<br>S2[1..j]  T  A  G  T  G  T  C  A<br>j  S  Alignments  Prefix alignmt<br> Paths  score   M[i,j]<br>S2[ j..m]<br>S1 A  C  G  T  C  A  T  C  A<br>S2 T<br>A  A<br>M[i,j] stores max score of prefix<br>G  G<br>alignment of S1[1..i] and S2[1..j]<br>T  T<br>G  C/G<br>Best alignment  Best path  T  T<br>C  C<br>through the matrix<br>A  A<br><!-- End of picture text -->

4

---

[← Remember Lecture 2](02-remember-lecture-2.md) · [Up: contents](index.md) · [Computing alignments recursively: M[i,j]=F(smaller) →](04-computing-alignments-recursively-m-i-j-f-smaller.md)
