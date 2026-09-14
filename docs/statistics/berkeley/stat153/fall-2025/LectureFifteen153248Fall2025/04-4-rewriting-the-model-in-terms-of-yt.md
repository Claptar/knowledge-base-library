---
title: 4 Rewriting the Model in terms of yt
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFifteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Rewriting the Model in terms of yt

**Source:** [`LectureFifteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFifteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The model (3) is written in terms of the DFT _bj_ . Because the original data can be written in terms of the DFT, we can convert (3) into a specification for the original data _yt_ . This will lead us to another model representation which is directly in terms of the original data _yt_ .

The key to this is the following formula which writes the data in terms of the DFT.


We saw this formula previously in Lecture 8. It is known as the **Inverse DFT** formula.

The right hand side of (4) involves complex numbers ( _bj_ and exp(2 _πijt/n_ )). On the other hand, the left hand is the data _yt_ which is always real. Below we change the right hand side in (4) to make it consist of only real terms.

3

We can rewrite the inverse DFT formula in the following way.


We can ignore the imaginary part above as the dataset consists of real numbers, and this leads to


We are assuming that _n_ is odd and that _m_ = ( _n −_ 1) _/_ 2. We split the sum above into _j_ = 1 _, . . . , m_ and then _j_ = _m_ + 1 _, . . . , n −_ 1, and then use _bn−j_ =<sup>¯</sup> _bj_ or, equivalently, Re( _bn−j_ ) = Re( _bj_ ) and Im( _bn−j_ ) = _−_ Im( _bj_ ). This gives


where we also used cos(2 _π_ ( _n − j_ ) _t/n_ ) = cos(2 _πjt/n_ ) and sin(2 _π_ ( _n − j_ ) _t/n_ ) = _−_ sin(2 _πjt/n_ ).

In other words, when _n_ is odd and _m_ = ( _n −_ 1) _/_ 2, we have


where, for _j_ = 1 _, . . . , m_ ,


The formula (5) holds for every dataset _y_ 0 _, . . . , yn−_ 1. As a result, the model (3) is equivalent to (5) with


The spectrum model therefore has the following three equivalent definitions:

- _∼_

- • **Definition 1** : Re( _b_ 1) _,_ Im( _b_ 1) _, . . . ,_ Re( _bm_ ) _,_ Im( _bm_ ) are all independent with Re( _bj_ ) _,_ Im( _bj_ )<sup>i.i.d</sup> _N_ (0 _, γj_<sup>2)for</sup><sup>_j_= 1</sup><sup>_, . . . , m_.</sup>

- **Definition 2** :


with _β_ 11 _, β_ 21 _, β_ 12 _, β_ 22 _, . . . , β_ 1 _m, β_ 2 _m_ all independent with


4

i.i.d • **Definition 3** : _I_ ( _j/n_ ) = _f_ ( _j/n_ ) _ηj_ with _ηj ∼ Exp_ (1).

These two definitions are equivalent because of (5) and (6). The three sets of parameters ( _γ_ 1<sup>2</sup><sup>_, . . . , γ_</sup> _m_<sup>2)and(</sup><sup>_τ_2</sup> 1<sup>_, . . . , τ_</sup> _m_<sup>2)and(</sup><sup>_f_(1</sup><sup>_/n_)</sup><sup>_, . . . , f_(</sup><sup>_m/n_))arerelatedvia:</sup>


which is because

and

---

[← 3 Spectrum Model from DFT](03-3-spectrum-model-from-dft.md) · [Up: contents](index.md) · [5 Regularized Estimation →](05-5-regularized-estimation.md)
