---
title: 7 Lecture Seven
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Lecture Seven

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **7.1 Geometric Distribution**

The Geometric distribution is a special case of the Negative Binomial distribution for _k_ = 1. It corresponds to the number of independent tosses (of a coin with probability of heads

36

_p_ ) required to get the first head. Formally, we say that _X_ has the Geometric distribution with parameter _p ∈_ [0 _,_ 1] (written as _X ∼ Geo_ ( _p_ )) if _X_ takes the values 1 _,_ 2 _, . . ._ with the probabilities:


The _Geo_ ( _p_ ) distribution has the interesting property of memorylessness i.e., if _X ∼ Geo_ ( _p_ ), then


This is easy to check as P _{X > m}_ = (1 _− p_ )<sup>_m_</sup> . It is also interesting that the Geometric distribution is the only distribution on _{_ 1 _,_ 2 _, . . . }_ which satisfies the memorylessness property (28). To see this, suppose that _X_ is a random variable satisfying (28) which takes values in _{_ 1 _,_ 2 _, . . . }_ . Let _G_ ( _m_ ) := P _{X > m}_ for _m_ = 1 _,_ 2 _, . . ._ . Then (28) is the same as


This clearly gives _G_ ( _m_ ) = ( _G_ (1))<sup>_m_</sup> for each _m_ = 1 _,_ 2 _, . . ._ . Now _G_ (1) = P _{X >_ 1 _}_ = 1 _−_ P _{X_ = 1 _}_ . If _p_ = P _{X_ = 1 _}_ , then


which means that P _{X_ = _i}_ = P _{X > i −_ 1 _} −_ P _{X > i}_ = _p_ (1 _− p_ )<sup>_i−_1</sup> for every _i ≥_ 1 meaning that _X_ is _Geo_ ( _p_ ).

### **7.2 Poisson Distribution**

A random variable _X_ is said to have the Poisson distribution with parameter _λ >_ 0 (denoted by _Poi_ ( _λ_ )) if _X_ takes the values 0 _,_ 1 _,_ 2 _, . . ._ with pmf given by


The main utility of the Poisson distribution comes from the following fact:

**Fact** : The binomial distribution _Bin_ ( _n, p_ ) is well-approximated by the Poisson distribution _Poi_ ( _np_ ) provided that the quantity _np_<sup>2</sup> is small.

To intuitively see why this is true, just see that


Note now that _np_<sup>2</sup> being small implies that _p_ is small (note that _p_ can be written as ~~�~~ _np_<sup>2</sup> _/n ≤_ ~~�~~ _np_<sup>2</sup> so small _np_<sup>2</sup> will necessarily mean that _p_ is small). When _p_ is small, we can approximate log(1 _− p_ ) as _−p − p_<sup>2</sup> _/_ 2 so we get


Now because _np_<sup>2</sup> is small, we can ignore the second term above to obtain that P _{Bin_ ( _n, p_ ) = 0 _}_ is approximated by exp( _−np_ ) which is precisely equal to P _{Poi_ ( _np_ ) = 0 _}_ . One can similarly approximate P _{Bin_ ( _n, p_ ) = _k}_ by P _{Poi_ ( _np_ ) = _k}_ for every fixed _k_ = 0 _,_ 1 _,_ 2 _, . . ._ .

There is a formal theorem (known as Le Cam’s theorem) which rigorously proves that _Bin_ ( _n, p_ ) _≈ Poi_ ( _np_ ) when _np_<sup>2</sup> is small. This is stated without proof below (its proof is beyond the scope of this class).

37

**Theorem 7.1** (Le Cam’s Theorem) **.** _Suppose X_ 1 _, . . . , Xn are independent random variables such that Xi ∼ Ber_ ( _pi_ ) _for some pi ∈_ [0 _,_ 1] _for i_ = 1 _, . . . , n. Let X_ = _X_ 1 + _· · ·_ + _Xn and λ_ = _p_ 1 + _. . . pn. Then_


