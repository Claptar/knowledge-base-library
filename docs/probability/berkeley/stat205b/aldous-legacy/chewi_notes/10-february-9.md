---
title: February 9
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 9

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **8.1 Characteristic Functions in** R<sup>_k_</sup>

For _t ∈_ R<sup>_k_</sup> , _x ∈_ R<sup>_k_</sup> , _t · x_ =<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_tixi_.</sup> _X_ = ( _X_ 1 _, . . . , Xk_ ) is a R<sup>_k_</sup> -valued RV. _t · X_ =<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_tiXi_isaR1-valuedRV.</sup>

The CF of _X_ is a function _φ_ ( _t_ ) = _E_ exp( _it · X_ ) as a function from R<sup>_k_</sup> to C.

The Uniqueness and Continuity Theorems are the same as in R<sup>1</sup> (see the Billingsley textbook).

**Theorem 8.1.** _Let X_<sup>(</sup><sup>_n_)</sup> _, n ≥_ 1 _, be_ R<sup>_k_</sup> _-valued RVs. Suppose φX_ ( _n_ )( _t_ ) _→ some limit φ_ ( _t_ ) _∀t ∈_ R<sup>_k_</sup> _. If either (i)_ ( _X_<sup>(</sup><sup>_n_)</sup> _, n ≥_ 1) _is tight, or (ii) φ is a CF, then X_<sup>(</sup><sup>_n_)</sup> _−→_ d _X, where X has CF φ._

**Theorem 8.2** (Cram´er-Wold Device) **.** _Let_ ( _X_<sup>(</sup><sup>_n_)</sup> ) _be_ R<sup>_k_</sup> _-valued RVs. Suppose t · X_<sup>(</sup><sup>_n_)</sup> _−→_ d _some Wt (convergence in_ R<sup>1</sup> _) as n →∞, for all t ∈_ R<sup>_k_</sup> _. If either (i)_ ( _X_<sup>(</sup><sup>_n_)</sup> _, n ≥_ 1) _is tight, or (ii) ∃X such that t · X_ =d _Wt ∀t ∈_ R _k. Then, X_<sup>(</sup><sup>_n_)</sup> _−→_ d _X, where t · X_ =d _Wt ∀t._

_Proof._

_φX_ ( _n_ )( _t_ ) = _E_ exp( _it · X_<sup>(</sup><sup>_n_)</sup> ) _→ E_ exp( _iWt_ ) def= _φ_ ( _t_ )

Under (i), 8.1 implies that _X_<sup>(</sup><sup>_n_)</sup> _−→_ d some _X_ . We know that _t · X_ ( _n_ ) _−→_ d _Wt_ . By the Continuous Mapping Theorem, _t · X_ =d _Wt_ . Under (ii), _φ_ ( _t_ ) = _E_ exp( _it · X_ ), and so is a CF. Apply (ii) of 8.1.

31

_LECTURE 8. FEBRUARY 9_

32

**Corollary 8.3.** _To show X_<sup>(</sup><sup>_n_)</sup> _−→_ d _X in_ R _k, it is enough to show E_<sup>�</sup> _kj_ =1<sup>_fj_(</sup><sup>_X_</sup> _j_<sup>(</sup><sup>_n_)</sup> ) _→ E_<sup>�</sup><sup>_k_</sup> _j_ =1<sup>_fj_(</sup><sup>_Xj_)</sup><sup>_for_</sup> _all bounded, continuous fj_ : R _→_ R _._

_Proof._ This extends to _fj_ : R _→_ C. However, _x �→ e_<sup>_it·x_</sup> _≡_<sup>�</sup><sup>_n_</sup> _j_ =1<sup>_eitjxj_isofthismultiplicativeform.So,</sup> we have _E_ exp( _it · X_<sup>(</sup><sup>_n_)</sup> ) _→ E_ exp( _it · X_ ) _∀t ∈_ R<sup>_k_</sup> .

### **8.2 Central Limit Theorem in** R<sup>_k_</sup>

**Theorem 8.4** (IID CLT in R<sup>_k_</sup> ) **.** _Consider X,_ R<sup>_k_</sup> _-valued, EX_ = 0 _. Let E_ [ _XjXℓ_ ] = Γ _j,ℓ < ∞ (_ Γ _is the covariance matrix). Let X_<sup>(</sup><sup>_n_)</sup> _be IID copies of X, S_<sup>(</sup><sup>_n_)</sup> =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_X_(</sup><sup>_i_)</sup><sup>_,_R</sup><sup>_k-valued,ES_(</sup><sup>_n_)=0</sup><sup>_.Then_</sup> _n_<sup>_−_1</sup><sup>_/_2</sup> _S_<sup>(</sup><sup>_n_)</sup> _−→_ d _Y , where Y has CF_


_Proof._


