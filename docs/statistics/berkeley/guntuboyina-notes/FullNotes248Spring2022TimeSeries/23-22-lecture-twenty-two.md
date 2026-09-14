---
title: 22 Lecture Twenty Two
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 22 Lecture Twenty Two

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **22.1 Recap: AIC**

In the last class, we looked at frequentist model selection using the Akaike Information Criterion (AIC) which is defined as:

_AIC_ ( _M_ ) := _−_ 2 _×_ (Maximized log-likelihood for _M_ ) + 2 _×_ (number of parameters in _M_ ) _._ (144)

This criterion arises in the process of estimation of the out-of-sample accuracy of the model. i.i.d More precisely, suppose that the data is _y_ 1 _, . . . , yn_ and the model is _Y_ 1 _, . . . , Yn ∼ pθ_ with parameter _θ_ . The in-sample accuracy of this model is


where _θ_<sup>ˆ</sup> _n_ is the MLE. Its out-of-sample accuracy is defined as


where _f_<sup>_∗_</sup> denotes the true data generating density. As we discussed last class, asymptotics (under a bunch of assumptions) justify


as an estimator of (146) where _p_ is the dimension of the parameter _θ_ . The AIC is just the above quantity multiplied by the constant factor _−_ 2 _n_ .

It can be noted that the out-of-sample accuracy can also be estimated more directly i.i.d (without using any asymptotics) if additional independent data _y_ ˜1 _, . . . ,_ ˜ _ym ∼ f_<sup>_∗_</sup> is available. In this case, we can use


as an estimate of (146). If additional data is not available, one can split the existing dataset _y_ 1 _, . . . , yn_ into two parts, and use one part to calculate _θ_<sup>ˆ</sup> _n_ and the other part as _y_ ˜ _j_ for the calculation of (148). To summarize, AIC and related test-data out-of-sample accuracy evaluations have the following issues:

1. AIC is popular but it uses many difficult to verify assumptions for obtaining the simple estimate (147) for (146).

2. Heldout/Test-set methodology is more popular but requires additional data. In the absence of additional data, one needs to construct training and test datasets whose choices can be adhoc. If the test dataset is too small, the estimate (148) will be noisy. On the other hand, if the tranining dataset set is too small, the MLE calculated from the training dataset will be quite different from the MLE calculated on the full dataset and which create bias in the estimation of (146).

We shall next study Bayesian Model Selection.

106

### **22.2 Bayesian Model Selection**

Bayesian model selection works for comparing Bayesian models. By a Bayesian model, I mean a model in which both the likelihood as well as the prior are specified. For example, given data _y_ 1 _, . . . , yn_ , consider the two models:


and


Model (149) is not a Bayesian model because the prior is not specified. The constraint _θ ∈_ [ _−_ 5 _,_ 5] does not precisely say how _θ_ is distributed on [ _−_ 5 _,_ 5]. On the other hand, the model (150) is a Bayesian model.

An important advantage of Bayesian models is that they allow calculation of the probability of the observed data under the model. For example, the Bayesian model (150) would calculate the probability of the observed data _y_ 1 _, . . . , yn_ as


On the other hand, the non-Bayesian model (149) would not allow computation of the probability of the observed dataset. Indeed, under the model (149), one can write the probability of the observed data as


for some _θ ∈_ [ _−_ 5 _,_ 5]. But this not give a precise answer to the probability of the observed data as it involves the unknown value _θ_ about which we only know that _θ ∈_ [ _−_ 5 _,_ 5].

Note the slight abuse of terminology here. By probability of the observed data under a model, I actually mean the joint density:


when the underlying random variables are continuous. In the case where the random variables are discrete, probability of the observed data will mean


In the continuous case, one really should think of an observation 1.29 as not being exactly equal to the number 1.29 but rather as [1 _._ 29 _− δ,_ 1 _._ 29 + _δ_ ] for some very small number _δ_ which represents recording precision. The observed dataset _y_ 1 _, . . . , yn_ is then really [ _y_ 1 _− δ, y_ 1 + _δ_ ] _, . . . ,_ [ _yn − δ, yn_ + _δ_ ]. In such a case, the probability of the observed dataset will be represented by


Thus, up to multiplication by the constant factor (2 _δ_ )<sup>_n_</sup> (which will be the same across different models), the probability of the observed dataset is proportional to the joint density. This justifies the abuse of notation referring to the joint density as the probability of the observed dataset.

107

Consider now a generic dataset _y_ ( _y_ could be a vector or matrix or something even more general). We have two Bayesian models for _y_ :


and


