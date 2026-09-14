---
title: 22 Lecture Twenty Two
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 22 Lecture Twenty Two

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **22.1 Linear Regression Recap**

So far we have studied the linear regression model:


under the prior that the components of _β_ are i.i.d Unif( _−C, C_ ) for a large _C_ . We have seen (Problem 1(a) in Homework Five) that


113

where _p_ is the dimension of _β_ . This is the posterior distribution of _β_ conditional on _σ_ . This cannot be used for inference on _β_ because _σ_ is unknown. The posterior of _β_ (without any conditioning on _σ_ ) is given by (under the prior log _σ ∼_ Unif( _−C, C_ ))


where _σ_ ˆ is the residual standard error. When _n − p_ is large, the _t_ -distribution will be quite close to normal, so we can write


Inference on _β_ is done either using (106) or (107).

### **22.2 Linear Regression with Gaussian prior**

It is common to consider other priors for linear regression. A general class of priors is given by


for a mean vector _m_ 0 and covariance matrix _Q_ 0. In this case, it can be shown (left as exercise) that the posterior distribution of _β_ conditional on _σ_ is given by


where


(109) is the analogue of (105) for the Gaussian prior (108). Actually, the result (105) can be seen as a special case of (109) when the prior covariance _Q_ 0 becomes large (think of the setting where the smallest eigenvalue of _Q_ 0 goes to _∞_ ). Because when _Q_ 0 approaches infinity, it is easy to see that

and also


As one concrete example of _Q_ 0 being large, think of _Q_ 0 = _CIp_ when _C_ is large. The posterior for this prior is the same as (105) (i.e., there is no difference between the Unif( _−C, C_ ) and _Np_ (0 _, CIp_ ) priors) . The Gaussian prior result (109) can thus be seen as a generalization of (105).

In many applications, it makes sense to work with the prior (108) as opposed to the _Unif_ ( _−C, C_ ) prior. We shall illustrate in a real data setting in the next section.

114

### **22.3 Linear Regression on an Earnings Dataset**

Consider the dataset `ex1029` from the R package `Sleuth3` (this package is written by Ramsey and Schafer to accompany their introductory statistics book _Statistical Sleuth_ ). This dataset contains weekly wages in 1987 for a sample of _n_ = 25682 males between the ages of 18 and 70 who worked full-time along some covariates including theiry years of experience. We shall work with the two variables:

_y_ = response variable = log(weekly earnings)

and


We shall fit linear regression models of _y_ on _x_ . The reason for working with log(earnings) as opposed to earnings directly is for better interpretation.

The most basic model between _y_ and _x_ is the usual linear model:


From a visual examination of the scatterplot between _y_ and _x_ , it can be easily seen that this simple linear regression model is not adequate as the relationship between _y_ and _x_ is clearly nonlinear ( _y_ increases with _x_ for small values of _x_ and decreses with _x_ for large values of _x_ ). A more suitable model is


where _s_ is also an unknown parameter. This model fits two lines which are connected at the point _s_ . The rate of change of _y_ with _x_ is _β_ 1 for _x ≤ s_ and _β_ 1 + _β_ 2 for _x > s_ . We have previously seen how to fit models of the form (110) to data.

For this specific dataset, the model (110) is not suitable either because there is no reason to just have one change of slope for the regression function. A more suitable model would be

_y_ = _β_ 0 + _β_ 1 _x_ + _β_ 2( _x − s_ 1)+ + _β_ 3( _x − s_ 2)+ + _· · ·_ + _βk_ +1( _x − sk_ )+ + _ϵ_

for a _k_ that is not too small. There are two problems with working with this model:

1. It is difficult to fit it to the data unless _k_ is very small. The methodology that we studied in Lecture 20 involved marginalizing the _β_ ’s and _σ_ to get a posterior only for _s_ 1 _, . . . , sk_ . This is a _k_ -dimensional posterior and a grid-based method for selecting the posterior mode or mean would be quite computationally challenging if _k_ is not small.

2. It is difficult to select a suitable value of _k_ .

One way to circumvent these problems is to introduce a change of slope term ( _x − s_ )+ at every possible value of _s_ . In this dataset, the variable _x_ takes the values 0 _,_ 1 _, . . . ,_ 63. So we consider the model:


