---
title: 28 Lecture 28
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 28 Lecture 28

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We shall study the method of proving rate minimaxity results via Fano’s inequality. The first step is to bound from below the minimax risk in a general decision-theoretic problem via the Bayes risk in a testing problem.

## **28.1 Minimax Lower Bound via Testing**

Consider the general decision-theoretic setting with a parameter space Θ, action space _A_ and nonnegative loss function _L_ ( _θ, a_ ). We observe data _X_ whose distribution belongs to the family _{Pθ, θ ∈_ Θ _}_ .

Let _F_ be a finite subset of Θ. We say that _F_ is _η_ -separated for a positive real number _η_ if


151

Let _w_ denote the uniform prior on _F_ . The lemma below shows that, when _F_ is _η_ -separated, the Bayes risk _R_ Bayes( _w_ ) is bounded from below by ( _η/_ 2) times the Bayes risk in the testing problem corresponding to the probability measures _Pθ, θ ∈ F_ .

**Lemma 28.1.** _Suppose F is η-separated. Then_


Note here that


where the infimum is over all decision rules _d_ in _R_ Bayes( _w_ ) and over all tests _T_ (i.e., functions from _X_ to _F_ ) in _B_ ( _{Pθ, θ ∈ F }_ ).

_Proof of Lemma 28.1._ Using _L_ ( _θ, a_ ) _≥_ ( _η/_ 2) _I{L_ ( _θ, a_ ) _≥ η/_ 2 _}_ , we obtain


For each decision rule _d_ , we now associate a test _T_ in the following way. Define _T_ ( _X_ ) as equal to _θ_ provided there exists a _θ ∈ F_ such that _L_ ( _θ, d_ ( _X_ )) _< η/_ 2 (note that because _F_ is _η_ -separated, there exists at most one _θ ∈ F_ such that _L_ ( _θ, d_ ( _X_ )) _< η/_ 2). If there is no such _θ ∈ F_ , then we take _T_ ( _X_ ) to be an arbitrary point in _F_ . With this construction, it is easy to see that


From here, inequality (254) immediately follows.

In the last class, we proved the following inequality (known as Fano’s inequality)


Combining this with Lemma 28.1 and the fact that _R_ Minimax _≥ R_ Bayes( _w_ ) for every prior _w_ , we obtain the following minimax lower bound:


We shall see two examples of this bound below: to sparse normal mean estimation and Lipschitz regression. The main challenge in using (255) is to make an appropriate choice of _F_ .

In many applications, Θ _⊆A_ and _L_ ( _θ, a_ ) = _d_<sup>2</sup> ( _θ, a_ ) for some pseudometric _d_ on _A_ . In this case, note that


This is because for every _θ_ 1 _, θ_ 2 _∈ F_ with _θ_ 1 _̸_ = _θ_ 2 and _a ∈A_ , we have


152

## **28.2 Sparse Normal Mean Estimation**

Consider the problem of estimating a 1-sparse vector _θ ∈_ R<sup>_n_</sup> in squared Euclidean loss from _Y ∼ Nn_ ( _θ, In_ ). Here Θ is the class of all 1-sparse vectors in R<sup>_n_</sup> , _A_ = R<sup>_n_</sup> and _L_ ( _θ, a_ ) is the squared Euclidean distance between _θ_ and _a_ . Also _Pθ_ is the _Nn_ ( _θ, In_ ) distribution.

It is natural here to apply (255) with _F_ = _{τe_ 1 _, . . . , τen}_ for some _τ >_ 0 (chosen later). Because _∥τei − τej∥_ = _τ √_ 2 for every _i̸_ = _j_ , it follows that _F_ is _η_ separated with _η_ = _τ_<sup>2</sup> (using (256)). Inequality (255) then gives


In the last class, we saw that

and this gives


