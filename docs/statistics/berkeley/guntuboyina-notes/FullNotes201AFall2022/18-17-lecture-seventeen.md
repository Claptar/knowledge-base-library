---
title: 17 Lecture Seventeen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 17 Lecture Seventeen

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall study the multivariate normal and multivariate _t_ -distributions today. Before going over them, let us first recall these densities in the univariate case.

### **17.1 Univariate normal and** _t_ **densities**

Let us start by looking at the standard normal distribution. We say that _Z_ is standard normal if its density is given by


The mean of _Z_ is zero and its variance equals 1.

87

From standard normal, we define general normal distributions via a scale and location change. Specifically, for two real numbers _µ_ and _a_ , define


The density of _X_ is given by (using the change of variable formula):


This density depends on the two quantities _µ_ and _a_<sup>2</sup> and is denoted by _N_ ( _µ, a_<sup>2</sup> ). Note that the quantity _a_ can be positive or negative but the density only depends on _|a|_ or _a_<sup>2</sup> . This density is called the Normal density with parameters _µ_ and _a_<sup>2</sup> . It is easy to check (using _X_ = _µ_ + _aZ_ ) that the mean of _X_ equals _µ_ and variance of _X_ equals _a_<sup>2</sup> .

Next we come to the _t_ -distribution. This is obtained by a further scale change involving an independent chi-squared distributed random variable. Specifically consider a random variable _V_ that has the _χ_<sup>2</sup> _k_<sup>distribution(</sup><sup>_χ_2</sup> _k_<sup>isthechi-squareddistributionwith</sup><sup>_k_degrees</sup> of freedom; recall that _χ_<sup>2</sup> _k_<sup>=</sup><sup>_Gamma_(</sup><sup>_k/_2</sup><sup>_,_1</sup><sup>_/_2))andassumethat</sup><sup>_V_and</sup><sup>_Z_areindependent.</sup> Define


Thus _T_ is very similar to _X_ except for the additional scale change involving the random variable _V/k_ . This random variable has mean and variance given by:

and


Thus when _k_ is large, _V/k_ is a random variable with mean 1 and very small variance which implies that _V/k_ will be highly concentrated around 1. Thus the additional scale change involving _V/k_ will play very little role if _k_ is large. But if _k_ is not very large, then it will make the distribution of _T_ considerably different from that of _X_ . The density of _T_ can be explicitly calculated using the following argument.


Observe now that

so that


As a result


88

The change of variable


now leads to


The density of this random variable _T_ will be denoted by _tk_ ( _µ, a_<sup>2</sup> ). In other words, the density of _tk_ ( _µ, a_<sup>2</sup> ) is proportional to


This density has heavier tails compared to the normal density _N_ ( _µ, σ_<sup>2</sup> ). The mean of _tk_ ( _µ, a_<sup>2</sup> ) exists if and only if _k >_ 1 and equals _µ_ . Its variance exists if and only if _k >_ 2 and equals _k−k_ 2<sup>_a_2.</sup>

### **17.2 Random Vectors and Covariance Matrices**

In order to discuss the multivariate normal distribution, we shall the language of random vectors and covariance matrices which are defined next.

A finite number of random variables can be viewed together as a random vector. More precisely, a random vector is a vector whose entries are random variables. Let _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> be an _n ×_ 1 random vector. Its Expectation E _Y_ is defined as a vector whose _i_ th entry is the expectation of _Yi_ i.e., E _Y_ = (E _Y_ 1 _,_ E _Y_ 2 _, . . . ,_ E _Yn_ )<sup>_T_</sup> . The covariance matrix of _Y_ , denoted by _Cov_ ( _Y_ ), is an _n × n_ matrix whose ( _i, j_ )th entry is the covariance between _Yi_ and _Yj_ . Two important but easy facts about _Cov_ ( _Y_ ) are:

1. The diagonal entries of _Cov_ ( _Y_ ) are the variances of _Y_ 1 _, . . . , Yn_ . More specifically the ( _i, i_ )th entry of the matrix _Cov_ ( _Y_ ) equals _var_ ( _Yi_ ).

2. _Cov_ ( _Y_ ) is a symmetric matrix i.e., the ( _i, j_ )th entry of _Cov_ ( _Y_ ) equals the ( _j, i_ ) entry. This follows because _Cov_ ( _Yi, Yj_ ) = _Cov_ ( _Yj, Yi_ ).

