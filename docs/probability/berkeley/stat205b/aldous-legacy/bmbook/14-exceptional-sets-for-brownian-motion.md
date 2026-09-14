---
title: Exceptional sets for Brownian motion
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Exceptional sets for Brownian motion

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The techniques developed in this book so far give a fairly satisfactory picture of the behaviour of a Brownian motion at a typical time, like a fixed time or a stopping time. In this chapter we explore exceptional times, for example times where the path moves slower or faster than in the law of the iterated logarithm, or does not wind as in Spitzer’s law. Again Hausdorff dimension is the right tool to describe just how exceptional an exceptional behaviour is, but we shall see that another notion of dimension, the packing dimension, can provide additional insight.

### **1. The fast times of Brownian motion**

In a famous paper from 1974, Orey and Taylor raise the question, how often, on a Brownian path, the law of the iterated logarithm fails. To understand this, recall that, by Corollary 5.3 and the Markov property, for a linear Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ and for every _t ∈_ [0 _,_ 1], almost surely,


This contrasts sharply with the following result (note the absence of the iterated logarithm!). Theorem 10.1. _Almost surely, we have_


Remark 10.2. At the time _t ∈_ [0 _,_ 1] where the maximum in Theorem 10.1 is attained, the law of the iterated logarithm fails and it is therefore an _exceptional_ time. _⋄_

**Proof.** The upper bound follows from L´evy’s modulus of continuity, Theorem 1.14, as


Readers who have skipped the proof of Theorem 1.14 given in Chapter 1 will be able to infer the upper bound directly from Remark 10.5 below. It remains to show that there exists a time _t ∈_ [0 _,_ 1] such that


275

Recall from Proposition 1.13 that, almost surely, for every constant _c < √_ 2 and every _ε, δ >_ 0 there exists _t ∈_ [0 _, δ_ ] and 0 _< h < ε_ with


are almost surely dense in [0 _,_ 1]. By continuity of Brownian motion they are open, and clearly _M_ ( _c, ε_ ) _⊂ M_ ( _d, δ_ ) whenever _c > d_ and _ε < δ_ . Hence, by Baire’s (category) theorem, the intersection


is dense and hence nonempty almost surely.

To explore how often we come close to the exceptional behaviour described in Theorem 10.1 we introduce a spectrum of exceptional points. Given _a >_ 0 we call a time _t ∈_ [0 _,_ 1] an _a_ **-fast time** if


and _t ∈_ [0 _,_ 1] is a **fast time** if it is _a_ -fast for some _a >_ 0. By Theorem 10.1 fast times exist, in fact the proof even shows that the set of fast times is dense in [0 _,_ 1] and hence is infinite. Conversely it is immediate from the law of the iterated logarithm that the set has Lebesgue measure zero, recall Remark 1.28. The appropriate notion to measure the quantity of _a_ -fast times is, again, Hausdorff dimension.

Theorem 10.3 (Orey and Taylor 1974). _Suppose {B_ ( _t_ ): _t ≥_ 0 _} is a linear Brownian motion. Then, for every a ∈_ [0 _,_ 1] _, we have almost surely,_


The rest of this section is devoted to the proof of this result. We start with a proof of the _upper bound_ , which also shows that there are almost surely no _a_ -fast points for _a >_ 1.

So fix an arbitrary _a >_ 0. Let _ε >_ 0 and _η >_ 1, having in mind that we later let _η ↓_ 1 and _ε ↓_ 0. The basic idea is to cover the interval [0 _,_ 1) by a collection of intervals of the form [ _jη_<sup>_−k_</sup> _,_ ( _j_ + 1) _η_<sup>_−k_</sup> ) with _j_ = 0 _, . . . , ⌈η_<sup>_k_</sup> _−_ 1 _⌉_ and _k ≥_ 1. Any such interval of length _h_ := _η_<sup>_−k_</sup> is included in the covering if, for _h_<sup>_′_</sup> := _kη_<sup>_−k_</sup> ,


Let I _k_ = I _k_ ( _η, ε_ ) be the collection of intervals of length _η_<sup>_−k_</sup> chosen in this procedure.

276

Lemma 10.4. _Almost surely, for every ε >_ 0 _and δ >_ 0 _, there is an η >_ 1 _and m ∈_ N _such that the collection_ I = I( _ε, δ_ ) = � _I ∈_ I _k_ : _k ≥ m_ � _is a covering of the set of a-fast points consisting of intervals of diameter no bigger than δ._

**Proof.** We first note that by Theorem 1.12 there exists a constant _C >_ 0 such that, almost surely, there exists _ρ >_ 0 such that, for all _s, t ∈_ [0 _,_ 2] with _|s − t| ≤ ρ_ ,

(1.1)


Choose _η >_ 1 such that<sup>_√_</sup> _<u>η −</u>_ <u>1</u> _≤ aε/C_ . Let _M_ be the minimal integer with _Mη_<sup>_−M_</sup> _≤ ρ_ and _m ≥ M_ such that _mη_<sup>_−m_</sup> _< δ_ and _kη_<sup>_−k_</sup> _< ℓη_<sup>_−ℓ_</sup> for all _k > ℓ ≥ m_ . Now suppose that _t ∈_ [0 _,_ 1] is an _a_ -fast point. By definition there exists an 0 _< u < mη_<sup>_−m_</sup> such that


We pick the unique _k ≥ m_ such that _kη_<sup>_−k_</sup> _< u ≤_ ( _k −_ 1) _η_<sup>_−k_+1</sup> , and let _h_<sup>_′_</sup> = _kη_<sup>_−k_</sup> . By (1.1), we have


As 0 _≤ u − h_<sup>_′_</sup> _≤_ ( _η −_ 1) _kη_<sup>_−k_</sup> , and by our choice of _η_ , the subtracted term is smaller than _aε_ ~~�~~ 2 _h_<sup>_′_</sup> log(1 _/h_<sup>_′_</sup> ) for sufficiently large _m_ . Hence there exists _k ≥ m_ such that


Now let _j_ be such that _t ∈_ [ _jη_<sup>_−k_</sup> _,_ ( _j_ + 1) _η_<sup>_−k_</sup> ). As before let _h_ = _η_<sup>_−k_</sup> . Then, by the triangle inequality and using (1.1) twice, we have


using in the last step that, by choosing _m_ sufficiently large, the subtracted term can be made smaller than 2 _aε_ �2 _h_<sup>_′_</sup> log(1 _/h_<sup>_′_</sup> ).

**Proof of the upper bound in Theorem 10.3.** This involves only a first moment calculation. All there is to show is that, for any _γ >_ 1 _− a_<sup>2</sup> there exists _ε >_ 0 such that the random variable<sup>�</sup> _I∈_ I( _ε,δ_ )<sup>_|I|γ_isfinite,almostsurely.Forthisitsufficestoverifythatits</sup> expectation is finite. Note that


So it all boils down to an estimate of a single probability, which is very simple as it involves just one normal random variable, namely _B_ ( _jη_<sup>_−k_</sup> + _kη_<sup>_−k_</sup> ) _− B_ ( _jη_<sup>_−k_</sup> ). More precisely, for _X_

277

standard normal,


for all sufficiently large _k_ and all 0 _≤ j <_ 2<sup>_k_</sup> , using the estimate for normal random variables of Lemma II.3.1 in the penultimate step. Given _γ >_ 1 _− a_<sup>2</sup> we can finally find _ε >_ 0 such that _γ_ + _a_<sup>2</sup> (1 _−_ 4 _ε_ )<sup>3</sup> _>_ 1, so that


completing the proof of the upper bound in Theorem 10.3.

Remark 10.5. If _a >_ 1 one can choose _γ <_ 0 in the previous proof, which shows that there are no _a_ -fast times as the empty collection is suitable to cover the set of _a_ -fast times. _⋄_

For the _lower bound_ we have to work harder. We divide, for any positive integer _k_ , the interval [0 _,_ 1] into nonoverlapping dyadic subintervals [ _j_ 2<sup>_−k_</sup> _,_ ( _j_ + 1)2<sup>_−k_</sup> ] for _j_ = 0 _, . . . ,_ 2<sup>_k_</sup> _−_ 1. As before, we denote this collection of intervals by C _k_ and by C the union over all collections C _k_ for _k ≥_ 1. To each interval _I ∈_ C we associate a _{_ 0 _,_ 1 _}_ -valued random variable _Z_ ( _I_ ) and then define sets


Because 1 _A_ = lim sup 1 _A_ ( _k_ ) the set _A_ is often called the **limsup fractal** associated with the family ( _Z_ ( _I_ ): _I ∈_ C). We shall see below that the set of _a_ -fast points contains a large limsup fractal and derive the lower bound from the following general result on limsup fractals.

Proposition 10.6. _Suppose that_ ( _Z_ ( _I_ ): _I ∈_ C) _is a collection of random variables with values in {_ 0 _,_ 1 _} such that pk_ := P _{Z_ ( _I_ ) = 1 _} is the same for all I ∈_ C _k. For I ∈_ C _m, with m < n, define_


_Let ζ_ ( _n_ ) _≥_ 1 _and γ >_ 0 _be such that_


_then_ dim _A ≥ γ almost surely for the limsup fractal A associated with_ ( _Z_ ( _I_ ): _I ∈_ C) _._

278

The _idea of the proof_ of Proposition 10.6 is to construct a probability measure _µ_ on _A_ and then use the energy method. To this end, we choose an increasing sequence ( _ℓk_ : _k ∈_ N) such that _Mℓk_ ( _D_ ) _>_ 0 for all _D ∈_ C _ℓk−_ 1. We then define a (random) probability measure _µ_ in the following manner: Assign mass one to any interval _I ∈_ C _ℓ_ 0. Proceed inductively: if _J ∈_ C _m_ with _ℓk−_ 1 _< m ≤ ℓk_ and _J ⊂ D_ for _D ∈_ C _ℓk−_ 1 define


Then _µ_ is consistently defined on all intervals in C and therefore can be extended to a probability measure on [0 _,_ 1] by the measure extension theorem. The crucial part of the proof is then to show that, for a suitable choice of ( _ℓk_ : _k ∈_ N) the measure _µ_ has finite _γ_ -energy.

