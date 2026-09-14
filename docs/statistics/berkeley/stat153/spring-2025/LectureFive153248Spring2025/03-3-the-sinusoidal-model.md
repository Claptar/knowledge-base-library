---
title: 3 The sinusoidal model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFive153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 The sinusoidal model

**Source:** [`LectureFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFive153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The simplest sinusoidal model for a time series _y_ 1 _, . . . .yn_ is


The unknown parameters in this model are _β_ 0 _, β_ 1 _, β_ 2 _, σ_ as well as the frequency parameter _f_ . As discussed above, we assume that the frequency _f_ lies between 0 and 0 _._ 5. If _f_ is assumed to be known, then clearly (3) is a multiple linear regression model and we can use the techniques of the past few lectures to do inference on _β_ 0 _, β_ 1 _, β_ 2 _, σ_ . But if _f_ is unknown (as will be the case for the sunspots dataset for example), then this is a nonlinear regression model.

We discuss the problem of parameter estimation and inference particularly focussing on the parameter _f_ .

### **3.1 MLE**

Let us first discuss the MLE. The likelihood is given by:


2

It is clear that the MLEs _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> 1 _, β_<sup>ˆ</sup> 2 _, f_<sup>ˆ</sup> will be given by minimizing the least squares criterion:


where


Let us use here the following notation (previously similar notation was used in the context of linear models):


The _Xf_ matrix is the same as the _X_ -matrix in the linear model when _f_ is assumed known (its first column is all ones, second column is cos(2 _πft_ ) evaluated at _t_ = 1 _, . . . , n_ , and the third column is sin(2 _πft_ ) evaluated at _t_ = 1 _, . . . , n_ ).

With this notation, (6) becomes


For each fixed value of _f_ , the quantity _S_ ( _β, f_ ) is minimized (over _β_ ) at _β_ = _β_<sup>ˆ</sup> ( _f_ ) where


Further


where _RSS_ ( _f_ ) is the Residual Sum of Squares in the regression problem of _y_ over _Xf_ for fixed _f_ . Because


These observations can be put together to get the following algorithm for computing the MLEs:

1. Take a grid of all possible values of _f_ in the range [0 _,_ 1 _/_ 2].

2. For each frequency value _f_ in the grid,

   - a) Form the matrix _Xf_

   - b) Do a regression of _y_ on _Xf_ and compute the Residual Sum of Squares _RSS_ ( _f_ )

3. Take _f_<sup>ˆ</sup> to be the grid value which minimizes _RSS_ ( _f_ ) over all the grid values.

4. Take _β_<sup>ˆ</sup> and _σ_ ˆ to be the usual regression estimates (of _β_ and _σ_ ) in the linear regression of _y_ on _Xf_ ˆ.

After finding the MLE, the next step is uncertainty quantification (which involves getting confidence intervals of the parameters etc.). However, this is tricky to do in this problem. We will instead use Bayesian analysis for uncertainty quantification.

3

### **3.2 Bayesian Inference**

We shall work with the following prior. We assume that _β_ 0 _, β_ 1 _, β_ 2 _, σ, f_ are independent with

_β_ 0 _, β_ 1 _, β_ 2 _,_ log _σ_<sup>i.i.d</sup> _∼_ unif( _−C, C_ ) and _f ∼_ unif[0 _,_ 1 _/_ 2] _._

The priors on _β_ 0 _, β_ 1 _, β_ 2 _, σ_ are the same as before in linear regression. The prior on _f_ is confined to [0 _,_ 1 _/_ 2] because, as already discussed, we are restricting the frequency parameter to [0 _,_ 1 _/_ 2].

The posterior joint density of all the parameters _β, f, σ_ (here _β_ denotes the vector consisting of _β_ 0 _, β_ 1 _β_ 2) is given by


The likelihood is given in (4) and the prior is


We shall drop the indicator terms involving _C_ while writing the posterior because, as we have seen previously in the case of linear regression, they will have essentially no impact on the posterior. The posterior is thus given by


To get the posterior density of _f_ alone ( _f_ is the most important parameter in the sinusoidal model), we need to integrate the joint posterior density above with respect to _β_ and _σ_ :


Let us first calculate the inner integral. _S_ ( _β, f_ ) is a quadratic function in _β_ so that � exp( _−S_ ( _β, f_ ) _/_ (2 _σ_<sup>2</sup> )) _dβ_ should be related to the normalizing constants in the multivariate normal density. To figure the integral precisely, we first use the Pythagorean identity (discussed last lecture):


Thus


4

where _|Xf_<sup>_TXf|_=det(</sup><sup>_X_</sup> _f_<sup>_TXf_).Here</sup><sup>_p_=3becausetherearethreecomponentsinside</sup><sup>_β_.</sup> Therefore


The change of variable _σ_ = _s_ ~~�~~ _S_ ( _β_<sup>ˆ</sup> ( _f_ ) _, f_ ), gives


The main term in this posterior is ( _S_ ( _β_<sup>ˆ</sup> ( _f_ ) _, f_ ))<sup>_−_(</sup><sup>_n−p_)</sup><sup>_/_2</sup> (the other term _|Xf_<sup>_TXf|−_1</sup><sup>_/_2does</sup> not vary significantly with _f_ ). It takes its largest value when _f_ equals the MLE _f_<sup>ˆ</sup> which minimizes _S_ ( _β_<sup>ˆ</sup> ( _f_ ) _, f_ ). The size of the power _n − p_ determines the amount of concentration of the posterior around the MLE _f_<sup>ˆ</sup> . When _n_ is large, this posterior is concentrated very tightly around _f_<sup>ˆ</sup> .

This posterior is evaluated numerically over a grid of values of _f_ in the range [0 _,_ 0 _._ 5]. The term _|Xf_<sup>_TXf|−_1</sup><sup>_/_2becomes infinite when</sup><sup>_|X_</sup> _f_<sup>_TXf|_= 0 i.e., when</sup><sup>_Xf_does not have full column</sup> rank. This is the case when _f_ = 0 or when _f_ = 1 _/_ 2. We need to exclude these edge cases while computing this posterior.

5

---

[← 2 The Sinusoid](02-2-the-sinusoid.md) · [Up: contents](index.md)
