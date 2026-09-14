---
title: 3 Formula for RSS ( f ) when f is a Fourier Frequency
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSix153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Formula for RSS ( f ) when f is a Fourier Frequency

**Source:** [`LectureSix153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSix153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

When _f_ is a Fourier Frequency, one can write down a more explicit formula for _RSS_ ( _f_ ). For this, first note that for every _f_ ,


Plugging in _β_<sup>ˆ</sup> _f_ = ( _Xf_<sup>_TXf_)</sup><sup>_−_1</sup><sup>_X_</sup> _f_<sup>_Ty_above,weget</sup>


Now


2

Now suppose that _f ∈_ (0 _,_ 0 _._ 5) and suppose that _f_ is a Fourier frequency i.e., it is of the form _f_ = _j/n_ for some integer _j_ . Then it turns out that


As a result, for such _f_ ,


This gives


Therefore for Fourier frequencies in the range (0 _,_ 0 _._ 5), we get


or equivalently

When _f_ = 0 and _f_ = 1 _/_ 2, the above formula needs to be slightly modified. When _f_ = 0, the sinusoidal model (1) simply becomes:


There is only one effective parameter coefficient parameter ( _β_ 0 + _β_ 1) here which will be estimated by _y_ ¯ so that RSS becomes


3

When _f_ = 1 _/_ 2 and _n_ is even (when _n_ is odd, 1 _/_ 2 cannot be a Fourier frequency so it will not be considered), the model (1) becomes


For this model, it is easy to check that

so that


Let us not worry too much about the edge cases _f_ = 0 and _f_ = 1 _/_ 2, and focus on the formula (4). Note again that this formula holds whenever _f ∈_ (0 _,_ 0 _._ 5) and _f_ is a Fourier frequency (i.e., _nf_ is an integer).

---

[← 2 Fourier Frequencies and Computation of RSS ( f )](02-2-fourier-frequencies-and-computation-of-rss-f.md) · [Up: contents](index.md) · [4 Proof of the identities in (3) →](04-4-proof-of-the-identities-in-3.md)
