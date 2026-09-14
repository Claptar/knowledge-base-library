---
title: Brownian local time
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Brownian local time

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this chapter we focus on linear Brownian motion and address the question how to measure the amount of time spent by a Brownian path at a given level. As we already know from Theorem 3.25 that the occupation times up to time _t_ are absolutely continuous measures, their densities are a viable measure for the time spent at level _a_ during the time interval [0 _, t_ ]. We shall show that these densities make up a continuous random field _{L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _, t ≥_ 0 _}_ , which is called the Brownian local time. Nontrivial information about the distribution of this process is contained in a theorem of L´evy (studying it as function of time) and the Ray-Knight theorem (studying it as function of the level). We finally show how to interpret local time as a family of Hausdorff measures.

### **1. The local time at zero**

How can we measure the amount of time spent by a standard linear Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ at zero? We have already seen that, almost surely, the zero set _{s ∈_ [0 _, t_ ): _B_ ( _s_ ) = 0 _}_ is a set of Hausdorff dimension 1 _/_ 2. Moreover, by Exercise 4.13, the 1 _/_ 2-dimensional Hausdorff measure of the zero set is zero, so Hausdorff measure as defined so far does not give a nontrivial answer.

We approach this problem by counting the number of downcrossings of a nested sequence of intervals decreasing to zero. More precisely, for a linear Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ with arbitrary starting point, given _a < b_ , we define stopping times _τ_ 0 = 0 and, for _j ≥_ 1,


We call the random functions


the _j_ th downcrossing of [ _a, b_ ]. For every _t >_ 0 we denote by


the number of _downcrossings_ of the interval [ _a, b_ ] before time _t_ . Note that _D_ ( _a, b, t_ ) is almost surely finite by the absolute continuity of Brownian motion on the compact interval [0 _, t_ ].

Theorem 6.1 (Downcrossing representation of the local time at zero). _There exists a nontrivial stochastic process {L_ ( _t_ ): _t ≥_ 0 _} called the_ **local time at zero** _such that for any sequences an ↑_ 0 _and bn ↓_ 0 _with an < bn, almost surely,_


_Moreover, this process is almost surely locally γ-H¨older continuous for any γ <_ 1 _/_ 2 _._

147

Remark 6.2. One might wonder about the meaning of the normalisation factor 2 in our theorem, which is omitted in some treatments (e.g. [ **KS88** ]). An intuitive answer is that the time spent near zero should be approximated by the number of downcrossings _plus_ the number of upcrossings of a small interval centred in zero. The factor thus compensates for the number of upcrossings, which is (up to an error of at most one) the same as the number of downcrossings. _⋄_

The key ingredient of the proof of Theorem 6.1 is the following fact.

Lemma 6.3. _Suppose that a < m < b and let {B_ ( _t_ ): 0 _≤ t ≤ T } be a linear Brownian motion stopped at the time T when it first hits a given level above b. Let_


_There exist two independent sequences X_ 0 _, X_ 1 _, . . . and Y_ 0 _, Y_ 1 _, . . . of independent nonnegative random variables, which are also independent of D, such that for j ≥_ 1 _the random variables Xj are geometric with mean_ ( _b − a_ ) _/_ ( _m − a_ ) _and the random variables Yj are geometric with mean_ ( _b − a_ ) _/_ ( _b − m_ ) _, and_


<!-- Start of picture text -->
y<br>B (j) B (j)<br>↓ ↑<br>b<br>m<br>−2 a<br>−3<br>σj τj σj+1<br>−4<br><!-- End of picture text -->

Figure 1. The downcrossing of [ _a, b_ ] contains one downcrossing of [ _a, m_ ] and the following upcrossing of [ _a, b_ ] contains one further downcrossing of [ _a, m_ ].

148

**Proof.** Recall the definition of the stopping times _σj_ , _τj_ from (1.1). For _j ≥_ 1, define the _j_<sup>th</sup> downcrossings, resp. upcrossings, of [ _a, b_ ] by


By the strong Markov property all these pieces of the Brownian path are independent. Note that _D_ depends only on the family ( _B↓_ ( _j_ )<sup>:</sup><sup>_j≥_1)ofdowncrossings.</sup>

_First_ look at _D_ l and denote by _X_ 0 the number of downcrossings of [ _a, m_ ] before the first downcrossing of [ _a, b_ ]. The _j_<sup>th</sup> downcrossing of [ _a, b_ ] contains exactly one downcrossing of [ _a, m_ ] and the _j_<sup>th</sup> upcrossing of [ _a, b_ ] contains a random number _Xj_ of downcrossings of [ _a, m_ ], which, by Theorem 2.45, satisfies


In other words _Xj_ is geometrically distributed with (success) parameter ( _m − a_ ) _/_ ( _b − a_ ).


<!-- Start of picture text -->
y B (j)<br>↓<br>b<br>m<br>B (j)<br>↑<br>τ˜1<br>−2 a<br>σ˜1<br>τ˜2<br>−3<br>σj τj σj+1<br>−4<br><!-- End of picture text -->

Figure 2. The downcrossing of [ _a, b_ ] contains three downcrossings of [ _m, b_ ] and the following upcrossing of [ _a, b_ ] contains no further downcrossings of [ _m, b_ ].

_Second_ look at _D_ u and denote by _Y_ 0 the number of downcrossings of [ _m, b_ ] after the last downcrossing of [ _a, b_ ]. No downcrossings of [ _m, b_ ] can occur during an upcrossing of [ _a, b_ ]. Fix a _j_ and look at the downcrossing _B↓_ ( _j_ ) of [ _a, b_ ]. Define stopping times _σ_ ˜0 = 0 and, for _i ≥_ 1,


This subdivides the path of _B↓_ ( _j_ )<sup>into independent downcrossing periods [˜</sup><sup>_σi−_1</sup><sup>_,_˜</sup><sup>_τi_], and upcrossing</sup> periods [˜ _τi,_ ˜ _σi_ ] of [ _m, b_ ]. By our assumption the upper hitting boundary is above _b_ and therefore can only be hit during the downcrossing periods, while the lifetime of _B↓_ ( _j_ ) expires when the lower boundary _a_ is hit, which can only occur during an upcrossing period. The probability of this event equals ( _b − m_ ) _/_ ( _b − a_ ) by Theorem 2.45.

149

Hence the number of downcrossings of [ _m, b_ ] during the _j_<sup>th</sup> downcrossing of [ _a, b_ ] is a geometric random variable _Yj_ with (success) parameter ( _b − m_ ) _/_ ( _b − a_ ), which completes the proof.

For the proof of Theorem 6.1 we first prove the convergence for the case when the Brownian motion is stopped at the time _T_ = _Tb_ when it first reaches some level _b > b_ 1. This has the advantage that there cannot be any uncompleted upcrossings.

Lemma 6.4. _For any two sequences an ↑_ 0 _and bn ↓_ 0 _with an < bn, the discrete time stochastic process_


_is a submartingale with respect to the natural filtration_ ( _Fn_ : _n ∈_ N) _._

**Proof.** We may assume that, for each _n_ , we have


which is no loss of generality, as we may replace a step where both _an_ and _bn_ are changed by two steps, where only one is changed at the time. The original sequence is then a subsequence of the modified one and inherits the submartingale property.

Now fix _n_ and _first_ assume that we are in case (1) _an_ = _an_ +1. By Lemma 6.3 for _D_ l, the total number _D_ ( _an, bn_ +1 _, T_ ) of downcrossings of [ _an, bn_ +1] given _Fn_ is the sum of _D_ ( _an, bn, T_ ) independent geometric random variables with parameter ( _bn_ +1 _−an_ ) _/_ ( _bn−an_ ) plus a nonnegative contribution. Hence,


which is the submartingale property (for the _n_ th step).

_Second_ assume that we are in case (1) _bn_ = _bn_ +1. Then Lemma 6.3 for _D_ u shows that the number of downcrossings of [ _an_ +1 _, bn_ ] given _Fn_ is the sum of _D_ ( _an, bn, T_ ) independent geometric random variables with parameter ( _bn − an_ +1) _/_ ( _bn − an_ ) plus a nonnegative contribution. Hence


and together with the first case this establishes that _{_ 2( _bn − an_ ) _D_ ( _an, bn, T_ ): _n ∈_ N _}_ is a submartingale with respect to its natural filtration.

Lemma 6.5. _For any two sequences an ↑_ 0 _and bn ↓_ 0 _with an < bn the limit_

_L_ ( _Tb_ ) := _n_ lim _→∞_<sup>2(</sup><sup>_bn −an_)</sup><sup>_D_(</sup><sup>_an, bn, Tb_)</sup>

_exists almost surely. It does not depend on the choice of sequences._

**Proof.** Observe that _D_ ( _an, bn, Tb_ ) is a geometric random variable with parameter ( _bn − an_ ) _/_ ( _b − an_ ). Recall that the variance of a geometric random variable with parameter _p_ is (1 _− p_ ) _/p_<sup>2</sup> , and so its second moment is bounded by 2 _/p_<sup>2</sup> . Hence


150

and thus the submartingale in Lemma 6.4 is _L_<sup>2</sup> -bounded. By the submartingale convergence theorem, see Theorem II.4.5, the limit


exists almost surely, and by Theorem II.4.12 also in _L_<sup>2</sup> ensuring that the limit is nontrivial. Finally, note that the limit does not depend on the choice of the sequence _an ↑_ 0 and _bn ↓_ 0 because if it did, then given two sequences with different limits we could construct a sequence of intervals alternating between the two sequences, which would not converge.

Lemma 6.6. _For any fixed time t >_ 0 _, almost surely, the limit_


**Proof.** We define an auxiliary Brownian motion _{Bt_ ( _s_ ): _s ≥_ 0 _}_ by _Bt_ ( _s_ ) = _B_ ( _t_ + _s_ ). For any integer _b > b_ 1 we denote by _Dt_ ( _an, bn, Tb_ ) the number of downcrossings of the interval [ _an, bn_ ] by the auxiliary Brownian motion before it hits _b_ . Then, almost surely,


