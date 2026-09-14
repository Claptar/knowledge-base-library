---
title: Finding optimal path using only linear space
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Finding optimal path using only linear space

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### Incoming scores Outgoing scores

k<sup>*</sup>

###### Sum the two  best transition


<!-- Start of picture text -->
k *<br><!-- End of picture text -->

###### F(M/2, k)

F<sup>r</sup> (M/2, N-k)


<!-- Start of picture text -->
k *<br>M/2  M/2<br><!-- End of picture text -->


<!-- Start of picture text -->
N-k *<br><!-- End of picture text -->


<!-- Start of picture text -->
M/2<br><!-- End of picture text -->

Iterate procedure in corner quadrants

###### Max F(M/2, k) + F<sup>r</sup> (M/2, N-k)


<!-- Start of picture text -->
k *<br>N-k *<br>M/2  M/2<br><!-- End of picture text -->

Total cost MN(1+½+¼+⅛+…)≤2MN

8

---

[← Algorithmic variations (save time and/or space)](05-algorithmic-variations-save-time-and-or-space.md) · [Up: contents](index.md) · [Genome alignment in an excel spreadsheet →](07-genome-alignment-in-an-excel-spreadsheet.md)
