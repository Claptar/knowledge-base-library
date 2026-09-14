---
title: 'Appendix I: Hints and solutions for selected exercises'
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Appendix I: Hints and solutions for selected exercises

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this section we give hints, solutions or additional references for the exercises marked with either of the symbols ( _∗_ ) or ( _∗∗_ ) in the main body of the text.

**Exercise 1.2.** Fix times 0 _< t_ 1 _< . . . < tn_ . Let


Then, for a Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ with start in _x_ , by definition, the vector


has independent standard normal entries. As both _D_ and _M_ are nonsingular, the matrix _A_ := _M_<sup>_−_1</sup> _D_<sup>_−_1</sup> is well-defined and, denoting also _b_ = ( _x, . . . , x_ ), we have that


By definition, this means that ( _B_ ( _t_ 1) _, . . . , B_ ( _tn_ )) is a Gaussian random vector.

**Exercise 1.4.** Note that _{X_ ( _t_ ): 0 _≤ t ≤_ 1 _}_ is a Gaussian process, while the distributions given in (a) determine Gaussian random vectors. Hence it suffices to identify the means and covariances of ( _X_ ( _t_ 1) _, . . . , X_ ( _tn_ )) and compare them with those given in (a). Starting with the mean, on the one hand we obviously have E _X_ ( _t_ ) = _x_ (1 _− t_ ) + _ty_ , on the other hand


and the integral can be seen to vanish by completing the square in the exponent of the integrand. To perform the covariance calculation one may assume that _x_ = _y_ = 0, which reduces the complexity of expressions significantly, see [ **Du96** , (8.5) in Chapter 7] for more details.

311

**Exercise 1.5.** _B_ ( _t_ ) does not oscillate too much between _n_ and _n_ + 1 if


Use the Borel-Cantelli lemma and a suitable estimate for


to obtain this result.

**Exercise 1.6.** One has to improve the lower bound, and show that, for every constant _c < √_ 2, almost surely, there exists _ε >_ 0 such that, for all 0 _< h < ε_ , there exists _t ∈_ [0 _,_ 1 _− h_ ] with


Then, using Lemma II.3.1, for any _k ≥_ 0,


Therefore, by our assumption on _c_ , and using that 1 _− x ≤ e_<sup>_−x_</sup> for all _x ≥_ 0,

From the Borel-Cantelli lemma we thus obtain that, almost surely, there exists _n_ 0 _∈_ N such that, for all _n ≥ n_ 0, there exists _t ∈_ [0 _,_ 1 _− e_<sup>_−_</sup><sup>_~~√~~_</sup> _<u>n</u>_ ] of the form _t_ = _ke−_<sup>_~~√~~_</sup> _<u>n</u>_ such that


In addition, we may choose _n_ 0 big enough to ensure that _e_<sup>_−_</sup><sup>_~~√~~_</sup> _~~n~~_ 0 is sufficiently small in the sense of Theorem 1.12. Then we pick _ε_ = _e_<sup>_−√_</sup> _~~n~~_ 0 and, given 0 _< h < ε_ , choose _n_ such that _e_<sup>_−_</sup><sup>_~~√~~_</sup> _n_ +1 _< h ≤ e−_<sup>_~~√~~_</sup> _<u>n</u>_ . Then, for _t_ as above,


It is not hard to see that the second (subtracted) term decays much more rapidly than the first, so that modifying _n_ 0 to ensure that it is below _δ_ (<sup>_√_</sup> _<u>ne</u>_<sup>_−√_</sup> _<u>n</u>_ ) <u>12</u> gives the result.

312

**Exercise 1.7.** It suffices to show that, for fixed _ε >_ 0 and _c >_ 0, almost surely, for all _t ≥_ 0, there exists 0 _< h < ε_ with _|B_ ( _t_ + _h_ ) _− B_ ( _t_ ) _| > ch_<sup>_α_</sup> . By Brownian scaling we may further assume _ε_ = 1. Note that, after this simplification, the complementary event means that there is a _t_ 0 _≥_ 0 such that


We may assume that _t_ 0 _∈_ [0 _,_ 1). Fix _l ≥_ 1 _/_ ( _α −_ 2<sup><u>1</u>).Then</sup><sup>_t_0</sup><sup>_∈_</sup> � _<u>k</u>_ 2 _−_<sup>_n_</sup> <u>1</u><sup>_,_</sup> 2<sup>_<u>kn</u>_</sup> � for any large _n_ and some 0 _≤ k <_ 2<sup>_n_</sup> _− l_ . Then, by the triangle inequality, for all _j ∈{_ 1 _, . . . ,_ 2<sup>_n_</sup> _− k}_ ,


Now, for any 0 _≤ k <_ 2<sup>_n_</sup> _− l_ , let Ω _n,k_ be the event


It suffices to show that, almost surely for all sufficiently large _n_ and all _k ∈{_ 0 _, . . . ,_ 2<sup>_n_</sup> _− l}_ the event Ω _n,k_ does not occur. Observe that


since the normal density is bounded by 1/2. Hence, for a suitable constant _C_ ,

which is summable. Thus


This is the required statement and hence the proof is complete.

**Exercise 1.8.** The proof can be found in [ **Du95** , Chapter 3] or [ **Ka02** , Theorem 3.15].

**Exercise 1.10.** Argue as in the proof of Theorem 1.30 with _B_ replaced by _B_ + _f_ . The resulting term


can be estimated in exactly the same manner as for the unshifted Brownian motion.

313