This is the model that we shall work with. It is a linear regression model with 65 coefficients. The intercept _β_ 0 is interpreted as the log(earnings) for someone who is starting their career ( _x_ = 0). Also, for _j_ = 1 _, . . . ,_ 63, the term 100 _βj_ is interpreted as the percent change in earnings when someone moves from ( _j −_ 1) years of experience to _j_ years in experience. [ **This interpretation is actually incorrect; see the notes for the next lecture (Lecture 23) for the correct interpretation** ]

115

How to fit the model (111) to the observed data. The first approach is to work with the uniform prior _βj ∼_ Unif( _−C, C_ ) for _j_ = 0 _,_ 1 _, . . . ,_ 63. This is equivalent to just doing the usual linear regression (using the R function `lm` for instance). This gives the least squares estimates _β_<sup>ˆ</sup> 0<sup>_ls, . . . ,β_ˆ</sup> 63<sup>_ls_andthefunctionthatweuseforexplainingtherelationshipbetween</sup> earnings and experience is _y_ = _f_<sup>ˆ</sup><sup>_ls_</sup> ( _x_ ) where


In this particular dataset, this function turns out to be somewhat wiggly and not smooth, which is not very interpretable. The situation is more pronounced when the number of observations _n_ not large. One can reduce the size of this dataset to, say, _n_ = 500 by sampling 500 observations (rows) at random from this dataset. One can then refit the least squares estimate of _y_ on _x,_ ( _x −_ 1)+ _, . . . ,_ ( _x −_ 63)+ to this smaller dataset. Here the fitted function (112) will be much more wiggly.

In order to obtain a smooth function fit to the data, one can use the prior


for a small _τ_ . Here, if we take _τ_ to be small, we are insisting on _β_ 1 _, . . . , β_ 64 to be small which will lead to a smoother fit. The assumption _β_ 0 _∼ N_ (0 _, C_ ) on _β_ 0 is very similar to _β_ 0 _∼_ Unif( _−C, C_ ) and it just says that we do not enforce anything on _β_ 0 a priori. We can write this prior as


where _β_ is the 65 _×_ 1 vector with components _β_ 0 _, β_ 1 _, . . . , β_ 64, _m_ 0 is the 65 _×_ 1 vector of zeros, and _Q_ 0 is the 65 _×_ 65 diagonal matrix with diagonal entries _C, τ_<sup>2</sup> _, τ_<sup>2</sup> _, . . . , τ_<sup>2</sup> . The posterior distribution of _β_ can then be calculated using (109) as:


This posterior can be used for inference on _β_ . Note that it depends on _τ_ and _σ_ . One can take a small value for _τ_ if smooth function fit is desired. For _σ_ , one can take a prior such as log _σ ∼_ Unif( _−C, C_ ) and calculate the marginal posterior of _β_ given the data alone (another method is described in the next section). The posterior mean is


which can be used to get the function fit:


When _τ_ is small, it can be checked that _f_<sup>˜</sup><sup>_τ_</sup> ( _x_ ) will be a very smooth function of _x_ . If _τ_ is really really small, then _f_<sup>˜</sup><sup>_τ_</sup> ( _x_ ) will be essentially a constant.

This is a pretty straightforward methodology for fitting a smooth function of experience to the log(earnings) data. However, the key issue is the choice of the tuning parameter _τ_ . Here is where probability gives a very nice solution. This is discussed next.

### **22.4 Choosing the tuning parameter** _τ_

The choice of _τ_ is quite crucial to this analysis. If _τ_ is large, then the estimator _β_<sup>˜</sup><sup>_τ_</sup> will be very similar to the least squares estimator _β_<sup>ˆ</sup><sup>_ls_</sup> so that the fitted function _f_<sup>˜</sup><sup>_τ_</sup> will be quite

116

wiggly. On the other hand, if _τ_ is extremely small, then the fitted function _f_<sup>˜</sup><sup>_τ_</sup> will be basically constant which would not be useful. So we our ideal choice for _τ_ should be neither too large nor too small. How do we make this choice?

Here is how probability theory solves this problem. We shall discuss choices for _τ_ as well as for _σ_ which is also an unknown parameter that needs to be chosen in order to calculate the estimate _β_<sup>˜</sup><sup>_τ_</sup> and _f_<sup>˜</sup><sup>_τ_</sup> . The idea is simply to treat _τ_ and _σ_ as unknown parameters and put priors on them. We shall use the prior:


