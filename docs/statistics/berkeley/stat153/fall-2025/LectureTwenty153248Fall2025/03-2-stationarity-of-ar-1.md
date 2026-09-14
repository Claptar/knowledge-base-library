---
title: 2 Stationarity of AR(1)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwenty153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Stationarity of AR(1)

**Source:** [`LectureTwenty153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwenty153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last lecture, we discussed whether the AR(1) model is stationary. The AR(1) difference equation is _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _ϵt_ . This is an implicit equation because _y_ appears in both sides of the equation. To be able to calculate mean, variance and covariance etc., we need a more explicit formula for _yt_ .

One way to get such an explicit formula is to apply the difference equation recursively on the right hand side as:


2

We continue in this way writing _yt−_ 3 = _φ_ 0 + _φ_ 1 _yt−_ 4 + _ϵt−_ 3 and then _yt−_ 4 = _φ_ 0 + _φ_ 1 _yt−_ 5 + _ϵt−_ 4 and so on. This leads to


This formula is true for every value of _M ≥_ 0 and every _φ_ 0 _, φ_ 1. The right hand side of (2) still depends on a _y_ -value (specifically _yt−M −_ 1).

Suppose now that _|φ_ 1 _| <_ 1. Then _φ_<sup>_M_</sup> 1<sup>+1</sup> decays rapidly to zero. In this case, we can let _M →∞_ in (2) and use


Thus taking _M →∞_ in (2) leads to


This expression is well-defined when _|φ_ 1 _| <_ 1. It is easy to check that _yt_ defined as (3) satisfies the AR(1) equation _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _ϵt_ . In the last lecture, we saw that (3) is a stationary time series model with:


In the formula (3), it is clear that _yt_ is determined by _ϵt, ϵt−_ 1 _, . . ._ i.e., by the present and past values of _ϵt_ . For this reason, (3) is called **Causal, Stationary AR(1)** (causal here roughly means that _yt_ is fully determined by present and past values of _{ϵt}_ ). One consequence of this kind of causality is that _ϵt_ is independent of the past _y_ -values _yt−_ 1 _, yt−_ 2 _, yt−_ 3 _. . . ._ (this is because these past _y_ -values only depend on _ϵt−_ 1 _, ϵt−_ 2 _, . . ._ which are all independent of _ϵt_ ).

When _|φ_ 1 _| ≥_ 1, the terms in the right hand side of (2) do not converge when _M →∞_ . In this case, it is not possible to get a stationary solution _yt_ of the AR equation which depends only on present and past _ϵ_ -values _ϵt, ϵt−_ 1 _, . . ._ . In other words, there is no causal stationary solution to the AR(1) equation when _|φ_ 1 _| ≥_ 1.

When _|φ_ 1 _| >_ 1 (note the strict inequality), there is a non-causal stationary solution for the AR(1) equation. This is obtained by rewriting the AR(1) equation as:


3

and then recursively plugging in _yt_ +1 _, yt_ +2 _, . . ._ as:


Letting _M →∞_ and using _|φ_ 1 _| >_ 1 (so that _|_ 1 _/φ_ 1 _| <_ 1), we get


It can be checked that (5) is also stationary (note now that _|φ_ 1 _| >_ 1) and satisfies the AR(1) equation _yt_ = _φ_ 0 + _φ_ 1 _yt−_ 1 + _ϵt_ . This AR(1) process is called **non-causal** because _yt_ depends on future values _ϵt_ +1 _, ϵt_ +2 _, . . ._ . Here _ϵt_ is **not** independent of the past _y_ -values _yt−_ 1 _, yt−_ 2 _, . . ._ .

If _|φ_ 1 _|_ = 1 (i.e., if _φ_ 1 = 1 or _φ_ 1 = _−_ 1), then neither (2) nor (4) converge as _M →∞_ . In fact, in this case ( _|φ_ 1 _|_ = 1), there cannot be a stationary solution to the AR(1) equation.

### **2.1 Practical Implications**

In practice, while fitting the AR(1) model, we use the `AutoReg` function (from the `statsmodels` library) which works with the likelihood:


This likelihood fixes the value of _y_ 1 and assumes that each _ϵt_ is independent of the past values _yt−_ 1 _, yt−_ 2 _, . . ._ . In other words, the model considered is:


i.i.d where _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) and independent of _yt−_ 1 _, . . . , y_ 1 for each _t_ = 2 _, . . . , n_ . The parameters _φ_ 0 _, φ_ 1 _, σ_ are estimated in the usual way (as is done in linear regression). For predictions, one works with the fitted model where the parameters are replaced by their estimates _φ_<sup>ˆ</sup> 0 _, φ_<sup>ˆ</sup> 1 (and also _σ_ ˆ).

Based on the value of _φ_<sup>ˆ</sup> 1, the following things can happen:

> 1. **Case One:** _|φ_<sup>ˆ</sup> 1 _| >_ 1. This happens often when we fit the AR(1) model directly to economic data (such as GDP or GNP). Here the fitted model (7) (with _φ_ 0 = _φ_<sup>ˆ</sup> 0 and _φ_ 1 = _φ_<sup>ˆ</sup> 1) is very different from the non-causal stationary AR(1) model given by (5). Note again that for (5), _ϵt_ becomes dependent on the past values _yt−_ 1 _, yt−_ 2 _, . . ._ . The fitted model (7) is quite far from being stationary and future predictions will often exhibit explosive behavior when the prediction horizon increases.

4

2. **Case Two:** _|φ_<sup>ˆ</sup> 1 _| <_ 1. This also happens very often. For economic data, this often happens after some preprocessing (e.g., by taking logarithms of the raw data and then differences once or twice). In this case, the fitted model (7) is also non-stationary and distinct from the causal stationary model (3). However, the discrepancy is minimal and they behave similarly in many ways:

   - a) The likelihood for (3) is


We saw this form of the likelihood in Lecture 17. The only difference between this likelihood and the likelihood (6) is the presence of the term involving _y_ 1. When _n_ is large, this single term (which only involves the first data point) does not affect the overall likelihood significantly, so both likelihood maximizations lead to similar answers.

- b) Recursing the difference equation in (7) from _t, . . . ,_ 2, we obtain (basically taking _M_ = _t −_ 2 in (2))


Because _|φ_ 1 _| <_ 1 (so that _|φ_ 1 _|_<sup>_j_</sup> decreases rapidly), we can expect the above to be close to (3) as long as _t_ is not very small.

- c) Future predictions for the models (7) and (3) work in identical fashion (for fixed identical parameter values). These predictions only use independence of _ϵt_ and past _y_ -values _yt−_ 1 _, yt−_ 2 _, . . ._ which is true in both (7) and (3).

Because of these reasons, when _|φ_<sup>ˆ</sup> 1 _| <_ 1, even though `AutoReg` is fitting (7), it is common to pretend as if we are working with the causal stationary AR(1) model (3).

3. **Case Three:** _|φ_<sup>ˆ</sup> 1 _|_ = 1. This is either _φ_<sup>ˆ</sup> 1 = 1 or _φ_<sup>ˆ</sup> 1 = _−_ 1. These models are all non-stationary. The case _φ_<sup>ˆ</sup> 1 = _−_ 1 almost never arises in practice (unless the data has a strange wild oscillatory pattern from each time point to the next). The case _φ_ ˆ1 = 1 is much more applicable. `AutoReg` may not give _φ_ ˆ1 = 1 exactly but it might give _φ_<sup>ˆ</sup> 1 that is close to 1. Note that when _φ_ 1 = 1, the AR(1) model equation can be rewritten as _yt − yt−_ 1 = _φ_ 0 + _ϵt_ ; this suggests preprocessing the data by taking successive differences _yt − yt−_ 1 and trying to fit models to this differenced data. AR(1) predictions with _φ_<sup>ˆ</sup> 1 = 1 grow linearly which may be well-suited for many datasets.

Thus from the practical perspective where we only consider causal models, stationary only corresponds to _|φ_ 1 _| <_ 1. (When _|φ_ 1 _| >_ 1, mathematically speaking, there is a stationary AR(1) model but this is non-causal and does not correspond to our likelihoods and fitting technique).

Next we shall look at AR( _p_ ) models for _p ≥_ 2 and discuss the analogue of the causalstationarity condition _|φ_ 1 _|_ when _p ≥_ 2.

Before we do that however, let us first go over an alternative method of deriving the causal stationary AR(1) model formula (3) using a formal technique involving Backshift notation.

Before describing this technique, we need to introduce the backshift notation.

5

---

[← 1 Moving Average (MA) Models](02-1-moving-average-ma-models.md) · [Up: contents](index.md) · [3 Backshift Notation →](04-3-backshift-notation.md)
