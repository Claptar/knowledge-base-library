---
title: 10 Lecture 10
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 Lecture 10

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **10.1 Recap of the Main Empirical Process Bound from last class**

Let us first recall our main bound on the expected suprema of empirical processes. If _F_ is a class of real-valued functions on _X_ with envelope _F_ , then (assuming that _PF_<sup>2</sup> _< ∞_ ), we have


where


An important implication of this bound is that when _F_ is a Boolean function class with finite VC dimension _D_ ,


50

Today, we shall discuss an application of the bounds (67) and (68) to a problem in _M_ -estimation. My treatment here will be a mix of rigor and heuristics. We shall come back to _M_ -estimation next week when all the heuristic arguments will be rigorized.

## **10.2 Application to an** _M_ **-estimation problem**

This can be seen as a mode estimation problem. Suppose _X_ 1 _, . . . , Xn_ are i.i.d observations from a univariate density _p_ . We shall assume that _p_ has a single mode _θ_ 0 and that it is symmetric about _θ_ 0 _∈_ R. In addition, we shall assume that _p_ is smooth and bounded and that _p_<sup>_′_</sup> ( _x_ ) _>_ 0 for _x < θ_ 0 and that _p_<sup>_′_</sup> ( _x_ ) _<_ 0 for _x > θ_ 0. You can think of _p_ as the normal density with mean _θ_ 0 or the Cauchy density centered at _θ_ 0.

Consider now the problem of estimating _θ_ 0. For this, let us define


Note that


Because of the assumptions on _p_ , it is clear that _M_<sup>_′_</sup> ( _θ_ 0) = 0 and for _θ̸_ = _θ_ 0, we have _M_<sup>_′_</sup> ( _θ_ ) _<_ 0 for _θ > θ_ 0 and _M_<sup>_′_</sup> ( _θ_ ) _>_ 0 for _θ < θ_ 0. This implies that _θ �→ M_ ( _θ_ ) has a unique maximum at _θ_ 0. Also _M_<sup>_′′_</sup> ( _θ_ 0) = _p_<sup>_′_</sup> ( _θ_ 0 + 1) _− p_<sup>_′_</sup> ( _θ_ 0 _−_ 1) _<_ 0.

Because _θ_ 0 uniquely maximizes _M_ ( _θ_ ) over _θ ∈_ R, a reasonable method of estimating _θ_ 0 is to estimate it by _θ_<sup>ˆ</sup> _n_ where _θ_<sup>ˆ</sup> _n_ is any maximizer of _Mn_ ( _θ_ ) over _θ ∈_ R with


It is now natural to ask the following questions:

1. Is _θ_<sup>ˆ</sup> _n_ consistent as an estimator for _θ_ 0 i.e., is it true that _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ converges in probability to zero.

2. One does have consistency in this example as we shall show. One can then ask: what is the rate of convergence _rn_ of _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ to zero?

3. What is the limiting distribution of _rn_ ( _θ_<sup>ˆ</sup> _n − θ_ 0)?

Below we shall prove consistency of _θ_<sup>ˆ</sup> _n_ rigorously. I will also provide a heuristic argument for finding the rate _rn_ which we shall make rigorous next week. The limiting distribution will be addressed in a few weeks after the discussion on uniform central limit theorems.

The fundamental first step for analyzing M-estimators is the following inequality:


where we have used the inequality _Mn_ ( _θ_ 0) _≤ Mn_ ( _θ_<sup>ˆ</sup> _n_ ) which holds because _θ_<sup>ˆ</sup> _n_ maximizes _Mn_ ( _·_ ). We can rewrite the above inequality in Empirical Process notation. For _θ ∈_ R, let us define the function _mθ_ : R _→_ R by


With this notation, the inequality becomes


51

This inequality is so fundamental that is has been referred to as the _basic inequality_ .

To derive the consistency of _θ_<sup>ˆ</sup> _n_ from (70), we can crudely bound the right hand side of (70) as


It is now easy to check that _{mθ, θ ∈_ R _}_ is a Boolean class of functions with VC dimension 2 and hence inequality (68) implies that


Combining this with (70), we obtain


Now because of our assumptions on _p_ , the following is true:


Indeed, for _M_ ( _θ_ ) as in (69), under our assumptions on _p_ , we have


because _M_ ( _·_ ) has a unique maximum at _θ_ 0. The two assumptions (71) and (72) imply together that _|θ_<sup>ˆ</sup> _n − θ_ 0 _|→P_ 0. To see this, first fix _ϵ >_ 0 and use (72) to obtain _η >_ 0 such that