One can also check:

1. E( _AY_ + _c_ ) = _A_ E( _Y_ )+ _c_ for every deterministic matrix _A_ and every deterministic vector _c_ .

2. _Cov_ ( _AY_ + _c_ ) = _ACov_ ( _Y_ ) _A_<sup>_T_</sup> for every deterministic matrix _A_ and every deterministic vector _c_ .

As a consequence of the second formula above, we get

_var_ ( _a_<sup>_T_</sup> _Y_ ) = _a_<sup>_T_</sup> _Cov_ ( _Y_ ) _a_ = � _aiajCov_ ( _Yi, Yj_ ) for every _n ×_ 1 vector _a. i,j_

### **17.3 Multivariate Normal and** _t_ **-densities**

We shall follow the same program as in the univariate case. We first define standard multivariate normal, then general multivariate normal followed by the multivariate _t_ .

89

We say that a _p ×_ 1 random vector _Z_ has the standard _p_ -variate normal distribution if its components _Z_ 1 _, . . . , Zp_ are independently distributed according to the standard normal i.i.d distribution i.e., _Z_ 1 _, . . . , Zp ∼ N_ (0 _,_ 1). The joint density of _Z_ 1 _, . . . , Zp_ is then


The mean vector of _Z_ is simply the zero vector and the covariance matrix of _Z_ is the _p × p_ identity matrix _Ip_ .

From the standard _p_ -variate normal, we obtain a general _p_ -variate normal distribution in the following way. Suppose _µ_ is a fixed _p_ -dimensional vector and suppose _A_ is a fixed _p × p_ **invertible** matrix. Define

_X_ = _µ_ + _AZ_

Here _AZ_ is the matrix-vector multiplication of the _p × p_ matrix _A_ with the _p ×_ 1 vector _Z_ . By the Jacobian formula, the joint density of the components _X_ 1 _, . . . , Xp_ of _X_ is given by


We now let

Σ := _AA_<sup>_T_</sup> _._

Because the determinant of a product of matrices equals the product of the determinants


which implies, in particular, that det(Σ) _>_ 0. Using this (and the fact that the determinant of the inverse of a matrix equals the inverse of the determinant), we can write


We can thus write


This density depends on the vector _µ_ as well as on the matrix Σ = _AA_<sup>_T_</sup> . It is therefore denoted by _Np_ ( _µ,_ Σ). It is easy to see (using _X_ = _µ_ + _AZ_ ) that _µ_ is the mean vector of _X_

90

and Σ is the covariance matrix of _X_ :


Let us now define the multivariate _t_ -density. This is obtained by changing the scale of the multivariate normal density via a chi-squared random variable. Specifically, let _V_ denote a _χ_<sup>2</sup> _k_<sup>randomvariablethatisindependentofa</sup><sup>_p_-variatestandardnormalvector</sup><sup>_Z_.Let</sup>


for a _p ×_ 1 vector _µ_ and an invertible _p × p_ matrix _A_ . Note that _T_ is given by


Note that the scale change on each component of _T_ is through the same scalar random variable _V_ .

The distribution of this random vector _T_ will be denoted by _tk,p_ ( _µ,_ Σ). Its density can be derived just as in the univariate case in the following way:


Observe that, when _V_ is fixed at _x_ , the random vector _T_ becomes


so that


where we used det( _x_<sup>_<u>v</u>_Σ) = (</sup><sup>_v/x_)</sup><sup>_p_det(Σ).Asaresult</sup>


91

The change of variable


leads to

Therefore the density corresponding to _tk,p_ ( _µ,_ Σ) distribution is proportional to


Note that, in the notation _tk,p_ ( _µ,_ Σ), _k_ denotes degrees of freedom, _p_ denotes dimension, _µ_ and Σ = _AA_<sup>_T_</sup> denote the mean vector and covariance matrix of the corresponding normal random vector _µ_ + _AZ_ .

As in the univariate case, when _k_ (degrees of freedom) is large, _tk,p_ ( _µ,_ Σ) is very close to _Np_ ( _µ,_ Σ).

As an application involving the multivariate normal and _t_ -densities, we shall look at Bayesian Linear Regression.

