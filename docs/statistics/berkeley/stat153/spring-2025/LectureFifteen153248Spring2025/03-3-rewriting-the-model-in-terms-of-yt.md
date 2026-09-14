---
title: 3 Rewriting the Model in terms of yt
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFifteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Rewriting the Model in terms of yt

**Source:** [`LectureFifteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFifteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The model (1) is written in terms of the DFT _bj_ . Because the original data can be written in terms of the DFT, we can convert (1) into a specification for the original data _yt_ . This will lead us to the model representation that we already saw in Lecture 13.

The key to this is the following formula which writes the data in terms of the DFT.


We saw this formula previously in Lecture 8. It is known as the **Inverse DFT** formula.

The right hand side of (3) involves complex numbers ( _bj_ and exp(2 _πijt/n_ )). On the other hand, the left hand is the data _yt_ which is always real. Below we change the right hand side in (3) to make it consist of only real terms.

We can rewrite the inverse DFT formula in the following way.


We can ignore the imaginary part above as the dataset consists of real numbers, and this leads to


We are assuming that _n_ is odd and that _m_ = ( _n −_ 1) _/_ 2. We split the sum above into _j_ = 1 _, . . . , m_ and then _j_ = _m_ + 1 _, . . . , n −_ 1, and then use _bn−j_ =<sup>¯</sup> _bj_ or, equivalently, Re( _bn−j_ ) = Re( _bj_ ) and Im( _bn−j_ ) = _−_ Im( _bj_ ). This gives


where we also used cos(2 _π_ ( _n − j_ ) _t/n_ ) = cos(2 _πjt/n_ ) and sin(2 _π_ ( _n − j_ ) _t/n_ ) = _−_ sin(2 _πjt/n_ ).

3

In other words, when _n_ is odd and _m_ = ( _n −_ 1) _/_ 2, we have

where, for _j_ = 1 _, . . . , m_ ,


The formula (4) holds for every dataset _y_ 0 _, . . . , yn−_ 1. As a result, the model (1) is equivalent to (4) with


The spectrum model therefore has the following two equivalent definitions:

- _∼_

- • **Definition 1** : Re( _b_ 1) _,_ Im( _b_ 1) _, . . . ,_ Re( _bm_ ) _,_ Im( _bm_ ) are all independent with Re( _bj_ ) _,_ Im( _bj_ )<sup>i.i.d</sup> _N_ (0 _, γj_<sup>2)for</sup><sup>_j_= 1</sup><sup>_, . . . , m_.</sup>

- **Definition 2** :


with _β_ 11 _, β_ 21 _, β_ 12 _, β_ 22 _, . . . , β_ 1 _m, β_ 2 _m_ all independent with


These two definitions are equivalent because of (4) and (5). The two sets of parameters _γ_ 1<sup>2</sup><sup>_, . . . , γ_</sup> _m_<sup>2and</sup><sup>_τ_2</sup> 1<sup>_, . . . , τ_</sup> _m_<sup>2arerelatedvia:</sup>


This is because


The power spectrum is given by:

---

[← 2 Power Spectral Density](02-2-power-spectral-density.md) · [Up: contents](index.md) · [4 Two key properties of the Spectrum Model →](04-4-two-key-properties-of-the-spectrum-model.md)
