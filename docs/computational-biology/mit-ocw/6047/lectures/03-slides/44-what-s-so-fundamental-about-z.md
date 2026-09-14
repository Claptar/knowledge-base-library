---
title: What’s so fundamental about Z?
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/lectures/03-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# What’s so fundamental about Z?

**Source:** `lectures/03-slides.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

#### • Learning the redundancy structure of a string S S = <mark>a a b c a a b x a a a</mark>

Z = 0 **1** 0 0 **3 1** 0 0 **2 2** 0

<mark>a a b a a b</mark>

- Z _i_ = fundamental property of internal redundancy structure

- Most pre-processings can be expressed in terms of Z

   - Length of the longest **prefix** starting/ending at position i

   - Length of the longest **suffix** starting/ending at position i

49

---

[← Running time of Z computation](43-running-time-of-z-computation.md) · [Up: contents](index.md) · [Back to string matching →](45-back-to-string-matching.md)
