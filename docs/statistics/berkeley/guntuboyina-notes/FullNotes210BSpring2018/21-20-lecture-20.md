---
title: 20 Lecture 20
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 20 Lecture 20

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall start our formal study of the theory of convergence of stochastic processes in this lecture. To understand the general ideas, it is helpful to look at the special case of the uniform empirical process.

104

## **20.1 The Uniform Empirical Process**

Suppose _X_ 1 _, . . . , Xn_ are i.i.d random variables that are uniformly distributed on [0 _,_ 1]. For each _t ∈_ [0 _,_ 1], let


The collection of random variables _{Un_ ( _t_ ) : 0 _≤ t ≤_ 1 _}_ represents a stochastic process indexed by [0 _,_ 1]. Every realization of this process (which corresponds to every realization of _X_ 1 _, . . . , Xn_ ) is a function on [0 _,_ 1] that is bounded (and also right continuous having left limits at every point in (0 _,_ 1]). Note that realizations of _{Un_ ( _t_ ) : _t ∈_ [0 _,_ 1] _}_ are not continuous functions.

By the usual Multivariate Central Limit Theorem, for every _k ≥_ 1 and _t_ 1 _, . . . , tk ∈_ [0 _,_ 1],


where Σ is given by Σ( _i, j_ ) := min( _ti, tj_ ) _− titj_ .

The Brownian Bridge is a stochastic process _{U_ ( _t_ ) : 0 _≤ t ≤_ 1 _}_ is a stochastic process indexed by [0 _,_ 1] that is defined by the following two properties:

1. Every realization of _U_ ( _t_ ) _, t ∈_ [0 _,_ 1] is continuous function on [0 _,_ 1] with _U_ (0) = _U_ (1) = 0.

2. For every fixed _t_ 1 _, . . . , tk ∈_ [0 _,_ 1], the random vector ( _U_ ( _t_ 1) _, . . . , U_ ( _tk_ )) has the multivariate normal distribution with mean vector 0 and covariance matrix Σ given by Σ( _i, j_ ) := min( _ti, tj_ ) _− titj_ .

Based on the above, it is clear that for every _k ≥_ 1 and _t_ 1 _, . . . , tk ∈_ [0 _,_ 1], we have


and this is a consequence of the usual CLT. By definition of convergence in distribution, the statement (181) means that


for every bounded, continuous function _g_ : R<sup>_k_</sup> _→_ R. It is also true that (182) holds for all bounded continuous functions _g_ : R<sup>_k_</sup> _→_ R if and only if (182) holds for all bounded Lipschitz functions _g_ : R<sup>_k_</sup> _→_ R. For a proof of this equivalence, see, for example, Pollard [20].

The result (181) can therefore be rephrased in the following manner: the expectation of any bounded continuous function of the stochastic process _Un_ that depends on _Un_ only through its values at a finite set of points in [0 _,_ 1] converges to the corresponding expectation of the Brownian Bridge _U_ . For example, this implies that


for every bounded continuous function _h_ : R _→_ R which is equivalent to


While this is useful, one often needs to deal with functions of _Un_ that depend on the entire process _Un_ and not just at its values at a finite set of points. For example, it is of interest (for example, for the statistical application of testing goodness of fit via the Kolmogorov-Smirnov test) to ask if


which is equivalent to


105

for all bounded continuous functions _h_ : R _→_ R. Obviously these functions depend on _Un_ through all its values on [0 _,_ 1] and not just at finitely many values. Here is a reasonable strategy to prove (184). Take a large finite grid of points 0 = _t_ 0 _< t_ 1 _< · · · < tk−_ 1 _< tk_ = 1 in [0 _,_ 1]. By right-continuity of _Un_ ( _t_ ), it would seem possible to choose a large enough grid so that


Also because Brownian Bridge _{U_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 _}_ has continuous sample paths, it seems reasonable that

Now by (183),


