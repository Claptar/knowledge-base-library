---
title: February 7
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 7

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **7.1 Method of Moments**

Say that dist( _X_ ) is **determined by its moments** if _E|X|_<sup>_k_</sup> _< ∞∀k_ and for all _Y_ , if _EY_<sup>_k_</sup> = _EX_<sup>_k_</sup> _∀k_ , then _Y_ =d _X_ .

**Lemma 7.1** (Method of Moments) **.** _To prove Xn −→_ d _X, it is sufficient to prove (i) X is determined by its moments, (ii) EXn_<sup>_k→EXkasn →∞,foreachk≥_1</sup><sup>_._</sup>

_Proof. EXn_<sup>2isbounded,so(</sup><sup>_Xn, n≥_1)istight.If</sup><sup>_Xj_</sup> _n −→_ d some _Y_ , then _EY k_ = _EX k_ implies that _Y_ =d _X_ . By the old “subsequence trick” lemma, _Xn −→_ d _X_ .

Not all distributions are determined by moments.


_then_ dist( _X_ ) _is determined by its moments._

Consider _X_ = Normal(0d _,_ 1).


Also ( _n_ ! )<sup>1</sup><sup>_/n_</sup> _∼ n/e_ as _n →∞_ . Set _k_ = 2 _m_ .


So, (7.1) holds for Normal(0 _,_ 1).

### **7.2 Application to Poisson Limits**

It is easy to check (7.1).

28

29

_LECTURE 7. FEBRUARY 7_

_Notation_ . _x_ ( _x −_ 1)( _x −_ 2) _· · ·_ ( _x − k_ + 1) = [ _x_ ] _k_ . [ _x_ ]1 = _x_ , [ _x_ ]2 = _x_ ( _x −_ 1), etc. For _X ≥_ 0, integer-valued,


For _X_ = Poisson(d _λ_ ),


_x_<sup>_k_</sup> can be written as a linear combination of [ _x_ ]1 _,_ [ _x_ ]2 _, . . . ,_ [ _x_ ] _k_ .

**Corollary 7.3** (Method of Moments Adapted to Poisson) **.** _For positive integer-valued Xn, to prove Xn −→_ d Poisson( _λ_ ) _, it is enough to prove E_ [ _Xn_ ] _k → λk as n →∞, for all k._ Consider a counting RV _X_ =<sup>�</sup> _i_<sup>1(</sup><sup>_A_</sup> _i_<sup>)for events</sup><sup>_Ai_.[</sup><sup>_X_]</sup><sup>_k_= �</sup> ( _i_ 1 _,...,ik_ )<sup>1</sup><sup>_A_</sup> _i_ 1<sup>1</sup><sup>_A_</sup> _i_ 2<sup>_· · ·_1</sup><sup>_A_</sup> _ik_<sup>over ordered distinct</sup> ( _i_ 1 _, . . . , ik_ ). Then, _E_ [ _X_ ] _k_ =<sup>�</sup> ( _i_ 1 _,...,ik_ )<sup>_P_(</sup><sup>_Ai_</sup> 1<sup>_∩Ai_</sup> 2<sup>_∩· · · ∩Ai_</sup> _k_<sup>).</sup>

**Example 7.4.** Put _M_ balls at random (uniformly, independently) into _N_ boxes. Let _X_ = _XM,N_ be the number of empty boxes,<sup>�</sup><sup>_N_</sup> _i_ =1<sup>_Ai_,where</sup><sup>_Ai_istheevent“box</sup><sup>_i_isempty”.</sup>


Consider _N, M →∞_ in some way, and we want to prove _XN,M −→_ d Poisson( _e−c_ ). We must prove _E_ [ _X_ ] _k → e_<sup>_−ck_</sup> . Asymptotically, we want


This is true, provided _M_ = _o_ ( _N_<sup>2</sup> ). Hence, we want to show _N_ exp( _−M/N_ ) _→ e_<sup>_−c_</sup> , so we want to show log _N − M/N →−c_ . Rearranging,


Define _M_ = _MN_ by (7.2) and check that the argument works.

#### **7.2.1 Coupon Collector Problem**

