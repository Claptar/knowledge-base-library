---
title: Hw
source: https://www.stat.berkeley.edu/~aldous/205A/hw.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/hw.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Hw

**Source:** [`hw.pdf`](https://www.stat.berkeley.edu/~aldous/205A/hw.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **205A Homework #1** , due Tuesday 6 September.

**1.** [Bill. 2.4] Let _Fn_ be classes of subsets of _S_ . Suppose each _Fn_ is a field, and _Fn ⊂Fn_ +1 for _n_ = 1 _,_ 2 _, . . ._ . Define _F_ = _∪_<sup>_∞_</sup> _n_ =1<sup>_Fn_.Showthat</sup><sup>_F_isa</sup> field. Give an example to show that, if each _Fn_ is a _σ_ -field, then _F_ need not be a _σ_ -field.

**2.** [Bill. 2.5(b)] Given a non-empty collection _A_ of sets, we defined _F_ ( _A_ ) as the intersection of all fields containing _A_ . Show that _F_ ( _A_ ) is the class of sets of the form _∪_<sup>_m_</sup> _i_ =1<sup>_∩n_</sup> _j_ =1<sup>_iAij_,whereforeach</sup><sup>_i_and</sup><sup>_j_either</sup><sup>_Ai,j∈A_or</sup> _A_<sup>_c_</sup> _ij_<sup>_∈A_,andwherethe</sup><sup>_m_sets</sup><sup>_∩n_</sup> _j_ =1<sup>_iAij,_1</sup><sup>_≤i ≤m_aredisjoint.</sup>

**3.** [Bill. 2.8] Suppose _B ∈ σ_ ( _A_ ), for some collection _A_ of subsets. Show there exists a countable subcollection _AB_ of _A_ such that _B ∈ σ_ ( _AB_ ).

**4.** Show that the Borel _σ_ -field on R<sup>_d_</sup> is the smallest _σ_ -field that makes all continuous functions _f_ : R<sup>_d_</sup> _→ R_ measurable.

**5.** [Durr. 1.3.5] A function _f_ : R<sup>_d_</sup> _→ R_ is _lower semicontinuous_ (l.s.c.) if lim inf _y→x f_ ( _y_ ) _≥ f_ ( _x_ ) for all x. A function is _upper semicontinuous_ (u.s.c.) if lim sup _y→x f_ ( _y_ ) _≤ f_ ( _x_ ) for all x. Show that, if _f_ is l.s.c. or u.s.c., then _f_ is measurable.

1

**205A Homework #2** , due Tuesday 13 September.

**1.** [similar Bill. 2.15] Let _B_ be the Borel subsets of R. For _B ∈B_ define


(a) Show that _µ_ is not finitely additive on _B_ .

(b) Show that _µ_ is finitely additive but not countably additive on the field _B_ 0 of finite disjoint unions of intervals ( _a, b_ ].

**2.** Show that, in the definition of “a probability measure _µ_ on a measurable space ( _S, S_ )”, we may replace “countably additive” by “finitely additive, and satisfies

if _An ↓ φ_ then _µ_ ( _An_ ) _→_ 0 _._ ”

**3.** [similar Durr. A.1.1] Give an example of a measurable space ( _S, S_ ), a collection _A_ and probability measures _µ_ and _ν_ such that

(i) _µ_ ( _A_ ) = _ν_ ( _A_ ) for all _A ∈A_

(ii) _S_ = _σ_ ( _A_ )

(iii) _µ̸_ = _ν_ .

Note: this can be done with _S_ = _{_ 1 _,_ 2 _,_ 3 _,_ 4 _}_

**4.** [similar Durr. Lemma A.2.1] Let _µ_ be a probability measure on ( _S, S_ ), where _S_ = _σ_ ( _F_ ) for a field _F_ . Show that for each _B ∈S_ and _ε >_ 0 there exists _A ∈F_ such that _µ_ ( _B_ ∆ _A_ ) _< ε_ .

**5.** Let _g_ : [0 _,_ 1] _→_ R be integrable w.r.t. Lebesgue measure. Let _ε >_

0. Show that there exists a continuous function _f_ : [0 _,_ 1] _→_ R such that � _|f_ ( _x_ ) _− g_ ( _x_ ) _| dx ≤ ε_ .

2

**205A Homework #3** , due Tuesday 20 September.

**1.** Use the monotone convergence theorem to prove the following.

(i) If _Xn ≥_ 0, _Xn ↓ X_ a.s. and _EXn < ∞_ for some _n_ then _EXn → EX_ .

(ii) If _E|X| < ∞_ then _E|X|_ 1( _|X|>n_ ) _→_ 0 as _n →∞_ .

(iii) If _E|X_ 1 _| < ∞_ and _Xn ↑ X_ a.s. then either _EXn ↑ EX < ∞_ or else _EXn ↑∞_ and _E|X|_ = _∞_ .

(iv) If _X_ takes values in the non-negative integers then


**2.** (i) For a counting r.v. _X_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>1</sup><sup>_A_</sup> _i_<sup>,giveaformulaforthevarianceof</sup>

_X_ in terms of the probabilities _P_ ( _Ai_ ) and _P_ ( _Ai ∩ Aj_ ), _i̸_ = _j_ .

(ii) If _k_ balls are put at random into _n_ boxes, what is the variance of _X_ = number of empty boxes?

**3.** (i) Suppose _EX_ = 0 and var( _X_ ) = _σ_<sup>2</sup> _< ∞_ . Prove


(ii) Suppose _X ≥_ 0 and _EX_<sup>2</sup> _< ∞_ . Prove


**4. Chebyshev’s other inequality.**

Let _f_ : R _→_ R and _g_ : R _→_ R be bounded and increasing functions. Prove that, for any r.v. _X_ ,


[In other words, _f_ ( _X_ ) and _g_ ( _X_ ) are positively correlated. This is intuitively obvious, but a little tricky to prove. Hint: consider an independent copy _Y_ of _X_ . For this and the next question you may need the product rule for expectations of independent r.v.s]

**5.** Let _X_ have Poisson( _λ_ ) distribution and let _Y_ have Poisson(2 _λ_ ) distribution.

(i) Prove _P_ ( _X ≥ Y_ ) _≤_ exp( _−_ (3 _− √_ 8) _λ_ ) if _X_ and _Y_ are independent.

(ii) Find constants _A < ∞_ , _c >_ 0, not depending on _λ_ , such that, without assuming independence, _P_ ( _X ≥ Y_ ) _≤ A_ exp( _−cλ_ ).

3

**205A Homework #4** , due Tuesday 27 September.

**1. Monte Carlo integration** [cf. Durr. 2.2.3] Let _f_ : [0 _,_ 1] _→_ R be such that �01<sup>_f_2(</sup><sup>_x_)</sup><sup>_dx < ∞_.Let(</sup><sup>_Ui_)bei.i.d.Uniform(0</sup><sup>_,_1).Let</sup>


(i) Use Chebyshev’s inequality to bound _P_ ( _|Dn| > ε_ ).

(ii) Show this bound remains true if the ( _Ui_ ) are only _pairwise_ independent.

**2.** Let _X ≥_ 0 and _Y ≥_ 0 be independent r.v.’s with densities _f_ and _g_ . Calculate the densities of _XY_ and of _X/Y_ .

_Note:_ this is just to remind you of “undergraduate” results.

**3.** [Durr. 2.2.2.] Let ( _Xi_ ) be r.v.’s with _EXi_ = 0 and _EXiXj ≤ r_ ( _j −i_ ) _,_ 1 _≤ i ≤ j < ∞_ , where _r_ ( _n_ ) is a deterministic sequence with _r_ ( _n_ ) _→_ 0 as _n →∞_ . Prove that _n_<sup>_−_1 �</sup><sup>_n_</sup> _i_ =1<sup>_Xi→_0inprobability.</sup>

**4.** [Durr. 2.3.11] Suppose events _An_ satisfy _P_ ( _An_ ) _→_ 0 and


Prove that


**5.** (a) Let _Z_ have standard Normal distribution. Show


(b) Let ( _Z_ 1 _, Z_ 2 _, . . ._ ) be independent with standard Normal distribution. Find constants _cn →∞_ such that

lim sup _Zn/cn_ = 1 a.s. _n_

4

**205A Homework #5** , due Tuesday 4 October.

**1.** Let ( _Xn_ ) be i.i.d. with _E|X_ 1 _| < ∞_ . Let _Mn_ = max( _X_ 1 _, . . . , Xn_ ). Prove that _n_<sup>_−_1</sup> _Mn →_ 0 a.s.

**2.** [Durr. 2.3.2] Let 0 _≤ X_ 1 _≤ X_ 2 _≤ . . ._ be r.v.’s such that _EXn ∼ an_<sup>_α_</sup> and var( _Xn_ ) _≤ Bn_<sup>_β_</sup> , where 0 _< a, B < ∞_ and 0 _< β <_ 2 _α < ∞_ . Prove that _n_<sup>_−α_</sup> _Xn → a_ a.s.

**3.** Prove that the following are equivalent.

- (i) _Xn → X_ in probability.

- (ii) There exist _εn ↓_ 0 such that _P_ ( _|Xn − X| > εn_ ) _≤ εn_ .

- (iii) _E_ min( _|Xn − X|,_ 1) _→_ 0.

**4.** Durr. exercise 2.4.4 ( _An Investment Problem_ ).

**5.** Prove the deterministic lemma we used in the proof of the GlivenkoCantelli Theorem.

**Lemma.** _If F_ 1 _, F_ 2 _, . . . , F are distribution functions and_

(i) _Fn_ ( _x_ ) _→ F_ ( _x_ ) _for each rational x_ (ii) _Fn_ ( _x_ ) _→ F_ ( _x_ ) _and Fn_ ( _x−_ ) _→ F_ ( _x−_ ) _for each atom x of F then_ sup _x |Fn_ ( _x_ ) _− F_ ( _x_ ) _| →_ 0.

5

**205A Homework #6** , due Tuesday 11 October.

**1.** [Durr. 2.5.9] Let ( _Xi_ ) be independent, _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_,</sup><sup>_S_</sup> _n_<sup>_∗_= max</sup><sup>_i≤n|Si|_.</sup> Prove that


[Hint. If _|Sj| >_ 2 _a_ and _|Sn − Sj| ≤ a_ then _|Sn| > a_ .]

**2.** [Durr. 2.5.10 and 11] In the setting of the previous question, prove

(i) if lim _n→∞ Sn_ exists in probability then the limit exists a.s.

(ii) if the ( _Xi_ ) are identically distributed and if _n_<sup>_−_1</sup> _Sn →_ 0 in probability then _n_<sup>_−_1</sup> max _m≤n Sm →_ 0 in probability.

**3.** [cf. Durr 2.2.8] Let ( _Xi_ ) be i.i.d. taking values in _{−_ 1 _,_ 1 _,_ 3 _,_ 7 _,_ 15 _, . . .}_ , such that


(which implicitly specifies _P_ ( _X_ 1 = _−_ 1)).

(a) Show _EX_ 1 = 0.

(b) Show that for all _α <_ 1,


_Comment._ This is sometimes described as “an unfair, fair game”. It shows that the conclusions of the SLLN and the “recurrence of sums” theorem can’t be strengthened much.

6

**205A Homework #7** , due Tuesday 18 October.

**1.** Suppose _S_ and _T_ are stopping times. Are the following necessarily stopping times? Give proof or counter-example.

(a) min( _S, T_ )

(b) max( _S, T_ )

(c) _S_ + _T_ .

**2.** Let ( _Xi_ ) be i.i.d. with _EXi_<sup>2</sup><sup>_<∞_.Let</sup><sup>_Sn_=�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_.Let</sup><sup>_T_bea</sup> bounded stopping time. Is it true in general that

var( _ST_ ) = (var( _X_ 1))( _ET_ )?

If not, is it true in the special case _EX_ 1 = 0?

**3.** Let ( _Xi_ ) be a sequence of random variables, and let _T_ be its tail _σ_ -field. Let _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_.Let</sup><sup>_bn↑∞_beconstants.Whichofthefollowingevents</sup> must be in _T_ ? Give proof or counter-example.

(i) _{Xn →_ 0 _}_ (ii) _{Sn_ converges _}_

(iii) _{Xn > bn_ infinitely often _}_

(iv) _{Sn > bn_ infinitely often _}_

_<u>√</u>_ <u>�</u> _<u>ni</u>_ =1<sup>_X_</sup> _<u>i</u>_<sup>2</sup> (v) _{ Sn →_ 0 _}_ .

**4.** Let _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_, where (</sup><sup>_Xi_) are i.i.d.with exponential(1) distribution.</sup> Use the large deviation theorem to get explicit limits for

_n_<sup>_−_1</sup> log _P_ ( _n_<sup>_−_1</sup> _Sn ≥ a_ ) _, a >_ 1 and _n_<sup>_−_1</sup> log _P_ ( _n_<sup>_−_1</sup> _Sn ≤ a_ ) _, a <_ 1.

**5. Oriented first passage percolation.** Consider the lattice quadrant _{_ ( _i, j_ ) : _i, j ≥_ 0 _}_ with directed edges ( _i, j_ ) _→_ ( _i_ + 1 _, j_ ) and ( _i, j_ ) _→_ ( _i, j_ + 1). Associate to each edge _e_ an exponential(1) r.v. _Xe_ , independent for different edges. For each directed path _π_ of length _d_ started at (0 _,_ 0), let _Sπ_ = �edges _e_ in path<sup>_Xe_.Let</sup><sup>_Hd_betheminimumof</sup><sup>_Sπ_overallsuchpaths</sup><sup>_π_</sup> of length _d_ . It can be shown that _d_<sup>_−_1</sup> _Hd → c_ a.s., for some constant _c_ . Give explicit upper and lower bounds on _c_ .

[Hint: use result of previous question for lower bound.]

7

**205A Homework #8** , due Tuesday 1 November.

[Theorem 7 and Corollary 8 refer to the notes linked from the “week 8” row of the schedule.]

**1.** Suppose probability measures satisfy _π ≪ ν ≪ µ_ . Show that


**2** . In the setting of Theorem 7 [hard part], where _S_ 2 is nice, show that _Q_ is unique in the following sense. If _Q_<sup>_∗_</sup> is another conditional probability kernel for _µ_ , then


**3.** Let _F_ be a distribution function. Let _c >_ 0. Find a simple formula for


**4** . In the proof of Corollary 8 we used the inverse distribution function


associated with the kernel _Q_ . Show that _f_ is product measurable.

**5** . Given a triple ( _X_ 1 _, X_ 2 _, X_ 3), we can define 3 p.m.’s _µ_ 12 _, µ_ 13 _, µ_ 23 on R<sup>2</sup> by


These p.m.’s satisfy a consistency condition:

the marginal distribution _µ_ 1 obtained from _µ_ 12 must coincide with the marginal obtained from _µ_ 13, and similarly for _µ_ 2 and _µ_ 3. (2)

Give an example to show that the converse is false. That is, give an example of _µ_ 12 _, µ_ 13 _, µ_ 23 satisfying (2) but for which there does not exist a triple ( _X_ 1 _, X_ 2 _, X_ 3) satisfying (1).

8

**205A Homework #9** , due Tuesday 8 November

**1** . Let _X, Y_ be random variables, and suppose _Y_ is measurable with respect to some sub- _σ_ -field _G_ . Let _µ_ ( _ω, ·_ ) be a regular conditional distribution for _X_ given _G_ . Prove that, for bounded measurable _h_ ,


**2.** For _i_ = 1 _,_ 2 let _Xi_ be a r.v. defined on (Ω _, F, P_ ) taking values in ( _Si, Si_ ). Let _G_ be a sub- _σ_ -field of _F_ . Prove that assertions (a),(b) and (c) below are equivalent. When these assertions hold, we say call _X_ 1 and _X_ 2 are conditionally independent <u>given</u> _<u>G</u>_ .

(a) _P_ ( _X_ 1 _∈ A_ 1 _, X_ 2 _∈ A_ 2 _|G_ ) = _P_ ( _X_ 1 _∈ A_ 2 _|G_ ) _P_ ( _X_ 2 _∈ A_ 2 _|G_ ) for all _Ai ∈Si_ .

(b) _E_ ( _h_ 1( _X_ 1) _h_ 2( _X_ 2) _|G_ ) = _E_ ( _h_ 1( _X_ 1) _|G_ ) _E_ ( _h_ 2( _X_ 2) _|G_ ) for all bounded measurable _hi_ : _Si →_ R.

(c) _E_ ( _h_ 1( _X_ 1) _|G, X_ 2) = _E_ ( _h_ 1( _X_ 1) _|G_ ) for all bounded measurable _h_ 1 : _S_ 1 _→_ R.

**3** . Suppose _X_ and _Y_ are conditionally independent given _Z_ . Suppose _X_ and _Z_ are conditionally independent given _F_ , where _F ⊆ σ_ ( _Z_ ). Prove that _X_ and _Y_ are conditionally independent given _F_ .

**4.** Let ( _Xn_ ) and ( _Yn_ ) be submartingales w.r.t. ( _Fn_ ). Show that ( _Xn_ + _Yn_ ) and that (max( _Xn, Yn_ )) are also submartingales w.r.t. ( _Fn_ ).

**5.** Give an example where

( _Xn_ ) is a submartingale w.r.t. ( _Fn_ )

( _Yn_ ) is a submartingale w.r.t. ( _Gn_ )

( _Xn_ + _Yn_ ) is not a submartingale w.r.t. any filtration.

9

**205A Homework #10** , due Tuesday 15 November.

**1.** Let _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ξi_,wherethe(</sup><sup>_ξi_)areindependent,</sup><sup>_Eξi_= 0andvar</sup><sup>_ξi<_</sup> _∞_ . Let _s_<sup>2</sup> _n_<sup>=�</sup><sup>_n_</sup> _i_ =1<sup>var</sup><sup>_ξi_.</sup> So we know that ( _Sn_<sup>2</sup><sup>_−s_2</sup> _n_<sup>)isamartingale.</sup> Suppose also that _|ξi| ≤ K_ for some constant _K_ . Show that


**2.** Let ( _Xn_ ) be a martingale with _X_ 0 = 0 and _EXn_<sup>2</sup><sup>_<∞_.Usingthefact</sup> that ( _Xn_ + _c_ )<sup>2</sup> is a submartingale, show that


**3.** Let ( _Xn_ ) and ( _Yn_ ) be martingales w.r.t. the same filtration with _E_ ( _Xn_<sup>2+</sup> _Yn_<sup>2)</sup><sup>_< ∞_.Showthat</sup>


**4.** Let ( _Xn, Fn_ ) _, n ≥_ 0 be a positive submartingale with _X_ 0 = 0. Let _Vn_ be random variables such that

(i) _Vn ∈Fn−_ 1 _, n ≥_ 1

(ii) _B ≥ V_ 1 _≥ V_ 2 _≥ . . . ≥_ 0, for some constant _B_ . Prove that for _λ >_ 0


**5.** Prove _Dubins’ inequality_ . If ( _Xn_ ) is a positive martingale then the number _U_ of upcrossings of [ _a, b_ ] satisfies


[if you follow sketch in Durrett then prove the quoted exercise]

10

**205A Homework #11** , due Tuesday 22 November.

In each question, there is some fixed filtration ( _Fn_ ) with respect to which martingales are defined.

**1.** Let ( _Xn_ ) be a submartingale such that sup _n Xn < ∞_ a.s. and _E_ sup _n_ ( _Xn− Xn−_ 1)<sup>+</sup> _< ∞_ . Show that _Xn_ converges a.s.

**2.** For a sequence ( _An_ ) of events, show that


**3.** Let ( _Xn_ ) be a martingale and write ∆ _n_ = _Xn − Xn−_ 1, Suppose that _bm ↑∞_ and<sup>�</sup><sup>_∞_</sup> _m_ =1<sup>_b_</sup> _m_<sup>_−_2</sup><sup>_E_∆2</sup> _m_<sup>_< ∞_.Provethat</sup><sup>_Xn/bn→_0a.s.</sup>

**4.** Let ( _Xn_ ) be a martingale with sup _n E|Xn| < ∞_ . Show that there is a representation _Xn_ = _Yn − Zn_ where ( _Yn_ ) and ( _Zn_ ) are non-negative martingales such that sup _n EYn < ∞_ and sup _n EZn < ∞_ .

**5.** Let ( _Xn_ ) be adapted to ( _Fn_ ) with 0 _≤ Xn ≤_ 1. Let _α, β >_ 0 with _α_ + _β_ = 1. Suppose _X_ 0 = _x_ 0 and

_P_ ( _Xn_ +1 = _α_ + _βXn|Fn_ ) = _Xn, P_ ( _Xn_ +1 = _βXn|Fn_ ) = 1 _− Xn._

Show that _Xn → X∞_ a.s., where _P_ ( _X∞_ = 1) = _x_ 0 and _P_ ( _X∞_ = 0) = 1 _−x_ 0. **6.** Suppose _Fn ↑F∞_ and _Yn → Y∞_ in _L_<sup>1</sup> . Show that _E_ ( _Yn|Fn_ ) _→ E_ ( _Y∞|F∞_ ) in _L_<sup>1</sup> .

**7.** Let _Sn_ be the total assets of an insurance company at the end of year _n_ . Suppose that in year _n_ the company receives premiums of _c_ and pays claims totaling _ξn_ , where _ξn_ are independent with Normal( _µ, σ_<sup>2</sup> ) distribution, where 0 _< µ < c_ . The company is ruined if its assets fall to 0 or below. Show

_P_ (ruin) _≤_ exp( _−_ 2( _c − µ_ ) _S_ 0 _/σ_<sup>2</sup> ) _._

11

---

[Up: contents](index.md)
