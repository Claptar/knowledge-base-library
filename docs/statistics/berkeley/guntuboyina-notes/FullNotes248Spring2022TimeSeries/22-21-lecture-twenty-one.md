---
title: 21 Lecture Twenty One
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 21 Lecture Twenty One

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **21.1 Model Selection**

We shall next look at the topic of model selection. This important problem appears in almost every data analysis. In our context of state space models, consider, for example, the problem of deciding between a local level model or a local linear model. This is the problem of Model Selection. There are Frequentist and Bayesian approaches to Model Selection. One popular frequentist approach is the AIC (Akaike Information Criterion) and one popular Bayesian approach is the BIC (Bayesian Information Criterion). We shall study these procedures.

### **21.2 Akaike Information Criterion (AIC)**

The AIC for a model _M_ is defined as:

_AIC_ ( _M_ ) := _−_ 2 _×_ (Maximized log-likelihood for _M_ ) + 2 _×_ (number of parameters in _M_ ) _._

This can be calculated for any model for which we can maximize likelihood. Let us look at the logic behind this criterion in the case of i.i.d models. State Space Models are not of this i.i.d kind but the analysis can be extended to them. Consider a dataset _y_ 1 _, . . . , yn_ . By an i.i.d model _M_ , we mean a model which postulates that _y_ 1 _, . . . , yn_ are realizations of random variables _Y_ 1 _, . . . , Yn_ which satisfy


96

for some family of densities _pθ_ with a _p_ -dimensional parameter _θ_ . The log-likelihood for this model is:


The maximizer of this log-likelihood is the MLE (Maximum Likelihood Estimator) _θ_<sup>ˆ</sup> _n_ . The AIC for this model is thus:


The AIC for a different model _M_<sup>˜</sup> which says that _Y_ 1 _, . . . , Yn_ are i.i.d _qα_ with a _q_ -dimensional parameter _α_ is


The logic behind the AIC formulae (128) and (129) is explained below.

#### **21.2.1 The simple case of no parameters**

Consider first the case where we consider models with no parameters. Specifically, _M_ is i.i.d i.i.d the model _Y_ 1 _, . . . , Yn ∼ p_ and _M_<sup>˜</sup> is the model _Y_ 1 _, . . . , Yn ∼ q_ . In this case, the AIC is simply the negative log-likelihood (multiplied by 2). In other words, we prefer the model with the higher loglikelihood. This makes sense and one of the explanations for looking at the loglikelihood is the following. Suppose that the true data generating process is given by:


It then makes sense to pick _p_ or _q_ depending on how close they are to _f_<sup>_∗_</sup> . This obviously depends on the specific way in which “closeness” is measured. One common choice is the Kullback-Leiber divergence:

and similarly


Note that the first term � _f_<sup>_∗_</sup> log _f_<sup>_∗_</sup> is the same for both _D_ ( _f_<sup>_∗_</sup> _∥p_ ) and _D_ ( _f_<sup>_∗_</sup> _∥q_ ). Thus comparing _D_ ( _f_<sup>_∗_</sup> _∥p_ ) and _D_ ( _f_<sup>_∗_</sup> _∥q_ ) is equivalent to comparing � _f_<sup>_∗_</sup> log _p_ and � _f_<sup>_∗_</sup> log _q_ . However _f_<sup>_∗_</sup> is unknown so we cannot directly compare � _f_<sup>_∗_</sup> log _p_ and � _f_<sup>_∗_</sup> log _q_ . But a simple unbiased estimate of � _f_<sup>_∗_</sup> log _p_ is simply:


because the true data generating mechanism is (130). Similarly


is unbiased for � _f_<sup>_∗_</sup> log _q_ . We thus compare


and pick the model with the higher value. This is clearly the same as comparing likelihoods.

97

#### **21.2.2 Models with parameters**

Now suppose that the two models are given by


and


The true data generating process is still (130). One can again consider the accuracy of estimating _f_<sup>_∗_</sup> under the Kullback-Leibler divergence. Model _M_ would provide the estimate _pθ_ ˆ _n_ and Model _M_<sup>˜</sup> would provide the estimate _qα_ ˆ _n_ for _f_<sup>_∗_</sup> . Here _θ_<sup>ˆ</sup> _n_ is the MLE of _θ_ under Model _M_ and _α_ ˆ _n_ is the MLE of _α_ under Model _M_<sup>˜</sup> . The Kullback-Leibler divergences are

and


Thus comparing the Kullback-Leibler divergences is equivalent to comparing


As we do not know _f_<sup>_∗_</sup> , we would need to estimate the above integrals from the data _y_ 1 _, . . . , yn_ generating according to (130). Natural estimators are given by


