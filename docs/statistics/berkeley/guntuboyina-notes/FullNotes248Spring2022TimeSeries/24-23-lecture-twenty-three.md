---
title: 23 Lecture Twenty Three
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 23 Lecture Twenty Three

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **23.1 Recap: Frequentist and Bayesian Model Selection**

We studied frequentist and Bayesian methods for model selection in the last couple of classes. Frequentist methods aim to estimate the generalization accuracy of each model with the best i.i.d parameter choices. For example, in the case of a model _Y_ 1 _, . . . , Yn ∼ pθ_ , frequentist methods aim to estimate generalization accuracy defined as:


where _f_<sup>_∗_</sup> denotes the true data generating density (it is assumed here that data are actually generated independently from the density _f_<sup>_∗_</sup> ), and _θ_<sup>ˆ</sup> _n_ denotes the MLE of _θ_ . Several estimators exist for the generalization error. The AIC is constructed based on the following estimate of the generalization error:


In fact, the AIC for the model is simply the above generalization accuracy estimate multiplied by constant factor _−_ 2 _n_ .

In practice, people often estimate the generalization accuracy (159) by splitting the observed dataset into two parts called training data and test data respectively, and then using the estimator:


where _y_ ˜1 _, . . . ,_ ˜ _ym_ denotes the test data and _θ_<sup>ˆ</sup> _n−m_ is the MLE of _θ_ computed from the training data. While this methodology is popular, there don’t exist principled ways of doing the testtraining split.

Bayesian Model Selection compares models in terms of the total probability each model assigns to the observed data. In the above context where the data is _y_ 1 _, . . . , yn_ and the model i.i.d is _Y_ 1 _, . . . , Yn ∼ pθ_ , the model is evaluated via


where _fθ_ denotes the prior distribution of _θ_ . This marginal probability _fY_ 1 _,...,Yn_ ( _y_ 1 _, . . . , yn_ ) is often referred to as the Evidence of the model. In the last class, we looked at the following

112

alternative formula for the evidence:


We remarked that this formula bears some resemblance to the formula for the AIC.

The Evidence also has some connection to estimates of generalization accuracy such as (161). This is because we can decompose the Evidence as


Thus the Evidence is simply the product of all the predictive probabilities for each of the data points, using the model “trained” on the previous data points. Note that


When _i_ is not too small, the posterior density _fθ|Y_ 1= _y_ 1 _,...,Yi−_ 1= _yi−_ 1( _θ_ ) should be peaked near the MLE based on the data _Y_ 1 _, . . . , Yi−_ 1 so this can be viewed as measuring the generalization accuracy of the MLE similar to (161).

The main issue that people have with Bayesian Model Selection is the reliance on the priors. The next section contains a simple example where the dependence on the prior can be seen explicitly.

### **23.2 Example: Normal Mean**

We use Bayesian Model Selection to evaluate the following two models for the observed data _y_ 1 _, . . . , yn_ :


and

i.i.d Model 2 : _Y_ 1 _, . . . , Yn ∼ N_ ( _θ,_ 1) with _θ ∼_ unif( _−C, C_ ) _._

The prior in Model 2 depends on the quantity _C_ . We assume that _C_ is large. The Evidence for _M_ 1 is


The Evidence for _M_ 2 is


Because _C_ is large, the limits _−C_ and _C_ can be replaced by _−∞_ and _∞_ respectively without nontrivially changing the value of the integral above. Thus


113

The ratio of the two Evidences is thus:


which can be simplified to


Note that if _y_ ¯ is exactly equal to zero or is close to zero, then the factors _C_ and<sup>_√_</sup> _<u>n</u>_ appearing in the formula above make the ratio of evidences quite large. Thus, when _y_ ¯ is close to zero, the simpler model _M_ 1 will be preferred. On the other hand, if _y_ ¯ is far from zero, the factor of _n_ appearing in the exponent of exp( _−ny_ ¯<sup>2</sup> _/_ 2) will make the evidence small. This, of course, is in line with intuition. If _y_ ¯ is neither very close to zero nor very far from zero, then the value of _C_ will be crucial for determining whether the ratio of evidences is larger or smaller than 1. This example shows how Bayes model selection based on evidences depends on the priors chosen in the individual models.

The ratio of the Evidence of model _M_ 1 to the Evidence of model _M_ 2 is often referred to as the _Bayes Factor_ especially in the statistics literature (see, for example, `https://en. wikipedia.org/wiki/Bayes_factor` ).

### **23.3 Application: Linear Regression**

Let us now calculate the Evidence for a linear regression model under a natural choice of prior. These evidences can be used for comparing various linear regression models (such as those obtained by different choices of covariates) for the same dataset.

