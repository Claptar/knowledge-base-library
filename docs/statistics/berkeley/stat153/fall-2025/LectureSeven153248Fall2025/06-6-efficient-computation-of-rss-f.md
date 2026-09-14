---
title: 6 Efficient Computation of RSS ( f )
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeven153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Efficient Computation of RSS ( f )

**Source:** [`LectureSeven153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeven153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_RSS_ ( _f_ ) describes how well the sinusoid with frequency _f_ fits the observed data _y_ 1 _, . . . , yn_ . It is crucial to estimation of _f_ in the model (1), and also for calculating the Bayesian posterior (4).

A plot of _RSS_ ( _f_ ) over different frequencies _f_ is also commonly used as an exploratory data analysis tool for identifying “which periodicities are present in the data”. This tool is often used even when one is not interested in eventually fitting the simple model (1) to the observed data.

For computing _RSS_ ( _f_ ), as discussed in the previous lecture, we need a grid of values for _f_ . The most commonly used grid is given by:


where [ _n/_ 2] is the largest integer smaller than or equal to _n/_ 2.

A frequency of the form _j/n_ where _j ∈{_ 0 _,_ 1 _,_ 2 _, . . . , n −_ 1 _}_ and _n_ is the observed data size is called a **Fourier Frequency** . So the grid (5) consists of all Fourier frequencies that are in the range [0 _,_ 1 _/_ 2].

The main reason for taking the grid to consist of Fourier Frequencies is that _RSS_ ( _f_ ) _, f ∈F_ can be computed very efficiently (in time _O_ ( _n_ log _n_ )) using a classical algorithm known as the Fast Fourier Transform (FFT). We explain the high level details behind this fact today (without going into the workings of the FFT algorithm).

### **6.1 Formula for** _RSS_ ( _f_ ) **when** _f_ **is a Fourier Frequency**

When _f_ is a Fourier Frequency, one can write down a more explicit formula for _RSS_ ( _f_ ). For this, first note that for every _f_ :


Thus


Plugging in _β_<sup>ˆ</sup> _f_ = ( _Xf_<sup>_TXf_)</sup><sup>_−_1</sup><sup>_X_</sup> _f_<sup>_Ty_above,weget</sup>


Now


4

Now suppose that _f ∈_ (0 _,_ 0 _._ 5) and suppose that _f_ is a Fourier frequency i.e., it is of the form _f_ = _j/n_ for some integer _j_ . Then it turns out that


As a result, for such _f_ ,


This gives


Therefore for Fourier frequencies in the range (0 _,_ 0 _._ 5), we get


or equivalently

When _f_ = 0 and _f_ = 1 _/_ 2, the above formula needs to be slightly modified. When _f_ = 0, the sinusoidal model (1) simply becomes:


There is only one effective parameter coefficient parameter ( _β_ 0 + _β_ 1) here which will be estimated by _y_ ¯ so that RSS becomes


5

When _f_ = 1 _/_ 2 and _n_ is even (when _n_ is odd, 1 _/_ 2 cannot be a Fourier frequency so it will not be considered), the model (1) becomes


For this model, it is easy to check that

so that


Let us not worry too much about the edge cases _f_ = 0 and _f_ = 1 _/_ 2, and focus on the formula (7). Note again that this formula holds whenever _f ∈_ (0 _,_ 0 _._ 5) and _f_ is a Fourier frequency (i.e., _nf_ is an integer).

### **6.2 Proof of the identities in** (6)

Note that 0 _< f <_ 1 _/_ 2 and that _nf_ is an integer.


because cos(2 _πnf_ ) = cos(2 _π_ (integer)) = 1 and sin(2 _πnf_ ) = sin(2 _π_ (integer)) = 0.

Similarly


Next note

6

and


The quantity<sup>�</sup> _t_<sup>cos(4</sup><sup>_πft_)whichappearsinboththeabovetermsturnsouttobezero</sup> because


because cos(4 _πnf_ ) = cos(4 _π_ (integer)) = 1 and sin(4 _πnf_ ) = sin(4 _π_ (integer)) = 0.

Finally


The intermediate calculations above include the terms _e_<sup>2</sup><sup>_πif_</sup> _−_ 1 and _e_<sup>4</sup><sup>_πif_</sup> _−_ 1 in the denominators. We need to make sure that these terms are not zero (otherwise the above proofs would not be valid).


which cannot be zero because cos(2 _πf_ ) _<_ 1 for _f ∈_ (0 _,_ 0 _._ 5), and


which also cannot be zero because cos(4 _πf_ ) _<_ 1 for _f ∈_ (0 _,_ 0 _._ 5).

### **6.3 The Periodogram**

Given a time series dataset _y_ 1 _, . . . , yn_ , its periodogram is the function _I_ ( _f_ ) _,_ 0 _< f <_ 1 _/_ 2, defined as follows:


7

From the formula (7), we have


The periodogram _I_ ( _f_ ) can be written in the following alternative way:


where _| · |_ denotes complex modulus. As we shall discuss in detail next lecture,


(when _f_ is a Fourier frequency) is closely related to the Discrete Fourier Transform (DFT) of _y_ 1 _, . . . , yn_ . The DFT can be efficiently computed using the Fast Fourier Transform (FFT) algorithm. This gives a way of computing _I_ ( _f_ ) and _RSS_ ( _f_ ) at Fourier frequencies efficiently.

8

---

[← 5 Bayesian Posterior](05-5-bayesian-posterior.md) · [Up: contents](index.md)
