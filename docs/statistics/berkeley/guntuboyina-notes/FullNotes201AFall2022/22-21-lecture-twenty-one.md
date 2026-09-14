---
title: 21 Lecture Twenty One
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 21 Lecture Twenty One

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **21.1 Logistic Regression**

Here is another regression model which can be handled in a straightforward fashion by probability theory. We are again in the usual regression setting where we observe data ( _yi, xi_ 1 _, xi_ 2 _, . . . , xim_ ) for _i_ = 1 _, . . . , n_ . There are _m_ explanatory variables _x_ 1 _, . . . , xm_ and one response variable. _xij_ denotes the value of the _j_<sup>_th_</sup> explanatory variable for the _i_<sup>_th_</sup> individual and _yi_ is the value of the response variable for the _i_<sup>_th_</sup> individual. Suppose now that the response variable is binary i.e., _y_ 1 _, . . . , yn_ take values in _{_ 0 _,_ 1 _}_ . In this case, the logistic regression model assumes that:


Letting _xi_ = (1 _, xi_ 1 _, . . . , xim_ )<sup>_T_</sup> and _β_ = ( _β_ 0 _, β_ 1 _, . . . , βm_ )<sup>_T_</sup> , we can write the model also as


where _β_ is the ( _m_ + 1) _×_ 1 vector with components _β_ 0 _, β_ 1 _, . . . , βm_ .

Suppose _x_<sup>_T_</sup> 1<sup>_, . . . , x_</sup> _n_<sup>_T_formtherowsofthe</sup><sup>_n × p_designmatrix</sup><sup>_X_(where</sup><sup>_p_=</sup><sup>_m_+ 1).The</sup> unknown parameters in the logistic regression model are _β_ 0 _, . . . , βm_ (note that, in contrast to the linear regression model, there is no _σ_ parameter in logistic regression). In order to use probability theory for inference on _β_ 0 _, . . . , βm_ , we assume the prior:


110

for a large _C_ . The posterior of _β_ is then


where


Note that _ℓ_ ( _β_ ) is simply the log-likelihood in this problem. The posterior density is not in standard form. If _p_ = 1 or _p_ = 2, then this can be plotted. One can use various MCMC techniques to obtain samples from this posterior. A closed form multivariate normal approximation that works quite well in practice can be found as follows. Bayesian inference from this normal approximation to the posterior coincides with usual frequentist inference for logistic regression. To get the normal approximation, first let us drop the indicator which will be irrelevant when _C_ is large to get


The normal approximation will be obtained by a second-order Taylor expansion of _ℓ_ ( _β_ ). We shall do the Taylor expansion around the MLE _β_<sup>ˆ</sup> because the posterior is peaked at _β_<sup>ˆ</sup> and the high regions of the posterior are most likely very close to _β_<sup>ˆ</sup> . Recall that the MLE _β_<sup>ˆ</sup> is defined as the maximizer of the likelihood (or log-likelihood):


It is obtained by taking the gradient of the log-likelihood and solving the equation obtained by setting the gradient to zero. It is easy to check that the gradient of the log-likelihood is


To get the maximum likelihood estimator _θ_<sup>ˆ</sup> , we need to set the gradient above to zero and solve the resulting equation for _θ_ . This cannot be done in closed form and the usual method is to use an iterative scheme such as Newton’s algorithm. The answer can be obtained from inbuilt functions in R or Python. More details behind the Newton algorithm will be provided a bit later.

Coming back to the posterior exp( _ℓ_ ( _β_ )), Taylor expansion of _ℓ_ ( _β_ ) around the MLE _β_<sup>ˆ</sup> gives


where _Hℓ_ ( _β_ ) denotes the Hessian of _ℓ_ ( _β_ ):


111

Because the _ℓ_ ( _β_<sup>ˆ</sup> ) term is a constant, it can be ignored in proportionality. Also _∇ℓ_ ( _β_<sup>ˆ</sup> ) equals zero. We thus have


We have switched above to _−Hℓ_ ( _β_<sup>ˆ</sup> ) because this matrix is positive semi-definite as _β_<sup>ˆ</sup> maximizes _ℓ_ ( _β_ ). The above term is simply the unnormalized density of the multivariate normal distribution with mean _β_<sup>ˆ</sup> and covariance matrix _−Hℓ_ ( _β_<sup>ˆ</sup> ). Observe that


