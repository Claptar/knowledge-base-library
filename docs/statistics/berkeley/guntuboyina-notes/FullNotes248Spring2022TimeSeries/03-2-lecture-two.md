---
title: 2 Lecture Two
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Lecture Two

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In the last class, we introduced state space models and looked at two examples (a tracking model and the local level model). To recap, state space models describe the distribution of _Y_ 0 _, . . . , YT_ in terms of a hidden set of random variables _X_ 0 _, . . . , XT_ . The joint distribution of _X_ 0 _, Y_ 0 _, . . . , XT , YT_ is specified via the joint density:


This means that the density of _X_ 0 is _p_ 0, the conditional density of _Xt_ given _Xt−_ 1 = _xt−_ 1 (as well as given _Xt−_ 1 = _xt−_ 1 _, . . . , X_ 0 = _x_ 0) equals _pt_ ( _xt | xt−_ 1) and the conditional density of _Yt_ given _Xt_ = _xt_ (as well as given _Xt_ = _xt, Xs_ = _xs_ for _s̸_ = _t_ ) equals _ft_ ( _yt | xt_ ).

Specifying the joint distribution via the joint density (4) requires writing down _p_ 0( _x_ 0), _pt_ ( _xt | xt−_ 1) as well as _ft_ ( _yt | xt_ ). In practice, people specify state space models via equations involving independent random variables. More precisely, one usually first specifies the distribution _p_ 0 of _X_ 0 (this is often a diffuse density such as a normal with a large variance or a uniform over a large range), and then specify the distribution of _Xt_ via the equation:


7

where _{Ut}_ are independent random variables that are also independent of _X_ 0. Finally the distribution of _Yt_ is specified via


where _{Vt}_ are independent random variables that are also independent of _{Ut}_ and _X_ 0. The functions _Kt_ and _Ht_ in (5) and (6) can be completely arbitrary.

Linear Gaussian State Space Models form a special case of state space models (inference is particularly easy in linear Gaussian State Space Model because of the Kalman filter; as we shall study in the next few weeks). Specifically, for a linear Gaussian state space model, _X_ 0 is normal, the state evolution equation (5) takes the form


and the observation equation (6) takes the form


Here _Ft−_ 1 and _Ht_ are deterministic matrices, and _Qt_ and _Rt_ are covariance matrices. Note that for the linear Gaussian state space model, each of the densities _p_ 0( _x_ 0), _pt_ ( _xt | xt−_ 1) and _ft_ ( _yt | xt_ ) are normal with mean being a linear function of the underlying variable and the covariance being a deterministic matrix.

We shall look at a few additional examples of state space models today.

### **2.1 Local Level and Local Linear Models**

In the last class, we looked at the simple local level model:


This model has the two parameters _ση_<sup>2and</sup><sup>_σ_</sup> _ϵ_<sup>2(theparameters</sup><sup>_m_0andΓ0of</sup><sup>_X_0areusually</sup> set to be some standard values corresponding to a diffuse distribution such _m_ 0 = 0 and Γ0 = 10<sup>8</sup> ). We have seen simulation examples involving smooth trend estimation where this model does a decent job in recovering the underlying smooth trend function (it does not work however when the underlying trend function is nonsmooth). But often the trend estimate provided by this model is somewhat wiggly and we might want to obtain a smoother fit. This can be achieved by the local _linear_ model given by


The difference between the local level and the local linear models is that the random walk specification in the local linear model is in terms of the slopes _Xt − Xt−_ 1 as opposed to the levels as in the local level model. This generally leads to smoother fits.

8

Note that the local linear model is also a state space model even though _{Xt}_ as defined by _Xt − Xt−_ 1 = _Xt−_ 1 _− Xt−_ 2 + _ηt_ is not Markov. This is because we can rewrite the model in terms of the state variable _X_<sup>˜</sup> _t_ defined by


The equation _Xt − Xt−_ 1 = _Xt−_ 1 _− Xt−_ 2 + _ηt_ is easily seen to be equivalent to


which implies that _{X_<sup>˜</sup> _t}_ is a Markov process. The observation equation _Yt_ = _Xt_ + _ϵt_ can be written in terms of _X_<sup>˜</sup> _t_ as


This shows that the local linear model is also a state space model.

This re-writing of a second order Markov process _{Xt}_ in terms of the Markov process _X_<sup>˜</sup> _t_ is reminiscent of a similar argument in Ordinary Differential Equations. For example, the second order differential equation


can be re-written as the first order differential equation


### **2.2 Stochastic Volatility Models**

Consider the model


Data generated from this model exhibits volatility clustering i.e., the variance remains high or low for considerable periods of time. This model is useful for finance data (say for logreturns of stocks) which exhibit volatility clustering. This model is an alternative to volatility time series models such as ARCH or GARCH (which are somewhat less natural even though they are widely used). It is easy to check that this is also a state space model (it is not a linear Gaussian state space model however).

### **2.3 Dynamic Regression Model**

Consider the following model for a response variable _Yt_ and an explanatory variable _xt_ ( _xt_ will be treated as deterministic and non-random in the model below) which are both indexed by time _t_ = 0 _,_ 1 _, . . . , T_ . Dynamic regression models (also known as linear regression with time varying parameters) are of the form:


The difference with the usual simple linear regression model is that both the intercept and the slope coefficients above are allowed to depend on _t_ . In order to make estimation of this

9

model feasible, we need further restrictions on _{αt}_ and _{βt}_ (otherwise there are just too many parameters in the model). One simple restriction is to assume that:


Note that this is an example of a state space model with the state variable:


which satisfies


which implies that the state process is Markov. Further the observation equation can be written as


Dynamic regression models are used in many regression situations where the response and explanatory variables are collected in time. One example is when _yt_ gives the returns on a particular stock and _xt_ gives the average returns of the market. Then the dynamic regression model allows one to study the performance of the stock with respect to the average performance of the market over the course of time.

### **2.4 Recommended Reading for Today**

1. For a description of linear Gaussian state space models, see Section 2.4 of the PetrisPetrone-Campagnoli book and Section 3.1 of the Durbin-Koopman book.

2. Local Linear Model: Section 3.2.1 of the Durbin-Koopman book, Section 11.3 of the Kitagawa book.

3. Stochastic volatility models: page 49 of Petris-Petrone-Campagnoli, Section 2.4.3 of Chopin-Papaspiliopoulos, Section 1.3.3 of Triantafyllopoulos

4. Dynamic linear regression: Section 3.2.7 of Petris-Petrone-Campagnoli and Section 4.1.5 of Triantafyllopoulos.

---

[← 1 Lecture One](02-1-lecture-one.md) · [Up: contents](index.md) · [3 Lecture Three →](04-3-lecture-three.md)