Taking _τ_<sup>2</sup> = log _n_ will give that _R_ Minimax _≥ c_ log _n_ for a positive constant _c_ (for _n_ large). This result is good enough to yield rate minimaxity of soft thresholding with _λ_ =<sup>_√_</sup> 2 log _n_ . However it is not strong enough to yield sharp asymptotic minimaxity.

## **28.3 Lipschitz Regression**

Let _F_ denote the class of all functions _f_ : [0 _, ._ 1] _→_ R that are bounded in absolute value by 1 and 1-Lipschitz. Consider the problem of estimating _f ∈F_ from i.i.d observations ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) where


We take Θ = _F_ , _A_ to be the class of all real-valued functions on [0 _,_ 1] and use the loss function


We shall denote by _Pf_ the joint distribution of ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ). Note that _Pf_ has the following density on [0 _,_ 1]<sup>_n_</sup> _×_ R<sup>_n_</sup> :


We are interested in the minimax risk:

It can be shown that _R_ Minimax _≤ Cn_<sup>_−_2</sup><sup>_/_3</sup> for a universal positive constant _C_ . This can be done by studying the least sqaures estimator over _F_ (using methods that we looked at previously in the class). One can also consider simpler kernel regression estimators (see, for example, Tsybakov [23, Chapter 1]). Here we shall prove (using (255)) that _R_ Minimax _≥ cn_<sup>_−_2</sup><sup>_/_3</sup> for a positive constant _c_ . This will prove, in particular, that the least squares estimator is minimax rate optimal for estimating functions in _F_ .

The main challenge is to construct a suitable finite subset _F_ of _F_ . The standard construction is as follows. Fix a small _δ >_ 0. For a closed subinterval _I_ of [0 _,_ 1] of length _δ_ , let _TI_ : _I →_ [0 _, δ_ ] denote the piecewise linear _tent_ function which equals its maximum value _δ_ at the midpoint of the interval _I_ (specifically _TI_ linearly

153

increases from 0 at the left end point of _I_ to _δ_ at the midpoint of _I_ and then linearly decreases to 0 at the right end point of _I_ ). Now consider the _m_ intervals:


We now construct 2<sup>_m_</sup> functions in _F_ . These functions will be indexed by _τ ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> and will be denoted by _{fτ , τ ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> _}_ . Specifically, for each _τ ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> , we define _fτ_ to equal the tent function _TIj_ on the interval _Ij_ if _τj_ = 1 and to equal zero on _Ij_ if _τj_ = 0. Also each _fτ_ will equal zero outside _∪jIj_ .

We shall apply (255) with this collection _{Pfτ_ : _τ ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> _}_ . The first step is find a suitable value _η_ for which _F_ := _{fτ , τ ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> _}_ is _η_ -separated. For this, fix _τ, τ_<sup>_′_</sup> _∈{_ 0 _,_ 1 _}_<sup>_m_</sup> with _τ̸_ = _τ_<sup>_′_</sup> . Then _τj̸_ = _τj_<sup>_′_forsome</sup> _j ∈{_ 1 _, . . . , m}_ and then it is easy to see that


It follows (from (256)) that _F_ is _η_ -separated with _η_ ≳ _δ_<sup>3</sup> . Inequality (255) then says that


We next need to bound _I_ from above. For this, we shall use


with _Q_ = _P_ 0 (i.e., _Pf_ corresponding to _f ≡_ 0). Note that for two functions _f, g_ ,


where

_X_ 1 _∼_ Unif[0 _,_ 1]; _Y_ 1 _|X_ 1 _∼ N_ ( _f_ ( _X_ 1) _,_ 1) and _X_ ˜1 _∼_ Unif[0 _,_ 1]; _Y_ ˜1 _|X_ ˜1 _∼ N_ ( _g_ ( ˜ _X_ 1) _,_ 1) _._ One can then also compute that


We thus have


and consequently _I ≤ nδ_<sup>2</sup> . We thus have


Because _m ≥ c_ 1 _/δ_ for a positive constant _c_ 1, we have


