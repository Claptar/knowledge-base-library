---
title: 21 Lecture 21
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 21 Lecture 21

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We proved the following process convergence theorem in the last class.

**Theorem 21.1.** _Suppose for each n ≥_ 1 _, {Xn_ ( _t_ ) _, t ∈_ [0 _,_ 1] _} is a stochastic process whose realizations are functions in ℓ_<sup>_∞_</sup> [0 _,_ 1] _. Suppose {Xt, t ∈_ [0 _,_ 1] _} is another stochastic process whose realizations are functions in C_ [0 _,_ 1] _. Assume that the following two conditions hold:_


_This assumption will be referred to as_ **_Finite Dimensional Convergence_** _._

110

_2. For every ϵ >_ 0 _and δ >_ 0 _, there exists an integer Nϵ,δ and a finite grid_ 0 = _t_ 0 _< t_ 1 _< · · · < tk−_ 1 _< tk_ = 1 _such that_


_This assumption will be referred to as_ **_Stochastic Equicontinuity_** _or_ **_Asymptotic Equicontinuity_** _._

_Then for every bounded continuous function h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R _(here we are viewing ℓ_<sup>_∞_</sup> [0 _,_ 1] _as a metric space under the uniform metric), we have_


Here are some remarks on this theorem.

1. If the sample paths of _Xn_ have jumps (such as when _Xn_ ( _t_ ) =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _Fn_ ( _t_ ) _− t_ )), then (as mentioned in the previous class) _h_ ( _Xn_ ) need not be measurable for every bounded continuous funciton _h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R. In this case, E _h_ ( _Xn_ ) may not be properly defined. This can be fixed by replacing E _h_ ( _Xn_ ) by its outer expectation E<sup>_∗_</sup> _h_ ( _Xn_ ) defined as


The result of the theorem will be true if E _h_ ( _Xn_ ) is replaced by E<sup>_∗_</sup> _h_ ( _Xn_ ). We shall ignore these measurability issues in our treatment. For a careful analysis, see Kato [12].

2. We take (198) to be the definition of the convergence of the sequence of stochastic processes _{Xn}_ to _X_ in _ℓ_<sup>_∞_</sup> [0 _,_ 1]. We shall write this as _Xn→L X_ as _n →∞_ . Like in the case of convergence in distribution on Euclidean spaces, the following are equivalent definitions of _Xn→L X_ :

   - (a) E<sup>_∗_</sup> _h_ ( _Xn_ ) _→_ E _h_ ( _X_ ) for every bounded Lipschitz function _h_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R.

   - (b) For every open set _G_ in _ℓ_<sup>_∞_</sup> [0 _,_ 1], we have lim inf _n→∞_ P<sup>_∗_</sup> _{Xn ∈ G} ≥_ P _{X ∈ G}_ .

   - (c) For every closed set _F_ in _ℓ_<sup>_∞_</sup> [0 _,_ 1], we have lim sup _n→∞_ P<sup>_∗_</sup> _{Xn ∈ F } ≤_ P _{X ∈ F }_ .

An important consequence of process convergence is the _continuous mapping theorem_ : Suppose _Xn→L X_ and _g_ : _ℓ_<sup>_∞_</sup> [0 _,_ 1] _→_ R<sup>_k_</sup> is continuous, then _g_ ( _Xn_ ) _→L g_ ( _X_ ). This is a trivial consequence of the definition of process convergence.

3. Finite dimensional convergence is usually a consequence of the Lindeberg-Feller Central Limit Theorem.

4. Stochastic equicontinuity is implied by


which is further implied by


For example, to see that (199) implies (197), note that for every _ϵ >_ 0 and _δ >_ 0, there exists _η >_ 0 such that


This further implies the existence of an integer _Nϵ,δ_ such that for all _n ≥ Nϵ,δ_ ,


111

Let 0 = _t_ 0 _< t_ 1 _< · · · < tk_ = 1 be a uniform grid in [0 _,_ 1] with spacing _η_ so that


