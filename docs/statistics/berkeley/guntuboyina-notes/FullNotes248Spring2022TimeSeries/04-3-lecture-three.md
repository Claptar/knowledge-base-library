---
title: 3 Lecture Three
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Lecture Three

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We are in the midst of looking at different applications of state space models. Our next step is to see that ARMA models are special cases of state space models. We shall first consider the AR(2) model before going to general state space models. Historically, the AR(2) model was introduced in the context of the sunspots data (see the classical 1927 paper titled “On a method of investigating periodicities disturbed series, with special reference to Wolfer’s sunspot numbers” by G. Udny Yule or the 2011 book “The Foundations of Modern Time Series Analysis” by T.C. Mills). It is often claimed that (see, for example, `https://en. wikipedia.org/wiki/Sunspot` ) the sunspot number varies according to an approximately 11-year cycle. We can verify this by fitting the simple sinusoidal model:


10

to the observed data ( _t_ 1 _, y_ 1) _, . . . ,_ ( _tn, yn_ ). Here _ti_ refers to year _i_ and _yi_ denotes the average number of sunspots for year _ti_ . In the dataset (obtained from `https://wwwbis.sidc.be/ silso/infosnytot` ), we have data for all years from 1700 to 2019. So we are analyzing the whole data, we can take _n_ = 320 and _t_ 1 = 1700 _, t_ 2 = 1701 _, t_ 3 = 1702 _, . . . , tn_ = 2019. In general, it is not necessary to have the observed times _ti_ to be consecutive (i.e., it is okay for the time series to have some observation gaps).

Today, we shall study the problem of fitting the model (7) and obtaining estimates of the frequency parameter _ω_ from the sunspots data. Note that, if we believe the 11-year cycle for the sunspots data, then we would expect the data to give an estimate of _ω_ (in the model (7)) that is close to 2 _π/_ 11 = 0 _._ 5712. In the next class, we shall see the connection between the model (7) and AR(2).

For the model (7), we shall assume that


which is the most standard distributional assumption for errors. The problem then is to estimate the frequency parameter _ω_ . The other four parameters _µ, α_ 1 _, α_ 2 _, σ_ are unknown but they are not our main focus (these parameters can be termed _nuisance parameters_ ). For principled estimation of _ω_ in the presence of the nuisance parameters _µ, α_ 1 _, α_ 2 _, σ_ , we shall take the Bayesian approach with the following natural prior:


for a large number _C_ (the exact value of _C_ will not matter in the following calculations). Note that as _σ_ is always positive, we have made the uniform assumption on log _σ_ (by the change =<sup>_I{e−C<x<eC_</sup><sup>_<u>}</u>_</sup> . of variable formula, we would have _fσ_ ( _x_ ) = _f_ log _σ_ (log _x_ ) _x_<sup><u>1</u>=</sup><sup>_I{−C<_</sup> 2 _Cx_<sup>log</sup><sup>_x<C}_</sup> 2 _Cx_

The posterior for all the unknown parameters _ω, µ, α_ 1 _, α_ 2 _,_ log _σ_ is then (below we write the term “data” for _Y_ 1 = _y_ 1 _, . . . , Yn_ = _yn_ ):

_fω,µ,α_ 1 _,α_ 2 _,σ|_ data( _ω, µ, α_ 1 _, α_ 2 _, σ_ ) _∝ fY_ 1 _,...,Yn|ω,µ,α_ 1 _,α_ 2 _,σ_ ( _y_ 1 _, . . . , yn_ ) _fω,µ,α_ 1 _,α_ 2 _,σ_ ( _ω, µ, α_ 1 _, α_ 2 _, σ_ ) _._

The two terms on the right hand side above are


and

_fω,µ,α_ 1 _,α_ 2 _,σ_ ( _ω, µ, α_ 1 _, α_ 2 _, σ_ ) = _fω_ ( _ω_ ) _fµ_ ( _µ_ ) _fα_ 1( _α_ 1) _fα_ 2( _α_ 2) _fσ_ ( _σ_ )


11

We thus obtain


To obtain the posterior density of _ω_ , we simply integrate the above with respect to _µ, α_ 1 _, α_ 2 _, σ_ . Thus for every _ω ∈_ ( _−C, C_ ),


When _C_ is large, the above integral is well-approximated by


This integral can be evaluated exactly. The calculation is easiest done using matrix notation. Let


With this notation,


so that (8) is the same as


Now if _β_<sup>ˆ</sup> is the least squares estimator:


then


The integral (9) then becomes

12

We shall now use the formula:


where Σ is a _p × p_ positive definite matrix and the integral is over _x_ = ( _x_ 1 _, . . . , xp_ ). This is basically the formula for the normalizing constant for the multivariate normal distribution which we shall study next week.

This formula with _p_ = 3 and Σ<sup>_−_1</sup> = _X_<sup>_′_</sup> _X/_ ( _σ_<sup>2</sup> ) (or equivalently Σ = _σ_<sup>2</sup> ( _X_<sup>_′_</sup> _X_ )<sup>_−_1</sup> ) gives


The integral (8) thus equals


The change of variable


then gives


Putting everything together, we have proved that


Note that the right hand side depends crucially on _ω_ because _X_ depends on _ω_ . Also _β_<sup>ˆ</sup> depends on _X_ as _β_<sup>ˆ</sup> = ( _X_<sup>_′_</sup> _X_ )<sup>_−_1</sup> _X_<sup>_′_</sup> _Y_ . To make this explicit, let us write _X_ ( _ω_ ) for _X_ and _β_ ˆ( _ω_ ) for _β_ ˆ:


This function of _ω_ can be plotted on the computer (and normalized so the density integrates to one). Note that _p_ = 3. This allows inference on _ω_ based on the data.

### **3.1 Connection to the Periodogram**

It turns out the Bayesian posterior (10) can be related to the periodogram which is a standard object in time series analysis. The periodogram corresponding to the time series data ( _ti, yi_ ) is defined as


13

This is a function of _ω ∈_ R. Usually, the periodogram is computed for uniformly spaced data (where the time points _tj_ can be taken to be consecutive integers such as 0 _, . . . , n −_ 1) and when _ω_ is of the form<sup><u>2</u></sup><sup>_<u>πk</u>_</sup> _n_ for some integer _k ∈{_ 1 _, . . . , n −_ 1 _}_ . These values of _ω_ are known as _Fourier Frequencies_ . Observe that _I_ ( _ω_ ) can also be written as


where _i_ =<sup>_√_</sup> _−_ 1, _e_<sup>_iωtj_</sup> is the complex number cos( _ωtj_ ) + _i_ sin( _ωtj_ ) and _|z|_ for a complex number _z_ denotes its modulus. The complex number


is termed the Discrete Fourier Transform of the data when _tj_ = _j −_ 1 and _ω_ ranges over the Fourier frequencies. Thus, the periodogram is basically the squared modulus of the DFT (scaled by _n_ ).

It is a standard procedure to look at the periodogram of an observed time series in order to determine periodic components present in the data. It turns out that the Bayesian posterior (10) is related to the periodogram as we shall argue below. To see this, first note that the posterior (10) is described in terms of the matrix _X_ ( _ω_ ). For this matrix, it is easy to see that


To see this, consider the case where the time points are consecutive in which case we take _tj_ = _j −_ 1. Then for a wide range of _ω_ , we will argue that


Let me provide the argument for one of the above assertions. The argument for the others is similar. We shall consider the assertion


14

To see this, write


The sums above can be evaluated explicitly under the assumption that the times are uniformly spaced _tj_ = _j −_ 1:

and similarly


Now if _ω_ is a Fourier frequency of the form _ω_ = 2 _πk/n_ , then _e_<sup>_±_2</sup><sup>_iωn_</sup> = _e_<sup>_±_4</sup><sup>_iπk_</sup> = cos(4 _πk_ ) _± i_ sin(4 _πk_ ) = 1 so the above displayed sums are zero leading to (12). If _ω_ is not a Fourier frequency, we can write


because _|e_<sup>2</sup><sup>_iωn_</sup> _−_ 1 _| ≤|e_<sup>2</sup><sup>_iωn_</sup> _|_ + 1 _≤_ 2. We can thus ignore this term if _n|e_<sup>2</sup><sup>_iω_</sup> _−_ 1 _|_ is large. Similarly the term


can be ignored if _n|e_<sup>_−_2</sup><sup>_iω_</sup> _−_ 1 _|_ is large. The assertion (12) is therefore justified if _n|e_<sup>_±_2</sup><sup>_iω_</sup> _−_ 1 _|_ is large (which will often be the case unless _ω_ is too close to zero).

In the rest of this section, we shall assume that


Under this condition, the integral (9) can be evaluated in the following alternative way. We start with


15

Thus the inner integral over R<sup>3</sup> in (9) can be broken down into 3 one dimensional integrals (as opposed to one three-dimensional integral) as


can be evaluated in the following alternative way. Each of the above three integrals can be evaluated explicitly using the one-dimensional integration formula:


We thus deduce


Finally the integration over _σ_ can be done as before to obtain

Using the periodogram formula (11), we can write the above as


Thus the Bayesian posterior for _ω_ is essentially a function of the periodogram (and the sample variance of the data). But it is important to note that it is a very specific function which can look quite different from the raw periodogram. For example, for the sunspots dataset, the periodogram has several peaks but the Bayesian posterior is typically quite strongly concentrated. Thus if we are trying to find a single frequency in a time series dataset, the Bayesian posterior will provide that information much more precisely compared to the periodogram.

### **3.2 Recommended Reading for Today**

1. The Bayesian analysis of the model (7) is taken from the book _Bayesian spectrum analysis and parameter estimation_ by Larry Bretthorst (available freely online). You can read Chapters 1 and 2 of that book.

16

2. The periodogram is a standard object in time series analysis and it can be found in many books; see for example Chapter 4 of the book _Time series analysis and its applications_ by Shumway and Stoffer (note that some authors use slightly different scaling factors while defining the periodogram).

---

[← 2 Lecture Two](03-2-lecture-two.md) · [Up: contents](index.md) · [4 Lecture Four →](05-4-lecture-four.md)