Bayesian Model Selection compares _M_ 1 and _M_ 2 by simply calculating the probabiliity of the observed data _y_ under both _M_ 1 and _M_ 2. Specifically, we compare


Preference will be given to the model for which the probability of observed data is higher. The following are alternative terms for _fY |M_ 1( _y_ ):

1. **Marginal or Integrated Likelihood** : _fY |M_ 1( _y_ ) is simply the integration of the likelihood _pθ_ ( _y_ ) with respect to the prior density _fθ_ ( _θ_ ).

2. **Evidence** : _fY |M_ 1( _y_ ) is often referred to as the Evidence of the model _M_ 1 under the observed data _y_ .

Thus Bayesian Model Selection compares the Integrated Likelihoods or Evidences of models. The following simple example is a good illustration of the basic idea behind Bayesian Model Selection.

**Example 22.1** (MacKay) **.** _This example is from Chapter 28 of David MacKay’s book titled Information Theory, Inference, and Learning Algorithms. We have the dataset −_ 1 _,_ 3 _,_ 7 _,_ 11 _. Consider the following two Bayesian models for this dataset:_

_1._ **_Model 1 (linear)_** _: Y_ 1 = _α and Yn_ +1 = _Yn_ + _β for n ≥_ 1 _. This model has the two parameters α and β. We assume that α and β are integer-valued that they are independently uniformly distributed over the set {−_ 50 _, −_ 49 _, . . . ,_ 49 _,_ 50 _} which has cardinality 101._

_2._ **_Model 2 (cubic)_** _: Y_ 1 = _a and Yn_ +1 = _bYn_<sup>3+</sup><sup>_cY_</sup> _n_<sup>2+</sup><sup>_d._</sup> _This model has the four parameters a, b, c, d. We assume that these four parameters are independent with a having the uniform on {−_ 50 _, −_ 49 _, . . . ,_ 49 _,_ 50 _} and b, c, d each having the distribution of x/y where x ∼ Unif{−_ 50 _, −_ 49 _, . . . ,_ 49 _,_ 50 _} and y ∼ Unif{_ 1 _, . . . ,_ 50 _} are independent._

_Which of these two models would you use for the data? Bayesian model selection is readily applicable here as both the models are Bayesian. We only need to calculate the probability of the observed data for the two models. For the linear model (M1):_


_For the cubic model:_


- = � P _{Y_ 1 = _−_ 1 _, Y_ 2 = 3 _, Y_ 3 = 7 _, Y_ 4 = 11 _| a, b, c, d,_ M2 _}_ P _{a_ = _a, b_ = _b, c_ = _c, d_ = _d |_ M2 _}_

- _a,b,c,d_

108

_It turns out that the cubic model explains the given data perfectly if and only if its four parameters a, b, c, d are chosen as a_ = _−_ 1 _, b_ = _−_ 1 _/_ 11 _, c_ = 9 _/_ 11 _, d_ = 23 _/_ 11 _. As a result_


_Clearly the probability of the observed data is much smaller for the cubic model compared to the simpler linear model. Bayesian model selection here will prefer the linear model and this would align with common sense. Note here both the models explain the data equally well. The cubic model gets downgraded however because the prior in the cubic model gives a much smaller probability to the correct parameter values compared to the linear model. We shall come back to this point later._

Bayesian model selection can also be understood from the perspective of hierarchical modeling. Specifically consider the following hierarchical model which converts the two models _M_ 1 and _M_ 2 (defined as in (151) and (152) respectively) into a _single Bayesian model_ .


The random variable _I_ represents one of the two models _M_ 1 and _M_ 2. More precisely _I_ = 1 represents _M_ 1 and _I_ = 2 represents _M_ 2. _ρ_ and 1 _− ρ_ represent the prior probabilities of _M_ 1 and _M_ 2. Under this single Bayesian model, we can calculate the posterior distribution of _I_ given the data _Y_ = _y_ as:


and


These are the posterior probabilities of the two models given the data _Y_ = _y_ . Model _M_ 1 will be preferred compared to Model _M_ 2 if and only if


As the denominators of the above probabilities are the same, this is equivalent to


Now if P _{I_ = 1 _}_ = P _{I_ = 2 _}_ i.e., if the two models are _a priori_ equally likely, then the above comparison is equivalent to comparing _fY |M_ 1( _y_ ) and _fY |M_ 2( _y_ ). Thus Bayesian model selection in terms of evidences is equivalent to looking at posterior probabilities of the two models in a hierarchical model where the prior probabilities are the same. When the prior model probabilities are not the same, we need to multiply the evidences by the prior probabilities before evaluating the models.

109

### **22.3 Two Alternative Expressions for the Evidence**

