---
title: Running time of Z computation
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Running time of Z computation

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

###### **Case 1:  k is outside a Z-box:  explicitly compute Zk**


<!-- Start of picture text -->
l  r<br>Zk  Zk<br>S<br>k<br>Case 2a:  Inside Z-box and Zk’ < r-k: set Zk = Zk’<br>a  a<br>Zk Zk’  Zk<br>S<br>k’  l  r<br>k<br>Case 2b:  Inside Z-box and Zk’ >= r-k: explicitly compute starting at r+1<br>a  a<br>Zk  Zk’ Zk<br>? ? ?  ? ? ?<br>S<br>k’  l  k  r<br><!-- End of picture text -->

48

---

[← Correctness of Z computation](42-correctness-of-z-computation.md) · [Up: contents](index.md) · [What’s so fundamental about Z? →](44-what-s-so-fundamental-about-z.md)