However, unlike in the case where there are no parameters, these are no longer unbiased estimators of � _f_<sup>_∗_</sup> log _pθ_ ˆ _n_ and � _f_<sup>_∗_</sup> log _qα_ ˆ _n_ respectively. Indeed, we would expect _n_<sup><u>1</u></sup> � _ni_ =1<sup>log</sup><sup>_p_</sup> _θ_<sup>ˆ</sup> _n_<sup>(</sup><sup>_Yi_)</sup> to be larger than � _f_<sup>_∗_</sup> log _pθ_ ˆ _n_ and this will be especially true if _pθ_ is a complicated model which overfits the data. In order to correct the bias, we need to understand the quantity:


and the analogous quantity for the second model. In order to estimate the above quantity, we need to know something about the behaviour of the maximum likelihood estimator _θ_<sup>ˆ</sup> _n_ .

#### **21.2.3 Digression: MLE asymptotic distribution**

i.i.d Given data _y_ 1 _, . . . , yn_ and a candidate model which stipulates _Y_ 1 _, . . . , Yn ∼ pθ_ , consider the behaviour of the MLE:


The asymptotic behaviour of the MLE is usually studied under two assumptions: wellspecified model and misspecified model.

**MLE Asymptotics when model is correctly specified** : By “model is correctly specified”, we assume that the observed data are realizations of random variables _Y_ 1 _, . . . , Yn_ which

98

are independent and identically distributed according to _pθ∗_ for some _θ_<sup>_∗_</sup> . In other words, the true data generating distribution belongs to the candidate model class _{pθ}_ . In this case, the MLE _θ_<sup>ˆ</sup> _n_ is an accurate estimator of _θ_<sup>_∗_</sup> . More precisely, it can be shown that


where _I_ ( _θ_<sup>_∗_</sup> ) is the Fisher information matrix:


Here E _θ∗_ denotes Expectation taken under the assumption _Y ∼ pθ∗_ . _I_ ( _θ_<sup>_∗_</sup> ) is a _p × p_ matrix where _p_ is the dimension of _θ_<sup>_∗_</sup> . According to the above definition, the ( _i, j_ )<sup>_th_</sup> entry of _I_ ( _θ_<sup>_∗_</sup> ) is given by


A sketch of the proof of (132) can be found in the next subsection in the more general setting of model misspecification.

It is important to note that the Fisher Information Matrix has two alternative formulae in this correctly specified case. The first is that


where Cov _θ∗_ denotes covariance taken under the assumption _Y ∼ pθ∗_ . To see this, note first that Cov( _Z_ ) = E( _ZZ_<sup>_T_</sup> ) _−_ (E _Z_ )(E _Z_ )<sup>_T_</sup> . Thus to see why this alternative formula of _I_ ( _θ_<sup>_∗_</sup> ) is true, we only need to show that


This is true because


Note that we have interchanged the two operations of integation with respect to _y_ and differentiation with respect to _θ_ . Some regularity conditions are necessary for such an interchange which we are ignoring in this treatment. This mean zero property validates the alternative formula (134).

99

The second alternative formula of Fisher Information is:


where _Hθ_ denotes Hessian. The ( _i, j_ )<sup>_th_</sup> entry of _I_ ( _θ_<sup>_∗_</sup> ) according to this formula is


To verify the validity of this alternative formula, we need to prove that (133) and(136) are equal. For this, observe first that


As a result


The first term in the right hand side above equals zero because


and this proves that (133) and (136) are equal.

Here is some popular terminology that is used to describe these results:

1. The quantity _θ �→∇θ_ log _pθ_ ( _y_ ) is called the score function corresponding to the model _{pθ}_ .

2. The Fisher Information Matrix is defined as the second moment of the score function evaluated at the true parameter value.

3. When the model is correctly specified, The Fisher Information Matrix equals the covariance matrix of the score function evaluated at the true parameter value.

4. When the model is correctly specified, the Fisher Information Matrix equals the negative of the Hessian of the log-likelihood evaluated at the true parameter value.

**MLE Asymptotics when model is misspecified** : Here we assume that the data i.i.d _y_ 1 _, . . . , yn_ are generated according to the model _Y_ 1 _, . . . , Yn ∼ f_<sup>_∗_</sup> where _f_<sup>_∗_</sup> does **not** necessarily belong to the class _pθ_ . In other words, _f_<sup>_∗_</sup> may not equal _pθ_ for any parameter value

100

_θ_ . This means that there is no “true” parameter value _θ_<sup>_∗_</sup> anymore. So what exactly is the MLE _θ_<sup>ˆ</sup> _n_ estimating? It turns out that the MLE _θ_<sup>ˆ</sup> _n_ is really estimating the parameter value _θ_<sup>_∗_</sup> for which _pθ∗_ is closest to _f_<sup>_∗_</sup> in Kullback-Leibler divergence:


