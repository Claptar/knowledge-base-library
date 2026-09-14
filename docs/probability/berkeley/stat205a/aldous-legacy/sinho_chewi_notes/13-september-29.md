---
title: September 29
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 29

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **11.1 Miscellaneous Measure Theory Related Topics**

#### **11.1.1 Kolgomorov’s** 0 **-** 1 **Law**

**Theorem 11.1** (Kolmogorov’s 0-1 Law) **.** _Consider X_ 1 _, X_ 2 _, . . . mapping onto any range space. Define τn_ = _σ_ ( _Xn, Xn_ +1 _, Xn_ +2 _, . . ._ ) _and_<sup>�</sup> _n≥_ 1<sup>_τn_=</sup><sup>_τ(the“tailσ-field”).If_(</sup><sup>_X_1</sup><sup>_, X_2</sup><sup>_, . . ._)</sup><sup>_areindependent,_</sup> _then A ∈ τ implies that P_ ( _A_ ) _is_ 0 _or_ 1 _, that is, τ is a trivial σ-field._

_Note_ . lim sup _n Xn_ is _τn_ -measurable for all _n_ , so it is _τ_ -measurable.

_Proof._ Define _Fn−_ 1 = _σ_ ( _X_ 1 _, . . . , Xn−_ 1). _Fn−_ 1 is independent of _τn_ , which implies that _Fn−_ 1 is independent of _τ_ , which implies that the field<sup>�</sup> _n_<sup>_Fn_isindependentof</sup><sup>_τ_.</sup> By the _π_ - _λ_ Lemma, _σ_ (<sup>�</sup> _Fn_ ) = _σ_ ( _X_ 1 _, X_ 2 _, . . ._ ) is independent of _τ_ , which implies that _τ_ is independent of _τ_ . Then, _A ∈ τ_ implies that _P_ ( _A ∩ A_ ) = _P_ ( _A_ ) _P_ ( _A_ ) = _P_ ( _A_ ). _x_<sup>2</sup> = _x_ implies that _x_ = 0 or 1.

**Lemma 11.2.** _If A is a trivial σ-field, and if X, a RV that takes on values in_ [ _−∞, ∞_ ] _, is A-measurable, then there exists x_ 0 _such that P_ ( _X_ = _x_ 0) = 1 _._

_Proof._ Define _x_ 0 = inf _{x_ : _P_ ( _X ≤ x_ ) = 1 _}_ . For the case where _x_ 0 _∈_ ( _−∞, ∞_ ), then _P_ ( _X ≤ x_ 0 + _ε_ ) = 1 and _P_ ( _X ≤ x_ 0 _− ε_ ) = 0 for all _ε_ .

#### **11.1.2 “Modes of Convergence” for** R **-Valued RVs**

_Xn −−→a.s. X_ means _P_ ( _ω_ : _Xn_ ( _ω_ ) _→ X_ ( _ω_ )) = 1.

_Xn −→P X_ means _P_ ( _|Xn − X| > ε_ ) _→_ 0 as _n →∞_ , for all _ε >_ 0.

_L_<sup>_p_</sup> _Xn −→ X_ means that _E|Xn − X|_<sup>_p_</sup> _→_ 0 and sup _n E|Xn|_<sup>_p_</sup> _< ∞_ ( _∞ > p ≥_ 1).

Facts:

- _L_<sup>_p_</sup>

- 1. We showed before that _−→_ implies _−→P_ , but not conversely.

2. _−−→a.s._ implies _−→P_ , but not conversely.

**Example 11.3.** Let _U_ be uniform on [0 _,_ 1]. Let _Xn_ = _n_ 1( _U ≤_ 1 _/n_ ). Then _Xn −→P_ 0, but _EXn_ = 1, so _Xn →_ 0 in _L_<sup>1</sup> is false.

41

_LECTURE 11. SEPTEMBER 29_

42

If _Xn −−→a.s. X_ , since _P_ ( _An_ inf. often) _≥_ lim sup _n P_ ( _An_ ),

