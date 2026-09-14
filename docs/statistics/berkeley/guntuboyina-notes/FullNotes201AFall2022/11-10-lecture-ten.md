---
title: 10 Lecture Ten
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 Lecture Ten

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **10.1 Variable Transformations**

It is often common to take functions or transformations of random variables. Consider a random variable _X_ and apply a function _u_ ( _·_ ) to _X_ to transform _X_ into another random variable _Y_ = _u_ ( _X_ ). How does one find the distribution of _Y_ = _u_ ( _X_ ) from the distribution of _X_ ?

If _X_ is a discrete random variable, then _Y_ = _u_ ( _X_ ) will also be discrete and then the pmf of _Y_ can be written directly in terms of the pmf of _X_ :


If _X_ is a continuous random variable with density _fX_ and _T_ ( _·_ ) is a smooth function, then it is fairly straightforward to write down the density of _Y_ = _T_ ( _X_ ) in terms of _fX_ . There are some general formulae for doing this but it is better to learn how to do it from first principles. The general idea will be clear from the following two examples.

**Example 10.1.** _Suppose X ∼ U_ ( _−π/_ 2 _, π/_ 2) _. What is the density of Y_ = tan( _X_ ) _? Here is the method for doing this from first principles. Note that the range of_ tan( _x_ ) _as x ranges over_ ( _−π/_ 2 _, π/_ 2) _is_ R _so fix y ∈_ R _and we shall find below the density g of Y at y._

51

_The formula for g_ ( _y_ ) _is_


_so that_


_Now for small δ,_


_where f is the density of X. Comparing the above with_ (42) _, we can conclude that_


_Using now the density of X ∼ U_ ( _−π/_ 2 _, π/_ 2) _, we deduce that_


_This is the_ **_Cauchy_** _density._

The answer derived in the above example is a special case of the following formula:


which makes sense as long as _T_ is invertible and _T_<sup>_−_1</sup> is differentiable. If the function _T_ is not invertible, then the formula above cannot be directly used but the method (based on first principles) used to derive the above formula is applicable in all cases. Here is an example illustrating this.

**Example 10.2.** _Suppose X has the standard normal density. What is the density of Y_ = _X_<sup>2</sup> _?_

_The function T_ ( _x_ ) = _x_<sup>2</sup> _is not invertible so the formula_ (43) _cannot be used directly. Instead we argue from first principles as follows. Let y >_ 0 _. The density of Y at y is given by_


_For small δ >_ 0 _, we can write_


52

_Thus_


_This is the density of the chi-squared random variable with 1 degree of freedom. This is also the Gamma random variable with shape parameter α_ = 0 _._ 5 _and rate parameter λ_ = 0 _._ 5 _._

_Note that we can also try to calculate the density of Y at_ 0 _by the above method:_

P _{_ 0 _< Y < δ}_ = P _{−√δ < X < √δ} ≈_ 2 _φ_ (0) _√δ_

_so that_


_This ∞ does not affect any calculation of probabilities_ P _{Y ∈ A} as these densities are calculated by the integral_ � _A_<sup>_fY_(</sup><sup>_y_)</sup><sup>_dyandthevalueoffYattheonepoint_0</sup><sup>_doesnotaffect_</sup> _the value of this integral._

### **10.2 The Cumulative Distribution Function and the Quantile Transform**

The _cumulative distribution function_ (cdf) of a random variable _X_ is the function defined as


This is defined for all random variables discrete or continuous. The cdf of every random variable has the following properties: (a) It is non-decreasing, (b) right-continuous, (c) lim _x↓−∞ F_ ( _x_ ) = 0 and lim _x↑_ + _∞ F_ ( _x_ ) = 1.

If the random variable _X_ has a density _fX_ , then its cdf is given by


and, in this case, it is generally true that _F_<sup>_′_</sup> ( _x_ ) = _fX_ ( _x_ ).

The _inverse_ of the cdf is used to define quantiles. Given a random variable _X_ and a number _u ∈_ (0 _,_ 1), the _u_ -quantile of the distribution of _X_ is given by a real number _qX_ ( _u_ ) satisfying


provided such a number _qX_ ( _u_ ) exists uniquely. If _FX_ is the cdf of _X_ , the equation (44) simply becomes


so we can write


Here are some simple examples.

**Example 10.3** (Uniform) **.** _Suppose X has the uniform distribution on_ (0 _,_ 1) _. Then FX_ ( _x_ ) = _x for x ∈_ (0 _,_ 1) _and thus FX_<sup>_−_1(</sup><sup>_u_)</sup><sup>_existsuniquelyforeveryu∈_(0</sup><sup>_,_1)</sup><sup>_andequalsu.Wethus_</sup> _have qX_ ( _u_ ) = _u for every u ∈_ (0 _,_ 1) _._

53

**Example 10.4** (Normal) **.** _Suppose X has the standard normal distribution. Then FX_ ( _x_ ) = Φ( _x_ ) _where_


