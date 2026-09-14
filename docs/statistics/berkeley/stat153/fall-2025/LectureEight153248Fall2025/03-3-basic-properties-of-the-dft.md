---
title: 3 Basic Properties of the DFT
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Basic Properties of the DFT

**Source:** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here are some basic things to note about the DFT (defined in (4)).

1. _b_ 0 is always equal to _y_ 0 + _· · ·_ + _yn−_ 1. To see this, just plug in _j_ = 0 in (4).

2. In general _bj_ is a complex number with real and imaginary parts given by:


Sometimes the imaginary part will be zero (for example, when _n_ is even and _j_ = _n/_ 2) but, in general, _bj_ will be complex-valued.

3. For each _j_ = 1 _, . . . , n −_ 1, the DFT term _bn−j_ equals the complex conjugate of _bj_ :


The reason for the above is


where, in the above, we used that exp( _−_ 2 _πit_ ) = 1 (because _t_ is an integer) and that 2 _πijt −_<sup>2</sup><sup>_πijt_</sup> exp _n_ is the complex conjugate of exp _n_ . Note that, for the above argu� � � � ment, it is crucial that _y_ 0 _, . . . , yn−_ 1 are real. If some of _y_ 0 _, . . . , yn−_ 1 are complex, the relation (5) is no longer true.

Because of (5), the DFT terms for later indices _j_ can be determined as complex conjugates for the DFT terms for earlier indices. For example, when _n_ = 11, the DFT can be written as:


and, for _n_ = 12, it is


Note that when _n_ = 12, the term _b_ 6 is necessarily real because _b_ 6 =<sup>¯</sup> _b_ 6.

Thus when _n_ = 11, the data consists of 11 real numbers while the DFT consists of one real number ( _b_ 0) and 5 complex numbers. On the other hand, when _n_ = 12, the data consists

3

of 12 real numbers while the DFT consists of two real numbers ( _b_ 0 and _b_ 6) and 5 complex numbers.

It turns out that the data _y_ 0 _, y_ 1 _, . . . , yn−_ 1 can be recovered from the DFT _b_ 0 _, . . . , bn−_ 1 using a simple formula (this formula is sometimes known as the inverse DFT formula). Before seeing this, it is necessary to understand orthogonality properties of complex sinusoids with Fourier frequencies.

---

[← 2 Discrete Fourier Transform (DFT) and Periodogram](02-2-discrete-fourier-transform-dft-and-periodogram.md) · [Up: contents](index.md) · [4 Complex Sinuoids and Orthogonality →](04-4-complex-sinuoids-and-orthogonality.md)