exists by the previous lemma. Given _t >_ 0 we fix a Brownian path such that this limit exists for all integers _b > b_ 1. Pick _b_ so large that _Tb > t_ . Define


To show that this is the required limit, observe that

_D_ ( _an, bn, Tb_ ) _− Dt_ ( _an, bn, Tb_ ) _−_ 1 _≤ D_ ( _an, bn, t_ ) _≤ D_ ( _an, bn, Tb_ ) _− Dt_ ( _an, bn, Tb_ ) _,_

where the correction _−_ 1 on the left hand side arises from the possibility that _t_ interrupts a downcrossing. Multiplying by 2( _bn − an_ ) and taking a limit gives _L_ ( _Tb_ ) _− Lt_ ( _Tb_ ) for both bounds, proving convergence.

We now have to study the dependence of _L_ ( _t_ ) on the time _t_ in more detail. To simplify the notation we write


The following lemma contains a probability estimate, which is sufficient to get the convergence of the downcrossing numbers jointly for all times and to establish H¨older continuity.

Lemma 6.7. _Let γ <_ 1 _/_ 2 _and_ 0 _< ε <_ (1 _−_ 2 _γ_ ) _/_ 3 _. Then, for all t ≥_ 0 _and_ 0 _< h <_ 1 _, we have_


**Proof.** As, by Fatou’s lemma,

P� _L_ ( _t_ + _h_ ) _− L_ ( _t_ ) _> h_<sup>_γ_�</sup> = P� lim inf _n→∞_<sup>_In_(</sup><sup>_t, t_+</sup><sup>_h_)</sup><sup>_> hγ_�</sup> _≤_ lim inf _n→∞_<sup>P</sup> � _In_ ( _t, t_ + _h_ ) _> h_<sup>_γ_�</sup> we can focus on estimating P _{In_ ( _t, t_ + _h_ ) _> h_<sup>_γ_</sup> _}_ for fixed large _n_ . By the Markov property it suffices to estimate P _x{In_ (0 _, h_ ) _> h_<sup>_γ_�</sup> uniformly for all _x ∈_ R. This probability is clearly

151

maximal when _x_ = _bn_ , so we may assume this. Let _Th_ = inf _{s >_ 0: _B_ ( _s_ ) = _bn_ + _h_<sup>(1</sup><sup>_−ε_)</sup><sup>_/_2</sup> _}_ and observe that

� _In_ (0 _, h_ ) _> h_<sup>_γ_�</sup> _⊂_ � _In_ (0 _, Th_ ) _> h_<sup>_γ_�</sup> _∪_ � _Th < h_ � _._

The number of downcrossings of [ _an, bn_ ] during the period before _Th_ is geometrically distributed with mean ( _bn − an_ )<sup>_−_1</sup> _h_<sup>(1</sup><sup>_−ε_)</sup><sup>_/_2</sup> + 1 and thus


With _{W_ ( _s_ ): _s ≥_ 0 _}_ denoting a standard linear Brownian motion,


where we have used Remark 2.19 in the last step. The result follows by adding the last two displayed formulas.

Lemma 6.8. _Almost surely,_


_exists for every t ≥_ 0 _._

**Proof.** It suffices to prove the simultaneous convergence for all 0 _≤ t ≤_ 1. We define a countable set of gridpoints


and show that the stated convergence holds on the set


which, by choosing _M_ suitably, has probability arbitrarily close to one by the previous two lemmas. Given any _t ∈_ [0 _,_ 1) and a large _m_ we find _t_ 1 _, t_ 2 _∈Gm_ with _t_ 2 _− t_ 1 = _m_<sup><u>1</u>and</sup><sup>_t ∈_[</sup><sup>_t_1</sup><sup>_, t_2].</sup> We obviously have

2( _bn − an_ ) _D_ ( _an, bn, t_ 1) _≤_ 2( _bn − an_ ) _D_ ( _an, bn, t_ ) _≤_ 2( _bn − an_ ) _D_ ( _an, bn, t_ 2) _._ Both bounds converge on our set, and the difference of the limits is _L_ ( _t_ 2) _− L_ ( _t_ 1), which is bounded by _m_<sup>_−γ_</sup> and thus can be made arbitrarily small by choosing a large _m_ .

Lemma 6.9. _For γ <_<sup><u>1</u></sup> 2<sup>_,almostsurely,theprocess{L_(</sup><sup>_t_):</sup><sup>_t ≥_0</sup><sup>_}islocallyγ-H¨oldercontinuous._</sup>

**Proof.** It suffices to look at 0 _≤ t <_ 1. We use the notation of the proof of the previous and show that _γ_ -H¨older continuity holds on the set constructed there. Indeed, whenever 0 _≤ s < t <_ 1 and _t − s <_ 1 _/M_ we pick _m ≥ M_ such that


We take _t_ 1 _< s_ with _t_ 1 _∈Gm_ and _s − t_ 1 _<_ 1 _/m_ , and _t_ 2 _> t_ with _t_ 2 _∈Gm_ and _t_ 2 _− t <_ 1 _/m_ .

152

Note that _t_ 2 _− t_ 1 _≤_ 2 _/m_ by construction and hence,


The result follows as the fraction on the right is bounded by 2.

This completes the proof of the downcrossing representation, Theorem 6.1. It is easy to see from this representation that, almost surely, the local time at zero increases only on the zero set of the Brownian motion, see Exercise 6.1.

Observe that the increasing process _{L_ ( _t_ ) : _t ≥_ 0 _}_ is _not_ a Markov process. Heuristically, the size of the increment _L_ ( _t_ + _h_ ) _− L_ ( _t_ ) depends on the position of the first zero of the Brownian motion after time _t_ , which is strongly dependent on the position of the last zero before time _t_ . The last zero however is the position of the last point of increase of the local time process before time _t_ , and therefore the path _{L_ ( _s_ ) : 0 _≤ s ≤ t}_ contains relevant information beyond its endpoint. Nevertheless, we can describe the law of the local time process, thanks to the following famous theorem of Paul L´evy, which describes the law of the local time at zero in terms of the maximum process of Brownian motion. It opens the door to finer results on the local time at zero, like those presented in Section 4 of this chapter.

Theorem 6.10 (L´evy). _The local time at zero {L_ ( _t_ ): _t ≥_ 0 _} and the maximum process {M_ ( _t_ ): _t ≥_ 0 _} of a standard linear Brownian motion have the same distribution._


The length of the embedded random walk is


which is easily seen to be independent of the actual walk.


**Proof.** First note that _{ξk_ ( _n_ )<sup>:</sup><sup>_k_= 1</sup><sup>_,_2</sup><sup>_, . . .}_definedby</sup>


is a sequence of independent random variables, for each _n_ . By Theorem 2.45 the mean of _ξk_ is 2<sup>_−_2</sup><sup>_n_</sup> and its variance is, by Brownian scaling, equal to _c_ 2<sup>_−_4</sup><sup>_n_</sup> for some constant _c >_ 0. (See, for example, Exercise 2.13 for instructions how to find the constant.) Define


153


We infer that, almost surely, lim _n→∞ S_<sup>(</sup><sup>_n_)</sup> ( _t_ ) = _t_ . For fixed _ε >_ 0, we pick _n_ 0 large so that

_S_ ( _n_ )( _t − ε_ ) _≤ t ≤ S_ ( _n_ )( _t_ + _ε_ ) for all _n ≥ n_ 0 _._

The sum over _ξk_ up to _N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) + 1 is at least _t_ , by definition, and hence we get _N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) + 1 _≥⌈_ 2<sup>2</sup><sup>_n_</sup> ( _t − ε_ ) _⌉_ . Conversely, the sum over _ξk_ up to _N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) is at most _t_ and hence _N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) _≤⌈_ 2<sup>2</sup><sup>_n_</sup> ( _t_ + _ε_ ) _⌉_ . The result follows as _ε >_ 0 was arbitrary.

Lemma 6.12. _Almost surely, for every t >_ 0 _,_


**Proof.** By Theorem 6.1 applied to the sequences _an_ = _−_ 2<sup>_−n_</sup> and _bn_ = 0 we have _n_ lim _↑∞_<sup>2</sup><sup>_−n_#</sup> � _k ∈{_ 1 _, . . . , N_ ( _n_ )( _t_ ) _}_ : _Xk−_ 1 = 0 _, Xk_ = _−_ 1� = 2<sup><u>1</u></sup><sup>_L_(</sup><sup>_t_)</sup><sup>_._</sup>

Applying Theorem 6.1 to the sequences _an_ = 0 and _bn_ = 2<sup>_−n_</sup> we get


As # _{k ≤ N_ : _Xk−_ 1 = 1 _, Xk_ = 0 _}_ and # _{k ≤ N_ : _Xk−_ 1 = 0 _, Xk_ = 1 _}_ differ by no more than one, the result follows by adding up the two displayed formulas.


<!-- Start of picture text -->
3 3<br>Mk Yk = Mk − Xk<br>2 2<br>1 1<br>k k<br>0 0<br>Xk<br>−1<br>−2<br>N (n) (t) N (n) (t)<br><!-- End of picture text -->

Figure 3. On the left an embedded random walk _{Xk_ : _k ≥_ 0 _}_ together with its maximum process _{Mk_ : _k ≥_ 0 _}_ . On the right the associated difference process _{Yk_ : _k ≥_ 0 _}_ defined by _Yk_ = _Mk − Xk_ .

154

We define the maximum process _{Mk_ ( _n_ )<sup>:</sup><sup>_k_=1</sup><sup>_,_2</sup><sup>_, . . .}_associatedwiththeembeddedrandom</sup> walk by _Mk_ = _Mk_ ( _n_ ) = max � _Xj_ ( _n_ ) : _j ∈{_ 0 _, . . . , k}_ � _._ Then the process _{Yk_ ( _n_ ) : _k_ = 1 _,_ 2 _, . . .}_ defined by _Yk_ := _Yk_ ( _n_ ) := _Mk − Xk_ is a Markov chain with statespace _{_ 0 _,_ 1 _,_ 2 _, . . .}_ and the following transition mechanism _•_ if _j̸_ = 0 then P _{Yk_ +1 = _j_ + 1 _| Yk_ = _j}_ = 2<sup><u>1</u>= P</sup><sup>_{Yk_+1=</sup><sup>_j −_1</sup><sup>_| Yk_=</sup><sup>_j}_,</sup> _•_ P _{Yk_ +1 = 0 _| Yk_ = 0 _}_ =<sup><u>1</u></sup> 2<sup>= P</sup><sup>_{Yk_+1= 1</sup><sup>_| Yk_= 0</sup><sup>_}_.</sup>

