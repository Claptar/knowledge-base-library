---
title: Image Classification
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/24_CNNs_Part2.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Image Classification

**Source:** [`public/lectures/24_CNNs_Part2.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- So: instead of having the entire image feed into each hidden unit, have each unit only look at **a small portion** of the image, e.g. 11x11 pixels (363 weights)

   - We can call this the **receptive field** for the unit

- Let’s offset each 11x11 unit by 4 pixels, giving 4096 “localized” units

_Receptive field_ for another unit

---

[← Image Classification](13-image-classification.md) · [Up: contents](index.md) · [Image Classification →](15-image-classification.md)
