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

_Input: 196,608 features_

- This localized network is pretty small, but still not very **expressive** (it only detects one “feature” at each location!)

- Stacking more “localized” or “fullyconnected” layers (or making them wider) could improve things, but at substantial cost


<!-- Start of picture text -->
…<br>4096<br>localized<br>units<br>1000 hidden<br>units<br>1000 output<br>units<br><!-- End of picture text -->

---

[← Image Classification](16-image-classification.md) · [Up: contents](index.md) · [Translation invariance →](18-translation-invariance.md)
