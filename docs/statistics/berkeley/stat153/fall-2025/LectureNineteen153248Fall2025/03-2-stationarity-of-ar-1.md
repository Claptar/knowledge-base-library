---
title: 2 Stationarity of AR(1)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNineteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureNineteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Stationarity of AR(1)

**Source:** [`LectureNineteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureNineteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The AR(1) equation is


One issue is that this equation does not fully specify _yt_ and there can be multiple processes _{yt}_ that satisfy (2):

1. Suppose _y_ 0 = 10. Define _y_ 1 _, y_ 2 _, y_ 3 _, . . ._ recursively via (2). Also define _y−_ 1 _, y−_ 2 _, y−_ 3 _, . . ._ recursively via the following equation for _t_ = 0 _, −_ 1 _, −_ 2 _, . . ._ :


Note that (3) is just a restatement of (2) obtained by rearranging (2) with _yt−_ 1 on the left hand side. The resulting time series model will then clearly satisfy (2). However it will not be stationary because:

var( _y_ 0) = 0 and var( _y_ 1) = var( _φ_ 0 + _φ_ 1 _y_ 0 + _ϵ_ 1) = var( _φ_ 0 + _ϵ_ 1) = var( _ϵ_ 1) = _σ_<sup>2</sup> _._

2. Suppose _|φ_ 1 _| <_ 1 and define


The summation in the right hand side above is an infinite summation, and hence we need to address convergence issues. Because _|φ_ 1 _| <_ 1, the terms _φ_<sup>_j_</sup> 1<sup>rapidlydecayto0</sup> as _j_ increases. This ensures that<sup>�</sup><sup>_∞_</sup> _j_ =0<sup>_φ_</sup> 1<sup>_jϵt−j_iswell-defined.</sup>

It is easy to check that (4) satisfies (2) because:


It is also true that (4) is a stationary model. This is because


and, for _h ≥_ 0,


4

Because cov ( _ϵt−j, ϵt_ + _h−k_ ) is non-zero (equal to _σ_<sup>2</sup> ) only when _t − j_ = _t_ + _h − k_ i.e., _k_ = _j_ + _h_ , we get


This clearly shows that _{yt}_ is stationary with ACVF and ACF given by:


We have thus proved that (4) is a stationary time series model that satisfies the AR(1) equation (2) when _|φ_ 1 _| <_ 1. In fact, it turns out that (4) is the only stationary solution of (2) when _|φ_ 1 _| <_ 1 (I am skipping proof of this). Thus (4) is the unique stationary AR(1) model when _|φ_ 1 _| <_ 1. The model (4) when _|φ_ 1 _| <_ 1 is known as the **causal stationary** AR(1) model. Causal refers to the fact that _yt_ is fully determined by present and past values of _{ϵt}_ .

3. Suppose _|φ_ 1 _| >_ 1 and define


Note that _yt_ is well-defined because the infinite sum above has the coefficients _φ_<sup>_−_</sup> 1<sup>_j_</sup> which decay rapidly as _|φ_ 1 _| >_ 1. It is easy to check that (5) also satisfies the AR(1) equation (2) and is stationary. In fact, it is the unique stationary AR(1) for _|φ_ 1 _| >_ 1. The model (5) is called the **non-causal, stationary** AR(1). It is non-causal because _yt_ depends on the future values of _ϵt_ +1 _, ϵt_ +2 _, . . ._ .

For the model (5), it is certainly not true that _ϵt_ is independent of _yt−_ 1 _, yt−_ 2 _, yt−_ 3 _, . . ._ . Recall that we used this estimation while writing the likelihood for AR(1) for parameter estimation. Thus, if we attempt to estimate the parameters _φ_ 0 _, φ_ 1 _, σ_ of (5) using our AR-parameter estimation technique, we will get incorrect an estimate of _φ_ 1 (for more details, see Example 3.3 and 3.4 in the Shumway-Stoffer book 4th edition).

To summarize the above discussion, there exist many non-stationary AR(1) time series models. When _|φ_ 1 _| <_ 1, there exists a unique stationary AR(1) model that is given by the formula (4), this is called the causal, stationary AR(1) model. When _|φ_ 1 _| >_ 1, there also exists a unique stationary AR(1) model that is given by the formula (5), this is called the non-causal, stationary AR(1) model.

When _|φ_ 1 _|_ = 1 (i.e., _φ_ 1 = 1 or _φ_ 1 = _−_ 1), neither of the two formulae (4) and (5) are meaningful (i.e., the infinite series do not converge). Here it turns out that there is no stationary AR(1) model. To see this, consider the case _φ_ 1 = 1 (the case _φ_ 1 = _−_ 1 is similar) where


This implies that for every _t ≥_ 1


When _φ_ 0 _̸_ = 0, clearly _yt_ and _y_ 0 have different means (because E _yt_ = E _y_ 0 + _tφ_ 0) so there is no stationarity. But even if _φ_ 0 = 0, we have

var( _yt − y_ 0) = var( _ϵ_ 1 + _· · ·_ + _ϵt_ ) = _tσ_<sup>2</sup>

5

which approaches _∞_ as _t ↑∞_ . But if _{yt}_ were stationary, we would have

var( _yt − y_ 0) _≤_ 2var( _yt_ ) + 2var( _y_ 0) _≤_ constant _._

Thus there are two kinds of AR(1): stationary and non-stationary. Stationarity is only possible when _|φ_ 1 _|̸_ = 1. There are also two kinds of stationary AR(1) models. When _|φ_ 1 _| <_ 1, the stationary AR(1) model has the formula (4); this is the causal kind of stationarity. When _|φ_ 1 _| >_ 1, the stationary AR(1) model has the formula (5); this is the non-causal kind of stationarity.

---

[← 1 Time Series Models and Stationarity](02-1-time-series-models-and-stationarity.md) · [Up: contents](index.md) · [References →](04-references.md)