**Exercise 1.11.** This can be found, together with stronger and more general results, in [ **BP84** ]. Put _I_ = � _B_ (1) _,_ sup0 _≤s≤_ 1 _B_ ( _s_ )� _,_ and define a function _g_ : _I →_ [0 _,_ 1] by setting


First check that almost surely the interval _I_ is non-degenerate, _g_ is strictly decreasing, left continuous and satisfies _B_ ( _g_ ( _x_ )) = _x_ . Then show that almost surely the set of discontinuities of _g_ is dense in _I_ . We restrict our attention to the event of probability 1 on which these assertions hold. Let


Now show that _Vn_ is open and dense in _I_ . By the Baire category theorem, _V_ :=<sup>�</sup> _n_<sup>_Vn_</sup> is uncountable and dense in _I._ Now if _x ∈ V_ then there is a sequence _xn ↑ x_ such that _g_ ( _xn_ ) _− g_ ( _x_ ) _> n_ ( _x − xn_ ) _._ Setting _t_ = _g_ ( _x_ ) and _tn_ = _g_ ( _xn_ ) we have _tn ↓ t_ and _tn − t > n_ ( _B_ ( _t_ ) _− B_ ( _tn_ )) _,_ from which it follows that _D_<sup>_∗_</sup> _B_ ( _t_ ) _≥_ 0 _._ On the other hand _D_<sup>_∗_</sup> _B_ ( _t_ ) _≤_ 0 since _B_ ( _s_ ) _≤ B_ ( _t_ ) for all _s ∈_ ( _t,_ 1) _,_ by definition of _t_ = _g_ ( _x_ ) _._

**Exercise 1.12.** We first fix some positive _ε_ and positive _a_ . For some small _h_ and an interval _I ⊂_ [ _ε,_ 1 _− ε_ ] with length _h_ , we consider the event _A_ that _t_ 0 _∈ I_ and we have


We now denote by _tL_ the left endpoint of _I_ . Using Theorem 1.12 we see there exists some positive _C_ so that


Hence the event _A_ implies the following events


We now define _T_ := inf( _s > tL_ + _h_<sup>1</sup><sup>_/_4</sup> : _B_ ( _s_ ) _> B_ ( _t_ ) _−_ 2 _ah_<sup>1</sup><sup>_/_4</sup> ). Then by definition we have that _T ≤ tL_ + 2 _h_<sup>1</sup><sup>_/_4</sup> and this implies the event


Now by the strong Markov property, these three events are independent and we obtain


We estimate the probabilities of these three events and obtain


Hence we obtain, for a suitable constant _K >_ 0, depending on _a_ and _ε_ , that


314

Summing over a covering collection of 1 _/h_ intervals of length _h_ gives the bound


Taking _h_ = 2<sup>_−_4</sup><sup>_n−_4</sup> in this bound and summing over _n_ , we see that


and from the Borel-Cantelli lemma we obtain that, almost surely, either _t_ 0 _̸ ∈_ [ _ε,_ 1 _− ε_ ], or


Now recall that _a_ and _ε_ are arbitrary positive numbers, so taking a countable union over _a_ and _ε_ gives that, almost surely, _D_<sup>*</sup> _B_ ( _t_ 0) = _−∞_ , as required.

**Exercise 1.13** By Brownian scaling it suffices to consider the case _t_ = 1.

( _a_ ) We first show that, given _M >_ 0 large, for any fixed point _s ∈_ [0 _,_ 1], almost surely there exists _n ∈_ N such that the dyadic interval _I_ ( _n, s_ ) := [ _k_ 2<sup>_−n_</sup> _,_ ( _k_ + 1)2<sup>_−n_</sup> ] containing _s_ satisfies

( _∗_ )


To see this, it is best to consider the construction of Brownian motion, see Theorem 1.4. Using the notation of that proof, let _d_ 0 = 1 and _dn_ +1 _∈Dn_ +1 _\ Dn_ be the dyadic point that splits the interval [ _k_ 2<sup>_−n_</sup> _,_ ( _k_ +1)2<sup>_−n_</sup> ) containing _s_ . This defines a sequence _Zdn, n_ = 0 _,_ 1 _, . . ._ of independent, normally distributed random variables. Now let


which is almost surely well-defined. Moreover,


where _±_ indicates that the inequality holds with either choice of sign. This implies that either _I_ ( _n, s_ ) or _I_ ( _n −_ 1 _, s_ ) satisfies ( _∗_ ). We denote by _N_ ( _s_ ) be the smallest nonnegative integer _n_ , for which ( _∗_ ) holds.

By Fubini’s theorem, almost surely, we have _N_ ( _s_ ) _< ∞_ for almost every _s ∈_ [0 _,_ 1]. On this event, we can pick a finite collection of disjoint dyadic intervals [ _t_ 2 _j, t_ 2 _j_ +1], _j_ = 0 _, . . . , k −_ 1, with summed lengths exceeding 1 _/_ 2, say, such that the partition 0 = _t_ 0 _< · · · < t_ 2 _k_ = 1 given by their endpoints satisfies


from which ( _a_ ) follows, as _M_ was arbitrary.

315

( _b_ ) Note that the number of (finite) partitions of [0 _,_ 1] consisting of dyadic points is countable. Hence, by ( _a_ ), given _n ∈_ N, we can find a finite set _Pn_ of partitions such that the probability that there exists a partition 0 = _t_ 0 _< · · · < tk_ = 1 in _Pn_ with the property that


