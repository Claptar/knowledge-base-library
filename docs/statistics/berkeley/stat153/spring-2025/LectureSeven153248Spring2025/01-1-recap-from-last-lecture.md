---
title: 1 Recap from last lecture
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSeven153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Recap from last lecture

**Source:** [`LectureSeven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last couple of lectures, we considered fitting the sinusoidal model


to observed time series _y_ 1 _, . . . , yn_ . A key role for inferring the frequency parameter _f_ in this model is played by:


where


_RSS_ ( _f_ ) is simply the residual sum of squares in the linear regression model obtained by fixing the frequency parameter _f_ . It describes how well the sinusoid with frequency _f_ fits the observed data _y_ 1 _, . . . , yn_ .

In the last lecture, we derived the following alternative formula for _RSS_ ( _f_ ) that holds when _f ∈_ (0 _,_ 0 _._ 5) is a Fourier frequency i.e., _nf_ is an integer:


where _I_ ( _f_ ) is defined by


_I_ ( _f_ ) is known as the _Periodogram_ of the data _y_ 1 _, . . . , yn_ .

In this lecture, we study the Discrete Fourier Transform (DFT) of the observed time series data, and see how the DFT is related to the periodogram.

1

---

[Up: contents](index.md) · [2 Orthogonality Properties of discretely-sampled Sinusoids at Fourier Frequencies →](02-2-orthogonality-properties-of-discretely-sampled-sinusoids-a.md)