Because _D_ ( _f_<sup>_∗_</sup> _∥pθ_ ) = � _f_<sup>_∗_</sup> log _f_<sup>_∗_</sup> _−_ � _f_<sup>_∗_</sup> log _pθ_ , we can also define _θ_<sup>_∗_</sup> as


In other words, _θ_<sup>_∗_</sup> can also be thought of as the maximizer of the average loglikelihood (averaged with respect to the true data generating density).

In this misspecified case, it again turns out that<sup>_√_</sup> _<u>n</u>_ converges to a zero mean � _θ_ ˆ _n − θ_<sup>_∗_�</sup> multivariate normal distribution with some covariance matrix. However the covariance matrix now is not simply the inverse of the Fisher Information Matrix. To understand this, first let us consider the following simple example.

_i.i.d ∼_ **Example 21.1** (Normal Mean Model) **.** _Suppose Y_ 1 _, . . . , Yn f_<sup>_∗_</sup> _for some density f_<sup>_∗_</sup> _. Consider the model N_ ( _θ,_ 1) _i.e.,_


_Let us consider the misspecified setting where f_<sup>_∗_</sup> _is not equal to N_ ( _θ,_ 1) _for any θ. What is θ_<sup>_∗_</sup> _in this case? The loglikelihood averaged with respect to f_<sup>_∗_</sup> _is:_


_It is clear that the minimizer of_ � _f_<sup>_∗_</sup> log _pθ over all θ ∈_ R _equals the mean corresponding to the density f_<sup>_∗_</sup> _. We thus take_


_On the other hand, given data Y_ 1 _, . . . , Yn, the MLE of θ is easily seen to be_

_By the Central Limit Theorem (assuming that the variance corresponding to f_<sup>_∗_</sup> _is finite), we have_


_where V_<sup>_∗_</sup> _is the variance corresponding to f_<sup>_∗_</sup> _. What is the Fisher Information Matrix in this case? The loglikelihood and the score function equal respectively_

_and_


101

_The second moment of the score function evaluated at θ_ = _θ_<sup>_∗_</sup> _is therefore:_


_Thus the asymptotic variance of the MLE does not equal the inverse of I_ ( _θ_<sup>_∗_</sup> ) _(in this case, it equals exactly the Fisher Information)._

Let us now state the result for the asymptotic distribution of the MLE _θ_<sup>ˆ</sup> _n_ in the misspecified case. We need some definitions. First the Fisher Information Matrix as before is defined as the second moment of the score function:


The crucial difference from the correctly specified case is that the Expectation is taken to be with respect to the true density _f_<sup>_∗_</sup> (and not _pθ∗_ ). As in the well-specified case, _I_ ( _θ_<sup>_∗_</sup> ) also equals the covariance matrix of the score function evaluated at _θ_<sup>_∗_</sup> . This is because


The last equality above is because the gradient of � log _pθ_ ( _y_ ) _f_<sup>_∗_</sup> ( _y_ ) _dy_ equals zero at _θ_ = _θ_<sup>_∗_</sup> as _θ_<sup>_∗_</sup> maximizes the average loglikelihood (with respect to _f_<sup>_∗_</sup> ) over _θ_ (this is the definition of _θ_<sup>_∗_</sup> ). Therefore


In the well-specified setting, we have seen that the Fisher Information Matrix also equals the negative of the Expected Hessian of the loglikelihood evaluated at _θ_ = _θ_<sup>_∗_</sup> (see the formula (135)). This is no longer in the case of misspecification. Specifically here _I_ ( _θ_<sup>_∗_</sup> ) is not necessarily the same as _J_ ( _θ_<sup>_∗_</sup> ) where


That _I_ ( _θ_<sup>_∗_</sup> ) and _J_ ( _θ_<sup>_∗_</sup> ) can be distinct is seen in the simple normal example.

**Example 21.2** (Normal Mean Model continued) **.** _Consider the same setting of Example_ (21.1) _. Here the Hessian of the loglikelihood is easily seen to be dθd_<sup>22log</sup><sup>_pθ_(</sup><sup>_y_)=</sup><sup>_−_1</sup><sup>_sothat_</sup> _J_ ( _θ_<sup>_∗_</sup> ) = 1 _. On the other hand, we saw in Example_ (21.1) _that I_ ( _θ_<sup>_∗_</sup> ) = _V_<sup>_∗_</sup> _where V_<sup>_∗_</sup> _is the variance corresponding to f_<sup>_∗_</sup> _. Thus, unless V_<sup>_∗_</sup> = 1 _, the two quantities I_ ( _θ_<sup>_∗_</sup> ) _and J_ ( _θ_<sup>_∗_</sup> ) _will be different. Note that if we insist on correct specification, f_<sup>_∗_</sup> = _N_ ( _θ_<sup>_∗_</sup> _,_ 1) _, then the variance corresponding to f_<sup>_∗_</sup> _will be 1 so that I_ ( _θ_<sup>_∗_</sup> ) _and J_ ( _θ_<sup>_∗_</sup> ) _will be the same._