For the proof of Proposition 10.6 we need two lemmas. The first one is a simple combination of two facts, which have been established at other places in the book: The bounds for the energy of a measure established in Lemma 9.20, and the lower bound of Hausdorff dimension in terms of capacity which follows from the potential theoretic method, see Theorem 4.27.

Lemma 10.7. _Suppose B ⊂_ [0 _,_ 1] _is a Borel set and µ is a probability measure on B. Then_


**Proof.** By Lemma 9.20 with _f_ ( _x_ ) = _x_<sup>_α_</sup> and _h_ ( _n_ ) = 2<sup>_−nα_</sup> (1 _−_ 2<sup>_−α_</sup> ) we obtain, for a suitable constant _C >_ 0 that


If the right hand side is finite, then so is the _α_ -energy of the measure _µ_ . We thus obtain dim _B ≥ α_ by Theorem 4.27.

For the formulation of the second lemma we use (2) to pick, for any _ℓ ∈_ N an integer _n_ = _n_ ( _ℓ_ ) _≥ ℓ_ such that


Lemma 10.8. _There exists an almost surely finite random variable ℓ_ 0 _such that, for all ℓ ≥ ℓ_ 0 _and D ∈_ C _ℓ, with n_ = _n_ ( _ℓ_ ) _,_


279

Remark 10.9. The first statement in the lemma says intuitively that the variance of the random variables _Mn_ ( _D_ ) is small, i.e. they are always close to their mean. This is essentially what makes this proof work. _⋄_

**Proof of Lemma 10.8.** For _m ≤ n, J ∈_ C _m_ we denote ∆ _n_ ( _J_ ) := _Mn_ ( _J_ ) _−_ E _Mn_ ( _J_ ) and, for _ℓ ≤ n_ and _D ∈_ C _ℓ_ , set


By assumption (1) we have E�∆ _n_ ( _J_ )<sup>2�</sup> _≤ ζ_ ( _n_ ) _pn_ 2<sup>_n−m_</sup> and therefore, for all _D ∈_ C _ℓ_ ,


By our choice of _n_ = _n_ ( _ℓ_ ) we thus obtain

Since the right hand side is summable in _ℓ_ we conclude that the summands inside the last expectation converge to zero as _ℓ ↑∞_ . In particular, there exists _ℓ_ 0 _< ∞_ such that, for all _ℓ ≥ ℓ_ 0 we have 2<sup>_−ℓγ_</sup> _≤_ 1 _/_ 4 and, for _n_ = _n_ ( _ℓ_ ) and _D ∈_ C _ℓ_ ,


The first statement follows from this very easily: For any _ℓ ≥ ℓ_ 0 and _n_ = _n_ ( _ℓ_ ) we have (recalling the definition of Υ _n_ ( _D_ )),


In order to get the second statement we calculate,


Since _Mn_ ( _J_ )<sup>2</sup> = �E _Mn_ ( _J_ ) + ∆ _n_ ( _J_ )�2 _≤_ 2�E _Mn_ ( _J_ )�2 + 2�∆ _n_ ( _J_ )�2 _,_ adding the inequalities (1.4) and (1.5) and setting _C_ := 2 + 2 _/_ (1 _−_ 2<sup>_−_(1+</sup><sup>_γ_)</sup> ) proves the second statement.

280

We now define the sequence ( _ℓk_ : _k ∈_ N) by _ℓk_ +1 = _n_ ( _ℓk_ ) for all integers _k ≥_ 0. The first statement of Lemma 10.8 ensures that _µ_ is well defined by (1.3), and together with the second statement will enable us to check that _µ_ has finite _γ_ -energy.

**Proof of Proposition 10.6.** We can now use Lemma 10.8 to verify the condition of Lemma 10.7 and finish the proof of Proposition 10.6. Indeed, by definition of _µ_ ,


Recall that _qk_ +1 := E _Mℓk_ +1( _D_ ) = 2<sup>_ℓk_+1</sup><sup>_−ℓk_</sup> _pℓk_ +1 and, by the first statement of Lemma 10.8, for every _k ∈_ N and _D ∈_ C _ℓk_ ,

21<sup>_qk_+1</sup><sup>_≤Mℓk_+1(</sup><sup>_D_)</sup><sup>_≤_2</sup><sup>_qk_+1</sup><sup>_._</sup>

Now, from the definition of the measure _µ_ we get, with _D ⊂ D_<sup>_′_</sup> _∈_ C _k−_ 1,


and therefore we can continue (1.6) with the upper bound


using the second statement of Lemma 10.8 and the definition of _qk_ +1. Finally, using the definition of _Mℓk_ +1 and the definition of ( _ℓk_ : _k ∈_ N) we note that,


This ensures convergence of the sequence (1.6) and thus completes the proof.

Coming back to the lower bound in Theorem 10.3 we fix _ε >_ 0. Given _I_ = [ _jh,_ ( _j_ + 1) _h_ ] with _h_ := 2<sup>_−k_</sup> we let _Z_ ( _I_ ) = 1 if and only if


Lemma 10.10. _Almost surely, the set A associated with this family_ ( _Z_ ( _I_ ): _I ∈_ C) _of random variables is contained in the set of a-fast times._

**Proof.** Recall that by Theorem 1.12 there exists a constant _C >_ 0 such that, almost surely,


281

