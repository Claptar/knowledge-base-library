---
title: 8 Lecture Eight
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 8 Lecture Eight

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **8.1 Some remarks on the local level model**

Consider the local level model:


i.i.d i.i.d where _X_ 0 _, Z_ 1 _, Z_ 2 _, . . . , ϵ_ 0 _, ϵ_ 1 _, . . ._ are independent with _Zt ∼ N_ (0 _, σZ_<sup>2)and</sup><sup>_ϵt_</sup> _∼ N_ (0 _, σϵ_<sup>2).</sup> The Kalman filter recursions for this model are given by

_mt|t−_ 1 = _mt−_ 1 _|t−_ 1 and _Qt|t−_ 1 = _Qt−_ 1 _|t−_ 1 + _σZ_<sup>2</sup>

and


Here _ms|t_ and _Qs|t_ denote the conditional mean and variance of _Xs_ given _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt_ (and _σZ, σϵ_ ).

It is interesting to note that _mt|t_ is a weighted linear combination of _mt|t−_ 1 and _yt_ . We see in simulations that when the _σZ_ parameter is large, then the filtering mean _mt|t_ is close to _yt_ for each _t ≥_ 0. This can be explained as follows. Because _Qt|t−_ 1 = _Qt−_ 1 _|t−_ 1 + _σZ_<sup>2</sup><sup>_≥σ_</sup> _Z_<sup>2,</sup> it follows that, when _σZ_ is large, each _Qt|t−_ 1 is also large. As a result, the weight for _yt_ dominates the weight for _mt|t−_ 1 in the formula for _mt|t_ leading to _mt|t ≈ yt_ when _σZ_ is large.

32

Note that _mt|t ≈ yt_ does not imply that the model is overfitting the observed data. This is because the log-likelihood multiplied by ( _−_ 2) is given by


When _σZ_ is large, we would have _mt−_ 1 _|t−_ 1 _≈ yt−_ 1 as remarked above. Thus the above expression for large _σZ_ becomes


The second term in the sum above is of smaller order compared to the first term when _σZ_ is large. Thus the behavior of the whole expression will be similar to the behavior to the first term which is increasing in _σZ_ . Thus as _σZ_ increases, the log-likelihood decreases (note that the above is the expression for **negative** log-likelihood multiplied by 2). This means that there is no overfitting for large _σZ_ (overfitting would happen when the likelihood keeps getting better and better when _σZ_ is increased which is not happening here).

In the last class, we mentioned that parameter estimates of _σZ_ and _σϵ_ can be obtained by maximizing the likelihood (or equivalently, minimizing negative two times the log-likelihood) over _σZ_ and _σϵ_ . The result of this optimization cannot be written in closed because it is a somewhat complicated optimization. This is because it depends on _σZ_ and _σϵ_ in a not-sosimple way. To highlight this, let us note that _Qt|t−_ 1 and _mt|t−_ 1 depend on _σZ_ and _σϵ_ , and also on the initial state variance _C_ . We shall therefore write them as _Qt|t−_ 1( _C, σZ, σϵ_ ) and _mt|t−_ 1( _C, σZ, σϵ_ ) respectively. We thus have


The dependence of this function on _C, σZ, σϵ_ is not so simple. Numerical routines can be used to optimize this function of _σZ_ and _σϵ_ . The following trick reduces this to a one-parameter optimization problem and it can be quite handy. To see this, first note that for _t_ = 0, we have _Q_ 0 _|−_ 1 = _C_ and _m_ 0 _|−_ 1 = 0. Thus


As _C_ is large, the first term is approximately log(2 _πC_ ) and the second term is zero. Thus


The log(2 _πC_ ) term does not depend on _σZ_ or _σϵ_ so it can be removed from the optimization so the goal is to minimize:


33

We shall now take _C_ = + _∞_ . The quantities _Qt|t−_ 1( _∞, σZ, σϵ_ ) and _mt|t−_ 1( _∞, σZ, σϵ_ ) are then obtained for _t_ = 1 _,_ 2 _, . . ._ by running the Kalman filter steps with the initialization _m_ 0 _|_ 0 = _y_ 0 and _Q_ 0 _|_ 0 = _σϵ_<sup>2.Ourgoalistominimize</sup>