One can recover the maximum process _{Mk_ : _k_ = 1 _,_ 2 _, . . .}_ from _{Yk_ : _k_ = 1 _,_ 2 _, . . .}_ by counting the number of flat steps


Hence we obtain, asymptotically, the maximum process of the Brownian motion as a limit of the number of flat steps in _{Yk_ ( _n_ ) : _k_ = 1 _,_ 2 _, . . .}_ .

Lemma 6.13. _For any time t >_ 0 _, almost surely,_


**Proof.** Note that #� _j ∈{_ 1 _, . . . , N }_ : _Yj_ = _Yj−_ 1� is the maximum of the random walk _{Xk_ : _k_ = 1 _,_ 2 _, . . . , N }_ over its entire length. This maximum, multiplied by 2<sup>_−n_</sup> , differs from _M_ ( _t_ ) by no more than 2<sup>_−n_</sup> , and this completes the argument.

Removing the flat steps in the process _{Yj_ ( _n_ ) : _j_ = 1 _,_ 2 _, . . .}_ we obtain a process _{Y_<sup>˜</sup> _k_ ( _n_ ) : _k_ = 1 _,_ 2 _, . . .}_ , which has the same law as _{|Xk|_ : _k_ = 1 _,_ 2 _, . . .}_ . By Lemma 6.12 we therefore have the convergence in distribution, as _n ↑∞_ ,


jointly for any finite set of times.

Lemma 6.14. _Almost surely,_


**Proof.** First note that when _{Yj_ : _j_ = 1 _,_ 2 _, . . .}_ returns to zero for the _i_ th time, the number of steps before it moves to one is given by a random variable _Zi_ with distribution


Denoting by _Z_ 0 the number of steps before it moves initially, the random variables _Z_ 0 _, Z_ 1 _, . . ._ are independent and independent of the process _{Y_<sup>˜</sup> _k_ ( _n_ ) : _k_ = 1 _,_ 2 _, . . .}_ . Let


155


<!-- Start of picture text -->
3 3<br>Yj Y˜k<br>2 A (n) = 2 2<br>1 1<br>j k<br>0 0<br>τ0 τ1<br>N (n) (t) − MN(n)(t) MN (n)(t)<br>N (n) (t)<br>0 2 4 6 8 10 0 2 4 6 8 10<br><!-- End of picture text -->

Figure 4. On the left a sample of the processes _{Yj_ : 0 _≤ j ≤ N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) _}_ . On the right the associated _{Y_<sup>˜</sup> _k_ : 0 _≤ k ≤ N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) _}_ , which is obtained by removing the two flat steps and extending the path to its original length.

be the total number of returns to zero before time _N_ . Then, almost surely, as _n ↑∞_ ,


because the first factor converges by Lemma 6.12 and the second by the law of large numbers. To study the effect of the removal of the flat pieces, recall that almost surely the length _N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) of the walk is of order 2<sup>2</sup><sup>_n_</sup> _t_ , by Lemma 6.11, and the number of flat pieces is _MN_ ( _n_ )( _t_ ), which is of order 2<sup>_n_</sup> , by Lemma 6.13. Hence, for all _ε >_ 0, if _n_ is large enough,


We infer from this that


and the right hand side converges almost surely to a random variable, which has the law of _L_ ( _t_ ) _− L_ ( _t − ε_ ) and hence can be made arbitrarily small by choice of _ε >_ 0.

**Proof of Theorem 6.10** Note that both processes in Theorem 6.10 are continuous, so that it suffices to compare their finite dimensional distributions. Equality of these follows directly by combining Lemma 6.13, Equation (1.2) and Lemma 6.14.

156

Theorem 6.15 (Occupation time representation of the local time at zero). _For all sequences an ↑_ 0 _and bn ↓_ 0 _with an < bn, almost surely,_


The proof is prepared by the following lemma, which we prove as Exercise 6.4.

Lemma 6.16. _Let {W_ ( _s_ ): _s ≥_ 0 _} be a standard linear Brownian motion and τ_ 1 _its first hitting time of level_ 1 _. Then_ E �0 _τ_ 1<sup>1</sup><sup>_{_0</sup><sup>_≤W_(</sup><sup>_s_)</sup><sup>_≤_1</sup><sup>_} ds_= 1</sup><sup>_._</sup>

**Proof of Theorem 6.15** Recall the stopping times _τj_ defined for _an < bn_ as in (1.1). For the proof of the lower bound note that


By Brownian scaling


where _{W_ ( _s_ ): _s ≥_ 0 _}_ is a standard linear Brownian motion and

_τ_ = inf � _s >_ 0: _W_ ( _s_ ) = 0 and there exists _t < s_ with _W_ ( _t_ ) = 1� _._

Hence


The first factor converges almost surely to <u>12</u><sup>_L_(</sup><sup>_t_),byTheorem6.1.</sup> From the law of large numbers and Lemma 6.16 we get for the second factor,


This verifies the lower bound. The upper bound can be obtained by including the period [ _τj, τj_ +1] for _j_ = _D_ ( _an, bn, t_ ) in the summation and using the same arguments as for the lower bound. This completes the proof of Theorem 6.15.

157

### **2. A random walk approach to the local time process**

Given a level _a ∈_ R the construction of the previous chapter allows us to define the _local time at level a_ for a linear Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ . Indeed, simply let _{L_<sup>_a_</sup> ( _t_ ): _t ≥_ 0 _}_ be the local time at zero of the auxiliary Brownian motion _{B_<sup>_a_</sup> ( _t_ ): _t ≥_ 0 _}_ defined by _B_<sup>_a_</sup> ( _t_ ) = _B_ ( _t_ ) _−a_ . Using Theorem 6.15 it is not hard to show that _{L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _}_ is the density of the occupation measure _µt_ introduced in Theorem 3.25.

Theorem 6.17. _For linear Brownian motion {B_ ( _t_ ): _t ≥_ 0 _}, almost surely, for any bounded measurable g_ : R _→_ R _and t >_ 0 _,_


**Proof.** First, observe that for the statement it suffices to have _{L_<sup>_a_</sup> ( _t_ ): _t ≥_ 0 _}_ defined for _L_ -almost every _a_ . Second, we may assume that _t_ is fixed. Indeed, it suffices to verify the second equality for a countable family of bounded measurable _g_ : R _→_ R, for example the indicator functions of rational intervals. Having fixed such a _g_ both sides are continuous in _t_ .

For fixed _t_ , we know from Theorem 3.25 that _µt ≪L_ almost surely, hence a density _f_ exists by the Radon-Nikodym theorem and may be obtained as


which equals _L_<sup>_a_</sup> ( _t_ ) by Theorem 6.15, almost surely for _L_ -almost every _a_ .

A major result about linear Brownian motion is the continuity of the density _{L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _}_ of the occupation measures, which we now prove. To explore _L_<sup>_a_</sup> ( _t_ ) as a function of the levels _a_ we extend the downcrossing representation to hold _simultaneously_ at all levels _a_ . We approach this problem via the random walks embedded in a Brownian motion.

For a Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ started in the origin we recall the definition of the embedded random walks _{Xk_ ( _n_ )<sup>:</sup><sup>_k_= 1</sup><sup>_,_2</sup><sup>_, . . .}_fromtheprevioussection:Definestoppingtimes</sup> _τ_ 0 := _τ_ 0( _n_ ) := 0 and


and define the _n_ th embedded random walk by


For any time _t >_ 0 the length of the embedded random walk is


which is independent of the _n_ th walk itself. Further, given _a ∈_ R, choose _j_ ( _a_ ) _∈{_ 0 _,_ 1 _, . . .}_ such that _j_ ( _a_ ) 2<sup>_−n_</sup> _≤ a <_ ( _j_ ( _a_ ) + 1) 2<sup>_−n_</sup> _._ Denote the number of downcrossings of 2<sup>_n_</sup> _a_ by the _n_ th embedded random walk by


158

Theorem 6.18 (Trotter’s theorem). _Let {B_ ( _t_ ): _t ≥_ 0 _} be a linear Brownian motion and let D_<sup>(</sup><sup>_n_)</sup> ( _a, t_ ) _be the number of downcrossings of_ 2<sup>_n_</sup> _a by the nth embedded random walk stopped at time N_<sup>(</sup><sup>_n_)</sup> ( _t_ ) _. Then, almost surely,_


_Moreover, for every γ <_<sup><u>1</u></sup> 2<sup>_,therandomfield_</sup>


_is almost surely locally γ-H¨older continuous._

Remark 6.19. Note that _{L_<sup>_a_</sup> ( _t_ ) : _a ∈_ R _, t ≥_ 0 _}_ is a stochastic process depending on more than one parameter, and to emphasise this fact we use the notion **random field** . _⋄_

The proof uses the following estimate for the sum of independent geometric random variables with mean two, which we prove as Exercise 6.5.

Lemma 6.20. _Let X_ 1 _, X_ 2 _, . . . are independent geometrically distributed random variables with mean_ 2 _. Then, for sufficiently small ε >_ 0 _, for all nonnegative integers k ≤ m,_


The following lemma is the heart of the proof of Theorem 6.18.

Lemma 6.21. _Suppose that a < b and let {B_ ( _t_ ): 0 _≤ t ≤ T } be a linear Brownian motion stopped at the time T when it first hits a given level above b. Let_

- _D be the number of downcrossings of the interval_ [ _a, b_ ] _,_


_Then, for sufficiently small ε >_ 0 _, for all nonnegative integers k ≤ m,_


**Proof.** By Lemma 6.3 we have that, given _{D_ = _k}_ , there exist independent random variables _X_ 0 _, X_ 1 _, X_ 2 _. . ._ , such that