It follows then that


where the last (converging to zero) assertion follows from (71). This proves that _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_

This argument for proving consistency of an _M_ -estimator is quite general and can be isolated in the following theorem (which can be found, for example, in Van der Vaart [24, Theorem 5.7]).

**Theorem 10.1** (Consistency) **.** _Let {Mn} be a sequence of random functions of θ ∈_ Θ _and let {M } be a fixed deterministic function of θ ∈_ Θ _. Let θ_<sup>ˆ</sup> _n be any maximizer of {Mn_ ( _θ_ ) _, θ ∈_ Θ _} and let θ_ 0 _be the unique maximizer of {M_ ( _θ_ ) _, θ ∈_ Θ _}. Suppose the following two conditions hold_

_1._ sup _θ∈_ Θ _|Mn_ ( _θ_ ) _− M_ ( _θ_ ) _|→P_ 0 _._

_2. For every ϵ >_ 0 _, the inequality_ sup _θ∈_ Θ: _d_ ( _θ,θ_ 0) _≥ϵ M_ ( _θ_ ) _< M_ ( _θ_ 0) _. Here d is a metric on_ Θ _._

_Then d_ ( _θ_<sup>ˆ</sup> _n, θ_ 0) _→P_ 0 _as n →∞._

The assumption sup _θ∈_ Θ _|Mn_ ( _θ_ ) _− M_ ( _θ_ ) _|→P_ 0 is often too strong for consistency (and also not always easy to check) but there exist results with weaker conditions.

Now that the consistency of _θ_<sup>ˆ</sup> _n_ is established, the next natural question is about the rate of convergence. We can first try to go over the consistency argument again to see it gives an explicit rate of convergence for _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ . I shall argue heuristically.

52

The consistency argument given above was based on the inequality:


For consistency, we used that the right hand side above converges in probability to zero. But the inequality (68) actually implies that


which gives


Inequality (73) then gives


From here, to obtain an explicit rate for _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ we need to use some structure of the function _M_ ( _·_ ). Note that the second derivative of _M_ at _θ_ 0 equals


which is strictly negative because, by assumption, _p_<sup>_′_</sup> ( _θ_ 0 + 1) _<_ 0 and _p_<sup>_′_</sup> ( _θ_ 0 _−_ 1) _>_ 0. As a result, there exists a constant _C_ and aneighbourhood of _θ_ 0 such that for all _θ_ in that neighbourhood, we can write


The value of _C_ is related to _M_<sup>_′′_</sup> ( _θ_ 0). Using this, we can heuristically write


In other words, I am assuming that _θ_<sup>ˆ</sup> _n_ belongs to the neighborhood of _θ_ 0 where (75) holds. Because of the consistency of _θ_<sup>ˆ</sup> _n_ (which we have rigorously proved), the inequality (76) can be made rigorous. Combining (76) with (74), we deduce that


which gives


We have therefore obtained _n_<sup>_−_1</sup><sup>_/_4</sup> as a rate of convergence for _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ . It turns out however that


In other words, _n_<sup>_−_1</sup><sup>_/_4</sup> is slower than the actual rate of convergence and is a reflection of some loosness in our proof technique. The main source of looseness is in the inequality:


It turns out that the left hand side above is much smaller than the right hand side. To get a heuristic understanding of the size of the left hand side above, let us first compute bounds for


for a fixed _θ_ which is close to _θ_ 0. Clearly


53

Now for _θ_ close to _θ_ 0 (and _θ < θ_ 0), we have


Thus


where, in the last inequality, we used the fact that the density of _X_ 1 has a mode at _θ_ 0 (so that the density at every other point is bounded by _p_ ( _θ_ 0)). Combining this with (78), we obtain


so that


This is true for a fixed _θ_ that is close to _θ_ 0. Heuristically, this suggests that


We shall formally justify this later. Note that this bound is an stronger compared to our earlier bound (77). Plugging this in the right hand side of the basic inequality (70) and using the quadratic bound (76) on the left hand side of (70), we deduce that


“Cancelling” _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_<sup>1</sup><sup>_/_2</sup> from both sides, we deduce that

As mentioned earlier, this is the correct rate for _θ_<sup>ˆ</sup> _n − θ_ 0. Indeed, it turns out that


as _n →∞_ where _Zh, h ∈_ R is two-sided Brownian motion starting from 0 and _a, b_ are two constants depending on _p_ and _θ_ 0. We shall prove this limiting result later but it tells us now that _n_<sup>_−_1</sup><sup>_/_3</sup> is the correct rate of convergence.

