---
title: 7 Lecture Seven
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Lecture Seven

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **7.1 The Kalman Filter**

Consider the linear Gaussian state space model:


with _X_ 0 _, U_ 1 _, . . . , V_ 0 _, V_ 1 _, . . ._ independent and _Ut ∼ N_ (0 _,_ Σ _t_ ) and _Vt ∼ N_ (0 _, Rt_ ). Each of the quantities _µ_ 0 _,_ Γ0 _, At, Bt,_ Σ _t, Rt_ appearing in the model above can depend on an unknown vector of parameters _θ_ . Every conditional distribution _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ is Gaussian and we can write


The Kalman filtering algorithm specifies how to compute _mt|t, Qt|t_ for _t_ = 0 _,_ 1 _, . . ._ using the following equations:


and


Equations (51) and (52) together comprise the Kalman Filter. The formal description of the Kalman Filter including the initialization is as follows. We are given the model (49) and we assume that _µ_ 0 _,_ Γ0 _, {At, t ≥_ 1 _}, {Bt, t ≥_ 0 _}_ , _{_ Σ _t, t ≥_ 0 _}_ and _{Rt, t ≥_ 0 _}_ are known. The Kalman filter for calculating the conditional distributions (50) for _s_ = _t_ is:

1. **Initialization** : Set _m_ 0 _|−_ 1 = _µ_ 0 and _Q_ 0 _|−_ 1 = Γ0. Implement (52) for _t_ = 0 to obtain _m_ 0 _|_ 0 and _Q_ 0 _|_ 0.

2. **Recursion** : For each _t_ = 1 _,_ 2 _, . . ._ , implement (51) and (52).

Note that the Kalman Filter algorithm also computes the one-step ahead prediction means _mt|t−_ 1 and covariances _Qt|t−_ 1 in intermediate computations. So the Kalman Filter can also be used to obtain these one-step ahead predictions.

### **7.2 Some Examples**

We shall give here some simple examples of linear Gaussian state space models and write the Kalman recursions more explicitly.

28

#### **7.2.1 Tracking One: Velocity Model**

Consider the problem of tracking the position of an object moving on a straight line. We observe the position of the object every ∆ _t_ seconds but these measurements are imprecise. For _k_ = 0 _,_ 1 _,_ 2 _, , . . ._ , let _xk_ denote the actual position of the object at time _k_ (∆ _t_ ) and let _yk_ denote the measurement. We assume that


for _k_ = 0 _,_ 1 _,_ 2 _, . . ._ . For the state model, in this “velocity model”, we assume that the velocity of the particle stays constant at a level _uk_ in the time interval [( _k −_ 1)(∆ _t_ ) _, k_ ∆ _t_ ] leading to the equation:


Further, we shall assume that _u_ 1 _, u_ 2 _, . . ._ are i.i.d _N_ (0 _, σu_<sup>2).Finally assume that</sup><sup>_x_0</sup><sup>_∼N_(0</sup><sup>_, C_)</sup> for a large positive constant _C_ . This is basically the local level model with the state evolution error variance equal to _σu_<sup>2(∆</sup><sup>_t_)2.</sup>

The Kalman filter for this model for computing


is easily checked to be given by


and


The Kalman Filter is initialized with _m_ 0 _|−_ 1 = 0 and _Q_ 0 _|−_ 1 = _C_ which leads to (via the filter update (39))


It is clear that when _C_ is large, the above equations imply that _m_ 0 _|_ 0 _≈ y_ 0 and _Q_ 0 _|_ 0 _≈ σϵ_<sup>2.</sup> Thus a commonly used initialization for the local level model is _m_ 0 _|_ 0 = _y_ 0 and _Q_ 0 _|_ 0 = _σϵ_<sup>2.</sup>

#### **7.2.2 Tracking Two: Acceleration Model**

Consider the same setting as the last subsection. We now consider a different model for the state evolution where we assume that the acceleration (not velocity) remains constant in each time period [( _k −_ 1)(∆ _t_ ) _, k_ (∆ _t_ )]. Denoting this acceleration by _ak_ , we see that the velocity at time ( _k −_ 1)(∆ _t_ ) (which we denote by _xk−_ 1 _,_ 2) and the velocity at time _k_ (∆ _t_ ) (which we denote by _xk,_ 2) are related by the equation:


29

Further the position at time ( _k −_ 1)(∆ _t_ ) (which we denote by _xk−_ 1 _,_ 1) and the position at time _k_ (∆ _t_ ) (which we denote by _xk,_ 1) are related by the equation:


Letting the state vector at time _k_ to be both the position and the velocity at time _k_ :


we can write the state evolution as