is bigger than 1 _− n_<sup><u>1</u>.Successivelyenumeratingthepartitionsin</sup><sup>_P_1</sup><sup>_, P_2</sup><sup>_, . . ._yieldsasequence</sup> satisfying the requirement of ( _b_ ).

**Exercise 1.14** To see convergence in the _L_<sup>2</sup> -sense one can use the independence of the increments of a Brownian motion,


Now, using that the fourth moments of a centred normal distribution with variance _σ_<sup>2</sup> is 3 _σ_<sup>4</sup> , this can be estimated by a constant multiple of


which goes to zero. Moreover, by the Markov inequality

and summability of the right hand side together with the Borel-Cantelli lemma ensures almost sure convergence.

**Exercise 2.3.** We first show that, given two disjoint closed time intervals, the maxima of Brownian motion on them are different almost surely. For this purpose, let [ _a_ 1 _, b_ 1] and [ _a_ 2 _, b_ 2] be two fixed intervals with _b_ 1 _< a_ 2. Denote by _m_ 1 and _m_ 2, the maxima of Brownian motion on these two intervals. Applying the Markov property at time _b_ 1 we see that the random variable _B_ ( _a_ 2) _− B_ ( _b_ 1) is independent of _m_ 1 _− B_ ( _b_ 1). Using the Markov property at time _a_ 2 we see that _m_ 2 _− B_ ( _a_ 2) is also independent of both these variables. Conditioning on the values of the random variables _m_ 1 _− B_ ( _b_ 1) and _m_ 2 _− B_ ( _a_ 2), the event _m_ 1 = _m_ 2 can be written as

_B_ ( _a_ 2) _− B_ ( _b_ 1) = _m_ 1 _− B_ ( _b_ 1) _−_ ( _m_ 2 _− B_ ( _a_ 2)) _._

The left hand side being a continuous random variable, and the right hand side a constant, we see that this event has probability 0.

Now the statement just proved holds jointly for all disjoint pairs of intervals with rational endpoints. The proposition follows, since if Brownian motion has a non-strict local maximum, there are two disjoint rational intervals where Brownian motion has the same maximum.

316

**Exercise 2.4. (i)** If _A ∈F_ ( _S_ ), then _A ∩{T ≤ t}_ = ( _A ∩{S ≤ t}_ ) _∩{T ≤ t} ∈F_<sup>+</sup> ( _t_ ) _._ **(ii)** By (i), _F_ ( _T_ ) _⊂F_ ( _Tn_ ) for all _n_ , which proves _⊂_ . On the other hand, if _A ∈_<sup>�</sup><sup>_∞_</sup> _n_ =1<sup>_F_(</sup><sup>_Tn_),</sup> then for all _t ≥_ 0,


**(iii)** Look at the discrete stopping times _Tn_ defined in the previous example. We have, for any Borel set _A ⊂_ R<sup>_d_</sup> ,


Hence _B_ ( _Tn_ ) is _F_ ( _Tn_ )-measurable, and as _Tn ↓ T_ , we get that _B_ ( _T_ ) = lim _B_ ( _Tn_ ) is _F_ ( _Tn_ )- measurable for any _n_ . Hence _B_ ( _T_ ) is _F_ ( _T_ )-measurable by part (ii).

**Exercise 2.5.** If _T_ = 0 almost surely, there is nothing to show, hence we may assume E[ _T_ ] _>_ 0. (a) By construction, _Tn_ is the sum of _n_ independent random variables with the law of _T_ , hence, by the law of large numbers, almost surely,


which, by assumption, is finite. This implies, in particular, that _Tn →∞_ almost surely, and together with the law of large numbers for Brownian motion, Corollary 1.11, we get almost surely, lim _n→∞ B_ ( _Tn_ ) _/Tn_ = 0 _._ The two limit statements together show that, almost surely,


(b) Again by construction, _B_ ( _Tn_ ) is the sum of _n_ independent random variables with the law of _B_ ( _T_ ), which we conveniently denote _X_ 1 _, X_ 2 _, . . ._ . As


the event _{|Xn| ≥ n}_ occurs only finitely often, so that the Borel-Cantelli lemma implies


Hence we have that


(c) By the law of large numbers, almost surely,


317

**Exercise 2.7.** Let _S_ be a nonempty, closed set _S_ with no isolated points. To see that it is uncountable, we construct a subset with the cardinality of _{_ 1 _,_ 2 _}_<sup>N</sup> . Start by choosing a point _x_ 1 _∈ S_ . As this point is not isolated there exists a further, different point _x_ 2 _∈ S_ . Now pick two disjoint closed balls _B_ 1 _, B_ 2 around these points. Again, as _x_ 1 is not isolated, we can find two points in _B_ 1 _∩ S_ , around which we can put disjoint balls contained in _B_ 1 _∩ S_ , similarly for _B_ 2 _∩ S_ , and so on. Now there is a bijection between _{_ 1 _,_ 2 _}_<sup>N</sup> and the decreasing sequences of balls in our construction. The intersection of the balls in each such sequence contains, as _S_ is closed, at least one point of _S_ , and two points belonging to two different sequences are clearly different. This completes the proof.

**Exercise 2.11.** By Fubini’s theorem,


Note that, by Brownian scaling, P _{M_ ( _x_<sup>1</sup><sup>_/α_</sup> ) _<_ 1 _} ≤ C x_<sup>_−_</sup> 2<sup><u>1</u></sup> _α_ for a suitable constant _C >_ 0, which implies that E[ _T_<sup>_α_</sup> ] _< ∞_ , as required.