so that by Markov inequality, we have


which proves (197).

In Theorem 21.1, the interval [0 _,_ 1] can be replaced by any other compact subinterval [ _a, b_ ] of R. In fact, it can be replaced by any abstract set _T_ . In this case, one gets the following theorem whose proof we will skip (the proof can be found, for example, in Kato [12, Theorem 11]).

Let _ℓ_<sup>_∞_</sup> ( _T_ ) denote the space of all bounded functions on _T_ viewed as a metric space with the metric ( _f_ 1 _, f_ 2) _�→_ sup _t∈T |f_ 1( _t_ ) _− f_ 2( _t_ ) _|_ .

**Theorem 21.2.** _For each n ≥_ 1 _, let Xn_ ( _t_ ) _, t ∈ T be a stochastic process with realizations in ℓ_<sup>_∞_</sup> ( _T_ ) _. Suppose_

_1. For every k ≥_ 1 _and t_ 1 _, . . . , tk ∈ T , the random vector sequence_ ( _Xn_ ( _t_ 1) _, . . . , Xn_ ( _tk_ )) _converges in distribution to some limit._

_2. There exists a semi-metric d on T for which_ ( _T, d_ ) _is totally bounded and such that_


_Then there exists a stochastic process X_ ( _t_ ) _, t ∈ T whose realizations are continuous functions on T (with respect to the metric d) such that Xn→L X in ℓ∞_ ( _T_ ) _or, equivalently,_ E _∗h_ ( _Xn_ ) _→_ E _h_ ( _X_ ) _as n →∞ for every bounded continuous function h_ : _ℓ_<sup>_∞_</sup> ( _T_ ) _→_ R _._

Note that Theorem 21.2 does not start with a limit object _X_ but it rather asserts the existence of a process _X_ ( _t_ ) _, t ∈ T_ with continuous sample paths (with respect to the metric _d_ with respect to which _Xn_ satisfies stochastic equicontinuity). Note that the limit object necessarily satisfies the property that ( _Xn_ ( _t_ 1) _, . . . , Xn_ ( _tk_ )) converges in distribution to ( _X_ ( _t_ 1) _, . . . , X_ ( _tk_ )) for every _k ≥_ 1 and _t_ 1 _, . . . , tk ∈ T_ .

## **21.1 Maximal Inequalities and Stochastic Equicontinuity**

As we have seen, the key condition for process convergence is stochastic equicontinuity. To prove it, we obviously need bounds on


In most of the applications _Xn_ will be related to an empirical process and hence we are led to bounds on the expected suprema of empirical process.

Let us illustrate the general ideas with an example first. Suppose that the index set _T_ = [0 _,_ 1] and _Xn_ is the uniform empirical process i.e.,


112

where _Pn_ is the empirical measure corresponding to the observations _X_ 1 _, . . . , Xn_ which are i.i.d uniform on [0 _,_ 1] (also _P_ is the distribution of [0 _,_ 1]). We shall attempt to prove here that _Xn_ satisfies stochastic equicontinuity. For this, first note that


where we use the following notation:

_F_ := � _I_ [0 _,t_ ] : 0 _≤ t ≤_ 1� and _Gη_ := � _I_ [0 _,t_ ] _− I_ [0 _,s_ ] : 0 _≤ s, t ≤_ 1 _, |s − t| ≤ η_ � for _η ∈_ [0 _,_ 1] _._

We can use our earlier bounds on the expected suprema of empirical processes to control


One of our main bounds on the expected suprema of empirical processes (from Lecture 9) is


where


where _H_ is the envelope of _H_ defined as _H_ ( _x_ ) := sup _h∈H |h_ ( _x_ ) _|_ . Applying this to _H_ = _Gη_ , we obtain


where _G_ is the envelope of _Gη_ . It is now easy to see that _G_ is the constant function that is equal to one. Note that _PG_<sup>2</sup> = 1 while _Pg_<sup>2</sup> _≤ η_ for every _g ∈Gη_ (in other words, _PG_<sup>2</sup> is much larger than sup _g∈Gη Pg_<sup>2</sup> ). Because _G ≡_ 1, the bound above becomes