and _X_ 1 _, X_ 2 _, . . ._ are geometrically distributed with mean 2. An inspection of the proof of Theorem 6.3 reveals that _X_ 0 is either zero or also geometrically distributed with mean 2, depending on the starting point of the Brownian motion.

159

Using Lemma 6.20 and Chebyshev’s inequality, we get, if _ε >_ 0 is small enough,


The argument is analogous for _D_ u, and this completes the proof.

We now fix _γ <_<sup><u>1</u></sup> 2<sup>andalargeinteger</sup><sup>_N_.WestoptheBrownianmotionattime</sup><sup>_TN_whenit</sup> first hits level _N_ , and abbreviate _D_<sup>(</sup><sup>_n_)</sup> ( _a_ ) := _D_<sup>(</sup><sup>_n_)</sup> ( _a, TN_ ). We denote the _n_ th dyadic grid by


Lemma 6.22. _Denote by_ Ω( _m_ ) _the event that, for all n ≥ m,_


_Then_


**Proof.** Item (a) follows by combining the following three items,


We observe that it is equivalent to show (i),(ii) for all _a ∈Dn_ +1 and (iii) for all _a ∈Dn_ . To estimate the probability of the first item we use Lemma 6.21 with _ε_ = _n_ <u>1</u><sup>22</sup><sup>_−nγ_and</sup><sup>_m_=</sup><sup>_k_.</sup> We get that


160

For the second item we get from Lemma 6.21 with _ε_ = 2<sup>_−γn_</sup> and _m_ = 2<sup>_n_</sup> _> k_ . This gives that


For the third item we use that the random variable _D_<sup>(</sup><sup>_n_)</sup> ( _a_ ) is geometrically distributed with parameter _N_ <u>2</u><sup>_−_</sup> _−_<sup>_n_</sup> _a_<sup>_≥_</sup><sup><u>2</u></sup> 2<sup>_−_</sup> _N_<sup>_n_.Wethereforeobtain,forsomesequence</sup><sup>_δn→_0,</sup>


hence, for sufficiently large _m_ ,

This completes the estimates needed for item (a).

Item (b) need only be checked for all _a, b ∈Dn_ with _|a − b|_ = 2<sup>_−n_</sup> . Note that _D_<sup>(</sup><sup>_n_)</sup> ( _a_ ), resp. _D_<sup>(</sup><sup>_n_)</sup> ( _b_ ), are the number of downcrossings of the lower, resp. upper, half of an interval of length 2<sup>_−n_+1</sup> , which may or may not be dyadic. Denote by _D_<sup>˜(</sup><sup>_n−_1)</sup> ( _a_ ) = _D_<sup>˜(</sup><sup>_n−_1)</sup> ( _b_ ) the number of downcrossings of this interval. Then


and summability of these probabilities over all _a, b ∈Dn_ with _|a − b|_ = 2<sup>_−n_</sup> and _n ≥ m_ has been established in the proof of item (a). This completes the proof.

Lemma 6.23. _On the set_ Ω( _m_ ) _we have that_


_exists for every a ∈_ [ _−N, N_ ) _._

**Proof.** We show that the sequence defined by 2<sup>_−n−_1</sup> _D_<sup>(</sup><sup>_n_)</sup> ( _a_ ), for _n ∈_ N, is a Cauchy sequence. Indeed, by item (a) in the definition of the set Ω( _m_ ) we get that, for any _a ∈_ [ _−N, N_ ] and _n ≥ m_ ,


Thus, for any _n ≥ m_ ,

and thus the sequence is a Cauchy sequence and therefore convergent.

161

Lemma 6.24. _On the set_ Ω( _m_ ) _the process {L_<sup>_a_</sup> ( _TN_ ): _a ∈_ [ _−N, N_ ) _} is γ-H¨older continuous._

**Proof.** Fix _a, b ∈_ [ _−N, N_ ) with 2<sup>_−n−_1</sup> _≤ a − b ≤_ 2<sup>_−n_</sup> for some _n ≥ m_ . Then, using item (a) and item (b) in the definition of Ω( _m_ ), for all _k ≥ n_ ,


Letting _k ↑∞_ , we get


which completes the proof.

Lemma 6.25. _For any fixed time t >_ 0 _, almost surely, the limit_


_and moreover {L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _} is γ-H¨older continuous._

**Proof.** Given _t >_ 0 define the auxiliary Brownian motion _{Bt_ ( _s_ ): _s ≥_ 0 _}_ by _Bt_ ( _s_ ) = _B_ ( _t_ + _s_ ) and denote by _Dt_ ( _n_ )<sup>(</sup><sup>_a_)thenumberofdowncrossingsassociatedtotheauxiliaryBrownianmo-</sup> tion. Then, almost surely, _L_<sup>_a_</sup> _t_<sup>(</sup><sup>_TN_) := lim</sup><sup>_n↑∞_2</sup><sup>_−n−_1</sup><sup>_D_</sup> _t_ ( _n_ )<sup>(</sup><sup>_a_)existsforall</sup><sup>_a ∈_Randintegers</sup><sup>_N_.</sup> On this event we pick _N_ so large that _TN > t_ . Define _L_<sup>_a_</sup> ( _t_ ) := _L_<sup>_a_</sup> ( _TN_ ) _− L_<sup>_a_</sup> _t_<sup>(</sup><sup>_TN_),andobserve</sup> that _{L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _}_ defined like this is _γ_ -H¨older continuous by Lemma 6.24. It remains to show that this definition agrees with the one stated in the lemma. To this end, observe that _D_ ( _n_ )( _a, TN_ ) _− Dt_ ( _n_ )<sup>(</sup><sup>_a, TN_)</sup><sup>_−_1</sup><sup>_≤D_</sup> ( _n_ )( _a, t_ ) _≤ D_ ( _n_ )( _a, TN_ ) _− Dt_ ( _n_ )<sup>(</sup><sup>_a, TN_)</sup><sup>_._</sup>

Multiplying by 2<sup>_−n−_1</sup> and taking a limit proves the claimed convergence.

Lemma 6.26. _Almost surely,_


_exists for every t ≥_ 0 _and a ∈_ R _and {L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _, t ≥_ 0 _} is γ-H¨older continuous._

**Proof.** It suffices to look at _t ∈_ [0 _, N_ ) and _a ∈_ [ _−N, N_ ). Recall the definition of the dyadic points _Dn_ in [ _−N, N_ ) and additionally define dyadic points in [0 _, N_ ) by


162

We show that the claimed statements hold on the set


which, by choosing _M_ suitably, has probability arbitrarily close to one by Lemma 6.25 and Lemma 6.7.

Given any _t ∈_ [0 _, N_ ) and _a ∈_ [ _−N, N_ ], for any large _m_ , we find _t_ 1 _, t_ 2 _∈Hm_ with _t_ 2 _− t_ 1 = 2<sup>_−m_</sup> and _t ∈_ [ _t_ 1 _, t_ 2]. We have


Both bounds converge on our set, and the difference of the limits is _L_<sup>_a_</sup> ( _t_ 2) _− L_<sup>_a_</sup> ( _t_ 1). We can then find _b ∈Hk_ for _k ≥ M_ with _|L_<sup>_a_</sup> ( _t_ 1) _− L_<sup>_b_</sup> ( _t_ 1) _| <_ 2<sup>_−mγ_</sup> and _|L_<sup>_a_</sup> ( _t_ 2) _− L_<sup>_b_</sup> ( _t_ 2) _| <_ 2<sup>_−mγ_</sup> and get


which can be made arbitrarily small by choice of _m_ , proving simultaneous convergence.

For the proof of continuity, suppose _a, b ∈_ [ _−N, N_ ) and _s, t ∈_ [0 _, N_ ) with 2<sup>_−m_</sup> _≤|a − b| ≤_ 2<sup>_−m_</sup> and 2<sup>_−m_</sup> _≤ t − s ≤_ 2<sup>_−m_</sup> for some _m ≥ M_ . We pick _s_ 1 _, s_ 2 _∈Hm_ and _t_ 1 _, t_ 2 _∈Hm_ such that


and all contributions on the right are bounded by constant multiples of 2<sup>_−mγ_</sup> , by the construction of our set. This completes the proof of _γ_ -H¨older continuity.

This completes the proof of Trotter’s theorem, Theorem 6.18.

### **3. The Ray-Knight theorem**

We now have a closer look at the distributions of local times _L_<sup>_x_</sup> ( _T_ ) as a function of the level _x_ in the case that Brownian motion is started at an arbitrary point and stopped at the time _T_ when it first hits level zero. The following remarkable distributional identity goes back to the work of Ray and Knight.

163

Theorem 6.27 (Ray-Knight theorem). _Suppose a >_ 0 _and {B_ ( _t_ ) : 0 _≤ t ≤ T } is a linear Brownian motion started at a and stopped at time T_ = inf _{t ≥_ 0 : _B_ ( _t_ ) = 0 _}, when it reaches level zero for the first time. Then_


_where {W_ ( _x_ ): _x ≥_ 0 _} is a standard planar Brownian motion._


<!-- Start of picture text -->
x<br>a a<br>B(t) |W (x)| 2 = L x (T )<br>t<br>0  0<br>0 T 0<br><!-- End of picture text -->

Figure 5. The Brownian path on the left, and its local time as a function of the level, on the right.

Remark 6.28. The process _{|W_ ( _x_ ) _|_<sup>2</sup> : _x ≥_ 0 _}_ of squared norms of a planar Brownian motion is called the squared _two-dimensional Bessel process_ . For any fixed _x_ , the random variable _⋄ |W_ ( _x_ ) _|_<sup>2</sup> is exponentially distributed with mean 2 _x_ , see Lemma II.3.8.

We carry out the proof of the Ray-Knight theorem in three steps. As a warm-up, we look at one point 0 _< x ≤ a_ . Recall from the downcrossing representation, Theorem 6.1, that

lim _n_ <u>2</u><sup>_Dn_(</sup><sup>_x_) =</sup><sup>_Lx_(</sup><sup>_T_)</sup> almost surely, _n→∞_