Putting the above three displayed equations together, it would seem to be possible to deduce (184). For this strategy to work, it is important that the approximation (185) holds “uniformly” in _n_ for all large _n_ . Indeed, if the grid _F_ has to change considerably as _n_ changes to maintain approximation, then this strategy cannot work. It seems clear from this discussion that move from finite-dimensional convergence of stochastic processes to infinite-dimensional convergence should be possible under an assumption which guarantees a grid approximation to the process uniformly at all large values of _n_ . This is the so-called assumption of asymptotic equicontinuity (also known as stochastic equicontinuity) which is formulated in the abstract result stated next.

## **20.2 An Abstract Result**

For the next result, we use the following notation. _ℓ_<sup>_∞_</sup> [0 _,_ 1] denotes the class of all bounded functions on [0 _,_ 1] (i.e., all functions _f_ for which sup0 _≤t≤_ 1 _|f_ ( _t_ ) _| < ∞_ ). We shall view _ℓ_<sup>_∞_</sup> [0 _,_ 1] as a metric space under the following metric:


When we refer to a continuous function _h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R, we mean that _h_ is continuous in the metric defined above.

Also, _C_ [0 _,_ 1] denotes the class of all continuous functions on [0 _,_ 1].

**Theorem 20.1.** _Suppose for each n ≥_ 1 _, {Xn_ ( _t_ ) _, t ∈_ [0 _,_ 1] _} is a stochastic process whose realizations are functions in ℓ_<sup>_∞_</sup> [0 _,_ 1] _. Suppose {Xt, t ∈_ [0 _,_ 1] _} is another stochastic process whose realizations are functions in C_ [0 _,_ 1] _. Assume that the following two conditions hold:_

_1. For every k ≥_ 1 _and t_ 1 _, . . . , tk ∈_ [0 _,_ 1] _,_


_This assumption will be referred to as_ **_Finite Dimensional Convergence_** _._

_2. For every ϵ >_ 0 _and δ >_ 0 _, there exists an integer Nϵ,δ and a finite grid_ 0 = _t_ 0 _< t_ 1 _< · · · < tk−_ 1 _< tk_ = 1 _such that_


_This assumption will be referred to as_ **_Stochastic Equicontinuity_** _or_ **_Asymptotic Equicontinuity_** _._

106

_Then for every bounded continuous function h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R _, we have_


**Remark 20.1.** _We can simplify assumption_ (188) _slightly by taking ϵ_ = _δ i.e., we change it to: for every η >_ 0 _, there exists an integer Nη and a finite grid_ 0 = _t_ 0 _< t_ 1 _< · · · < tk−_ 1 _< tk_ = 1 _such that_


_It is easy to see that_ (188) _and_ (190) _are equivalent. Indeed,_ (188) _obviously implies_ (190) _. Also,_ (190) _for η_ = min( _ϵ, δ_ ) _implies_ (188) _._

The Stochastic Equicontinuity assumption(188) essentially says that _Xn_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 can be aprproximated by _Xn_ ( _t_ ) _, t ∈{t_ 0 _, t_ 1 _, . . . , tk}_ for all large _n_ i.e., the approximation holds uniformly in _n_ as long as _n_ is large.

_Proof of Theorem 20.1._ We shall prove (189) for all functions _h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R that are bounded and Lipschitz. It turns out that if (189) holds for all bounded Lipschitz _h_ , then it also holds for all bounded continuous _h_ but we shall skip the proof of this.

Let us therefore assume that _h_ is bounded in absolute value by _B_ and is _L_ -Lipschitz i.e.,


Fix _ϵ >_ 0 and invoke the stochastic equicontinuity assumption with _ϵ >_ 0 and _δ_ = _ϵ_ to get an integer _N_ = _Nϵ_ and a grid 0 = _t_ 0 _< t_ 1 _< · · · < tk−_ 1 _< tk_ = 1 such that (188) holds. Let _F_ := _{t_ 0 _, t_ 1 _, . . . , tk}_ and let _AF_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→ ℓ_<sup>_∞_</sup> [0 _,_ 1] defined by


