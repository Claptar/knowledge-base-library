---
title: 5 Lecture Five
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Lecture Five

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We start today with the problem of fitting state space models to observed time series data. This is the main topic of the class. We shall denote the observed time series data by _y_ 0 _, y_ 1 _, . . . , yT_ (note that the number of observations is _T_ + 1). We shall assume that the observations are realizations of random variables _Y_ 0 _, Y_ 1 _, . . . , YT_ . State space models describe the distribution of _Y_ 0 _, . . . , YT_ in terms of a hidden set of state random variables _X_ 0 _, . . . , XT_ . The joint density of _X_ 0 _, . . . , XT , Y_ 0 _, . . . , YT_ is given by


As we have seen previously, this means that _X_ 0 _, . . . , XT_ is Markov, and also that _Y_ 0 _, . . . , YT_ are independent conditional on _X_ 0 = _x_ 0 _, . . . , XT_ = _xT_ with


Often, in actual specifications of state space models, the description of the conditional densities _fX_ 0 _, fXt|Xt−_ 1 _, fYt|Xt_ depends on additional unknown parameters _θ_ (for example, in the local level model, _θ_ = ( _ση_<sup>2</sup><sup>_, σ_</sup> _ϵ_<sup>2) where</sup><sup>_σ_</sup> _η_<sup>2and</sup><sup>_σ_</sup> _ϵ_<sup>2are the state and observation error variances).</sup> We shall follow the full Bayesian approach in the treatment of these nuisance parameters _θ_ . Specifically, we shall assume that they are random and employ a (usually diffuse) prior density _fθ_ ( _·_ ). From now on, we shall explicitly acknowledge that _fX_ 0 _, fXt|Xt−_ 1 _, fYt|Xt_ depend on _θ_ by using the notation:


Our main goal is to fit the state space model to the observed data _y_ 0 _, . . . , yT_ . Fitting a model in the Bayesian context means computing the conditional distribution of the unknown parameters of the model given the observed data _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ . For the state space model, the unknown parameters are _X_ 0 _, . . . , XT_ as well as _θ_ . The conditional distribution of _X_ 0 _, . . . , XT , θ_ given the observed data _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ equals


With the normalizing constant,


21

This is a high-dimensional density which, in principle, answers any inferential question about the unknown parameters _X_ 0 _, . . . , XT , θ_ based on the data _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ . In practice, the quantities of main interest would be the conditional densities of each individual state conditioned on the data _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ :


In principle it is possible to deduce


from the full posterior (23). But a naive way of doing this would involve high dimensional integration that would not be computationally feasible. We shall study principled computationally feasible algorithms for obtaining (24) for _t_ = 0 _, . . . , T_ . I will give a high level overview of the main ideas in this class and we shall study full details in the coming classes. The first step is to write (24) as


This implies that the task of calculating (24) can be broken down into the following two subtasks:

1. Calculate _fXt|Y_ 0= _y_ 0 _,...,YT_ = _yT ,θ_ ( _xt_ ). This is the conditional density of _Xt_ given the entire data as well as _θ_ .

2. Calculate _fθ|Y_ 0= _y_ 0 _,...,YT_ = _yT_ ( _θ_ ). This is the conditional density of _θ_ given the entire data. This can be done via calculating the likelihood _fY_ 0 _,...,YT |θ_ ( _y_ 0 _, . . . , yT_ ) because, by Bayes rule,


It is convenient here to introduce some standard terminology. The conditional distributions:


are called **smoothing distributions** . Thus, the conditional densities (24) can be determined from the smoothing distributions as well as the likelihood _fY_ 0 _,...,YT |θ_ ( _y_ 0 _, . . . , yT_ ).

### **5.1 Outline of Approach to Calculate Smoothing Distributions**

The approach that we will use for efficiently calculating all the smoothing distributions i.e., all the conditional distributions (25) for _t_ = 0 _,_ 1 _, . . . , T_ is the following. This is a sequential approach that has the following two steps:

1. The first step calculates the distributions:


for each _t_ = 0 _,_ 1 _, . . . , T_ . Note that the conditioning above is on _Y_ 0 _, . . . , Yt_ and not on the whole data _Y_ 0 _, . . . , YT_ . These conditional distributions are known as **Filtering Distributions** and algorithms for calculating them are called **Filtering Algorithms** . We shall study the standard filtering algorithms: Kalman filter (for Linear Gaussian State Space Models) and Partile filter (for arbitrary state space models). These algorithms calculate the filtering densities recursively starting from _t_ = 0 and then for _t_ = 1 _, . . . , T_ .

22

2. After the filtering step, the last smoothing distribution:

_XT | Y_ 0 = _y_ 0 _, Y_ 1 = _y_ 1 _, . . . , YT_ = _yT , θ_

is already available. From here, the idea is to calculate the rest of the smoothing distributions (25) recursively for _t_ = _T −_ 1 _, T −_ 2 _, . . . ,_ 0. Note that this is a backward recursion.

This overall approach to calculating the smoothing distributions is known as FFBS (Forward Filtering and Backward Smoothing). We shall study this approach in the case of general state space models. For the special case of linear Gaussian state space models, these recursions can be solved in closed form.

### **5.2 Linear Gaussian State Space Models**

A state space model is specified by the densities _fX_ 0 _|θ_ ( _x_ 0), _fXt|Xt−_ 1= _xt−_ 1 _,θ_ ( _xt_ ) for _t_ = 1 _, . . . , T_ and _fYt|Xt_ = _xt_ ( _yt_ ) for _t_ = 0 _, . . . , T_ . We say that a state space model is **Linear Gaussian** if the following three conditions are all satisfied:

1. _fX_ 0 _|θ_ ( _·_ ) is a Gaussian density.

2. _fXt|Xt−_ 1= _xt−_ 1( _·_ ) is a Gaussian density whose mean is a linear function of _xt−_ 1 and whose covariance does not depend on _xt−_ 1.

3. _fYt|Xt_ = _xt_ ( _·_ ) is a Gaussian density whose mean is a linear function of _xt_ and whose covariance does not depend on _xt_ .

Quite often, linear Gaussian state space models are specified as:


where _X_ 0 _, U_ 1 _, . . . , UT , V_ 0 _, . . . , VT_ are independent with


It is easy to see that this specification satisfies the three conditions of the Linear Gaussian State Space Model. The quantities Σ0 _, At, Bt,_ Σ _t, Rt_ all potentially depend on unknown parameters _θ_ .

For the linear Gaussian state space model, all the filtering and smoothing distributions turn out to be Gaussian which means that they are specified by means and covariances. The general approach for filtering and smoothing can be specialized to this case as recursions in terms of means and covariances. This leads to the Kalman Filter and Kalman Smoother algorithms. We shall start our study of these in the next class.

### **5.3 Recommended Reading for Today**

1. Definitions of filtering and smoothing distributions and the general problem of Sequential Analysis of State Space Models is described in Section 2.3 of the ChopinPapaspiliopoulos book.

2. Chapter 1 of the S¨arkk¨a book also describes the main goals in the analysis of state space models and gives a list of the common Filtering and Smoothing algorithms.

23

---

[← 4 Lecture Four](05-4-lecture-four.md) · [Up: contents](index.md) · [6 Lecture Six →](07-6-lecture-six.md)
