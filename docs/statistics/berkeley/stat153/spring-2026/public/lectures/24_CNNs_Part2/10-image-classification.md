---
title: Image classification
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/24_CNNs_Part2.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Image classification

**Source:** [`public/lectures/24_CNNs_Part2.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/24_CNNs_Part2.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Formalization of the image classification problem:

   - **Input** : an image (256 x 256 RGB pixels = 196,608 features)

   - **Target** : a 1-hot vector (e.g. [0, 1, 0, 0, 0, …, 0]) indicating the “class” or “label” of the image


[1,0,…,0]

---

[← Pooling layer](09-pooling-layer.md) · [Up: contents](index.md) · [Image classification →](11-image-classification.md)