**Exercise 2.14.** By Exercise 2.13 the process _{X_ ( _t_ ): _t ≥_ 0 _}_ defined by


defines a martingale. Observe that _T_ = inf _{t >_ 0: _B_ ( _t_ ) = _a_ + _bt}_ is a stopping time for the natural filtration, which is finite exactly if _B_ ( _t_ ) = _a_ + _bt_ for some _t >_ 0. Then


and because _{X_<sup>_T_</sup> ( _t_ ): _t ≥_ 0 _}_ is bounded, the right hand side equals _e_<sup>_−_2</sup><sup>_ab_</sup> .

**Exercise 2.15.** Use the binomial expansion of ( _B_ ( _t_ ) + ( _B_ ( _t_ + _h_ ) _− B_ ( _t_ )))<sup>3</sup> to deduce that _X_ ( _t_ ) = _B_ ( _t_ )<sup>3</sup> _−_ 3 _tB_ ( _t_ ) defines a martingale. We know that P _x{TR < T_ 0 _}_ = _x/R_ . Write _τ∗_ = _τ_ ( _{_ 0 _, R}_ ). Then


Solving the last equation for _γ_ gives the claim.

**Exercise 2.18.** Part (a) can be proved similarly to Theorem 2.47, which in fact is the special case _λ_ = 0 of this exercise. For part (b) choose _u_ : _U →_ R as a bounded solution of


with _x_ lim _→x_ 0<sup>_u_(</sup><sup>_x_) =</sup><sup>_f_(</sup><sup>_x_0)forall</sup><sup>_x_0</sup><sup>_∈∂U_.Then</sup>


318

defines a martingale. For any compact _K ⊂ U_ we can pick a twice continuously differentiable function _v_ : R<sup>_d_</sup> _→_ R with _v_ = _u_ on _K_ and _v_ = 0 on _U_<sup>c</sup> Apply the optional stopping theorem to stopping times _S_ = 0, _T_ = inf _{t ≥_ 0: _B_ ( _T_ ) _̸ ∈ K}_ . to get, for every _x ∈ K_ ,


Now choose a sequence _Kn ↑ U_ of compacts and pass to the limit on the right hand side of the equation.

**Exercise 3.2.** To prove the result for _k_ = 1 estimate _|u_ ( _x_ ) _− u_ ( _y_ ) _|_ in terms of _| x − y|_ using the mean value formula for harmonic functions and the fact that, if _x_ and _y_ are close, the volume of the symmetric difference of _B_ ( _x, r_ ) and _B_ ( _y, r_ ) is bounded by a constant multiple of _r_<sup>_d−_1</sup> _| x−y|_ . For general _k_ note that the partial derivatives of a harmonic function are themselves harmonic, and iterate the estimate.

**Exercise 3.4.** Define a random variable _Y_ by _Y_ := _X_ , if _X > λ_ E[ _X_ ], and _Y_ := 0, otherwise. Applying the Cauchy-Schwarz inequality to E[ _Y_ ] = E[ _Y_ 1 _{Y >_ 0 _}_ ] gives


hence, as _X ≥ Y ≥ X − λ_ E[ _X_ ], we get

**Exercise 3.6.** For _d ≥_ 3, choose _a_ and _b_ such that _a_ + _br_<sup>2</sup><sup>_−d_</sup> = _u_ ˜( _r_ ) _,_ and _a_ + _bR_<sup>2</sup><sup>_−d_</sup> = _u_ ˜( _R_ ) _._ Notice that the harmonic functions given by _u_ ( _x_ ) = _u_ ˜( _| x|_ ) and _v_ ( _x_ ) = _a_ + _b| x|_<sup>2</sup><sup>_−d_</sup> agree on _∂D_ . They also agree on _D_ by Corollary 3.7. So _u_ ( _x_ ) = _a_ + _b| x|_<sup>2</sup><sup>_−d_</sup> . By similar consideration we can show that _u_ ( _x_ ) = _a_ + _b_ log _| x|_ in the case _d_ = 2.

**Exercise 3.7.** Let _x, y ∈_ R<sup>_d_</sup> , _a_ = _| x − y|_ . Suppose _u_ is a positive harmonic function. Then


This converges to _u_ ( _y_ ) as _R →∞_ , so _u_ ( _x_ ) _≤ u_ ( _y_ ), and by symmetry, _u_ ( _x_ ) = _u_ ( _y_ ) for all _x, y_ . Hence _u_ is constant.

**Exercise 3.8.** Uniqueness is clear, because there is at most one _continuous_ extension of _u_ . Let _D_ 0 _⊂ D_ be a ball whose closure is contained in _D_ , which contains _x_ . _u_ is bounded and harmonic on _D_ 1 = _D_ 0 _\ {x}_ and continuous on _D_ 1 _\ {x}_ . Show that this already implies that _u_ ( _z_ ) = E _z_ [ _u_ ( _τ_ ( _D_ 1))] on _D_ 1 and that the right hand side has an obvious harmonic extension to _D_ 1 _∪{x}_ , which defines the global extension.

319

**Exercise 3.12.** To obtain joint continuity one can show equicontinuity of _G_ ( _x, ·_ ) and _G_ ( _· , x_ ) in _D \ B_ ( _x, ε_ ) for any _ε >_ 0. This follows from the fact that these functions are harmonic, by Exercise 3.11, and the estimates of Exercise 3.2.

**Exercise 3.13.** Recall that


The expectation can be evaluated (one can see how in the proof of Theorem 3.43). The final answer is


