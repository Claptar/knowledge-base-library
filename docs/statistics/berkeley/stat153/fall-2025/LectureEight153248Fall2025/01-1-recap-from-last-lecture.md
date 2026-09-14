---
title: 1 Recap from last lecture
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Recap from last lecture

**Source:** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we considered fitting the sinusoidal model


to observed time series _y_ 1 _, . . . , yn_ . A key role for inferring the frequency parameter _f_ in this model is played by:


where


_RSS_ ( _f_ ) is simply the residual sum of squares in the linear regression model obtained by fixing the frequency parameter _f_ . It describes how well the sinusoid with frequency _f_ fits the observed data _y_ 1 _, . . . , yn_ .

Calculating _RSS_ ( _f_ ) separately for each value of _f_ in a grid of values of _f_ can be computationally quite inefficient (particularly when _n_ is large). We have started discussing efficient computation of _RSS_ ( _f_ ) in the last lecture. The key here is to recognize the following alternative formula for _RSS_ ( _f_ ) (proved in last lecture) that holds when _f ∈_ (0 _,_ 0 _._ 5) is a Fourier frequency i.e., _nf_ is an integer:


where _I_ ( _f_ ) is defined by


_I_ ( _f_ ) is known as the _Periodogram_ of the data _y_ 1 _, . . . , yn_ .

In this lecture, we study the Discrete Fourier Transform (DFT) of the observed time series data, and see how the DFT is related to the periodogram.

1

---

[Up: contents](index.md) · [2 Discrete Fourier Transform (DFT) and Periodogram →](02-2-discrete-fourier-transform-dft-and-periodogram.md)