We shall now show that the integral above is bounded from above by a constant. There are at least two ways of showing this. For the first way, argue that the class _{I_ [0 _,s_ ] _− I_ [0 _,t_ ] : 0 _≤ s, t ≤_ 1 _}_ has finite VC subgraph dimension (at most 3??) and use our earlier relations between packing numbers and VC subgraph dimensions. For the second way, the trivial inequality


which holds for every _s, t_ and every pair of functions _f_ 1 and _f_ 2 implies that


This is because we can cover functions _I_ [0 _,s_ ] _− I_ [0 _,t_ ] to within 2 _δ_ in _L_<sup>2</sup> ( _Q_ ) distance by covering the individual functions _I_ [0 _,t_ ] to within _δ_ and then taking all pairs of functions in the cover. This gives


where _c_ and _C_ are positive constants (the latter inequality follows from the fact that _F_ is a Boolean function class with VC dimension 1).

113

We have therefore proved that


Note that the second inequality above cannot be significantly improved because the integral is at least 1. Unfortunately, the bound above is not strong enough to yield


To improve our bounds in order to deduce the above, we need to use bounds that are better than (200). Recall (from Lecture 9) that although (200) was stated as a main bound, it actually follows from the following inequality:


From this bound, we can argue as follows. For every _δ ∈_ [0 _,_ 1], we can write


By (201), we can replace the second integral by a constant and the first integral by the integral of the covering numbers of _F_ to get


The last expected supremum can be controlled (as in the last lecture) via


where we used the trivial inequality _√a_ + _b ≤_<sup>_√_</sup> _<u>a</u>_ + _√b_ . As we mentioned earlier, sup _g∈Gη Pg_<sup>2</sup> _≤ η_ so that


Note now that _{g_<sup>2</sup> : _g ∈Gη}_ is a Boolean class of VC dimension at most 2 so that


Combining this with (204), we obtain


114

As a consequence,

and further


Since this is true for every _δ >_ 0, the inequality will also hold if we take limit of the right hand side as _δ →_ 0. It is now easy to show that this limit would be zero (this is because the integral from 0 to 1 is finite so the integral from 0 to _δ_ should go to zero as _δ →_ 0 by the dominated convergence theorem). We have thus proved (202) which is same as stochastic equicontinuity of _Xn_ ( _t_ ) _, t ∈_ [0 _,_ 1]. Combined with finite dimensional convergence, we have proved that the uniform empirical process converges in distribution to Brownian Bridge. This is Donsker’s theorem for the uniform empirical process.

We had to do a bit of work above to go from (203) to (202). There exist other maximal inequalities which allow one to deduce of (202) more easily. The following theorem (taken from Kato [12, Theorem 8]) is one such result.

**Theorem 21.3.** _Let H be an envelope for the class H with PH_<sup>2</sup> _< ∞. Then_


_for every δ satisfying_

_Here_


Let us now demonstrate that Theorem 21.3 yields (202) quite easily. Indeed, applying inequality (205) to _H_ = _Gη_ (with envelope _H ≡_ 1) and _δ_ =<sup>_√_</sup> _<u>η</u>_ (note that sup _g∈Gη Pg_<sup>2</sup> _≤ η_ and _PG_<sup>2</sup> = 1), we get


which implies

lim sup _n→∞_<sup>E</sup> _g_<sup>sup</sup> _∈Gη |_<sup>_√_</sup> _n_ ( _Png − Pg_ ) _| ≤ CJ_ (<sup>_√_</sup> _<u>η</u>_ <u>)</u>


which, as before, goes to 0 as _η ↓_ 0. This gives a shorter proof of (202) (albeit reliant on the nontrivial result from Theorem 21.3).

---

[← 20 Lecture 20](21-20-lecture-20.md) · [Up: contents](index.md) · [22 Lecture 22 →](23-22-lecture-22.md)
