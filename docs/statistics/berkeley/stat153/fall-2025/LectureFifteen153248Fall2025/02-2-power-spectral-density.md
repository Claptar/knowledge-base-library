---
title: 2 Power Spectral Density
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Power Spectral Density

**Source:** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Since the mean of the _Exp_ (1) distribution equals 1, the mean of _I_ ( _j/n_ ) in the Spectrum Model (1) is given by _f_ ( _j/n_ ). This quantity is known as the **power** of frequency _j/n_ :

_f_ ( _j/n_ ) := power of frequency _j/n_ = mean of _I_ ( _j/n_ ) in model (1) _._

If we plot the points ( _j/n, f_ ( _j/n_ )) for _j_ = 1 _, . . . , m_ and join the neighboring points by lines, we get a continuous function plot. This function is known as the **power spectral density** and is defined on [0 _,_ 0 _._ 5].

This definition of the power spectral density is not rigorous. For a rigorous treatment, see any book on time series (e.g., Chapter 4 of Shumway and Stoffer; or the book “Spectral Analysis for Univariate Time Series” by Percival and Walden).

Note that the power spectral density is not a probability density function in the sense that it does not integrate to one.

2

---

[← 1 Smoothing the Periodogram](01-1-smoothing-the-periodogram.md) · [Up: contents](index.md) · [3 Spectrum Model from DFT →](03-3-spectrum-model-from-dft.md)