where _Dn_ ( _x_ ) denotes the number of downcrossings of the interval [ _x, x −_ 1 _/n_ ] before time _T_ . Lemma 6.29. _For any_ 0 _< x ≤ a, we have n_<sup><u>2</u></sup><sup>_Dn_(</sup><sup>_x_) =</sup><sup>_⇒|W_(</sup><sup>_x_)</sup><sup>_|_2</sup><sup>_asn ↑∞._</sup>

**Proof.** By the strong Markov property and the exit probabilities from an interval described in Theorem 2.45, it is clear that, provided _n >_ 1 _/x_ , the random variable _Dn_ ( _x_ ) is geometrically distributed with (success) parameter 1 _/_ ( _nx_ ), i.e. P _{Dn_ ( _x_ ) = _k}_ = _nx_ <u>1</u><sup>(1</sup><sup>_−_</sup> _nx_ <u>1</u><sup>)</sup><sup>_k−_1forall</sup><sup>_k∈_</sup> _{_ 1 _,_ 2 _, . . .}_ . Hence, as _n →∞_ , we obtain that


and the result follows, as _|W_ ( _x_ ) _|_<sup>2</sup> is exponentially distributed with mean 2 _x_ .

164

Lemma 6.29 is the ‘one-point version’ of Theorem 6.27. The essence of the Ray-Knight theorem is captured in the ‘two-point version’, which we prove next. We fix two points _x_ and _x_ + _h_ with 0 _< x < x_ + _h < a_ . The next three lemmas are the crucial ingredients for the proof of Theorem 6.27.

Lemma 6.30. _Let_ 0 _< x < x_ + _h < a. Then, for all n > h, we have_


_where_

- _D_ = _D_<sup>(</sup><sup>_n_)</sup> _is the number of downcrossings of the interval_ [ _x_ + _h − n_<sup><u>1</u></sup><sup>_, x_+</sup><sup>_h_]</sup><sup>_beforethe_</sup> _Brownian motion hits level x,_

- _for any j ∈_ N _the random variable Ij_ = _Ij_ ( _n_ ) _is Bernoulli distributed with mean nh_ <u>1+1</u><sup>_,_</sup>

- _• for any j ∈_ N _the random variable Nj_ = _Nj_ ( _n_ ) _is geometrically distributed with mean nh_ + 1 _,_

_and all these random variables are independent of each other and of Dn_ ( _x_ ) _._


<!-- Start of picture text -->
B (2j−1)<br>xk+1<br>xk+1 − n 1<br>xk<br>xk − n 1<br>τ2j−2 τ2j−1<br>−5 0 5 10 15 20 25 30 35 40 45<br><!-- End of picture text -->

Figure 6. The random variables _Ij_ and _Nj_ depend only on the pieces _B_<sup>(2</sup><sup>_j−_1)</sup> for _j ≥_ 1. For this sample _Ij_ = 1 as the path hits _x_ + _h_ before _x − n_<sup><u>1</u>and</sup><sup>_Nj_= 2,</sup> because the path downcrosses [ _x_ + _h, x_ + _h − n_<sup><u>1</u>]twicebeforehitting</sup><sup>_x −_</sup> _n_<sup><u>1</u>.</sup>

**Proof.** The decomposition of _Dn_ ( _x_ + _h_ ) is based on counting the number of downcrossings of the interval [ _x_ + _h−_ 1 _/n, x_ + _h_ ] that have taken place between the stopping times in the sequence


165

for _j ≥_ 1. By the strong Markov property the pieces


are all independent. The crucial observation of the proof is that the vector _Dn_ ( _x_ ) is a function of the pieces _B_<sup>(2</sup><sup>_j_)</sup> for _j ≥_ 1, whereas we shall define the random variables _D_ , _I_ 1 _, I_ 2 _, . . ._ and _N_ 1 _, N_ 2 _. . ._ depending only on the other pieces _B_<sup>(0)</sup> and _B_<sup>(2</sup><sup>_j−_1)</sup> for _j ≥_ 1.

First, let _D_ be the number of downcrossings of [ _x_ + _h, x_ + _h −_ 1 _/n_ ] during the time interval [0 _, τ_ 0]. Then fix _j ≥_ 1 and hence a piece _B_<sup>(2</sup><sup>_j−_1)</sup> . Define _Ij_ to be the indicator of the event that _B_<sup>(2</sup><sup>_j−_1)</sup> reaches level _x_ + _h_ during its lifetime. By Theorem 2.45 this event has probability 1 _/_ ( _nh_ + 1). Observe that the number of downcrossings by _B_<sup>(2</sup><sup>_j−_1)</sup> is zero if the event fails. If the event holds, we define _Nj_ as the number of downcrossings of [ _x_ + _h, x_ + _h −_ 1 _/n_ ] by _B_<sup>(2</sup><sup>_j−_1)</sup> , which is a geometric random variable with mean _nh_ + 1 by the strong Markov property and Theorem 2.45.

The claimed decomposition follows now from the fact that the pieces _B_<sup>(2</sup><sup>_j_)</sup> for _j ≥_ 1 do not upcross the interval [ _x_ + _h, x_ + _h −_ 1 _/n_ ] by definition and that _B_<sup>(2</sup><sup>_j−_1)</sup> for _j_ = 1 _, . . . , Dn_ ( _x_ ) are exactly the pieces that take place before the Brownian motion reaches level zero.

Lemma 6.31. _Suppose nun are nonnegative, even integers and un → u. Then_


_where X_<sup>˜</sup> _, Y_<sup>˜</sup> _are normally distributed with mean zero and variance h, the random variable M is Poisson distributed with parameter u/_ (2 _h_ ) _and Z_<sup>˜</sup> 1 _, Z_<sup>˜</sup> 2 _, . . . are exponentially distributed with mean h, and all these random variables are independent._

**Proof.** By Lemma 6.29, we have, for _X_<sup>˜</sup> , _Y_<sup>˜</sup> as defined in the lemma,


Moreover, we observe that


where _Bn_ is binomial with parameters _nun/_ 2 _∈{_ 0 _,_ 1 _, . . .}_ and 1 _/_ ( _nh_ + 1) _∈_ (0 _,_ 1) and independent of _N_ 1( _n_ )<sup>_, N_</sup> 2( _n_ )<sup>_, . . ._.Wenowshowthat,when</sup><sup>_n↑∞_,therandomvariables</sup><sup>_Bn_convergein</sup> distribution to _M_ and the random variables _n_<sup><u>1</u></sup><sup>_N_</sup> _j_ ( _n_ ) converge to _Z_<sup>˜</sup> _j_ , as defined in the lemma. For this purpose it suffices to show convergence of the Laplace transforms, see Proposition II.1.8. First note that, for _λ, θ >_ 0, we have


166

and hence


For the binomial distributions we have


and thus


Lemma 6.32. _Suppose X is standard normally distributed, Z_ 1 _, Z_ 2 _, . . . standard exponentially distributed and N Poisson distributed with parameter ℓ_<sup>2</sup> _/_ 2 _for some ℓ>_ 0 _. If all these random variables are independent, then_


**Proof.** It suffices to show that the Laplace transforms of the random variables on the two sides of the equation agree. Let _λ >_ 0. Completing the square, we find


From the special case _ℓ_ = 0 we get E exp _{−λ X_<sup>2</sup> _}_ = _~~√~~_ 2 _λ_ <u>1+1</u><sup>.Forany</sup><sup>_θ>_0,</sup>


167

Using this and that E exp _{−_ 2 _λ Zj}_ = 2 _λ_ <u>1+1</u><sup>weget</sup>


which completes the proof.

Remark 6.33. An alternative proof of Lemma 6.32 will be given in Exercise 6.6.


By combining the previous three lemmas we obtain the following convergence result for the conditional distribution of _Dn_ ( _x_ + _h_ ) given _Dn_ ( _x_ ), which is the ‘two-point version’ of the RayKnight theorem.

Lemma 6.34. _Suppose nun are nonnegative, even integers and un → u. For any λ ≥_ 0 _we have_


_where {W_ ( _x_ ): _x ≥_ 0 _} denotes a planar Brownian motion started in_ (0 _,_<sup>_√_</sup> _<u>u</u>_ <u>)</u> _∈_ R<sup>2</sup> _._ **Proof.** Combining Lemmas 6.30 and 6.31 we get


with _X_ , _Y_ are standard normally distributed, _Z_ 1 _, Z_ 2 _, . . ._ are standard exponentially distributed and _M_ is Poisson distributed with parameter _ℓ_<sup>2</sup> _/_ 2, for _ℓ_ = � _u/h_ . By Lemma 6.32 the right hand side can thus be rewritten as E� exp � _− λh_ �( _X_ + ~~�~~ _u/h_ )<sup>2</sup> + _Y_<sup>2��</sup> = E(0 _,_<sup>_~~√~~_</sup> _<u>u</u>_ <u>)�</u> exp � _− λ|W_ ( _h_ ) _|_<sup>2��</sup> _,_

which proves the lemma.

Now we complete the proof of Theorem 6.27. Note that, as both _{L_<sup>_x_</sup> ( _T_ ) : _x ≥_ 0 _}_ and _{|W_ ( _x_ ) _|_<sup>2</sup> : _x ≥_ 0 _}_ are continuous processes, it suffices to show that, for any

0 _< x_ 1 _< · · · < xm < a_

the vectors


have the same distribution. The Markov property of the downcrossing numbers, which approximate the local times, allows us to reduce this problem to the study of the ‘two-point version’.

168

Lemma 6.35. _For all sufficiently large integers n, the process_


_is a (possibly inhomogeneous) Markov chain._

**Proof.** Fix _k ∈{_ 2 _, . . . , m}_ . By Lemma 6.30 applied to _x_ = _xk−_ 1 and _h_ = _xk − xk−_ 1 we can write _Dn_ ( _xk_ ) as a function of _Dn_ ( _xk−_ 1) and various random variables, which by construction, are independent of _Dn_ ( _x_ 1) _, . . . , Dn_ ( _xk−_ 1). This establishes the Markov property.

