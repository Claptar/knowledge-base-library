---
title: September 1
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 1

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Take the case of _S_ = _{_ 0 _,_ 1 _,_ 2 _, . . . }_ and _S_ = all subsets of _S_ .


Define, for _A ⊂ S_ , _µ_ ( _A_ ) =<sup>�</sup> _i∈A_<sup>_pi_.This</sup><sup>_µ_isaprobabilitymeasure(PM).</sup> _•_ Given a PM _µ_ on this _S_ , define _pi_ = _µ_ ( _{i}_ ) and (3.1) holds.

Consider a set _S_ and let _A_ and _C_ denote classes of subsets of _S_ .

Call _A_ a _π_ -class if _A_ 1 _, A_ 2 _∈A_ = _⇒ A_ 1 _∩ A_ 2 _∈A_ .

Call _C_ a _λ_ -class if

1. _S ∈C_ 2. If _A, B ∈C_ , if _A ⊂ B_ , then _B \ A ∈C_ .

3. If _An ∈C_ , if _An ↑ A_ , then _A ∈C_ .

**Lemma 3.1** (Dynkin’s _π_ - _λ_ Class Lemma) **.** _If C is a λ-class, if A is a π-class, and if C ⊇A, then C ⊇ σ_ ( _A_ ) _._

_Proof._ See text for proof.

**Lemma 3.2** (Identification Lemma for PMs) **.** _If µ_ 1 _and µ_ 2 _are PMs on_ ( _S, S_ ) _, if µ_ 1( _A_ ) = _µ_ 2( _A_ ) _∀A ∈A, if A is a π-class, and if S_ = _σ_ ( _A_ ) _, then µ_ 1 = _µ_ 2 _(µ_ 1( _B_ ) = _µ_ 2( _B_ ) _∀B ∈S)._

10

_LECTURE 3. SEPTEMBER 1_

11

_Proof._ Consider the collection _C_ def= _{A_ : _µ_ 1( _A_ ) = _µ_ 2( _A_ ) _}_ , so _C ⊇A_ by hypothesis. To apply 3.1, we only need to check _C_ is a _λ_ -class (clear from the definition of a PM).

- **Theorem 3.3.** _• There exists a σ-finite measure λ on_ (R<sup>1</sup> _, B_<sup>1</sup> ) _such that λ_ ([ _a, b_ ]) = _b − a for all −∞ < a < b < ∞. This is the_ **_Lebesgue measure on_** R _(“length”)._

   - _There exists a PM λ_ 1 _on_ [0 _,_ 1] _such that λ_ 1([ _a, b_ )) = _b − a for all_ 0 _≤ a ≤ b ≤_ 1 _. This is the_ **_Lebesgue measure on_** [0 _,_ 1] _or the_ **_uniform distribution on_** [0 _,_ 1] _._

_Proof._ See text for proof.

Consider _f_ : ( _S_ 1 _, S_ 1) _→_ ( _S_ 2 _, S_ 2), a measurable function. We know that for _B ∈S_ 2, _f_<sup>_−_1</sup> ( _B_ ) _∈S_ 1. Given a PM _µ_ on ( _S_ 1 _, S_ 2), we can define a PM _µ_ ˆ on ( _S_ 2 _, S_ 2) by


This _µ_ ˆ is a PM because _f_<sup>_−_1</sup> commutes with Boolean operations.

### **3.2 Probability Measures on** R<sup>1</sup>

Given a PM _µ_ on R, define _F_ ( _x_ ) = _µ_ (( _−∞, x_ ]). This _F_ has the properties

- increasing: _x_ 1 _≤ x_ 2 = _⇒ F_ ( _x_ 1) _≤ F_ ( _x_ 2)

- right-continuous: if _xn ↓ x_ , then _F_ ( _xn_ ) _↓ F_ ( _x_ )

- lim _x→∞_ = 1 and lim _x→−∞ F_ ( _x_ ) = 0

A function _F_ with these properties is called a **distribution function** .

**Theorem 3.4.** _Given a distribution function F , there exists a unique PM µ such that_


_Undergraduate Version_ . Take _U_ a RV Uniform[0 _,_ 1]. Then _F_<sup>_−_1</sup> ( _U_ ) is a RV with distribution function _F_ .

Define _G_ (a version of _F_<sup>_−_1</sup> ):


_G_ is increasing, so _G_ is measurable. For each _x_ :


The “push-forward” lemma says that there exists a PM _µ_ ˆ on R such that


### **3.3 Coin-Tossing Space**

Take a 2-element set _B_ = _{H, T }_ or _{_ 0 _,_ 1 _}_ .

The infinite product space _B_<sup>_∞_</sup> = _B_<sup>N</sup> is the set of all **b** = ( _b_ 1 _, b_ 2 _, b_ 3 _, . . ._ ), _bi ∈ B_ . Given a finite string _π_ = ( _π_ 1 _, . . . , πn_ ), _πi ∈ B_ , the length is _n_ = _|π|_ .

Set _Aπ ⊆ B_<sup>_∞_</sup> , where _Aπ_ = _{_ **b** : ( _b_ 1 _, . . . , b|π|_ ) = ( _π_ 1 _, . . . , π|π|_ ) _}_ .

Define a _σ_ -field _B_<sup>_∞_</sup> on _B_<sup>_∞_</sup> as _σ_ (all _Aπ_ ; _π_ a finite string).

_LECTURE 3. SEPTEMBER 1_

12


_Conceptual Point_ . This theorem is equivalent to the theorem that _λ_ 1 exists.

The binary expansion of real _x ∈_ (0 _,_ 1) (for example, _x_ = 0 _._ 110110010001 _. . ._ ) is given by


The function _x �→ bi_ ( _x_ ) is measurable.

Define _g_ : [0 _,_ 1] _→ B_<sup>_∞_</sup> by _g_ ( _x_ ) = ( _b_ 1( _x_ ) _, b_ 2( _x_ ) _, . . ._ ). It is easily checked that _g_ is measurable. Use the push-forward lemma to set a PM _µ_ on _B_<sup>_∞_</sup> with


for some _k_ , if _|π|_ = _n_ .

Given _µ_ on _B_<sup>_∞_</sup> , define _h_ : _B_<sup>_∞_</sup> _→_ [0 _,_ 1] by


The push-forward is _λ_ 1.

## **Lecture 4**

---

[← August 30](04-august-30.md) · [Up: contents](index.md) · [September 6 →](06-september-6.md)