Put balls uniformly independently into _N_ boxes. Let _LN_ be the number of balls until there are no empty boxes. _P_ ( _LN ≤ M_ ) = _P_ ( _XN,M_ = 0) because they are the same events. Under relation (7.2), the probability goes to exp( _−e_<sup>_−c_</sup> ) because _XN,M −→_ d Poisson( _e−c_ ). Then, _P_ ( _LN ≤ N_ log _N_ + _cN_ ) _→_ exp( _−e−c_ ), so

that is,


where _ξ_ has distribution function _P_ ( _ξ ≤ c_ ) = exp( _−e_<sup>_−c_</sup> ) for _−∞ < c < ∞_ . This is known as the **Gumbel distribution** .

_LECTURE 7. FEBRUARY 7_

30

### **7.3 Weak Convergence in Metric Spaces**

Recall the definition of a complete, separable metric space ( _S, d_ ). As an example, take R<sup>_k_</sup> , with


for _x_ = ( _x_ 1 _, . . . , xk_ ).

On R<sup>_k_</sup> , we have a partial order _x ≤ y ⇐⇒ xi ≤ yi_ , 1 _≤ i ≤ k_ . We can define a distribution function for R<sup>_k_</sup> -valued _X_ = ( _X_ 1 _, . . . , Xk_ ).


However, this is less useful than in one dimension.

**Theorem 7.5** (Portmanteau Theorem) **.** _On_ ( _S, d_ ) _, let µn,_ 1 _≤ n ≤∞ be PMs on_ ( _S, d_ ) _. The following are equivalent, and define weak convergence µn → µ∞. n→∞ (a)_ � _S_<sup>_f_d</sup><sup>_µn_</sup> _−−−−→_ � _S_<sup>_f_d</sup><sup>_µ∞forallboundedcontinuousf_:</sup><sup>_S→_R</sup><sup>_._</sup> _(b)_ lim sup _n µn_ ( _C_ ) _≤ µ∞_ ( _C_ ) _for all closed C. (c)_ lim inf _n µn_ ( _G_ ) _≥ µ∞_ ( _G_ ) _for all open G. (d) µn_ ( _A_ ) _→ µ∞_ ( _A_ ) _for all A such that µ∞_ ( _A_<sup>¯</sup> _\ A_<sup>0</sup> ) = 0 _. (This is the analog of continuity points.) (e) There exist S-valued RVs X_<sup>ˆ</sup> _n such that_ dist( _X_<sup>ˆ</sup> _n_ ) = _µn,_ 1 _≤ n ≤∞, and X_<sup>ˆ</sup> _n → X_<sup>ˆ</sup> _∞ a.s._

The hard part is = _⇒_ ( _e_ ), which is the Skorokhod Representation Theorem.

We will state analogs of R<sup>1</sup> results.

**Lemma 7.6** (Continuous Mapping Theorem) **.** _If Xn −→_ d _X∞, then f_ ( _Xn_ ) _−→_ d _f_ ( _X∞_ ) _for any f_ : _S → S′ such that P_ ( _X∞ ∈Df_ ) = 0 _, where Df_ = _{x ∈ S_ : _f is not continuous at x}._

**Theorem 7.7.** _For_ R<sup>_k_</sup> _-valued_ ( _Xn_ ) _, Xn −→_ d _X∞ if and only if Fn_ ( _x_ ) _→ F∞_ ( _x_ ) _for all continuity points x of F∞._

**Definition 7.8.** ( _Xn,_ 1 _≤ n < ∞_ ) is **tight** if for all _ε >_ 0, there exists a compact _Kε ⊆ S_ such that sup _n P_ ( _Xn ∈/ Kε_ ) _≤ ε_ .

In R<sup>_k_</sup> , ( _Xn,_ 1 _≤ n < ∞_ ) is tight if and only if _∀ε >_ 0 _∃Bε < ∞_ such that sup _n P_ ( _|Xn| ≥ Bε_ ) _≤ ε_ .

**Theorem 7.9** (Prohorov’s Theorem) **.** _(a) If Xn −→_ d _some X∞, then_ ( _Xn,_ 1 _≤ n < ∞_ ) _is tight. (b) If_ ( _Xn,_ 1 _≤ n < ∞_ ) _is tight, then there exists a subsequence Xnj −→_ d _some X∞._

See the section in Billingsley on Convergence of PMs.

## **Lecture 8**

---

[← February 2](08-february-2.md) · [Up: contents](index.md) · [February 9 →](10-february-9.md)
