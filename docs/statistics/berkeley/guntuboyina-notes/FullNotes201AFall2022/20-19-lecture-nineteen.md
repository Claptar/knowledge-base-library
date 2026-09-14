---
title: 19 Lecture Nineteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 19 Lecture Nineteen

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **19.1 Last Class: Linear Regression**

Last class, we used probability to perform inference in the usual linear regression model. Here one observes data ( _yi, xi_ 1 _, xi_ 2 _, . . . , xim_ ) for _i_ = 1 _, . . . , n_ . There are _m_ explanatory variables _x_ 1 _, . . . , xm_ and one response variable. _xij_ denotes the value of the _j_<sup>_th_</sup> explanatory variable for the _i_<sup>_th_</sup> individual and _yi_ is the value of the response variable for the _i_<sup>_th_</sup> individual. The model is


The goal is to estimate the parameters _β_ 0 _, . . . , βm_ as well as _σ_ from the data. _σ_ is usually treated as a nuisance parameter and the main parameters of interest are _β_ 0 _, . . . , βm_ .

We used the prior distribution:


Under this assumption, we derived the posterior distribution for _β_ 0 _, . . . , βm_ to be


where


is the least squares criterion, and _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ are the least squares estimators (these are the minimizers of _S_ ( _β_ 0 _, . . . , βm_ )).

We also saw that the posterior density can also be written as


100

using the notation:


If we ignore the indicator function, the above density is simply the multivariate _t_ -density with dimension _p_ = _m_ + 1, degrees of freedom _k_ = _n − p_ , mean parameter _β_<sup>ˆ</sup> and covariance matrix parameter Σ where


Therefore the posterior density is just the _tn−p,p_ ( _β,_<sup>ˆ</sup> Σ) density truncated to the set _−C < β_ 0 _, β_ 1 _, . . . , βm < C_ . When _C_ is large, this truncation will have little practical effect so we can just treat the posterior density as _tn−p,p_ ( _β,_<sup>ˆ</sup> Σ). Point estimates for _β_ will just be the least squares estimator _β_<sup>ˆ</sup> , and uncertainty is usually summarized by the standard errors which are simply the square roots of the diagonal entries of Σ. In other words, the standard error corresponding to _β_<sup>ˆ</sup> _j_ equals ~~�~~ _Sn_ <u>(</u> _−β_<sup>ˆ</sup> _p_ <u>)</u><sup>multipliedbythesquare-rootofthecorresponding</sup> diagonal entry of ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> .

### **19.2 Nonlinear Regression Models**

In this framework, parameter inference in nonlinear regression models is handled in a very similar way. For a concrete example, consider the model:


i.i.d for _i_ = 1 _, . . . , n_ where, as in the previous section, _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ). This is a nonlinear regression model because the parameter _β_ 2 enters via the exponential function which is nonlinear. There are four unknown parameters _β_ 0 _, β_ 1 _, β_ 2 _, σ_ . We can obtain parameter estimates and standard errors for them in a manner that is very similar to the analysis in linear regression. We work with the prior:


for a large _C >_ 0. The posterior density of the parameters is then given by: The joint posterior for all the unknown parameters _β_ 0 _, β_ 1 _, β_ 2 _, σ_ is then given by (below we write the term “data” for _Y_ 1 = _y_ 1 _, . . . , Yn_ = _yn_ ):


101

The two terms on the right hand side above are the likelihood:


and


We thus obtain


Using the notation


for the sum of squares criterion, we can write the posterior as We thus obtain


Often our interest is only in the parameters _β_ 0 _, β_ 1 _, β_ 2 ( _σ_ is a nuisance parameter). To obtain the posterior of _β_ 0 _, β_ 1 _, β_ 2, we integrate the full posterior above with respect to _σ_ . Assuming that _C_ is large, we can do the integral from 0 to _∞_ and this leads to (the calculation is the same as in the linear regression case)


This posterior density will take its largest value when ( _β_ 0 _, β_ 1 _, β_ 2) minimizer the sum of squares _S_ ( _β_ 0 _, β_ 1 _, β_ 2). In other words, the maximu posterior density will be achieved by the least squares estimator:


Unlike in the linear regression case where we can write the least squares estimator in closed form as ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _Y_ , we may not be able to write the least squares estimator in this nonlinear regression model in closed form. Nevertheless, generally there exists a unique least

102

squares estimator. The posterior distribution will assign nonnegligible probability only to those parameter values _β_ 0 _, β_ 1 _, β_ 2 for which _S_ ( _β_ 0 _, β_ 1 _, β_ 2) is close to the smallest possible value _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, β_<sup>ˆ</sup> 2). This can be seen, for example, by rewriting the posterior density as


For this reason, we can neglect the indicator function above (because the action will be very close to the least squares estimator _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, β_<sup>ˆ</sup> 2) and write


Unlike in the linear regression case, the right hand side above is not the (unnormalized) density of a multivariate _t_ -distribution. However, we can approximate it by a multivariate _t_ - distribution by a second Taylor expansion of _S_ ( _β_ 0 _, β_ 1 _, β_ 2) around the least squares estimator _β_ ˆ0 _, β_ ˆ1 _, β_ ˆ2. This Taylor expansion is justified because the posterior density will usually be quite concentrated around _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, β_<sup>ˆ</sup> 2. Writing _β_ for the vector ( _β_ 0 _, β_ 1 _, β_ 2) and _β_<sup>ˆ</sup> for the vector ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, β_<sup>ˆ</sup> 2), Taylor expansion is


