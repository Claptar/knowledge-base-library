---
title: 1 Lecture One
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Lecture One

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Time series refers to observations collected sequentially in time. One can have univariate time series (where a single observation is collected at each point in time) or multivariate time series (where a bunch of obserations are collected at each point in time). In this class, we shall denote the observed time series by

_y_ 0 _, y_ 1 _, . . . , yT ._

Here _y_ 0 denotes the observed value at the first time point, _y_ 1 denotes the observed value at the second time point etc. Typically the time points where the observations are taken are uniformly spaced but there do exist situations where the time points are not uniformly spaced (if the time points are not uniformly spaced, we shall denote them by _t_ 0 _, t_ 1 _, . . . , tT_ and note that the observation _yi_ corresponds to the time _ti_ ).

Time series are commonly analyzed through time series models. These models assume first that the observed time series _y_ 0 _, . . . , yT_ are a realization of random variables _Y_ 0 _, Y_ 1 _, . . . , YT_ , and then proceed to describe the joint distribution of _Y_ 0 _, . . . , YT_ . We shall focus on _State Space Models_ in this class as these are a general class of time series models with wide applicability.

### **1.1 State Space Models**

State space models assume that _{Yt,_ 0 _≤ t ≤ T }_ are noisy measurements of a hidden or latent _Markov process {Xt,_ 0 _≤ t ≤ T }_ .

Here _{Xt,_ 0 _≤ t ≤ T }_ is a Markov process means that the conditional distribution of _Xt_ given _Xt−_ 1 = _xt−_ 1 _, . . . , X_ 0 = _x_ 0 is the same as the conditional distribution of _Xt_ given _Xt−_ 1 = _xt−_ 1 for every 1 _≤ t ≤ T_ and _x_ 0 _, x_ 1 _, . . . , xt_ . We shall denote the density of _X_ 0 by _p_ 0( _·_ ) and the density of _Xt_ given _Xt−_ 1 = _xt−_ 1 by _pt_ ( _xt | xt−_ 1) for _t_ = 1 _, . . . , T_ . _p_ 0 is called the initial distribution of the Markov process _{Xt}_ and _pt_ ( _xt | xt−_ 1) is called the _t_<sup>_th_</sup> transition density. If the transition densities are the same for all _t_ , we say that _{Xt}_ is a time

4

homogeneous Markov process (otherwise, _{Xt}_ is said to be a time inhomogeneous Markov process). Note that the joint density of _X_ 0 _, . . . , XT_ equals


State space models specify that _{Xt,_ 0 _≤ t ≤ T }_ is a Markov process and, additionally, that _Y_ 0 _, . . . , YT_ are independent conditionally on _X_ 0 _, . . . , XT_ and, moreoever, that the conditional distribution of _Yt_ given _X_ 0 = _x_ 0 _, . . . , XT_ = _xT_ is the same as the conditional distribuion of _Yt_ given _Xt_ = _xt_ for each 0 _≤ t ≤ T_ . We shall denote the conditional density of _Yt_ given _Xt_ = _xt_ by _ft_ ( _yt | xt_ ). The conditional joint density of _Y_ 0 _, . . . , YT_ given _X_ 0 = _x_ 0 _, . . . , XT_ = _xT_ equals


To summarize, state space models specify that the joint distribution _X_ 0 _, Y_ 0 _, . . . , XT , YT_ equals


The random variables _X_ 0 _, . . . XT_ are known as state variables (or hidden or latent variables) and _Y_ 0 _, . . . , YT_ are known as data variables. Observe that the joint density of the data variables _Y_ 0 _, . . . , YT_ is given by integrating (1) with respect to _x_ 0 _, . . . , xT_ :


State space models can also be referred to as Hidden Markov Models although some authors use Hidden Markov Models to refer to models where the state variables _Xt_ are discrete random variables.

### **1.2 Examples of State Space Models**

#### **1.2.1 Direct Examples: Tracking**