Taking _δ_<sup>3</sup> = ( _c_ 1 log 2) _/_ (2 _n_ ), we obtain _R_ Minimax ≳ _n_<sup>_−_1</sup> for all large _n_ . Note however that we set out to prove _R_ Minimax ≳ _n_<sup>_−_2</sup><sup>_/_3</sup> so the above argument yields a suboptimal lower bound for _R_ Minimax. The reason where this argument becomes weak is in the separation calculation. Indeed, we used the fact that


154

It is also easy to see that the above bound is tight up to a constant multiplicative factor when _τ_ and _τ_<sup>_′_</sup> differ in only one coordinate (i.e., _H_ ( _τ, τ_<sup>_′_</sup> ) :=<sup>�</sup> _j_<sup>_I{τj̸_=</sup><sup>_τ ′_</sup> _j_<sup>_}_equalsexactly1).However,ingeneral,the</sup><sup>_L_2</sup> distance between _fτ_ and _fτ ′_ depends on _H_ ( _τ, τ_<sup>_′_</sup> ). Precisely, it is easily seen that


The Gilbert-Varshamov Lemma (stated and proved next) proves the existence of a subset _W_ of _{_ 0 _,_ 1 _}_<sup>_m_</sup> with cardinality _|W | ≥_ exp( _m/_ 8) and such that _H_ ( _τ, τ_<sup>_′_</sup> ) _> m/_ 4 for every _τ, τ_<sup>_′_</sup> _∈ W_ with _τ̸_ = _τ_<sup>_′_</sup> . The idea then is to apply (255) to _F_ = _{fτ_ : _τ ∈ W }_ as opposed to _F_ = _{fτ_ : _τ ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> _}_ . The inequality (257) above along with _H_ ( _τ, τ_<sup>_′_</sup> ) ≳ _m_ ≳ (1 _/δ_ ) for _τ, τ_<sup>_′_</sup> _∈ W_ with _τ̸_ = _τ_<sup>_′_</sup> implies then that _F_ = _{fτ_ : _τ ∈ W }_ is _η_ -separated with _η_ ≳ _δ_<sup>2</sup> . The mutual information bound remains the same as before. We would then obtain


The choice _δ_<sup>3</sup> = ( _c_ 1 log 2) _/_ (2 _n_ ) would then give _R_ Minimax ≳ _n_<sup>_−_2</sup><sup>_/_3</sup> for all large _n_ .

## **28.4 Gilbert-Varshamov Lemma**

**Lemma 28.2.** _For every m ≥_ 1 _, there exists a subset W of {_ 0 _,_ 1 _}_<sup>_m_</sup> _with cardinality |W | ≥_ exp( _m/_ 8) _such that H_ ( _τ, τ_<sup>_′_</sup> ) _> m/_ 4 _for every τ, τ_<sup>_′_</sup> _∈ W with τ̸_ = _τ_<sup>_′_</sup> _._

_Proof._ The following elementary probability bound will be used here:


To prove (258), note that (the first equality follows by symmetry)


Taking _λ_ = log 3, we get


Now let _W_ be a maximal subset of _{_ 0 _,_ 1 _}_<sup>_m_</sup> for which _H_ ( _τ, τ_<sup>_′_</sup> ) _> m/_ 4 for every _τ, τ_<sup>_′_</sup> _∈ W_ with _τ̸_ = _τ_<sup>_′_</sup> . Maximal here means that the separation condition will be violated if any other element of _{_ 0 _,_ 1 _}_<sup>_m_</sup> is added to _W_ . This implies then that

so that


Now for every _A ⊆{_ 0 _,_ 1 _}_<sup>_m_</sup> , we have


Thus


Inequality (259) then immediately gives _|W | ≥_ exp( _m/_ 8) which completes the proof of Lemma 28.2.

155

## **28.5 Yang-Barron Method for Avoiding Explicit Construction of** _F_