where _∇S_ ( _β_<sup>ˆ</sup> ) and _HS_ ( _β_<sup>ˆ</sup> ) are the gradient and Hessian of _S_ at _β_<sup>ˆ</sup> . Because _β_<sup>ˆ</sup> minimizes _S_ ( _β_ ), we have _∇S_ ( _β_<sup>ˆ</sup> ) = 0 and so


Thus the posterior density is approximated by


Writing _p_ = 3 for the dimension of the vector _β_ , we get


This is clearly a multivariate _t_ -density. More specifically,


One can summarize this posterior distribution by simply reporting the point estimates _β_ ˆ0 _, β_ ˆ1 _, β_ ˆ2 and their standard errors which are the square roots of the diagonal entries of


103

The earlier linear regression analysis is a special case of this analysis because we recover the earlier result by taking _S_ ( _β_ ) = _∥Y − Xβ∥_<sup>2</sup> (in this case _HS_ ( _β_ ) = 2 _X_<sup>_T_</sup> _Xβ_ ).

It should be noted that the result (92) is an approximation (in other words, the exact posterior is not _t_ -distributed) obtained by the second order Taylor expansion of _S_ ( _β_ ) around _β_ ˆ. An exact analysis of the posterior can be done in the following way. In this specific problem, there are three _β_ parameters; _β_ 0 _, β_ 1 _, β_ 2. The model is linear in _β_ 0 _, β_ 1 for every fixed _β_ 2. This means that the conditional posterior of _β_ 0 _, β_ 1 for fixed _β_ 2 is exactly _t_ -distributed. So the marginal posterior density of _β_ 2 can be calculated exactly. We shall do this analysis in more generality in the next section.

### **19.3 More on Nonlinear Regression Models**

Consider the nonliear regression model written in vector-matrix notation as:


where _Y_ is _n ×_ 1, _ω_ is a _k ×_ 1 vector of unknown parameters, _X_ ( _ω_ ) is an _n × p_ matrix that depends in a known way on the unknown parameters in _ω_ , _β_ is a _p ×_ 1 vector of unknown parameters and _ϵ_ is a _n ×_ 1 vector consisting of i.i.d _N_ (0 _, σ_<sup>2</sup> ) errors. This model has _k_ + _p_ +1 parameters: _k_ elements of _ω_ , _p_ elements of _β_ and _σ_ . The model depends linearly on the _β_ parameters but possibly nonlinearly on the _ω_ parameters. This setting includes the following special cases.

1. In the concrete example considered in the previous section, we can take _ω_ = ( _β_ 2) and _β_ = ( _β_ 0 _, β_ 1). The matrix _X_ ( _ω_ ) is given by


2. Consider the model


This is a nonlinear regression model where we are modeling the response as a sinusoidal function of the explanatory variable where the sinusoid has an unknown frequency _f_ . This is a special case of (95) with _ω_ = _f_ , _β_ is the vector with components _β_ 0 _, β_ 1 _, β_ 2 and the _X_ ( _ω_ ) matrix is


3. Consider the model


104

This is a changepoint in mean model where the response variable has mean _β_ 0 when _x_ is atmost _ω_ and mean _β_ 0 + _β_ 1 when _x_ exceeds _ω_ . This is also a special case of (95) with


#### 4. Consider the model


This is a broken stick regression model where the regression line has slope _β_ 1 when the covariate is at most _ω_ and has slope _β_ 1 + _β_ 2 when the covariate exceeds _ω_ . Here ( _x − ω_ )+ = max( _x − ω,_ 0). This is also a special case of (95) with


The likelihood of the model (95) is


To perform Bayesian analysis in the model (95), we assume as before that all the components of _ω_ , all the components of _β_ and log _σ_ are all i.i.d uniformly distributed on ( _−C, C_ ) for a large _C_ . The posterior density is then given by


where we have ignored the indicator functions (assuming _C_ is large). Often the main interest is in the _ω_ parameters. So we integrate the posterior with respect to _β_ and _σ_ . This gives


Now if _β_<sup>ˆ</sup> ( _ω_ ) is the least squares estimator for fixed _ω_ :


then using


105

the integral (96) then becomes


We shall now use the formula:

where Σ is a _p × p_ positive definite matrix and the integral is over _x_ = ( _x_ 1 _, . . . , xp_ ). This is basically the formula for the normalizing constant for the multivariate normal distribution.

This formula with Σ<sup>_−_1</sup> = _X_ ( _ω_ )<sup>_′_</sup> _X_ ( _ω_ ) _/_ ( _σ_<sup>2</sup> ) (or equivalently Σ = _σ_<sup>2</sup> ( _X_ ( _ω_ )<sup>_′_</sup> _X_ ( _ω_ ))<sup>_−_1</sup> ) gives


The required integral is


The change of variable


then gives


Putting everything together, we have proved that


This function of _ω_ can be numerically understood when the dimension of _ω_ is low. For example, if _ω_ is one-dimensional, we can plot the posterior density on the computer and normalize it so the density integrates to one.

---

[← 18 Lecture Eighteen](19-18-lecture-eighteen.md) · [Up: contents](index.md) · [20 Lecture Twenty →](21-20-lecture-twenty.md)
