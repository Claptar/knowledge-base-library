---
title: 13 Lecture Thirteen
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 13 Lecture Thirteen

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall cover the following two topics today:

1. The EM algorithm in the context of the more general MM class of algorithms

2. The Forward Filtering Backward **Sampling** algorithm for sampling from the full posterior of all the states _X_ 0 _, . . . , XT_ given the data _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ and _θ_ .

### **13.1 The MM Algorithm**

The EM algorithm is much easier to understand in the context of a more general class of algorithms called MM. Consider the general problem of maximizing a function _F_ ( _θ_ ) over _θ_ . In this setting, MM stands for Minorize-Maximize (if we are studying the problem of _minimizing F_ ( _θ_ ) as opposed to maximizing, MM would stand for Majorize-Minimize). The MM algorithm for maximizing _F_ ( _θ_ ) over _θ_ is iterative and the update from _θ_<sup>(</sup><sup>_n_)</sup> to _θ_<sup>(</sup><sup>_n_+1)</sup> has the following two steps:

1. Construct a function _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) which minorizes _F_ ( _θ_ ) for every _θ_ and agrees with _F_ ( _θ_ ) at _θ_ = _θ_<sup>(</sup><sup>_n_)</sup> . In other words, _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) must satisfy:


2. Take _θ_<sup>(</sup><sup>_n_+1)</sup> to be the maximizer of _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) over _θ_ .

The most important fact about the MM algorithm is that the objective function increases (or stays the same) when going from _θ_<sup>(</sup><sup>_n_)</sup> to _θ_<sup>(</sup><sup>_n_+1)</sup> :


This can be easily proved via:


Note that the first inequality above follows from the fact that _G_ ( _·, θ_<sup>(</sup><sup>_n_)</sup> ) minorizes _F_ ( _θ_ ), the second inequality follows because _θ_<sup>(</sup><sup>_n_+1)</sup> maximizes _G_ ( _·, θ_<sup>(</sup><sup>_n_)</sup> ) and the third inequality follows because _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) matches _F_ ( _θ_ ) at _θ_ = _θ_<sup>(</sup><sup>_n_)</sup> .

The property (88) is very desirable for a maximization procedure and it is remarkable that the MM algorithm satisfies it without any explicit line search scheme for choosing step sizes.

57

Before seeing why the EM algorithm is a special case of the MM algorithm, let us first look at two simple examples.

**Example 13.1.** _Consider the problem of maximizing the function F_ ( _θ_ ) = cos _θ. The MM algorithm can be used for this in the following way. In order to go from θ_<sup>(</sup><sup>_n_)</sup> _to θ_<sup>(</sup><sup>_n_+1)</sup> _, the first step is to construct G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) _for which we argue as follows. For every θ, we can write_


_for some z that lies between θ and θ_<sup>(</sup><sup>_n_)</sup> _. Thus_


_and thus we take_


_It is easy to see that G_ ( _θ_<sup>(</sup><sup>_n_)</sup> _, θ_<sup>(</sup><sup>_n_)</sup> ) = _F_ ( _θ_<sup>(</sup><sup>_n_)</sup> ) _. Thus G satisfies both the requirements of the first step of the MM algorithm. Further as G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) _is quadratic in θ, it is easy to maximize it over θ to obtain_


_It is an exercise to show that this iterative scheme converges to the true maximizer_ 0 _when initialized anywhere in the open interval_ ( _−π, π_ ) _._

**Example 13.2.** _Given m real numbers y_ 1 _, . . . , ym, consider the problem of maximizing_


_over θ. Any solution of this problem can be termed a median of F . The usual algorithms for computing the median involve sorting the data. MM provides another method for median computation that does not require sorting the data. The key to the MM iterate θ_<sup>(</sup><sup>_n_)</sup> _→ θ_<sup>(</sup><sup>_n_+1)</sup> _is the construction of G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) _. For this, consider the following inequality:_


_where we used the elementary fact: ab ≤_<sup>_<u>a</u>_</sup> 2<sup>2+</sup><sup>_<u>b</u>_</sup> 2<sup>2</sup><sup>_.Wethustake_</sup>


_It is easy to check that G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) _minorizes F_ ( _θ_ ) _(because of_ (89) _) and that G_ ( _θ_<sup>(</sup><sup>_n_)</sup> _, θ_<sup>(</sup><sup>_n_)</sup> ) = _F_ ( _θ_<sup>(</sup><sup>_n_)</sup> ) _. Because G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) _is a quadratic function in θ, it is easy to write down its maximizer (over θ) in closed form:_


58

