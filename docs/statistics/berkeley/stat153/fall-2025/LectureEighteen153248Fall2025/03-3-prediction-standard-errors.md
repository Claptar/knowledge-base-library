---
title: 3 Prediction Standard Errors
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureEighteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Prediction Standard Errors

**Source:** [`LectureEighteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureEighteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

To compute prediction standard errors, we can again fix the parameter values _θ_ , and then attempt to calculate:


The prediction standard error corresponding to the predicted value for _yn_ + _i_ can then be taken to be ~~�~~ _Vi_ ( _θ_<sup>ˆ</sup> ) (note that _θ_ is replaced by the conditional MLE _θ_<sup>ˆ</sup> ).

It turns out that it is not really possible to setup a recursion for _Vi_ ( _θ_ ). To see this, note that:

_V_ 1( _θ_ ) = var( _yn_ +1 _| y_ 1 _, . . . , yn, θ_ ) = var( _ϕ_ 0 + _ϕ_ 1 _yn_ + _ϕ_ 2 _yn−_ 1 + _· · ·_ + _ϕpyn_ +1 _−p_ + _ϵn_ +1 _| y_ 1 _, . . . , yn, θ_ ) = var( _ϵn_ +1 _| y_ 1 _, . . . , yn, θ_ ) = _σ_<sup>2</sup> _._

Next

_V_ 2( _θ_ ) = var( _yn_ +2 _| y_ 1 _, . . . , yn, θ_ ) = var( _ϕ_ 0 + _ϕ_ 1 _yn_ +1 + _ϕ_ 2 _yn_ + _· · ·_ + _ϕpyn_ +2 _−p_ + _ϵn_ +2 _| y_ 1 _, . . . , yn, θ_ ) = var( _ϕ_ 1 _yn_ +1 + _ϵn_ +2 _| y_ 1 _, . . . , yn, θ_ ) = _ϕ_<sup>2</sup> 1<sup>var(</sup><sup>_yn_+1</sup><sup>_| y_1</sup><sup>_, . . . , yn, θ_) + var(</sup><sup>_ϵn_+2</sup><sup>_| y_1</sup><sup>_, . . . , yn, θ_)</sup> = _ϕ_<sup>2</sup> 1<sup>_V_1(</sup><sup>_θ_) +</sup><sup>_σ_2=</sup><sup>_σ_2(1 +</sup><sup>_ϕ_2</sup> 1<sup>)</sup><sup>_._</sup>

The next term is

_V_ 3( _θ_ ) = var( _yn_ +3 _| y_ 1 _, . . . , yn, θ_ ) = var( _ϕ_ 0 + _ϕ_ 1 _yn_ +2 + _ϕ_ 2 _yn_ +1 + _· · ·_ + _ϕpyn_ +3 _−p_ + _ϵn_ +3 _| y_ 1 _, . . . , yn, θ_ ) = var( _ϕ_ 1 _yn_ +2 + _ϕ_ 2 _yn_ +2 + _ϵn_ +3 _| y_ 1 _, . . . , yn, θ_ ) = var( _ϕ_ 1 _yn_ +2 + _ϕ_ 2 _yn_ +2 _| y_ 1 _, . . . , yn, θ_ ) + var( _ϵn_ +3 _| y_ 1 _, . . . , yn, θ_ ) _._

The first term in the right hand side above cannot be written down in terms of _V_ 1( _θ_ ) a nd _V_ 2( _θ_ ) alone. It also involves the covariance between _yn_ +1 and _yn_ +2 (given _y_ 1 _, . . . , yn, θ_ ).

Instead of working with the variances alone, we will get the recursion by working with the conditional **covariance matrices** of _yn_ +1 _, . . . , yn_ + _k_ (given _θ_ and the data) for _k_ = 1 _,_ 2 _, . . ._ .

Below we review some basic facts about covariance matrices.

### **3.1 Covariance Matrices**

A finite number of random variables can be viewed together as a random vector. More precisely, a random vector is a vector whose entries are random variables. Let _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> be an _n ×_ 1 random vector. Its Expectation E _Y_ is defined as a vector whose _i_ th entry is the expectation of _Yi_ i.e., E _Y_ = (E _Y_ 1 _,_ E _Y_ 2 _, . . . ,_ E _Yn_ )<sup>_T_</sup> . The covariance matrix of _Y_ , denoted by Cov( _Y_ ), is an _n × n_ matrix whose ( _i, j_ )th entry is the covariance between _Yi_ and _Yj_ . Two important but easy facts about Cov( _Y_ ) are:

1. The diagonal entries of Cov( _Y_ ) are the variances of _Y_ 1 _, . . . , Yn_ . More specifically the ( _i, i_ )th entry of the matrix Cov( _Y_ ) equals _var_ ( _Yi_ ).

4

2. Cov( _Y_ ) is a symmetric matrix i.e., the ( _i, j_ )th entry of Cov( _Y_ ) equals the ( _j, i_ ) entry. This follows because Cov( _Yi, Yj_ ) = Cov( _Yj, Yi_ ).

The following formulae are very important:

1. E( _AY_ + _c_ ) = _A_ E( _Y_ )+ _c_ for every deterministic matrix _A_ and every deterministic vector _c_ .

2. Cov( _AY_ + _c_ ) = _A_ Cov( _Y_ ) _A_<sup>_T_</sup> for every deterministic matrix _A_ and every deterministic vector _c_ .

As a consequence of the second formula above, we get


Given two random vectors _Y_ ( _p ×_ 1) and _W_ ( _q ×_ 1), we use Cov( _Y, W_ ) to denote the _p × q_ matrix whose ( _i, j_ )<sup>_th_</sup> entry equals the covariance Cov( _Yi, Wj_ ) between _Yi_ and _Wj_ . With this definition, the previous notion of Cov( _Y_ ) equals simply Cov( _Y, Y_ ). It can be checked that


### **3.2 Covariance Recursion in** _AR_ ( _p_ )

We shall set up a recursion for the covariance matrices:


The ( _i, j_ )<sup>_th_</sup> entry of Γ _k_ ( _θ_ ) is


The diagonal entries of Γ _k_ ( _θ_ ) equal _V_ 1( _θ_ ) _, . . . , Vk_ ( _θ_ ).

To initialize the recursion for Γ _k_ ( _θ_ ), note that


We now relate Γ _k_ +1( _θ_ ) to Γ _k_ ( _θ_ ) to establish the recursion. We can write


where


5

_Vk_ ( _θ_ ) = var ( _yn_ + _k | θ, y_ 1 _, . . . , yn_ ) _._

and, as before,

We compute _γ_ ˆ _k_ 1 as


where, for _i_ = 1 _, . . . , k −_ 1,


Thus if _a_ is the ( _k −_ 1) _×_ 1 vector with entries _a_ 1 _, . . . , ak−_ 1, we have


Further


The equation for obtaining Γ _k_ ( _θ_ ) from Γ _k−_ 1( _θ_ ) is therefore

The algorithm for calculating the variances _Vi_ ( _θ_ ) for _i_ = 1 _,_ 2 _, . . . , K_ is thus given by

6

1. Initialize with Γ1( _θ_ ) = _V_ 1( _θ_ ) = _σ_<sup>2</sup> .

2. For _k_ = 2 _,_ 3 _, . . . , K_ , repeat the following

   - a) Form the ( _k −_ 1) _×_ 1 vector _a_ whose _i_<sup>_th_</sup> entry is _ϕk−i_ if _k − p ≤ i ≤ k −_ 1 and 0 otherwise.

   - b) Calculate Γ _k_ ( _θ_ ) using Γ _k−_ 1( _θ_ ) and _a_ by the formula given above.

3. The variances _Vi_ ( _θ_ ) _, i_ = 1 _,_ 2 _, . . . , K_ are given by the diagonal entries of the matrix Γ _K_ ( _θ_ ).

Because _θ_ is unknown, in practice, we run this recursion with _θ_ replaced by its conditional MLE _θ_<sup>ˆ</sup> . The prediction standard errors are then the square roots of _Vi_ ( _θ_<sup>ˆ</sup> ). These prediction errors coincide with those given by the `get prediction` function in `statsmodels` .

7

---

[← 2 Predictions from AR ( p ) models](02-2-predictions-from-ar-p-models.md) · [Up: contents](index.md)