The observed dataset is _y_ 1 _, . . . , yn_ . For each response value _yi_ , we also associate a _p ×_ 1 covariate vector _xi_ . The response values _y_ 1 _, . . . , yn_ are usually placed in a _n ×_ 1 vector denoted by _Y_ . The covariate vectors are placed as rows of the _n × p_ matrix _X_ . We shall consider the matrix _X_ to be deterministic. The linear model is given by


for two parameters _β_ and _σ_<sup>2</sup> . The parameter vector is _θ_ = ( _β, σ_ ). The Maximum Likelihood Estimate of _θ_ is _θ_<sup>ˆ</sup> := ( _β,_<sup>ˆ</sup> ˆ _σ_ ) where


To make this into a Bayesian model, we need a prior on _θ_ . Let us consider a generic prior _fθ_ ( _θ_ ) for now which will be specified shortly. The Evidence is then given by


The likelihood function


114

will have a single peak at _θ_<sup>ˆ</sup> and usually the likelihood is concentrated around _θ_<sup>ˆ</sup> . The prior _fθ_ ( _θ_ ), on the other hand, will be quite diffuse. As a result, we can approximate the Evidence as


The integral above can be evaluated explicitly as


Using the change of variable _σ_ = _t_<sup>_−_1</sup><sup>_/_2</sup> , the above integral can be checked to equal:


We have thus proved


We shall now specify the prior _fθ_ ( _θ_ ). We take _β_ and _σ_ to be independent with


This prior depends on the two hyperparameters _τ_ and _σ_ . The normality assumption for _β_ is standard and facilitates computation. Note that we have taken the covariance to be proportional to ( _X_<sup>_′_</sup> _X_ )<sup>_−_1</sup> as opposed to the identity matrix. This is because usually the different components of _β_ correspond to widely different covariates (e.g., _X_ 1 might be age, _X_ 2 might be current weight in pounds, _X_ 3 might be weight a year ago in kilograms etc.). In such cases, we should not treat the different components in the same footing and _β ∼ N_ (0 _, τ_<sup>2</sup> ( _X_<sup>_′_</sup> _X_ )<sup>_−_1</sup> ) is a more sensible assumption than _β ∼ N_ (0 _, τ_<sup>2</sup> _Ip_ ). The prior _β ∼ N_ (0 _, τ_<sup>2</sup> ( _X_<sup>_′_</sup> _X_ )<sup>_−_1</sup> ) is usually referred to as the Zellner prior. The uniform prior for log _σ_ is quite standard. Thus


115

Our formula for the Evidence then becomes


Plugging in the value of _σ_ ˆ = _n_<sup>_−_1</sup><sup>_/_2</sup> _∥Y − Xβ_<sup>ˆ</sup> _∥_ , we get

This quantity depends on the two prior hyperparameters _τ_ and _C_ . The dependence on _C_ is not very problematic because the indicator term _I{e_<sup>_−C_</sup> _< σ_ ˆ _< e_<sup>_C_</sup> _}_ will always be positive as _C_ is large, and the other factor (1 _/_ (2 _C_ )) will be common across the various linear regression models provided we choose the same value of _C_ in every model. The dependence on _τ_ is more sensitive however. This means that the probability assigned to the data by the Bayesian linear regression model depends sensitively on the parameter _τ_ . For some values of _τ_ , the probability of the observed data will be high and for some other values of _τ_ , the probability of the observed data will be low. Furthermore, the values of _τ_ where the probability of the observed data will be high (or low) will depend on the specific regression model (i.e., they will be different from one regression model to another, and this will have a bearing on the model selection problem).

To deal with this, the sensible way (from a Bayes perspective) is to take a prior on _τ_ and then integrate the evidence formula above with respect to that prior. For a prior _fτ_ ( _τ_ ) on _τ_ , the integrated evidence (with respect to _fτ_ ) equals


We take the prior


This leads to


We thus have


This formula depends on _C_ and _C_ 1. The indicator will usually equal 1. The rest of the formula is proportional to _CC_ 1. If these constants are chosen to be equal across the different linear regression models, then all the evidences will be affected by _C_ and _C_ 1 in the same way. In that case, we can write (ignoring terms that do not depend on the particular regression model):


116

### **23.4 Recommended Reading for Today**

1. For more comments on the relation between the Bayesian Evidence (163) and generalization accuracy estimates via cross validation, see David MacKay’s Bayes FAQ webpage `http://www.inference.org.uk/mackay/Bayes_FAQ.html#gcv` . In particular, see MacKay’s response to the question on the relation between Bayes and GCV.

2. The simple normal mean example in Section 23.2 is taken from Section 5.3 of the 1990 paper titled _From Laplace to Supernova SN 1987A: Bayesian Inference in Astrophysics_ by Tom Loredo.

3. Model selection via calculations similar to Section 23.3 can be found in Chapter 5 of the book _Bayesian spectrum analysis and parameter estimation_ by Larry Bretthorst.

117

---

[← 22 Lecture Twenty Two](23-22-lecture-twenty-two.md) · [Up: contents](index.md)
