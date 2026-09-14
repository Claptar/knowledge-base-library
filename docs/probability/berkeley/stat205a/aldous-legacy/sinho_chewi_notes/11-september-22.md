---
title: September 22
source: https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf
source_file: sources/berkeley-stat205a/aldous-legacy/sinho_chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# September 22

**Source:** [`sinho_chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205A/sinho_chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **9.1 SLLN**

**Theorem 9.1** (Kolmogorov’s Maximal Inequality) **.** _Let_ ( _Xi,_ 1 _≤ i ≤ n_ ) _be independent, EXi_ = 0 _, and EXi_<sup>2</sup><sup>_< ∞.LetSm_= �</sup><sup>_m_</sup> _i_ =1<sup>_XiandS_</sup> _n_<sup>_∗_= max1</sup><sup>_≤m≤n|Sm|.Then_</sup>


_Comments_ :

1. Markov’s inequality gives


The theorem gives a stronger result.

2. Idea: There is a “first time” that something happens.

3. Martingale theory develops better notation.

_Proof._ Fix _x_ . Consider the event _{Sn_<sup>_∗≥x}_= �</sup><sup>_m_</sup> _k_ =1<sup>_Ak_,where</sup><sup>_Ak_=</sup><sup>_{|Sk| ≥x, |Si| < x,_all1</sup><sup>_≤i < k}_.</sup> The events _Ak_ are disjoint. Note that ( _Sk, Ak_ ) is independent of _Sn − Sk_ . _Sn − Sk_ depends on _Xk_ +1 _, Xk_ +2 _, . . . , Xn_ , while ( _Sk, Ak_ ) depends on ( _X_ 1 _, . . . , Xn_ ). Then, since _Sn_ = _Sk_ + ( _Sn − Sk_ ),


34

_LECTURE 9. SEPTEMBER 22_

35

because _Sk_ 1 _Ak_ and _Sn − Sk_ are independent, _E_ ( _Sn − Sk_ ) = 0, and _|Sk| ≥ x_ on _Ak_ .

“<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_xi_converges”meansthatlim</sup><sup>_N→∞_</sup> � _Ni_ =1<sup>_xi_existsandisfinite.TheCauchycriterionsaysthatthis</sup> is equivalent to sup _n≥K_ ��� _ni_ = _k_ +1<sup>_xi_</sup> �� _→_ 0 as _k →∞_ . “� _i∞_ =1<sup>_Xi_convergesa.s.”means</sup>


**Theorem 9.2.** _Let_ ( _Xi_ ) _be independent, with EXi_ = 0 _and σi_<sup>2= var(</sup><sup>_Xi_)</sup><sup>_< ∞.If_�</sup><sup>_∞_</sup> _i_ =1<sup>_σ_</sup> _i_<sup>2</sup><sup>_< ∞,then_</sup> � _∞i_ =1<sup>_Xiconvergesa.s._</sup>


which shows that<sup>�</sup><sup>_∞_</sup> _i_ =1<sup>_Xi_isfinitea.s.Thisargumentisincorrectbecause</sup><sup>_apriori_,wedonotknowthat</sup> we have a convergent random variable.

_Exercise_ . Knowing 9.2, show (9.1).

_Proof._ Define _Mk_ = sup _n>k_ ��� _ni_ = _k_ +1<sup>_Xi_</sup> ��. It is enough to show that _Mk →_ 0 a.s. as _k →∞_ . Define also _Wk_ = sup _n_ 2 _>n_ 1 _>k_ ��� _ni_ =2 _n_ 1+1<sup>_Xi_</sup> �� and note that _Mk ≤ Wk ≤_ 2 _Mk_ and _Wk_ decreases as _k_ increases.


Taking _N →∞_ , _P_ ( _Mk > ε_ ) _≤ ε_<sup>_−_2 �</sup><sup>_∞_</sup> _i_ =1<sup>_σ_</sup> _i_<sup>2.</sup>

Taking _k →∞_ , then _Wk ↓ W∞_ for some _W∞_ a.s. Then _P_ ( _W∞ > ε_ ) = 0, which implies that _W∞_ = 0 a.s., which implies that _Wk ↓_ 0 a.s. and _Mk →_ 0 a.s.

**Lemma 9.3** (Deterministic Lemma (Kronecker)) **.** _Let_ ( _xn_ ) _be a sequence of reals, Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_xi,_</sup> 0 _< an ↑∞ as n ↑∞. If_<sup>�</sup> _i_<sup>_xi/aiconverges,thenSn/an→_0</sup><sup>_._</sup>

_Proof._ Exercise/Textbook.

**Corollary 9.4.** _Let_ ( _Xi_ ) _be independent, EXi_ = 0 _, EXi_<sup>2</sup><sup>_<∞,andSn_=�</sup><sup>_n_</sup> _i_ =1<sup>_Xi.If_0</sup><sup>_<an↑∞as_</sup> _n ↑∞ and if_<sup>�</sup> _n_<sup>_EX_</sup> _n_<sup>2</sup><sup>_/a_2</sup> _n_<sup>_< ∞,thenSn/an→_0</sup><sup>_a.s._</sup>

_Proof._ 9.2 implies that<sup>�</sup> _n_<sup>_Xn/an_convergesa.s.Then9.3impliesthat</sup><sup>_Sn/an→_0a.s.</sup>

_Specialization_ . Suppose also that _EXn_<sup>2</sup><sup>_∼cn_2</sup><sup>_α_,</sup><sup>_α>_0.Take</sup><sup>_a_2</sup> _n_<sup>=</sup><sup>_n_1+2</sup><sup>_α_+2</sup><sup>_ε_(</sup><sup>_ε>_0issmall).Then9.4</sup> implies that _Sn/n_<sup>1</sup><sup>_/_2+</sup><sup>_α_+</sup><sup>_ε_</sup> _→_ 0 a.s.

_Specialization_ . Suppose that sup _n EXn_<sup>2</sup><sup>_< ∞_.Take</sup><sup>_a_2</sup> _n_<sup>=</sup><sup>_n_(log</sup><sup>_n_)1+</sup><sup>_ε_.Then 9.4 implies that</sup><sup>_Sn/_</sup> � _n_ log<sup>1+</sup><sup>_ε_</sup> _n →_ 0 a.s. We know implicitly from the CLT that if ( _Xi_ ) are IID, then _Sn/_<sup>_√_</sup> _<u>n</u> →_ 0 a.s. is **not** true. The law of iterated logarithm gives the proper borderline.

_LECTURE 9. SEPTEMBER 22_

36

**Theorem 9.5** (SLLN) **.** _Let_ ( _Xi_ ) _be IID with E|X| < ∞. Then Sn/n → EX a.s. as n →∞._

_Proof._ The idea is to truncate, center, and then apply 9.4.

If _Z ≥_ 0, then


Define _Yk_ = _Xk_ 1( _|Xk|≤k_ ). Then

Then the First Borel-Cantelli Lemma implies that _P_ ( _Yk_ = _Xk,_ ultimately) = 1. It is enough to prove that (1 _/n_ )<sup>�</sup><sup>_n_</sup> _k_ =1<sup>_Yk→EX_a.s.</sup>


_Claim_ : _G_ ( _y_ ) _≤_ 4, for all 0 _< y < ∞_ . Since _G_ ( _y_ ) _≤_<sup>�</sup> _k_<sup>1</sup><sup>_/k_2</sup><sup>_≤_2for</sup><sup>_y≤_1,thisistruefor</sup><sup>_y≤_1.Take</sup> _y >_ 1.

so

Since _y >_ 1,


(by a picture). Then


as _i →∞_ . By dominated convergence, (1 _/n_ )<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_EYi −EX_)</sup><sup>_→_0a.s.Addthetwoequationstoget</sup> (1 _/n_ )<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_Yi −EX_)</sup><sup>_→_0a.s.,whichimpliesthat(1</sup><sup>_/n_) �</sup><sup>_n_</sup> _i_ =1<sup>_Yi→EX_a.s.</sup>

## **Lecture 10**

---

[← September 20](10-september-20.md) · [Up: contents](index.md) · [September 27 →](12-september-27.md)
