---
title: 1 Bayesian Inference for Linear Regression
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFive153248Fall2026.pdf
source_file: sources/berkeley-stat153/fall-2026/LectureFive153248Fall2026.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Bayesian Inference for Linear Regression

**Source:** [`LectureFive153248Fall2026.pdf`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureFive153248Fall2026.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In multiple linear regression, we have one response variable _y_ and _m_ covariates _x_ 1 _, . . . , xm_ ( _m_ = 1 corresponds to simple linear regression). We observe data on _n_ instances or subjects for all these variables: ( _yi, xi_ 1 _, . . . , xim_ ) for _i_ = 1 _, . . . , n_ . The multiple linear regression model (with normal errors) is given by:


In Bayesian inference for (1), we work with the prior


for a very large positive _C_ . The joint posterior density of _β_ 0 _, . . . , βm, σ_ is then given by


where we use the notation


for the sum of squares.

The posterior over only the coefficient parameters _β_ 0 _, . . . , βm_ can be obtained by integrat-

1

ing (or marginalizing) the parameter _σ_ .


where _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ denote the least squares estimators of _β_ 0 _, . . . , βm_ (i.e., ( _β_<sup>ˆ</sup> 0 _, . . . , β_<sup>ˆ</sup> _m_ ) minimizes _S_ ( _β_ 0 _, . . . , βm_ ) over all values of _β_ 0 _, . . . , βm_ ).

Our posterior density for _β_ 0 _, . . . , βm_ is thus:


It turns out that this joint density is a multivariate _t_ -density. This is explained next.

### **1.1 Why is** (2) **a** _t_ **-density?**

If you go to the wikipedia page ( `https://en.wikipedia.org/wiki/Multivariate_t-distribution` ) for Multivariate _t_ -distribution, it gives the following formula for the density:


Their notation for this distribution is _tp_ ( _µ,_ Σ _, ν_ ) where:

1. _p_ denotes dimension of the vector _x_ (this is a _p_ -variate joint density)

2. _µ_ is a _p ×_ 1 vector called the location

3. Σ is a _p × p_ matrix called the scale matrix

4. _ν >_ 0 denotes the degrees of freedom.

Here is some more information about the _t_ -density (3):

1. **Connection to the Multivariate Normal Density** : The most important term in the formula (3) is ( _x − µ_ )<sup>_T_</sup> Σ<sup>_−_1</sup> ( _x − µ_ ). This exact term also appears in the multivariate

2

normal density. If _X ∼ N_ ( _µ,_ Σ), then the density of _X_ is given by:


This suggests that the _t_ -density is closely related to the multivariate normal density. Here is the connection. Suppose _X ∼ Np_ ( _µ,_ Σ) and _V ∼ χν_<sup>2(thisisthechi-squared</sup> distribution with _ν_ degrees of freedom) are independent. Then


Thus, in the notation _tp_ ( _µ,_ Σ _, ν_ ), _ν_ denotes degrees of freedom, _p_ denotes dimension, _µ_ and Σ denote the mean vector and covariance matrix of the corresponding normal random vector _X_ . For completeness, we include a proof of (4) in Section 1.4.

2. **Individual Components as well as Linear Combinations of Components of** _T_ **are also** _t_ **-distributed** : Suppose _T ∼ tp_ ( _µ,_ Σ _, ν_ ) and the components of _T_ are _T_ 1 _, . . . , Tp_ . Then each individual component _Tj_ is also _t_ -distributed. Also every linear combination _a_ 0 + _a_ 1 _T_ 1 + _a_ 2 _T_ 2 + _· · ·_ + _apTp_ is also _t_ -distributed. To see this, first write


where _a_ is the _p ×_ 1 vector with components _a_ 1 _, . . . , ap_ . Using the formula (4), we can write


Because _a_ 0 + _a_<sup>_T_</sup> _X ∼ N_ ( _a_ 0 + _a_<sup>_T_</sup> _µ, a_<sup>_T_</sup> Σ _a_ ), the same fact (4) applied to this case gives: _a_ 0 + _a_<sup>_T_</sup> _T ∼ t_ 1( _a_ 0 + _a_<sup>_T_</sup> _µ, a_<sup>_T_</sup> Σ _a, ν_ ) _._

In particular, this implies that for each _j_ = 1 _, . . . , p_ ,


where _µj_ is the _j_ th component of _µ_ and Σ( _j, j_ ) is the ( _j, j_ )th entry of Σ.

3. **When** _ν_ **is large,** _t_ **is very close to normal** : This can intuitively be seen by noting that when _ν_ is large, the term ( _x − µ_ )<sup>_T_</sup> Σ<sup>_−_1</sup> ( _x − µ_ ) _/ν_ is small so that


where we used the observation that 1 + _z ≈ e_<sup>_z_</sup> when _z_ is small. Thus the _t_ -density (3) for large _ν_ becomes approximately:


because<sup>_ν_</sup><sup><u>+</u></sup> _ν_<sup>_<u>p</u>_</sup> _≈_ 1 when _ν_ is large. This gets us the normal density:

In our regression case, the degrees of freedom is _n − m −_ 1 where _n_ is the number of observations, and _m_ is the number of covariates. Thus **if** _n − m −_ 1 **is large** , then the posterior distribution (which is actually _t_ ) is approximately normal:


It turns out that (2) is a special case of (3) for some _p, µ,_ Σ _, ν_ . To see this, we need to first rewrite (2) using matrix notation which we do in the next section.

3

### **1.2 Matrix Notation for Multiple Linear Regression**


This notation is used not just to write formulae for linear regression, but also in code. For example, the OLS function in `statsmodels` uses the syntax `sm.OLS(y, X).fit()` to fit the linear regression model, where _y_ ( _n ×_ 1 vector) and _X_ ( _n ×_ ( _m_ +1) matrix) are defined above.

With this notation, one can write the sum of squares _S_ ( _β_ 0 _, . . . , βm_ ) as:


There are two important facts about _S_ ( _β_ ):

1. **Fact 1** : the least squares estimator _β_<sup>ˆ</sup> is given by the formula:


The proof of (5) is as follows. The gradient of _S_ ( _β_ ) is given by


Because _β_<sup>ˆ</sup> minimizes _S_ ( _β_ ), the gradient should equal zero when _β_ = _β_<sup>ˆ</sup> , and this leads to


2. **Fact 2** : The following Pythagorean identity holds:


To prove (7), write


The cross product is zero (leading to (7)) because:


where we used (6).

4

Using (7), we can write the posterior density (2) as


The above formula is a special case of (3) with


or equivalently


We thus have

With the posterior density (9), one can do uncertainty quantification about the parameters _β_ 0 _, β_ 1 _, . . . , βm_ . One can generate multiple samples from _tm_ +1( _β,_<sup>ˆ</sup> ( _S_ ( _β_<sup>ˆ</sup> ) _/_ ( _n − m −_ 1))( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _, n − m −_ 1) and plot the resulting fitted values to visualize the uncertainty in the coefficients.

### **1.3 Uncertainty Intervals**

The quantity _S_ ( _β_<sup>ˆ</sup> ) _/_ ( _n − m −_ 1) is the **frequentist unbiased** estimator for _σ_<sup>2</sup> , so we denote it by _σ_ ˆ<sup>2</sup> :


_σ_ ˆ can also be justified as a Bayesian estimator of _σ_ (See Question 4 (e) of Homework One). The terminology **Residual Standard Error** is sometimes used for _σ_ ˆ.

With the notation for _σ_ ˆ, the posterior (10) becomes:


By one of the facts mentioned about the _t_ -distribution, the posterior of each individual _βj_ is also _t_ :


5

where ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> is the ( _j_ + 1)<sup>_th_</sup> diagonal entry of ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> (note that we are using the ( _j_ + 1)th diagonal entry of _X_<sup>_T_</sup> _X_ because _βj_ is the ( _j_ + 1)th component of _β_ ). Writing this density out, we have


which implies that


This can be used to obtain uncertainty intervals for _βj_ . If _tn−m−_ 1 _,α/_ 2 is the point beyond which the _t_ -distribution (with _n − m −_ 1 degrees of freedom) assigns probability _α/_ 2, then


which is same as:


is called the 100(1 _− α_ )% Bayesian Credible interval for _βj_ . It **exactly coincides** with the frequentist 100(1 _− α_ )% confidence interval for _βj_ .

When _n−m−_ 1 is large, the _t_ -density (10) is approximately equal to the _Nm_ +1( _β,_<sup>ˆ</sup> ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> ). Further, when _n − m −_ 1 is large, the distribution <u>(11)</u> will be close to the normal distribution _N_ ( _β_<sup>ˆ</sup> _j,_ ˆ _σ_<sup>2</sup> ( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> ). The quantity _σ_ ˆ�( _X_<sup>_T_</sup> _X_ )<sup>_j_+1</sup><sup>_,j_+1</sup> is known as the standard error corresponding to _βj_ .

### **1.4 Proof of** (4)

_Proof of_ (4) _._ Start with the formula:


Observe that


so that


6

where we used det( _x_<sup>_<u>ν</u>_Σ) = (</sup><sup>_ν/x_)</sup><sup>_p_det(Σ).Asaresult</sup>


The change of variable

leads to

which proves (4).

---

[Up: contents](index.md) · [2 Nonlinear Regression →](02-2-nonlinear-regression.md)
