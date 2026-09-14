---
title: 17 Lecture Seventeen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 17 Lecture Seventeen

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **17.1 Recap: Bootstrap Particle Filter**

In the last class, we studied the Bootstrap Particle Filter Algorithm for solving the filtering problem via Monte Carlo in general sequential state space models.


The algorithm proceeds sequentially. At time _t−_ 1, one has access to the samples _Xt_<sup>(1)</sup> _−_ 1<sup>_, . . . , X_</sup> _t_<sup>(</sup> _−_<sup>_N_</sup> 1<sup>)</sup> satisfying (108) for _t −_ 1 and using these, one generates the samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> by following the three steps given below.

1. **Generation** : For each _i_ = 1 _, . . . , N_ , generate independent samples:


To execute this step, we need to be able to simulate from the state transition density _fXt|Xt−_ 1= _xt−_ 1.

2. **Weights** : For each _i_ = 1 _, . . . , N_ , compute


Normalize these weights so they sum to one:


To execute this step, we need to be able to evaluate the conditional density _fYt|Xt_ = _xt_ ( _yt_ ).

3. **Resampling** : Generate


79

This algorithm is initialized by taking


and then following the steps 2 (weights) and 3 (resampling) above to generate _X_ 0<sup>(1)</sup><sup>_, . . . , X_</sup> 0<sup>(</sup><sup>_N_)</sup> . One can then repeat the recursion for _t_ = 1 _,_ 2 _,_ 3 _, . . ._ . This is similar to the Kalman Filter initialization.

The algorithm also allows computation of the likelihood _fY_ 0 _,...,YT |θ_ ( _y_ 0 _, . . . , yT_ ) as:


### **17.2 Unique Values and Particle Degeneracy**

It is clear from the description of the algorithm that the samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> output by the Bootstrap Particle Filter are actually sampled from the discrete distribution:


An immediate implication of this is that _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> will not all be distinct and there will be repeats among them. A useful diagnostic here is the number of unique values _Nt_ among _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> . If _Nt_ is particularly small for some _t_ , the Monte Carlo approximation (108) will not be accurate. If _Nt_ is small for some time indices _t_ , then one says that the particle filter algorithm suffers from the problem of _Particle Degeneracy_ .

The Bootstrap particle filter can suffer from particle degeneracy. To understand when this problem is particularly serious, observe first that, in the generation step, _X_<sup>˜</sup> _t_<sup>(1)</sup> _, . . . , X_<sup>˜</sup> _t_<sup>(</sup><sup>_N_)</sup> can be seen as i.i.d samples from the one-step ahead prediction density:


The two densities in play here are the proposal density given by _fXt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ and the target density given by _fXt|Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ . The algorithm will not work well if these two densities are far from each other. Specifically, particle degeneracy occurs if the target density _fXt|Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ ( _xt_ ) is quite small when _xt_ belongs to the high-density regions of the proposal density _fXt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _xt_ ). Note that the only difference between the proposal and target densities is the additional conditioning on _Yt_ = _yt_ in the target density. Thus the proposal and target densities will be different if _Yt_ provides significantly more and different information about _Xt_ beyond that already provided by _Y_ 0 _, . . . , Yt−_ 1. This tends to happen, for example, if the observation model relating _Yt_ to _Xt_ has small errors. For example, in the local level model _Yt_ = _Xt_ + _ϵt_ , if _ϵt_ is small (e.g., when _σϵ_ is small), then _Yt_ is quite informative for _Xt_ and, in such situations, the bootstrap particle filter algorithm suffers from particle degeneracy.

80

This also tends to happen for _t_ = 0 when the proposal density is _fX_ 0 _|θ_ and the target density is _fX_ 0 _|Y_ 0= _y_ 0 _,θ_ . The proposal density is usually quite diffuse and the target density is relatively informative leading to small weights for most of the samples (and, consequently, small _N_ 0).

In such situations where _Yt_ is quite informative about _Xt_ , a natural fix is to change the proposal distribution by including information on _Yt_ . This is the idea underlying the Guided Particle Filter Algorithm.

### **17.3 The Guided Particle Filter Algorithm**

