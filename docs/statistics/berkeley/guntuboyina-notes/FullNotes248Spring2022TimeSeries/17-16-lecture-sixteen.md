---
title: 16 Lecture Sixteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 16 Lecture Sixteen

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Our next topic is Sequential Monte Carlo methods for general state space models. Here the conditional densities _fXt|Xt−_ 1= _xt−_ 1 _,θ_ ( _·_ ) and _fYt|Xt_ = _xt,θ_ ( _·_ ) (as well as the initial density _fX_ 0)

72

can be arbitrary. We shall first look at the problem of filtering. Recall that filtering can be used for writing down the likelihood (which is necessary for inference of _θ_ ). Filtering will also be necessary for solving the smoothing problem which we shall study later.

Recall that filtering refers to the problem of determining the conditional distributions:


Our approach will be recursive and we shall determine the above distributions sequentially for _t_ = 0 _,_ 1 _,_ 2 _, . . ._ . In Lecture Six, we have seen closed form formulae for obtaining the filtering density at time _t_ using the filtering density at time _t −_ 1. This involved two steps which we termed _one-step ahead prediction update_ and _filtering update_ . The one-step ahead prediction update is the following formula for the density of _Xt_ given _Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ in terms of the density of _Xt−_ 1 given _Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ :


The filtering update is the following formula for the density of _Xt_ given _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ in terms of the density of _Xt_ given _Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1:


Formula (100) can be seen as an application of the Bayes rule with the following choices of “prior” and “likelihood”:


The “posterior” corresponding to the above prior and likelihood is the density of _Xt_ given _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ and is obtained by the Bayes rule leading to the formula (100).

For general state space models, the integral involved in (99) cannot be evaluated in closed form. This would make (100) intractable as well (because (100) needs _fXt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ as input). One approach for dealing with intractibility is to use Monte Carlo which leads to Sequential Monte Carlo methods for state space models. In Monte Carlo methods, the focus is not on evaluating an unknown density _f_ in closed form, and instead, the focus is on obtaining i.i.d samples _X_<sup>(1)</sup> _, . . . , X_<sup>(</sup><sup>_N_)</sup> from _f_ . Once these samples are obtained, the distribution corresponding to the density _f_ is approximated by the discrete uniform distribution on _X_<sup>(1)</sup> _, . . . , X_<sup>(</sup><sup>_N_)</sup> :


In order to evaluate the expectation of a function _g_ with respect to the density _f_ , the Monte Carlo approach will give


### **16.1 Notation for Discrete Distributions**

We shall use the following notation in the sequel. A discrete distribution that takes the values _x_<sup>(1)</sup> _, . . . , x_<sup>(</sup><sup>_N_)</sup> with probabilities _p_<sup>(1)</sup> _, . . . , p_<sup>(</sup><sup>_N_)</sup> will be denoted by


73

For example, the distribution taking the three values 5 _,_ 2 _, −_ 6 with probabilities 0 _._ 3 _,_ 0 _._ 5 _,_ 0 _._ 2 respectively will be written as


Note that the uniform distribution (102) is written as


in this notation.

### **16.2 Monte Carlo versions of** (99) **and** (100)

In terms of Monte Carlo, the basic question underlying filtering is the following:

**Question 16.1.** _Suppose we are given i.i.d samples Xt_<sup>(1)</sup> _−_ 1<sup>_, . . . , X_</sup> _t_<sup>(</sup> _−_<sup>_N_</sup> 1<sup>)</sup><sup>_fromthedistribution_</sup> _Xt−_ 1 _| Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ (this is the filtering distribution at time t −_ 1 _). How then do we generate i.i.d samples Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> _from the distribution Xt | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ (this is the filtering distribution at time t)?_

We shall solve this question by using Monte Carlo versions of (99) and (100). We start with i.i.d samples _Xt_<sup>(1)</sup> _−_ 1<sup>_, . . . , X_</sup> _t_<sup>(</sup> _−_<sup>_N_</sup> 1<sup>)fromthefilteringdensity</sup><sup>_fX_</sup> _t−_ 1<sup>_|Y_</sup> 0<sup>=</sup><sup>_y_</sup> 0<sup>_,...,Y_</sup> _t−_ 1<sup>=</sup><sup>_y_</sup> _t−_ 1<sup>_,θ_attime</sup> _t −_ 1. For the one-step ahead prediction update, we need to obtain samples from the density of _Xt_ given _Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ . This is easily done via:


This makes sense because the right hand side of (99) is simply the marginal density of _Xt_ under the model:


