---
title: Kernels
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Kernels

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### So the key step is to take your input data and transform it into a kernel matrix


<!-- Start of picture text -->
F (xi) • i) • ) •  F (xj) = scalar!<br><!-- End of picture text -->


<!-- Start of picture text -->
F (xi) • i) • ) •  F<br>1  2  N<br>xi=(1,2) 1<br>2<br>2<br>N<br>1<br>K(Xi,Xj)<br><!-- End of picture text -->

- We have then done two very useful things: 1. Transformed X into a high (possibly infinite) dimensional space (where we hope are data are separable)

2. Taken dot products in this space to create scalars

71

---

[← Kernel Mapping](26-kernel-mapping.md) · [Up: contents](index.md) · [Example Kernels →](28-example-kernels.md)