In tracking problems, the goal is to track the movement of an unknown moving object from noisy measurements _{Yt}_ . Here the state space model directly arises with the state variable _Xt_ representing attributes of the moving object (such as position and velocity). To give a concrete example, consider a body moving in the two-dimensional plane. Suppose we discretize time to a resolution _δ_ (so that the time points are _t_ 0 _, t_ 1 _, . . ._ with _tk_ = _kδ_ ).

Denote the position of the object at time _tk_ by ( _x_ 1 _k, x_ 2 _k_ ) (remember we are assuming that the movement is in the two-dimensional plane). Also let the velocity of the object at time _ti_ is ( _x_ 3 _k, x_ 4 _k_ ). If the velocity in the time period [ _tk−_ 1 _, tk_ ] is assumed to be nearly constant, we would have


One can assume these equations to be exact (as opposed to approximate) by incorporating error variables:


5

Here _q_ 1 _k, q_ 2 _k_ denote error variables which can be modeled as i.i.d with a normal distribution. Further the assumption that the velocity is nearly constant in the time period [ _tk−_ 1 _, tk_ ] can be written as


These two equations can also be assumed to be exact by incorporating error variables:


If we therefore let


denote the position and velocities of the unknown object, then _Xk_ satisfies the equation


If we assume that _qk_ are i.i.d, then it is easy to check that _{Xk}_ is a Markov process.

The observation _Yk_ here is a noisy measurement of _Xk_ . The exact relationship between _Yk_ and _Xk_ depends on the nature of the measurements. Suppose that we are obtaining noisy measurements only of the position of the object. Then


Suppose we assume that _ϵk_ = are i.i.d and also that the two error sequences _{ϵk}_ and � _ϵϵ_ 21 _kk_ � _{qk}_ are independent. Then this represents a state space model (it turns out that this is a linear Gaussian state space model as will be clear soon).

In another measurement model, we could only be measuring the angle that the unknown object makes with the positive _x_ -axis (this is sometimes known as bearings-only tracking). Here we would have


This is again a state-space model (this is a nonlinear state space model).

#### **1.2.2 Trend Estimation**

State space models can be used to estimate trend in state space models. Trend in a time series can be generally understood as a smooth function that tracks well the evolution or course of the time series. One way of estimating a smooth trend is via the following state space model. As usual, we let _Y_ 0 _, . . . , YT_ to be the data random variables. The idea is that the hidden state variables _X_ 0 _, . . . , XT_ represent the trend. Because trend is supposed to be smooth, we assume that


6

This equation says that _Xt_ is centered around _Xt−_ 1 with an error whose size is controlled by _ση_ . If _ση_ is small, then _Xt ≈ Xt−_ 1 representing a smooth trend. Note that (2) clearly implies that _{Xt}_ is a Markov process.

The data variables _Yt_ are connected to the state variables _Xt_ via


This equation captures the intuition that the trend _Xt_ tracks the time series _Yt_ .

The noise parameters _ση_ and _σϵ_ control the twin objectives of smooth trend and tracking the data respectively. If _ση_ is small, we would get smoother trends while if _σϵ_ is small, our trend estimate will closely track the data. Note however if the observed time series _yt_ is not very smooth, then both the objectives cannot be simultaneously achieved. In general, one chooses _ση_ and _σϵ_ so as to obtain the best fit to the data (we shall see all this later).

The state space model given by the pair of equations (2) and (3) is called the local level model. It is a common way of estimating trend in time series.

### **1.3 Recommended Reading for Today**

1. Definition of State Space Models: Sections 2.1 and 2.2 of the Chopin-Papaspiliopoulos book.

2. Tracking application of State Space Models: Section 2.4.1 of the Chopin-Papaspiliopoulos book, and Section 1.3.2 of the Triantafyllopoulos book.

3. Local level model: Section 2.1 of the Durbin-Koopman book, and Section 1.2 of the Triantafyllopoulos book.

---

[← Contents](01-contents.md) · [Up: contents](index.md) · [2 Lecture Two →](03-2-lecture-two.md)
