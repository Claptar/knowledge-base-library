---
title: 18 Lecture Eighteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 18 Lecture Eighteen

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **18.1 Recap: Multivariate Normal and** _t_ **Distributions**

In the last class, we looked at the multivariate normal distribution _Np_ ( _µ,_ Σ) ( _p_ denotes dimension, _µ_ denotes mean vector and Σ denotes covariance matrix) with density:


and the multivariate _t_ -distribution _tk,p_ ( _µ,_ Σ) ( _k_ is the degrees of freedom) with density proportional to


One can generate random vectors having these distributions in the following way. First consider a _p ×_ 1 random vector _Z_ whose components _Z_ 1 _, . . . , Zp_ are i.i.d standard normal. Then


has the _Np_ ( _µ,_ Σ) distribution with Σ = _AA_<sup>_T_</sup> . Also


has the _tk,p_ ( _µ,_ Σ) distribution. Here _V_ has the _χ_<sup>2</sup> _k_<sup>distributionandweassumethat</sup><sup>_V_and</sup><sup>_Z_</sup> are independent.

The following fact will be useful in the sequel.


_where µi is the i_<sup>_th_</sup> _component of µ and_ Σ( _i, i_ ) _is the_ ( _i, i_ )<sup>_th_</sup> _entry of_ Σ _. In words, each Ti has the univariate t-distribution._

_Proof._ This fact follows directly from (88) because


Now<sup>�</sup><sup>_p_</sup> _j_ =1<sup>_A_(</sup><sup>_i, j_)</sup><sup>_Zj_hasthenormaldistributionwithmeanzeroandvariance</sup>


Therefore we can write


Thus


This has the same form as (88) except instead of _AZ_ <u>,</u> we have the univariate product ~~�~~ Σ( _i, i_ ) _W_ where _W ∼ N_ (0 _,_ 1). Thus _Ti ∼ tk_ ( _µi,_ ~~�~~ Σ( _i, i_ )).

95

### **18.2 Application to Linear Regression**

We considered the usual linear regression model in the last class. One observes data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ). _xi_ denotes the explanatory variable value and _yi_ denotes the response variable value for the _i_<sup>_th_</sup> individual. We consider the model


There are three parameters in this model _β_ 0 _, β_ 1 and _σ_<sup>2</sup> . The goal is to estimate the parameters _β_ 0 _, β_ 1 and also characterize the uncertainty in the estimates.

We worked with the prior distribution


for a large number _C_ and calculated the posterior density of _β_ 0 _, β_ 1 (by integrating the full posterior of _β_ 0 _, β_ 1 _, σ_ over _σ_ ) to be


We show below that this density is very closely related to the multivariate _t_ -density (87) . To see this, let us use the notation


The usual point estimates of _β_ 0 and _β_ 1 are simply the minimizers _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 of the least squares criterion _S_ ( _β_ 0 _, β_ 1).

We can then rewrite the above posterior as


Note that we have been able to bring in the term ( _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1))<sup>_n/_2</sup> because it does not depend on _β_ 0 _, β_ 1 and is thus a constant.

Using the notation


we can write


96

We now use the following Pythagorean decomposition

_S_ ( _β_ ) = _∥Y − Xβ∥_<sup>2</sup> = _∥Y − Xβ_<sup>ˆ</sup> _∥_<sup>2</sup> + _∥Xβ − Xβ_<sup>ˆ</sup> _∥_<sup>2</sup> = _S_ ( _β_<sup>ˆ</sup> ) + ( _β − β_<sup>ˆ</sup> )<sup>_T_</sup> _X_<sup>_T_</sup> _X_ ( _β − β_<sup>ˆ</sup> ) _._

We can thus write


If we ignore the indicator above, the above density is simply the multivariate _t_ -density with dimension _p_ = 2, degrees of freedom _k_ = _n −_ 2, mean parameter _β_<sup>ˆ</sup> and covariance matrix parameter Σ where


Therefore the posterior density is just the _tn−_ 2 _,_ 2( _β,_<sup>ˆ</sup> Σ) density truncated to the set _−C < β_ 0 _, β_ 1 _< C_ . When _C_ is large, this truncation will have little practical effect so we can just treat the posterior density as _tn−_ 2 _,_ 2( _β,_<sup>ˆ</sup> Σ).

Let us now use some standard regression terminology:


We have thus proved that


With this posterior density, one can do uncertainty quantification about the parameters _β_ 0 and _β_ 1. One can generate multiple samples from _tn−_ 2 _,_ 2( _β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ) and plot the resulting lines to visualize the uncertainty in _β_ 0 and _β_ 1. One can also use Fact 18.1 to deduce that