We now note the following useful fact:


I will leave the proof of this fact as an exercise. To compute _mt|t−_ 1( _∞, σZ/σϵ,_ 1) and _Qt|t−_ 1( _∞, σZ/σϵ,_ 1), we would need to run the Kalman filter with _σZ_ and _σϵ_ replaced by _σZ/σϵ_ and 1 respectively (the initialization would then be _m_ 0 _|_ 0 = _y_ 0 and _Q_ 0 _|_ 0 = 1).

Because of the scaling fact (42), we can write _ℓ_<sup>_∗_</sup> ( _σZ, σϵ_ ) as


The goal is to minimize the above function over all _σϵ >_ 0 and _σZ >_ 0. Equivalently, we need to minimize this over all _σϵ >_ 0 and _q_ :=<sup>_<u>σ</u>_</sup> _σ_<sup>_<u>Z</u>_</sup> _ϵ_<sup>_>_0.Theadvantageofviewingtheproblem</sup> as an optimization over _σϵ_ and _q_ is that it is easy to find the best _σϵ_ for each value of _q_ . Specifically, we need to minimize


over both _σϵ >_ 0 and _q >_ 0. For each fixed _q_ , it is easy to find the minimizing _σϵ_ by simply taking the derivative with respect to _σϵ_<sup>2andsettingitequaltozero.Thisgives</sup>


Plugging this value of _σϵ_<sup>2in(43),weget</sup>


This function will need to be numerically minimized over _q >_ 0 to obtain the minimizer _q_ ˆ. This is an easier optimization problem (compared to minimizing _ℓ_<sup>_∗_</sup> ( _σZ, σϵ_ ) over both _σZ_ and _σϵ_ ) for numerical methods as it only depends on the one variable _q_ . After obtaining the minimizer _q_ ˆ, _σϵ_<sup>2isestimatedby</sup><sup>_σ_ˆ</sup> _ϵ_<sup>2(ˆ</sup><sup>_q_)(i.e.,therighthandsideof(44)with</sup><sup>_q_=</sup><sup>_q_ˆ)andthen</sup> _σZ_ is estimated by _q_ ˆ _σ_ ˆ _ϵ_ (ˆ _q_ ). Finally, note that to form the objective (45), we need to calculate _σ_ ˆ _ϵ_<sup>2(</sup><sup>_q_)and,forthis,itisnecessarytoimplementtheKalmanfilterwith</sup><sup>_σZ_setto</sup><sup>_q_and</sup><sup>_σϵ_</sup> set to 1 in order to calculate _mt|t−_ 1( _∞, q,_ 1) and _Qt|t−_ 1( _∞, q,_ 1).

34

### **8.2 Application of the Kalman Filter to Linear Regression**

Consider the usual linear regression setting where we observe data ( _z_ 0 _, y_ 0) _, . . . ,_ ( _zT , yT_ ) where _zt_ is the _p ×_ 1 covariate and _yt_ is the scalar response corresponding to index _t_ . The usual linear model for this setting assumes that the covariates _z_ 0 _, . . . , zT_ are deterministic and the response _yt_ is related to _zt_ via


In Bayesian treatments of the linear model, one supplements the model above with the prior


If no information on _β_ is available, one can set _µ_ 0 = 0 and Γ0 = _CI_ for a large constant _C_ . Having a prior is a good idea in general as it avoids degeneracy issues. For example, when the matrix _Z_ of covariates (whose rows are _z_ 0<sup>_′, . . . , z_</sup> _T_<sup>_′_)doesnothavefullcolumnrank,the</sup> usual least squares estimator is not defined but the Bayesian posterior is well-defined as long as Γ0 is invertible.

The posterior distribution of _β_ is given by