Now assume that _k_ is large enough that (<sup><u>2</u></sup> _aε_<sup>_<u>C</u>_</sup> �2 _k_ log 2+ _k_ log _k ≤ k_ 2 log 2. Let _t ∈ A_ and suppose that _t ∈ I ∈_ C _k_ with _Z_ ( _I_ ) = 1. Then, by the triangle equality,


As this happens for infinitely many _k_ , this proves that _t_ is an _a_ -fast point.

The next lemma singles out the crucial estimates of expectation and variance needed to apply Proposition 10.6. The first is based on the upper tail estimate for a standard normal distribution, the second on the ‘short range’ of the dependence of the family ( _Z_ ( _I_ ) : _I ∈_ C).

Lemma 10.11. _Define pn_ = E[ _Z_ ( _I_ )] _for I ∈_ C _n, and η_ ( _n_ ) := 2 _n_ + 1 _. Then,_


**Proof.** For part (a), denoting by _X_ a standard normal random variable,


for all sufficiently large _k_ and all 0 _≤ j <_ 2<sup>_k_</sup> , using the lower estimate for normal random variables of Lemma 3.1 in the penultimate step.

For part (b) note that for two intervals _J_ 1 _, J_ 2 _∈_ C _n_ the associated random variables _Z_ ( _J_ 1) and _Z_ ( _J_ 2) are independent if their distance is at least than _n_ 2<sup>_−n_</sup> . Using this whenever possible and the trivial estimate E[ _Z_ ( _J_ 1) _Z_ ( _J_ 2)] _≤_ E _Z_ ( _J_ 1) otherwise, we get


Hence we obtain


which settles the lemma.

**Proof of the lower bound in Theorem 10.3.** By Lemma 10.11 the conditions of Proposition 10.6 hold for any _γ <_ 1 _− a_<sup>2</sup> (1 + _ε_ )<sup>3</sup> . As, for any _ε >_ 0, the set _A_ associated to ( _Z_ ( _I_ ): _I ∈_ C) is contained in the set of _a_ -fast times, the latter has at least dimension 1 _− a_<sup>2</sup> .

282

### **2. Packing dimension and limsup fractals**

In this section we ask for a precise criterion, whether a set _E_ contains _a_ -fast times for various values of _a_ . It turns out that such a criterion depends not on the Hausdorff, but on the packing dimension of the set _E_ . We therefore begin by introducing the concept of _packing dimension_ , which was briefly mentioned in the beginning of Chapter 4, in some detail.

We choose to define packing dimension in a way, which indicates its nature as a concept, which is a natural _dual_ to the notion of Hausdorff dimension. The natural _dual_ operation to covering a set with balls, as we have done in the case of Hausdorff dimension, is the operation of _packing_ balls into the set.

Definition 10.12. _Suppose E is a metric space. For every δ >_ 0 _, a δ_ **-packing** _of A ⊂ E is a countable collection of_ disjoint _balls_


_with centres xi ∈ A and radii_ 0 _≤ ri ≤ δ. For every s ≥_ 0 _we introduce the_ **s-value** _of the packing as_<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_r_</sup> _i_<sup>_s.The_</sup><sup>**s-packingnumber**</sup><sup>_ofAisdefinedas_</sup>


Note that the packing number is defined in the same way as the Hausdorff measure with efficient (small) coverings replaced by efficient (large) packings. A difference is that the packing numbers do _not_ define a reasonable measure. However a small modification gives the so-called packing measure,


The packing dimension has a definition analogous to the definition of Hausdorff dimension with Hausdorff measures replaced by packing measures.

Definition 10.13.

_⋄ The_ **packing dimension** _of E is_ dim _P E_ = inf _{s_ : _P_<sup>_s_</sup> ( _E_ ) = 0 _}._

Remark 10.14. It is not hard to see that

dim _P E_ = inf _{s_ : _P_<sup>_s_</sup> ( _E_ ) _< ∞}_ = sup _{s_ : _P_<sup>_s_</sup> ( _E_ ) _>_ 0 _}_ = sup _{s_ : _P_<sup>_s_</sup> ( _E_ ) = _∞},_ a proof of this fact is suggested as Exercise 10.1.


An alternative approach to packing dimension is to use a suitable _regularisation_ of the upper Minkowski dimension, recall Remark 4.4.4 where we have hinted at this possibility.

Theorem 10.15. _For every metric space E we have_


283

Remark 10.16. We have, for all bounded sets _E_ , that dim _P E ≤_ dim _M E_ and, of course, strict inequality may hold. Obviously, every countable set has packing dimension 0, compare with the example in Exercise 4.2. For this definition it is not hard to see that the countable stability property is satisfied. _⋄_

**Proof.** Define, for every _A ⊂ E_ and _ε >_ 0,

_. P_ ( _A, ε_ ) = max � _k_ : there are disjoint balls _B_ ( _x_ 1 _, ε_ ) _, . . . , B_ ( _xk, ε_ ) with _xi ∈ A_ � Recall the definition of the numbers _M_ ( _A, ε_ ) from (1.1) in Chapter 4. We first show that


Indeed, if _k_ = _P_ ( _A, ε_ ) let _B_ ( _x_ 1 _, ε_ ) _, . . . , B_ ( _xk, ε_ ) be disjoint balls with _xi ∈ A_ . Suppose _x ∈ A \_<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_B_(</sup><sup>_xi,_2</sup><sup>_ε_),then</sup><sup>_B_(</sup><sup>_x, ε_)isdisjointfromallballs</sup><sup>_B_(</sup><sup>_xi, ε_)contradictingthechoiceof</sup><sup>_k_.</sup> Hence _B_ ( _x_ 1 _,_ 2 _ε_ ) _, . . . , B_ ( _xk,_ 2 _ε_ ) is a covering of _A_ and we have shown _M_ ( _A,_ 2 _ε_ ) _≤ P_ ( _A, ε_ ). For the other inequality let _m_ = _M_ ( _A,_ 2 _ε_ ) and _k_ = _P_ ( _A,_ 4 _ε_ ) and choose _x_ 1 _, . . . , xm ∈ A_ and _y_ 1 _, . . . , yk ∈ A_ such that


Then each _yj_ belongs to some _B_ ( _xi,_ 2 _ε_ ) and no such ball contains more than one such point. Thus _k ≤ m_ , which proves _P_ ( _A,_ 4 _ε_ ) _≤ M_ ( _A,_ 2 _ε_ ).

Suppose now that inf _{t_ : _P_<sup>_t_</sup> ( _E_ ) = 0 _} < s_ . Then there is _t < s_ and _E_ =<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_Ai_suchthat,for</sup> every set _A_ = _Ai_ , we have _P_<sup>_t_</sup> ( _A_ ) _<_ 1. Obviously, _Pε_<sup>_t_(</sup><sup>_A_)</sup><sup>_≥P_(</sup><sup>_A, ε_)</sup><sup>_εt_.Letting</sup><sup>_ε ↓_0gives</sup>


Hence dim _M A ≤ t_ and by definition sup<sup>_∞_</sup> _i_ =1 dim _M Ai ≤ t < s_ . To prove the opposite inequality, let


and _Ai ⊂ E_ bounded with _E_ =<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_Ai_.Itsufficestoshowthat</sup> dim _M_ ( _Ai_ ) _≥ t_ for some _i_ . Since _P_<sup>_s_</sup> ( _E_ ) _>_ 0 there is _i_ such that _P_<sup>_s_</sup> ( _Ai_ ) _>_ 0. Let 0 _< α < P_<sup>_s_</sup> ( _Ai_ ), then for all _δ ∈_ (0 _,_ 1) we have _Pδ_<sup>_s_(</sup><sup>_Ai_)</sup><sup>_> α_andthereexistdisjointballs</sup><sup>_B_(</sup><sup>_x_1</sup><sup>_, r_1)</sup><sup>_, B_(</sup><sup>_x_2</sup><sup>_, r_2)</sup><sup>_, B_(</sup><sup>_x_3</sup><sup>_, r_3)</sup><sup>_, . . ._withcentres</sup> _xj ∈ Ai_ and radii _rj_ smaller than _δ_ with


For every _m_ let _km_ be the number of balls with radius 2<sup>_−m−_1</sup> _< rj ≤_ 2<sup>_−m_</sup> . Then,


284

This yields, for some integer _N ≥_ 0, 2<sup>_Nt_</sup> (1 _−_ 2<sup>_t−s_</sup> ) _α ≤ kN ,_ since otherwise


Since _rj ≤ δ_ for all _j_ , we have 2<sup>_−N−_1</sup> _< δ_ . Moreover,


which gives


Letting _δ ↓_ 0, and recalling the relation of _M_ ( _A, ε_ ) and _P_ ( _A, ε_ ) established at the beginning of the proof, we obtain


and thus dim _M Ai ≥ t_ , as required.

Remark 10.17. It is easy to see that, for every metric space, dim _P E ≥_ dim _E_ . This is suggested as Exercise 10.2. _⋄_

The following result shows that every closed subset of R<sup>_d_</sup> has a large subset, which is ‘regular’ in a suitable sense. It will be used in the proof of Theorem 10.28 below.

Lemma 10.18. _Let A ⊂_ R<sup>_d_</sup> _be closed._

- (i) _If any open set V which intersects A satisfies_ dim _M_ ( _A ∩ V_ ) _≥ α , then_ dimP( _A_ ) _≥ α._

- (ii) _If_ dim _P_ ( _A_ ) _> α, then there is a (relatively closed) nonempty subset A_<sup>�</sup> _of A, such that, for any open set V which intersects A_<sup>�</sup> _, we have_ dim _P_ ( _A_<sup>�</sup> _∩ V_ ) _> α._

**Proof.** Let _A ⊂_<sup>�</sup><sup>_∞_</sup> _j_ =1<sup>_Aj_,wherethe</sup><sup>_Aj_areclosed.Wearegoingtoshowthatthereexist</sup> an open set _V_ and an index _j_ such that _V ∩ A ⊂ Aj_ . For this _V_ and _j_ we have,


This in turn implies that dim _P_ ( _A_ ) _≥ α_ .

Suppose now that for any _V_ open such that _V ∩ A̸_ = _∅_ , it holds that _V ∩ A̸ ⊂ Aj_ . Then _A_<sup>_c_</sup> _j_ is a dense open set relative to _A_ . By Baire’s (category) theorem _A ∩_<sup>�</sup> _j_<sup>_Ac_</sup> _j̸_<sup>=</sup><sup>_∅_,whichmeans</sup> that _A̸ ⊂_<sup>�</sup> _j_<sup>_Aj_,contradictingourassumptionandproving(i).</sup>

Now choose a countable basis _B_ of the topology of R<sup>_d_</sup> and define


Then, dim _P_ ( _A \ A_<sup>�</sup> ) _≤ α_ using dim _P ≤_ dim _M_ and countable stability of packing dimension. From this we conclude that

dim _P A_<sup>�</sup> = dim _P A > α._

285

If for some _V_ open, _V ∩ A_<sup>�</sup> _̸_ = _∅_ and dim _P_ ( _A_<sup>�</sup> _∩ V_ ) _≤ α_ then _V_ contains some set _B ∈B_ such that _A_<sup>�</sup> _∩ B̸_ = _∅_ . For that set we have dim _P_ ( _A ∩ B_ ) _≤_ dim _P_ ( _A \ A_<sup>�</sup> ) _∧_ dim _P_ ( _A_<sup>�</sup> _∩ B_ )) _≤ α,_ contradicting the construction of _A_<sup>�</sup> .

Example 10.19. As an example of a result demonstrating the duality between Hausdorff and packing dimension is the _product formula_ , see [ **BP96** ]. In the dimension theory of smooth sets (manifolds, linear spaces) we have the following formula for product sets


The example discussed in Exercise 2.3 shows that this formula fails for Hausdorff dimension, a reasonable formula for the Hausdorff dimension of product sets necessarily involves information about the packing dimension of one of the factor sets. In [ **BP96** ] it is shown that, for every Borel set _A ⊂_ R<sup>_d_</sup> ,


where the supremum is over all compact sets _B ⊂_ R<sup>_d_</sup> . One can also show that, if _A_ satisfies _⋄_ dim _A_ = dim _P A_ , then the product formula dim( _A × B_ ) = dim _A_ + dim _B_ holds.

Before moving back to our study of Brownian paths we study the packing dimension of the ‘test sets’ we have used in the stochastic codimension method, see Section 9.1.

Theorem 10.20. _Let γ ∈_ [0 _, d_ ] _and_ Γ[ _γ_ ] _be a percolation limit set in_ R<sup>_d_</sup> _with retention parameter_ 2<sup>_−γ_</sup> _. Then_

- dim _P_ Γ[ _γ_ ] _≤ d − γ almost surely,_


**Proof.** For the first item, as packing dimension is bounded from above by the upper Minkowski dimension, it suffices to show that <u>dim</u> ~~M~~<sup>Γ[</sup><sup>_γ_]</sup><sup>_≤d−γ_almostsurely.</sup> For this purpose we use the formula for the upper Minkowski dimension given in Remark 4.2. For a given _n_ , we cover the percolation limit set by S _n_ , the collection of cubes retained in the _n_ th construction step. The probability that a given cube of sidelength 2<sup>_−n_</sup> is in S _n_ is 2<sup>_−nγ_</sup> and hence the expected number of cubes in S _n_ is 2<sup>_n_(</sup><sup>_d−γ_)</sup> . Hence, for any _ε >_ 0, P�2<sup>_n_(</sup><sup>_γ−d−ε_)</sup> #S _n >_ 1� _≤_ 2<sup>_n_(</sup><sup>_γ−d−ε_)</sup> E#S _n ≤_ 2<sup>_−nε_</sup> _,_

which is summable. Hence, almost surely, 2<sup>_n_(</sup><sup>_γ−d−ε_)</sup> #S _n ≤_ 1 for all but finitely many _n_ . Thus, almost surely,


For the second item recall the corresponding statement for Hausdorff dimension from Exercise 9.3. The result follows, as packing dimension is bounded from below by the Hausdorff dimension, see Remark 10.17.

286

Remark 10.21. At a first glance the concept of packing dimension does not seem to add substantial news to the discussion of fine properties of _d_ -dimensional Brownian motion. However, a first sign that something interesting might be going on can be found in Exercise 10.5, where we show that the Hausdorff and packing dimension of the sets of _a_ -fast points differ. This is indicative of the fact that optimal coverings of these sets uses coverings sets of widely differing size, and that optimal packings use sets of quite different scale. _⋄_

