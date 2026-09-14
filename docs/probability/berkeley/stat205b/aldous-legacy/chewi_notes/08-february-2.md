---
title: February 2
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# February 2

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **6.1 Lindeberg Theorem**

Restatement of the Lindeberg Theorem without prior rescaling:

**Lindeberg Theorem** : For each _n_ , assume that the ( _Xn,m,_ 1 _≤ m ≤ n_ ) are independent, _EXn,m_ = 0, _s_<sup>2</sup> _n_<sup>= �</sup><sup>_n_</sup> _m_ =1<sup>var(</sup><sup>_Xn,m_)</sup><sup>_< ∞_,</sup><sup>_Sn_= �</sup><sup>_n_</sup> _m_ =1<sup>_Xn,m_(so</sup><sup>_ESn_= 0).If</sup>


as _n →∞_ , for each _ε >_ 0 (UAN), then _Sn/sn −→_ d Normal(0 _,_ 1).

This is the previous version applied to _Xn,m/sn_ .

**Corollary 6.1.** _Suppose_ ( _Y_ 1 _, Y_ 2 _, . . ._ ) _are independent, EYi_ = 0 _. Suppose s_<sup>2</sup> _n_<sup>=�</sup><sup>_n_</sup> _i_ =1<sup>var(</sup><sup>_Yi_)</sup><sup>_<∞.If_</sup> _|Yi| ≤ M a.s. and if sn →∞ as n →∞, then_


_Proof._ Apply the Lindeberg Theorem 5.3 to _Xn,m_ = _Ym_ . The event _|Xn,m| ≥ εsn_ can only happen if _M ≥ εsn_ , that is, _sn ≤ M/ε_ . The event has probability 0 for large _n_ , which implies UAN.

**Corollary 6.2.** _In 5.3, we may replace UAN by_ **_Lyapunov’s condition_** _: ∃δ >_ 0 _such that_


_Proof._


24

_LECTURE 6. FEBRUARY 2_

25

So,


which checks UAN.

**Corollary 6.3.** _Let_ ( _Yi, i ≥_ 1) _be independent, EYi_ = 0 _. Suppose_ var( _Yi_ ) _→ σ_<sup>2</sup> _< ∞ as i →∞. Suppose ∃δ >_ 0 _such that M_ := sup _i E|Yi|_<sup>2+</sup><sup>_δ_</sup> _< ∞. Then_


_Proof._ Set _Xn,m_ = _Ym_ and check Lyapunov’s condition.

We conclude


and _sn ∼ σ_<sup>_√_</sup> _<u>n</u>_ <u>.</u>

**Corollary 6.4.** _If_ ( _Xi, i ≥_ 1) _are independent, |Xi| ≤ A, µi_ = _EXi, σi_<sup>2=var(</sup><sup>_Xi_)</sup><sup>_<∞,andif_</sup> _Sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi−−→_</sup> _a.s._<sup>_someS∞,whichisfinite,then_�</sup> _i_<sup>_n_</sup> =1<sup>_µiand_�</sup><sup>_n_</sup> _i_ =1<sup>_σ_</sup> _i_<sup>2</sup><sup>_convergetoafinitelimit._</sup>

_Proof._ By contradiction. Suppose _sn_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_σ_</sup> _i_<sup>2</sup><sup>_→∞_as</sup><sup>_n →∞_.Wecanapply6.1to</sup><sup>_Xi −µi_.</sup>


The first term converges in distribution to 0. The second term is a constant. The LHS can only converge in distribution to a constant. This contradiction implies that _sn → s∞ < ∞_ .

By 205A, this implies<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_Yi −µi_)convergesa.s.,so</sup><sup>_Sn −_�</sup><sup>_n_</sup> _i_ =1<sup>_µi_convergesa.s.Since</sup><sup>_Sn→S∞_a.s.,</sup> this implies<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_µi_convergesa.s.</sup>

### **6.2 3 Series Theorem**

