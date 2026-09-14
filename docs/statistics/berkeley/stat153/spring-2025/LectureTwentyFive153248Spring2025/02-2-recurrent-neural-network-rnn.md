---
title: 2 Recurrent Neural Network (RNN)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyFive153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Recurrent Neural Network (RNN)

**Source:** [`LectureTwentyFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyFive153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

RNN is given by


This formula can also be written as


Here the activation function _σ_ tanh is the tanh activation function given by


The parameters now are _Wr_ ( _k × k_ matrix), _W_ ( _k × p_ matrix), _b_ ( _k ×_ 1 vector), _β_ 0 (scalar) and _β_ ( _k ×_ 1 vector).

2

In (6), _rt_ depends on all of _xu, u ≤ t_ . To see this, just note (below _σ_ = _σ_ tanh)


From the above, _rt_ clearly depends on all of _x_ 1 _, . . . , xt_ . But the strength of the dependence of _rt_ on _xs_ varies with _s_ . To see this, observe that


Here _∂x∂rut_<sup>denotesthe</sup><sup>_k× p_JacobianMatrixofderivativesof</sup><sup>_rt_withrespectto</sup><sup>_xu_.On</sup> the right hand side in (8), _σ_<sup>_′_</sup> ( _st_ ) should be interpreted as _k × k_ diagonal matrices whose diagonal entries are obtained by applying the _σ_<sup>_′_</sup> ( _u_ ) = _dud_<sup>_σ_(</sup><sup>_u_)functiontoeachelementof</sup><sup>_st_</sup> ( _σ_<sup>_′_</sup> ( _st−_ 1) _, . . ._ are similarly defined as _k × k_ diagonal matrices).

As a concrete example,


Note that these gradient formulae are with respect to inputs _xu_ , and not with respect to the parameters (which is crucial to parameter estimation). In the formula (8), it is clear that when _u_ is much smaller than _t_ , many more terms appear in the right hand side of (8) compared to the case when _u_ is closer to _t_ . Note here that _σ_ is the tanh activation function:


Thus each _σ_<sup>_′_</sup> ( _·_ ) term will add a fractional multiplier to _∂rt/∂xu_ . The number of these fractional multipliers will increase as _u_ decreases in (8).

Further the matrix _Wr_ also plays a key role in (8). For the model equation in (5) to be stable, _Wr_ needs to have spectral radius (defined as the largest modulus of any eigenvalue) to be strictly smaller than one. In that case, each additional _Wr_ multiplier will bring the whole term down, leading to _∂rt/∂xu_ being small when _u_ is much smaller than _t_ .

This points to the following shortcoming of RNNs that more sophisticated models such as GRUs and LSTMs attempt to fix. We want _rt_ to represent the ideal summary of _x_ 1 _, . . . , xt_ that is relevant for the output _yt_ . However, in an RNN, _rt_ effectively only depends on those inputs _xu_ which are somewhat close to _t_ . In this sense, the RNN can be thought of as not having a very long memory.

This “lack of long memory” problem with RNNs can be fixed by use of GRUs and LSTMs.

---

[← 1 Nonlinear AutoRegression](01-1-nonlinear-autoregression.md) · [Up: contents](index.md) · [3 GRU (Gated Recurrent Unit) →](03-3-gru-gated-recurrent-unit.md)