The guided particle filter algorithm uses more general proposal distributions. For each time point _t ≥_ 0, each value _x_ in the space of the hidden variables _{Xt}_ , and each value _y_ in the space of the observation variables _{Yt}_ , let


be an arbitrary density. The general algorithm described below works for any such set of densities _qt_ ( _· | x, y, θ_ ). The only requirement is that it should be possible simulate from this density. This general algorithm is known as the guided particle filter algorithm and an alternative name for the same algorithm is the _Sequential Importance Resampling_ (SIR) algorithm. In order to apply this algorithm in an actual problem, it is necessary to specify _qt_ ( _· | x, y, θ_ ). For this, two choices are commonly used:

1. _qt_ ( _u | x, y, θ_ ) := _fXt|Xt−_ 1= _x,θ_ ( _u_ ). The following algorithm for this choice of _qt_ reduces to the Bootstrap Particle Filter algorithm. Therefore the SIR algorithm is a generalization of the Bootstrap Particle Filter. Note that this choice of _qt_ ( _· |, x, y, θ_ ) does not depend on _y_ (it only depends on _x_ ).

2. _qt_ ( _u, | x, y, θ_ ) := _fXt|Xt−_ 1= _x,Yt_ = _y,θ_ ( _u_ ). This is commonly used as an alternative to the Bootstrap particle filter when the latter suffers from particle degeneracy. The use of this density in the SIR algorithm requires one to be able to simulate from the conditional density of _Xt_ given _Xt−_ 1 = _x, Yt_ = _y, θ_ .

The following is the SIR algorithm. As the Bootstrap particle filter algorithm, the goal is to output, for each _t ≥_ 0, samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> such that

Unif _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> _≈ Xt | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ._ (110) � � The algorithm proceeds sequentially. At time _t−_ 1, one has access to the samples _Xt_<sup>(1)</sup> _−_ 1<sup>_, . . . , X_</sup> _t_<sup>(</sup> _−_<sup>_N_</sup> 1<sup>)</sup> satisfying (114) for _t −_ 1 and using these, one generates the samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> by following the three steps given below.

1. **Generation** : For each _i_ = 1 _, . . . , N_ , generate independent samples:


To execute this step, we obviously need to be able to simulate from _q_ ( _· | x_ = _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>_, y_=</sup> _yt_ ).

2. **Weights** : For each _i_ = 1 _, . . . , N_ , compute


81

Normalize these weights so they sum to one:


To execute this step, we need to be able to evaluate _fXt|Xt−_ 1= _xt−_ 1( _xt_ ) and _fYt|Xt_ = _xt_ ( _yt_ ).

3. **Resampling** : Generate


This algorithm is initialized by taking


and then repeating the three steps described above for _t_ = 1 _,_ 2 _, . . ._ .

The justification for the weights (115) is as follows. Note first that ( _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>_,X_˜</sup> _t_<sup>(</sup><sup>_i_))for</sup><sup>_i_=</sup> 1 _, . . . , N_ are i.i.d samples from the joint density:


The target should have, as its second marginal, the filtering density at time _t_ . This suggests the target density:


The importance weights will then be given by


with _xt−_ 1 = _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>and</sup><sup>_xt_=</sup><sup>_X_˜</sup> _t_<sup>(</sup><sup>_i_).The above expression can be simplified using Bayes rule as</sup>


As a result, we can view the weights in the SIR algorithm as the weights given by (112) with _c_ = _fYt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _yt_ ). This justifies the choice of weights in the SIR algorithm. Note also that because _c_ = _fYt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _yt_ ), the average of the unnormalized weights provides an approximation of _fYt|Y_ 0= _y_ 0 _,...,Yt−_ 1= _yt−_ 1 _,θ_ ( _yt_ ):


The product of these averages for _t_ = 1 _, . . . , T_ (additionally multiplied by _fY_ 0( _y_ 0)) gives an approximation for the likelihood.

82

### **17.4 Weights when** _qt_ ( _u | x, y, θ_ ) := _fXt|Xt−_ 1= _x,Yt_ = _y,θ_ ( _u_ )

