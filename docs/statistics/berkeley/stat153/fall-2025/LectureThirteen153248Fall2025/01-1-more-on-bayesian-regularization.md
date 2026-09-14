---
title: 1 More on Bayesian Regularization
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureThirteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureThirteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 More on Bayesian Regularization

**Source:** [`LectureThirteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureThirteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1.1 Recap**

In the last lecture, we discussed Bayesian regularization in the context of the following highdimensional linear regression model:


The unknown parameters in this model are _β_ 0 _, . . . , βn−_ 1 as well as _σ_ . We can write this model in regression form as _y_ = _Xβ_ + _ϵ_ for the very special matrix _X_ :


We discussed Bayesian inference with the prior (throughout _C_ denotes a very large constant):


This prior depends on the unknown parameter (sometimes called ’hyperparameter’) _τ_ . We treat _τ_ also as an unknown parameter (along with _σ_ ) and place the following prior on _τ, σ_ :


The prior assumption (2) can be written in matrix notation as:


where _Q_ is the diagonal matrix with diagonal entries _C, C, τ_<sup>2</sup> _, . . . , τ_<sup>2</sup> .

1

We calculated the posterior distribution of all the parameters _β, σ, τ_ in the last lecture. This posterior can be described as follows. First the conditional posterior distribution of _β_ given the other two parameters _τ, σ_ is given by:


Because _Q_ is diagonal with diagonal entries _C, C,_ 1 _/τ_<sup>2</sup> _, . . . ,_ 1 _/τ_<sup>2</sup> , it is easy to see that _Q_<sup>_−_1</sup> is also diagonal with diagonal entries 1 _/C,_ 1 _/C, τ_<sup>_−_2</sup> _, . . . , τ_<sup>_−_2</sup> . Because _C_ is large, we can approximate _Q_<sup>_−_1</sup> by the matrix with diagonal entries 0 _,_ 0 _, τ_<sup>_−_2</sup> _, . . . , τ_<sup>_−_2</sup> . In other words:


With this approximation, the conditional posterior of _β_ (given _τ, σ_ ) in (3) becomes:


We saw in the last lecture that the mean of this conditional posterior distribution:


coincides with the Ridge Regularized estimate with tuning parameter _λ_ provided _λ_ = _σ_<sup>2</sup> _/τ_<sup>2</sup> .

We also derived that the posterior of _τ_ and _σ_ is given by the formula:


Using again the approximation _Q_<sup>_−_1</sup> _≈_ (1 _/τ_<sup>2</sup> ) _J_ as well as det _Q_ = _C_<sup>2</sup> _τ_<sup>2(</sup><sup>_n−_2)</sup> _∝ τ_<sup>2(</sup><sup>_n−_2)</sup> , we get


This posterior lets us figure out the value of _τ_ (as well as _σ_ ) from the data. Specifically, we can take a grid of _σ_ and _τ_ values and compute the above posterior (on the logarithmic

2

scale) at the grid points. We then obtain point estimates of _σ_ and _τ_ by taking the posterior mode or mean. Alternatively, we can obtain posterior samples of _σ_ and _τ_ by sampling from the grid points with posterior weights. For each ( _σ, τ_ ) sample, one can sample _β_ using the multivariate normal distribution (6).

In most cases, the posterior _fτ,σ|_ data( _τ, σ_ ) will prefer values of _τ_ that are not too large. Note that large _τ_ would mean that the resulting _β_ estimates (see (4)) will lead to fitted values that overfit the data. In other words, this Bayesian approach for selecting _τ_ automatically avoids overfitting.

Further, unless the data is very simple (in the sense of being well-explained by a single line), the posterior _fτ,σ|_ data( _τ, σ_ ) will also prefer values of _τ_ that are not too small. Note that small _τ_ will mean that the resulting fitted values will be very close to the least squares line.

Thus, this Bayesian approach offers protection from both overfitting and underfitting. To get some insight as to why _fτ,σ|_ data( _τ, σ_ ) protects from overfitting and underfitting, consider the following alternative expression for it:


In the above, _fτ,σ_ ( _τ, σ_ ) is a very flat function (because we are using uninformative priors for _τ_ and _σ_ ) so the behavior of _fτ,σ|_ data( _τ, σ_ ) will be mainly driven by the first term: _f_ data _|τ,σ_ (data). This term can be seen as the likelihood of the data only in terms of _τ_ and _σ_ . It is related to the original likelihood _f_ data _|β,σ_ (data) via


This integrated likelihood _f_ data _|τ,σ_ (data) tends to prefer values of _τ_ which are neither too small nor too large. For example, suppose _τ_ is very small. The the prior _fβ|τ_ ( _β_ ) will be concentrated on values of _β_ for which the corresponding fitted values are close to a single line. But for such _β_ , the data likelihood _f_ data _|β,σ_ (data) will be small (unless the dataset is simple enough to be explained by a single line).

On the other hand, suppose _τ_ is very large. Then the prior _fβ|τ_ ( _β_ ) will be quite flat over a large region so it will assign a small value (because of the factor 1 _/τ_ ) for most values of _β_ . This will bring down the overall integral value for (5).

It is important to note that the Bayesian approach for selecting hyperparameters such as _τ_ is very different from the frequentist approach for selecting the tuning parameter _λ_ using Cross-Validation (CV). CV relies on splitting the data into two parts: training and test, while the Bayesian calculation uses the entire data (no splits are necessary). For more on the relation between Bayesian approaches for hyperparameter tuning and model selection, and frequentist methods, see `http://www.inference.org.uk/mackay/Bayes_FAQ.html#gcv` and `https://statmodeling.stat.columbia.edu/2011/12/04/david-mackay-and-occams-razor/` .

### **1.2 Calculations with a slightly different prior**

The Bayesian method described above involves placing a grid on both _τ_ and _σ_ . This grid approach can be avoided by using MCMC methods such as the Gibbs sampler. We shall not be discussing these (see the 248 problem in Homework 3 if you are interested in Gibbs sampling).

There is a slightly different prior which lets us integrate over _σ_ in closed form. So the

3

grid approach would then be needed only for _τ_ (and not _σ_ ) which reduces the computational burden to some extent. This method is described here.

The idea is to reparametrize _τ_ as _τ_ = _σγ_ for a new parameter _γ_ , and change the prior to


and


where _Q_ is the diagonal matrix with diagonal entries _C, C, γ_<sup>2</sup> _σ_<sup>2</sup> _, . . . , γσ_<sup>2</sup> (this is the same _Q_ as before; the only difference is that now we are writing _γσ_ for _τ_ ). The prior joint density for _β, γ, σ_ now becomes:


This new parameter _γ_ is almost directly related to the tuning parameter _λ_ in ridge regression. Specifically, _λ_ = 1 _/γ_<sup>2</sup> or _γ_ = 1 _/√λ_ .

The likelihood function is exactly the same as before:


So the posterior for _β, γ, σ_ is:


From here, we proceed exactly as in last lecture to derive:

Again, as in last lecture, we integrate _β_ from the joint posterior to obtain the posterior of _γ, σ_ :


Simplying by use of det _Q ∝_ ( _γ_<sup>2</sup> _σ_<sup>2</sup> )<sup>_n−_2</sup> and _Q_<sup>_−_1</sup> _≈ J/_ ( _γ_<sup>2</sup> _σ_<sup>2</sup> ). we can write

_fγ,σ|_ data( _γ, σ_ )


4

The advantage of this parametrization (i.e., in terms of _γ, σ_ as opposed to _τ, σ_ ) is that the conditional posterior distribution of _σ_ given _γ_ (and the data) can be written in closed form. This is because from the above expression, we can write


The right hand side above is actually the pdf of an inverse gamma density (see `https:// en.wikipedia.org/wiki/Inverse-gamma_distribution` ). This can be seen by converting it into the density of 1 _/σ_<sup>2</sup> :


Thus


Finally, we can marginalize _σ_ to obtain the posterior of _γ_ alone as follows:


Letting


we get


By the change of variable _σ_ = _s√A_ , we obtain


With this, inference can be carried out by first taking a grid of _γ_ values and computing the above posterior (on the logarithmic scale) at the grid points. This posterior can be used to obtain posterior samples of _γ_ . For each sample of _γ_ , we can then sample _σ_ using the distribution (7). Given samples from both _γ_ and _σ_ , we can then sample _β_ using (6).

In the connection with usual ridge regression, we noted previously that _λ_ = _σ_<sup>2</sup> _/τ_<sup>2</sup> . With the new parametrization _τ_<sup>2</sup> = _γ_<sup>2</sup> _σ_<sup>2</sup> , we have _λ_ = 1 _/γ_<sup>2</sup> so that _γ_ = 1 _/√λ_ .

5

---

[Up: contents](index.md) · [2 Variance Models →](02-2-variance-models.md)
