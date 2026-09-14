---
title: The proof of Theorem 6.1.
source: https://www.stat.berkeley.edu/~aldous/205B/511.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/511.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# The proof of Theorem 6.1.

**Source:** [`511.pdf`](https://www.stat.berkeley.edu/~aldous/205B/511.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

_Case 1._ Suppose _α_ = 0, so the move measure Φ puts mass 1 _/_ 2 each at 0 and 1; this is the stationary measure too, with stationarity being achieved in one move. Since _α_<sup>_′_</sup> = 0, the theorem holds.

_Case 2._ Suppose _α_ = _∞_ , so the move measure Φ concentrates on 1 _/_ 2. Starting from _x_ , the chain moves to<sup><u>1</u></sup> 2<sup>_x_or</sup><sup>_x_+</sup><sup><u>1</u></sup> 2<sup>_−_</sup><sup><u>1</u></sup> 2<sup>_x_=</sup><sup><u>1</u></sup> 2<sup>+</sup><sup><u>1</u></sup> 2<sup>(1</sup><sup>_−x_)witha50–50chance.</sup> Clearly, the uniform distribution is invariant, its image under the motion having mass<sup><u>1</u></sup> 2<sup>uniformly distributed over [0</sup><sup>_,_</sup><sup><u>1</u></sup> 2<sup>], and mass</sup><sup><u>1</u></sup> 2<sup>uniform on [</sup><sup><u>1</u></sup> 2<sup>_,_1].Since</sup><sup>_α′_= 1</sup> and Beta(1 _,_ 1) is uniform, the theorem holds.

_Case 3._ This was discussed in Section 2.1.

_Case 4._ Suppose the move measure Φ is Beta( _α, α_ ) with 0 _< α <_ 1 or 1 _< α < ∞_ . Recall that _α_<sup>_′_</sup> = _α/_ ( _α_ + 1); and let _U_<sup>_′_</sup> _∼_ Beta( _α_<sup>_′_</sup> _, α_<sup>_′_</sup> ). By Corollary 6.1 and some tedious algebra,


We must now compute the first 4 moments of the stationary distribution; the latter exists by Theorem 5.1. Let _U_ have the stationary distribution and let _V ∼_ Beta( _α, α_ ); make these two random variables be independent. As before, write _L_ ( _Z_ ) for the law of _Z_ . Then


because _U_ + _V − UV_ = 1 _−_ (1 _− U_ )(1 _− V_ ) and _U_ , _V_ are symmetric. In particular,


_E_ ( _V_<sup>_n_</sup> ) is given by Corollary 6.1, so equation (6.5) can be solved recursively for the moments of _U_ , and _E_ ( _U_<sup>_n_</sup> ) = _E_ ( _U_<sup>_′n_</sup> ) for _n_ = 1 _,_ 2 _,_ 3. However,


Consequently,


(Again, unpleasant algebraic details are suppressed.) Figure 7 shows the graph of the right side of (6.6), plotted against _α_ . As will be seen, the discrepancy is rather small.

ITERATED RANDOM FUNCTIONS

29

Figure 7. Difference between 4th moment of stationary distribution and 4th moment of approximating Beta, scaled by 10<sup>4</sup> and plotted against _α_ ; symmetric chain, Beta( _α, α_ ) move distribution.


<!-- Start of picture text -->
1.50<br>0.75<br>0.00<br>1 2 3 4 5<br>–0.75<br>–1.50<br><!-- End of picture text -->

**Remark.** Theorem 6.1 is connected to results in Dubins and Freedman (1967). Consider generating a random distribution function by constructing its graph in the unit square. Draw a horizontal line through the square, cutting the vertical axis into a lower segment and an upper segment whose lengths stand in the ratio _p_ to 1 _− p_ . Pick a point at random on this line. That divides the square into four rectangles. Now repeat the construction in the lower left and upper right rectangles. (The description may be cumbersome, but the inductive step is easy.) The limiting monotone curve connecting all the chosen points is the graph of a random distribution function. The average of these distribution functions turns out to be absolutely continuous: let _φ_ be its density. This density is, by construction, invariant under the following operation. Choose _x_ at random uniformly on [0 _,_ 1]; distribute mass _p_ according to _φ_ rescaled over [0 _, x_ ] and mass 1 _− p_ according to _φ_ rescaled over [ _x,_ 1]. If _U_ is uniform and _X ∼ φ_ , then


In short, _φ_ is the stationary density for our Markov process. The equation in Lemma 6.3 is discussed in Section 9 of Dubins and Freedman (1967).

**7. Dirichlet distributions.** The Dirichlet distribution is the multidimensional analog of the more familiar Beta, and is often used in Bayesian nonparametric statistics. An early paper is Freedman (1963); also see Fabius (1964) or Ferguson (1973). Sections 7.1–2 sketch a construction of the Dirichlet. The setting is an infinite dimensional space, namely, the space of all probability measures on an underlying complete separable metric space. Section 7.3 discusses the law of the mean of _F_ picked at random from a Dirichlet distribution, which can sometimes be computed in closed form. The setting is the real line.

**7.1. Random measures.** Let (X _, ρ_ ) be a complete separable metric space, for instance, the real line. Let P be the set of all probability measures on X; _p_ and _q_ will be typical elements of P, that is, typical probabilities on X. We will be

PERSI DIACONIS AND DAVID FREEDMAN

30

considering random probabilities _P_ on X: these are random objects with values in P. The “law” of such an object is a probability on P. Let _α_ be a finite measure on X. The “Dirichlet with base measure _α_ ”, usually abbreviated as _Dα_ , is the law of a certain random probability on X. Thus, _Dα_ is a probability on P.

Here, we show how to construct _Dα_ by modifying the argument for Theorem 5.1. The state space _S_ for the Markov chain is P. The variation distance between _p_ and _q_ is defined as


where _B_ runs over all the Borel subsets of X. The “parameter space” for the Lipschitz functions will be Θ = [0 _,_ 1] _×_ P. If 0 _≤ u ≤_ 1 and _p ∈_ P, let _fu,p_ map P into P by the rule


It is easy to see that _fu,p_ is an affine map of P into itself. Furthermore, this function is Lipschitz, with Lipschitz constant _Ku,p_ = _u_ .

If _µ_ is any probability measure on the parameter space Θ, the Markov chain on P driven by _µ_ has a unique stationary distribution. The Dirichlet will be obtained by specializing _µ_ . Caution: the stationary distribution is a probability on P, that is, a probability on the probabilities on X; and there is a regularity condition, namely,


Recall that _L_ stands for law. Then _Q_ has the stationary distribution if


where _L_ ( _U, P_ ) = _µ_ independent of _Q_ . The stationary distribution may be represented by the backward iteration, as the law of the random probability


In (7.3), the ( _Un, Pn_ ) are independent, with common distribution _µ_ ; as will be seen in a moment, the sum converges almost surely. The limit is a random probability on X because each _Pn_ is a random probability on X, and the _Un_ are random elements of [0 _,_ 1]. Furthermore,


telescopes to 1.

In variation distance, P is complete but not separable. Thus, Theorem 5.1 does not apply. Rather than deal with the measure-theoretic technicalities created by an inseparable space, we sketch a direct argument for convergence. First, we have to prove that the sum in (7.4) converges almost surely. Indeed, write _Tn_ for the _n_ th term. Then _E{Tn}_ = (1 _− φ_ ) _φ_<sup>_n−_1</sup> , where


ITERATED RANDOM FUNCTIONS

31

by (7.1). Thus _P {Tn >_ � _φ_<sup>_n−_1</sup> _} <_ � _φ_<sup>_n−_1</sup> , and<sup>�</sup> _n_ � _φ_<sup>_n−_1</sup> _< ∞_ . An immediate consequence: with probability 1, the sum on the right in (7.3) is Cauchy and hence converges in variation norm (completeness). The law of _S∞_ is easily seen to be stationary, using the criterion (7.2). To get a geometric rate of convergence, suppose the chain starts from _q_ . Let _Sn_ be the sum of the first _n_ terms in (7.3). After _n_ moves starting from _q_ , the backward process will be at _Sn_ + _Rn_ , where _Rn_ = _U_ 1 _U_ 2 _· · · Unq_ . By previous arguments, except for a set of geometrically small probability, _∥Sn − S∞∥_ and _∥Rn∥_ are geometrically small. We have proved the following result.

**Theorem 7.1.** _Suppose (7.1) holds. Consider the Markov chain on_ P _driven by µ. Let Pn_ ( _q, dp_ ) _be the law of the chain after n moves starting from q._

- (i) _There is a unique invariant probability π._

- (ii) _There is a positive, finite constant A and an r with_ 0 _< r <_ 1 _such that ρ_ [ _Pn_ ( _q, ·_ ) _, π_ ] _≤ Ar_<sup>_n_</sup> _for all n_ = 1 _,_ 2 _, . . . and all q ∈_ P _._

In this theorem, _ρ_ is the Prokhorov metric on probabilities on P, constructed from the variation distance on P, as in Definition 5.1. The constant _A_ is universal, because variation distance is uniformly bounded. If condition (7.1) fails, the chain stagnates at the starting position _q_ .

We now specialize _µ_ to get the Dirichlet. Recall that _α_ is a finite measure on X. Let _∥α∥_ = _α_ (X) be the total mass of _α_ and let _γ_ = _α/∥α∥_ , which is a probability on X. Let _γ_ ˜ be the image of _γ_ under the map _x → δx_ , with _δx ∈_ P being point mass at _x ∈_ X. Thus, _γ_ ˜ is a probability on P, namely, the law of _δx_ when _x ∈_ X is chosen at random from _γ_ . (Caution: see Section 7.2 for measurability.) Finally, we set _µ_ = Beta( _∥α∥,_ 1) _×_ ˜ _γ_ . In other words, _µ_ is the law of ( _u, δx_ ), where _u_ is chosen from the Beta( _∥α∥,_ 1) distribution and _x_ is independently chosen from _α/∥α∥_ . For this _µ_ , the law of the random probability defined by (7.3) is Dirichlet, with base measure _α_ .


where


- (7.7b) _U_ is Beta( _∥α∥,_ 1),

- (7.7c) _W_ is _i_ with probability _αi/∥α∥_ , and

(7.7d) _Q, U, W_ are independent.

Of course, _{Q_ 0 _, Q_ 1 _}_ —the masses assigned by _Q_ to 0 and 1 —should be Dirichlet with parameters _α_ 0 _, α_ 1 _, α_ 2 by (7.7a). The density of a Dirichlet distribution with these parameters is


32 PERSI DIACONIS AND DAVID FREEDMAN

for ( _x, y_ ) with _x >_ 0 _, y >_ 0 _, x_ + _y <_ 1. The normalizing constant _C_ makes � _f_ = 1; its numerical value will not matter here. Condition on _W_ in (7.6) and use (7.7cd). Stationarity boils down to

(7.8)


where


and _g_ is the density of the random variable _U_ in (7.6). By (7.7b), _g_ ( _u_ ) = _∥α∥u_<sup>_∥α∥−_1</sup> . We deal with _T_ 1 and _T_ 2, below.

The next task is to determine the range of the integral in (7.9). There are several constraints on _u_ . First is that


Second, ( _x −_ 1 + _u_ ) _/u <_ 1, which follows from _x <_ 1. Third, _u > y_ , which follows from (7.10), because 1 _− x > y_ . Fourth,


which follows from _x_ + _y <_ 1. Finally, _u <_ 1. Thus, the integral in (7.9) goes from 1 _− x_ to 1; there is quite a lot of cancellation of _u_ ’s, and


The terms _T_ 1 and _T_ 2 in (7.8) can be evaluated the same way:


So


because _x_ + _y_ + (1 _− x − y_ ) = 1. This completes the proof of (7.6).

ITERATED RANDOM FUNCTIONS

33

The same argument goes through for any finite X. Then compact X can be handled by taking limits. Along the way, it helps to check that


A complete separable X can be embedded into a compact set, so the general case follows from the compact case; (7.11) shows that _Dα_ sits on X, as desired, rather than spilling over onto points added by compactification.

**7.2. Measure-theoretic issues.** Put the weak-star _σ_ -field on P: this is generated by the functions _p →_ � _f dp_ as _f_ ranges over the bounded continuous functions on X. The variation norm is weak-star measurable, because


as _f_ ranges over the continuous functions on X with 0 _≤ f ≤_ 1. With a bit of effort, we can restrict _f_ to a countable, dense set of continuous functions. Measurability of the norm is then clear. For example, if X is [0 _,_ 1], we can restrict _f_ to the polynomials with rational coefficients.

Put the usual Borel _σ_ -field on [0 _,_ 1]. Then ( _u, p, q_ ) _→ fu,p_ ( _q_ ) is jointly measurable, from [0 _,_ 1] _×_ P _×_ P to P. Likewise, ( _u, p_ ) _→ Ku,p_ = _u_ is measurable. For each _n_ , the map


is jointly measurable from Θ<sup>_n_</sup> _×_ P to P. Finally, the map _x → δx_ is measurable from X to P.

The “Borel” _σ_ -field in P is generated by the open sets in the norm topology, and seems to fit better with variation distance. But there is a real problem: the map _x → δx_ is not measurable if we put the Borel _σ_ -fields on X and P. A reference is Dubins and Freedman (1964). We need the variation norm to get the Lipschitz property and the weak-star _σ_ -field to handle measurability. In a complete separable metric space, all reasonable _σ_ -fields coincide—ranging from the Borel _σ_ -field to (for instance) the _σ_ -field generated by the bounded, uniformly continuous functions. The space of probability measures is complete in the variation distance but not separable. That is the source of the measure-theoretic complications.

**7.3. Random means.** Let _P_ be a random pick from _Dα_ , as defined in Section 7.1 above. Let _f_ be a measurable function on X. Consider the random variable �X<sup>_f dP_.</sup> (Of course, the random variable is defined only when the integral converges.) Feigen and Tweedie (1989) prove the following result.

**Proposition 7.1.** _|f_ ( _x_ ) _| P_ ( _dx_ ) _< ∞ for Dα-almost all P if and only if_ �X


34 PERSI DIACONIS AND DAVID FREEDMAN

We now specialize X to the real line ( _−∞, ∞_ ), and _f_ ( _x_ ) to _x_ . Suppose


Then


is a random variable—being the mean of a _P_ picked at random from _Dα_ . Formula (7.14) must be distinguished from (7.11). In (7.11), you pick _P_ at random from _Dα_ , and take the mean over all _P_ ’s relative to _Dα_ : for any measurable _A ⊂_ X,


In (7.14), you pick _P_ at random from _Dα_ , and take the mean over all _x_ ’s relative to _P_ . That gives a random variable _X_ ( _P_ ) = � _−∞∞_<sup>_x dP_.</sup>

In a number of cases, the distribution of _X_ relative to _Dα_ can be be computed explicitly, using the idea of iterated random functions. For instance, Cifarelli and Regazzini (1990) show that unless _α_ is a point mass, _P →_ � _x dP_ has an absolutely continuous distribution, and they give formulas for the density. Additional results are obtained by Diaconis and Kemperman (1996).

**Example 7.1.** Suppose _α_ concentrates on two points, 0 and 1. Relative to _Dα_ , _P → X_ ( _P_ ) has the Beta( _α_ 0 _, α_ 1) distribution. This is immediate from the discussion in Section 7.1 above: after all, _X_ ( _P_ ) is the mass _P_ assigns to 1.

**Example 7.2.** If _α_ is uniform on [0 _,_ 1], then _X_ has the density


**Example 7.3.** If _α_ is Cauchy then _X_ also has the Cauchy distribution. See Yamamoto (1984). Of course, � _x α_ ( _dx_ ) does not converge. On the other hand, (7.13) holds, so that for almost all _P_ drawn from _Dα_ , the integral in (7.14) does converge. Picks from _Dα_ have a shorter tail than _α_ .

**Example 7.4.** Let _Z_ be Cauchy. If _α_ is the law of _e_<sup>_Z_</sup> _/_ (1 + _e_<sup>_Z_</sup> ), then _X_ is uniform on [0 _,_ 1].

For the mathematics behind examples (7.2–3–4), we refer to Diaconis and Kemperman (1996) where connections to the Markov moment problem and recent work of Kerov (1993) are explained. We conclude by showing how the law of _X_ in (7.14) can be obtained as the stationary distribution under random iterated functions. This is fairly immediate on the basis of Section 7.1. The state space is the real line. From _x_ , the chain moves to _Ux_ + (1 _− U_ ) _W_ , where _U_ is Beta( _∥α∥,_ 1), and _W_ is an

ITERATED RANDOM FUNCTIONS

35

independent pick from _α/∥α∥_ . The limiting stationary distribution, which is _L_ ( _X_ ), is the distribution of


where ( _Ui, Wi_ ) are i.i.d. copies of ( _U, W_ ): see (7.3).

**Acknowledgment.** We would like to thank Philippe Bougerol, Olle H¨aggstr¨om, and Yuval Peres for many useful suggestions. We also thank our very helpful editors, Dan Rockmore and Nick Trefethen.

Technical Report No. 511 Department of Statistics University of California Berkeley, CA 94720

---

[← Remarks.](05-remarks.md) · [Up: contents](index.md) · [References →](07-references.md)