As already remarked, the two most common choices of _qt_ in the SIR algorithm are _qt_ ( _u | x, y, θ_ ) = _fXt|Xt−_ 1= _x_ ( _u_ ) (which corresponds to the bootstrap filter) and _qt_ ( _u | x, y, θ_ ) = _fXt|Xt−_ 1= _x,Yt_ = _y_ ( _u_ ). The weights for the latter choice can be simplified (using Bayes rule in the denominator) as:


In other words, the weight corresponding to ( _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>_,X_˜</sup> _t_<sup>(</sup><sup>_i_))forSIRwith</sup><sup>_qt_(</sup><sup>_u|x, y, θ_)=</sup> _fXt|Xt−_ 1= _x,Yt_ = _y_ ( _u_ ) is given by

_wt_<sup>(</sup><sup>_i_)</sup> = _fYt|Xt−_ 1= _Xt_ ( _−i_ )1<sup>_,θ_(</sup><sup>_yt_)</sup><sup>_._</sup> It is interesting to contrast this weight with the weight _fYt|Xt_ = ˜ _Xt_<sup>(</sup><sup>_i_)</sup> _,θ_<sup>(</sup><sup>_yt_) used in the bootstrap</sup> particle filter.

### **17.5 Example: Local Level Model**

As already remarked, the bootstrap particle filter is widely applicable because, in order to use it, one only needs to be able to simulate from the state transition density _fXt|Xt−_ 1= _xt−_ 1 and be able to compute the density _fYt|Xt_ = _xt_ ( _yt_ ). On the other hand, in order to apply the Guided Particle Filter algorithm with


one should be able to simulate from _fXt|Xt−_ 1= _x,Yt_ = _y,θ_ and evaluate _fYt|Xt−_ 1= _xt−_ 1( _yt_ ). While this may not always possible, here is a simple setting where the method can be easily applied. This is the case of the local level model:

_X_ 0 _∼ N_ (0 _, C_ ) _Xt_ = _Xt−_ 1 + _Zt Yt_ = _Xt_ + _ϵt_ i.i.d i.i.d where _X_ 0 _, Z_ 1 _, Z_ 2 _, . . . , ϵ_ 0 _, ϵ_ 1 _, . . ._ are independent with _Zt ∼ N_ (0 _, σZ_<sup>2)and</sup><sup>_ϵt_</sup> _∼ N_ (0 _, σϵ_<sup>2).</sup> For this model, we have _Xt | Xt−_ 1 = _xt−_ 1 _, θ ∼ N_ ( _xt−_ 1 _, σZ_<sup>2)</sup> and _Yt | Xt_ = _xt, Xt−_ 1 = _xt−_ 1 _, θ ∼ N_ ( _xt, σϵ_<sup>2)</sup>

from which it readily follows that


Thus the Guided Particle Filter Algorithm with (113) is feasible in this case and the generation step simulates observations as:


83

We also have


so that the weights are computed as


where _φ_ ( _y_ ; _µ, σ_<sup>2</sup> ) denotes the normal density with mean _µ_ and variance _σ_<sup>2</sup> evaluated at _y_ . Initialization is done by generating observations from the distribution:


It can easily be seen (in simulations) that when _σϵ_<sup>2issmall,thebootstrapparticlefilter</sup> suffers from particle degeneracy. The performance of the guided particle filter with (113) is much better.

### **17.6 Recommended Reading for Today**

1. Good references for the SIR or Guided Particle Filter algorithms are:

   - a) Section 5.1 of the Petris-Petrone-Campagnoli book

   - b) Section 7.4 of the S¨arkk¨a book

   - c) Section 6.7.3 of the Triantafyllopoulos book

   - d) Sections 10.3.1 and 10.3.2 of the Chopin-Papaspiliopoulos (they derive these algorithms from a slightly more general viewpoint involving Feynman-Kac models which are described in Chapter 5 of their book)

---

[← 16 Lecture Sixteen](17-16-lecture-sixteen.md) · [Up: contents](index.md) · [18 Lecture Eighteen →](19-18-lecture-eighteen.md)