Given a set _E ⊂_ [0 _,_ 1] we now ask for the maximal value of _a_ such that _E_ contains an _a_ -fast time with positive probability. This notion of size is most intimately linked to packing dimension as the following theorem shows. We denote by _F_ ( _a_ ) _⊂_ [0 _,_ 1] the set of _a_ -fast times.

Theorem 10.22 (Khoshnevisan, Peres and Xiao). _For any compact set E ⊂_ [0 _,_ 1] _, almost surely,_


_Moreover, if dimP_ ( _E_ ) _> a_<sup>2</sup> _, then dimP_ ( _F_ ( _a_ ) _∩ E_ ) = dim _P_ ( _E_ ) _._

Remark 10.23. The result can be extended from compact sets _E_ to more general classes of _⋄_ sets, more precisely the _analytic_ sets, see [ **KPX00** ].

Remark 10.24. An equivalent formulation of the theorem is that, for any compact _E ⊂_ [0 _,_ 1], almost surely,


Using the compact percolation limit sets _E_ = Γ[ _γ_ ] in this result and Hawkes’ theorem, Theorem 9.5, one can obtain an alternative proof of the Orey-Taylor theorem. Indeed, by Theorem 10.20, if _γ <_ 1 _− a_<sup>2</sup> we have dim _P_ ( _E_ ) _> a_<sup>2</sup> with positive probability, and therefore, P� _F_ ( _a_ ) _∩ E̸_ = _∅_ � _>_ 0. Hence, by Hawkes’ theorem, dim _F_ ( _a_ ) _≥_ 1 _− a_<sup>2</sup> with positive probability. Brownian scaling maps _a_ -fast points onto _a_ -fast points. Therefore there exists _ε >_ 0 such that, for any _n ∈_ N and 0 _≤ j ≤ n −_ 1,


and hence

P� dim _F_ ( _a_ ) _≥_ 1 _− a_<sup>2�</sup> _≥_ 1 _−_ (1 _− ε_ )<sup>_n_</sup> _→_ 1 _._ Conversely, by Theorem 10.20, if _γ >_ 1 _−a_<sup>2</sup> we have dim _P_ ( _E_ ) _< a_<sup>2</sup> almost surely, and therefore, P� _F_ ( _a_ ) _∩ E̸_ = _∅_ � = 0. Hence, by Hawkes’ theorem, Theorem 9.5, we have dim _F_ ( _a_ ) _≤_ 1 _− a_<sup>2</sup> almost surely. _⋄_

Theorem 10.22 can be seen as a probabilistic interpretation of packing dimension. The upper and lower Minkowski dimensions allow a similar definition when the order of sup and lim are interchanged.

287

Theorem 10.25. _For any compact E ⊂_ [0 _,_ 1] _almost surely,_


**Proof of the upper bounds in Theorem 10.22 and Theorem 10.25.** Suppose _E ⊂_ [0 _,_ 1] is compact. We assume that dim _M_ ( _E_ ) _< λ_ for some _λ < a_<sup>2</sup> and show that


Note that this is the upper bound in Theorem 10.25. Once this is shown it immediately implies


Now, for any decomposition _E_ =<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_Ei_,wehave</sup>


where we have made use of the fact that the upper Minkowski dimension is insensitive under taking the closure of a set. Theorem 10.15 now implies that


which is the upper bound in Theorem 10.22.

For the proof of (2.2) cover _E_ by disjoint subintervals _I_ = [( _j/k_ ) _η_<sup>_−k_</sup> _,_ (( _j_ + 1) _/k_ ) _η_<sup>_−k_</sup> ) for _j_ = 0 _, . . . , ⌈kη_<sup>_k_</sup> _−_ 1 _⌉_ , of equal length _h_ = _η_<sup>_−k_</sup> _/k_ such that _I ∩ E̸_ = _∅_ . By definition of the upper Minkowski dimension there exists an _m_ such that, for all _k ≥ m_ , no more than _η_<sup>_λk_</sup> different such intervals of length _h_ = _η_<sup>_−k_</sup> _/k_ intersect _E_ .

Now fix _ε >_ 0 such that _λ <_<sup>_<u>a</u>_</sup> 2<sup>2(1</sup><sup>_−ε_)3,whichispossiblebyourconditionon</sup><sup>_λ_.Let</sup><sup>_Z_(</sup><sup>_I_) = 1</sup> if , for _h_<sup>_′_</sup> = _η_<sup>_−k_</sup> ,


Recall from the proof of Lemma 10.4 that there is an _η >_ 1 such that, for any _m ∈_ N, the collection


is a covering of the set

Moreover, we recall from (1.2), that


288

and, sticking to our notation _I_ = [( _j/k_ ) _η_<sup>_−k_</sup> _,_ (( _j_ + 1) _/k_ ) _η_<sup>_−k_</sup> ) for a little while longer,


and hence by the Borel-Cantelli lemma there exists an _m_ such that _Z_ ( _I_ ) = 0 whenever _I_ = [( _j/k_ ) _η_<sup>_−k_</sup> _,_ (( _j_ + 1) _/k_ ) _η_<sup>_−k_</sup> ) for some _k ≥ m_ . This means that the set _M_ ( _m_ ) can be covered by the empty covering, so it must itself be empty. This shows (2.2) and completes the proof.

We are going to embed the proof of the lower bound now into a more general framework, including the discussion of limsup fractals in a _d_ -dimensional cube.

Definition 10.26. _Fix an open unit cube_ Cube = _x_ 0 + (0 _,_ 1)<sup>_d_</sup> _⊂_ R<sup>_d_</sup> _. For any nonnegative integer k, denote by_ C _k the collection of dyadic cubes_


_and_ C =<sup>�</sup> _k≥_ 0<sup>C</sup><sup>_k.Denoteby_(</sup><sup>_Z_(</sup><sup>_I_):</sup><sup>_I∈_C)</sup><sup>_acollectionofrandomvariableseachtakingvalues_</sup> _in {_ 0 _,_ 1 _}. The_ **limsup fractal** _associated to this collection is the random set_


_where_ int( _I_ ) _is the interior of the cube I._


Remark 10.27. Compared with the setup of the previous section we have switched to the use of _open_ cubes in the definition of limsup fractals. This choice is more convenient when we prove hitting estimates, whereas in Proposition 10.6 the choice of closed cubes was more convenient when constructing random measures on _A_ . _⋄_

_⋄_

The key to our result are the hitting probabilities for the discrete limsup fractal _A_ under some conditions on the random variables ( _Z_ ( _I_ ): _I ∈_ C).

Theorem 10.28. _Suppose that_

(i) _the means pn_ = E[ _Z_ ( _I_ )] _are independent of the choice of I ∈_ C _n and satisfy_


- (ii) _there exists c >_ 0 _such that the random variables Z_ ( _I_ ) _and Z_ ( _J_ ) _are independent whenever I, J ∈_ C _n and the distance of I and J exceeds cn_ 2<sup>_n_</sup> _._

_Then, for any compact E ⊂_ Cube _with_ dim _P_ ( _E_ ) _> γ, we have_


289

Remark 10.29. The second assumption, which gives us the necessary independence for the lower bound, can be weakened, see [ **KPX00** ]. Note that no assumption is made concerning _⋄_ the dependence of random variables _Z_ ( _I_ ) for intervals _I_ of different size.

**Proof of Theorem 10.28** Let _E ⊂_ Cube be compact with dim _P E > γ_ . Let _E_<sup>�</sup> be defined as in Lemma 10.18 for example as


From the proof of Lemma 10.18 we have dim _P E_ = dim _P E_<sup>�</sup> . Define open sets


and


By definition _A_<sup>_∗_</sup> _n_<sup>_∩E_�isopenin</sup><sup>_E_�.Wewillshowthatitisalsodensein</sup><sup>_E_�withprobability</sup> one. This, by Baire’s category theorem, will imply that


as required. To show that _A_<sup>_∗_</sup> _n_<sup>_∩E_�isdensein</sup><sup>_E_�,weneedtoshowthatforanyopenbinary</sup> cube _J_ which intersects _E_<sup>�</sup> , the set _A_<sup>_∗_</sup> _n_<sup>_∩E_�</sup><sup>_∩J_isalmostsurelynon-empty.</sup>

For the rest of the proof, take _ε >_ 0 small and _n_ large enough so that _E_<sup>�</sup> _∩ J_ intersects more than 2<sup>_n_(</sup><sup>_γ_+2</sup><sup>_ε_)</sup> binary cubes of sidelength 2<sup>_−n_</sup> , and so that (log _pn_ ) _/n > −_ (log 2)( _γ_ + _ε_ ). Let _Sn_ be the set of cubes in C _n_ that intersect _E_<sup>�</sup> . Define


so that P� _An ∩ E_<sup>�</sup> _∩ J_ = _∅_ � = P _{Tn_ = 0 _}._ To show that this probability converges to zero, by the Paley-Zygmund inequality, it suffices to prove that (Var _Tn_ ) _/_ (E _Tn_ )<sup>2</sup> does. The first moment of _Tn_ is given by


where _sn_ denotes the cardinality of _Sn_ . The variance can be written as


Here each summand is at most _pn_ , and the summands for which _I_ and _J_ have distance at least _cn_ 2<sup>_−n_</sup> vanish by assumption. Thus


290

This implies that (Var _Tn_ ) _/_ (E _Tn_ )<sup>2</sup> _→_ 0. Hence, almost surely, _A_<sup>_∗_</sup> _n_<sup>isanopendenseset,</sup> concluding the proof.

We now show how the main statement of Theorem 10.22 follows from this, and how the ideas in the proof also lead to the lower bound in Theorem 10.25.

**Proof the lower bound in Theorem 10.22 and Theorem 10.25.** For the lower bound we look at a compact set _E ⊂_ (0 _,_ 1) with dim _P_ ( _E_ ) _> a_<sup>2</sup> _/_ 2 and first go for the result in Theorem 10.22. Choose _ε >_ 0 such that dim _P_ ( _E_ ) _>_<sup>_<u>a</u>_</sup> 2<sup>2(1 +</sup><sup>_ε_)3.Associatetoeverydyadic</sup> interval _I_ = [ _jh,_ ( _j_ + 1) _h_ ] _∈_ C _k_ with _h_ = 2<sup>_−k_</sup> the random variable _Z_ ( _I_ ), which takes the value one if and only if, for _h_<sup>_′_</sup> = _k_ 2<sup>_−k_</sup> ,


