---
title: '1 Recap: previous two lectures'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Recap: previous two lectures

**Source:** [`LectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We observe time series data _y_ 0 _, . . . , yn−_ 1 (note we are now using Python indexing starting from 0). We want to fit the sinusoidal model:


The main parameter is the frequency _f_ (which we restrict to the interval [0 _,_ 0 _._ 5]). The other parameters ( _β_ 0 _, β_ 1 _, β_ 2 _, σ_ ) are nuisance parameters.

The key role in the inference of _f_ is played by the RSS:


where


_RSS_ ( _f_ ) is simply the residual sum of squares in the linear regression model obtained by fixing the frequency parameter _f_ . It describes how well the sinusoid with frequency _f_ fits the observed data _{yt}_ .

To estimate _f_ , we minimize _RSS_ ( _f_ ). For uncertainty quantification for _f_ , we can use the posterior formula:


For both these tasks (minimization of _RSS_ ( _f_ ) and calculation of the posterior of _f_ ), we need to discretize and restrict _f_ to a finite set of values in the range (0 _,_ 1 _/_ 2). Here there are two options:

1. Take a dense grid of values in (0 _,_ 1 _/_ 2)

1

2. Work with the Fourier frequencies _j/n_ which are in the range (0 _,_ 1 _/_ 2).

The advantage of taking the second option (Fourier Frequencies) is that it admits very fast computation of _RSS_ ( _f_ ) via the following:

1. Calculate the DFT of the data:


This can be done via a very fast algorithm called the FFT (in python, use `np.fft.fft()` ).

2. Calculate the periodogram:


3. Use the formula:


This formula was proved in Lecture 7. The key observation is that when _f_ is a Fourier frequency lying in (0 _,_ 0 _._ 5), we have


4. Minimize _RSS_ ( _j/n_ ) over _j_ to obtain _f_<sup>ˆ</sup> .

5. Calculate the posterior of _f_ via:


Note that we did not write the _|Xf_<sup>_TXf|−_1</sup><sup>_/_2term above.This is because, when</sup><sup>_f_is a Fourier</sup> frequency in (0 _,_ 0 _._ 5), we have (2) so that _|Xf_<sup>_TXf|_=</sup><sup>_n_3</sup><sup>_/_8whichdoesnotdependon</sup><sup>_f_(so</sup> _|Xf_<sup>_TXf|−_1</sup><sup>_/_2canbeabsorbedintheconstantofproportionality).</sup>

It is important to note that restriction to Fourier frequencies is only done for computational reasons. There are no other advantages to doing this, and, in fact, there could be significant loss of information in doing so. This can be easily seen in real datasets such as the sunspots dataset.

---

[Up: contents](index.md) · [2 Sinusoidal Models with more frequencies →](02-2-sinusoidal-models-with-more-frequencies.md)