In the special case when _p_ 1 = _· · ·_ = _pn_ = _p_ , the above theorem says that


and thus when _np_<sup>2</sup> is small, the probability P _{Bin_ ( _n, p_ ) = _k}_ is close to P _{Poi_ ( _np_ ) = _k}_ for each _k_ = 0 _,_ 1 _, . . ._ .

An implication of this fact is that for every fixed _λ >_ 0, we have


This is because when _p_ = _λ/n_ , we have _np_<sup>2</sup> = _λ_<sup>2</sup> _/n_ which will be small when _n_ is large.

This approximation property of the Poisson distribution is the reason why the Poisson distribution is used to model counts of rare events. For example, it is common to use the Poisson distribution to model the number of phone calls a telephone operator receives in a day, the number of accidents in a particular street in a day, the number of typos found in a book, the number of goals scored in a football game etc. Can you justify why the Poisson distribution might be appropriate for these random variables?

### **7.3 Continuous Random Variables**

Continuous random variables are random variables that potentially take a continuous set of values. The distribution of a continuous random variable _X_ is often described by a function called the _probability density function_ (pdf). The pdf is a function _f_ on R that satisfies _f_ ( _x_ ) _≥_ 0 for every _x ∈_ R and


The pdf _f_ of _X_ can be used to calculate P _{X ∈ A}_ for every set _A_ via


Note that if _X_ has pdf _f_ , then for every _y ∈_ R,


It is important to remember that the pdf _f_ ( _x_ ) of a random variable does not represent probability (in particular, it is quite common for _f_ ( _x_ ) to take values much larger than one). Instead, the value _f_ ( _x_ ) can be thought of as a constant of proportionality for probabilities. This is because usually (as long as _f_ is continuous at _x_ ):


38

If _X_ is a continuous random variable with density (pdf) _f_ , the expectation of _g_ ( _X_ ) is defined as


We shall next look at some standard Continuous Distributions.

### **7.4 Uniform Distribution**

A random variable _U_ is said to have the uniform distribution on (0 _,_ 1) if it has the following pdf:


We write _U ∼ U_ [0 _,_ 1].

More generally, given an interval ( _a, b_ ), we say that a random variable _U_ has the uniform distribution on ( _a, b_ ) if it has the following pdf:


We write this as _U ∼ U_ ( _a, b_ ).

### **7.5 The Gaussian or Normal Distribution**

A random variable _X_ has the Gaussian or normal distribution with mean _µ_ and variance _σ_<sup>2</sup> _>_ 0 if it has the following pdf:


We write _X ∼ N_ ( _µ, σ_<sup>2</sup> ). When _µ_ = 0 and _σ_<sup>2</sup> = 1, we say that _X_ has the _standard_ normal distribution and the standard normal pdf is simply denote by _φ_ ( _·_ ):


The following is the reason for the presence of the factor _√_ 2 _π_ above:


To see why (30) is true, note that


From the above (and by a change of variable), we can derive


If _X ∼ N_ ( _µ, σ_<sup>2</sup> ), then E( _X_ ) = _µ_ and _V ar_ ( _X_ ) = _σ_<sup>2</sup> .

39

#### **7.5.1 The Gauss Derivation of the Normal Distribution**

We shall next look at the Gauss derivation of the normal distribution. Gauss applied the normal distribution in the context of data analysis. The basic question that Gauss addressed is the following: Suppose we take measurements _x_ 1 _, . . . , xn_ on some physical quantity _θ_ . When is _x_ ¯ := ( _x_ 1 + _· · ·_ + _xn_ ) _/n_ the right estimate for _θ_ ? Before the work of Gauss, some prominent mathematicians had doubts about the use of _x_ ¯ to estimate _θ_ . Jaynes (see Jaynes [1, Section 7.4]) writes that Euler thought that combining many observations would make their errors multiply instead of canceling. As is clear from quote below (taken from Jaynes [1, Page 204]), Daniel Bernoulli thought that taking the average of observations amounts to assuming that the individuals errors in the observations are uniformly distributed and that assuming that the errors are uniformly distributed contradicts common sense:

_Now is it not self-evident that the hits must be assumed to be thicker and more numerous on any given band the nearer this is to the mark? If all the places on the vertical plane, whatever their distance from the mark, were equally liable to be hit, the most skillful shot would have no advantage over a blind man. That, however, is the tacit assertion of those who use the common rule (the arithmetic mean) in estimating the value of various discrepant observations, when they treat them all indiscriminately._

The quote above (by Daniel Bernoulli) is in the context of an archer shooting at a vertical line drawn on a target and contemplating on the number of shoots landing on vertical bands on either side of the vertical line.

Gauss showed that taking the average of the distributions is the right way of estimating _θ_ when the errors have the Gaussian distribution. Gauss first assumed that the errors have a distribution _f_ . More specifically, assume that


for _i_ = 1 _, . . . , n_ with


for a density _f_ . The maximum likelihood estimator of _θ_ is then given by the maximizer _θ_<sup>ˆ</sup> of


Letting _g_ ( _u_ ) = log _f_ ( _u_ ), we can say that _θ_<sup>ˆ</sup> maximizes


which means (assuming _g_ is smooth)


Gauss asked for what density _f_ is it true that the maximum likelihood estimator _θ_<sup>ˆ</sup> equals the mean _x_ ¯ for every dataset _x_ 1 _, . . . , xn_ . More precisely, for what _f_ (or equivalently _g_ ) do we have

_n_


40

Gauss showed that this equation leads to _g_<sup>_′_</sup> being the linear function:


for some _a ∈_ R. This means _g_ ( _u_ ) = _au_<sup>2</sup> _/_ 2 + _b_ so that


For _f_ to be a density over ( _−∞, ∞_ ), we need _a <_ 0 in which case _f_ will be normal:


for some _σ >_ 0. The density of the observations _x_ 1 _, . . . , xn_ is then


Gauss therefore showed that the only distribution on the errors which leads to maximum likelihood estimates being averages is the Normal. This accounts for the popularity (since Gauss) of normal error assumptions in data analysis.

Here is the argument for (31). If we take _n_ = 2, we get


which means _g_<sup>_′_</sup> (0) = 0 and _g_<sup>_′_</sup> ( _−x_ ) = _−g_<sup>_′_</sup> ( _x_ ). Now taking

_x_ 1 = _nu_ and _x_ 2 = _· · ·_ = _xn_ = 0 _,_

for some _u_ (so that _x_ ¯ = _u_ ), we get


which gives (combining with _g_<sup>_′_</sup> ( _−x_ ) = _−g_<sup>_′_</sup> ( _x_ ))


Taking _m_ = _n −_ 1, we have proved that


This can also be written as (replacing _u_ by _u/m_ ) _g_<sup>_′_</sup> ( _u/m_ ) = _g_<sup>_′_</sup> ( _u_ ) _/m_ and thus we have


for every _n, m ≥_ 1 which is same as _g_<sup>_′_</sup> ( _ru_ ) = _rg_<sup>_′_</sup> ( _u_ ) for every positive rational _r_ and real _u_ . If we now assume that _g_<sup>_′_</sup> is continuous, we obtain _g_<sup>_′_</sup> ( _uv_ ) = _vg_<sup>_′_</sup> ( _u_ ) for every _v >_ 0 and _u_ which gives _g_<sup>_′_</sup> ( _u_ ) = _ug_<sup>_′_</sup> (1). This proves (31) with _a_ = _g_<sup>_′_</sup> (1). Something can still be said without continuity (see the wiki article on the Cauchy Functional Equation `https: //en.wikipedia.org/wiki/Cauchy%27s_functional_equation` ).

For more comments on Gauss’s derivation of the normal distribution, see Jaynes [1, Section 7.4].

41

---

[← 6 Lecture Six](07-6-lecture-six.md) · [Up: contents](index.md) · [8 Lecture Eight →](09-8-lecture-eight.md)