and note that by Lemma 10.10 the limsup fractal associated to these random variables is contained in the set of _a_ -fast times. It remains to note that the collection _{Z_ ( _I_ ) : _I ∈_ C _k , k ≥_ 0 _}_ satisfies the condition (i) with _γ_ = _<u>a</u>_ 2<sup>2(1+</sup><sup>_ε_)3by(1.7)andcondition(ii)with</sup><sup>_c_=1.</sup> Theorem 10.28 now gives that


### and therefore


For the lower bound in Theorem 10.25 we look at a compact set _E ⊂_ (0 _,_ 1) with dim _M_ ( _E_ ) _> a_<sup>2</sup> _/_ 2 and fix _ε >_ 0 such that dim _M_ ( _E_ ) (1 _− ε_ )<sup>2</sup> _≥_<sup>_<u>a</u>_</sup> 2<sup>2.Hencethereexistsasequence(</sup><sup>_nk_:</sup><sup>_k∈_N)</sup> such that


With _Z_ ( _I_ ) defined as above we obtain, using notation and proof of Theorem 10.28, that


and


By Chebyshev’s inequality we get, for 1 _/_ 2 _< η <_ 1,

P� _|Tnk −_ E _Tnk| ≥_ (E _Tnk_ )<sup>_η_�</sup> _≤_ (2 _nk_ + 1) (E _Tnk_ )<sup>1</sup><sup>_−_2</sup><sup>_η_</sup> _._

As E _Tn_ is exponentially increasing we can infer, using the Borel-Cantelli lemma, that


This implies that _Tnk̸_ = 0 for all sufficiently large _k_ . Hence, as _Z_ <u>(</u> _I_ <u>) = 1</u> and _I ∩ E̸_ = _∅_ imply that there exists _t ∈ I ∩ E_ with with _|B_ ( _t_ + _h_<sup>_′_</sup> ) _− B_ ( _t_ ) _| ≥ a_ ~~�~~ _h_<sup>_′_</sup> log(1 _/h_<sup>_′_</sup> ) for _h_<sup>_′_</sup> = _nk_ 2<sup>_nk_</sup> _,_ by the proof of Lemma 10.10, we have completed the proof of Theorem 10.25.

291

### **3. Slow times of Brownian motion**

At the fast times Brownian motion has, in infinitely many small scales, an unusually large growth. Conversely, one may ask whether there are times where a Brownian path has, at _all_ small scales, unusually small growth.

This question of _slow times_ for the Brownian motion is related to nondifferentiability of the Brownian path. Indeed, in our proof of non-differentiability, we showed that almost surely,


and in 1963 Dvoretzky showed that there exists a constant _δ >_ 0 such that almost surely,


In 1983 Davis and, independently, Perkins and Greenwood, found that the optimal constant in this result is equal to one.

Theorem 10.30 (Davis, Perkins and Greenwood). _Almost surely,_


Remark 10.31. We call a time _t ∈_ [0 _,_ 1] an _a_ **-slow time** if


The result shows that _a_ -slow times exist for _a >_ 1 but not for _a <_ 1. The Hausdorff dimension _⋄_ of the set of _a_ -slow times is studied in Perkins [ **Pe83** ].

_⋄_

For the proof of Theorem 10.30 we need to investigate the probability that the graph of a Brownian motion stays within a parabola open to the right. The following lemma is what we need for an upper bound.

Lemma 10.32. _Let M_ := max0 _≤t≤_ 1 _|B_ ( _t_ ) _| and, for r <_ 1 _, define the stopping time_


_Then_ E _T < ∞._

**Proof.** By Theorem 2.44, for every _t ≥_ 1, we have


where H¨older’s inequality was used in the last step. This gives


292

and as E[ _M_<sup>2</sup> ] _< ∞_ we get that E[ _T ∧ t_ ] is bounded and hence E _T < ∞_ .


is empty almost surely. The crucial input is that, for any interval _I_ = [ _a, b_ ] _⊂_ [0 _,_ 1], we have by the triangle inequality and Brownian scaling, for _M_ = max _{|B_ ( _t_ ) _|_ : 0 _≤ t ≤ b − a}_ ,


Now, dividing [0 _,_ 1] into _n_ intervals of length 1 _/n_ we get


We turn to the proof of the upper bound. Again we start by studying exit times from a parabola. For 0 _< r < ∞_ and _a >_ 0 let


For the moment it suffices to note the following property of _T_ (1 _, a_ ).

Lemma 10.33. _We have_ E _T_ (1 _, a_ ) = _∞._

**Proof.** Suppose that E _T_ (1 _, a_ ) _< ∞_ . Then, by Theorem 2.44, we have that E _T_ (1 _, a_ ) = E _B_ ( _T_ (1 _, a_ ))<sup>2</sup> = E _T_ (1 _, a_ ) + _a,_ which is a contradiction. Hence E _T_ (1 _, a_ ) = _∞_ .

For 0 _< r < ∞_ and _a >_ 0 we now define further stopping times


Lemma 10.34. _If r >_ 1 _there is a p_ = _p_ ( _r_ ) _<_ 1 _such that_ E[ _S_ ( _r,_ 1)<sup>_p_</sup> ] = _∞. In particular,_


The proof uses the following general lemma.

Lemma 10.35. _Suppose X is a nonnegative random variable and_ E _X_<sup>_p_</sup> = _∞ for some p <_ 1 _. Then_


and hence, for all _N_ ,


This implies that E[ _X_<sup>_p_</sup> ] = sup E[( _X ∧ N_ )<sup>_p_</sup> ] _< ∞_ , and so the statement follows.

**Proof of Lemma 10.34.** Define a sequence of stopping times by _τ_ 0 = 1 and, for _k ≥_ 1,


By the strong Markov property and Brownian scaling we get, for any _λ >_ 0,


Define, with P1 referring to a Brownian motion started in _B_ (0) = 1,


To pass from this estimate to the _p_<sup>th</sup> moments we use that, for any nonnegative random variable _X_ , we have E _X_<sup>_p_</sup> = �0 _∞_<sup>P</sup><sup>_{Xp>λ} dλ_.</sup> This is an easy consequence of Fubini’s theorem and gives


294

Now, using the formula for E _X_<sup>_p_</sup> again, but for _X_ = _T_ (1 _,_ 1) and noting that _{τ_ 2 _k−_ 2 _< S_ ( _r,_ 1) _}_ = _{τ_ 2 _k−_ 3 _< τ_ 2 _k−_ 2 _}_ , we obtain


and by iterating this,


Note that, by Fatou’s lemma and by Lemma 10.33,


Hence we may pick _p <_ 1 such that E[ _T_ (1 _,_ 1)<sup>_p_</sup> ] _>_ 1 _/c_ . Then


as _k ↑∞_ , which is the first statement we wanted to prove. The second statement follows directly from the general fact stated as Lemma 10.35.


Note that _n ≥ m_ implies _A_ ( _n_ ) _⊂ A_ ( _m_ ). We show that


For _n ∈_ N and let _v_ (0 _, n_ ) = 0 and, for _i ≥_ 1,