**Exercise 3.14.** Suppose _x, y̸ ∈ B_ (0 _, r_ ) and _A ⊂B_ (0 _, r_ ) compact. Then, by the strong Markov property applied to the first hitting time of _∂B_ (0 _, r_ ),


Use Theorem 3.43 to show that, for _B ⊂ A_ Borel, _µ∂B_ (0 _,r_ )( _x, B_ ) _≤ Cµ∂B_ (0 _,r_ )( _y, B_ ) for a constant _C_ not depending on _B_ . Complete the argument from there.

**Exercise 4.1.** Let _α_ = log 2 _/_ log 3. For the upper bound it suffices to find an efficient covering of _C_ by intervals of diameter _ε_ . If _ε ∈_ (0 _,_ 1) is given, let _n_ be the integer such that 1 _/_ 3<sup>_n_</sup> _<_ 2 _ε ≤_ 1 _/_ 3<sup>_n−_1</sup> and look at the sets


These sets obviously cover _C_ and each of them is contained in an open ball centred in an interval of diameter 2 _ε_ . Hence


This implies dim _M C ≤ α ._

For the lower bound we may assume we have a covering by intervals ( _xk − ε, xk_ + _ε_ ), with _xk ∈ C_ , and let _n_ be the integer such that 1 _/_ 3<sup>_n_+1</sup> _≤_ 2 _ε <_ 1 _/_ 3<sup>_n_</sup> . Let _xk_ =<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_xi,k_3</sup><sup>_−i_.Then</sup>


and we need at least 2<sup>_n_</sup> sets of the latter type to cover _C_ . Hence,

_M_ ( _C, ε_ ) _≥_ 2<sup>_n_</sup> = 3<sup>_αn_</sup> = (1 _/_ 3)<sup>_α_�</sup> 3<sup>_n_+1�</sup><sup>_α_</sup> _≥_ (1 _/_ 3)<sup>_α_</sup> (1 _/ε_ )<sup>_α_</sup> _._

This implies <u>dim</u> _~~M~~_<sup>_C≥α ._</sup>

320

**Exercise 4.2.** Given _ε ∈_ (0 _,_ 1) find the integer _n_ such that 1 _/_ ( _n_ + 1)<sup>2</sup> _≤ ε <_ 1 _/n_<sup>2</sup> . Then the points in _{_ 1 _/k_ : _k > n} ∪{_ 0 _}_ can be covered by _n_ + 1 intervals of diameter _ε_ . _n_ further balls suffice to cover the remaining _n_ points. Hence


implying dim _M_ ( _E_ ) _≤_ 1 _/_ 2. On the other hand, as the distance between neighbouring points is


we always need at least _n −_ 1 sets of diameter _ε_ to cover _E_ , which implies


hence <u>dim</u> _~~M~~_<sup>(</sup><sup>_E_)</sup><sup>_≥_1</sup><sup>_/_2.</sup>

**Exercise 4.3.** Suppose _E_ is a bounded metric space with <u>dim</u> _~~M~~_<sup>_E<α_.Choose</sup><sup>_ε>_0such</sup> that <u>dim</u> _<u>EM</u> < α − ε_ . Then, for every _k_ there exists 0 _< δ < k_<sup><u>1</u>andacovering</sup><sup>_E_1</sup><sup>_, . . . , En_of</sup><sup>_E_</sup> by sets of diameter at most _δ_ with _n ≤ δ_<sup>_−α_+</sup><sup>_ε_</sup> . The _α_ -value of this covering is at most _nδ_<sup>_α_</sup> _≤ δ_<sup>_ε_</sup> , which tends to zero for large _k_ . Hence _H∞_<sup>_α_(</sup><sup>_E_) = 0,anddim</sup><sup>_E≤α_.</sup>

**Exercise 4.4.** Indeed, as _E ⊂ F_ implies dim _E ≤_ dim _F_ , it is obvious that


To see the converse, we use

Hence,


This proves the converse inequality.

321

**Exercise 4.6.** Suppose that _f_ is surjective and _α_ -H¨older continuous with H¨older constant _C >_ 0, and assume that _H_<sup>_αβ_</sup> ( _E_ 1) _< ∞_ . Given _ε, δ >_ 0 we can cover _E_ 1 with sets _B_ 1 _, B_ 2 _, . . ._ of diameter at most _δ_ such that


Note that the sets _f_ ( _B_ 1) _, f_ ( _B_ 2) _, . . ._ cover _E_ 2 and that _|f_ ( _Bi_ ) _| ≤ C |Bi|_<sup>_α_</sup> _≤ C δ_<sup>_α_</sup> . Hence


from which the claimed result for the Hausdorff measure readily follows.

**Exercise 4.8.** Start with _d_ = 1. For any 0 _< a <_ 1 _/_ 2 let _C_ ( _a_ ) be the Cantor set obtained by iteratively removing from each construction interval a central interval of 1 _−_ 2 _a_ of its length. Note that at the _n_ th level of the construction we have 2<sup>_n_</sup> intervals each of length _a_<sup>_n_</sup> . It is not hard to show that _C_ ( _a_ ) has Hausdorff dimension log 2 _/_ log(1 _/a_ ), which solves the problem for the case _d_ = 1.

