---
title: SVM Formulation
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# SVM Formulation

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We define a vector **w** normal to the separating line **w** Assume all data satisfy the following: **x**  **w**  b  **i** 1  for yi =+1 **x**  **w**  b  b **i** 1  for yi =-1 **xi•w** yi  **xi**  **w**  b   1

**Labels Y=+1 Y=-1**

**_We want to find the separator with the largest margin_**

64

<u>An Optimization Problem</u> **~~Only need dot~~ product of input For full derivation, see Burges (1998) data!**

1 Minimize LD   _i_   _i j yi y j_ **xi**  **x j** 2 _i i_ , _j_  subject to  _i yi_ 0  and  _j_  0 _i_ **Solving for**  _i_  _yi_  **xi**  **w**  _b_   1   0 **w**   _i yi_ **xi** _i_

Quadratic Programming

Only some i are non-zero

**x** i with ai >0 are the _support vectors_ **_w_** is _determined by these data points!_

65

---

[← Classifying A New Protein](21-classifying-a-new-protein.md) · [Up: contents](index.md) · [Using an SVM →](23-using-an-svm.md)