Thus _X_<sup>˜</sup> _t_<sup>(1)</sup> _, . . . , X_<sup>˜</sup> _t_<sup>(</sup><sup>_N_)</sup> are i.i.d samples from the one-step ahead prediction distrbution _Xt | Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ . One can then approximate the one-step ahead prediction distribution by


Let us now come to (100). As noted earlier, this equation arises from the Bayes rule with prior and likelihood given in (101). We do not have access to the prior density _fXt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ as we have not evaulated (99) in closed form. We do, however, have the Monte Carlo approximation (103) for the one-step ahead prediction distribution so it is natural to approximate (100) by applying Bayes rule with


The unnormalized posterior corresponding to the prior and likelihood above is given by the weights:


74

The properly normalized posterior is then given by


This discrete distribution approximates the filtering distribution at time _t_ :


In order to generate i.i.d samples from the filtering distribution at time _t_ , we can simply generate samples from the above discrete distribution:


This algorithm for solving the filtering problem in general state space models using Monte Carlo is called _Bootstrap Particle Filter_ . We stae the algorithm formally in the next section.

### **16.3 The Bootstrap Particle Filter**

For each _t ≥_ 0, this algorithm outputs samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> such that


The algorithm proceeds sequentially. At time _t−_ 1, one has access to the samples _Xt_<sup>(1)</sup> _−_ 1<sup>_, . . . , X_</sup> _t_<sup>(</sup> _−_<sup>_N_</sup> 1<sup>)</sup> and using these, one generates the samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> by following the three steps given below.

1. **Generation** : For each _i_ = 1 _, . . . , N_ , generate independent samples:


To execute this step, we need to be able to simulate from the state transition density _fXt|Xt−_ 1= _xt−_ 1.

2. **Weights** : For each _i_ = 1 _, . . . , N_ , compute


Normalize these weights so they sum to one:


To execute this step, we need to be able to evalute the conditional density _fYt|Xt_ = _xt_ ( _yt_ ) at least up to a constant that does not depend on _xt_ .

3. **Resampling** : Generate


75

This algorithm is initialized by taking


and then following the steps 2 (weights) and 3 (resampling) above to generate _X_ 0<sup>(1)</sup><sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_N_)</sup> . One can then repeat the recursion for _t_ = 1 _,_ 2 _,_ 3 _, . . ._ . This is similar to the way we initialized the Kalman filter.

This algorithm is called the Bootstrap Particle Filter because: (a) Monte-Carlo samples are called particles in the physics literature, (b) The resampling step is reminiscent of the bootstrap procedure in statistics.

The Bootstrap Particle Filter is very simple and easy to implement. It can also be understood from the point of view of Importance Sampling. Before describing this connection to importance sampling, let us briefly recall importance sampling.

### **16.4 Importance Sampling Recalled**

Consider a probability measure _P_ with density _p_ . Suppose we do not know the formula for _p_ exactly but we only know it up to some unknown multiplicative constant factor _c_ . In other words, we know the explicit formula for the function _x �→ cp_ ( _x_ ) but we do not know _c_ and hence we do not know _p_ ( _x_ ) explicitly.

Importance sampling attempts to approximate _P_ using i.i.d samples _X_<sup>˜(1)</sup> _, . . . , X_<sup>˜(</sup><sup>_n_)</sup> drawn from another probability measure _Q_ having density _q_ . The idea is to form weights


and the corresponding normalized weights:


Then the importance sampling approximation for _P_ is


In Lecture 15, we used the terminology “self-normalized” importance sampling for the above estimator of � _gdP_ .

Note that _w_<sup>(1)</sup> _, . . . , w_<sup>(</sup><sup>_N_)</sup> depend on the constant _c_ but the normalized weights _W_<sup>(1)</sup> _, . . . , W_<sup>(</sup><sup>_N_)</sup> don’t. This means that the approximation<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_W_(</sup><sup>_i_)</sup><sup>_δ_</sup> _{X_<sup>˜(</sup><sup>_i_)</sup> _}_<sup>doesnotdependon</sup><sup>_c_.</sup>

It will be helpful to note the following two things before moving on:

1. **Estimating** _c_ : Importance sampling provides the following estimate for the unknown constant _c_ :


76

To see why this estimator makes sense, just note that


2. **Samples from** _P_ : Importance sampling can be used to obtain approximately i.i.d samples from _P_ . Indeed as the importance sampling approximation for _P_ equals � _Ni_ =1<sup>_W_(</sup><sup>_i_)</sup><sup>_δ_</sup> _{X_<sup>˜(</sup><sup>_i_)</sup> _}_<sup>,onecanobtain(approximate)samplesfrom</sup><sup>_P_bysamplingfrom</sup> the discrete distribution<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_W_(</sup><sup>_i_)</sup><sup>_δ_</sup> _{X_<sup>˜(</sup><sup>_i_)</sup> _}_<sup>:</sup>


