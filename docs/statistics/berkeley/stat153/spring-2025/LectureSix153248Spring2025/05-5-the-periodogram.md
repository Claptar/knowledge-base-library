---
title: 5 The Periodogram
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSix153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 The Periodogram

**Source:** [`LectureSix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Given a time series dataset _y_ 1 _, . . . , yn_ , its periodogram is the function _I_ ( _f_ ) _,_ 0 _< f <_ 1 _/_ 2, defined as follows:


5

From the formula (4), we have


The periodogram _I_ ( _f_ ) can be written in the following alternative way:


where _| · |_ denotes complex modulus. As we shall discuss in detail next lecture,


(when _f_ is a Fourier frequency) is closely related to the Discrete Fourier Transform (DFT) of _y_ 1 _, . . . , yn_ . The DFT can be efficiently computed using the Fast Fourier Transform (FFT) algorithm. This gives a way of computing _I_ ( _f_ ) and _RSS_ ( _f_ ) at Fourier frequencies efficiently.

6

---

[← 4 Proof of the identities in (3)](04-4-proof-of-the-identities-in-3.md) · [Up: contents](index.md)