Note that, by rotational invariance of planar Brownian motion, _{|W_ ( _xk_ ) _|_<sup>2</sup> : _k_ = 1 _, . . . , m}_ is a Markov chain with transition probabilities given by


for all _λ >_ 0. The following general fact about the convergence of families of Markov chains ensures that we have done enough to complete the proof of Theorem 6.27.

Lemma 6.36. _Suppose, for n_ = 1 _,_ 2 _, . . ., that {Xk_ ( _n_ ) : _k_ = 1 _, . . . , m} is a Markov chain with discrete state space_ Ω _n ⊂_ [0 _, ∞_ ) _and that {Xk_ : _k_ = 1 _, . . . , m} is a Markov chain with state space_ [0 _, ∞_ ) _. Suppose further that_


_Then_

_and, in particular, the vectors_ ( _X_ 1 _, . . . , Xm_ ) _and_ ( _Y_ 1 _, . . . , Ym_ ) _have the same distribution._

**Proof.** Recall from Proposition II.1.8 that it suffices to show that the Laplace transforms converge. Let _λ_ 1 _, . . . , λm ≥_ 0. By assumption (2) we have _X_ 1( _n_ ) _⇒ X_ 1 and hence we may assume, by way of induction, that for some fixed _k_ = 1 _, . . . , m −_ 1, we have


This implies, in particular, that ( _X_ 1 _, . . . , Xk_ ) and ( _Y_ 1 _, . . . , Yk_ ) have the same distribution. Define


and


169

Then, combining assumption (1) and (3), Φ _n_ ( _Xk_ ( _n_ )<sup>)</sup><sup>_→_Φ(</sup><sup>_Yk_)almostsurely.Hence,usingthis</sup> and once more assumption (1),


As the vectors ( _X_ 1 _, . . . , Xk_ ) and ( _Y_ 1 _, . . . , Yk_ ) have the same distribution the limit can be rewritten as


and this completes the induction step.

Finally, as ( _X_ 1( _n_ )<sup>_, . . . , X_(</sup> _m_<sup>_n_))convergesalmostsurely,andhencealsoindistributionto</sup> ( _Y_ 1 _, . . . , Ym_ ), this vector must have the same distribution as ( _X_ 1 _, . . . , Xm_ ). This completes the proof.

**Proof of Theorem 6.27.** We use Lemma 6.36 with _X_ ( _n_ ) = <u>2</u> _k n_<sup>_Dn_(</sup><sup>_xk_),</sup><sup>_Xk_=</sup><sup>_|W_(</sup><sup>_xk_)</sup><sup>_|_2</sup> and _Yk_ = _L_<sup>_xk_</sup> ( _T_ ). Then assumption (1) is satisfied by the downcrossing representation, assumption (2) follows from Lemma 6.29 and assumption (3) from Lemma 6.34. Lemma 6.36 thus gives that the random vectors ( _L_<sup>_x_1</sup> ( _T_ ) _, . . . , L_<sup>_xm_</sup> ( _T_ )) and ( _|W_ ( _x_ 1) _|_<sup>2</sup> _, . . . , |W_ ( _xm_ ) _|_<sup>2</sup> ) have the same distribution, which concludes the proof.

As an easy application of the Ray-Knight theorem, we answer the question whether, almost surely, _simultaneously_ for all levels _x ∈_ [0 _, a_ ) the local times at level _x_ are positive. Theorem 6.37 (Ray’s theorem). _Suppose a >_ 0 _and {B_ ( _t_ ) : 0 _≤ t ≤ Ta} is a linear Brownian motion started at zero and stopped at time Ta_ = inf _{t ≥_ 0 : _B_ ( _t_ ) = _a}, when it reaches level a for the first time. Then, almost surely, L_<sup>_x_</sup> ( _Ta_ ) _>_ 0 _for all_ 0 _≤ x < a._

**Proof.** The statement can be reworded as saying that the process _{L_<sup>_a−x_</sup> ( _Ta_ ) : 0 _< x ≤ a}_ almost surely does not hit zero. By the Ray-Knight theorem (applied to the Brownian motion _{a − B_ ( _t_ ): _t ≥_ 0 _}_ ) this process agrees with _{|W_ ( _x_ ) _|_<sup>2</sup> : 0 _< x ≤ a}_ for a standard planar Brownian motion _{W_ ( _x_ ) : _x ≥_ 0 _}_ which, by Theorem 3.19, never returns to the origin.

Ray’s theorem can be exploited to give a result on the Hausdorff dimension of the level sets of the Brownian motion, which holds _simultaneously_ for all levels _a ∈_ R.