For arbitrary dimension _d_ and given _α_ we find _a_ such that dim _C_ ( _a_ ) = _α/d_ . Then the Cartesian product _C_ ( _a_ ) _× . . .d ×C_ ( _a_ ) has dimension _α_ . The upper bound is straightforward, and the lower bound can be verified, for example, from the mass distribution principle, by considering the natural measure that places mass 1 _/_ 2<sup>_dn_</sup> to each of the 2<sup>_dn_</sup> cubes of sidelength _a_<sup>_n_</sup> at the _n_ th construction level.

**Exercise 4.13.** Recall that it suffices to show that _H_<sup>1</sup><sup>_/_2</sup> (Rec) = 0 almost surely. In the proof of Lemma 4.21 the maximum process was use to define a measure on the set of record points: this measure can be used to define ‘big intervals’ analogous to the ‘big cubes’ in the proof of Theorem 4.18. A similar covering strategy as in this proof yields the result.

**Exercise 5.1.** Use the Borel-Cantelli lemma for the events


and test for which values of _a_ the series P( _En_ ) converges. To estimate the probabilities, the reflection principle and Lemma II.3.1 will be useful.

**Exercise 5.2.** The lower bound is immediate from the one-dimensional statement. For the upper bound pick a finite subset _S ⊂ ∂B_ (0 _,_ 1) of directions such that, for every _x ∈ ∂B_ (0 _,_ 1) there exists _x_ ˜ _∈ S_ with _|x − x_ ˜ _| < ε_ . Almost surely, all Brownian motions in dimension one obtained by projecting _{B_ ( _t_ ) : _t ≥_ 0 _}_ on the line determined by the vectors in _S_ satisfy the statement. From this one can infer that the limsup under consideration is bounded from above by 1 + _ε_ .

322

**Exercise 5.3.** Let _Ta_ = inf _{t >_ 0: _B_ ( _t_ ) = _a}_ . The proof of the upper bound can be based on the fact that, for _A <_ 1 and _q >_ 1,


**Exercise 5.4.** Define the stopping time _τ−_ 1 = min _{k_ : _Sk_ = _−_ 1 _}_ and recall the definition of _pn_ from (2.3). Then

_pn_ = P _{Sn ≥_ 0 _} −_ P _{Sn ≥_ 0 _, τ−_ 1 _< n}._ Let _{Sj_<sup>_∗_:</sup><sup>_j≥_0</sup><sup>_}_denotetherandomwalkreflectedattime</sup><sup>_τ−_1,thatis</sup>


Note that if _τ−_ 1 _< n_ then _Sn ≥_ 0 if and only if _Sn_<sup>_∗≤−_2,so</sup>

_pn_ = P _{Sn ≥_ 0 _} −_ P _{Sn_<sup>_∗≤−_2</sup><sup>_}._</sup>

Using symmetry and the reflection principle, we have


which means that


Recall that Stirling’s Formula gives _m_ ! _∼ √_ 2 _πm_<sup>_m_+1</sup><sup>_/_2</sup> _e_<sup>_−m_</sup> , where the symbol _∼_ means that the ratio of the two sides approaches 1 as _m →∞_ . One can deduce from Stirling’s Formula that _pn ∼_ �2 _/πn,_ which proves the result.

**Exercise 5.5.** Denote by _In_ ( _k_ ) the event that _k_ is a point of increase for _S_ 0 _, S_ 1 _, . . . , Sn_ and by _Fn_ ( _k_ ) = _In_ ( _k_ ) _\_<sup>�</sup><sup>_k_</sup> _i_ =0<sup>_−_1</sup><sup>_In_(</sup><sup>_i_)theeventthat</sup><sup>_k_isthefirstsuchpoint.Theeventsthat</sup> _{Sk_ is largest among _S_ 0 _, S_ 1 _, . . . Sk}_ and that _{Sk_ is smallest among _Sk, Sk_ +1 _, . . . Sn}_ are independent, and therefore P( _In_ ( _k_ )) = _pkpn−k_ .

Observe that if _Sj_ is minimal among _Sj, . . . , Sn_ , then any point of increase for _S_ 0 _, . . . , Sj_ is automatically a point of increase for _S_ 0 _, . . . , Sn_ . Therefore for _j ≤ k_ we can write

_Fn_ ( _j_ ) _∩ In_ ( _k_ ) =


The three events on the right-hand side are independent, as they involve disjoint sets of summands; the second of these events is of the type considered in Lemma 5.9. Thus,

P( _Fn_ ( _j_ ) _∩ In_ ( _k_ )) _≥_ P( _Fj_ ( _j_ )) _p_<sup>2</sup> _k−j_<sup>_pn−k_</sup>


since _pn−k ≥ pn−j_ . Here the two events on the right are independent, and their intersection is precisely _Fn_ ( _j_ ). Consequently P( _Fn_ ( _j_ ) _∩ In_ ( _k_ )) _≥ p_<sup>2</sup> _k−j_<sup>P(</sup><sup>_Fn_(</sup><sup>_j_))</sup><sup>_._</sup>

323

Decomposing the event _In_ ( _k_ ) according to the first point of increase gives


This yields an upper bound on the probability that _{Sj_ : _j_ = 0 _, . . . , n}_ has a point of increase by time _n/_ 2; but this random walk has a point of increase at time _k_ if and only if the reversed walk _{Sn − Sn−i_ : _i_ = 0 _, . . . , n}_ has a point of increase at time _n − k_ . Thus, doubling the upper bound given by (0.1) proves the statement.

**Exercise 5.7.** In the proof of Exercise 5.5 we have seen that,


By Lemma 5.9, we have, for _j ≤ k ≤ n_ ,


Thus,


This implies the statement.

