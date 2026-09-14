---
title: 3 Complex Sinusoidal Vectors at Fourier Frequencies
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSeven153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Complex Sinusoidal Vectors at Fourier Frequencies

**Source:** [`LectureSeven153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeven153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1** _f ∈_ [0 _,_ 1) **as opposed to** _f ∈_ [0 _,_ 0 _._ 5]

cos(2 _πft_ ) and sin(2 _πft_ ) can be represented in terms of complex exponentials as


Note here that we have to deal with _−f_ as well (because of the second term _e_<sup>_−_2</sup><sup>_πift_</sup> = _e_<sup>2</sup><sup>_πi_(</sup><sup>_−f_)</sup><sup>_t_</sup> ) and _−f_ lies between _−_ 1 _/_ 2 and 0. Thus when discussing sinusoids in terms of complex exponentials _e_<sup>2</sup><sup>_πift_</sup> _, t_ = 0 _,_ 1 _, . . . , n −_ 1, we take _f ∈_ ( _−_ 0 _._ 5 _,_ 0 _._ 5] (note that _f_ = _−_ 0 _._ 5 leads to the same _e_<sup>2</sup><sup>_πift_</sup> as _f_ = 0 _._ 5 so we drop _f_ = _−_ 0 _._ 5 from consideration). If one does not want to deal with negative frequencies, then we can use

_e_<sup>_−_2</sup><sup>_πift_</sup> = cos(2 _πft_ ) _− i_ sin(2 _πft_ ) = cos(2 _π_ (1 _− f_ ) _t_ ) + _i_ sin(2 _π_ (1 _− f_ ) _t_ ) = _e_<sup>2</sup><sup>_πi_(1</sup><sup>_−f_)</sup><sup>_t_</sup>

because cos(2 _π_ (1 _− f_ ) _t_ ) = cos(2 _πt −_ 2 _πft_ ) = cos(2 _πft_ ) (note _t_ is an integer) and sin(2 _π_ (1 _− f_ ) _t_ ) = sin(2 _πt −_ 2 _πft_ ) = _−_ sin(2 _πft_ ).

Therefore, if we want to use complex exponentials _e_<sup>2</sup><sup>_πift_</sup> but we do not want to deal with negative frequencies, then we can restrict _f_ to [0 _,_ 1). From here on, whenever we consider the complex sinusoid _xt_ = _e_<sup>2</sup><sup>_πift_</sup> for _t_ = 0 _,_ 1 _, . . . , n −_ 1, we restrict _f ∈_ [0 _,_ 1).

### **3.2 Complex Sinusoids**

For every 0 _≤ j ≤_ ( _n −_ 1), let us define the _n ×_ 1 vector


This vector can be interpreted as the complex sinusoid _e_<sup>2</sup><sup>_πift_</sup> with Fourier frequency _f_ = _j/n_ evaluated at the time points _t_ = 0 _,_ 1 _, . . . ,_ ( _n −_ 1). It is easy to see that

3

1. When _j_ = 0, we have _u_<sup>0</sup> = (1 _,_ 1 _, . . . ,_ 1).

2. When 1 _≤ j ≤ n −_ 1, we have _u_<sup>_j_</sup> = _u_<sup>_n−j_</sup> . Here _u_ ¯ denotes complex conjugate of _u_ (the complex conjugate _u_ ¯ of a vector _u_ is defined as the vector obtained by taking the complex conjugates of each entry of _u_ ).

The most important property of these complex valued vectors _u_<sup>0</sup> _, u_<sup>1</sup> _, . . . , u_<sup>_n−_1</sup> is **orthogonality** . Specifically, for 0 _≤ j̸_ = _k ≤ n −_ 1, we have


Recall that the inner product between two complex valued vectors _a_ = ( _a_ 1 _, . . . , an_ )<sup>_T_</sup> and _b_ = ( _b_ 1 _, . . . , bn_ )<sup>_T_</sup> is given by


Note specially the complex conjugate of _bj_ above.

Here is the proof of (7). Fix 0 _≤ j̸_ = _k ≤ n −_ 1 and write


This proves (7). It is also easy to see that (just take _j_ = _k_ in the above calculation and the answer can be found in the third line)


Therefore the _n_ complex-valued vectors _u_<sup>0</sup> _, u_<sup>1</sup> _, . . . , u_<sup>_n−_1</sup> are orthogonal and they all have the same squared length equal to _n_ . This immediately implies that they form a **basis** for the space C<sup>_n_</sup> consisting of all complex-valued vectors of length _n_ . In other words, every complex-valued vector of length _n_ can be written as a linear combination of _u_<sup>0</sup> _, u_<sup>1</sup> _, . . . , u_<sup>_n_</sup> . This observation is the foundation for the definition of the Discrete Fourier Transform.

4

### **3.3 The Discrete Fourier Transform (DFT)**

Because _u_<sup>0</sup> _, . . . , u_<sup>_n−_1</sup> form a basis, we can write any _n ×_ 1 vector of complex entries:


as a linear combination of _u_<sup>0</sup> _, . . . , u_<sup>_n−_1</sup> . More specifically, we can write


Take the inner product of both sides of the above equation with _u_<sup>_j_</sup> for a fixed _j_ and use orthogonality so that � _u_<sup>_j_</sup> _.u_<sup>_k_�</sup> = 0 for _k̸_ = _j_ and the fact that � _u_<sup>_j_</sup> _, u_<sup>_j_�</sup> = _n_ to obtain


We are now ready to define the Discrete Fourier Transform (DFT). The DFT of _y_ 0 _, y_ 1 _, . . . , yn−_ 1 is defined by


More specifically, the _n_ (possibly) complex numbers _b_ 0 _, b_ 1 _, . . . , bn−_ 1 are collectively called the DFT of _y_ 0 _, . . . , yn−_ 1. Typically, _y_ 0 _, . . . , yn−_ 1 will represent observed time series data. It is important to note that even though _y_ 0 _, . . . , yn−_ 1 are real-valued, their DFT _b_ 0 _, . . . , bn−_ 1 can be complex-valued.

Here are some basic things to note about the DFT:

1. _b_ 0 is always equal to _y_ 0 + _· · ·_ + _yn−_ 1. To see this, just plug in _j_ = 0 in (10).

2. In general _bj_ is a complex number with real and imaginary parts given by:


3. The DFT of _y_ = ( _y_ 0 _, . . . , yn−_ 1)<sup>_T_</sup> can be obtained in `numpy` using the command `np.fft.fft(x)` . Here `fft` stands for Fast Fourier Transform which is a special efficient algorithm for computing the DFT (we will not be going over the details of the FFT algorithm).

### **3.4 The Periodogram**

The Periodogram is a way of visualizing the DFT. The DFT consists of complex numbers so it is difficult to visualize it directly. The common visualization consists of looking at the squared absolute values of the DFT. More precisely, the periodogram is defined by


One visualizes the size of the DFT terms by plotting the periodogram. Note that _j_ = 0 is not plotted as _b_ 0 is simply the sum of the data values and does not provide any information on the sinusoidal components present in the data.

5

Because


we can write the periodogram as:


6

---

[← 2 Orthogonality Properties of discretely-sampled Sinusoids at Fourier Frequencies](02-2-orthogonality-properties-of-discretely-sampled-sinusoids-a.md) · [Up: contents](index.md)
