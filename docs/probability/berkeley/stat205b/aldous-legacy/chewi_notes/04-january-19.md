---
title: January 19
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# January 19

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **2.1 Conditions for Weak Convergence**

**Theorem 2.1** (Scheffe’s Theorem) **.** _Let θ_ ( _·_ ) _be a σ-finite measure on S. If hn, h_ : _S →_ [0 _, ∞_ ) _satisfy_ � _S_<sup>_hn_d</sup><sup>_θ_= 1</sup><sup>_,_</sup> � _S_<sup>_h_d</sup><sup>_θ_= 1</sup><sup>_,andhn_(</sup><sup>_s_)</sup><sup>_→h_(</sup><sup>_s_)</sup><sup>_θ-a.e.,then_</sup> � _S_<sup>_|hn_(</sup><sup>_s_)</sup><sup>_−h_(</sup><sup>_s_)</sup><sup>_|θ_(d</sup><sup>_s_)</sup><sup>_→_0</sup><sup>_._</sup>

**Proposition 2.2.** _Suppose_ ( _Xn,_ 1 _≤ n < ∞_ ) _and X are integer-valued. The following are equivalent: (a) Xn −→_ d _X. (b) P_ ( _Xn_ = _i_ ) _−−−−→n→∞ P_ ( _X_ = _i_ ) _, for all i. (c)_<sup>�</sup> _i_<sup>_|P_(</sup><sup>_Xn_=</sup><sup>_i_)</sup><sup>_−P_(</sup><sup>_X_=</sup><sup>_i_)</sup><sup>_| →_0</sup><sup>_._</sup>

_Proof._ ( _a_ ) = _⇒_ ( _b_ ): _P_ ( _Xn ≤ i_ + 1 _/_ 2) _→ P_ ( _X ≤ i_ + 1 _/_ 2). Then, _P_ ( _Xn_ = _i_ ) = _P_ ( _Xn ≤ i_ + 1 _/_ 2) _− P_ ( _Xn ≤ i −_ 1 _/_ 2) _→ P_ ( _X ≤ i_ + 1 _/_ 2) _− P_ ( _X ≤ i −_ 1 _/_ 2) = _P_ ( _X_ = _i_ ) _._ ( _b_ ) = _⇒_ ( _c_ ): Scheffe’s Theorem 2.1 for _θ_ ( _i_ ) _≡_ 1 for all _i_ , _hn_ ( _i_ ) = _P_ ( _Xn_ = _i_ ). ( _c_ ) = _⇒_ ( _a_ ):


**Proposition 2.3.** _If Xn and X have probability densities fn_ ( _x_ ) _and f_ ( _x_ ) _, if fn_ ( _x_ ) _→ f_ ( _x_ ) _for almost all x, then Xn −→_ d _X._

_Proof._ Scheffe’s Theorem 2.1:


7

_LECTURE 2. JANUARY 19_

8

### **2.2 Tight Distributions**

Consider R-valued ( _Xn,_ 1 _≤ n < ∞_ ).

**Definition 2.4.** Say ( _Xn_ ) is **tight** if lim _B↑∞_ sup _n P_ ( _|Xn| ≥ B_ ) = 0.

**Definition 2.5.** Say ( _Xn_ ) is **uniformly integrable** if lim _B↑∞_ sup _n E_ [ _|Xn|_ 1( _|Xn|≥B_ )] = 0.

Actually, the above definitions are properties of _µn_ = dist( _Xn_ ).

**Lemma 2.6** (Easy) **.** _(a) If_ sup _n E|Xn| < ∞, or more generally if_ sup _n Eφ_ ( _|Xn|_ ) _< ∞ for some_ 0 _≤ φ_ ( _x_ ) _↑∞ as x ↑∞, then_ ( _Xn_ ) _is tight. (b) If supnEXn_<sup>2</sup><sup>_<∞,ormoregenerallyif_sup</sup> _n_<sup>_Eφ_(</sup><sup>_|Xn|_)</sup><sup>_<∞forsome_0</sup><sup>_≤φ_(</sup><sup>_x_)</sup><sup>_↑∞suchthat_</sup> _φ_ ( _x_ ) _/x →∞ as x →∞, then_ ( _Xn_ ) _is UI._

_Proof._ (a) Markov’s inequality:


**Lemma 2.7** (205A) **.** _If Xn → X a.s., if_ ( _Xn,_ 1 _≤ n < ∞_ ) _is UI, then E|X| < ∞ and EXn → EX._

**Corollary 2.8.** _If Xn −→_ d _X, if_ ( _Xn,_ 1 _≤ n < ∞_ ) _is UI, then E|X| < ∞ and EXn → EX._

(Apply the lemma to _X_<sup>ˆ</sup> _n_ .)

Distribution functions _F_ , or equivalently, PMs _µ_ on ( _−∞, ∞_ ), satisfy:

- 0 _≤ F_ ( _x_ ) _≤_ 1, _∀x ∈_ ( _−∞, ∞_ ).

- _x �→ F_ ( _x_ ) is increasing.

- _F_ ( _x_ +) = _F_ ( _x_ ) (right-continuity).

- lim _x↑∞ F_ ( _x_ ) = 1, lim _x↓−∞ F_ ( _x_ ) = 0.

An **extended distribution function** (EDF) _F_ has the first three properties above.


There is a one-to-one correspondence between PMs _µ_ on [ _−∞, ∞_ ] and EDFs. Think of an RV _X_ with values in [ _−∞, ∞_ ].