### **17.4 Bayesian Linear Regression**

Here one observes data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ). _xi_ denotes the explanatory variable value and _yi_ denotes the response variable value for the _i_<sup>_th_</sup> individual. In usual linear regression analysis, we assume the model


for _i_ = 1 _, . . . , n_ where


There are three parameters in this model _β_ 0 _, β_ 1 and _σ_<sup>2</sup> . How to fit this model to the observed data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) i.e., how do we estimate the parameters _β_ 0 _, β_ 1 _, σ_ and also characterize the uncertainty in the estimates.

As an alternative to the usual frequentist analysis, we shall apply probability theory to solve this problem. The first step is to select a prior for the unknown parameters _β_ 0 _, β_ 1 _, σ_ . A reasonable prior reflecting ignorance is


for a large number _C_ (the exact value of _C_ will not matter in the following calculations). Note that as _σ_ is always positive, we have made the uniform assumption on log _σ_ (by the change of variable formula, the density of _σ_ would be given by _fσ_ ( _x_ ) = _f_ log _σ_ (log _x_ ) _x_<sup><u>1</u>=</sup> _I{−C<_ 2 _Cx_ log _x<C}_ =<sup>_I{e−C_</sup> 2<sup>_<x<e_</sup> _Cx_<sup>_C_</sup><sup>_<u>}</u>_</sup> .

The joint posterior for all the unknown parameters _β_ 0 _, β_ 1 _, σ_ is then given by (below we write the term “data” for _Y_ 1 = _y_ 1 _, . . . , Yn_ = _yn_ ):


92

The two terms on the right hand side above are


and


We thus obtain


The above is the joint posterior over _β_ 0 _, β_ 1 _, σ_ . The posterior over only the main parameters _β_ 0 _, β_ 1 can be obtained by integrating the parameter _σ_ as follows:


When _C_ is large, the above integral can be evaluated from 0 to _∞_ which gives


The change of variable


allows us to write the integral as


93

The posterior density of ( _β_ 0 _, β_ 1) is thus


A key role in the above posterior is played by the least squares criterion:


The usual point estimates of _β_ 0 and _β_ 1 are simply the minimizers _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 of the least squares criterion _S_ ( _β_ 0 _, β_ 1).

We can rewrite the posterior (84) as


Note that we have been able to bring in the term ( _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1))<sup>_n/_2</sup> because it does not depend on _β_ 0 _, β_ 1 and is thus a constant.

Generally, the density (89) will be quite sharply concentrated around the least squares estimator ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1) especially when _n_ is large. This is because, when ( _β_ 0 _, β_ 1) is such that _S_ ( _β_ 0 _, β_ 1) is large compared to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1), the quantity


would be quite negligible because of the large power _n/_ 2. As a result, the posterior density _fβ_ 0 _,β_ 1 _|_ data( _β_ 0 _, β_ 1) will be concentrated around those values of ( _β_ 0 _, β_ 1) for which _S_ ( _β_ 0 _, β_ 1) is quite close to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). For a concrete example, suppose _n_ = 762 and ( _β_ 0 _, β_ 1) is such that _S_ ( _β_ 0 _, β_ 1) = (1 _._ 1) _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). Then


Such ( _β_ 0 _, β_ 1) will thus get negligible posterior probability. Even for ( _β_ 0 _, β_ 1) such that _S_ ( _β_ 0 _, β_ 1) = (1 _._ 01) _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1), we have


and so such ( _β_ 0 _, β_ 1) will also get fairly small posterior probability.

To sum up, when _n_ is large, the posterior probability will be concentrated around those ( _β_ 0 _, β_ 1) for which _S_ ( _β_ 0 _, β_ 1) is very close to _S_ ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). Generally, this would imply that ( _β_ 0 _, β_ 1) would itself have to be close to ( _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1). For this reason, the indicator term in (89) has no effect when _C_ is large. We can thus drop this indicator term and refer to the Bayesian posterior as simply


We shall show in the next class that the above posterior density is simply the multivariate _t_ -density.

94

---

[← 16 Lecture Sixteen](17-16-lecture-sixteen.md) · [Up: contents](index.md) · [18 Lecture Eighteen →](19-18-lecture-eighteen.md)