We shall make the rate result (79) rigorous next week. A key ingredient in the rigorous argument will involve establishing the inequality


for _δ_ sufficiently small. The above inequality can be derived as a consequence of (67). Indeed, to apply (67), we first need to obtain an envelope for the class _{mθ − mθ_ 0 : _|θ − θ_ 0 _| ≤ δ}_ . It is not hard to see that


54

is an envelope function. Further

_PF_<sup>2</sup> _≤_ 2P _{θ_ 0 _−_ 1 _− δ ≤ X_ 1 _≤ θ_ 0 _−_ 1 + _δ}_ + 2P _{θ_ 0 + 1 _− δ ≤ X_ 1 _≤ θ_ 0 + 1 + _δ} ≤ Cp_ ( _θ_ 0) _δ ≤ Cδ._ Thus (67) gives


where _F_ := _{mθ − mθ_ 0 : _|θ − θ_ 0 _| ≤ δ}_ . This will prove (80) provided _J_ ( _F, F_ ) _< ∞_ . This will follow from the fact that the class _{mθ − mθ_ 0 _}_ has finite VC subgraph dimension (to be defined shortly). Note that this is not a Boolean class of functions so we need VC subgraph dimension as opposed to VC dimension.

Let us now summarize this discussion of a heuristic argument for the rate of _M_ -estimators. Although we did for a special _M_ -estimator which corresponded to _mθ_ ( _x_ ) := _I{θ −_ 1 _≤ x ≤ θ_ + 1 _}_ , the ideas are actually fairly general. The most important ingredient is the Basic inequality (70). The left hand side _P_ ( _mθ_ 0 _− mθ_ ˆ _n_ ) is bounded from below by an assumption on the second derivative of _θ �→ Pmθ_ at _θ_ = _θ_ 0. The right hand side can be understood by calculating


For the specific choice of _mθ_ ( _x_ ) = _I{θ −_ 1 _≤ x ≤ θ_ + 1 _}_ , it turned out that


For other _mθ_ , the right hand side might be different (for example, it is common to have _C|θ − θ_ 0 _|_<sup>2</sup> on the right hand side). Plugging these bounds in the basic inequality will yield an inequality involving _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ and _n_ which can be solved to get explicit rates (such as _n_<sup>_−_1</sup><sup>_/_3</sup> ) in this problem. This heuristic will be justified next week. Before concluding this section, let us state a result from Van der Vaart and Wellner [25, Page 294] on the rate of convergence of _M_ -estimators. We shall formally prove this result later but, based on the above heuristics, its conclusion should be quite obvious.

**Theorem 10.2** (Van der Vaart and Wellner, Page 294) **.** _Let X_ 1 _, X_ 2 _, . . . be i.i.d observations from a distribution P . Suppose_ Θ _⊆_ R _is an open set and let mθ, θ ∈_ Θ _be a collection of real-valued functions on X that are indexed by_ Θ _. Suppose there exist α >_ 0 _and a function M on X with PM_<sup>2</sup> _< ∞ for which_


_Let θ_<sup>ˆ</sup> _n and θ_ 0 _denote maximizers of Pnmθ and Pmθ over θ ∈_ Θ _. If θ �→ Pmθ has two derivatives at θ_ 0 _with the second derivative strictly negative, then_


_Heuristic Argument._ We use the heuristics summarized above to justify (82) based on the assumptions made in the theorem. Note that assumption (81) implies that

E ( _mθ_ ( _X_ 1) _− mθ_ 0( _X_ 1))<sup>2</sup> _≤_ E � _M_<sup>2</sup> ( _X_ 1) _|θ − θ_ 0 _|_<sup>2</sup><sup>_α_�</sup> _≤|θ − θ_ 0 _|_<sup>2</sup><sup>_α_</sup> _PM_<sup>2</sup> _≤ C|θ − θ_ 0 _|_<sup>2</sup><sup>_α_</sup> _._

This suggests the heuristic


Combining with the basic inequality (and the lower bound _C_ ( _θ_<sup>ˆ</sup> _n − θ_ 0)<sup>2</sup> on _P_ ( _mθ_ 0 _− mθ_ ˆ _n_ ), we obtain the inequality

which gives


Note that when _α_ = 1, Theorem 10.2 gives the usual _n_<sup>_−_1</sup><sup>_/_2</sup> rate for _|θ_<sup>ˆ</sup> _n − θ_ 0 _|_ .

55

---

[← 9 Lecture 9](10-9-lecture-9.md) · [Up: contents](index.md) · [11 Lecture 11 →](12-11-lecture-11.md)