where ( _X_<sup>_T_</sup> _X_ )<sup>11</sup> and ( _X_<sup>_T_</sup> _X_ )<sup>22</sup> are the first and second diagonal entries of ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> respectively. These univariate _t_ -densities describe the marginal uncertainty in the intercept and slope parameters. When _n_ is large, these will be close to the normal distributions _N_ ( _<u>β</u>_<sup>ˆ</sup> <u>0</u> _<u>,</u>_ ˆ _σ_<sup>2</sup> <u>(</u> _X_<sup>_T_</sup> _X_ )<sup>11</sup> ) and _N_ ( _β_<sup>ˆ</sup> 1 _,_ ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>22</sup> ) respectively. The quantities _σ_ ˆ�( _X_<sup>_T_</sup> _X_ )<sup>11</sup> and _σ_ ˆ ~~�~~ ( _X_<sup>_T_</sup> _X_ )<sup>22</sup> are known as the standard errors of the intercept and the slope respectively.

97

### **18.3 Multiple Linear Regression**

The analysis for multiple linear regression is very similar to analysis of the last section. Here one observes data ( _yi, xi_ 1 _, xi_ 2 _, . . . , xim_ ) for _i_ = 1 _, . . . , n_ . There are _m_ explanatory variables _x_ 1 _, . . . , xm_ and one response variable. _xij_ denotes the value of the _j_<sup>_th_</sup> explanatory variable for the _i_<sup>_th_</sup> individual and _yi_ is the value of the response variable for the _i_<sup>_th_</sup> individual. The model is


for _i_ = 1 _, . . . , n_ where


The goal is to estimate the parameters _β_ 0 _, . . . , βm_ as well as _σ_ from the data. _σ_ is usually treated as a nuisance parameter and the main parameters of interest are _β_ 0 _, . . . , βm_ . The model studied in the previous section is often called simple linear regression and it corresponds to _m_ = 1 (i.e., there is only one explanatory variable).

We shall work with the prior distribution:


Under this assumption, it can be easily seen that the posterior for _β_ 0 _, . . . , βm_ is given (just like in the last section) as


where


is the least squares criterion, and _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ are the least squares estimators (these are the minimizers of _S_ ( _β_ 0 _, . . . , βm_ )). Using the matrix notation:


it can be seen that


and


We can then show (using the same Pythagorean decomposition as in the last section) that


98

If we ignore the indicator above, the above density is simply the multivariate _t_ -density with dimension _p_ = _m_ +1, degrees of freedom _k_ = _n−p_ , mean parameter _β_<sup>ˆ</sup> and covariance matrix parameter Σ where


Therefore the posterior density is just the _tn−p,p_ ( _β,_<sup>ˆ</sup> Σ) density truncated to the set _−C < β_ 0 _, β_ 1 _, . . . , βm < C_ . When _C_ is large, this truncation will have little practical effect so we can just treat the posterior density as _tn−p,p_ ( _β,_<sup>ˆ</sup> Σ). We can then use the Fact 18.1 to obtain marginal _t_ -distributions for each individual component _βj, j_ = 0 _,_ 1 _, . . . , m_ .

Multiple Linear Regression can be used to fit even when there is only one explanatory variable to fit certain nonlinear functions of the explanatory variable. For example, one can fit quadratic functions via the model:


i.i.d with _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ) by the multiple linear regression methodology with


 _β_ 0 The posterior density of _β_ = _β_ 1  _β_ 2 will then be given by _tn−_ 3 _,_ 3(ˆ _β,_ ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ) (note that the dimension now is 3 and the degrees of freedom is _n −_ 3).

A more general polynomial trend model (of degree _k_ ) can be fit analogously (the dimension of _β_ will then be _k_ +1 and the degrees of freedom of the posterior _t_ -density will be _n − k −_ 1).

Other examples include the following. To capture seasonal trend in time series data (here the explanatory variable is time with values _t_ 1 _, . . . , tn_ ) with known period _s_ (for example _s_ = 12 in monthly data), one can use a model of the form


This is also a linear regression model with


and the _i_<sup>_th_</sup> row of the _n ×_ (2 _r_ + 1) matrix _X_ is given by


Here the posterior _t_ -density of _β_ will have dimension 2 _r_ +1 and degrees of freedom _n−_ (2 _r_ +1).

Time series datasets often have both trend and seasonality. These effects can be estimated by models of the form:


99

Inference for this model can also be done through linear regression. The degrees of freedom for the posterior _t_ -density of the coefficients will now be _n −_ (2 _r_ + _k_ + 1). Our methodology will work as long as _n >_ 2 _r_ + _k_ + 1.

### **18.4 Models with Nonlinear Parameter Dependence**

The Bayesian methodology can be used even to fit models with nonlinear parameter dependence such as:

_Yi_ = _β_ 0 + _β_ 1 cos(2 _πfxi_ ) + _β_ 2 sin(2 _πfxi_ ) + _ϵi_ (91)

i.i.d with _ϵi ∼ N_ (0 _, σ_<sup>2</sup> ). The setting here is the usual simple linear regression setting (there is only one explanatory variable). The parameters are _β_ 0 _, β_ 1 _, β_ 2 _, σ_ as well as the frequency parameter _f_ . One cannot use linear regression methodology directly here because the parameter _f_ appears nonlinearly in the equation (91). We shall see how to handle this in the next class.

---

[← 17 Lecture Seventeen](18-17-lecture-seventeen.md) · [Up: contents](index.md) · [19 Lecture Nineteen →](20-19-lecture-nineteen.md)