0 = _P_ ( _|Xn − X| ≥ ε_ inf. often) _≥_ lim sup _P_ ( _|Xn − X| ≥ ε_ ) = 0 _n_

which implies that _Xn → X_ in probability.

**Example 11.4.** Take independent events ( _An_ ) with _P_ ( _An_ ) _→_ 0, which implies that 1 _An →_ 0 in probability.<sup>�</sup> _n_<sup>_P_(</sup><sup>_An_)=</sup><sup>_∞_implies,bytheSecondBorel-CantelliLemma,that</sup><sup>_P_(</sup><sup>_An_inf.often)=1,</sup> which implies that 1 _An →_ 0 a.s. is false.

Recall the Dominated Convergence Theorem (DCT): If _Xn → X_ a.s., if _∃Y ≥_ 0 with _EY < ∞_ , and _|Xn| ≤ Y_ for all _n_ , then _E|Xn − X| →_ 0 and _EXn → EX_ .

**Lemma 11.5.** _If Xn −→P X, then there exists a subsequence, n_ 1 _< n_ 2 _< n_ 3 _< · · · such that Xnj −−→a.s. X as j →∞._

_Proof._ Choose _nj_ inductively.


Then<sup>�</sup> _j_<sup>_P_(</sup><sup>_|Xn −X|≥_2</sup><sup>_−j_)</sup><sup>_<∞_.TheFirstBorel-CantelliLemmaimpliesthat</sup> �� _Xnj − X_ �� _≤_ 2 _−j_ , ultimately in _j_ , a.e., which implies that _Xnj → X_ a.s.

_Aside_ . The result is related to the fact that “a.s. convergence” is not convergence in a metric.

**Corollary 11.6.** _The DCT remains true under the assumption that Xn → X in probability._

_Proof._ Suppose that the statement is false: _∃ε >_ 0 and a subsequence _m_ 1 _< m_ 2 _< m_ 3 _< · · ·_ such that _E_ �� _Xmj − X_ �� _≥ ε ∀j_ . Now _Xmj → X_ in probability, so 11.5 implies that there exists a subsequence ( _nj_ ) of ( _mj_ ) such that _Xnj → X_ a.s. and _E_ �� _Xnj − X_ �� _≥ ε ∀j_ . This contradicts the DCT.

This proof uses the “subsequence trick”.

_Exercise_ . Obvious: If _f_ is continuous, _Xn → X_ a.s. implies that _f_ ( _Xn_ ) _→ f_ ( _X_ ) a.s. Less obvious: If _f_ is continuous, _Xn → X_ in probability implies that _f_ ( _Xn_ ) _→ f_ ( _X_ ) in probability. (This can be proven with the subsequence trick.)

#### **11.1.3 Radon-Nikodym Derivative**

There are two views of integration in calculus.

1. Given _f, a, b_ , then � _ab_<sup>_f_(</sup><sup>_x_) d</sup><sup>_x_isanumber.</sup> 2.


Integration is an operation _f �→ F_ , which is the opposite of _F �→ F_<sup>_′_</sup> .

In MT, given a PM _µ_ , integration is a map _h �→ I_ ( _h_ ) = � _h_ d _µ_ . The analog in MT involves _measures_ , not functions.

_LECTURE 11. SEPTEMBER 29_

43

Take a measurable space ( _S, S_ ). Fix a _σ_ -finite measure _µ_ on ( _S, S_ ). Consider a measurable _h_ : _S →_ [0 _, ∞_ ). For _A ∈S_ , define _ν_ ( _A_ ) = � _A_<sup>_h_d</sup><sup>_µ ≤∞_.</sup>

_Claim_ . _ν_ is a _σ_ -finite measure on ( _S, S_ ).

The fact that _µ_ is _σ_ -finite implies that there exists _An ↑ S_ , with _µ_ ( _An_ ) _< ∞_ . Define _Bn_ = _An∩{s_ : _h_ ( _s_ ) _≤ n}_ . Then _Bn ↑ S_ and _ν_ ( _Bn_ ) _≤ nµ_ ( _An_ ) _< ∞_ .