As we mentioned earlier, the main difficulty in applying (255) is the construction of a finite subset _F_ of Θ. Yang and Barron [26] had a nice idea of avoiding the explicit construction of _F_ provided results on packing and covering numbers of Θ are available. Here are the details behind this idea.

For _η >_ 0, suppose _N_ ( _η,_ Θ) is any positive real number such that there exists an _η_ -separated finite subset _F_ of Θ with cardinality _|F | ≥ N_ ( _η,_ Θ). Applying inequality (255) to such an _F_ , we get


We now bound _I_ = _I_ ( _{Pθ, θ ∈ F }_ ) from above in the following way. We know that


for every probability measure _Q_ on _X_ . Suppose now that _Q_ 1 _, . . . , QM_ are arbitrary probability measures on _X_ and apply (261) with _Q_ = _Q_<sup>¯</sup> = ( _Q_ 1 + _· · ·_ + _QM_ ) _/M_ . This gives the bound


Now for each _θ ∈ F_ , if _q_ 1 _, . . . , qM_ denote the densities of _Q_ 1 _, . . . , QM_ w.r.t _µ_ respectively (and _pθ_ denote the density of _Pθ_ w.r.t _µ_ ), then


Now for every 1 _≤ j ≤ M_ , we have _q_ 1 + _· · ·_ + _qM ≥ qj_ so that


Since this is true for every 1 _≤ j ≤ M_ , we deduce


Since this is true for every _θ ∈ F_ , we obtain


Now for _ϵ >_ 0 and a subset _S_ of Θ, let _M_ ( _ϵ, S_ ) denote the minimal number _M_ of probability measures _Q_ 1 _, . . . , QM_ on _X_ such that


The above argument then gives


Using this bound in (260), we obtain that for every _η >_ 0 and _ϵ >_ 0,


The inequality _M_ ( _ϵ, F_ ) _≤ M_ ( _ϵ,_ Θ) (this is only useful if _M_ ( _ϵ,_ Θ) _< ∞_ ) then gives


156

The advantage with this bound is that it only depends on properties of Θ. For example, in the Lipschitz regression example, it is known (Lecture 6) that the packing numbers of _F_ (here _F_ is the class of all real-valued functions on [0 _,_ 1] that are 1-Lipschitz and bounded by 1) under the _L_<sup>2</sup> metric satisfy:


Using this, it is easy to show that we can take


in (262). This gives


From here taking _ϵ ∼ n_<sup>1</sup><sup>_/_6</sup> and _η ∼ n_<sup>_−_2</sup><sup>_/_3</sup> (and adjusting the underlying constants appropriately), we can immediately derive _R_ Minimax ≳ _n_<sup>_−_2</sup><sup>_/_3</sup> . Note that no explicit construction of a finite subset _F_ has been used in this argument (that work is implicitly done in the proof of the packing number bounds).

More generally, recall the smoothness class _Sd,α_ from Lecture 6. Consider the estimation of a function _f ∈Sd,α_ from _n_ i.i.d observations ( _X_ 1 _, Y_ 1) _, . . . ,_ ( _Xn, Yn_ ) with


Consider the integral _L_<sup>2</sup> loss function on [0 _,_ 1]<sup>_d_</sup> :


In this case, using the fact that the packing numbers of _Sd,α_ satisfy (stated in Lecture 6):


we can take (the constants here all depend on _d_ )


in (262). This gives


Taking _ϵ ∼ n_<sup>_d/_(2(2</sup><sup>_α_+</sup><sup>_d_))</sup> and _η_ = _n_<sup>_−_2</sup><sup>_α/_(2</sup><sup>_α_+</sup><sup>_d_)</sup> , we obtain that

_R_ Minimax _≥ n_<sup>_−_2</sup><sup>_α/_(2</sup><sup>_α_+</sup><sup>_d_)</sup> _._

---

[← 27 Lecture 27](28-27-lecture-27.md) · [Up: contents](index.md) · [References →](30-references.md)