Now let _W_ denote the _n × n_ diagonal matrix whose _i_<sup>_th_</sup> diagonal entry is


and also recall again that _X_ is the _n × p_ matrix with rows _x_<sup>_′_</sup> 1<sup>_, . . . , x_</sup> _n_<sup>_′_.It is then easy to check</sup> that


The posterior normal approximation is thus


The standard errors corresponding to _β_ 0 _, . . . , βm_ can then be obtained by the square roots of the diagonal entries of ( _X_<sup>_′_</sup> _WX_ )<sup>_−_1</sup> .

It turns out that Bayesian inference done with the above normal posterior approximation (101) coincides with the frequentist inference in the logistic regression model. It is easy to check this, say, in R (construct a 95% credible interval for, say, one of the components of _β_ and then compare it with the frequentist interval). Thus the usual frequentist inference for the logistic regression model can be viewed from a Bayesian perspective. Note that the above analysis relies on two assumptions: (a) the prior for _β_ is assumed to be uniform on the large cube ( _−C, C_ )<sup>_p_</sup> , and (b) the posterior is approximated by a normal distribution. These assumptions may be of course not reasonable in a particular application. In such a situation, it is conceptually very clear as to how one would proceed: if the normal approximation to the posterior is not accurate, one needs to work with the actual posterior. If the uniform prior is not reasonable, one can do the full posterior analysis (or by taking a normal approximation to the posterior) for a more appropriate prior.

### **21.2 Details behind the Newton Algorithm for computing the MLE**

The MLE _β_<sup>ˆ</sup> of _β_ is the maximizer of _ℓ_ ( _β_ ). The maximizer of _ℓ_ ( _β_ ) cannot be computed in closed form. Newton’s method is commonly used for maximizing _ℓ_ ( _β_ ). Newton’s method uses the iterative scheme


As was saw in (99),


112

where _πi_ is given by


Letting _π_ be the _n ×_ 1 vector with entries _π_ 1 _, . . . , πn_ , we can write _∇ℓ_ ( _β_ ) in matrix notation as (note that _X_ has rows _x_<sup>_T_</sup> 1<sup>_, . . . , x_</sup> _n_<sup>_T_or,equivalently,</sup><sup>_XT_hascolumns</sup><sup>_x_1</sup><sup>_, . . . , xn_):</sup>


where, as usual in regression, _Y_ denotes the _n ×_ 1 vector of response values. Also from (100), we can write


where _W_ is the _n × n_ diagonal matrix whose _i_<sup>_th_</sup> diagonal entry is _πi_ (1 _− πi_ ). Newton’s iterative scheme (102) therefore becomes


This can be rewritten as


where


The method of obtaining the MLE _β_<sup>ˆ</sup> therefore proceeds iteratively as follows. First have an initial estimate of _β_ . Call this initial estimator _β_<sup>ˆ(0)</sup> . Use this estimator to calculate _pi_ via


Use these values of _πi_ to create the response variable values _Zi_ via (104) and also use values of _πi_ to construct the matrix _W_ . With _Z_ and _W_ , we can estimate _β_ via


Now replace the initial estimator _β_<sup>ˆ(0)</sup> by _β_<sup>ˆ(1)</sup> and repeat this process. Keep repeating this until two successive estimates _β_<sup>ˆ(</sup><sup>_m_)</sup> and _β_<sup>ˆ(</sup><sup>_m_+1)</sup> do not change much. At that point, stop and report the estimate of _β_ in the logistic regression model as _β_<sup>ˆ(</sup><sup>_m_)</sup> .

The expression ( _X_<sup>_T_</sup> _WX_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _WZ_ is reminiscent of the usual ( _X_<sup>_T_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_T_</sup> _Y_ which is the usual estimate of _β_ in the linear model. In fact, this is the least squares estimate in a weighted least squares model.

---

[← 20 Lecture Twenty](21-20-lecture-twenty.md) · [Up: contents](index.md) · [22 Lecture Twenty Two →](23-22-lecture-twenty-two.md)
