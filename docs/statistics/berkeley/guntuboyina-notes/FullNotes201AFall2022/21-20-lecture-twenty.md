---
title: 20 Lecture Twenty
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 20 Lecture Twenty

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **20.1 Last Class: Nonlinear Regression Models with both linear and nonlinear parameter dependence**

Consider the nonliear regression model written in vector-matrix notation as:


106

where _Y_ is _n ×_ 1, _ω_ is a _k ×_ 1 vector of unknown parameters, _X_ ( _ω_ ) is an _n × p_ matrix that depends in a known way on the unknown parameters in _ω_ , _β_ is a _p ×_ 1 vector of unknown parameters and _ϵ_ is a _n ×_ 1 vector consisting of i.i.d _N_ (0 _, σ_<sup>2</sup> ) errors. This model has _k_ + _p_ +1 parameters: _k_ elements of _ω_ , _p_ elements of _β_ and _σ_ . The model depends linearly on the _β_ parameters but possibly nonlinearly on the _ω_ parameters. This setting includes the following special cases.

1. In the concrete example considered in the previous section, we can take _ω_ = ( _β_ 2) and _β_ = ( _β_ 0 _, β_ 1). The matrix _X_ ( _ω_ ) is given by


2. Consider the model


This is a nonlinear regression model where we are modeling the response as a sinusoidal function of the explanatory variable where the sinusoid has an unknown frequency _f_ . This is a special case of (95) with _ω_ = _f_ , _β_ is the vector with components _β_ 0 _, β_ 1 _, β_ 2 and the _X_ ( _ω_ ) matrix is


3. Consider the model


This is a changepoint in mean model where the response variable has mean _β_ 0 when _x_ is atmost _ω_ and mean _β_ 0 + _β_ 1 when _x_ exceeds _ω_ . This is also a special case of (95) with


#### 4. Consider the model


This is a broken stick regression model where the regression line has slope _β_ 1 when the covariate is at most _ω_ and has slope _β_ 1 + _β_ 2 when the covariate exceeds _ω_ . Here

107

( _x − ω_ )+ = max( _x − ω,_ 0). This is also a special case of (95) with


The likelihood of the model (95) is


To perform Bayesian analysis in the model (95), we assume as before that all the components of _ω_ , all the components of _β_ and log _σ_ are all i.i.d uniformly distributed on ( _−C, C_ ) for a large _C_ . The posterior density is then given by


where we have ignored the indicator functions (assuming _C_ is large). Often the main interest is in the _ω_ parameters. So we integrate the posterior with respect to _β_ and _σ_ . This gives


Now if _β_<sup>ˆ</sup> ( _ω_ ) is the least squares estimator for fixed _ω_ :


then using


the integral (96) then becomes


We shall now use the formula:


where Σ is a _p × p_ positive definite matrix and the integral is over _x_ = ( _x_ 1 _, . . . , xp_ ). This is basically the formula for the normalizing constant for the multivariate normal distribution.

This formula with Σ<sup>_−_1</sup> = _X_ ( _ω_ )<sup>_′_</sup> _X_ ( _ω_ ) _/_ ( _σ_<sup>2</sup> ) (or equivalently Σ = _σ_<sup>2</sup> ( _X_ ( _ω_ )<sup>_′_</sup> _X_ ( _ω_ ))<sup>_−_1</sup> ) gives


108

The required integral is


The change of variable


then gives


Putting everything together, we have proved that


This function of _ω_ can be numerically analyzed when the dimension of _ω_ is low. For example, if _ω_ is one-dimensional, we can plot the posterior density on the computer and normalize it so the density integrates to one.

### **20.2 Logistic Regression**

Here is another regression model which can be handled in a straightforward fashion by probability theory. We are again in the usual regression setting where we observe data ( _yi, xi_ 1 _, xi_ 2 _, . . . , xim_ ) for _i_ = 1 _, . . . , n_ . There are _m_ explanatory variables _x_ 1 _, . . . , xm_ and one response variable. _xij_ denotes the value of the _j_<sup>_th_</sup> explanatory variable for the _i_<sup>_th_</sup> individual and _yi_ is the value of the response variable for the _i_<sup>_th_</sup> individual. Suppose now that the response variable is binary i.e., _y_ 1 _, . . . , yn_ take values in _{_ 0 _,_ 1 _}_ . In this case, the logistic regression model assumes that:


Letting _xi_ = (1 _, xi_ 1 _, . . . , xim_ )<sup>_T_</sup> and _β_ = ( _β_ 0 _, β_ 1 _, . . . , βm_ )<sup>_T_</sup> , we can write the model also as


Observe that _x_<sup>_T_</sup> 1<sup>_, . . . , x_</sup> _n_<sup>_T_form the rows of the</sup><sup>_n×p_design matrix</sup><sup>_X_(where</sup><sup>_p_=</sup><sup>_m_+1).The</sup> unknown parameters in the logistic regression model are _β_ 0 _, . . . , βm_ (note that, in contrast to the linear regression model, there is no _σ_ parameter in logistic regression). In order to use probability theory for inference on _β_ 0 _, . . . , βm_ , we assume the prior:


109

for a large _C_ . The posterior of _β_ is then


where


Note that _ℓ_ ( _β_ ) is simply the log-likelihood in this problem. The posterior density is not in standard form. If _p_ = 1 or _p_ = 2, then this can be plotted. One can use various MCMC techniques to obtain samples from this posterior. A closed form multivariate normal approximation that works quite well in practice will be described in the next class. Bayesian inference from this normal approximation to the posterior coincides with usual frequentist inference for logistic regression.

---

[← 19 Lecture Nineteen](20-19-lecture-nineteen.md) · [Up: contents](index.md) · [21 Lecture Twenty One →](22-21-lecture-twenty-one.md)
