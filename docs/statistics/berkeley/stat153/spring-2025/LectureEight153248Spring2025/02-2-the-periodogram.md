---
title: 2 The Periodogram
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEight153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEight153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 The Periodogram

**Source:** [`LectureEight153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEight153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The Periodogram is a way of visualizing the DFT. The DFT consists of complex numbers so it is difficult to visualize it directly. The common visualization consists of looking at the squared absolute values of the DFT. More precisely, the periodogram is defined by


One visualizes the size of the DFT terms by plotting the periodogram. Note that _j_ = 0 is not plotted as _b_ 0 is simply the sum of the data values and does not provide any information on the sinusoidal components present in the data.

Because


we can write the periodogram as:

2

---

[← 1 DFT](01-1-dft.md) · [Up: contents](index.md) · [3 Utility of the Periodogram →](03-3-utility-of-the-periodogram.md)