Direct computation of mean vector and covariance matrix of the above posterior distribution requires inverting the _p × p_ matrix Γ<sup>_−_</sup> 0<sup>1</sup> + _Z_<sup>_′_</sup> _Z/σ_<sup>2</sup> and this can be computationally costly (note that calculating Γ<sup>_−_</sup> 0<sup>1</sup> is usually not hard as Γ0 is commonly a constant multiple of the identity; the main issue here involves inverting Γ<sup>_−_</sup> 0<sup>1</sup> + _Z_<sup>_′_</sup> _Z/σ_<sup>2</sup> ).

The Kalman filter provides an alternative way of computing the posterior mean and variance via a sequential algorithm which does not involve matrix inversion at any step. This is described below. The first step is to write the linear regression model in state space form. We take the state variables to be _β_ 0 _, β_ 1 _, . . ._ with the state evolution as


The observation is


Finally the initial condition is _β_ 0 _∼ N_ ( _µ_ 0 _,_ Γ0). This linear Gaussian state space model is exactly the Bayesian linear regression model and so we can apply the Kalman filter. Note that (46) is simply the filtering distribution in this state space model at time _T_ . Thus


The Kalman filter provides an alternative way of computing _mT |T_ and _QT |T_ using the following recursions. Because _βt_ = _βt−_ 1, the one-step ahead prediction update is simply _mt|t−_ 1 = _mt−_ 1 _|t−_ 1 and _Qt|t−_ 1 = _Qt−_ 1 _|t−_ 1. The filter update is


35

These recursions are initialized with _m_ 0 _|−_ 1 = _µ_ 0 _, Q_ 0 _|−_ 1 = Γ0 leading to


The main point to be noted here is that, in the Kalman filter, at no point do we need to invert a _p × p_ matrix. There are matrix vector products and other elementary operations but there is no matrix inversion.

### **8.3 Prediction**

Prediction, in the context of state space models, refers to the problem of finding the distribution _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ for _s > t_ . The prediction problem for linear Gaussian state space models is readily solved by the Kalman filter. To see this, note that we need to find the mean _ms|t_ and covariance _Qs|t_ for each _s > t_ . The Kalman filter tells us how to compute _mt|t, Qt|t_ . The prediction problem for _s_ = _t_ + 1 is easily solved via (this is basically the same as the one-step ahead prediction update used in the Kalman filter):


Next for _s_ = _t_ + 2, observe that


Note now that


and further _Xt_ +1 and _Ut_ +2 are independent conditional on _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ . Thus

_Xt_ +2 _|_ ( _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ ) _∼ N_ ( _At_ +2 _mt_ +1 _|t, A_<sup>_′_</sup> _t_ +2<sup>_Q_</sup> _t_ +1 _|t_<sup>_At_+2+ Σ</sup><sup>_t_+2)</sup><sup>_._</sup>

Therefore


Note that the terms _mt_ +1 _|t_ and _Qt_ +1 _|t_ appearing on the right hand side above have already been calculated in (47).

More generally, one can write _ms|t, Qs|t_ for _s > t_ in terms of _ms−_ 1 _|t, Qs−_ 1 _|t_ as


This equation can be used recursively for _s_ = _t_ + 1 _, t_ + 2 _,_ to calculate all prediction distributions.

### **8.4 Smoothing**

Smoothing, in the context of state space models, refers to the problem of finding the distribution of _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ for _s ≤ t_ . These are calculated by backward recursion starting for _s_ = _t_ and then decreasing _s_ (note that the smoothing distribution for _s_ = _t_ is a filtering distribution which is given by the Kalman filter). The details for this will be discussed next week.

36

### **8.5 Recommended Reading for Today**

1. The technique described in Section 8.1 for reducing the likelihood optimization to a one-dimensional optimization problem can be found in Section 2.10.2 of the DurbinKoopman. This technique holds in some more settings as described in Section 9.6 of the Kitagawa book.

2. See Sections 3.1, 3.2 and 3.3 of the S¨arkk¨a book for treatment of linear regression and application of the Kalman filter for recursive linear regression. Also see Section 3.4 for a treatment of the linear regression with drift model.

3. The prediction recursions can be found in Section 9.5 of the Kitagawa book.

---

[← 7 Lecture Seven](08-7-lecture-seven.md) · [Up: contents](index.md) · [9 Lecture Nine →](10-9-lecture-nine.md)
