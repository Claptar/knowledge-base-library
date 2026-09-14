---
title: 'Step 3: Trace back pointers to construct alignment'
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/02-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Step 3: Trace back pointers to construct alignment

**Source:** `lectures/02-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
-  A G T<br>Initialization:<br>-  0  -2  -4  -6<br>• Top left: 0<br>1<br>-1  -1<br>Update Rule:<br>A -2  1  -1  -3  M( i , j )=max{<br>1<br>-1  -1  • M( i -1 ,    j  ) - 2  gap<br>• M(   i   ,  j -1) - 2  gap<br>A -4  -1  0  -2<br>1  • M( i -1 ,  j -1) -1<br>mismatch<br>-1<br>-1<br>• M( i -1 ,  j -1)+1<br>match<br>G }<br>-6  -3  0  -1<br>-1  -1  Termination:<br>-1<br>• Bottom right<br>C  -8  -5  -2  -1<br>Path segments that lead to locally optimal choices<br>41<br>Path segments that lead to the globally optimal solution<br><!-- End of picture text -->

---

[← Dynamic Programming for sequence alignment](34-dynamic-programming-for-sequence-alignment.md) · [Up: contents](index.md) · [Genome alignment in an excel spreadsheet →](36-genome-alignment-in-an-excel-spreadsheet.md)
