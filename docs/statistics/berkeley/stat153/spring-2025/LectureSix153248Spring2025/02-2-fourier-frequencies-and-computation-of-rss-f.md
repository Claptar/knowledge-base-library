---
title: 2 Fourier Frequencies and Computation of RSS ( f )
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSix153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Fourier Frequencies and Computation of RSS ( f )

**Source:** [`LectureSix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_RSS_ ( _f_ ) describes how well the sinusoid with frequency _f_ fits the observed data _y_ 1 _, . . . , yn_ . A plot of _RSS_ ( _f_ ) over different frequencies _f_ is frequently used as an exploratory data analysis tool for identifying “which periodicities are present in the data”. This tool is often used even when one is not interested in eventually fitting the simple model (1) to the observed data.

For computing _RSS_ ( _f_ ), as discussed in the previous lecture, we need a grid of values for _f_ . The most commonly used grid is given by:


where [ _n/_ 2] is the largest integer smaller than or equal to _n/_ 2.

A frequency of the form _j/n_ where _j ∈{_ 0 _,_ 1 _,_ 2 _, . . . , n −_ 1 _}_ and _n_ is the observed data size is called a **Fourier Frequency** . So the grid (2) consists of all Fourier frequencies that are in the range [0 _,_ 1 _/_ 2].

The main reason for taking the grid to consist of Fourier Frequencies is that _RSS_ ( _f_ ) _, f ∈F_ can be computed very efficiently (in time _O_ ( _n_ log _n_ )) using a classical algorithm known as the Fast Fourier Transform (FFT). We explain the high level details behind this fact today (without going into the workings of the FFT algorithm).

---

[← 1 Recap from last lecture](01-1-recap-from-last-lecture.md) · [Up: contents](index.md) · [3 Formula for RSS ( f ) when f is a Fourier Frequency →](03-3-formula-for-rss-f-when-f-is-a-fourier-frequency.md)