Note that this prior implies that we are allowing essentially (because _C_ is large) all possible values of _τ_ and _σ_ . In particular, we are not _a priori_ ruling out large _τ_ because we don’t like wiggly solutions. We then compute the posterior of _τ_ and _σ_ as:


We need to calculate the likelihood term above which is the conditional distribution of the data given _τ_ and _σ_ alone. As the model specifies the distribution of the data _Y_ 1 _. . . . , Yn_ in terms of _β_ , we need to integrate out _β_ to obtain the likelihood in terms of _τ_ and _σ_ . Fortunately, this integral can be obtained in closed form because of the following result:

_β ∼ Np_ ( _m_ 0 _, Q_ 0) and _Y | β ∼ Nn_ ( _Xβ, σ_<sup>2</sup> _In_ ) = _⇒ Y ∼ N_ � _Xm_ 0 _, XQ_ 0 _X_<sup>_T_</sup> + _σ_<sup>2</sup> _In_ � _._

Therefore (note that for us _m_ 0 is the zero vector)


Recall that _Q_ 0 is the diagonal matrix with diagonal entries _C, τ_<sup>2</sup> _, . . . , τ_<sup>2</sup> . Throughout _C_ is a large constant (in the analysis of the Earnings data, I took _C_ = 10<sup>6</sup> ). We can use this likelihood in (113) to calculate the posterior of _τ_ and _σ_ . We can get a grid based discrete appriximation of this posterior. Generally, this posterior will be peaked around the maximum likelihood values _τ_ ˆ and _σ_ ˆ so one can obtain a simpler procedure by just taking _τ_ and _σ_ to be the maximum likelihood values.

In the Earnings dataset, this procedure can be applied to the dataset of size 500 (randomly sampled from the original dataset). One can also apply this to the full dataset but the matrix inversions appearing above can be somewhat slow (some linear algebra tricks can be used to make this implementable for larger _n_ ). This analysis leads to a fairly small value of _τ_ ˆ that leads to a smooth function fit _f_<sup>˜</sup><sup>_τ_ˆ</sup> . There is something quite interesting here. There is a big difference between the two likelihoods:


Indeed, maximizing _f_ data _|β,σ_ (data) leads to the least squares estimate _β_<sup>ˆ</sup><sup>_ls_</sup> which would be quite wiggly. On the other hand, maximizing _f_ data _|τ,σ_ (data) leads to a fairly small estimate of _τ_ ˆ leading to a smooth function fit _f_<sup>˜</sup><sup>_τ_ˆ</sup> . The reason for this discrepancy can be understood by noting that


When _τ_ is large, the term _fβ|τ_ ( _β_ ) will be small simply because the normal density with variance _τ_<sup>2</sup> will be flat for large _τ_ . On the other hand, when _τ_ is too small, the weight _fβ|τ_ ( _β_ ) will be significant only for very smooth _β_ s but these _β_ s will have poor values for _f_ data _|β,σ_ (data).

117

Let me stress once more that this method for choosing _τ_ does not _a priori_ prefer small values of _τ_ . The marginal or integrated likelihood automatically selects a value of _τ_ that is small because it gives the best likelihood for the observed data.

It should be emphasized that the integrated likelihood _f_ data _|τ,σ_ (data) really does not exist in frequentist statistics so this method of tuning parameter selection is largely Bayesian.

### **22.5 Additional Comments and References**

The method for regression with the prior _N_ (0 _, τ_<sup>2</sup> ) is very similar to Ridge Regression ( `https: //en.wikipedia.org/wiki/Ridge_regression` ). Usually, the tuning parameter in Ridge regression is selected via Cross-Validation which is a method that is quite different from the above approach using the integrated or marginal likelihood. For a somewhat nuanced discussion on the benefits of Bayesian tuning parameter selection and Cross Validation, see `http://www.inference.org.uk/mackay/Bayes_FAQ.html#cv` .

If you want to read more into this approach for high-dimensional models, I strongly recommend the 1992 paper titled _Bayesian Interpolation_ by David MacKay (MacKay gives a short summary of this paper in this blog post: `https://statmodeling.stat.columbia. edu/2011/12/04/david-mackay-and-occams-razor/` ).

---

[← 21 Lecture Twenty One](22-21-lecture-twenty-one.md) · [Up: contents](index.md) · [23 Lecture Twenty Three →](24-23-lecture-twenty-three.md)