_There is no closed form expression for_ Φ _but its values can be obtained in R (for example) using the function pnorm._ Φ _is a strictly increasing function from_ ( _−∞, ∞_ ) _to_ (0 _,_ 1) _so its inverse exists uniquely and we thus have_


_There is no closed form expression for qX_ = Φ<sup>_−_1</sup> _but its values can be obtained from R by the function qnorm._

**Example 10.5** (Cauchy) **.** _Suppose X has the standard Cauchy density:_


_Its cdf is given by_


_It is easy to see that this is a strictly increasing function from_ ( _∞, ∞_ ) _to_ (0 _,_ 1) _and its inverse is given by_


_Thus the quantile function for the Cauchy distribution is given by_


How to define the _u_ -quantile when there is no solution or multiple solutions to the equation _FX_ ( _q_ ) = _u_ ? No solutions for _FX_ ( _q_ ) = _u_ can happen for discrete distributions (for example, for _X ∼ Ber_ (0 _._ 5) and _u_ = 0 _._ 25, there is no _q_ satisfying P _{X ≤ q}_ = _u_ ). Multiple solutions can also happen. For example, if _X_ is uniformly distributed on the set [0 _,_ 1] _∪_ [2 _,_ 3] and _u_ = 0 _._ 5, then every _q ∈_ [1 _,_ 2] satisfies _FX_ ( _q_ ) = 0 _._ 5. In such cases, it is customary to define the _u_ -quantile via


This can be seen as a generalization of _FX_<sup>_−_1(</sup><sup>_u_).Indeed,ifthereisaunique</sup><sup>_q_suchthat</sup> _FX_ ( _q_ ) = _u_ , it is easy to see then that _qX_ ( _u_ ) = _q_ .

The function _qX_ : (0 _,_ 1) _→_ ( _−∞, ∞_ ) defined by (45) is called the quantile function or the quantile transform of the random variable _X_ . It can be checked that the definition (45) ensures that


**Example 10.6** (Bernoulli) **.** _Suppose X ∼ Ber_ ( _p_ ) _i.e.,_ P _{X_ = 0 _}_ = 1 _−p and_ P _{X_ = 1 _}_ = _p. When then is qX_ ( _u_ ) _for u ∈_ (0 _,_ 1) _? It can be checked that_


The quantile transform is important for the following reason.

54

**Proposition 10.7.** _The following two statements are true._

_1. Suppose U is a random variable distributed according to the uniform distribution on_ (0 _,_ 1) _. Then qX_ ( _U_ ) _has the same distribution as X. In other words, the function qX transforms the uniform distribution to the distribution of X._

_2. Suppose X is a random variable with a_ **_continuous_** _cdf FX . Then FX_ ( _X_ ) _has the uniform distribution on_ (0 _,_ 1) _. In other words, the function FX transforms the distribution of X into the Unif_ (0 _,_ 1) _distribution (provided the distribution of X is continuous)._

It should be stressed that the first conclusion of the above Proposition holds for every _X_ (discrete or continuous) while the second conclusion is only true if _FX_ is continuous. To see why the second conclusion is false when _FX_ is not continuous, suppose that _X ∼ Ber_ ( _p_ ) so that _X_ takes only the two values 0 and 1. Then _FX_ ( _X_ ) also takes only two values: _FX_ (0) = 1 _− p_ and _FX_ (1) = 1; thus _FX_ ( _X_ ) cannot have the uniform distribution on (0 _,_ 1).

**Example 10.8** (Cauchy) **.** _We have seen in Example 10.5 that for a standard Cauchy random variable, qX_ ( _u_ ) = tan( _π_ ( _u −_ 0 _._ 5)) _. Proposition 10.7 then gives that if U ∼ Unif_ (0 _,_ 1) _, then_


_Note that π_ ( _U −_ 0 _._ 5) _∼ Unif_ ( _−π/_ 2 _, π/_ 2) _. Thus the tan function applied to a uniformly distributed random variable on_ ( _−π/_ 2 _, π/_ 2) _results in a random variable having the Cauchy distribution (as we have seen in Example 10.1)._

**Example 10.9** (Bernoulli) **.** _The quantile function for Ber_ ( _p_ ) _was calculated in_ (10.6) _as_


_As a result, the first conclusion of Proposition 10.7 states that, for U ∼ Unif_ (0 _,_ 1) _,_


_as can be checked directly. Note that this function q is not the only function with the property that q_ ( _U_ ) _∼ Ber_ ( _p_ ) _. For example, the function q_ ˜( _u_ ) = _I{_ 0 _< u < p} also satisfies q_ ˜( _U_ ) _∼ Ber_ ( _p_ ) _._

---

[← 9 Lecture Nine](10-9-lecture-nine.md) · [Up: contents](index.md) · [11 Lecture Eleven →](12-11-lecture-eleven.md)