_This algorithm clearly does not involve sorting the data. One problem with this algorithm is that it does not work when θ_<sup>(</sup><sup>_n_)</sup> _equals yi for some i (note then that wi_<sup>(</sup><sup>_n_)</sup> _equals 0). It is difficult (probably impossible) to construct a quadratic G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) _satisfying our requirements when θ_<sup>(</sup><sup>_n_)</sup> _equals yi for some i. A practical fix is to change the weights w_<sup>(</sup><sup>_n_)</sup> _slightly by adding a small ϵ to the denominator as: w_<sup>(</sup><sup>_n_)</sup> = <u>1</u> _i |yi−θ_<sup>(</sup><sup>_n_)</sup> _|_ + _ϵ_<sup>_._</sup>

It should be clear from the above examples that the most important step for the use of the MM algorithm is the construction of the _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) function. There are some general ideas for this (see the book _MM Optimization Algorithms_ by Kenneth Lange, or chapter 12 in the book _Numerical Analysis for Statisticians_ by Kenneth Lange, or these slides: `https://www.stat.berkeley.edu/~aldous/Colloq/lange-talk.pdf` ).

### **13.2 The EM Algorithm as a special case of MM**

The EM algorithm is a special case of MM corresponding to a special choice of _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) in the latent variable model setting. We shall describe this below. Let us first recall the notion of Kullback-Leibler divergence (also known as Relative Entropy).

#### **13.2.1 The Kullback-Leibler Divergence**

The Kullback-Leibler divergence _D_ ( _p∥q_ ) between two densities _p_ and _q_ is defined as


The most important property of _D_ ( _p∥q_ ) is that it is always nonnegative. This can be proved as a consequence of the elementary inequality:


Because of this inequality:


Another way of proving _D_ ( _p∥q_ ) _≥_ 0 is via the use of the Jensen inequality.

It should also be noted that


This can be argued using the fact that _x_ log _x_ = _x −_ 1 if and only if _x_ = 1.

It is also very important to note that _D_ ( _q∥p_ ) and _D_ ( _p∥q_ ) are in general **not equal** .

59

#### **13.2.2 EM and MM**

We are now ready to explain the connection between the EM and MM algorithms. Consider the latent variable setting where the goal is to maximize the log-likelihood:


There is a latent variable _X_ and the model is specified via the full density _fY,X|θ_ ( _y, x_ ). It is important to note that the conditional density of _X_ given _Y_ = _y_ depends on the value of _θ_ . We shall denote this by _fX|Y_ = _y,θ_ ( _x_ ).

We shall show below that the EM update for _θ_<sup>(</sup><sup>_n_)</sup> _→ θ_<sup>(</sup><sup>_n_+1)</sup> is exactly equal to the MM update corresponding to


Because the Kullback-Leibler divergence is always nonnegative, it is clear that _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) _≤ F_ ( _θ_ ) for every _θ_ . Further, because of (90), _G_ ( _θ_<sup>(</sup><sup>_n_)</sup> _, θ_<sup>(</sup><sup>_n_)</sup> ) = _F_ ( _θ_<sup>(</sup><sup>_n_)</sup> ). Thus _G_ satisfies the conditions required for the first step of the MM algorithm. Note that we can write _G_ alternately as


Recall that the first term on the right hand side above is precisely the function _E_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) that appears in the Expectation Step of the EM algorithm. We have thus proved that


The second term above does not depend on _θ_ . Therefore maximizing _G_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) over _θ_ is equivalent to maximizing _E_ ( _θ, θ_<sup>(</sup><sup>_n_)</sup> ) over _θ_ . This shows that the second steps of the MM algorithm (with _G_ defined in (91)) and the EM algorithm are identical, which completes the proof of the claim that MM (with _G_ in (91)) is exactly the EM algorithm. The EM algorithm is therefore a special case of MM.

### **13.3 Full Smoothing Distribution**

In our discussion of smoothing, we have so far discussion the computation of the marginal distributions:


60

for each _t_ = 0 _, . . . , T_ , as well as the pairwise distributions:


It turns out ideas used for the above calculations can also be used to obtain the full conditional joint density:


for all the states given the observations (and _θ_ ). To see this, first write (below “data” refers to _Y_ 0 = _y_ 0 _, . . . , YT_ = _yT_ )


The Markov property of _{Xt}_ and the conditional independence of _Yt_ given _X_ 0 _, . . . , XT_ imply


This means that _Xs_ = _xs_ for _s > t_ + 1 and _Ys_ = _ys_ for _s > t_ can be dropped from the conditioning. As a result


