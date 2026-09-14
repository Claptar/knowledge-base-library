---
title: 3 Prediction Uncertainty
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEighteen153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureEighteen153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Prediction Uncertainty

**Source:** [`LectureEighteen153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureEighteen153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall next discuss how to provide uncertainty quantification for predictions given by the _AR_ ( _p_ ) model. This can be done via the variance of the future observations given the data. Specifically by


and the corresponding standard deviations. We approximate these conditional variances as (below we write “data” for _y_ 1 _, . . . , yn_ )


The second term above is generally small. This is because E ( _yn_ + _i | θ,_ data) is a function of _θ_ and then we take the expectation of _θ_ with respect to the posterior distribution. Because the posterior distribution is usually quite concentrated, the variance will be small. We shall thus ignore the second term and write


To calculate this, the main task is to compute


It turns that it is difficult to directly setup a recursion for _Vi_ ( _θ_ ). Instead, we will get the recursion by working with the conditional **covariance matrices** of _Yn_ +1 _, . . . , Yn_ + _k_ (given _θ_ and the data) for _k_ = 1 _,_ 2 _, . . ._ . Let us first review some basic formulae for covariance matrices.

4

### **3.1 Covariance Matrices**

A finite number of random variables can be viewed together as a random vector. More precisely, a random vector is a vector whose entries are random variables. Let _Y_ = ( _Y_ 1 _, . . . , Yn_ )<sup>_T_</sup> be an _n ×_ 1 random vector. Its Expectation E _Y_ is defined as a vector whose _i_ th entry is the expectation of _Yi_ i.e., E _Y_ = (E _Y_ 1 _,_ E _Y_ 2 _, . . . ,_ E _Yn_ )<sup>_T_</sup> . The covariance matrix of _Y_ , denoted by Cov( _Y_ ), is an _n × n_ matrix whose ( _i, j_ )th entry is the covariance between _Yi_ and _Yj_ . Two important but easy facts about Cov( _Y_ ) are:

1. The diagonal entries of Cov( _Y_ ) are the variances of _Y_ 1 _, . . . , Yn_ . More specifically the ( _i, i_ )th entry of the matrix Cov( _Y_ ) equals _var_ ( _Yi_ ).

2. Cov( _Y_ ) is a symmetric matrix i.e., the ( _i, j_ )th entry of Cov( _Y_ ) equals the ( _j, i_ ) entry. This follows because Cov( _Yi, Yj_ ) = Cov( _Yj, Yi_ ).

The following formulae are very important:

1. E( _AY_ + _c_ ) = _A_ E( _Y_ )+ _c_ for every deterministic matrix _A_ and every deterministic vector _c_ .

2. Cov( _AY_ + _c_ ) = _A_ Cov( _Y_ ) _A_<sup>_T_</sup> for every deterministic matrix _A_ and every deterministic vector _c_ .

As a consequence of the second formula above, we get


Given two random vectors _Y_ ( _p ×_ 1) and _W_ ( _q ×_ 1), we use Cov( _Y, W_ ) to denote the _p × q_ matrix whose ( _i, j_ )<sup>_th_</sup> entry equals the covariance Cov( _Yi, Wj_ ) between _Yi_ and _Wj_ . With this definition, the previous notion of Cov( _Y_ ) equals simply Cov( _Y, Y_ ). It can be checked that

Cov( _AY_ + _c, BW_ + _d_ ) = _A_ Cov( _Y, W_ ) _B_<sup>_T_</sup> _._

### **3.2 Covariance Recursion for Future Variables in** _AR_ ( _p_ )

We shall set up a recursion for the covariance matrices:


The ( _i, j_ )<sup>_th_</sup> entry of Γ _k_ ( _θ_ ) is


We shall see how to do this in the next lecture.

### **3.3 Optional Additional Reading for Today**

1. For more on fitting _AR_ ( _p_ ) models to data, see Section 3.5 of the book by Shumway and Stoffer titled _Time Series Analysis and its applications_ (Fourth Edition).

2. For more on prediction with AR models, see Section 3.4 of the Shumway-Stoffer book.

5

---

[← 2 Predictions given by AR ( p ) models](02-2-predictions-given-by-ar-p-models.md) · [Up: contents](index.md)
