---
title: 4 Complex Sinuoids and Orthogonality
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEight153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Complex Sinuoids and Orthogonality

**Source:** [`LectureEight153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEight153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Complex Sinusoids**

As we saw in the last lecture, sinusoids are linear combinations of cos(2 _πft_ ) and sin(2 _πft_ ). While doing algebra with sinusoids, it is very useful to represent them in terms of complex exponentials as:


In the last lecture, we saw that while dealing with sinusoids at integer valued time points _t_ , we can restrict the frequency _f_ to [0 _,_ 1 _/_ 2]. However, if we use the formulae above, note that we have to deal with _−f_ as well (because of the second term _e_<sup>_−_2</sup><sup>_πift_</sup> = _e_<sup>2</sup><sup>_πi_(</sup><sup>_−f_)</sup><sup>_t_</sup> ) and _−f_ lies between _−_ 1 _/_ 2 and 0. Thus when discussing sinusoids in terms of complex exponentials _e_<sup>2</sup><sup>_πift_</sup> _, t_ = 0 _,_ 1 _, . . . , n −_ 1, one takes _f ∈_ [ _−_ 0 _._ 5 _,_ 0 _._ 5) (note that _f_ = _−_ 0 _._ 5 leads to the same _e_<sup>2</sup><sup>_πift_</sup> as _f_ = 0 _._ 5 so we drop _f_ = 0 _._ 5 from consideration). For example, the function `np.fft.fftfreq(n)` gives all Fourier frequencies in [ _−_ 0 _._ 5 _,_ 0 _._ 5).

If one does not want to deal with negative frequencies, then we can use


because cos(2 _π_ (1 _− f_ ) _t_ ) = cos(2 _πt −_ 2 _πft_ ) = cos(2 _πft_ ) (note _t_ is an integer) and sin(2 _π_ (1 _− f_ ) _t_ ) = sin(2 _πt −_ 2 _πft_ ) = _−_ sin(2 _πft_ ).

Therefore, if we want to use complex exponentials _e_<sup>2</sup><sup>_πift_</sup> but we do not want to deal with negative frequencies, then we can restrict _f_ to [0 _,_ 1). From here on, whenever we consider the complex sinusoid _xt_ = _e_<sup>2</sup><sup>_πift_</sup> for _t_ = 0 _,_ 1 _, . . . , n −_ 1, we restrict _f ∈_ [0 _,_ 1).

### **4.2 Complex Sinusoidal Vectors**

For every 0 _≤ j ≤_ ( _n −_ 1), let us define the _n ×_ 1 vector


This vector can be interpreted as the complex sinusoid _e_<sup>2</sup><sup>_πift_</sup> with Fourier frequency _f_ = _j/n_ evaluated at the time points _t_ = 0 _,_ 1 _, . . . ,_ ( _n −_ 1). It is easy to see that

1. When _j_ = 0, we have _u_<sup>0</sup> = (1 _,_ 1 _, . . . ,_ 1).

> 2. When 1 _≤ j ≤ n −_ 1, we have _u_<sup>_j_</sup> = _u_<sup>_n−j_</sup> . Here _u_ ¯ denotes complex conjugate of _u_ (the complex conjugate _u_ ¯ of a vector _u_ is defined as the vector obtained by taking the complex conjugates of each entry of _u_ ).

4

The most important property of these complex valued vectors _u_<sup>0</sup> _, u_<sup>1</sup> _, . . . , u_<sup>_n−_1</sup> is **orthogonality** . Specifically, for 0 _≤ j̸_ = _k ≤ n −_ 1, we have


Recall that the inner product between two complex valued vectors _a_ = ( _a_ 1 _, . . . , an_ )<sup>_T_</sup> and _b_ = ( _b_ 1 _, . . . , bn_ )<sup>_T_</sup> is given by


Note specially the complex conjugate of _bj_ above.

Here is the proof of (6). Fix 0 _≤ j̸_ = _k ≤ n −_ 1 and write


This proves (6). It is also easy to see that (just take _j_ = _k_ in the above calculation and the answer can be found in the third line)


Therefore the _n_ complex-valued vectors _u_<sup>0</sup> _, u_<sup>1</sup> _, . . . , u_<sup>_n−_1</sup> are orthogonal and they all have the same squared length equal to _n_ . This immediately implies that they form a **basis** for the space C<sup>_n_</sup> consisting of all complex-valued vectors of length _n_ . In other words, every complex-valued vector of length _n_ can be written as a linear combination of _u_<sup>0</sup> _, u_<sup>1</sup> _, . . . , u_<sup>_n_</sup> .

### **4.3 The Inverse DFT formula**

The inverse DFT formula recovers the data _y_ 0 _, . . . , yn−_ 1 from their DFT _b_ 0 _, . . . , bn−_ 1. We derive this formula below.

The main observation is the following: Because _u_<sup>0</sup> _, . . . , u_<sup>_n−_1</sup> form a basis, we can write any _n ×_ 1 vector of complex entries:


5

as a linear combination of _u_<sup>0</sup> _, . . . , u_<sup>_n−_1</sup> . More specifically, we can write


Take the inner product of both sides of the above equation with _u_<sup>_j_</sup> for a fixed _j_ and use orthogonality so that � _u_<sup>_j_</sup> _.u_<sup>_k_�</sup> = 0 for _k̸_ = _j_ and the fact that � _u_<sup>_j_</sup> _, u_<sup>_j_�</sup> = _n_ to obtain


By the formula (4) for the DFT _bj_ , it is easy to see that _aj_ = _bj/n_ . As a consequence (7) becomes:


Writing the _t_ -th entry on both sides, we get


This is the inverse DFT formula. Note that the inverse DFT formula (9) as well as the DFT definition (4) look similar; the differences being in the sign of the exponent in the complex exponential and the presence of the factor 1 _/n_ in (9).

6

---

[← 3 Basic Properties of the DFT](03-3-basic-properties-of-the-dft.md) · [Up: contents](index.md)