Theorem 6.38. _Almost surely,_ dim _{t ≥_ 0 : _B_ ( _t_ ) = _a_ � _≥_ 2<sup><u>1</u></sup><sup>_,foralla ∈_R</sup><sup>_._</sup>

**Proof.** Obviously, it suffices to show that, for every fixed _a >_ 0, almost surely,

dim �0 _≤ t < Ta_ : _B_ ( _t_ ) = _x_ � _≥_ 2<sup><u>1</u></sup> for all 0 _≤ x < a ._

This can be achieved using the mass distribution principle. Considering the increasing function _L_<sup>_x_</sup> : [0 _, T_<sup>_a_</sup> ) _→_ [0 _, ∞_ ) as distribution function of a measure _ℓ_<sup>_x_</sup> , we infer from Theorem 6.37 and Theorem 6.18 that, almost surely, for every _x ∈_ [0 _, a_ ), the measure _ℓ_<sup>_x_</sup> is a mass distribution

170

on the set _{_ 0 _≤ t < Ta_ : _B_ ( _t_ ) = _x}_ . By Theorem 6.18, for any _γ <_ 1 _/_ 2, almost surely, there exists a (random) _C >_ 0 such that, for all _x ∈_ [0 _, a_ ), _t ∈_ [0 _, Ta_ ) and _ε ∈_ (0 _,_ 1),

_ℓ_<sup>_x_</sup> ( _t − ε, t_ + _ε_ ) _≤|L_<sup>_x_</sup> ( _t_ + _ε_ ) _− L_<sup>_x_</sup> ( _t − ε_ ) _| ≤ C_ (2 _ε_ )<sup>_γ_</sup> _._

The claim therefore follows from the mass distribution principle, Theorem 4.19.

Remark 6.39. Equality holds in Theorem 6.38. We will obtain the full result later as an easy corollary of Kaufman’s dimension doubling theorem, see Theorem 9.28. _⋄_

### **4. Brownian local time as a Hausdorff measure**

In this section we show that the local time _L_<sup>0</sup> ( _t_ ) can be obtained as an intrinsically defined measure of the random set Zero _∩_ [0 _, t_ ]. The only family of intrinsically defined measures on metric spaces we have encountered so far in this book is the family of _α_ -dimensional Hausdorff measures. As the _α_ -dimensional Hausdorff measure of the zero set is always either zero (if _α ≥_<sup><u>1</u></sup> 2<sup>)orinfinity(if</sup><sup>_α <_</sup><sup><u>1</u></sup> 2<sup>)weneedtolookoutforanalternativeconstruction.</sup>

We need not look very far. The definition of Hausdorff dimension still makes sense if we evaluate coverings by applying, instead of a simple power, an arbitrary nondecreasing function to the diameters of the sets in a covering.

Definition 6.40. _A nondecreasing function φ_ : [0 _, ε_ ) _→_ [0 _, ∞_ ) _with φ_ (0) = 0 _defined on a nonempty interval_ [0 _, ε_ ) _is called a_ **(Hausdorff) gauge function** _._

_Let X be a metric space and E ⊂ X. For every gauge function φ and δ >_ 0 _define_


_Then_

_is the_ **generalised** _φ_ **-Hausdorff measure** _of the set E._


Theorem* 6.41. _There exists a constant c >_ 0 _such that, almost surely, for all t >_ 0 _,_


The remainder of this section is devoted to the proof of this theorem. The material developed here will not be used in the remainder of the book. An important tool in the proof is the following classical theorem of Rogers and Taylor.

171

Proposition 6.42 (Rogers-Taylor Theorem). _Let µ be a Borel measure on_ R<sup>_d_</sup> _and let φ be a Hausdorff gauge function._

**(i)** _If_ Λ _⊂_ R<sup>_d_</sup> _is a Borel set and_


_for all x ∈_ Λ _, then H_<sup>_φ_</sup> (Λ) _≥ α_<sup>_−_1</sup> _µ_ (Λ) _._

**(ii)** _If_ Λ _⊂_ R<sup>_d_</sup> _is a Borel set and_


_for all x ∈_ Λ _, then H_<sup>_φ_</sup> (Λ) _≤ κdθ_<sup>_−_1</sup> _µ_ ( _V_ ) _for any open set V ⊂_ R<sup>_d_</sup> _that contains_ Λ _, where κd depends only on d._

_Moreover, in d_ = 1 _one can also obtain an analogue of (i) for one-sided intervals._

**(iii)** _If_ Λ _⊂_ R _is a closed set and_


Remark 6.43. If _µ_ is finite on compact sets, then _µ_ (Λ) is the infimum of _µ_ ( _V_ ) over all open sets _V ⊃_ Λ, see for example [ **Ru86** , 2.18]. Hence _µ_ ( _V_ ) can be replaced by _µ_ (Λ) on the right _⋄_ hand side of the inequality in (ii).

**Proof. (i)** We write


and note that _µ_ (Λ _ε_ ) _→ µ_ (Λ) as _ε ↓_ 0.

Fix _ε >_ 0 and consider a cover _{Aj}_ of Λ _ε_ . Suppose that _Aj_ intersects Λ _ε_ and _rj_ = _|Aj| < ε_ for all _j_ . Choose _xj ∈ Aj ∩_ Λ _ε_ for each _j_ . Then _µB_ ( _xj, rj_ ) _< αφ_ ( _rj_ ) for every _j_ , whence


Thus _Hε_<sup>_φ_(Λ)</sup><sup>_≥H_</sup> _ε_<sup>_φ_(Λ</sup><sup>_ε_)</sup><sup>_≥α−_1</sup><sup>_µ_(Λ</sup><sup>_ε_).Letting</sup><sup>_ε ↓_0proves(i).</sup>

**(ii)** Let _ε >_ 0. For each _x ∈_ Λ, choose a positive _rx < ε_ such that _B_ ( _x,_ 2 _rx_ ) _⊂ V_ and _µB_ ( _x, rx_ ) _> θφ_ ( _rx_ ); then among the dyadic cubes of diameter at most _rx_ that intersect _B_ ( _x, rx_ ), let _Qx_ be a cube with _µ_ ( _Qx_ ) maximal. (We consider here dyadic cubes of the form � _di_ =1<sup>[</sup><sup>_ai/_2</sup><sup>_m,_(</sup><sup>_ai_+ 1)</sup><sup>_/_2</sup><sup>_m_)where</sup><sup>_ai_areintegers).Inparticular,</sup><sup>_Qx⊂V_and</sup><sup>_|Qx| > rx/_2sothe</sup> side-length of _Qx_ is at least _rx/_ (2 _√d_ ). Let _Nd_ = 1 + 8 _⌈√d⌉_ and let _Q_<sup>_∗_</sup> _x_<sup>bethecubewiththe</sup> same center _zx_ as _Qx_ , scaled by _Nd_ (i.e., _Q_<sup>_∗_</sup> _x_<sup>=</sup><sup>_zx_+</sup><sup>_Nd_(</sup><sup>_Qx−zx_)).Observethat</sup><sup>_Q_</sup> _x_<sup>_∗_contains</sup>

172

_B_ ( _x, rx_ ), so _B_ ( _x, rx_ ) is covered by at most _Nd_<sup>_d_dyadic cubes that are translates of</sup><sup>_Qx_.Therefore,</sup> for every _x ∈_ Λ, we have


Let _{Qx_ ( _j_ ) : _j ≥_ 1 _}_ be any enumeration of the maximal dyadic cubes among _{Qx_ : _x ∈_ Λ _}_ . Then


The collection of cubes _{Q_<sup>_∗_</sup> _x_ ( _j_ )<sup>:</sup><sup>_j≥_1</sup><sup>_}_formsacoverofΛ.Sinceeachofthesecubesiscovered</sup> by _Nd_<sup>_d_cubesofdiameteratmost</sup><sup>_rx_(</sup><sup>_j_),weinferthat</sup>


Letting _ε ↓_ 0 proves (ii).

**(iii)** Without loss of generality we may assume that _µ_ has no atoms. Given _ε >_ 0 we find _δ >_ 0 such that


satisfies _µ_ (Λ _δ_ ( _α_ )) _>_ (1 _− ε_ ) _µ_ (Λ). Observe that Λ _δ_ ( _α_ ) is closed. Given a cover _{I_<sup>˜</sup> _j}_ of Λ with _|I_<sup>˜</sup> _j| < δ_ we look at _Ij_ = [ _aj, bj_ ] where _aj_ is the maximum and _bj_ the minimum of the closed set cl _I_<sup>˜</sup> _j ∩_ Λ _δ_ ( _α_ ). Then _{Ij}_ covers Λ _δ_ ( _α_ ) and hence


and (iii) follows for _δ ↓_ 0, as _ε >_ 0 was arbitrary.

For the proof of Theorem 6.41 we first note that, by Theorem 6.10, it is equivalent to show that, for the maximum process _{M_ ( _t_ ): _t ≥_ 0 _}_ of a Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ , we have, almost surely,


where Rec = _{s ≥_ 0: _B_ ( _s_ ) = _M_ ( _s_ ) _}_ denotes the set of record points of the Brownian motion. We define the measure _µ_ on Rec as given by the distribution function _M_ , i.e.


Then _µ_ is also the image measure of the Lebesgue measure on [0 _, ∞_ ) under the mapping


The main part is to show that, for closed sets Λ _⊂_ [0 _, ∞_ ),


where _φ_ ( _r_ ) = � _r_ log log(1 _/r_ ) and _c, C_ are positive constants.

173

The easier direction, the lower bound for the Hausdorff measure, follows from part **(iii)** of the Rogers-Taylor theorem and the upper bound in the law of the iterated logarithm. Indeed, for any level _a >_ 0 let _Ta_ = inf _{s ≥_ 0 : _B_ ( _t_ ) = _a}_ . Then, by Corollary 5.3 applied to the standard Brownian motion _{B_ ( _Ta_ + _t_ ) _− B_ ( _Ta_ ): _t ≥_ 0 _}_ , almost surely,


Defining the set

_A_ = � _s ∈_ Rec : lim sup _µ_ [ _s, s_ + _r_ ] _/φ_ ( _r_ ) _≤ √_ 2 ~~�~~ _, r↓_ 0

this means that, for every _a >_ 0, we have _Ta ∈ A_ almost surely. By Fubini’s theorem,


and hence, almost surely, _µ_ ( _A_<sup>c</sup> ) = 0. By part **(iii)** of the Rogers-Taylor theorem, for every closed set Λ _⊂_ [0 _, ∞_ ),


showing the left inequality in (4.1).

For the harder direction, the upper bound for the Hausdorff measure, it is important to note that the lower bound in Corollary 5.3 does not suffice. Instead, we need a law of the iterated logarithm which holds simultaneously for _H_<sup>_φ_</sup> -almost all record times.

Lemma 6.44. _For every ϑ >_ 0 _small enough, almost surely,_


**Proof.** We only need to prove that, for some _ϑ >_ 0, the set

satisfies _H_<sup>_φ_</sup> (Λ( _ϑ_ )) = 0. Moreover, denoting


we have


It thus suffices to show, for fixed _δ >_ 0, that, almost surely,


Fix _δ >_ 0 and a positive integer _n_ such that 1 _/_<sup>_√_</sup> _<u>n < δ</u>_ . For parameters


which we choose later, we say that an interval of the form _I_ = [( _k −_ 1) _/n, k/n_ ] with _k ∈ {_ 1 _, . . . , n}_ is _good_ if

174

(i) _I_ contains a record point, in other words,


and either of the following two conditions hold,

(ii) there exists _j ≥_ 0 with 1 _≤ q_<sup>_j_+1</sup> _≤_<sup>_√_</sup> _<u>n</u>_ such that


(iii) for all _j ≥_ 0 with 1 _≤ q_<sup>_j_+1</sup> _≤_<sup>_√_</sup> _<u>n</u>_ we have that


We now argue pathwise, and show that, given _A >_ 1, _θ > ϑ_ we can find _q >_ 2 such that the good intervals cover the set Λ _δ_ ( _ϑ_ ). Indeed, suppose that _I_ is not good but contains a minimal record point _τ ∈_ [( _k −_ 1) _/n, k/n_ ]. Then there exists _j ≥_ 0 with 1 _≤ q_<sup>_j_+1</sup> _≤_<sup>_√_</sup> _<u>n</u>_ such that


This implies that, for any _t ∈_ [( _k −_ 1) _/n, k/n_ ] _∩_ Rec,

if _q_ is chosen large enough. Hence the interval _I_ does not intersect Λ _δ_ ( _ϑ_ ) and therefore the good intervals cover this set.

Next we show that, for any _A > √_ 2 _> θ_ and suitably chosen _C >_ 0, for every _I_ = [( _k−_ 1) _/n, k/n_ ] with _I ∩_ [ _δ,_ 1 _− δ_ ] _̸_ = _∅_ ,


By Lemma 4.22 in conjunction with Theorem 6.10 we get, for some constant _C_ 0 _>_ 0 depending only on _δ >_ 0,


We further get, for some constant _C_ 1 _>_ 0, for all _j_ with _q_<sup>_j_+1</sup> _≤_<sup>_√_</sup> _<u>n</u>_ <u>,</u>


Using the independence of these events and summing over all _j ≥_ 0 with 1 _≤ q_<sup>_j_+1</sup> _≤_<sup>_√_</sup> _<u>n</u>_ <u>,</u> of which there are no more than _C_ 2 log _n_ , we get that


175

To estimate the probability that [( _k −_ 1) _/n, k/n_ ] satisfies (i) and (iii) we first note that


using Lemma II.3.1. From this we infer that, for suitable _c_ 3 _>_ 0,


Combining this with the estimate for _τ < k/n_ we get that


As _θ < √_ 2, the right hand side in (4.4) is of smaller order than the right hand side in (4.3) and hence we have shown (4.2).

Finally, we look at the expected _φ_ -values of our covering. We obtain that


and, by Fatou’s lemma we get, almost surely,


as required to complete the proof.

The right inequality in (4.1) now follows easily from Lemma 6.44 and part **(ii)** of the RogersTaylor theorem. We define the set


and note that _H_<sup>_φ_</sup> (Rec _∩ A_<sup>c</sup> ) = 0, for _ϑ_ sufficiently small. By part **(ii)** of the Rogers-Taylor theorem we get, for every Borel set Λ _⊂_ [0 _, ∞_ ),


This implies the right inequality and hence completes the proof of (4.1).

176

To complete the proof of Theorem 6.41 we look at the process _{X_ ( _a_ ): _a ≥_ 0 _}_ defined by

_X_ ( _a_ ) = _H_<sup>_φ_�</sup> Rec _∩_ [0 _, Ta_ ]� _._

The next lemma will help us to show that this process is trivial.

Lemma 6.45. _Suppose {Y_ ( _t_ ): _t ≥_ 0 _} is stochastic process starting in zero with the following properties,_

- _the paths are almost surely continuous,_

- _the increments are independent, nonnegative and stationary,_

- _there exists a C >_ 0 _such that, almost surely, Y_ ( _t_ ) _≤ C t for all t >_ 0 _._

_Then there exists c_ ˜ _≥_ 0 _such that, almost surely, Y_ ( _t_ ) = ˜ _c t for every t ≥_ 0 _._

**Proof.** We first look at the function _m_ : [0 _, ∞_ ) _→_ [0 _, ∞_ ) defined by _m_ ( _t_ ) = E _Y_ ( _t_ ). This function is continuous, as the paths of _{Y_ ( _t_ ): _t ≥_ 0 _}_ are continuous and bounded on compact sets. Further, because the process _{Y_ ( _t_ ): _t ≥_ 0 _}_ has independent and stationary increments, the function _m_ is linear and hence there exists _c_ ˜ _≥_ 0 with _m_ ( _t_ ) = ˜ _c t_ .

It thus suffices to show that the variance of _Y_ ( _t_ ) is zero. Indeed, for every _n >_ 0, we have


and hence _Y_ ( _t_ ) = E _Y_ ( _t_ ) = ˜ _c t_ as claimed.

Let us check that _{X_ ( _a_ ): _a ≥_ 0 _}_ satisfies the conditions of Lemma 6.45. We first note that

_X_ ( _a_ + _h_ ) _− X_ ( _a_ ) = _H_<sup>_φ_�</sup> Rec _∩_ [0 _, Ta_ + _h_ ]� _−H_<sup>_φ_�</sup> Rec _∩_ [0 _, Ta_ ]� = _H_<sup>_φ_�</sup> Rec _∩_ [ _Ta, Ta_ + _h_ ]� _,_

as can be seen easily from the definition of the Hausdorff measure _H_<sup>_φ_</sup> .

Using this, continuity of the paths follows from the fact that, by (4.1),


The strong Markov property implies that the increments are independent and stationary, and they are obviously nonnegative. And finally, by (4.1), almost surely, for any _a ≥_ 0,


Lemma 6.45 thus implies that there exists _c_ ˜ _≥_ 0 with


for all _a ≥_ 0. The set _{Ta_ : _a ∈_ R _}_ is dense in Rec. Indeed, the only elements in Rec _\{Ta_ : _a ∈_ R _}_ are the countably many times when the Brownian motion revisits a local maximum for the first time. These times are stopping times and can therefore be approximated from the right by elements of _{Ta_ : _a ∈_ R _}_ .

177

Using continuity, we infer that, almost surely, _H_<sup>_φ_�</sup> Rec _∩_ [0 _, t_ ]� = _c M_ ˜ ( _t_ ) for all _t ∈_ Rec. For general _t ≥_ 0 we let _τ_ = max(Rec _∩_ [0 _, t_ ]) and note that

_H_<sup>_φ_�</sup> Rec _∩_ [0 _, t_ ]� = _H_<sup>_φ_�</sup> Rec _∩_ [0 _, τ_ ]� = ˜ _c M_ ( _τ_ ) = ˜ _c M_ ( _t_ ) _._ By the lower bound in (4.1) we must have _c >_ ˜ 0 and hence we can put _c_ = 1 _/c_ ˜ and get _M_ ( _t_ ) = _c H_<sup>_φ_�</sup> Rec _∩_ [0 _, t_ ]� = _H_<sup>_cφ_�</sup> Rec _∩_ [0 _, t_ ]� _,_

as required to complete the proof of Theorem 6.41.

178

### **Exercises**

Exercise 6.1. Using the downcrossing representation of the local time process _{L_ ( _t_ ): _t ≥_ 0 _}_ given in Theorem 6.1, show that, almost surely, _L_ ( _s_ ) = _L_ ( _t_ ) for every interval ( _s, t_ ) not containing a zero of the Brownian motion. In other words, the local time at zero increases only on the zero set of the Brownian motion.

Exercise 6.2. Show, by reviewing the argument in the proof of Theorem 6.10, that for a standard linear Brownian motion the processes _{_ ( _|B_ ( _t_ ) _|, L_ ( _t_ )): _t ≥_ 0 _}_ and _{_ ( _M_ ( _t_ ) _− B_ ( _t_ ) _, M_ ( _t_ )): _t ≥_ 0 _}_ have the same distribution.

**Hint.** In Theorem 7.36 we give an alternative proof of this result using stochastic integration.

Exercise 6.3. Show that P0 _{L_ ( _t_ ) _>_ 0 for every _t >_ 0 _}_ = 1.

**Hint.** This follows easily from Theorem 6.10.

Exercise 6.4 ( _∗_ ). Let _{W_ ( _s_ ): _s ≥_ 0 _}_ be a standard linear Brownian motion and _τ_ 1 its first hitting time of level 1. Show that


**Hint.** Use Exercise 2.15.

Exercise 6.5 ( _∗_ ). Suppose _X_ 1 _, X_ 2 _, . . ._ are independent geometrically distributed random variables with mean 2. Then, for sufficiently small _ε >_ 0, for all nonnegative integers _k ≤ m_ ,


Exercise 6.6 ( _∗_ ). Give an alternative proof of Lemma 6.32 by computing the densities of the random variables ( _X_ + _ℓ_ )<sup>2</sup> and _X_<sup>2</sup> + 2<sup>�</sup><sup>_N_</sup> _j_ =1<sup>_Zj_.</sup>

179

Exercise 6.7. Use the Ray-Knight theorem and L´evy’s theorem, Theorem 6.10, to show that, for a suitable constant _c >_ 0, the function

_ϕ_ ( _h_ ) = _c_ ~~�~~ _h_ log(1 _/h_ ) for 0 _< h <_ 1 _,_

is a modulus of continuity for the random field _{L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _, t ≥_ 0 _}_ .

180

### **Notes and Comments**

The study of local times is crucial for the Brownian motion in dimension one and good references are [ **RY94** ] and the survey article [ **Bo89** ]. Brownian local times were first introduced by Paul L´evy in [ **Le48** ] and a thorough investigation is initiated in a paper by Trotter [ **Tr58** ] who showed that there is a version of local time continuous in time and space. An alternative construction of local times can be given in terms of stochastic integrals, using Tanaka’s formula as a definition. We shall explore this direction in Section 7.3.

The equality for the upcrossing numbers in Lemma 6.3 agrees with the functional equation for a branching process with immigration. The relationship between local times and branching processes, which is underlying our entire treatment, can be exploited and extended in various ways. One example of this can be found in Neveu and Pitman [ **NP89** ], for more recent progress in this direction, see Le Gall and Le Jan, [ **LL98** ]. A good source for further reading is the discussion of L´evy processes and trees by Duquesne and Le Gall in [ **DL02** ]. For an introdution into branching processes with and without immigration, see [ **AN04** ].

In a similar spirit, a result which is often called the second Ray-Knight theorem describes the process _{L_<sup>_a_</sup> _T_<sup>:</sup><sup>_a>_0</sup><sup>_}_when</sup><sup>_T_=inf</sup><sup>_{t>_0:</sup><sup>_L_0</sup> _t_<sup>=</sup><sup>_x}_,see[</sup><sup>**RY94**]ortheoriginalpapersby</sup> Ray and Knight cited above. The resulting process is a Feller diffusion, which is the canonical process describing critical branching with initial mass _x_ . The local times of Brownian motion can therefore be used to encode the branching information for a variety of processes describing the evolution of particles which undergo critical branching and spatial migration. For more information on this powerful link between Brownian motion and the world of spatial branching processes, see for example [ **LG99** ].

The concept of local times can be extended to a variety of processes like continuous semimartingales, see e.g. [ **RY94** ], or Markov processes [ **BG68** ]. The idea of introducing local times as densities of occupation measure has been fruitful in a variety of contexts, in particular in the introduction of local times on the intersection of Brownian paths. Important papers in this direction are [ **GH80** ] and [ **GHR84** ].

The Ray-Knight theorem was discovered by D. Ray and F. Knight independently by different methods in 1963. The proof of Knight uses discretisation, see [ **Kn63** ] for the original paper and [ **Kn81** ] for more information. Ray’s approach to Theorem 6.27 is less intuitive but more versatile, and is based on the Feynman-Kac formula, see [ **Ra63b** ] for the original paper. Our presentation is simpler than Knight’s method. The distributional identity at its core, see Lemma 6.32, is yet to be explained probabilistically. The analytic proof given in Exercise 6.6 is due to H. Robbins and E.J.G. Pitman [ **RP49** ].

181

Extensions of the Ray-Knight theorem includes a characterisation of _{L_<sup>_x_</sup> ( _T_ ) : _x ≥_ 0 _}_ for parameters exceeding _a_ . This is best discussed in the framework of Brownian excursion theory, see for example [ **RY94** ]. The Ray-Knight theorem can be extended into a deep relationship between the local times of symmetric Markov processes and an associated Gaussian process, which is the subject of the famous Dynkin isomorphism theorem. See Eisenbaum [ **Ei94** ] or the comprehensive monograph by Marcus and Rosen [ **MR06** ] for more on this subject.

According to Taylor [ **Ta86** ], Hausdorff measures with arbitrary gauge functions were introduced by A.S. Besicovitch. General theory of outer measures, as presented in [ **Ro99** ] shows that _H_<sup>_φ_</sup> indeed defines a measures on the Borel sets of a metric space. The fact that the local time at zero agrees with the _H_<sup>_φ_</sup> Hausdorff measure of the zero set is due to Taylor and Wendel [ **TW66** ]. It can be shown that the local times _L_<sup>_a_</sup> ( _t_ ) agree with the Hausdorff measure of the set _{s ∈_ [0 _, t_ ]: _B_ ( _s_ ) = _a}_ simultaneously for all levels _a_ and times _t_ . This delicate result is proved in [ **Pe81** ] using nonstandard analysis.

The Rogers-Taylor theorem is due to C.A. Rogers and S.J. Taylor in [ **RT61** ]. The original statement is slightly more general as it allows to replace _µ_ ( _V_ ) by _µ_ (Λ) on the right hand side without any regularity condition on _µ_ . Most proofs in the literature of the harder half, statement (ii) in our formulation, use the Besicovitch covering theorem. We give a self-contained proof using dyadic cubes instead.

Other natural measures related to Brownian motion can also be shown to agree with Hausdorff measures with suitable gauge functions. The most notable example is the occupation measure, whose gauge function is


This result is due to Ciesielsky and Taylor [ **CT62** ] in the first case, and to Ray [ **Ra63a** ] and Taylor [ **Ta64** ] in the second case. A stimulating survey of this subject is [ **LG85** ].

182

### CHAPTER 7

---

[← Brownian motion and random walk](09-brownian-motion-and-random-walk.md) · [Up: contents](index.md) · [Stochastic integrals and applications →](11-stochastic-integrals-and-applications.md)