and ( _AF x_ )(1) = _x_ (1). It is easy to check that for every _x ∈ ℓ_<sup>_∞_</sup> [0 _,_ 1],


Therefore


We now change the grid _F_ so that the above inequality also holds for the process _X_ ( _t_ ) _,_ 0 _≤ t ≤_ 1 as well (note that _X_ has continuous sample paths). For this, let _S_ = _{s_ 0 _, s_ 1 _, s_ 2 _, . . . }_ be a countable dense subset of [0 _,_ 1] with _s_ 0 = 0 and _s_ 1 = 1. Then, for every _x ∈ C_ [0 _,_ 1],


Because _X_ has continuous sample paths, we have


Thus for all large _m_ , we have


Take such a large _m_ “merge” the two grids _{s_ 0 _, s_ 1 _, . . . , sm}_ and _{t_ 0 _, t_ 1 _, . . . , tk}_ . For the resulting merged grid, say _T_ , we have


107

Note that _ϵ_ changed to 2 _ϵ_ inside the probability (this is because when _ti ≤ sj ≤ t < ti_ + _ϵ_ , we used the bound _|Xn_ ( _t_ ) _− Xn_ ( _sj_ ) _| ≤|Xn_ ( _t_ ) _− Xn_ ( _ti_ ) _|_ + _|Xn_ ( _ti_ ) _− Xn_ ( _sj_ ) _|_ and similarly for _X_ ).

Now for the function _h_ satisfying (191), we can write


For the first term on the right hand side above, we argue as