_E_ �� _n−_ 1 _/_ 2 _S_ ( _n_ )��2 = _E|X|_ 2, so ( _n−_ 1 _/_ 2 _S_ ( _n_ ) _, n ≥_ 1) is tight in R _k_ . To apply Cram´er-Wold 8.2, we need to show _t ·_ ( _n_<sup>_−_1</sup><sup>_/_2</sup> _S_<sup>(</sup><sup>_n_)</sup> ) _−→_ d some _Wt_ .


by the 1-dimensional CLT, since

and


**Definition 8.5.** A R<sup>_k_</sup> -valued _Y_ has Normal(0 _,_ Γ) distribution if its CF is (8.1).

Let _A_ be an arbitrary non-random _k×k_ matrix. Let _Z_ = ( _Z_ 1 _, Z_ 2 _, . . . , Zk_ ) have IID Normal(0 _,_ 1) components. Consider _Y_ = _AZ_ , _Yi_ =<sup>�</sup> _j_<sup>_Ai,jZj_.</sup>


_LECTURE 8. FEBRUARY 9_

33


This says _Y_ has Normal(0 _, AA_<sup>_⊤_</sup> ) distribution.

_Check_ : _t · Y_ is Normal.

**Proposition 8.6.** _For a k × k matrix_ Γ _, the following are equivalent:_

_1._ Γ = _AA_<sup>_⊤_</sup> _for some A._

_2. The_ Normal(0 _,_ Γ) _distribution exists, and can be constructed as AZ for Z_ = ( _Z_ 1 _, . . . , Zk_ ) _IID_ Normal(0 _,_ 1) _and for A as in 1._

_3._ Γ _is the covariance matrix of some X with EX_ = 0 _._

_4._ Γ _is symmetric and non-negative definite: t_<sup>_⊤_</sup> Γ _t ≥_ 0 _∀t._

_Proof._ 1 = _⇒_ 2: We already proved this. 2 = _⇒_ 3: Specialization. 3 = _⇒_ 4: _t_<sup>_⊤_</sup> Γ _t_ is var( _t · X_ ). 4 = _⇒_ 1 is matrix theory. Γ = _U_<sup>_⊤_</sup> _DU_ = _U_<sup>_⊤_</sup> _D_<sup>1</sup><sup>_/_2</sup> _D_<sup>1</sup><sup>_/_2</sup> _U_ = _AA_<sup>_⊤_</sup>

for _U_ orthonormal, _D_ diagonal, _D ≥_ 0.

The CLT 8.4 gives 3 = _⇒_ 2.

### **8.3 Weak Convergence in** R<sup>_k_</sup>

**Example 8.7** (Artificial Example) **.** Consider a probability measure on the unit square which is uniform on parallel diagonal lines. _U_ is uniform on [0 _,_ 1], _Xn_ = _U_ ,


_Simple Facts_ . For R-valued _X_ s and _Y_ s, a statement like


is a statement about weak convergence on R<sup>2</sup> . Consider


_LECTURE 8. FEBRUARY 9_

34

**Continuous Mapping Theorem** . If ( _Xn, Yn_ ) _−→_ d ( _X, Y_ ), then _g_ ( _Xn, Yn_ ) _−→_ d _g_ ( _X, Y_ ) for continuous _g_ . ( _x, y_ ) _�→ x_ is continuous.

Not conversely!

So, ( _Xn, Yn_ ) _−→_ d ( _X, Y_ ) implies _Xn_ + _Yn −→_ d _X_ + _Y_ , _Xn/Yn −→_ d _X/Y_ provided _P_ ( _Y_ = 0) = 0.

**Lemma 8.8.** _Suppose Xn −→_ d _X and Yn −→_ d _Y . If either (i) P_ ( _Y_ = _y_ 0) = 1 _for some y_ 0 _, or (ii) Xn and Yn are independent (each n), then_ ( _Xn, Yn_ ) _−→_ d ( _X, Y_ ) _, where X and Y are independent._

**Example 8.9** (Artificial Example) **.** ID and pairwise independence are _not_ enough for the CLT.


Take _ξ_ 0 _, ξ_ 1 _, ξ_ 2 _, . . ._ , IID, _P_ ( _ξ_ = 1) = 1 _/_ 2 = _P_ ( _ξ_ = _−_ 1). Define _Xn_ = _ξ_ 0 � _i_ : _bi_ ( _n_ )=1<sup>_ξi_,</sup><sup>_n≥_0.</sup><sup>_Xn_takes</sup> values _{±_ 1 _}_ . Check that the ( _Xn_ ) are pairwise independent.


_ES_ = 0, var( _S_ ) = 2<sup>_j_</sup> . Then, _P_ ( _S_ = 2<sup>_j_</sup> ) = _P_ ( _S_ = _−_ 2<sup>_j_</sup> ) = (1 _/_ 2)2<sup>_−j_</sup> , and _S_ = 0 otherwise. 2<sup>_−j/_2</sup> _S_ does not converge to Normal(0 _,_ 1).

## **Lecture 9**

---

[← February 7](09-february-7.md) · [Up: contents](index.md) · [February 14 →](11-february-14.md)