The evidence _fY |M_ 1( _y_ ) satisfies the following two alternative expressions which bear some similarities to the AIC formula (144). Both these formulae are consequences of the following expression for posterior density of the parameter _θ_ in the model _M_ 1:


Here prior( _θ_ ) = _fθ_ ( _θ_ ) and posterior( _θ_ ) is the density of _θ_ conditional on _Y_ = _y_ in the model _M_ 1. As a result, we have


Taking _θ_ to be the MLE _θ_<sup>ˆ</sup> in the model _M_ 1, we obtain


This immediately gives the formula:


log _pθ_ ˆ( _y_ ) is simply the maximized log-likelihood for the model _M_ 1. Thus


Note the similarity of (155) with (144). The first term above measures the fit of the best model in _M_ 1 to the observed data, while the second term measures model complexity. The model complexity term is more complicated compared to (144). The posterior evaluated at the MLE will generally be larger than the prior evaluated at the MLE which means that the model complexity term in (155) will be positive.

**Example 22.2** (Example 22.1 continued) **.** _Here both the models M_ 1 _(linear) and M_ 2 _(cubic) perfectly explain the observed data. Therefore the maximized log-likelihood value is the same for both M_ 1 _and M_ 2 _. Also both the models have exactly one parameter setting which explains the data perfectly, and every other setting gives zero probability to the observed data. This means that posterior_ ( _θ_<sup>ˆ</sup> ) _equals 1 for both the models. The only difference in the models will be in the prior evaluated at the best parameter setting. This term is much higher for the linear model compared to the cubic model. The reason is that the prior for the cubic model is supported on a much larger set (compared to the prior for the linear model) and consequently the prior mass assigned to each individual element of the large set is much smaller._

For the second alternative formula, take logarithms on both sides of (154) to get


Integrating both sides of the above equation with respect to posterior( _θ_ ), we get (note left hand side does not depend on _θ_ ):


110

where _D_ ( _·∥·_ ) denotes Kullback-Leibler divergence. In other words


This is similar to (156) except that maximized log-likelihood is replaced by the expected loglikelihood where the expectation is taken with respect to the posterior, and the complexity term is replaced by the Kullback-Leibler divergence between the posterior and the prior. Generally, for complex models, the posterior will be quite different from the prior leading to greater penalization (for a concrete example, consider the setting of Example 22.1).

### **22.4 The BIC**

The BIC (Bayesian Information Criterion) is obtained as an approximation for (155) when the posterior is replaced by its normal approximation. As we have seen previously, in some cases, the posterior distribution is well approximated by a normal distribution _Np_ ( _θ,_<sup>ˆ</sup> Σ _/n_ ) where _θ_<sup>ˆ</sup> is the MLE, _n_ denotes sample size and Σ is a _p × p_ covariance matrix (generally Σ is related to the Hessian of the log-likelihood evaluated at _θ_<sup>ˆ</sup> ). In such cases,


which implies that

posterior( _θ_<sup>ˆ</sup> ) = (2 _π_ )<sup>_−p/_2</sup> (det(Σ _/n_ ))<sup>_−_1</sup><sup>_/_2</sup> _._

As a result


Now if the sum of the terms<sup>_<u>p</u>_</sup> 2<sup>(log(2</sup><sup>_π_)),</sup><sup><u>1</u></sup> 2<sup>log detΣandlog prior(ˆ</sup><sup>_θ_)issmallcomparedto</sup> _<u>p</u>_ 2<sup>log</sup><sup>_n_:</sup>


then we can approximate the term in the parantheses by just 1 leading to


The formula (156) then simplifies to

_−_ 2 log (Evidence( _M_ 1)) _≈−_ 2 _×_ (Maximized log-likelihood for _M_ 1) + _p_ log _n._ (158)

The right hand side above is called the BIC (Bayesian Information Criterion). It is similar to the AIC with a more stringent penality for model complexity. As a result, BIC leads to smaller models compared to the AIC. Also note that because of (157), the formula (158) does not depend on the prior _π_ making this convenient to use in practice.

111

### **22.5 Recommended Reading for Today**

1. For a very good treatment of Bayesian Model Comparison, see Chapter 28 of the book _Information Theory, Inference and Learning Algorithms_ by David MacKay, or Chapter 20 of the book _Probability Theory: the logic of science_ by E. T. Jaynes.

2. The formulae (155) and (156) can be found in the 2010 paper titled _Bayesian system identification based on probability logic_ by James L. Beck.

---

[← 21 Lecture Twenty One](22-21-lecture-twenty-one.md) · [Up: contents](index.md) · [23 Lecture Twenty Three →](24-23-lecture-twenty-three.md)