E _|h_ ( _Xn_ ) _− h_ ( _AT Xn_ ) _| ≤_ E _|h_ ( _Xn_ ) _− h_ ( _AT Xn_ ) _| I{∥Xn − AT Xn∥∞ ≤_ 2 _ϵ}_ + E _|h_ ( _Xn_ ) _− h_ ( _AT Xn_ ) _| I{∥Xn − AT Xn∥∞ >_ 2 _ϵ} ≤ L_ (2 _ϵ_ ) + 2 _B_ (P _{I{∥Xn − AT Xn∥∞ >_ 2 _ϵ}_ ) _≤_ 2 _Lϵ_ + 2 _Bϵ._

The same upper bound also holds for the second term in (192). For the third term in (192), use the finitedimensional convergence assumption (note that the grid _T_ does not depend on _n_ ) to claim that


We have thus proved that


Since _ϵ >_ 0 is arbitrary, we have proved (189).

## **20.3 Back to the Uniform Empirical Process**

Recall the uniform empirical process _Un_ in (180) and the Brownian Bridge _U_ . Then, as we have seen, the multivariate CLT implies finite dimensional convergence. We shall argue here that the _Un_ satisfies stochastic equicontinuity as well. For this, let us first note that stochastic equicontinuity follows from


Indeed, if (193) holds, then given _ϵ >_ 0 and _δ >_ 0, there exists _η >_ 0 and an integer _Nϵδ_ such that for every _n ≥ Nϵ,δ_ , we have


Let 0 = _t_ 0 _< t_ 1 _< · · · < tk_ = 1 be a uniform grid in [0 _,_ 1] with spacing _η_ . Then clearly


and thus, by Markov’s inequality, we have


which gives stochastic equicontinuity.

We shall now verify (193). This will be done via a bound for the expected suprema of empirical processes that we studied way back in Lecture 9. Let _Pn_ denote the empirical measure of _X_ 1 _, . . . , Xn_ and let _P_ denote the uniform measure on [0 _,_ 1]. Then


108

where


We then use the following inequality (proved in Lecture 9)

The class _F_ has the trivial envelope _F ≡_ 1 so we <u>get</u> ( **There is a mistake here. We cannot deduce from** sup _f ∈F_ ~~�~~ _Pnf_<sup>2</sup> _≤_ 1 **that** _M_ ( _ϵ_ sup _f ∈F_ ~~�~~ _Pnf_<sup>2</sup> _, F, L_<sup>2</sup> ( _Pn_ )) _≤ M_ ( _ϵ, F, L_<sup>2</sup> ( _Pn_ )) **; the inequality will actually go the other way because** _ϵ_ **-packing numbers increase as** _ϵ_ **decreases ; see next lecture for the correct argument. I am leaving this incorrect argument here so we know that it does not work.** )


Bound the VC subgraph dimension of _F_ and use the relation between packing numbers and the VC subgraph dimension to show that


which gives


where we used the trivial inequality _√a_ + _b ≤_<sup>_√_</sup> _<u>a</u>_ + _√b_ . For every _f_ = _I_ [0 _,s_ ] _− I_ [0 _,t_ ] _∈F_ , we have _Pf_<sup>2</sup> = _P_ � _I_ [0 _,s_ ] _− I_ [0 _,t_ ]�2 = _s_ + _t −_ 2 min( _s, t_ ) = _|s − t| ≤ η_

so we get


Argue now that _{f_<sup>2</sup> : _f ∈F}_ is a Boolean class of VC dimension at most 2 so that


which goes to zero as _η →_ 0 and _n →∞_ thereby proving (193).

The finite dimensional convergence of _Un_ to _U_ along with stochastic equicontinuity implies that (by Theorem 20.1)


for every bounded continuous function _h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R.

109

## **20.4 An Issue with Measurability**

There are some measurability issues with the assertion (194). It turns out that it cannot happen that _h_ ( _Un_ ) is measurable for every bounded continuous function _h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R. Let us illustrate this below for the case when _n_ = 1 (the argument can be extended for higher values of _n_ as well; see, for example, Pollard [18, Problem 1, Page 86]).

Note first that the stochastic process _U_ 1 depends on _X_ 1 alone. In fact, the function _U_ 1 in _ℓ_<sup>_∞_</sup> [0 _,_ 1] precisely equals


where _Id_ is the function _Id_ ( _t_ ) = _t_ . We shall assume, if possible, that


and arrive at a contradiction. It is easy to see that the above assertion is equivalent to


By a standard connection between continuous functions and closed sets (see for example, Billingsley [2, Chapter 1]), it can be shown that (195) implies that


Here open sets in _ℓ_<sup>_∞_</sup> [0 _,_ 1] are defined with respect to the metric (186). It can now be verified that for every subset _A ⊆_ [0 _,_ 1], the following is true:


where _B_ ( _I_ [ _s,_ 1] _,_ 1 _/_ 2) refers to the open ball in _ℓ_<sup>_∞_</sup> [0 _,_ 1] (with respect to the metric (186)) centered at _I_ [ _s,_ 1] and of radius 1 _/_ 2. Because an arbitrary union of open sets is open, the set _O_ defined above is open. We have therefore obtained, as a consequence of (195), that _I{X_ 1 _∈ A}_ is measurable for every subset _A_ of [0 _,_ 1]. Because _X_ 1 is distributed according to the uniform distributoin on [0 _,_ 1], this means that it would be possible to define a probability measure on the set of all subsets of [0 _,_ 1] such that the probability of every interval equals the length of the interval. This cannot happen under the axiom of choice.

Due to the contradiction above, it follows that _h_ ( _U_ 1) cannot be measurable for all bounded continuous functions _h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R. One can also show that the same holds for _h_ ( _Un_ ) for every _n ≥_ 1. This therefore means that we cannot really talk about E _h_ ( _Un_ ). As a fix, one considers outer Expectations here (denoted by E<sup>_∗_</sup> _h_ ( _Un_ )). Fortunately, the theory goes through with this fix. More details will be provided in the next lecture.

---

[← 19 Lecture 19](20-19-lecture-19.md) · [Up: contents](index.md) · [21 Lecture 21 →](22-21-lecture-21.md)
