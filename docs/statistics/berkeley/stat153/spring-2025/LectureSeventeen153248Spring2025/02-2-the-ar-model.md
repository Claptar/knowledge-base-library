---
title: 2 The AR Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeventeen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureSeventeen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 The AR Model

**Source:** [`LectureSeventeen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureSeventeen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let us start with the AR(1) model (we will later address AR(p) for _p ≥_ 2).

The AR(1) model is given by:


### **2.1 Detour: usual regression**

The model (2) looks just like a usual regression model:


except we are using _φ_ instead of _β_ for the coefficients, and the index is now _t_ as opposed to _i_ . Let us recall how one writes the likelihood (for parameter estimation) in (3). The data is ( _xi, yi_ ) _, i_ = 1 _, . . . , m_ ( _m_ is the number of data points). The likelihood is the probability density function of the data treated as a function of the parameters _θ_ = ( _β_ 0 _, β_ 1 _, σ_ ) ( _σ_ is the standard deviation of the errors):


We first assume independence across _i_ (i.e., ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) are independent) to get


Because the model (3) specifies an equation for _yi_ in terms of _xi_ , it is natural to condition first on _xi_ leading to:


Now we use the model equation to replace _yi_ by _β_ 0 + _β_ 1 _xi_ + _ϵi_ :


2

We now assume that _ϵi_ is independent of _xi_ and that _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ). These result in


How do we deal with the last term<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_fx_</sup> _i_<sup>_|θ_(</sup><sup>_xi_)?Wesimplyassumethatthistermdoes</sup> not depend on _θ_ so it only becomes a constant (in terms of _θ_ ) multiplicative factor in the likelihood that can be omitted leading to


This is the standard form of the likelihood in linear regression that we worked with previously (see e.g., Lectures 2 and 3). To sum up, we used the following assumptions to derive this likelihood:

1. Independence of ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ )

2. The model equation (3)

3. Independence of _ϵi_ and _xi_

4. _ϵi ∼ N_ (0 _, σ_<sup>2</sup> )

5. The density of _xi_ does not depend on _θ_ = ( _β_ 0 _, β_ 1 _, σ_ ).

### **2.2 Back to AR(1)**

Let us now get back to the AR(1) model (2). Superficially, (2) looks the same as (3) with _i_ = _t_ , _xi_ = _yt−_ 1 and _β_ 0 = _φ_ 0 and _β_ 1 = _φ_ 1. However, some of the other regression assumptions listed above do not hold for (2):

1. Independence of ( _xi, yi_ ) across _i_ no longer holds. This is because ( _xt, yt_ ) = ( _yt−_ 1 _, yt_ ) so one observation is shared between ( _xt, yt_ ) for successive values of _t_ .

2. The density of _xt_ = _yt−_ 1 will depend on _θ_ (because _yt−_ 1 = _φ_ 0 + _φ_ 1 _yt−_ 2 + _ϵt−_ 1 so _φ_ 0 _, φ_ 1 and _σ_ certainly affect _yt−_ 1).

As a result, we cannot use the same principles as in usual linear regression to write the likelihood for AR models. Instead we shall proceed as follows. As the data is _y_ 1 _, . . . , yn_ , the

3

likelihood is given by (below _θ_ = ( _φ_ 0 _, φ_ 1 _, σ_ ) denotes the set of parameters)

Likelihood for Model (2)


Now we assume that _ϵt_ is independent of _y_ 1 _, . . . yt−_ 1. This gives

Likelihood for Model (2)


With _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ), we get

which is equivalent to:

To sum up, we used the following assumptions to derive the likelihood (4):

1. The model equation (2).

2. Independence of _ϵt_ and _y_ 1 _, . . . , yt−_ 1 for each _t_ = 2 _, . . . , n −_ 1.

3. _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ).

The likelihood (4) has the term _fy_ 1 _|θ_ ( _y_ 1) which we should make explicit before we can compute estimators. Note that the model equation (2) is only for _t_ = 2 _, . . . , n_ which means that _y_ 1 never appears on the left side. So it is not possible to compute _fy_ 1 _|θ_ ( _y_ 1) using (2). There are two approaches of dealing with _fy_ 1 _|θ_ ( _y_ 1).

1. **Approach One** : Here one simply assumes that _fy_ 1 _|θ_ ( _y_ 1) does not depend on _θ_ . Then _fy_ 1 _|θ_ ( _y_ 1) becomes a constant factor in (4) that can be ignored in proportionality leading to


It is easy to verify that maximizing the above likelihood leads to estimates _φ_<sup>ˆ</sup> 0 _, φ_<sup>ˆ</sup> 1 that are identical to those obtained by regression _Y_ on _X_ as described in Section 1. The right hand side of (5) is actually equal to the conditional density of _y_ 2 _, . . . , yn_ given _y_ 1 _, θ_ (under the aforementioned assumptions: model (2), _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) and independence of _ϵt_ and _y_ 1 _, . . . , yt−_ 1). For this reason, (5) is called “Conditional Likelihood” and the resulting maximizers “Conditional MLEs” or “Conditional Least Squares Estimators”. “Conditional” here refers to conditional on _y_ 1.

4

2. **Approach Two** : Here one extends the model equation (2) to _t_ = 1 _,_ 0 _, −_ 1 _, −_ 2 _, . . ._ . This allows possible computation of _fy_ 1 _|θ_ ( _y_ 1) in the following way. Applying (2) for _t_ = 1 _,_ 0 _, −_ 1 _, −_ 2 _, . . ._ recursively, we get


Continuing this way with using (2) for _t_ = _−_ 2 _, −_ 3 _, . . . , −M_ (for some large _M_ ), we get


This equation is not enough to allow us to deduce _fy_ 1 _|θ_ ( _y_ 1) because it involves the unknown quantity _y−M_ . If _|φ_ 1 _| <_ 1, then the coefficient _φ_<sup>_M_</sup> 1<sup>+1</sup> in front of _y−M_ is very small. In this case, it might make sense to ignore the term _φ_<sup>_M_</sup> 1<sup>+1</sup> _y−M_ when _M_ is large. This allows us to write


The term<sup>�</sup><sup>_∞_</sup> _j_ =0<sup>_φ_</sup> 1<sup>_jϵ_1</sup><sup>_−j_isthesumofindependentnormalrandomvariables,soitis</sup> Normal with mean zero (as each _ϵ_ 1 _−j_ has mean zero) and with variance:


Thus when _|φ_ 1 _| <_ 1, we can write

which gives

Plugging this in (4), we get

Likelihood for (2)

This is a more complicated likelihood compared to (5). This is applicable only when _|φ_ 1 _| <_ 1. We shall see later the implications of this assumption. (6) is referred to as the full likelihood for AR(1), and the estimates obtained by maximization of (6) as full MLEs (as opposed to conditional MLEs obtained by maximizing (5)). In cases where the assumption _|φ_ 1 _| <_ 1 is reasonable, full MLEs will be different from conditional MLEs although when _n_ is large, they will generally be quite close to each other.

5

### **2.3 AR(p)**

The AR(p) model is given by:


We can write the likelihood as


The conditional likelihood is calculated as


In order to proceed further, we shall make the following assumption:


This is equivalent to assuming that _ϵt ∼ N_ (0 _, σ_<sup>2</sup> ) and that _ϵt_ is independent of _y_ 1 _, . . . , yt−_ 1. With (8), we get


Observe that, in order to write the above formula, we only used the model equation (7) for _t_ = _p_ + 1 _, . . . , n_ .

To obtain the parameter estimates, we can directly maximize this conditional likelihood. The resulting estimates, which are identical to the OLS method described in Section 1, are known as Conditional MLEs or Conditional Least Squares Estimates.

The full likelihood is


If we assume that _fy_ 1 _,...,yp|θ_ ( _y_ 1 _, . . . , yp_ ) does not depend on _θ_ , then maximizing the full likelihood is equivalent to maximizing the conditional likelihood. If we want to derive _fy_ 1 _,dots,yp|θ_ ( _y_ 1 _, . . . , yp_ ) in a more principled way, then we have to use the model equation (7) for smaller values of _t_ (i.e., _t_ = _p, p −_ 1 _, p −_ 2 _, . . . ,_ 0 _, −_ 1 _, . . ._ ). We shall see later how this is done (this will also require some assumptions similar to _|φ_ 1 _| <_ 1 for _p_ = 1).

6

---

[← 1 AutoRegressive Models](01-1-autoregressive-models.md) · [Up: contents](index.md) · [3 Predictions and Difference Equations →](03-3-predictions-and-difference-equations.md)