Because the accelerations _a_ 1 _, a_ 2 _, . . ._ are unknown, a simple way of dealing with them is to assume that:


Then the state evolution becomes

The equation relating the observation and state variables becomes


The Kalman filter for this model simplifies to the following equations. Note that _ms|t_ is a 2 _×_ 1 vector and _Qs|t_ is a 2 _×_ 2 matrix. The one-step prediction update is

and


The filter update is given by the two equations:


and


In the above, we used _Qt|t−_ 1[ _i, j_ ] for the ( _i, j_ )<sup>_th_</sup> entry of the matrix _Qt|t−_ 1 and _mt|t−_ 1[1] for the first entry of the 2 _×_ 1 vector _mt|t−_ 1.

30

#### **7.2.3 Tracking Three: Local Linear Model**

The local linear model that we saw previously can be seen as an approximation of the acceleration model of the last subsection. Specifically, in the position equation (41), we drop the last term _ak_ (∆ _t_ )<sup>2</sup> _/_ 2 the idea being that if ∆ _t_ is small, then this term will generally be negligible compared to at least one of the other two terms _xk−_ 1 _,_ 1(∆ _t_ ) and _xk−_ 1 _,_ 1(∆ _t_ ). This leads to the equations:


We can combine these two equations into one by using _xk,_ 2 =<sup>_xk_</sup><sup><u>+1</u></sup><sup>_<u>,</u>_</sup> ∆<sup>1</sup><sup>_−_</sup> _t_<sup>_xk,_1</sup> (which is obtained from the first equation) in the second equation to deduce

_xk,_ 1 _−_ 2 _xk−_ 1 _,_ 1 + _xk−_ 2 _,_ 1 = _ak−_ 1(∆ _t_ )<sup>2</sup> _∼ N_ (0 _, σa_<sup>2(∆</sup><sup>_t_)4)</sup>

which is the local linear model with the state evolution error variance equal to _σa_<sup>2(∆</sup><sup>_t_)4.</sup> This can be written as a state space model using as the state or as in the previous � _xxk−k,_ 11 _,_ 1�

_xk,_ 1 subsection with as the state. Note that this shows that there can �(∆ _t_ )<sup>_−_1</sup> ( _xk,_ 1 _− xk−_ 1 _,_ 1)� be many different ways to write a model in state space form. The Kalman recursions for the local level model are left as exercise.

### **7.3 Use of the Kalman Filter for Parameter Estimation by Maximum Likelihood**

As mentioned previously, the quantities _µ_ 0 _,_ Γ0 _, At, Bt,_ Σ _t, Rt_ appearing in the state space model (49) typically depend on an unknown vector of parameters _θ_ which needs to be estimated from the observed data _y_ 0 _, . . . , yT_ . A standard method for parameter estimation is maximum likelihood and the Kalman filter output is useful for writing down the likelihood function. To see this, first note that the likelihood for the observed data _y_ 0 _, . . . , yT_ is given by


Conditionally on _Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ , the random variables _Xt_ and _Vt_ are independent having the _N_ ( _mt|t−_ 1 _, Qt|t−_ 1) and _N_ (0 _, Rt_ ) respectively. Thus


Thus, for each _t_ = 0 _,_ 1 _, . . . , T_ , we have


where _| · |_ denotes determinant. Let

_ϵt_ ( _θ_ ) := _yt − Btmt|t−_ 1 and _Ht_ ( _θ_ ) := _BtQt|t−_ 1 _Bt_<sup>_′_+</sup><sup>_Rt_</sup>

for _t_ = 0 _,_ 1 _,_ 2 _, . . ._ . Then


31

Thus


For calculating this likelihood, we only need _mt|t−_ 1 and _Qt|t−_ 1 for _t_ = 0 _,_ 1 _,_ 2 _, . . ._ which can be obtained from the Kalman Filter. One can maximize likelihood by minimizing the right hand side above over the parameters _θ_ . Numerical optimization routines can be used for this purpose.

### **7.4 Recommended Reading for Today**

1. The local level model is analyzed in detail in Chapter 2 of the Durbin-Koopman book. In particular, see Section 2.2.1 for the Kalman filter updates in the local level model. Some comments on the initial distribution _X_ 0 _∼ N_ (0 _, C_ ) (for a large _C_ ) can be found in Section 2.9.

2. The acceleration model of Subsection 7.2.2 can be found in `https://en.wikipedia. org/wiki/Kalman_filter` (see Section 7).

3. For likelihood computation using the Kalman filter, see Section 9.6 of the Kitagawa book.

---

[← 6 Lecture Six](07-6-lecture-six.md) · [Up: contents](index.md) · [8 Lecture Eight →](09-8-lecture-eight.md)
