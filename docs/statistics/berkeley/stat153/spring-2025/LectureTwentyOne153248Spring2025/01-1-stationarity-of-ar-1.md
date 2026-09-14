---
title: 1 Stationarity of AR(1)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwentyOne153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Stationarity of AR(1)

**Source:** [`LectureTwentyOne153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwentyOne153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The AR(1) equation is


One issue is that this equation does not fully specify _yt_ and there can be multiple processes _{yt}_ that satisfy (1):

1. Suppose _y_ 0 = 10. Define _y_ 1 _, y_ 2 _, y_ 3 _, . . ._ recursively via (1). Also define _y−_ 1 _, y−_ 2 _, y−_ 3 _, . . ._ recursively via the following equation for _t_ = 0 _, −_ 1 _, −_ 2 _, . . ._ :


Note that (2) is just a restatement of (1) obtained by rearranging (1) with _yt−_ 1 on the left hand side. The resulting time series model will then clearly satisfy (1). However it will not be stationary because:


2. Suppose _|φ_ 1 _| <_ 1 and define


The summation in the right hand side above is an infinite summation, and hence we need to address convergence issues. Because _|φ_ 1 _| <_ 1, the terms _φ_<sup>_j_</sup> 1<sup>rapidlydecayto0</sup> as _j_ increases. This ensures that<sup>�</sup><sup>_∞_</sup> _j_ =0<sup>_φ_</sup> 1<sup>_jϵt−j_iswell-defined.</sup>

1

It is easy to check that (3) satisfies (1) because:


It is also true that (3) is a stationary model. This is because


and, for _h ≥_ 0,


Because cov ( _ϵt−j, ϵt_ + _h−k_ ) is non-zero (equal to _σ_<sup>2</sup> ) only when _t − j_ = _t_ + _h − k_ i.e., _k_ = _j_ + _h_ , we get


This clearly shows that _{yt}_ is stationary with ACVF and ACF given by:


We have thus proved that (3) is a stationary time series model that satisfies the AR(1) equation (1) when _|φ_ 1 _| <_ 1. In fact, it turns out that (3) is the only stationary solution of (1) when _|φ_ 1 _| <_ 1 (I am skipping proof of this). Thus (3) is the unique stationary AR(1) model when _|φ_ 1 _| <_ 1. The model (3) when _|φ_ 1 _| <_ 1 is known as the **causal stationary** AR(1) model. Causal refers to the fact that _yt_ is fully determined by present and past values of _{ϵt}_ .

3. Suppose _|φ_ 1 _| >_ 1 and define


Note that _yt_ is well-defined because the infinite sum above has the coefficients _φ_<sup>_−_</sup> 1<sup>_j_</sup> which decay rapidly as _|φ_ 1 _| >_ 1. It is easy to check that (4) also satisfies the AR(1) equation (1) and is stationary. In fact, it is the unique stationary AR(1) for _|φ_ 1 _| >_ 1. The model (4) is called the **non-causal, stationary** AR(1). It is non-causal because _yt_ depends on the future values of _ϵt_ +1 _, ϵt_ +2 _, . . ._ .

2

For the model (4), it is certainly not true that _ϵt_ is independent of _yt−_ 1 _, yt−_ 2 _, yt−_ 3 _, . . ._ . Recall that we used this estimation while writing the likelihood for AR(1) for parameter estimation. Thus, if we attempt to estimate the parameters _φ_ 0 _, φ_ 1 _, σ_ of (4) using our AR-parameter estimation technique, we will get incorrect an estimate of _φ_ 1 (for more details, see Example 3.3 and 3.4 in the Shumway-Stoffer book 4th edition).

To summarize the above discussion, there exist many non-stationary AR(1) time series models. When _|φ_ 1 _| <_ 1, there exists a unique stationary AR(1) model that is given by the formula (3), this is called the causal, stationary AR(1) model. When _|φ_ 1 _| >_ 1, there also exists a unique stationary AR(1) model that is given by the formula (4), this is called the non-causal, stationary AR(1) model.

When _|φ_ 1 _|_ = 1 (i.e., _φ_ 1 = 1 or _φ_ 1 = _−_ 1), neither of the two formulae (3) and (4) are meaningful (i.e., the infinite series do not converge). Here it turns out that there is no stationary AR(1) model. To see this, consider the case _φ_ 1 = 1 (the case _φ_ 1 = _−_ 1 is similar) where


This implies that for every _t ≥_ 1


When _φ_ 0 _̸_ = 0, clearly _yt_ and _y_ 0 have different means (because E _yt_ = E _y_ 0 + _tφ_ 0) so there is no stationarity. But even if _φ_ 0 = 0, we have


which approaches _∞_ as _t ↑∞_ . But if _{yt}_ were stationary, we would have


Thus there are two kinds of AR(1): stationary and non-stationary. Stationarity is only possible when _|φ_ 1 _|̸_ = 1. There are also two kinds of stationary AR(1) models. When _|φ_ 1 _| <_ 1, the stationary AR(1) model has the formula (3); this is the causal kind of stationarity. When _|φ_ 1 _| >_ 1, the stationary AR(1) model has the formula (4); this is the non-causal kind of stationarity.

---

[Up: contents](index.md) · [2 On the formulae for stationary AR(1) →](02-2-on-the-formulae-for-stationary-ar-1.md)
