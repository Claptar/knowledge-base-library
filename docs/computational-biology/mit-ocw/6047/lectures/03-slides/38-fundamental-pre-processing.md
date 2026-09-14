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

- Learning the redundancy structure of a string S

1 2 3 4 5 6 7 8 9 10 11 S = <mark>a a b c a a b x a a a</mark> Z = 0 **1** 0 0 **3 1** 0 0 **2 2** 1 Z-box = <mark>a a b c a a b x a a a</mark> r = <mark>a a b c a a b x a a a</mark> l = <mark>a a b c a a b x a a a</mark> Z1 Z2 Z3 … Zk-1 **Zk** <mark>a a b c a a b x a a a</mark> k left right

Can we compute Z, r, l in linear time O(|S|)?

43

---

[← Fundamental pre-processing](37-fundamental-pre-processing.md) · [Up: contents](index.md) · [Computing Zk given Z1 .. Zk-1 →](39-computing-zk-given-z1-zk-1.md)
