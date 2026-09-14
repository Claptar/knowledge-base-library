---
title: 2 Lecture 2
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Lecture 2

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **2.1 Uniform Central Limit Theorems**

Let us now describe the second fundamental question that is addressed by the theory of empirical process.

By the usual Central Limit Theorem (CLT), we have that


converges in distribution to the normal distribution with mean zero and variance _V ar_ ( _f_ ( _X_ 1)) as _n →∞_ . This statement is true for every _f ∈F_ . Does this convergence hold uniformly over _f_ in the class _F_ in a reasonable sense? To illustrate this, let us look at the following example.

**Example 2.1.** _Suppose that X_ 1 _, . . . , Xn are i.i.d observations from the uniform distribution on_ [0 _,_ 1] _. Also suppose that F consists of all indicator functions {I_ ( _−∞,t_ ] : _t ∈_ R _}. In this case, for f_ = _I−∞,t_ ] _, the quantity_


_where Fn is the empirical distribution function of the observations X_ 1 _, . . . , Xn. Define_


_Un_ ( _t_ ) _represents a collection of random variables as t varies in_ [0 _,_ 1] _. The stochastic process {Un_ ( _t_ ) _, t ∈_ [0 _,_ 1] _} is known as the “Uniform Empirical Process”. It is easy to see that every realization of {Un_ ( _t_ ) _, t ∈_ [0 _,_ 1] _}, viewed as a function on_ [0 _,_ 1] _, is piecewise linear with jump discontinuities at the n data points X_ 1 _, . . . , Xn. Also Un_ (0) = _Un_ (1) = 0 _for every n._

_The CLT states that for each t ∈_ [0 _,_ 1] _, the sequence of real random variables {Un_ ( _t_ ) _} converges in distribution to N_ (0 _, t − t_<sup>2</sup> ) _as n →∞. Moreover, the multivariate CLT states that for every fixed t_ 1 _, . . . , tk, the sequence of random vectors_ ( _Un_ ( _t_ 1) _, . . . , Un_ ( _tk_ )) _converges in distribution to the multivariate normal distribution with zero means and covariances given by_ min( _ti, tj_ ) _− titj._

_At this point, let us introduce an object called Brownian Bridge. The Brownian Bridge on_ [0 _,_ 1] _is a stochastic process {U_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 _} that is characterized by the following two requirements:_

_1. Every realization is a continuous function on_ [0 _,_ 1] _with U_ (0) _and U_ (1) _always fixed to be equal to 0._

_2. For every fixed t_ 1 _, . . . , tk in_ [0 _,_ 1] _, the random vector_ ( _U_ ( _t_ 1) _, . . . , U_ ( _tk_ )) _has the multivariate normal distribution with zero means and covariances given by_ min( _ti, tj_ ) _− titj._

8

_We therefore see that the “finite dimensional distributions” of the process {Un_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 _} converge to the “finite dimensional distributions” of {U_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 _}. It is natural to ask here if one can claim anything beyond finite-dimensional convergence here. Does the entire process {Un_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 _} converge to {U_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 _}? This was first conjectured by Doob and rigorously proved by Donsker._

_What is the meaning of the statement that the sequence of stochastic processes {Un_ ( _t_ ) _, t ∈_ [0 _,_ 1] _} converges in distribution to {U_ ( _t_ ) _, t ∈_ [0 _,_ 1] _}? To understand, let us first recall the usual notion of convergence in distribution for sequences of random vectors. We say that a sequence of random vectors {Zn} taking values in_ R<sup>_k_</sup> _converges in distribution to Z if and only if_


_for every_ **_bounded continuous real-valued function_** _h_ : R<sup>_k_</sup> _→_ R _._

_One can attempt a direct generalization of this to define convergence of Un_ ( _·_ ) _to U_ ( _·_ ) _as a stochastic process. These processes take values not in_ R<sup>_k_</sup> _but in the space of all bounded functions on_ [0 _,_ 1] _. Let us denote this space by ℓ_<sup>_∞_</sup> ([0 _,_ 1]) _. This space can be metrized by the supremum metric:_ sup0 _≤t≤_ 1 _|g_ 1( _t_ ) _− g_ 2( _t_ ) _|. We can then say that Gn converges in distribution to U as a stochastic process provided_


_for every bounded and continuous real valued function h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R _. This definition almost makes sense except for one measure-theoretic issue. It turns out that there exist bounded and continuous real valued functions h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R _for which the random variable h_ ( _Un_ ) _is not measurable. One therefore replaces the left hand side in_ (4) _by its_ **_outer_** _expectation_ E<sup>_∗_</sup> _h_ ( _Un_ ) _(formally defined later)._

_In this sense, Donsker showed that Un converges in distribution to Brownian Bridge._

Let us now return to the general case. Here we consider the stochastic process:


Under a simple assumption such as sup _f ∈F |f_ ( _x_ ) _| < ∞_ for every _x ∈X_ , the function _f �→ Gn_ ( _f_ ) belongs to the space _ℓ_<sup>_∞_</sup> ( _F_ ). We say then that the uniform central limit theorem holds over _F_ if the stochastic process _Gn_ ( _f_ ) _, f ∈F_ converges in distribution in _ℓ_<sup>_∞_</sup> ( _F_ ) to a process _G_ ( _f_ ) _, f ∈F_ as _n →∞_ . The limit process _G_ ( _f_ ) _, f ∈F_ will have the property that for every _f_ 1 _, . . . , fk ∈F_ , the random vector ( _G_ ( _f_ 1) _, . . . , G_ ( _fk_ )) will have a multivariate normal distribution having the same covariance as ( _Gn_ ( _f_ 1) _, . . . , Gn_ ( _fk_ )).

We shall characterize convergence in distribution in _ℓ_<sup>_∞_</sup> ( _F_ ) and then see some sufficient conditions on _F_ that ensure that the Uniform CLT holds.

The following are some statistical applications of Uniform CLTs.

**Example 2.2** (Classical Motivation: Goodness of Fit Testing) **.** _Suppose one observes i.i.d observations X_ 1 _, . . . , Xn from a distribution (cdf) F and wants to test the null hypothesis H_ 0 : _F_ = _F_ 0 _against the alternative hypothesis H_ 1 : _F̸_ = _F_ 0 _. Here F_ 0 _is a fixed distribution function._

_Kolmogorov recommended testing this hypothesis via the quantity_


_where Fn is the empirical cdf of the data X_ 1 _, . . . , Xn. The idea is to reject H_ 0 _when Dn is large. To calculate the p-value of this test, the null distribution (i.e., the distribution of Dn under H_ 0 _) needs to be determined. An interesting property of the null distribution of Dn is that the null distribution does not depend on F_ 0 _as long as F_ 0 _is continuous. (I will leave this fact as an exercise; it can, for example, be proved via the quantile transformation)._

9

_Because of this fact, one can compute the null distribution of Dn assuming that F_ 0 _is the uniform distribution on_ (0 _,_ 1) _. In this case, we can write_


_where Un_ ( _t_ ) _is the uniform empirical process from Example 180._

_The fact that {Un_ ( _t_ ) _, t ∈_ [0 _,_ 1] _} converges in distribution to a Brownian bridge {U_ ( _t_ ) _, t ∈_ [0 _,_ 1] _} as n →∞ actually allows one to claim that_


_The latter probability can be exactly computed (see, for example, Dudley [5, Proposition 12.3.4]). Thus the uniform central limit theorem gives a way of computing asymptotically valid p-values for Goodness of fit testing via the Kolmogorov Statistic._

_The same argument can be used for many related goodness of fit statistics such as_

_1. Cramer-Von Mises Statistic: Defined as_


_2. Anderson-Darling Statistic: Defined as_


_3. Smirnov statistics: Defined as_


_The asymptotic null distribution of all these statistics can be computed from Brownian bridge and this will be validated by the uniform CLT._

**Example 2.3** (Asymptotic Distribution of MLE) **.** _Suppose X_ 1 _, . . . , Xn are i.i.d from an unknown density pθ_ 0 _belonging to a known class {pθ_ : _θ ∈_ Θ _⊆_ R<sup>_k_</sup> _}. Let θ_<sup>ˆ</sup> _n denote the maximum likelihood estimator of θ_ 0 _defined as the maximizer of_


_over θ ∈_ Θ _. A classical result is that, under some smoothness assumptions,_<sup>_√_</sup> _<u>n</u> θ_ ˆ _n − θ_ 0 _converges in_ � � _distribution to Nk_ (0 _, I_<sup>_−_1</sup> ( _θ_ 0)) _where I_ ( _θ_ 0) _denotes the k × k Fisher information matrix defined as_


_where the gradient ∇θ is evaluated at θ_ = _θ_ 0 _and the expectation is taken with respect to the density pθ_ 0 _._

_What smoothness assumptions need to be imposed on pθ, θ ∈_ Θ _for this result to hold? Because the result involves the information matrix I_ ( _θ_ 0) _which involves gradients, a minimal assumption seems to be that θ �→_ log _pθ_ ( _x_ ) _needs to be differentiable with respect to θ. Also because of the presence of the expectation in the definition of I_ ( _θ_ 0) _, it should be okay if the derivative with respect to θ does not exist on sets of measure zero with respect to pθ_ 0 _(think about the model pθ_ ( _x_ ) := exp( _−|x − θ|_ ) _/_ 2 _)._

_The classical proofs of this result assume however that this map allows two (or sometimes even three) derivatives. Using uniform central limit theorems, we shall present later a proof using a minimal differentiability assumption called Differentiability in Quadratic Mean (DQM)._

10

