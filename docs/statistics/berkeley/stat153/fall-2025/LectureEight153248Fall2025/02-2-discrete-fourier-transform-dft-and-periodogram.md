---
title: 2 Discrete Fourier Transform (DFT) and Periodogram
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Discrete Fourier Transform (DFT) and Periodogram

**Source:** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The periodogram _I_ ( _f_ ) clearly can be rewritten as:


The term inside the modulus sign above is almost the same as the Discrete Fourier Transform (DFT) of the data. There is only one difference which comes from changing the data indexing slightly. While discussing the DFT, it is a standard convention to write the data as _y_ 0 _, y_ 1 _, . . . , yn−_ 1 (instead of _y_ 1 _, . . . , yn_ ). In other words, we start the indexing with 0 (as in Python) as opposed to 1. With this indexing, the DFT is defined as follows.

The DFT of data _y_ 0 _, . . . , yn−_ 1 is defined by:


In words, _bj_ is the dot product between the data and the complex sinusoid with frequency _f_ = _j/n_ . Note that the complex sinusoid with frequency _f_ is given by:


The _n_ (possibly) complex numbers _b_ 0 _, b_ 1 _, . . . , bn−_ 1 are collectively called the DFT of _y_ 0 _, . . . , yn−_ 1. Typically, _y_ 0 _, . . . , yn−_ 1 will represent observed time series data. It is important to note that even though _y_ 0 _, . . . , yn−_ 1 are real-valued, their DFT _b_ 0 _, . . . , bn−_ 1 can be complex-valued.

**More on indexing** : As mentioned previously, while defining the DFT, we index the data starting from zero. In the definition (4), the first data point (which is _y_ 0) is being multiplied by exp( _−_ 2 _πij_ (0) _/n_ ) = 1, the second data point is being multiplied by exp( _−_ 2 _iπj/n_ ) and, in general, the _t_ -th data point is being multiplied by exp( _−_ 2 _iπj_ ( _t −_ 1) _/n_ ). If we instead define the DFT by:


then the _t_ -th data point will be multiplied by exp( _−_ 2 _iπjt/n_ ). _bj_ and<sup>˜</sup> _bj_ will be different and they will be related by:


The multiplier exp(2 _πij/n_ ) above has modulus one which means that


So if we are only looking at the moduli of the DFT terms (note the periodogram only involves the moduli of DFT), then it does not matter whether we index data starting with 0 or 1. The standard convention while studying the DFT is to index starting from 0.

The connection between the periodogram and the DFT is given by:


2

and the connection between _RSS_ ( _j/n_ ) and DFT is given by:


It is important to note that the DFT can be calculated very efficiently. The DFT of _y_ = ( _y_ 0 _, . . . , yn−_ 1)<sup>_T_</sup> can be obtained in `numpy` using the command `np.fft.fft(y)` . Here `fft` stands for Fast Fourier Transform which is a special efficient algorithm for computing the DFT. Naively, it would seem that to compute the DFT would need _O_ ( _n_<sup>2</sup> ) computation (for each of _n_ values of _j_ , we have to compute _bj_ which requires a sum over the dataset of size _n_ ), but the FFT algorithm exploits symmetry and redundancy in the complex exponentials to compute the DFT in only _O_ ( _n_ log _n_ ) time. We will not be going over the details of the FFT algorithm in class.

---

[← 1 Recap from last lecture](01-1-recap-from-last-lecture.md) · [Up: contents](index.md) · [3 Basic Properties of the DFT →](03-3-basic-properties-of-the-dft.md)