By the Bayes rule (note that _fXt_ +1 _|Xt_ = _xt,Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ ( _xt_ +1) = _fXt_ +1 _|Xt_ = _xt,θ_ ( _xt_ +1)), we obtain


This is a formula for the full smoothing joint density in terms of the filtering densities.

For linear Gaussian state space models, the conditional density (93) can be computed in closed form (as we saw in Lecture Nine) as:


where Γ _t_ +1 = _Qt|tAt_<sup>_′_</sup> +1<sup>_Q−_</sup> _t_ +1<sup>1</sup> _|t_<sup>.This gives a closed form expression for the full smoothing joint</sup> density.

### **13.4 Forward Filtering Backward SAMPLING**

Suppose we want to generate independent samples


for _i_ = 1 _, . . . , N_ from the conditional distribution (92). This can be done using the formulae from the previous section. For linear Gaussian state space models, we use (94) to obtain the following sampling algorithm. Repeat the following steps for each _i_ = 1 _, . . . , N_ :

> 1. Generate _XT_<sup>(</sup><sup>_i_)</sup> from the filtering distribution at time _T_ i.e., we generate _XT_<sup>(</sup><sup>_i_)</sup> from the _N_ ( _mT |T , QT |T_ ) distribution.

61


Note that this algorithm requires the quantities _mT |T , QT |T , mt|t, Qt|t, mt_ +1 _|t, Qt_ +1 _|t,_ Γ _t_ +1 which are all obtained from the Kalman Filter. Thus, one would need to implement the Kalman Filter before running the sampling algorithm. Note however that this sampling algorithm does not use any output of the usual Kalman Smoother algorithm.

For a general state space model, sampling can be done by discretization (we shall see other approaches later). The first step is to setup a dense grid _x_<sup>(</sup><sup>_g_)</sup> _, g ∈ G_ covering the range of _Xt_ and perform filtering. This will lead to discrete distributions:


which approximate the densities _fXt|Y_ 0= _y_ 0 _,...,Yt_ = _yt,θ_ for each _t_ = 0 _,_ 1 _, . . . , T_ . Then the sampling algorithm to generate _X_ 0<sup>(</sup><sup>_i_)</sup><sup>_, . . . , X_</sup> _T_<sup>(</sup><sup>_i_)</sup> for _i_ = 1 _, . . . , N_ from the conditional distribution (92) is as follows. Repeat the following steps for each _i_ = 1 _, . . . , N_ :

1. Generate _X_<sup>(</sup><sup>_i_)</sup> _T_ from _pT |T_ ( _x_<sup>(</sup><sup>_g_)</sup> ) _, g ∈ G_ (this is the discrete filtering approximation at

time _T_ ).

2. Sequentially for _t_ = _T −_ 1 _, . . . ,_ 0, repeat the following steps:

   - a) Calculate _wg_ := _pt|t_ ( _x_<sup>(</sup><sup>_g_)</sup> ) _fXt_ +1 _|Xt_ = _x_ ( _g_ ) _,θ_ ( _Xt_<sup>(</sup> +1<sup>_i_))for</sup><sup>_g∈G_.</sup>

   - b) Normalize _wg, g ∈ G_ calculated above so they sum to one.

   - c) Generate _Xt_<sup>(</sup><sup>_i_)</sup> from the discrete distribution which gives probability _wg_ to the grid point _x_<sup>(</sup><sup>_g_)</sup> for _g ∈ G_ .

Note again that this algorithm only uses the filtering approximations (95). It is not necessary to calculate smoothing approximations to run this sampling algorithm.

These sampling algorithms for sampling observations from the full conditional distribution of the states given the data (and the parameters _θ_ ) are known as FFBS (Forward Filtering Backward SAMPLING). They should be contrasted with the previous FFBS (Forward Filtering Backward SMOOTHING) algorithms which computed the smoothing densities (exactly or approximately).

### **13.5 Recommended Reading for Today**

1. References for the MM algorithm are the book _MM Optimization Algorithms_ by Kenneth Lange, or chapter 12 in the book _Numerical Analysis for Statisticians_ by Kenneth Lange, or these slides: `https://www.stat.berkeley.edu/~aldous/Colloq/lange-talk. pdf` .

2. For the FFBSampling algorithm, see Section 5.7.2 of the Triantafyllopoulos book or Section 4.4.1 of the Petris-Petrone-Campagnoli book,

62

---

[← 12 Lecture Twelve](13-12-lecture-twelve.md) · [Up: contents](index.md) · [14 Lecture Fourteen →](15-14-lecture-fourteen.md)
