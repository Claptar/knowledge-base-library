---
title: 2 Orthogonality Properties of discretely-sampled Sinusoids at Fourier Frequencies
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSeven153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Orthogonality Properties of discretely-sampled Sinusoids at Fourier Frequencies

**Source:** [`LectureSeven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The key fact underlying the Discrete Fourier Transform (DFT) is orthogonality of (discretely sampled) sinusoids at Fourier frequencies. Last lecture, we proved the following formulae. If _f_ is a Fourier frequency with 0 _< f <_ 0 _._ 5, then


The sums above are over _t_ = 1 _, . . . , n_ . It should be clear that the same formulae are true if we sum over _t_ = 0 _,_ 1 _, . . . , n −_ 1 (because the value of cos(2 _πft_ ) and sin(2 _πft_ ) at _t_ = 0 and _t_ = _n_ coincide when _f_ is a Fourier frequency). When discussing the DFT, it is a standard convention to take _t_ = 0 _,_ 1 _, . . . , n −_ 1, and this is what we shall be doing in the this lecture. Rewriting the above formulae with _t_ = 0 _,_ 1 _, . . . , n −_ 1, we get


when _f ∈_ (0 _,_ 0 _._ 5) is a Fourier frequency. The conditions (3) say that discretely sampled sinusoids at Fourier frequencies _f ∈_ (0 _,_ 0 _._ 5) have mean zero. Conditions (4) say that they have energy equal to _n/_ 2. Condition (7) says that the discretely sampled cosine and sine are orthogonal, or equivalently, that their correlation is zero.

There is another very important property. If _f_ 1 and _f_ 2 are two distinct Fourier frequencies in (0 _,_ 0 _._ 5), then


This means that the sampled sinusoids at distinct Fourier frequencies are orthogonal (or equivalently uncorrelated).

These properties allow us to construct an orthogonal basis for R<sup>_n_</sup> consisting of sinusoids. Define


and


2

These are the vectors obtained by evaulating cos(2 _πft_ ) and sin(2 _πft_ ) with Fourier Frequency _f_ = _j/n_ at time points _t_ = 0 _,_ 1 _, . . . ,_ ( _n −_ 1). So far we have assumed that 0 _< f_ = _j/n <_ 1 _/_ 2 i.e., 0 _< j < n/_ 2. When _j_ = 0, the vector **c**<sup>0</sup> is the vector of all ones, while **s**<sup>0</sup> equals the zero vector. When _f_ = 1 _/_ 2 (this is only when _n_ is even other 1 _/_ 2 will not be a Fourier frequency) or _j_ = _n/_ 2, we have


Thus when _n_ is even, we are looking at the vectors:


When _n_ is odd, we are looking at


In either case, the total number of these vectors equals _n_ . By the properties stated above, these vectors are orthogonal, and hence form a basis for the _n_ -dimensional vector space of real-valued vectors R<sup>_n_</sup> . This means that every vector _y ∈_ R<sup>_n_</sup> can be written as a linear combination of these basis vectors. The coefficients in this linear combination are closely related to the DFT. This is the idea behind the DFT. For the formal definition, we use complex exponentials as opposed to sines and cosines.

---

[← 1 Recap from last lecture](01-1-recap-from-last-lecture.md) · [Up: contents](index.md) · [3 Complex Sinusoidal Vectors at Fourier Frequencies →](03-3-complex-sinusoidal-vectors-at-fourier-frequencies.md)