**Exercise 5.9.** Suppose that _X_ is an arbitrary random variable with vanishing expectation and finite variance. For each _n ∈_ N divide the intersection of the support of _X_ with the interval [ _−n, n_ ] into finitely intervals with mesh _< n_<sup><u>1</u>.If</sup><sup>_x_1</sup><sup>_< · · · < xm_are the partition points, construct</sup> the law of _Xn_ by placing, for any _j ∈{_ 0 _, . . . , m}_ , atoms of size _P {X ∈_ [ _xj, xj_ +1) _}_ in position _E_ [ _X | xj ≤ X < xj_ +1], using the convention _x_ 0 = _−∞_ and _xm_ +1 = _∞_ . By construction, _Xn_ takes only finitely many values.

Observe that _E_ [ _Xn_ ] = 0 and _Xn_ converges to _X_ in distribution. Moreover, one can show that _τn → τ_ almost surely. This implies that _B_ ( _τn_ ) _→ B_ ( _τ_ ) almost surely, and therefore also in distribution, which implies that _X_ has the same law as _B_ ( _τ_ ). Fatou’s lemma implies that


Hence, by Wald’s second lemma, _E_ [ _X_<sup>2</sup> ] = E[ _B_ ( _τ_ )<sup>2</sup> ] = E[ _τ_ ].

324

**Exercise 6.4.** From Exercise 2.15 we get, for any _x ∈_ (0 _,_ 1) that


and this limit is increasing. Hence


**Exercise 6.5.** Observe that E exp _{λZj}_ = _e_<sup>_λ_</sup> _/_ (2 _− e_<sup>_λ_</sup> ) for all _λ <_ log 2, and hence, for a suitable constant _C_ and all small _λ >_ 0,

E exp � _λ_ ( _Zj −_ 2)� _≤ λ_<sup>2</sup> + _Cλ_<sup>3</sup> _,_ by a Taylor expansion. Using this for _λ_ = 2<sup>_<u>ε</u>_wegetfromChebyshev’sinequality,</sup>


which proves the the more difficult half of the claim. The inequality for the lower tail is obvious.

**Exercise 6.6.** We have that


So the density of the left hand side is

which by Taylor expansion is


325

Recall that _X_<sup>2</sup> _/_ 2 is distributed as Gamma(<sup><u>1</u></sup> 2<sup>),andgiven</sup><sup>_N_thesum�</sup> _i_<sup>_N_</sup> =1<sup>_Zi_isdistributedas</sup> Gamma( _N_ ). By conditioning on _N_ , we get that the density of the right hand side is


Recall that


and so the densities of both sides are equal.


**Exercise 7.3.** First establish a Taylor formula of the form


where Hes _xf_ = ( _∂ijf_ ) is the _d × d_ -Hessian matrix of second derivatives in the directions of _x_ , and


and the modulus of continuity of Hes _xf_ by


where _∥· ∥_ is the operator norm of a matrix. Then argue as in the proof of Theorem 7.13.

**Exercise 7.4.** First use Brownian scaling and the Markov property, as in the original proof of Theorem 2.33 to reduce the problem to showing that the distribution of _B_ ( _T_ (1)) (using the notation of Theorem 2.33) is the Cauchy distribution.

The map defined by _f_ ( _z_ ) = 2 _−z z_<sup>,for</sup><sup>_z∈_C,takesthehalf-plane</sup><sup>_{_(</sup><sup>_x, y_):</sup><sup>_x<_1</sup><sup>_}_ontotheunit</sup> disk and _f_ (0) = 0. The image measure of harmonic measure on _V_ (1) from 0 is the harmonic measure on the unit sphere from the origin, which is uniform. Hence the harmonic measure _µV_ (1)(0 _, ·_ ) is the image measure of the uniform distribution _ϖ_ on the unit sphere under _f_<sup>_−_1</sup> , which can be calculated using the derivative of _f_ .

**Exercise 7.5.** Use that _θ_ ( _t_ ) = _W_ 2( _H_ ( _t_ )) and lim _t↑∞ H_ ( _t_ ) = _∞_ .

326

**Exercise 7.7.** Suppose _h_ is supported by [0 _, b_ ] and look at the partitions given by _t_ ( _kn_ ) = _bk_ 2<sup>_−n_</sup> , for _k_ = 0 _, . . . ,_ 2<sup>_n_</sup> . By Theorem 7.32 and Theorem 6.18 we can choose a continuous modification of the process _{_ �0 _t_<sup>sign(</sup><sup>_B_(</sup><sup>_s_)</sup><sup>_−a_)</sup><sup>_dB_(</sup><sup>_s_):</sup><sup>_a ∈_R</sup><sup>_}_.Hence the Lebesgue integral on the left hand</sup> side is also a Riemann integral and can be approximated by the sum

where


This is a uniformly bounded sequence, which is uniformly convergent to the Lebesgue integral


Therefore the sequence of stochastic integrals converges in L<sup>2</sup> to the stochastic integral �0 _∞_<sup>_F_(</sup><sup>_B_(</sup><sup>_s_))</sup><sup>_dB_(</sup><sup>_s_),whichistherighthandsideofourformula.</sup>

**Exercise 8.1.** Suppose that _u_ is subharmonic and _B_ ( _x, r_ ) _⊂ U_ . Let _τ_ be the first exit time from _B_ ( _x, r_ ), which is a stopping time. As ∆ _u_ ( _z_ ) _≥_ 0 for all _z ∈ U_ we see from the multidimensional version of Itˆo’s formula that