_∧_ inf � _t ≥ v_ ( _i −_ 1 _, n_ ) + _n_<sup><u>1</u>:</sup><sup>_|B_(</sup><sup>_t_)</sup><sup>_−B_(</sup><sup>_v_(</sup><sup>_i −_1</sup><sup>_, n_))</sup><sup>_| ≥r_</sup> ~~�~~ _t − v_ ( _i −_ 1 _, n_ ) ~~�~~ _._ Then P _{v_ ( _i_ + 1 _, n_ ) _− v_ ( _i, n_ ) = 1 _| F_ ( _v_ ( _i, n_ )) _}_ = P _{S_ ( _r,_ 1) _≥ n}_ , and by Brownian scaling, (3.3) E[ _v_ ( _i_ + 1 _, n_ ) _− v_ ( _i, n_ ) _| F_ ( _v_ ( _i, n_ ))] = _n_<sup><u>1</u>E[</sup><sup>_S_(</sup><sup>_r,_1)</sup><sup>_∧n_]</sup><sup>_._</sup> Of course _v_ ( _k, n_ ) _≥_ 1 if _v_ ( _i, n_ ) _− v_ ( _i −_ 1 _, n_ ) = 1 for some _i ≤ k_ . Thus, for any _m_ , P _{v_ ( _i_ + 1 _, n_ ) _− v_ ( _i, n_ ) = 1 for some _i ≤ m_ such that _v_ ( _i, n_ ) _≤_ 1�


Let ( _nk_ : _k ∈_ N) be an increasing sequence of integers such that


and E[ _S_ ( _r,_ 1) _∧ nk_ ] _≤ nk/_ 6 for all _k_ , which is possible by Lemma 10.34.

295

Choose the integers _mk_ so that they satisfy


Summing (3.3) over all _i_ = 1 _, . . . , mk −_ 1,


hence P _{v_ ( _mk, nk_ ) _≥_ 1 _} ≤_ 1 _/_ 2. Now we get, putting all our ingredients together,

This proves (3.2). It remains to observe that, by Brownian scaling, there exists _δ >_ 0 such that, for all _n ∈_ N,


Hence, by independence,


This completes the proof of the lower bound, and hence completes the proof of Theorem 10.30.

### **4. Cone points of planar Brownian motion**

We now focus on a planar Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ . Recall from Section 7.2 that around a _typical point_ on the path this motion performs an infinite number of windings in both directions. It is easy to see that there are exceptional points for this behaviour: Let


Then Brownian motion does not perform _any_ windings around ( _x,_ 0), as this would necessarily imply that it crosses the half-line _{_ ( _y,_ 0): _y < x}_ contradicting the minimality of _x_ . More generally, each point ( _x, y_ ) _∈_ R<sup>2</sup> with _x_ = min _{x_ : ( _x, y_ ) _∈ B_ [0 _,_ 1] _}_ has this property, if the set is nonempty. Hence, the set of such points has dimension at least one, as the projection onto the _y_ -axis gives a nontrivial interval. We shall see below that this set has indeed Hausdorff dimension one.

We now look at points where a cone-shaped area with the tip of the cone placed in the point is avoided by the Brownian motion. These points are called cone points.

Definition 10.36. _Let {B_ ( _t_ ) : _t ≥_ 0 _} be a planar Brownian motion. For any angle α ∈_ (0 _,_ 2 _π_ ) _and direction ξ ∈_ [0 _,_ 2 _π_ ) _, define the closed_ **cone**


296

_Given a cone x_ + _W_ [ _α, ξ_ ] _we call its_ **dual** _the reflection of its complement about the tip, i.e. the cone x_ + _W_ [2 _π − α, ξ_ + _π_ ] _. A point x_ = _B_ ( _t_ ) _,_ 0 _< t <_ 1 _, is an α_ **-cone point** _if there exists ε >_ 0 _and ξ ∈_ [0 _,_ 2 _π_ ) _such that_


Remark 10.37. Clearly, if _x_ = _B_ ( _t_ ) is a cone point, then there exists a small _δ >_ 0 such that _B_ ( _t − δ, t_ + _δ_ ) _⊂ x_ + _W_ [ _α, ξ_ ]. Hence the path _{B_ ( _t_ ): 0 _≤ t ≤_ 1 _}_ performs only a finite number of windings around _x_ . _⋄_

We now identify the angles _α_ for which there exist _α_ -cone points, and, if they exist, determine the Hausdorff dimension of the set of _α_ -cone points.

Theorem 10.38 (Evans 1985). _Let {B_ ( _t_ ): 0 _≤ t ≤_ 1 _} be a planar Brownian motion. Then, almost surely, α-cone points exist for any α ≥ π but not for α < π. Moreover, if α ∈_ [ _π,_ 2 _π_ ) _, then_


In the proof of Theorem 10.38 we identify R<sup>2</sup> with the complex plane and use complex notation wherever convenient. Suppose that _{B_ ( _t_ ): _t ≥_ 0 _}_ is a planar Brownian motion defined for all positive times. We first fix an angle _α ∈_ (0 _,_ 2 _π_ ) and a direction _ξ ∈_ [0 _,_ 2 _π_ ) and define the notion of an approximate cone point as follows: For any 0 _< δ < ε_ we let


and


We say that _z ∈_ R<sup>2</sup> is a ( _δ, ε_ ) _-approximate cone point_ if


Note that we do not require ( _δ, ε_ )-approximate cone points to belong to the Brownian path. The relation between cone points and approximate cone points will become clear later, we first collect the necessary information about the probability that a given point is a ( _δ, ε_ )-approximate cone point. The strong Markov property allows us to consider the events happening during the intervals [0 _, Tδ_ ( _z_ )] and [ _Tδ/_ 2( _z_ ) _,_ 1] separately.

Lemma 10.39. _There exist constants C > c >_ 0 _such that, for every δ >_ 0 _,_


- (b) _for all z ∈_ R<sup>2</sup> _with_ 0 _∈ z_ + _W_ [ _α/_ 2 _, ξ_ ] _,_


297

**Proof.** We write _z_ = _|z| e_<sup>**i**</sup><sup>_θ_</sup> and apply the skew-product representation, Theorem 7.25, to the Brownian motion _{z − B_ ( _t_ ): _t ≥_ 0 _}_ and obtain


for _R_ ( _t_ ) = exp( _W_ 1( _H_ ( _t_ )) and _θ_ ( _t_ ) = _W_ 2( _H_ ( _t_ )), where _{W_ 1( _t_ ): _t ≥_ 0 _}_ and _{W_ 2( _t_ ): _t ≥_ 0 _}_ are independent linear Brownian motions started in log _|z|_ , resp. in _θ_ , and a strictly increasing time-change _{H_ ( _t_ ): _t ≥_ 0 _}_ which depends only on the first of these motions. This implies that _Tδ_ ( _z_ ) = inf _{s ≥_ 0: _R_ ( _s_ ) _≤ δ}_ and therefore


We infer that


The latter event means that a linear Brownian motion started in _θ_ stays inside the interval [ _ξ − π − α/_ 2 _, ξ − π_ + _α/_ 2] up to the independent random time _τ_ log _δ._ For the probability of such events we have found two formulas, (4.2) and (4.3) in Chapter 7. The latter formula gives


using Exercise 2.16 (a) to evaluate the Laplace transform of the first hitting times of a point by linear Brownian motion. Now note that the upper bound, part (a) of the lemma, is trivial if _|z| ≤_ 2 _δ_ , and otherwise one can bound the exact formula from above by


The lower bound, part (b) of the lemma, follows from Brownian scaling if _δ/|z|_ is bounded from below. Otherwise note that, under our assumption on _z_ we have _|θ_ + _π − ξ| ≤_<sup>_<u>α</u>_</sup> 4<sup>andthusthe</sup> sine term corresponding to _k_ = 0 is bounded from below by sin( _π/_ 4) _>_ 0. Thus we get a lower bound of


and the bracket is bounded from below by a positive constant if _δ/|z|_ is sufficiently small.

An entirely analogous argument also provides the estimates needed for the events imposed _after_ the Brownian motion has hit the ball _B_ ( _z, δ/_ 2).

298

Lemma 10.40. _There exist constants C > c >_ 0 _such that, for every_ 0 _< δ < ε,_

- (a) _for all x, z ∈_ R<sup>2</sup> _with |x − z|_ = _δ/_ 2 _,_


- (b) _for all x, z ∈_ R<sup>2</sup> _with |x − z|_ = _δ/_ 2 _and x − z ∈ W_ [ _α/_ 2 _, ξ_ ] _,_


We now focus on the _upper bound_ . Using the strong Markov property we may combine Lemmas 10.39 (a) and 10.40 (a) to obtain the following lemma.

Lemma 10.41. _There exists a constant C_ 0 _>_ 0 _such that, for any z ∈_ R<sup>2</sup> _,_


where we have used Lemmas 10.39 (a) and 10.40 (a). The result follows with _C_ 0 := _C_<sup>2</sup> .

Let _M_ ( _α, ξ, ε_ ) be the set of all points in the plane, which are ( _δ, ε_ )-approximate cone points for all _δ >_ 0. Obviously _z ∈ M_ ( _α, ξ, ε_ ) if and only if there exist _t >_ 0 such that _z_ = _B_ ( _t_ ) and


where


Lemma 10.42. _Almost surely,_

- _if α ∈_ (0 _, π_ ) _then M_ ( _α, ξ, ε_ ) = _∅,_


**Proof.** Take a compact cube Cube of unit sidelength not containing the origin. It suffices to show that _M_ ( _α, ξ, ε_ ) _∩_ Cube = _∅_ if _α ∈_ (0 _, π_ ) and dim _M_ ( _α, ξ, ε_ ) _∩_ Cube _≤_ 2 _−_<sup><u>2</u></sup> _α_<sup>_<u>π</u>_if</sup><sup>_α ∈_(</sup><sup>_π,_2</sup><sup>_π_).</sup> Given a dyadic subcube _D ∈_ D _k_ of sidelength 2<sup>_−k_</sup> let _D_<sup>_∗_</sup> _⊃ D_ be a concentric ball around _D_ with radius (1 + _√_ 2)2<sup>_−k_</sup> . Define the _focal point x_ = _x_ ( _D_ ) of _D_ to be

- if _α < π_ the tip of the cone _x_ + _W_ [ _α, ξ_ ] whose boundary halflines are tangent to _D_<sup>_∗_</sup> ,

- if _α > π_ the tip of the cone whose dual has boundary halflines tangent to _D_<sup>_∗_</sup> .

The following properties are easy to check:

- for every _y ∈ D_ we have _y_ + _W_ [ _α, ξ_ ] _⊂ x_ + _W_ [ _α, ξ_ ],

299


- for some _k_ 0 _∈_ N depending only on _α_ and _ε_ , every _y ∈ D_ and _k ≥ k_ 0, _B_ ( _y, ε_ ) _⊃B_ ( _x, ε/_ 2) _._

This implies that, if _k ≥ k_ 0 and the cube _D ∈_ D _k_ contains a (2<sup>_−k_</sup> _, ε_ )-approximate cone point, then its focal point _x_ is a ( _C_ 12<sup>_−k_</sup> _, ε/_ 2)-approximate cone point. Hence, by Lemma 10.41, for a constant _C_ 2 _>_ 0,


Note that, given Cube and _ε >_ 0 we can find _k_ 1 _≥ k_ 0 such that _|x_ ( _D_ ) _|_ is bounded away from zero over all _D ∈_ D _k_ and _k ≥ k_ 1. Hence we obtain _C_ 3 _>_ 0 such that, for all _k ≥ k_ 1,


Then, if _α ∈_ (0 _, π_ ),


proving part (a). Moreover, if _α ∈_ ( _π,_ 2 _π_ ) and _k ≥ k_ 1, we may cover _M_ ( _α, ξ, ε_ ) _∩_ Cube by the collection of cubes _D ∈_ D _k_ which contain a (2<sup>_−k_</sup> _, ε_ )-approximate cone point. Then, for any _γ >_ 2 _−_<sup><u>2</u></sup> _α_<sup>_<u>π</u>_theexpected</sup><sup>_γ_-valueofthiscoveringis</sup>


and this proves that, almost surely, dim _M_ ( _α, ξ, ε_ ) _≤ γ_ .

**Proof of the upper bound in Theorem 10.38.** Suppose _δ >_ 0 is arbitrary and _z ∈_ R<sup>2</sup> is an _α_ -cone point. Then there exist a rational number _q ∈_ [0 _,_ 1), a rational direction _ξ ∈_ [0 _,_ 2 _π_ ), and a rational _ε >_ 0, such that _z_ = _B_ ( _t_ ) for some _t ∈_ ( _q,_ 1) and


By Lemma 10.42 for every fixed choice of rational parameters this set is empty almost surely if _α_ + _δ < π_ . For any _α < π_ we can pick _δ >_ 0 with _α_ + _δ < π_ and hence there are no _α_ -cone points almost surely. Similarly, if _α ≥ π_ we can use Lemma 10.42 and the countable stability of Hausdorff dimension to obtain an almost sure upper bound of 2 _−_ 2 _π/_ ( _α_ + _δ_ ) for the set of _α_ -cone points. The result follows as _δ >_ 0 was arbitrary.

300

We now establish the framework to prove the lower bound in Theorem 10.38. Again we fix _x_ 0 _∈_ R<sup>_d_</sup> and a cube Cube = _x_ 0 + [0 _,_ 1)<sup>_d_</sup> . Recall the definition of the collection D _k_ of dyadic subcubes of sidelength 2<sup>_−k_</sup> and let D =<sup>�</sup><sup>_∞_</sup> _k_ =1<sup>D</sup><sup>_k_.Supposethat</sup><sup>_{Z_(</sup><sup>_I_):</sup><sup>_I∈_D</sup><sup>_}_isacollection</sup> of random variables each taking values in _{_ 0 _,_ 1 _}_ . With this collection we associate the random set


Theorem 10.43. _Suppose that the random variables {Z_ ( _I_ ) : _I ∈_ D _} satisfy the monotonicity condition_


_Assume that, for some positive constants γ, c_ 1 _and C_ 1 _,_


(ii) E� _Z_ ( _I_ ) _Z_ ( _J_ )� _≤ C_ 1 _|I|_<sup>2</sup><sup>_γ_</sup> dist( _I, J_ )<sup>_−γ_</sup> _for all I, J ∈_ D _k and k ≥_ 1 _. Then, for λ > γ and_ Λ _⊂_ Cube _closed with H_<sup>_λ_</sup> (Λ) _>_ 0 _, there exists a p >_ 0 _, such that_


Remark 10.44. Though formally, if the monotonicity condition holds, _A_ is a limsup fractal, the monotonicity establishes a strong dependence of the random variables _{Z_ ( _I_ ) : _I ∈_ D _k}_ which in general invalidates the second assumption of Theorem 10.28. We therefore need a result which deals specifically with this situation. _⋄_

We prepare the proof with a little lemma, based on Fubini’s theorem.

Lemma 10.45. _Suppose ν is a probability measure on_ R<sup>_d_</sup> _such that νB_ ( _x, r_ ) _≤ Cr_<sup>_λ_</sup> _for all x ∈_ R<sup>_d_</sup> _, r >_ 0 _. Then, for all_ 0 _< β < λ there exists C_ 2 _>_ 0 _such that,_


_|x − y|_<sup>_−β_</sup> _dν_ ( _x_ ) _dν_ ( _y_ ) _< ∞ . This implies, in particular, that_ ��

**Proof.** Fubini’s theorem gives


which implies the first statement. Moreover,


**Proof of Theorem 10.43.** We show that there exists _p >_ 0 such that, for every 0 _< β < λ − γ_ , with probability at least _p_ , there exists a positive measure _µ_ on Λ _∩ A_ such that its _β_ -energy _Iβ_ ( _µ_ ) is finite. This implies dim( _A ∩_ Λ) _≥ β_ by the energy method, see Theorem 4.27.

To begin with, given Λ _⊂_ Cube with _H_<sup>_λ_</sup> (Λ) _>_ 0, we use Frostman’s lemma to find a Borel probability measure _ν_ on Λ and positive constants 0 _< c < C_ such that _ν_ ( _D_ ) _≤ C|D|_<sup>_λ_</sup> for all Borel sets _D ⊂_ R<sup>_d_</sup> . Writing


we define _µn_ to be the measure supported on Λ given by

_µn_ ( _B_ ) = 2<sup>_nγ_</sup> _ν_ ( _B ∩ An_ ) for any Borel set _B ⊂_ R<sup>_d_</sup> .

Then, using (i), we get


Moreover, using (ii), we obtain


where finiteness of _C_ 3 follows from the second statement of Lemma 10.45. We now show that, for every _β < λ − γ_ we find _k_ ( _β_ ) such that E _Iβ_ ( _µn_ ) _≤ k_ ( _β_ ). Indeed,


For the first summand, we use that dist( _I, J_ )<sup>_−γ_</sup> _≤_ (3 _√d_ )<sup>_γ_</sup> _|x − y|_<sup>_−γ_</sup> whenever _x ∈ I_ and _y ∈ J_ , and infer boundedness from the second statement of Lemma 10.45. For the second summand the first statement of Lemma 10.45 gives a bound of


302

Hence, E _Iβ_ ( _µn_ ) is bounded uniformly in _n_ , as claimed. We therefore find _ℓ_ ( _β_ ) _>_ 0 such that


Now, by the Paley-Zygmund inequality, see Lemma 3.22,


Hence we obtain that


Using Fatou’s lemma we infer that


On this event we can pick a subsequence along which _µn_ converges to some measure _µ_ . Then _µ_ is supported by _A_ and _µ_ (Cube) _≥_ lim inf _µn_ (Cube) = lim inf _µn_ ( _An_ ) _≥ c_ 1 _/_ 2.

Finally, for each _ε >_ 0, where the limit is taken along the chosen subsequence,


and for _ε ↓_ 0 we get _Iβ_ ( _µ_ ) _≤ ℓ_ ( _β_ ).

We now use Theorem 10.43 to give a _lower bound_ for the dimension of the set of cone points. Fix _α ∈_ ( _π,_ 2 _π_ ) and a unit cube


Choose a large radius _R >_ 2 such that Cube _⊂B_ (0 _, R/_ 2) and define


Given a cube _I ∈_ C _k_ ( _x_ 0) we denote by _z_ its centre and let _Z_ ( _I_ ) = 1 if _z_ is a (2<sup>_−k_</sup> _, rk_ )- approximate cone point with direction _ξ_ = _π_ , i.e. if


and otherwise let _Z_ ( _I_ ) = 0. By our choice of the sequence ( _rk_ ) we have


Lemma 10.46. _There are constants_ 0 _< c_ 1 _< C_ 1 _< ∞ such that, for any cube I ∈_ C _, we have_


303

**Proof.** The upper bound is immediate from Lemma 10.41. For the lower bound we use that, for any _z ∈_ Cube and _δ >_ 0,


and hence, if _z_ is the centre of _I ∈_ C _k_ and _δ_ = 2<sup>_−k_</sup> , using Lemmas 10.39 (b) and 10.40 (b),

which gives the desired statement, as _|z|_ is bounded away from infinity.

Lemma 10.47. _There is a constant_ 0 _< C_ 1 _< ∞ such that, for any cubes I, J ∈_ C _k, k ≥_ 1 _, we have_


Exchanging the rˆoles of _I_ and _J_ gives the corresponding estimate


and the proof is completed by adding the two estimates.

**Proof of the lower bound in Theorem 10.38.** The set _A_ which we obtain from our choice of _{Z_ ( _I_ ): _I ∈_ C _}_ is contained in the set


304

Therefore, by Theorem 10.43, we have dim _A_<sup>˜</sup> _≥_ 2 _−_ 2 _π/α_ with positive probability. Given any 0 _< δ <_ 1 _/_ 2, we define a sequence _τ_ 1( _δ_ ) _≤ τ_ 2( _δ_ ) _≤ . . ._ of stopping times by _τ_ 1( _δ_ ) = 0 and, for _k ≥_ 1,


Denoting


we have that


Now fix _β <_ 2 _−_ 2 _π/α_ . The events _{_ dim _Ak_ ( _δ_ )<sup>_≥β}_allhavethesameprobability,whichcannot</sup> be zero as this would contradict the lower bound on the dimension of _A_<sup>˜</sup> . In particular, there exists _p_ ( _Rδ_ )<sup>_>_0suchthat</sup>


By scaling we get that _p_ ( _Rδ_ )<sup>doesnotdependon</sup><sup>_R_.Hence,byBlumenthal’szero-onelaw,we</sup> have that _p_ ( _Rδ_ )<sup>= 1forall</sup><sup>_δ>_0</sup><sup>_, R >_0.Letting</sup><sup>_ε ↓_0weget,almostsurely,</sup>


for every _δ >_ 0, _R >_ 0. On this event we may choose first _R >_ 1 and then _δ >_ 0 such that

and get that the Hausdorff dimension of the set of _α_ -cone points is at least 2 _−_<sup><u>2</u></sup> _α_<sup>_<u>π</u>_</sup>


A surprising consequence of the non-existence of cone points for angles smaller then _π_ is that the convex hull of the planar Brownian curve is a fairly smooth set.

Theorem 10.48 (Adelman (1982)). _Almost surely, the convex hull of {B_ ( _s_ ): 0 _≤ s ≤_ 1 _} has a differentiable boundary._

**Proof.** A compact, convex subset _H ⊂_ R<sup>2</sup> is said to have a _corner_ at _x ∈ ∂H_ if there exists a cone with vertex _x_ and opening angle _α < π_ which contains _H_ . If _H_ does not have corners, the supporting hyperplanes are unique at each point _x ∈ ∂H_ and thus _∂H_ is a differentiable boundary.

So all we have to show is that the convex hull _H_ of _{B_ ( _s_ ) : 0 _≤ s ≤_ 1 _}_ has no corners. Clearly, by Spitzer’s theorem, _B_ (0) and _B_ (1) are no corners almost surely. Suppose any other point _x ∈ ∂H_ is a corner, then obviously it is contained in the path, and therefore it is an _α_ -cone point for some _α > π_ . By Theorem 10.38, almost surely, such points do not exist and this is a contradiction.

305

### **Exercises**

Exercise 10.1. Show that, for every metric space _E_ ,

dim _P E_ = inf _{s_ : _P_<sup>_s_</sup> ( _E_ ) _< ∞}_ = sup _{s_ : _P_<sup>_s_</sup> ( _E_ ) _>_ 0 _}_ = sup _{s_ : _P_<sup>_s_</sup> ( _E_ ) = _∞}._

Exercise 10.2 ( _∗_ ). Show that, for every metric space _E_ , we have


Exercise 10.3. Let _{mk_ : _k ≥_ 1 _}_ be a rapidly increasing sequence of positive integers such that


Define two subsets of [0 _,_ 1] by


and


Show that


(2) dim _P E_ = dim _M E_ = 1 and dim _P F_ = dim _M F_ = 1, (3) dim( _E × F_ ) _≥_ 1.

Exercise 10.4. Show that, almost surely,

- dim _P_ Range = 2, for Brownian motion in _d ≥_ 2,


306

Exercise 10.5. Show that, for every _a ∈_ [0 _, √_ 2], we have almost surely,


**Hint.** This can be done directly, but it can also be derived from more general ideas, as formulated for example in Exercise 10.9.

Exercise 10.6. Show that


Exercise 10.7 ( _∗_ ). Use Theorem 10.43 to prove once more that the zero set Zero of linear Brownian motion has Hausdorff dimension 2<sup><u>1</u>almostsurely.</sup>

Exercise 10.8. Show that, if


then, for any compact _E ⊂_ [0 _,_ 1] with dim _P_ ( _E_ ) _< γ_ , we have


Note that no independence assumption is needed for this statement.

Exercise 10.9 ( _∗_ ).

(a) Suppose _A_ is a discrete limsup fractal associated to random variables _{Z_ ( _I_ ) : _I ∈_ C _k, k ≥_ 1 _}_ satisfying the conditions of Theorem 10.28. Then, if dim _P_ ( _E_ ) _> γ_ , we have almost surely, dim _P_ ( _A ∩ E_ ) = dim _P_ ( _E_ ).

(b) Show that, if dim _P_ ( _E_ ) _> a_<sup>2</sup> , then almost surely


where _F_ ( _a_ ) is the set of _a_ -fast points.

307

Exercise 10.10 ( _∗_ ). Give a proof of Lemma 10.40 (a) based on Theorem 7.24.

Exercise 10.11. Suppose _K ⊂_ R<sup>2</sup> is a compact set and _x ∈_ R<sup>2</sup> _\ K_ a point outside the set. Imagine _K_ as a solid body, and _x_ as the position of an observer. This observer can only see a part of the body, which can be formally described as


where [ _x, y_ ] denotes the compact line segment connecting _x_ and _y_ . It is natural to ask for the Hausdorff dimension of the visible part of a set _K_ . Assuming that dim _K ≥_ 1, an unresolved conjecture in geometric measure theory claims that, for Lebesgue-almost every _x̸ ∈ K_ , the Hausdorff dimension of _K_ ( _x_ ) is one.

Show that this conjecture holds for the path of planar Brownian motion, _K_ = _B_ [0 _,_ 1], in other words, almost surely, for Lebesgue almost every _x ∈_ R<sup>2</sup> , the Hausdorff dimension of the visible part _B_ $$0 _,_ 1$$( _x_ ) is one.

Exercise 10.12. Let _{B_ ( _t_ ): _t ≥_ 0 _}_ be a planar Brownian motion and _α ∈_ [ _π,_ 2 _π_ ). Show that, almost surely, no double points are _α_ -cone points.

Exercise 10.13 ( _∗_ ). Let _{B_ ( _t_ ): _t ≥_ 0 _}_ be a planar Brownian motion and _α ∈_ (0 _, π_ ]. A point _x_ = _B_ ( _t_ ), 0 _< t <_ 1, is a _one-sided α_ -cone point if there exists _ξ ∈_ [0 _,_ 2 _π_ ) such that

_B_ (0 _, t_ ) _⊂ x_ + _W_ [ _α, ξ_ ] _._

- (a) Show that for _α ≤_<sup>_<u>π</u>_</sup> 2<sup>,almostsurely,therearenoone-sided</sup><sup>_α_-conepoints.</sup>

- (b) Show that for _α ∈_ (<sup>_<u>π</u>_</sup> 2<sup>_, π_],almostsurely,thesetofone-sided</sup><sup>_α_-conepointshas</sup> Hausdorff dimension 2 _− α_<sup>_<u>π</u>_.</sup>

308

### **Notes and Comments**

The paper [ **OT74** ] by Orey and Taylor is a seminal work in the study of dimension spectra for exceptional points of Brownian motion. It contains a proof of Theorem 10.3 using the mass distribution principle and direct construction of the Frostman measure. This approach can be extended to other limsup fractals, but this method requires quite strong independence assumptions which make this method difficult in many more general situations. In [ **OT74** ] the question how often on a Brownian path the law of the iterated logarithm fails is also answered in the sense that, for _θ >_ 1, almost surely, the set


has zero or infinite Hausdorff measure for the gauge function _φ_ ( _r_ ) = _r_ log(1 _/r_ )<sup>_γ_</sup> depending whether _γ < θ_<sup>2</sup> _−_ 1 or _γ > θ_<sup>2</sup> _−_ 1.

Our proof of Theorem 10.3 is based on estimates of energy integrals. This method was used by Hu and Taylor [ **HT97** ] and Shieh and Taylor [ **ST99** ], and our exposition follows closely [ **DPRZ00** ]. In the latter paper an interesting class of exceptional times for the Brownian motion is treated, the _thick times_ of Brownian motions in dimension _d ≥_ 3. For any time _t ∈_ (0 _,_ 1) we let _U_ ( _t, ε_ ) = _L{s ∈_ (0 _,_ 1) : _|B_ ( _s_ ) _− B_ ( _t_ ) _| ≤ ε}_ the set of times where the Brownian is up to _ε_ near to its position at time _t_ . It is shown that, for all 0 _≤ a ≤ π_<sup><u>162</u>,almost</sup> surely,


This paper should be very accessible to anyone who followed the arguments of Section 10.1. The method of [ **DPRZ00** ] can be extended to limsup fractals with somewhat weaker independence properties and also extends to the study of dimension spectra with strict equality.

The third way to prove Theorem 10.3 is the method of stochastic codimension explored in Section 10.2. An early reference for this method is Taylor [ **Ta66** ] who suggested to use the range of stable processes as test sets, and made use of the potential theory of stable processes to obtain lower bounds for Hausdorff dimension. This class of test sets is not big enough for all problems: the Hausdorff dimension of a stable processes is bounded above by its index, hence cannot exceed 2, and therefore these test sets can only test dimensions in the range [ _d −_ 2 _, d_ ]. A possible remedy is to pass to multiparameter processes, see the recent book of Khoshnevisan [ **Kh02** ] for a survey. Later, initiated by seminal papers of Hawkes [ **Ha81** ] and R. Lyons [ **Ly90** ], it was discovered that percolation limit sets are a very suitable class of test functions, see [ **KPX00** ]. Our exposition closely follows the latter reference.

Kaufman [ **Ka75** ] showed that every compact set _E ⊂_ [0 _,_ 1] with dim( _E_ ) _> a_<sup>2</sup> almost surely contains an _a_ -fast point, but the more precise result involving the packing dimension is due to [ **KPX00** ]. The concept of packing dimension was introduced surprisingly late by Tricot in [ **Tr82** ] and in [ **TT85** ] it was investigated together with the packing measure and applied to the Brownian path by Taylor and Tricot. Lemma 10.18(i) is from [ **Tr82** ], Lemma 10.18(ii) for

309

trees can be found in [ **BP94** ], see Proposition 4.2(b), the general version given is in Falconer and Howroyd [ **FH96** ] and in Mattila and Mauldin [ **MM97** ].

Several people contributed to the investigation of slow points, for example Dvoretzky [ **Dv63** ], Kahane [ **Ka76** ], Davis [ **Da83** ], Greenwood and Perkins [ **GP83** ] and Perkins [ **Pe83** ]. There are a number of variants, for example one can allow _h <_ 0 in (3.1) or omit the modulus signs. The Hausdorff dimension of _a_ -slow points is discussed in [ **Pe83** ], this class of exceptional sets is not tractable with the limsup-methods: note that an exceptional behaviour is required at all small scales. The crucial ingredient, the finiteness criterion for moments of the stopping times _T_ ( _r, a_ ) is due to Shepp [ **Sh67** ].

Cone points were discussed by Evans in [ **Ev85** ], an alternative discussion can be found in Lawler’s survey paper [ **La99** ]. Our argument essentially follows the latter paper. The correlation condition in Theorem 10.43 appears in the strongly related context of quasi-Bernoulli percolation on trees, see Lyons [ **Ly92** ].

An alternative notion of _global_ cone points requires that the entire path of the Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ stays inside the cone with tip in the cone point. The same dimension formula holds for this concept. The upper bound follows of course from our consideration of local cone points, and our proof gives the lower bound with positive probability. The difficult part is to show that the lower bound holds with probability one. A solution to this problem is contained in Burdzy and San Mart´ın [ **BSM89** ], and this technique has also been successfully used in the study of the Brownian frontier [ **La96b, BJPP97** ].

A discussion of the smoothness of the boundary of the convex hull can be found in Cranston, Hsu and March [ **CHM89** ], but our Theorem 10.48 is older. The result was stated by L´evy [ **Le48** ] and was probably first proved by Adelman in 1982, though this does not seem to be published.

It is conjectured in geometric measure theory that for any set of Hausdorff dimension dim _K ≥_ 1, for Lebesgue-almost every _x̸ ∈ K_ , the Hausdorff dimension of the visible part _K_ ( _x_ ) is one. For upper bounds on the dimension and the state of the art on this conjecture, see [ **ON04** ]. It is natural to compare this to Makarov’s theorem on the support of harmonic measure: if the rays of light were following Brownian paths rather than straight lines, the conjecture would hold by Makarov’s theorem, see [ **Ma85** ].

310

---

[← Intersections and self-intersections of Brownian paths](13-intersections-and-self-intersections-of-brownian-paths.md) · [Up: contents](index.md) · [Appendix I: Hints and solutions for selected exercises →](15-appendix-i-hints-and-solutions-for-selected-exercises.md)