**Theorem 2.9** (Helly’s Selection Theorem) **.** _Let F_ 1 _, F_ 2 _, . . . be distribution functions on_ ( _−∞, ∞_ ) _._

- _There exists nj →∞ and an EDF G such that Fnj_ ( _x_ ) _→ G_ ( _x_ ) _for all continuity points x of G._

- _• If_ ( _Fn,_ 1 _≤ n < ∞_ ) _is tight, then G is a distribution function on_ ( _−∞, ∞_ ) _._

_LECTURE 2. JANUARY 19_

9

Suppose _Z_ is standard Normal, with distribution function Φ( _z_ ). _J_ is uniform on _{_ 1 _,_ 2 _,_ 3 _}_ , and


Then, the distribution function of _Xn_ does not converge to a distribution function.

_Proof._ (a) Let _q_ 1 _, q_ 2 _, q_ 3 _, . . . ,_ be the rationals. The sequence _F_ 1( _q_ 1) _, F_ 2( _q_ 2) _, F_ 3( _q_ 3) _, . . ._ is in [0 _,_ 1] so (compactness) there exists a subsequence _m_ (1 _,_ 1) _, m_ (1 _,_ 2) _, m_ (1 _,_ 3) _, . . ._ such that


Then, we use a _diagonal argument_ . _Fm_ (1 _,i_ )( _q_ 2), _i_ = 1 _,_ 2 _, . . ._ is a sequence in [0 _,_ 1]; there exists a subsequence _m_ (2 _,_ 1) _, m_ (2 _,_ 2) _, m_ (2 _,_ 3) _, . . ._ such that _Fm_ (2 _,i_ )( _q_ 2) _→_ some _G_ 0( _q_ 2).

Repeat for each _k ≥_ 1: find a subsequence ( _m_ ( _k, i_ ) _, i ≥_ 1) of ( _m_ ( _k −_ 1 _, i_ ) _, i ≥_ 1) such that


Consider _m_ ( _i, i_ ) (the “diagonal”): this has the property _Fm_ ( _i,i_ )( _qk_ ) _−−−→i→∞_<sup>_G_0(</sup><sup>_qk_)for</sup><sup>_allk_.</sup>

Now, define an EDF _G_ by


Check that _G is_ an EDF.

Fix _x_ . For any _q > x_ ,


by letting _q ↓ x_ . By the same argument, lim inf _i Fm_ ( _i,i_ )( _x_ ) _≥ G_ ( _x−_ ). So, if _G_ ( _x_ ) = _G_ ( _x−_ ), then _Fm_ ( _i,i_ )( _x_ ) _→ G_ ( _x_ ).

(b) Tight implies that there exists _K_ ( _B_ ) such that lim sup _n P_ ( _Xn ≤ B_ ) _≥_ 1 _− K_ ( _B_ ), _K_ ( _B_ ) _↓_ 0 as _B ↑∞_ . Consider _Fm_ ( _i,i_ )( _q_ ) _→ G_ ( _q_ ) _∀q_ , which implies that _G_ ( _B_ ) _≥_ 1 _− K_ ( _B_ ), so _G_ puts 0 mass on + _∞_ .

**Corollary 2.10.** _Given_ ( _Xn,_ 1 _≤ n < ∞_ ) _and X (_ R _-valued RVs), suppose_ ( _Xn_ ) _is tight. Suppose that, whenever Xnj −→_ d _some Y as j →∞ for some_ ( _nj_ ) _, we have Y_ =d _X. Then, Xn −→_ d _X as n →∞._

_Proof._ By contradiction. If _Xn̸ → X_ in distribution, then there exists _x_ 0, a continuity point of _X_ , such that _P_ ( _Xn ≤ x_ 0) _̸ → P_ ( _X ≤ x_ 0). _∃ε >_ 0 and _mj →∞_ such that �� _P_ ( _Xnj ≤ x_ ) _− P_ ( _X ≤ x_ )�� _≥ ε_ for all _j_ . Apply Helly 2.9 to ( _Xnj_ ): there exists a subsequence _Xnj −→_ d some _Y_ . But _Y_ =d _X_ by hypothesis, so �� _P_ ( _Xnj ≤ x_ ) _− P_ ( _X ≤ x_ )�� _→_ 0, which is a contradiction.

_LECTURE 2. JANUARY 19_

10

**Lemma 2.11.** _Suppose EX_ = 0 _, EX_<sup>2</sup> = 1 _, and EX_<sup>4</sup> _≤ K. Then, there exists c_ ( _K_ ) _>_ 0 _, depending on K, such that P_ ( _X >_ 0) _≥ c_ ( _K_ ) _._

_Proof._ By contradiction. There exists _K_ such that the statement is false. So, there exists _Xn_ such that _EXn_ = 0, _EXn_<sup>2=1,</sup><sup>_EX_</sup> _n_<sup>4</sup><sup>_≤K_,but</sup><sup>_P_(</sup><sup>_Xn>_0)</sup><sup>_≤_1</sup><sup>_/n_.Helly2.9impliesthatthereexistsa</sup> subsequence _Xnj −→_ d some _X_ . So, _EX_ = 0, _EX_ 2 = 1, and _P_ ( _X >_ 0) = 0, which is impossible.

## **Lecture 3**

---

[← January 17](03-january-17.md) · [Up: contents](index.md) · [January 24 →](05-january-24.md)
