---
title: Remarks.
source: https://www.stat.berkeley.edu/~aldous/205B/511.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/511.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Remarks.

**Source:** [`511.pdf`](https://www.stat.berkeley.edu/~aldous/205B/511.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(i) Plainly, _ρ_ ( _P, Q_ ) _≤_ 1.

(ii) Let _ρ_<sup>_∗_</sup> be as in Definition 5.1, with _C_ ranging over all Borel sets. Plainly, _ρ_<sup>_∗_</sup> _< δ_ entails _ρ ≤ δ_ . That is, _ρ ≤ ρ_<sup>_∗_</sup> . Conversely, suppose _ρ < δ_ . Fix a Borel set _B_ and a small positive _ε_ . Find a compact set _C ⊂ B_ with _P_ ( _B_ ) _< P_ ( _C_ ) + _ε_ and _Q_ ( _B_ ) _< Q_ ( _C_ ) + _ε_ . Then


and similarly for _Q_ ( _B_ ). Thus, _ρ_<sup>_∗_</sup> _≤ ρ_ + _ε_ and hence _ρ_<sup>_∗_</sup> _≤ ρ_ . In short, _ρ_<sup>_∗_</sup> = _ρ_ .

(iii) Dudley (1989) is a standard reference for results on the Prokhorov metric.

We need the definition of a random variable with an “algebraic tail”. Basically, _U_ has an algebraic tail if log(1 + _U_<sup>+</sup> ) has a Laplace transform in a neighborhood of 0, where _U_<sup>+</sup> = max _{_ 0 _, U }_ is the positive part of _U_ . Of course, it is a matter of taste whether one uses log(1 + _U_<sup>+</sup> ) or log<sup>+</sup> _U_ .

**Definition 5.2.** A random variable _U_ has an algebraic tail if there are positive, finite constants _α_ , _β_ such that Prob _{U > u} < α/u_<sup>_β_</sup> for all _u >_ 0. This condition has force only for large positive _u_ ; and we allow Prob _{U_ = _−∞} >_ 0.

**5.2. The Main Theorem.** Fix a probability measure _µ_ on _X_ . Assume that

(5.1) _f → Kf_ has an algebraic tail relative to _µ_ .

Fix a reference point _x_ 0 _∈ S_ ; assume too that

(5.2) _f → ζ_ ( _f_ ) = _ρ_ [ _f_ ( _x_ 0) _, x_ 0] has an algebraic tail relative to _µ_ .

If, for instance, _S_ is the line and the _f_ ’s are linear, condition (5.1) constrains the slopes and then (5.2) constrains the intercepts. As will be seen later, any reference point in _S_ may be used.

Consider a Markov chain moving around in _S_ according to the following rule: starting from _x ∈ S_ , the chain chooses _f ∈X_ at random from _µ_ and goes to _f_ ( _x_ ). We say that the chain “moves according to _µ_ ”, or “ _µ_ is the move measure”; in Section 1, this Markov chain was called “the forward iteration”.

ITERATED RANDOM FUNCTIONS

17

**Theorem 5.1.** _Suppose µ is a probability on the Lipschitz functions. Suppose conditions (5.1) and (5.2) hold. Suppose further that_


_the integral may be −∞. Consider a Markov chain on S that moves according to µ. Let Pn_ ( _x, dy_ ) _be the law of the chain after n moves starting from x._

- (i) _There is a unique invariant probability π._

- (ii) _There is a positive, finite constant Ax and an r with_ 0 _< r <_ 1 _such that ρ_ [ _Pn_ ( _x, ·_ ) _, π_ ] _≤ Axr_<sup>_n_</sup> _for all n_ = 1 _,_ 2 _, . . . and x ∈ S._

- (iii) _The constant r does not depend on n or x; the constant Ax does not depend on n, and Ax < a_ + _bρ_ ( _x, x_ 0) _where_ 0 _< a, b < ∞._

In (ii) and (iii), _ρ_ is the Prokhorov metric (Definition 5.1). The argument for Theorem 5.1 can be sketched as follows. Although the forward process


does not converge as _n →∞_ , the backward process—with the composition in reverse order—does converge. Thus, we consider

(5.4) _Yn_ ( _x_ ) = ( _f_ 1 _◦ f_ 2 _◦· · · ◦ fn_ )( _x_ ) _._

The main step will be the following.

**Proposition 5.1.** _Assume (5.1–2–3). Define the backward process {Yn_ ( _x_ ) _} by (5.4). Then Yn_ ( _x_ ) _converges at a geometric rate as n →∞ to a random limit that does not depend on the starting point x._

To realize the stationary process, let


be independent with common distribution _µ_ , and let

(5.6) _Wm_ = _fm ◦ fm−_ 1 _◦ fm−_ 2 _◦· · · ,_

where the composition “goes all the way”. Rigor will come after some preliminary lemmas, and it will be seen that the process _{Wm}_ is stationary with the right transition law.

**Lemma 5.2.** _Let ξi be i.i.d random variables; P {ξi_ = _−∞} >_ 0 _is allowed. Suppose there are positive, finite constants α, β such that P {ξi > v} < αe_<sup>_−βv_</sup> _for all v >_ 0 _. Let ξ be distributed as ξi. Then_

- (i) _−∞≤ E{ξ} < ∞._

- (ii) _If c is a finite real number with c > E{ξ}, there are positive, finite constants A and r such that r <_ 1 _and P {ξ_ 1+ _· · ·_ + _ξn > nc} < Ar_<sup>_n_</sup> _for all n_ = 1 _,_ 2 _, . . . . The constants A and r depend on c and the law of ξ, not on n._

18 PERSI DIACONIS AND DAVID FREEDMAN

Proof. _Case 1._ Suppose _ξ_ is bounded below. Then (i) is immediate, with _−∞ < m < ∞_ ; (ii) is nearly standard, but we give the argument anyway. First, _E{_ exp( _λξ_ ) _} < ∞_ for _−∞ < λ < β_ . Next, let _m_ = _E{ξ}_ . We claim that


Indeed, fix _γ_ with 0 _< γ < β_ ; let _|t| <_ 1 and _λ_ = _tγ_ . Then _|λ| < γ_ , so


The right hand side of (5.8) has finite expected value, proving (5.7). As a result, there are positive constants _λ_ 0 and _d_ for which


provided 0 _≤ λ ≤ λ_ 0. Let


By Markov’s inequality,


If 0 _≤ λ ≤ λ_ 0, we have a bound on _rλ,c_ . Set _λ_ = ( _c − m_ ) _/_ 2 _d_ to complete the proof in Case 1, with _r_ = exp[ _−_ ( _c − m_ )<sup>2</sup> _/_ 4 _d_ ]. This is legitimate provided _m ≤ c ≤ c_ 0 = _m_ + 2 _dλ_ 0. Larger values of _c_ may be replaced by _c_ 0.

_Case 2._ Let _ξi_<sup>_′_be</sup><sup>_ξi_truncatedbelowataconstantthatdoesnotdependon</sup><sup>_i_.</sup> Then<sup>�</sup> _i_<sup>_ξi≤_�</sup> _i_<sup>_ξ_</sup> _i_<sup>_′_.Case1appliestothetruncatedvariables,whosemeanwillbe</sup> less than _c_ if the truncation point is sufficiently negative. Our idea of truncation can be defined by example: _x_ truncated below at _−_ 17 equals _x_ if _x ≥−_ 17, and _−_ 17 if _x ≤−_ 17. Q.E.D.

Let _fn_ be an i.i.d. sequence of picks from _µ_ . Fix _x ∈ S_ . Consider the forward process starting from _x_ :


**Lemma 5.3.** _ρ_ [ _Xn_ ( _x_ ) _, Xn_ ( _y_ )] _≤_ �� _nj_ =1<sup>_Kfj_</sup> � _ρ_ ( _x, y_ ) _._

Proof. This is obvious for _n_ = 0 and _n_ = 1. Now


The next two lemmas will prove the uniqueness part of Theorem 5.1.

ITERATED RANDOM FUNCTIONS

19

**Lemma 5.4.** _Suppose (5.1) and (5.3). If ε >_ 0 _is sufficiently small, there are positive, finite constants A and r with r <_ 1 _and_


_for all n_ = 1 _,_ 2 _, . . . . The constants A and r depend on ε but not on n._

Proof. Apply Lemma 5.2 to the random variables _ξi_ = log _Kfi_ .

Q.E.D.

**Lemma 5.5.** _Suppose (5.1) and (5.3). For sufficiently small positive ε: except for a set of f_ 1 _, . . . , fn of probability less than Ar_<sup>_n_</sup> _, ρ_ [ _Xn_ ( _x_ ) _, Xn_ ( _y_ )] _≤_ exp( _−nε_ ) _ρ_ ( _x, y_ ) _for all x, y ∈ S. Again, A and r depend on ε but not on n._

Proof. Use Lemmas 5.3 and 5.4.


**Corollary 5.1.** _There is at most one invariant probability._

Proof. Suppose _π_ and _π_<sup>_′_</sup> were invariant. Choose _x_ from _π_ and _x_<sup>_′_</sup> from _π_<sup>_′_</sup> , independently. Let _Yn_ = _Xn_ ( _x_ ) and _Yn_<sup>_′_=</sup><sup>_Xn_(</sup><sup>_x′_).Now</sup><sup>_ρ_(</sup><sup>_Yn, Y_</sup> _n_<sup>_′_)</sup><sup>_≤_exp(</sup><sup>_−nε_)</sup><sup>_ρ_(</sup><sup>_Y_0</sup><sup>_, Y_</sup> 0<sup>_′_)</sup> except for a set of exponentially small probability. So, the laws of _Yn_ and _Yn_<sup>_′_merge;</sup> but the former is _π_ and the latter is _π_<sup>_′_</sup> . Q.E.D.

The next lemma gives some results on variables with algebraic tails, leading to a proof that if (5.1) holds, and (5.2) holds for some particular _x_ 0, then (5.2) holds for all _x_ 0 _∈ S_ . The lemma and its corollary are only to assist the interpretation.

**Lemma 5.6.**

- (i) _If U is non-negative and bounded above, then U has an algebraic tail._

- (ii) _If U has an algebraic tail and c >_ 0 _, then cU has an algebraic tail._

- (iii) _If U and V have algebraic tails, so does U_ + _V ; these random variables may be dependent. (In principle, there are two α’s and two β’s; it is convenient to use the larger α and the smaller β, if both of the latter are positive.)_

Proof. Claims (i) and (ii) are obvious. For claim (iii),


**Corollary 5.2.** _Suppose condition (5.1) holds. If (5.2) holds for any particular x_ 0 _∈ S, then (5.2) holds for any x_ 0 _∈ S. In other words, there are finite positive constants α, β with µ{ f_ : _ρ_ [ _f_ ( _x_ 0) _, x_ 0] _> u } < α/u_<sup>_β_</sup> _for all u >_ 0 _. The constant α may depend on x_ 0 _, but the shape parameter β does not._

Proof. Use Lemma 5.6 and the triangle inequality.


**Lemma 5.7.** _Let f and g be mappings of S into itself; let x ∈ S. Then_


Proof. By the triangle inequality,


Now use the definition of _Kf_ . Q.E.D.

20 PERSI DIACONIS AND DAVID FREEDMAN

**Corollary 5.3.** _Let {gi} be mappings of S into itself; let x ∈ S. Then_


**Proof of Proposition 5.1.** We assume conditions (5.1–3) and consider the behavior when _n →∞_ of the backward iterations _Yn_ ( _x_ ) = ( _f_ 1 _◦ f_ 2 _◦· · · ◦ fn_ )( _x_ ). Convergence of _Yn_ ( _x_ ) as _n →∞_ will follow from the Cauchy criterion. In view of Lemma 5.5, it is enough to consider _x_ = _x_ 0. As in Lemma 5.3,

(5.10) _ρ_ [ _Yn_ + _m_ ( _x_ ) _, Yn_ ( _x_ )] _≤ Kf_ 1 _· · · Kfnρ_ [( _fn_ +1 _◦ fn_ +2 _◦· · · ◦ fn_ + _m_ )( _x_ ) _, x_ ] _._

We use Corollary 5.3 with _fn_ + _i_ for _gi_ to bound the right hand side of (5.10), concluding that


By Lemma 5.4, except for a set of probability _A_<sup>_′_</sup> _r_<sup>_n_0</sup> ,


for all _n ≥ n_ 0 and all _i_ = 0 _,_ 1 _, . . ._ .

Next, condition (5.2) comes into play. Write _ζj_ = _ρ_ [ _fj_ ( _x_ ) _, x_ ]. By the Definition 5.2 of algebraic tails, there are positive finite constants _α_ and _β_ such that _P {ζj > s_<sup>_j_</sup> _} < α/s_<sup>_βj_</sup> . Choose _s >_ 1 but so close to 1 that _se_<sup>_−ε_</sup> _<_ 1. Except for another set of exponentially small probability,

(5.13)


for all _n ≥ n_ 0 and all _i_ = 0 _,_ 1 _, . . . ._ Now there are finite positive constants _c_ 0, _r_ 0, _r_ 1, with _r_ 0 _<_ 1 and _r_ 1 _<_ 1, such that for all _n_ 0, for all _n ≥ n_ 0, and all _m_ = 0 _,_ 1 _, . . . ,_


except for a set of probability _c_ 0 _r_ 0<sup>_n_0.Thus,</sup><sup>_Yn_(</sup><sup>_x_)isCauchy,andhenceconverges</sup> to a limit in _S_ . We have already established that the limit does not depend on _x_ ; call the limit _Y∞_ . An exponential rate for the convergence of _Yn_ ( _x_ ) to _Y∞_ follows by letting _m →∞_ in (5.14). Q.E.D.

ITERATED RANDOM FUNCTIONS

21

**Lemma 5.8.** _Let X, X_<sup>_′_</sup> _be random mappings into S, with distributions λ, λ_<sup>_′_</sup> _. Suppose X, X_<sup>_′_</sup> _can be realized so that P {ρ_ ( _X, X_<sup>_′_</sup> ) _≥ δ} < δ. Then ρ_ ( _λ, λ_<sup>_′_</sup> ) _≤ δ. (In the first instance, ρ is the metric on S; in the second, ρ is the induced Prokhorov metric on probabilities: see Definition 5.1.)_

Proof. Let _C_ be a compact subset of _S_ . Then _X ∈ C_ entails _X_<sup>_′_</sup> _∈ Cδ_ , except for probability _δ_ . Likewise, _X_<sup>_′_</sup> _∈ C_ entails _X ∈ Cδ_ , except for probability _δ_ . Q.E.D.

**Remark.** The converse to Lemma 5.8 is true too: one proof goes by discretization and the “Marriage Lemma”. See Strassen (1965) or Dudley (1988, Chapter 11).

**Proof of Theorem 5.1.** There are only a few details to clean up. Recall the doubly-infinite sequence _{fi}_ from (5.5). By Proposition 5.1, we can define _Wm_ as follows:


The limit does not depend on _x_ . Proposition 5.1 applies, because—as before—


It is easy to verify that


is stationary with the right transition probabilities. And _Y∞_ is distributed like any of the _Wm_ . Thus, the convergence assertion (ii) in Theorem 5.1 follows from Lemma 5.8 and Proposition 5.1. The argument is complete.

**Proof of Theorem 1 and Proposition 1.** These results are immediate from Proposition 5.1 and Theorem 5.1. Indeed, the moment conditions in Theorem 1 imply conditions (5.1–2–3); we stated Theorem 1 using the more restrictive conditions in order to postpone technicalities.

Figure 4. The backward iterations converge rapidly to a limit that is random but does not depend the starting state.


<!-- Start of picture text -->
1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0 5 10 15 20 25<br><!-- End of picture text -->


<!-- Start of picture text -->
1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0 5 10 15 20 25<br><!-- End of picture text -->

PERSI DIACONIS AND DAVID FREEDMAN

22

The essence of the thing is that the backward iterations converge at a geometric rate to a limit that depends on the functions being composed—but not on the starting point. Figure 4 illustrates the idea for the Markov chain discussed in Section 2.1. The left hand panel shows the backward iteration starting from _x_ 0 = 1 _/_ 3 or _x_ 0 = 2 _/_ 3. Exactly the same functions are used to generate the two paths; the only difference is the starting point. (Position at time _n_ is plotted against _n_ = 0 _,_ 1 _, . . . ,_ 25, with linear interpolation.) The paths merge for all practical purposes around _n_ = 7. The right hand panel shows the same thing, with a new lot of random functions. Convergence is even faster, but the limit is different—randomness in action. (By contrast, the forward iteration does not converge, but wanders around ergodically in the state space: Figure 1.) Figure 5 plots the logarithm (base 10) of the absolute difference between the paths in the corresponding panels of Figure 4. The linear decay on the log scale corresponds to exponential decay on the original scale. The difference in slopes between the two panels is due to the randomness in choice of functions; this difference wears off as the number of iterations goes up.

Figure 5. Logarithm to base 10 of the absolute difference between paths in the backward iteration.


<!-- Start of picture text -->
5 10 15 20 25 5 10 15 20 25<br>–5 –5<br>–10 –10<br>–15 –15<br><!-- End of picture text -->

---

[← Lemma 5.1.](03-lemma-5-1.md) · [Up: contents](index.md) · [Remarks. →](05-remarks.md)