Note that _∂u/∂xi_ is bounded on the closure of _B_ ( _x, r_ ), and thus everything is well-defined. We can now take expectations, and use Exercise 7.1 to see that


Now let _t ↑∞_ , so that the left hand side converges to E _x_ [ _u_ ( _B_ ( _τ_ ))] and note that this gives the mean value property for spheres. The result follows by integrating over _r_ .

**Exercise 8.2.** Let _u_ be a solution of the Poisson problem on _U_ . Define open sets _Un ↑ U_ by


Let _τn_ be the first exit time of _Un_ , which is a stopping time. As<sup><u>1</u></sup> 2<sup>∆</sup><sup>_u_(</sup><sup>_x_) =</sup><sup>_−g_(</sup><sup>_x_)forall</sup><sup>_x ∈U_</sup> we see from the multidimensional version of Itˆo’s formula that


Note that _∂u/∂xi_ is bounded on the closure of _Un_ , and thus everything is well-defined. We can now take expectations, and use Exercise 7.1 to see that


327

Note that both integrands are bounded. Hence, as _t ↑∞_ and _n →∞_ , bounded convergence yields that


where we have use the boundary condition to eliminate the left hand side.

**Exercise 9.2.** Use decompositions as in the proof of Theorem 9.22 to transfer the results of Theorem 9.8 from intersections of independent Brownian motions to self-intersections of one Brownian motion.

**Exercise 9.4.** A counterexample as required in part (d) can be constructed as follows: Let _A_ 1 and _A_ 2 be two disjoint closed sets on the line such that the Cartesian squares _A_<sup>2</sup> _i_<sup>have Hausdorff</sup> dimension less than 1 _/_ 2 yet the Cartesian product _A_ 1 _× A_ 2 has dimension strictly greater than 1 _/_ 2. Let _A_ be the union of _A_ 1 and _A_ 2. Then Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ on A is 1-1 with positive probability (if _B_ ( _A_ 1) is disjoint from _B_ ( _A_ 2)) yet with positive probability _B_ ( _A_ 1) intersects _B_ ( _A_ 2). For instance let _A_ 1 consist of points in [0 _,_ 1] where the binary _n_<sup>th</sup> digit vanishes whenever (2 _k_ )! _≤ n <_ (2 _k_ + 1)! for some _k_ . Let _A_ 2 consist of points in [2 _,_ 3] where the binary _n_<sup>th</sup> digit vanishes whenever (2 _k −_ 1)! _≤ n <_ (2 _k_ )! for some _k_ . then dim( _A_<sup>2</sup> _i_<sup>)=0for</sup><sup>_i_=1</sup><sup>_,_2yet</sup> dim( _A_ 1 _× A_ 2) _≥_ dim( _A_ 1 + _A_ 2) = 1, in fact dim( _A_ 1 _× A_ 2) = 1.

**Exercise 9.5.** Let _{B_ 1( _t_ ): 0 _≤ t ≤_ 1 _}_ be the first component of the planar motion. By Kaufman’s theorem, almost surely,


and, as in Corollary 9.30, the dimension on the right equals 1 _/_ 2 for every _a ∈_ (min _{x_ : ( _x, y_ ) _∈ B_ [0 _, t_ ] _},_ max _{x_ : ( _x, y_ ) _∈ B_ [0 _, t_ ] _}_ ).

**Exercise 10.2.** For every decomposition _E_ =<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_Ei_of</sup><sup>_E_intoboundedsets,wehave,using</sup> countable stability of Hausdorff dimension,


and passing to the infimum yields the statement.

**Exercise 10.7** The argument is sketched in [ **La99** ].

**Exercise 10.9.** For (a) note that Theorem 10.28 can be read as a criterion to determine the packing dimension of a set _E_ by hitting it with a limsup random fractal. Hence dim _P_ ( _A ∩ E_ ) can be found by evaluating P _{A ∩ A_<sup>_′_</sup> _∩ E_ = _∅}_ for _A_<sup>_′_</sup> an independent copy of _A_ . Now use that _A ∩ A_<sup>_′_</sup> is also a discrete limsup fractal.

328

**Exercise 10.10** To apply Theorem 7.24 for the proof of Lemma 10.40 (a) we shift the cone by defining a new tip _z_ ˜ as follows:

- If _α < π_ the intersection of the line through _x_ parallel to the central axis of the cone with the boundary of the dual cone,

- if _α > π_ the intersection of the line through _x_ parallel to the central axis of the cone with the boundary of the cone.

Note that _z_ + _W_ [ _α, ξ_ ] _⊂ z_ ˜ + _W_ [ _α, ξ_ ] and there exists a constant _C >_ 1 depending only on _α_ such that _|z − z_ ˜ _| < Cδ_ . There is nothing to show if _Cδ > ε/_ 2 and otherwise

P _x_ � _B_ (0 _, Tε_ ( _z_ )) _⊂ z_ + _W_ [ _α, ξ_ ]� _≤_ P _x_ � _B_ (0 _, Tε/_ 2(˜ _z_ )) _⊂ z_ ˜ + _W_ [ _α, ξ_ ]� _._

By shifting, rotating and scaling the Brownian motion and by Theorem 7.24 we obtain an upper bound for the right hand side of


where _C_ 0 _, C_ 1 _>_ 0 are suitable constants.

329

---

[← Exceptional sets for Brownian motion](14-exceptional-sets-for-brownian-motion.md) · [Up: contents](index.md) · [Appendix II: Background and prerequisites →](16-appendix-ii-background-and-prerequisites.md)
