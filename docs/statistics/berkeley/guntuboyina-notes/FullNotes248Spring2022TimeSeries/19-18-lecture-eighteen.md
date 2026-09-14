---
title: 18 Lecture Eighteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 18 Lecture Eighteen

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **18.1 Sequential Importance Resampling**

In the last class, we looked at the Sequential Importance Resampling (SIR) algorithm (we also used the term “Guided Particle Filter”) which generates, for each _t ≥_ 0, samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> such that


The algorithm proceeds sequentially. At time _t−_ 1, one has access to the samples _Xt_<sup>(1)</sup> _−_ 1<sup>_, . . . , X_</sup> _t_<sup>(</sup> _−_<sup>_N_</sup> 1<sup>)</sup> satisfying (114) for _t −_ 1 and using these, one generates the samples _Xt_<sup>(1)</sup> _, . . . , Xt_<sup>(</sup><sup>_N_)</sup> by following the three steps given below.

1. **Generation** : For each _i_ = 1 _, . . . , N_ , generate independent samples:


To execute this step, we obviously need to be able to simulate from _q_ ( _· | x_ = _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>_, y_=</sup> _yt_ ).

84

2. **Weights** : For each _i_ = 1 _, . . . , N_ , compute


Normalize these weights so they sum to one:


To execute this step, we need to be able to evaluate _fXt|Xt−_ 1= _xt−_ 1( _xt_ ) and _fYt|Xt_ = _xt_ ( _yt_ ).

3. **Resampling** : Generate


This algorithm is initialized by taking


and then repeating the three steps described above for _t_ = 1 _,_ 2 _, . . ._ .

The density _q_ ( _· | xt−_ 1 _, yt_ ) appearing above is often referred to as a proposal density. The SIR algorithm works for pretty much any proposal density (the only requirement is the ability to simulate from it). The two most common choices of the proposal density are:

1. **Bootstrap Particle Filter** : _q_ ( _xt | xt−_ 1 _, yt_ ) = _fXt|Xt−_ 1= _xt−_ 1( _xt_ ). Note that this choice of _q_ does not depend on _yt_ . The weights corresponding to this proposal are _fYt|Xt_ = _xt_ ( _yt_ ) i.e., _wt_<sup>(</sup><sup>_i_)</sup> = _fYt|Xt_ = ˜ _Xt_<sup>(</sup><sup>_i_)(</sup><sup>_yt_).</sup>

2. **“Optimal” Guided Particle Filter** : _q_ ( _xt | xt−_ 1 _, yt_ ) = _fXt|Xt−_ 1= _xt−_ 1 _,Yt_ = _yt_ ( _xt_ ). This algorithm is only feasible if it is possible to simulate from the conditional density of _Xt_ given _Xt−_ 1 = _xt−_ 1 and _Yt_ = _yt_ . The reason why this choice of _q_ for the Guided Particle Filter algorithm is called “optimal” can be found, for example, in Theorem 10.1 of the Chopin-Papaspiliopoulos book. We shall not make any use of this optimality criterion. The weights corresponding to this proposal are _fYt|Xt−_ 1= _xt−_ 1( _yt_ ) i.e., _wt_<sup>(</sup><sup>_i_)</sup> = _fYt|Xt−_ 1= _Xt_ ( _−i_ )1<sup>(</sup><sup>_yt_).Notethattheseweightsdonotdependontheparticles</sup>

_X_ ˜ _t_<sup>(</sup><sup>_i_)</sup> generated in this iterate of the algorithm.

The second algorithm above (optimal guided particle filter) usually suffers from less particle degeneracy compared to the Bootstrap particle filter because the function


is less concentrated compared to the function


### **18.2 Example: Local Level Model with non-Gaussian evolution errors**

Consider the local level model:


85

This model can be used to model trend functions that are piecewise constant. The parameter _α_ and the variance _σ_ 0<sup>2willbothbesmallinsuchapplications.</sup>

The Kalman filter is obviously not applicable here as the evolution error is non-Gaussian. The bootstrap filter algorithm is quite easy to implement: in the generation step, the challenge is to simulate