**Example 2.4** (Asymptotic Distribution Results for M-estimators) **.** _Uniform central limit theorems can be used to derive limiting distributions of other M-estimators as well._

_For example, consider the sample median defined as:_


_Assuming that the distribution function F of the observations is differentiable at its median θ_ 0 _with positive derivative f_ ( _θ_ 0) _, it can be proved that_


_converges in distribution to N_ (0 _,_ (4 _f_<sup>2</sup> ( _θ_ 0))<sup>_−_1</sup> ) _._

_For the mode defined as_ argmax _θ∈_ R � _ni_ =1<sup>_mθ_(</sup><sup>_Xi_)</sup><sup>_with mθ_(</sup><sup>_x_) :=</sup><sup>_I{|x−θ| ≤_1</sup><sup>_} and_Θ = R</sup><sup>_,the asymptotic_</sup> _distribution is much more complicated. The result is that_


_converges in distribution to_

argmax � _aZ_ ( _h_ ) _− bh_<sup>2�</sup> _h∈_ R

_where Z is a standard two-sided Brownian motion starting from 0,_


_Here p_ ( _·_ ) _represents the density of the observations and it is assumed that p is unimodal and symmetric with mode θ_ 0 _i.e., p_<sup>_′_</sup> ( _x_ ) _>_ 0 _for x < θ_ 0 _and p_<sup>_′_</sup> ( _x_ ) _<_ 0 _for x > θ_ 0 _. This result is stated here just to illustrate that the limiting distributions of even simple-looking M-estimators can be quite complicated. We shall later see how to prove these results via Uniform CLTs._

## **2.2 Concentration Results**

Let us now start with our discussion of uniform laws of large numbers. The key object of study is


where _X_ 1 _, . . . , Xn_ are i.i.d random objects taking values in a space _X_ and _F_ is a collection of real-valued functions on _X_ . We shall argue that (5) concentrates around its expectation. This is fairly easy to prove when it is assumed that the all functions in _F_ are bounded by a positive constant _B_ :


Under the above assumption, we shall prove a concentration result for (5). We shall do this as a consequence of the _bounded differences_ concentration inequality.

**Theorem 2.5** (Bounded Differences Concentration Inequality) **.** _Suppose X_ 1 _, . . . , Xn are independent random variables taking values in a set X . Suppose g_ : _X × · · · × X →_ R _be a function that satisfies the following “bounded differences” assumption’:_


11

_for every i_ = 1 _, . . . , n. Then for every t ≥_ 0 _, we have_


_and_


**Remark 2.1.** _The bounded differences condition_ (211) _is equivalent to the following:_


_whenever_ ( _x_ 1 _, . . . , xn_ ) _and_ ( _z_ 1 _, . . . , zn_ ) _differ in exactly the i_<sup>_th_</sup> _coordinate._

_It is also equivalent to the following condition:_


Theorem 2.5 can be seen as a quantification of the following qualitative statement of Talagrand (see Talagrand [22, Page 2]): _A random variable that depends on the influence of many independent variables (but not too much on any of them) concentrates’_ . The numbers _ci_ control the effect of the _i_<sup>_th_</sup> variable on the function _g_ .

We shall prove Theorem 2.5 in the next class. Let us argue here that it implies a concentration inequality

for


under the condition (6). Indeed, let


We shall show below that _g_ satisfies the bounded differences assumption (211) with _ci_ := 2 _B/n_ for _i_ = 1 _, . . . , n_ . To see this, note that


For every _f ∈F_ , by triangle inequality and the fact that _|f_ ( _xi_ ) _| ≤ B_ and _|f_ ( _x_<sup>_′_</sup> _i_<sup>)</sup><sup>_| ≤B_,wehave</sup>


Taking supremum over _f ∈F_ on both sides, we obtain


12

Interchanging the roles of _xi_ and _x_<sup>_′_</sup> _i_<sup>,wecandeducethat</sup>


so that (211) holds with _ci_ = 2 _B/n_ . Theorem 2.5 (specifically inequality (8)) then gives


Setting


we deduce that the following inequality:

holds with probability at least 1 _− δ_ for every _δ >_ 0.

This inequality implies that E( _Z_ ) is usually the dominating term for understanding the behavior of _Z_ . This is because typically E( _Z_ ) dominates the last term on the right hand side of (10). Indeed, for every _f ∈F_ ,

Because


it is reasonable to believe that the right hand side of (11) will typically be of order � _var_ ( _f_ ( _X_ 1)) _/n_ . Thus (unless _var_ ( _f_ ( _X_ 1)) is much smaller compared to _B_<sup>2</sup> for every _f ∈F_ ), the first term on the right hand side of (10) usually dominates the second term and hence in order to control the random variable _Z_ , it is enough to focus on the expectation E _Z_ .

---

[← 1 Lecture 1](02-1-lecture-1.md) · [Up: contents](index.md) · [3 Lecture 3 →](04-3-lecture-3.md)
