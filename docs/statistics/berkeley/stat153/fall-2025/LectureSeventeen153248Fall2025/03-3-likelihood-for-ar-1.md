---
title: 3 Likelihood for AR(1)
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureSeventeen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Likelihood for AR(1)

**Source:** [`LectureSeventeen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureSeventeen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us now write the likelihood for the AR(1) model (2). Superficially, (2) looks the same as (3) with _i_ = _t_ , _xi_ = _yt−_ 1 and _β_ 0 = _ϕ_ 0 and _β_ 1 = _ϕ_ 1. However, some of the other regression assumptions listed above do not hold for (2):

1. The density of _xt_ = _yt−_ 1 will depend on _θ_ (because _yt−_ 1 = _ϕ_ 0 + _ϕ_ 1 _yt−_ 2 + _ϵt−_ 1 so _ϕ_ 0 _, ϕ_ 1 and _σ_ certainly affect _yt−_ 1).

2. It is also unclear why _ϵ_ 2 _, . . . , ϵn_ should be independent of _x_ 2 = _y_ 1 _, . . . , xn_ = _yn−_ 1.

As a result, we cannot use the same principles as in usual linear regression to write the likelihood for AR models. Instead we shall proceed as follows (using a different set of assumptions). As the data is _y_ 1 _, . . . , yn_ , the likelihood is given by (below _θ_ = ( _ϕ_ 0 _, ϕ_ 1 _, σ_ )

3

denotes the set of parameters)

Likelihood for Model (2)


Now we assume that _ϵt_ is independent of _y_ 1 _, . . . yt−_ 1. This gives

Likelihood for Model (2)


With _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ), we get

which is equivalent to:

To sum up, we used the following assumptions to derive the likelihood (5):

1. The model equation (2).

2. Independence of _ϵt_ and _y_ 1 _, . . . , yt−_ 1 for each _t_ = 2 _, . . . , n −_ 1.

3. _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ).

The likelihood (5) has the term _fy_ 1 _|θ_ ( _y_ 1) which we should make explicit before we can compute estimators. Note that the model equation (2) is only for _t_ = 2 _, . . . , n_ which means that _y_ 1 never appears on the left side. So it is not possible to compute _fy_ 1 _|θ_ ( _y_ 1) using (2). There are two approaches of dealing with _fy_ 1 _|θ_ ( _y_ 1).

### **3.1 Approach One: Assume** _fy_ 1 _|θ_ ( _y_ 1) **does not depend on** _θ_

Here one simply assumes that _fy_ 1 _|θ_ ( _y_ 1) does not depend on _θ_ . Then _fy_ 1 _|θ_ ( _y_ 1) becomes a constant factor in (5) that can be ignored in proportionality leading to


This likelihood is identical to the likelihood in usual regression with _xt_ = _yt−_ 1 (even though the assumptions that led to the likelihood are different from the case of linear regression).

4

Because of this, Bayesian inference here (with the prior _ϕ_ 0 _, ϕ_ 1 _,_ log _σ_<sup>i.i.d</sup> _∼_ uniform( _−C, C_ ) will lead to identical results as in the case of linear regression. In other words, the posterior for ( _ϕ_ 0 _, ϕ_ 1) will be:


where _ϕ_<sup>ˆ</sup> 0 and _ϕ_<sup>ˆ</sup> 1 represent the least squares estimates obtained by regressing _yt_ on _yt−_ 1. Note that the residual degrees of freedom (i.e., the degrees of freedom of the _t_ -distribution) equal _n −_ 3 because the number of observations in this regression equals _n −_ 1 (as _t_ = 2 _, . . . , n_ ) and the number of columns of _X_ equals 2.

Frequentist inference for AutoRegression will be quite different from inference in linear regression. First note that, under the likelihood (6), the MLEs of _ϕ_ 0 _, ϕ_ 1 _, σ_ will be identical to the MLEs in linear regression (because the likelihood (6) is the same as for linear regression). However, in order to derive the distribution of the MLEs, we now have to use the AR assumptions which are more complicated. This part is usually done by asymptotics i.e., by letting _n →∞_ (see for example Shumway and Stoffer [1, Chapter 4]). In this analysis, inference is based on the normal distribution and justified in the large sample limit as _n →∞_ ; in other words, _t_ -distributions no longer arise.

This is one concrete problem where Bayesian inference and frequentist inference differ. Bayesian inference is simpler while frequentist inference is more complicated and uses asymptotic arguments (specifically, Central Limit Theorems and Laws of Large Numbers for dependent random variables).

Usual library functions for AutoRegression (such as the function `AutoReg` in the `statsmodels` library) use the frequentist formulas so they give different results from those obtained by just running the OLS function for regressing _yt_ on _xt_ = _yt−_ 1. For example, they give standard errors and _z_ -scores as opposed to _t_ -scores. Most of the time in practice, the difference between the two kinds of inferences is negligible. However, strictly speaking, they are different.

### **3.2 Approach Two: Computing** _fy_ 1 _|θ_ ( _y_ 1) **by extending** (2) **to** _t ≤_ 1

So far we assumed the model equation (2) only for _t_ = 2 _, . . . , n_ . With this, _y_ 1 never appears on the left hand side in (2) which means that we have not assumed anything about _fy_ 1 _|θ_ ( _y_ 1). In order to be able to compute it, a natural idea is to extend the model equation for _t_ = 1 _,_ 0 _, −_ 1 _, . . ._ . This allows computation of _fy_ 1 _|θ_ ( _y_ 1) in the following way. Applying (2) for _t_ = 1 _,_ 0 _, −_ 1 _, −_ 2 _, . . ._ recursively, we get


Continuing this way with using (2) for _t_ = _−_ 2 _, −_ 3 _, . . . , −M_ (for some large _M_ ), we get


5

This equation is not enough to allow us to deduce _fy_ 1 _|θ_ ( _y_ 1) because it involves the unknown quantity _y−M_ . If _|ϕ_ 1 _| <_ 1, then the coefficient _ϕ_<sup>_M_</sup> 1<sup>+1</sup> in front of _y−M_ is very small. In this case, it might make sense to ignore the term _ϕ_<sup>_M_</sup> 1<sup>+1</sup> _y−M_ when _M_ is large. This allows us to write


The term<sup>�</sup><sup>_∞_</sup> _j_ =0<sup>_ϕ_</sup> 1<sup>_jϵ_1</sup><sup>_−j_isthesumofindependentnormalrandomvariables,soitisNormal</sup> with mean zero (as each _ϵ_ 1 _−j_ has mean zero) and with variance:


Thus when _|ϕ_ 1 _| <_ 1, we can write

which gives


Plugging this in (5), we get

Likelihood for (2)


This is a more complicated likelihood compared to (6). This is applicable only when _|ϕ_ 1 _| <_ 1. We shall see later the implications of this assumption.

---

[← 2 Detour: usual linear regression](02-2-detour-usual-linear-regression.md) · [Up: contents](index.md) · [4 Two AR(1) Models →](04-4-two-ar-1-models.md)