This method of sample generation is referred to as _Importance Resampling_ because _X_<sup>(1)</sup> _, . . . , X_<sup>(</sup><sup>_N_)</sup> are sampled from _X_<sup>˜(1)</sup> _, . . . , X_<sup>˜(</sup><sup>_N_)</sup> (with weights _W_<sup>(1)</sup> _, . . . , W_<sup>(</sup><sup>_N_)</sup> ) which are themselves sampled from _Q_ .

### **16.5 Bootstrap Particle Filter as Importance Resampling**

The Bootstrap Particle Filter algorithm can be understood from the lens of importance resampling. This generalized view is helpful for the creation of other particle filtering algorithms. There are two (very similar) ways of seeing the connection between the Bootstrap Particle Filter and Importance Resampling.

#### **16.5.1 First Way of Seeing the Connection**

As explained in Section 16.2, the samples _X_<sup>˜</sup> _t_<sup>(1)</sup> _, . . . , X_<sup>˜</sup> _t_<sup>(</sup><sup>_N_)</sup> generated in the first step of the Bootstrap particle filter recursion (from time _t −_ 1 to _t_ ) can be seen as samples from the one-step ahead prediction distribution _Xt | Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ :


If we now apply importance sampling to use these samples to approximate the the filtering distribution at time _t_ : _Xt | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ , we need to use, for some positive constant _c_ , the weights


It is now clear that the Bootstrap Particle Filter uses the above weights for


so that the weights simplify to _fYt|Xt_ = ˜ _Xt_<sup>(</sup><sup>_i_)</sup> _,θ_<sup>(</sup><sup>_yt_).ThereforeeachrecursionoftheBootstrap</sup> Particle Filter can be seen as a version of Importance Resampling.

77

#### **16.5.2 Second Way of Seeing the Connection**

In the first step of the Bootstrap Particle Recursion to go from _t−_ 1 to _t_ , we generate samples _X_ ˜ _t_<sup>(1)</sup> _, . . . , X_<sup>˜</sup> _t_<sup>(</sup><sup>_N_)</sup> independently according to


This means that jointly ( _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>_,X_˜</sup> _t_<sup>(</sup><sup>_i_))</sup><sup>_, i_= 1</sup><sup>_, . . . , N_arei.i.dsamplesfromthejointdensity:</sup>


which is just the density of _Xt−_ 1 _, Xt | Y_ 0 = _y_ 0 _, . . . , Yt−_ 1 = _yt−_ 1 _, θ_ . We can now employ importance sampling to convert these samples into an approximation of the distribution


We would need to use weights (for some constant _c >_ 0)


with _xt−_ 1 = _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>and</sup><sup>_xt_=</sup><sup>_X_˜</sup> _t_<sup>(</sup><sup>_i_).The above expression can be simplified using Bayes rule as</sup>


As a result, we can view the weights in the bootstrap particle filter as the weights given by (107) with _c_ = _fYt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _yt_ ).

### **16.6 Likelihood Approximation from the Bootstrap Particle Filter**

In the previous section, we have seen that the recursion (to go from time _t −_ 1 to time _t_ ) in the Bootstrap Particle Filter can be seen as importance sampling with weights (107) (or equivalently (106)) with _c_ = _fYt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _yt_ ). The observation (105) can therefore be used to deduce that:


for each _t_ = 1 _, . . . , T_ (here _wt_<sup>(</sup><sup>_i_)</sup> is as defined in (109)). One can also similarly argue that


78

The likelihood _fY_ 0 _,...,YT |θ_ ( _y_ 0 _, . . . , yT_ ) can thus be approximated as


In this way, the bootstrap particle filter algorithm directly allows likelihood computation.

### **16.7 Recommended Reading for Today**

1. For the Bootstrap Particle Filter Algorithm, I recommend Section 15.2 of the Kitagawa book (Kitagawa refers to the algorithm as simply _The Monte Carlo Filter_ ).

2. For more details about importance sampling and resampling, I recommend Chapters 8 and 9 of the Chopin-Papaspiliopoulos book.

---

[← 15 Lecture Fifteen](16-15-lecture-fifteen.md) · [Up: contents](index.md) · [17 Lecture Seventeen →](18-17-lecture-seventeen.md)
