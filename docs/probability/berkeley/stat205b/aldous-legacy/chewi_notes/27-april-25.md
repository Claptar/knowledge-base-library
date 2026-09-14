---
title: April 25
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# April 25

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **25.1 Martingale Central Limit Theorem**

Take standard Brownian motion ( _B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ). Given dist( _X_ ) with E _X_ = 0, there exists a stopping time _T_ such that _B_ ( _T_ ) =d _X_ , which implies E _T_ = E _X_ 2 = var( _X_ ). We can show E _T_ 2 _≤ c_ E _X_ 4 for constant _c_ .

**Theorem 25.1** (Martingale Embedding into BM) **.** _Take a MG_ 0 = _S_ 0 _, S_ 1 _, S_ 2 _, . . . . Then, there exists stopping times_ 0 = _T_ 0 _≤ T_ 1 _≤ T_ 2 _such that_ ( _S_ 0 _, S_ 1 _, S_ 2 _, . . ._ ) = (d _B_ ( _T_ 0) _, B_ ( _T_ 1) _, B_ ( _T_ 2) _, . . ._ ) _._

_Proof._ By induction on _k_ . Condition on ( _S_ 0 = 0 _, S_ 1 = _s_ 1 _, . . . , Sk_ = _sk_ ) (or condition on _Fk_ ). The conditional distribution of ( _Sk_ +1 _− Sk_ ) given _Fk_ is a mean-0 distribution. Apply the embedding to the conditional distribution and ( _B_ ( _Tk_ + _t_ ) _− B_ ( _Tk_ ) _, t ≥_ 0) to get _Tk_ +1 _− Tk_ = _T_<sup>ˆ</sup> _k_ .

Note: E[ _Tk_ +1 _− Tk | Fk_ ] = E[( _Sk_ +1 _− Sk_ )<sup>2</sup> _| Fk_ ] and


**Theorem 25.2** (Lindeberg-Feller CLT for Martingales) **.** _For each n, let_ ( _Xn,m, Fn,m, m_ = 0 _,_ 1 _, . . . , n_ ) _be a martingale difference sequence, that is,_ ( _Sn,m, Fn,m, m_ = 0 _,_ 1 _, . . . , n_ ) _is a MG, Sn,m_ =<sup>�</sup><sup>_m_</sup> _i_ =1<sup>_Xn,i,_</sup> _that is, Xn,m is Fn,m-measurable,_ E[ _Xn,m_ +1 _|Fn,m_ ] = 0 _. Write Vn,k_ =<sup>�</sup><sup>_k_</sup> _m_ =1<sup>E[</sup><sup>_X_</sup> _n,m_<sup>2</sup><sup>_|Fn,m−_1]</sup><sup>_.Suppose_</sup> _(i) Vn,nt −→_ P<sup>_tasn →∞,_0</sup><sup>_≤t ≤_1</sup><sup>_fixed(Vn,ntdefinedbylinearinterpolation),_</sup> _(ii)_<sup>�</sup><sup>_n_</sup> _m_ =1<sup>E[</sup><sup>_X_</sup> _n,m_<sup>21</sup> ( _|Xn,m|>ε_ )<sup>_| Fn,m−_1]</sup><sup>_−→_</sup> P<sup>0</sup><sup>_asn →∞._</sup> _Then,_ ( _Sn,nt,_ 0 _≤ t ≤_ 1) _−→_ d ( _B_ ( _t_ ) _,_ 0 _≤ t ≤_ 1) _as C_ [0 _,_ 1] _-valued random functions. In particular, Sn,n −→_ d Normal(0 _,_ 1) _._

_Outline Proof._ (See Durrett 3rd Edition).

We prove this under the stronger assumption _|Xn,m| ≤ εn_ , _εn ↓_ 0. For a single sequence ( _ξi, i ≥_ 1), then


so the stronger assumption is saying _|ξn| ≤ εn√n_ <u>.</u>

97

_LECTURE 25. APRIL 25_

98

If we stop the process if _Vn,·_ reaches 3 _/_ 2, take _εn <_ 1 _/_ 2, then we can assume _Vn,n ≤_ 2 by (i).

Regard the embedding ( _B_ ( _Tn,m_ ) _, m_ = 0 _,_ 1 _, . . . , n_ ) as the definition of ( _Sn,m, m_ = 0 _,_ 1 _, . . . , n_ ). So, ( _Sn,nt,_ 0 _≤ t ≤_ 1) =d ( _B_ ( _Tn,nt_ ) _,_ 0 _≤ t ≤_ 1). It is enough to show _Tn,nt −→_ P<sup>_t_as</sup><sup>_n→∞_(forfixed</sup><sup>_t_),and</sup> then use continuity of BM paths as in Donsker’s Theorem. Write _tn,m_ = _Tn,m − Tn,m−_ 1.


By orthogonality of the increments of the MDS _tn,m −_ E[ _Tn,m | Fn,m−_ 1],


### **25.2 The 3 Arcsine Laws**

The 3 arcsine RVs associated with ( _B_ ( _t_ ) _,_ 0 _≤ t ≤_ 1):


so


We know how to calculate these quantities since


From calculus, the density is


_Fact_ : The process ( _M_ ( _t_ ) _− B_ ( _t_ ) _,_ 0 _≤ t < ∞_ ) has the same distribution as ( _|B_ ( _t_ ) _|,_ 0 _≤ t < ∞_ ). This is different from the fact _M_ ( _t_ ) =d _|B_ ( _t_ ) _|_ , which holds for fixed _t_ .

The RV _L_ applied to ( _M_ ( _t_ ) _− B_ ( _t_ )) is some RV _L_<sup>ˆ</sup> applied to ( _B_ ( _t_ )).


_LECTURE 25. APRIL 25_

99

So, _L_<sup>ˆ</sup> also has the same arcsine density _fL_ ( _t_ ) at (25.2).

Rewrite: _ψ_ 2 : _C_ [0 _,_ 1] _→_ R, where


_ψ_ 2( _B_ ) has the arcsine density.

3. We considered (last class) _ψ_ 3( _t_ ) = Leb _{_ 0 _≤ t ≤_ 1 : _f_ ( _t_ ) _>_ 0 _}_ .

_Fact_ : _ψ_ 3( _B_ ) also has the arcsine density.

_History_ : The original proof is based on a combinatorial identity for a simple symmetric RW


The combinatorial identity is


Multiply by 1 _/n_ .


Rescale to


The LHS of (25.3) is close to _ψ_ 3( _Sn_<sup>_∗_)andtheRHSof(25.3)iscloseto</sup><sup>_ψ_2(</sup><sup>_S_</sup> _n_<sup>_∗_).As</sup><sup>_n→∞_,the</sup> differences converge in probability to 0. Donsker’s Theorem implies that


which implies _ψ_ 2( _B_ ) =d _ψ_ 3( _B_ ).

## **Lecture 26**

---

[← April 13](26-april-13.md) · [Up: contents](index.md) · [April 27 →](28-april-27.md)