102

Here is the correct asymptotic distribution result for the MLE in the misspecified setting:


The formula _J_ ( _θ_<sup>_∗_</sup> )<sup>_−_1</sup> _I_ ( _θ_<sup>_∗_</sup> ) _J_ ( _θ_<sup>_∗_</sup> )<sup>_−_1</sup> for the covariance is sometimes called the “Sandwich Formula” (see e.g., `http://www.econ.uiuc.edu/~roger/courses/476/lectures/L10.pdf` ). In the case of correct specification, we have _J_ ( _θ_<sup>_∗_</sup> ) = _I_ ( _θ_<sup>_∗_</sup> ) as we saw in the previous section so that (141) is identical to (132).

It is easy to see that (141) gives the correct answer in the simple normal mean example. **Example 21.3** (Normal Mean Model Continued) **.** _Here I_ ( _θ_<sup>_∗_</sup> ) = _V_<sup>_∗_</sup> _and J_ ( _θ_<sup>_∗_</sup> ) = 1 _so that_ (141) _gives_


_which coincides with_ (137) _._

Here is a sketch of the proof of (141).

_Proof of_ (141) _._ By definition, the MLE _θ_<sup>ˆ</sup> _n_ maximizes the loglikelihood function:


Thus the gradient of the loglikelihood evaluated at the MLE _θ_<sup>ˆ</sup> _n_ will be zero:


Now intuitively, _θ_<sup>ˆ</sup> _n_ should be close to _θ_<sup>_∗_</sup> . So we do a Taylor expansion of _∇ℓ_ ( _θ_<sup>ˆ</sup> _n_ ) around _θ_<sup>_∗_</sup> :


which immediately gives


We rewrite the above as

Now


i.i.d By (138), each random variable _∇θ_ log _pθ_ ( _Yi_ ) (note _Yi ∼ f_<sup>_∗_</sup> ) has mean zero. Thus by the Central Limit Theorem (and (139)),


Further, by the law of large numbers (and (140)),

Thus

which proves (141).

103

### **21.3 Back to AIC**

Let us now get back to the setting of Section 21.2.2. Our goal is to understand the quantity (131). This is a random variable (as it is a function of _Y_ 1 _, . . . , Yn_ which are independently distributed according to _f_<sup>_∗_</sup> ). We shall concentrate on finding the expectation of (131):


We write


where


and

It is clear that _Q_ 2 = 0 so we only need to focus on _Q_ 1 and _Q_ 3. For _Q_ 1, Taylor expansion around _θ_<sup>_∗_</sup> gives


The gradient in the first term above equals zero (because of (138)). The Hessian equals


because of the definition (140) of _J_ ( _θ_<sup>_∗_</sup> ). Thus


Because of (141), we take


to get


104

For _Q_ 3, we use Taylor expansion around the MLE _θ_<sup>ˆ</sup> _n_ to get


The gradient in the first term above equals zero because _θ_<sup>ˆ</sup> _n_ maximizes log-likelihood. The Hessian for large _n_ can be approximated by _−J_ ( _θ_<sup>_∗_</sup> ) (this is because _θ_<sup>ˆ</sup> _n_ will be close to _θ_<sup>_∗_</sup> ). Thus


which (just as in the computation of _Q_ 1) leads to


We have thus proved


This suggests the estimator:

for

(142) is not really an estimator because the second term depends on _θ_<sup>_∗_</sup> . However if we assume that the model is well-specified, then _I_ ( _θ_<sup>_∗_</sup> ) = _J_ ( _θ_<sup>_∗_</sup> ) so that the second term equals _p_ (note _p_ is the dimension of _θ_<sup>_∗_</sup> ). We then get


as the estimate for (143). The quantity (142) is simply the AIC multiplied by the constant _−_ 2<sup><u>1</u></sup> _n_<sup>.ThismotivatestheuseofAICformodelselection.</sup>

### **21.4 Recommended Reading for Today**

1. A description of the AIC can be found in Chapter 4 (especially Section 4.5) of the Kitagawa book.

2. Various applications of the AIC for model selection in state space models can be found throughout the Kitagawa-Gersch and the Kitagawa books.

3. More details on the AIC and other related model selection criteria can be found in the book _Information Criteria and Statistical Modeling_ by Konishi and Kitagawa (accessible through the Berkeley library website).

105

---

[← 20 Lecture Twenty](21-20-lecture-twenty.md) · [Up: contents](index.md) · [22 Lecture Twenty Two →](23-22-lecture-twenty-two.md)
