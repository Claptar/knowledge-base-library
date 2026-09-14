---
title: 14 Lecture Fourteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 14 Lecture Fourteen

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall discuss full Bayesian estimation of state space models today. Full Bayesian estimation means that we put a prior on the unknown parameters _θ_ (as opposed to obtaining point estimates for _θ_ and ignoring the uncertainty in their estimation). Let us start by considering the local level model.

### **14.1 Local Level Model**

We have as usual


i.i.d i.i.d with _Zt ∼ N_ (0 _, σZ_<sup>2)and</sup><sup>_ϵt_</sup> _∼ N_ (0 _, σϵ_<sup>2).</sup><sup>_σZ_and</sup><sup>_σϵ_areunknownparametersand</sup><sup>_C_isa</sup> large constant. Previously we obtained maximum likelihood estimates for _σZ_ and _σϵ_ and then went on to obtain smoothing estimates of _X_ 0 _, . . . , XT_ ignoring the uncertainty in estimation of _σZ_ and _σϵ_ . Now we shall place priors on _σZ_ and _σϵ_ . Natural priors on scale parameters reflecting ignorance are:


The full joint density of _θ, X_ 0 _, . . . , XT , Y_ 0 _, . . . , YT_ (here _θ_ = ( _σZ, σϵ_ )) is proportional to


As a result


Often the main interest is in the conditional distribution of _X_ 0 _, . . . , XT_ given _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ and we can obtain this by integrating over the _σZ_ and _σϵ_ . This integration can be done in closed form if we assume that _C_ is large (so that the indicator above can be dropped). We then get


and ignored the Γ( _m/_ 2) terms in proportionality.

63

The posterior density:


can, in principle, be used for all inference on the hidden variables _X_ 0 _, . . . , XT_ given the observed data. The problem is that it does not correspond to any state space model so it is not clear how to derive from it the marginal posterior densities _Xt | Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ in an efficient way. In particular, the Kalman smoother cannot be implemented as this posterior does not correspond to a state space model. As a result, instead of integrating out _θ_ from the joint posterior of _θ, X_ 0 _, . . . , XT_ , the common approach is to obtain samples _θ_<sup>(</sup><sup>_i_)</sup> _, X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_)</sup> for _i_ = 1 _, . . . , N_ from the joint posterior _θ, X_ 0 _, . . . , XT_ . Then _X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_)</sup> for _i_ = 1 _, . . . , N_ can be used for posterior inference on the hidden states given the observed data. Also the samples _θ_<sup>(1)</sup> _, . . . , θ_<sup>(</sup><sup>_N_)</sup> can be used for posterior inference on the parameters _θ_ given the observed data.

For generating the posterior samples _θ_<sup>(</sup><sup>_i_)</sup> _, X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_)</sup> for _i_ = 1 _, . . . , N_ , it is convenient to use the Gibbs sampler algorithm.

### **14.2 Gibbs Sampler**

Suppose we want to approximate a joint distribution _fA,B_ over two random variables _A_ and _B_ . The Gibbs sampler algorithm is applicable in situations where the conditional densities _fA|B_ = _b_ and _fB|A_ = _a_ are easy to simulate from for each value of _a_ and _b_ . The algorithm is as follows:

1. Start with _a_ = _a_<sup>(0)</sup>

2. For each _i_ = 1 _,_ 2 _, . . . , N_ ,


When _N_ is large, this method generates samples ( _a_<sup>(</sup><sup>_i_)</sup> _, b_<sup>(</sup><sup>_i_)</sup> ) for _i_ = 1 _, . . . , N_ having the property that


for many functions _g_ .

### **14.3 Gibbs Sampler for the Local Level Model**

The Gibbs sampler for generating samples _θ_<sup>(</sup><sup>_i_)</sup> _, X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_)</sup> for _i_ = 1 _, . . . , N_ from the full posterior distribution _θ, X_ 0 _, . . . , XT | Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_

works as follows:


64