The two measures _ν_ and _µ_ have a relationship. For all _A_ , if _µ_ ( _A_ ) = 0, then _ν_ ( _A_ ) = 0. This property has a name: _ν_ is **absolutely continuous** with respect to _µ_ , denoted _ν ≪ µ_ .

**Theorem 11.7** (Radon-Nikodym Theorem) **.** _If µ and ν are σ-finite measures on_ ( _S, S_ ) _, if ν ≪ µ, then there exists a measurable h_ : _S →_ [0 _, ∞_ ) _such that ν_ ( _A_ ) = � _A_<sup>_h_d</sup><sup>_µ ∀A ∈S._</sup>

_Notation_ . Write


and


and call _h_ =<sup>d</sup><sup>_ν_</sup> d _µ_<sup>theRadon-Nikodym</sup><sup>**density**of</sup><sup>_ν_withrespectto</sup><sup>_µ_.</sup>

d _<u>µ</u>_ In particular, if _µ_ is a probability measure on R<sup>1</sup> and if _µ ≪_ Leb, then _h_ = dLeb<sup>exists (the density function,</sup> e.g. Normal, Exponential, etc.).

_Proof of Radon-Nikodym._ See the MT text. We will prove this via martingales later.

#### **11.1.4 Probability Measures on** R

We know there is a 1-1 correspondence between probability measures _µ_ and distribution functions _F_ .


- “ _x_ is an **atom** of _µ_ ” means that _µ_ ( _{x}_ ) _>_ 0. _µ_ can have only countably many atoms.

There are three basic types of PMs _µ_ :

1. _µ ≪_ Leb, so it can be described by its density _f_ .


Here, _f_ can be any measurable function with _f ≥_ 0 and � _−∞∞_<sup>_f_(</sup><sup>_x_) d</sup><sup>_x_= 1.</sup>

2. _µ_ is **purely atomic** if there exists a countable set of atoms _x_ 1 _, x_ 2 _, . . ._ and<sup>�</sup> _i_<sup>_µ_(</sup><sup>_{xi}_)=1,which</sup> implies that _µ_ (R _\ ∪i{xi}_ ) = 0 (discrete).

3. **Singular measures** : there exists _A_ such that Leb( _A_ ) = 0, _µ_ ( _A_ ) = 1, but there are no atoms.

Take _x ∈_ [0 _,_ 1] with a binary expansion, e.g. 0 _._ 10110100011 _. . ._ . Say that _bi_ ( _x_ ) is the _i_ th digit of the binary expansion of _x_ ( _⌊_ 2<sup>_i_</sup> _n⌋_ mod 2), which defines a map from [0 _,_ 1] to _B_<sup>_∞_</sup> . Next, map to _{_ 0 _,_ 1 _,_ 2 _}_<sup>_∞_</sup> by converting 1s to 2s, and then map back to [0 _,_ 1] by interpreting the result base 3, to obtain<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>3</sup><sup>_−i_(2</sup><sup>_bi_(</sup><sup>_x_)).Putting</sup> these together yields a measurable map _H_ : [0 _,_ 1] _→_ [0 _,_ 1]. Take _U_ to be Uniform[0 _,_ 1]. What is the distribution of _H_ ( _U_ )?

_LECTURE 11. SEPTEMBER 29_

44

_F_ ( _x_ ) = _P_ ( _H_ ( _U_ ) _≤ x_ ) is the **Cantor function** , which is continuous. The set of possible values of _H_ is “the base-3 expansion has no “1”” is the **Cantor set** , _C_ , and Leb( _C_ ) = 0 while _P_ ( _H_ ( _U_ ) _∈ C_ ) = 1.

The distribution of _H_ ( _U_ ) is called the “uniform distribution on the Cantor set”.

_Fact_ . Any PM _µ_ on R<sup>1</sup> has a unique decomposition


where _ai ≥_ 0, _a_ 1 + _a_ 2 + _a_ 3 = 1.

## **Lecture 12**

---

[← September 27](12-september-27.md) · [Up: contents](index.md) · [October 4 →](14-october-4.md)
