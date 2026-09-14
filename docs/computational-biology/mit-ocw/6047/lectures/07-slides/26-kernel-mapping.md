---
title: Kernel Mapping
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Kernel Mapping

**Source:** `lectures/07-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Want a **mapping** from input space, R<sup>d</sup> , to other euclidean space, H

From previous slide, SVMs _only depend_ on **dot product**

F(x): R<sup>d</sup> -> H

**becomes Xi • Xj** F( **Xi) •** F **(Xj)**

Here is trick: if we have a kernel function such that

**K(Xi,Xj) =** F( **Xi) •** F **(Xj)**

**We can just use K and never know** F **(x) explicitly!**

F **(X) is high dimensional K is a scalar**

70

---

[← Kernel Mapping](25-kernel-mapping.md) · [Up: contents](index.md) · [Kernels →](27-kernels.md)