2. For each _i_ = 1 _, . . . , N_ ,

- a) Generate _X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_)from the conditional joint distribution of</sup><sup>_X_0</sup><sup>_, . . . , XT_given</sup> _θ_ = _θ_<sup>(</sup><sup>_i_)</sup> and _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ . Because we are conditioning on _θ_ = _θ_<sup>(</sup><sup>_i_)</sup> here, these samples are obtained by the FFBSampling algorithm discussed in the last class.

- b) Generate _θ_<sup>(</sup><sup>_i_)</sup> from the conditional distribution of _θ_ given _X_ 0 = _X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, X_1=</sup> _X_ 1<sup>(</sup><sup>_i_)</sup><sup>_, . . . , XT_=</sup><sup>_X_</sup> _T_<sup>(</sup><sup>_i_)</sup> and _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ . The details for doing this are given below.

For the second step above, we need to be able to simuate from the conditional distribution:


and this can be done as follows:


as calculated previously. Thus, conditional on _X_ 0 = _x_ 0 _, . . . , XT_ = _x_ 0 _, Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ , the two parameters _σZ_ and _σϵ_ are independent with


and


By changing the indicators to _I{σZ >_ 0 _}_ and _I{σϵ >_ 0 _}_ (which is justified when _C_ is large), and using the standard change of variable formula, we obtain


and


Thus the second step in the iteration for the Gibbs sampler, we simply generate Gamma random variables _G_<sup>(</sup> _Z_<sup>_i_)and</sup><sup>_G_</sup> _ϵ_<sup>(</sup><sup>_i_)</sup> from the above pair of distributions (with _xt_ = _Xt_<sup>(</sup><sup>_i_))and</sup> then transform them as _σZ_<sup>(</sup><sup>_i_):= 1</sup><sup>_/_</sup> ~~�~~ _G_<sup>(</sup> _Z_<sup>_i_)and</sup><sup>_σ_</sup> _ϵ_<sup>(</sup><sup>_i_)</sup> := 1 _/_ ~~�~~ _G_<sup>(</sup> _ϵ_<sup>_i_).Thus implementing the Gibbs</sup> sampler for the local level model is quite simple.

65

### **14.4 Gibbs sampler for general Linear Gaussian state space models**

The Gibbs sampler algorithm for general Linear Gaussian state space models is basically the same as the one we saw in the last section:

1. Start with _θ_<sup>(0)</sup> .

2. For each _i_ = 1 _, . . . , N_ ,

   - a) Generate _X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_)from the conditional joint distribution of</sup><sup>_X_0</sup><sup>_, . . . , XT_given</sup> _θ_ = _θ_<sup>(</sup><sup>_i_)</sup> and _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ . Because we are conditioning on _θ_ = _θ_<sup>(</sup><sup>_i_)</sup> here, these samples are obtained by the FFBSampling algorithm discussed in the last class.

   - b) Generate _θ_<sup>(</sup><sup>_i_)</sup> from the conditional distribution of _θ_ given _X_ 0 = _X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, X_1=</sup> _X_ 1<sup>(</sup><sup>_i_)</sup><sup>_, . . . , XT_=</sup><sup>_X_</sup> _T_<sup>(</sup><sup>_i_)</sup> and _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ . Unlike the case of the local level model, this step may not always be carried out in closed form. It depends on the specific dependence of the matrices defining the linear Gaussian model on the parameters _θ_ .

### **14.5 Recommended Reading for Today**

1. A general introduction to the Gibbs sampler is in Section 5.7.1 of the Triantafyllopoulos book and in Section 1.6.1 of the Petris-Petrone-Campagnoli book.

2. The Gibbs sampler for the local level model is given in Section 4.4.3 of the PetrisPetrone-Campagnoli book and Section 5.7.3 of the Triantafyllopoulos book.

---

[← 13 Lecture Thirteen](14-13-lecture-thirteen.md) · [Up: contents](index.md) · [15 Lecture Fifteen →](16-15-lecture-fifteen.md)