**Theorem 6.5** (Classical “3 Series Theorem”) **.** _Suppose_ ( _Xi_ ) _are independent. Then_<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xiconverges_</sup> _a.s. to a finite limit if and only if, for some A, 1._<sup>�</sup> _i_<sup>_P_(</sup><sup>_|Xi| ≥A_)</sup><sup>_< ∞,_</sup> _2. For Yi_ = _Xi_ 1( _|Xi|≤A_ ) _, we have_<sup>�</sup> _i_<sup>_n_</sup> =1<sup>_EYiconverges,_</sup>

_LECTURE 6. FEBRUARY 2_

26

_3._<sup>�</sup> _i_<sup>var(</sup><sup>_Yi_)</sup><sup>_< ∞._</sup>

_Proof._ “If”: We implicitly proved this part in 205A.

For “only if”, assume<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi_converges.Theevents</sup><sup>_{|Xn|>A}_occuronlyfinitelyoften.ByBorel-</sup> Cantelli 2,<sup>�</sup> _i_<sup>_P_(</sup><sup>_|Xn| > A_)</sup><sup>_< ∞_.Also,�</sup> _i_<sup>_Yi_convergesa.s.Apply6.4to(</sup><sup>_Yi_):�</sup> _i_<sup>_EYi_and�</sup> _i_<sup>var(</sup><sup>_Yi_)</sup> converge.

### **6.3 Classical Theory: “Infinitely Divisible Distributions”**

What are all possible limits


See Durrett 3.7 and 3.8.

### **6.4 Poisson Limits**

For PMs _µ_ 1, _µ_ 2 on measurable ( _S, S_ ),


This is the **variational distance** .

(Easy) If _S_ is countable, then


If _S_ = R and _µi_ has density _fi_ , then


_Know_ . Class 2 says for _countable S_ ,


Let _f∞_ = 1 and _fn_ be a sinusoid on [0 _,_ 1] with period 1 _/n_ . Here, _µn → µ∞_ weakly but _∥µn − µ∞∦ →_ 0.

**Lemma 6.6** (Easy?) **.** _(a) If_ dist( _Xi_ ) = _µi, i_ = 1 _,_ 2 _, then P_ ( _X_ 1 _̸_ = _X_ 2) _≥∥µ_ 1 _− µ_ 2 _∥. (b) Given µ_ 1 _, µ_ 2 _, there exist_ ( _X_ 1 _, X_ 2) _with_ dist( _Xi_ ) = _µi and P_ ( _X_ 1 _̸_ = _X_ 2) = _∥µ_ 1 _− µ_ 2 _∥._

This uses a **coupling** argument.

“ _X_ is Bernoulli( _p_ )” means _P_ ( _X_ = 1) = _p_ , _P_ ( _X_ = 0) = 1 _− p_ .

**Theorem 6.7** (Le Cam’s Theorem) **.** _Suppose_ ( _Xr,_ 1 _≤ r ≤ n_ ) _are independent_ Bernoulli( _pr_ ) _. Write S_ =<sup>�</sup><sup>_n_</sup> _r_ =1<sup>_Xr,λ_= �</sup><sup>_n_</sup> _r_ =1<sup>_pr.Then∥_dist(</sup><sup>_S_)</sup><sup>_−_Poisson(</sup><sup>_λ_)</sup><sup>_∥≤_�</sup><sup>_n_</sup> _r_ =1<sup>_p_</sup> _r_<sup>2</sup><sup>_._</sup>

_LECTURE 6. FEBRUARY 2_

27

_Proof._ Given _p_ (small), we want ( _X, Y_ ), _X_ =d Bernoulli( _p_ ), _Y_ =d Poisson( _p_ ), and _P_ ( _X̸_ = _Y_ ) is small. Define


(Check that this works.)


## **Lecture 7**

---

[← January 31](07-january-31.md) · [Up: contents](index.md) · [February 7 →](09-february-7.md)
