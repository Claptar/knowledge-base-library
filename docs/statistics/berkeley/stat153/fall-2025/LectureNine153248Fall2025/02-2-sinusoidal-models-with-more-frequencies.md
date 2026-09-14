---
title: 2 Sinusoidal Models with more frequencies
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNine153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Sinusoidal Models with more frequencies

**Source:** [`LectureNine153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNine153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Consider the model:

_yt_ = _β_ 0 + _β_ 1 cos(2 _πf_ 1 _t_ ) + _β_ 2 sin(2 _πf_ 1 _t_ ) + _β_ 3 cos(2 _πf_ 2 _t_ ) + _β_ 4 sin(2 _πf_ 2 _t_ ) + _ϵt._ (3) Formal inference for this model proceeds very similarly to inference for model (1). The main difference is that the definition of _RSS_ should now be changed to:

_RSS_ ( _f_ 1 _, f_ 2)


2

The analysis now proceeds as before with this modified definition of _RSS_ . The least squares estimates of _f_ 1 and _f_ 2 are obtained by minimizing _RSS_ ( _f_ 1 _, f_ 2) over _f_ 1 _, f_ 2, and the Bayesian posterior is given by


where _Xf_ 1 _,f_ 2 is now given by


Evaluation and minimization of _RSS_ ( _f_ 1 _, f_ 2) needs to be done on a joint grid for _f_ 1 and _f_ 2.

### **2.1 Restriction to Fourier Frequencies**

Suppose we restrict _f_ 1 and _f_ 2 to be distinct Fourier frequencies lying strictly between 0 and 0 _._ 5. Then it can be proved that


From the above, it is clear that _f_ 1 and _f_ 2 which minimize _RSS_ ( _f_ 1 _, f_ 2) equal the top two maximizers of the periodogram (remember that we are assuming _f_ 1 and _f_ 2 to be distinct).

The equality (4) is a consequence of the orthogonality of sinusoidal vectors corresponding to Fourier frequencies. It is proved below.

### **2.2 Orthogonality of Sinusoidal Vectors at Fourier Frequencies**

Orthogonality of Sinusoids at Fourier frequencies is best described through complex sinusoids.

For every 0 _≤ j ≤_ ( _n −_ 1), let us define the _n ×_ 1 vector


This vector can be interpreted as the complex sinusoid _e_<sup>2</sup><sup>_πift_</sup> with Fourier frequency _f_ = _j/n_ evaluated at the time points _t_ = 0 _,_ 1 _, . . . ,_ ( _n −_ 1). It is easy to see that

1. When _j_ = 0, we have _u_<sup>0</sup> = (1 _,_ 1 _, . . . ,_ 1).

2. When 1 _≤ j ≤ n −_ 1, we have _u_<sup>_j_</sup> = _u_<sup>_n−j_</sup> . Here _u_ ¯ denotes complex conjugate of _u_ (the complex conjugate _u_ ¯ of a vector _u_ is defined as the vector obtained by taking the complex conjugates of each entry of _u_ ).

The most important property of these complex valued vectors _u_<sup>0</sup> _, u_<sup>1</sup> _, . . . , u_<sup>_n−_1</sup> is **orthogonality** . Specifically, for 0 _≤ j̸_ = _k ≤ n −_ 1, we have


3

Recall that the inner product between two complex valued vectors _a_ = ( _a_ 1 _, . . . , an_ )<sup>_T_</sup> and _b_ = ( _b_ 1 _, . . . , bn_ )<sup>_T_</sup> is given by


Note specially the complex conjugate of _bj_ above.

Here is the proof of (5). Fix 0 _≤ j̸_ = _k ≤ n −_ 1 and write


This proves (5). It is also easy to see that (just take _j_ = _k_ in the above calculation and the answer can be found in the third line)


This orthogonality of complex sinusoids also extends to real sinusoids made of sines and cosines. For a Fourier frequency _j/n_ strictly lying between 0 and 1 (i.e., 0 _< j/n <_ 1 _/_ 2), define


and


These are the vectors obtained by evaulating cos(2 _πft_ ) and sin(2 _πft_ ) with Fourier Frequency _f_ = _j/n_ at time points _t_ = 0 _,_ 1 _, . . . ,_ ( _n −_ 1). So far we have assumed that 0 _< f_ = _j/n <_ 1 _/_ 2 i.e., 0 _< j < n/_ 2. The definition can be extended to the boundary points 0 and 1 _/_ 2 as well.

When _j_ = 0, the vector **c**<sup>0</sup> is the vector of all ones, while **s**<sup>0</sup> equals the zero vector. When _f_ = 1 _/_ 2 (this is only when _n_ is even other 1 _/_ 2 will not be a Fourier frequency) or _j_ = _n/_ 2, we have


Thus when _n_ is even, the non-zero vectors among these are:


4

When _n_ is odd, we are looking at


In either case, the total number of these vectors equals _n_ .

These vectors are orthogonal in R<sup>_n_</sup> . This can be proved as a consequence of the orthogonality of _u_<sup>0</sup> _, . . . , u_<sup>_n−_1</sup> , and the facts:


For example, fix two distinct Fourier frequencies _j/n_ and _k/n_ which are both strictly in (0 _,_ 1 _/_ 2). Then


Each inner product above equals zero because of orthogonality of _u_<sup>0</sup> _, . . . , u_<sup>_n−_1</sup> . Indeed, � _u_<sup>_j_</sup> _, u_<sup>_k_�</sup> and � _u_<sup>_n−j_</sup> _, u_<sup>_n−k_�</sup> are zero because _j̸_ = _k_ . Also we assumed that _j/n <_ 0 _._ 5 and _k/n <_ 0 _._ 5 so that _j_ + _k < n_ which means that _n − j̸_ = _k_ and also _n − k̸_ = _j_ . Thus � _u_<sup>_j_</sup> _, u_<sup>_n−k_�</sup> and � _u_<sup>_n−j_</sup> _, u_<sup>_k_�</sup> are also zero. Therefore: � **c**<sup>_j_</sup> _,_ **c**<sup>_k_�</sup> = 0 for _j̸_ = _k_ (it can be easily checked that this will be true even when _j/n_ or _k/n_ equal 0 or 1 _/_ 2).

One can similarly prove that other inner products (such as those between sines) also equal zero. As another example


where we used � _u_<sup>_j_</sup> _, u_<sup>_j_�</sup> = _n_ for every _j_ .

### **2.3 Proof of** (4)

Suppose _f_ 1 = _j/n_ and _f_ 2 = _k/n_ with _j̸_ = _k_ and both 0 _< j/n, k/n <_ 0 _._ 5. Then note that _Xf_ 1 _,f_ 2 is a _n ×_ 5 matrix with columns **c**<sup>0</sup> _,_ **c**<sup>_j_</sup> _,_ **s**<sup>_j_</sup> _,_ **c**<sup>_k_</sup> _,_ **s**<sup>_k_</sup> . As a result,


It is also easy to see that


5

We noted these in Lecture 7. They also follow from properties of the complex sinusoidal vectors _u_<sup>_j_</sup> . For example,

Thus


From here the proof proceeds in the same way as in the case of a single Fourier frequency in Lecture 7 to yield (4).

### **2.4 More than two Fourier frequencies**

When there are three or more Fourier frequencies, the formula (4) generalizes in the same way. For example, if _f_ 1 _, f_ 2 _, f_ 3 are all distinct Fourier frequencies strictly lying between 0 and 1 _/_ 2, then


So if we are trying to find the three best Fourier frequencies which best fit the data, we simply pick the top three maximizers of the periodogram. If we do not restrict to Fourier frequencies however, we have to do a harder (say grid based) minimization of _RSS_ ( _f_ 1 _, f_ 2 _, f_ 3). Depending on the application, there could be significant gains in RSS if we go beyond Fourier frequencies.

---

[← 1 Recap: previous two lectures](01-1-recap-previous-two-lectures.md) · [Up: contents](index.md) · [3 Other Nonlinear Models →](03-3-other-nonlinear-models.md)