for _xt−_ 1 = _Xt_<sup>(</sup> _−_<sup>_i_)</sup> 1<sup>.ThisisamixtureofGaussiandistributions.Onecansimulatefromthis</sup> mixture by first simulating a Bernoulli random variable _B_ with success probability _α_ . If _α_ = 1, then one would simulate _x_ ˜ _t_ from _N_ ( _xt−_ 1 _, σa_<sup>2)andif</sup><sup>_α_=1,thenonewouldsimulate</sup> _x_ ˜ _t_ from _N_ ( _xt−_ 1 _, σ_ 0<sup>2).Theweightsaregivenby</sup>


where _φ_ ( _x_ ; _µ, σ_<sup>2</sup> ) stands for the normal density with mean _µ_ and variance _σ_<sup>2</sup> . Note that if _yt_ is far from _x_ ˜ _t_ and _σϵ_ is relatively small, then there will be particle degeneracy. Also note that, when the parameters _α_ and _σ_ 0<sup>2aresmall,most((1</sup><sup>_−α_)fraction)ofthegenerated</sup> observations _x_ ˜ _t_ will be close to _xt−_ 1.

Now let us consider applying the optimal guided particle filter for this model. Particle generation will have to be done from the conditional density _fXt|Xt−_ 1= _xt−_ 1 _,Yt_ = _yt_ . By Bayes rule:


We now use the following elementary identity (which can be proved by direct calculation): For every _θ, x, µ ∈_ ( _−∞, ∞_ ) and _τ, σ >_ 0, we have


We get


The integral of the right hand side above with respect to _xt_ is


As a result


86

This is just a mixture of two normal distributions so one can simulate observations from it by first generating a Bernoulli random variable _B_ with success probability:


If _B_ = 1, one simulates from

and if _B_ = 0, one simulates from


Finally note that


which is useful for weight calculation. Note that, as a function of _xt−_ 1, the right hand side above is more diffuse compared to the weight function in the Bootstrap filter (116). This implies that, in this example, the optimal guided particle filter suffers from less particle degeneracy compared to the Bootstrap particle filter.

It should be noted that it is not always possible to implement the optimal guided particle filter in closed form (as in the above example). For example, consider the local level model again where the _N_ (0 _, σa_<sup>2)distributionintheevolutionerrorisreplacedbythestandard</sup> Cauchy distribution:


where _C_ (0 _,_ 1) denotes the standard Cauchy distribution with density proportional to (1 + _x_<sup>2</sup> )<sup>_−_1</sup> . In this case, _fXt|Xt−_ 1= _xt−_ 1 _,Yt_ = _yt_ is given by


where _γ_ ( _xt_ ; _xt−_ 1) is the density of a Cauchy random variable centered at _xt−_ 1 (and scale parameter equal to 1):


Using the fact (117), we obtain


Letting


87

we can write


The integral of the right hand side above with respect to _xt_ equals

so that

The density function _y �→ V_ ( _y_ ; _µ, σ_<sup>2</sup> ) is known as the Voigt profile (see `https://en. wikipedia.org/wiki/Voigt_profile` ) and efficient algorithms exist for its computation. In order to simulate _x_ ˜ _t_ from the above conditional density, the main challenge is to simulate from the conditional density:


It is not clear if this can be done in closed form. One can use some numerical techniques for this. For example, a straightforward approach is to use discretization: one can discretize the domain and approximate the continuous distribution with density given by (118) by a discrete distribution supported on the discrete set of values. One can then simulate from the discrete distribution.

Note that the filter algorithms can be used for obtaining the likelihood (which is the joint density of _Y_ 0 _, . . . , YT_ given the parameters) which can be used for maximum likelihood estimation of the parameters.

### **18.3 Recommended Reading for Today**

1. Good references for the SIR or Guided Particle Filter algorithms are:

   - a) Section 5.1 of the Petris-Petrone-Campagnoli book

   - b) Section 7.4 of the S¨arkk¨a book

   - c) Section 6.7.3 of the Triantafyllopoulos book

   - d) Sections 10.3.1 and 10.3.2 of the Chopin-Papaspiliopoulos (they derive these algorithms from a slightly more general viewpoint involving Feynman-Kac models which are described in Chapter 5 of their book)

2. The local level model with non-Gaussian errors for estimating piecewise constant trend functions is discussed in Section 15.2.6 of the Kitagawa book, and in Section 8.4 of the Kitagawa-Gersch book.

88

---

[← 17 Lecture Seventeen](18-17-lecture-seventeen.md) · [Up: contents](index.md) · [19 Lecture Nineteen →](20-19-lecture-nineteen.md)
