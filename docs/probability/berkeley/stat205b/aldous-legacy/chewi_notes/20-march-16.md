---
title: March 16
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# March 16

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **18.1 Rejection Sampling**

_Undergraduate_ . _F_<sup>_−_1</sup> ( _U_ ) has the distribution function _F_ .

“Rejection sampling”.

_Want_ : To simulate from a given density _g_ ( _x_ ).

_Know_ : How to simulate from some density _f_ ( _x_ ).

_Know_ :


- _x_ is a sample from _f_ .

- With probability _g_ ( _x_ ) _/_ ( _Cf_ ( _x_ )), output _x_ .

- Else, repeat.

On each step,


P(some output) = 1 _/C_ , so the density given that we have an output is _g_ ( _x_ ).

### **18.2 Markov Chains on Measurable State Spaces**

Consider a MC ( _Xn, n ≥_ 0) on measurable _S_ , specified by the kernel _Q_ ( _s, A_ ) = P( _X_ 1 _∈ A | X_ 0 = _s_ ).


**Lemma 18.1.** _Let β be a PM on S with the following assumption:_

_(H1) Suppose that ∀x ∈ S, there exists a stopping time Tx < ∞ a.s. for the_ ( _δx, Q_ ) _-chain such that_ P _x_ ( _XTx ∈·_ ) = _β_ ( _·_ ) _._

70

_LECTURE 18. MARCH 16_

71

_Then, for the_ ( _β, Q_ ) _-chain, ∃T < ∞ such that_ P _β_ ( _XT ∈·_ ) = _β_ ( _·_ ) _and define µ_ ( _A_ ) def= E _β_ [ _number of visits to A before T_ ] _._

_Suppose ∃An ↑ S such that µ_ ( _An_ ) _< ∞. This defines a (maybe σ-finite) invariant measure µ._

_Proof._ Condition on the first step.

Consider the following assumption:

(H2) There exists a PM _β_ and _∃δ >_ 0 such that _Q_ ( _x, ·_ ) _≥ δβ_ ( _·_ ) _∀x ∈ S_ .

**Lemma 18.2.** ( _H_ 2) = _⇒_ ( _H_ 1) _._

_Proof._ This is rejection sampling.

Write _Q_ ( _x, ·_ ) = _δβ_ ( _·_ ) + (1 _− δ_ ) _R_ ( _x, ·_ ), which is the definition of the kernel _R_ ( _x, ·_ ). Let ( _ξi, i ≥_ 1) be independent, P( _ξi_ = 1) = _δ_ , P( _ξi_ = 0) = 1 _− δ_ . Construct a _Q_ -chain: given _Xn−_ 1 = _x_ , if _ξn_ = 1, then _Xn_ has distribution _β_ ; if _ξn_ = 0, then _Xn_ has distribution _R_ ( _x, ·_ ). Define _T_ = min _{n_ : _ξn_ = 1 _}_ . _T_ has the Geometric( _δ_ ) distribution, and _XT_ has the distribution _β_ .

_Useful Version_ . Consider the assumptions:

(H3) There exists a subset _A ⊆ S_ and a PM _β_ and _δ >_ 0 such that

(i) P _x_ ( _TA < ∞_ ) = 1 _∀x ∈ S_ , (ii) _Q_ ( _x, ·_ ) _≥ δβ_ ( _·_ ) _∀x ∈ A_ .

This is a **Harris chain** .

**Lemma 18.3.** ( _H_ 3) = _⇒_ ( _H_ 1) _._

_Proof._ Define _Vj_ to be the time of the _j_ th visit to _A_ , _Vj_ +1 = min _{n > Vj_ : _Xn ∈ A}_ . Define _Yj_ = _X_ (1+ _Vj_ ) _._

Then, ( _Yj_ ) is a MC with some kernel _Q_<sup>ˆ</sup> , and by (ii), _Q_<sup>ˆ</sup> satisfies (H2). Therefore, ( _Yj_ ) satisfies (H1), so ( _Xn_ ) satisfies (H1).

We can derive limit theorems from (H1) analogously to the countable state case. In particular, if we have _µ_ ( _S_ ) _< ∞⇐⇒_ positive-recurrent, then


is a stationary distribution and


(for any initial distribution) and


See Durrett, section 6.8.

_LECTURE 18. MARCH 16_

72

**Example 18.4.** _S_ = R<sup>_d_</sup> . _Q_ ( _x, ·_ ) has the density _q_ ( _x, y_ ) _>_ 0 everywhere which is a continuous function of ( _x, y_ ).

Take _A_ = ball( **0** _, B_ ). Then, inf _x,y∈A q_ ( _x, y_ ) _≡ ε >_ 0 by uniform continuity, so (ii) holds for the choice _β_ = Uniform( _A_ ) and


We need to show _TA < ∞_ a.s. It is enough to show _∃B_ E _x|X_ 1 _| ≤|x|_ for all _x_ with _|x| > B_ . By super-MG convergence, _TA < ∞_ .

This method cannot work if there are only a countable number of possible transitions from a state.

### **18.3 Markov Chains as Iterated Random Functions**

This follows the posted Diaconis-Freedman paper. It is also known as **coupling from the past** .

_Background_ . Given _f_ : _S → S_ , we can iterate: if we have _f_ ( _s_ ), _f_<sup>(2)</sup> ( _s_ ) = _f_ ( _f_ ( _s_ )), and


Let _S_ be measurable and _µ_ be a PM invariant under _f_ . This is the structure of **ergodic theory** .

If _S_ is a topological space, and _f_ is continuous, consider _s_ 0, _s_ 1 = _f_ ( _s_ 0), _sn_ +1 = _f_ ( _sn_ ) = _f_<sup>(</sup><sup>_n_)</sup> ( _s_ 0). Consider _µn_ , the empirical distribution on ( _S_ 0 _, S_ 1 _, . . . , Sn_ ):


Suppose _µn →_ some _µ_ weakly. Then, _µ_ is invariant. This is the study of dynamical systems or “chaos”.

**Lemma 18.5** (Old Lemma) **.** _Given a PM µ on S ×S, the first marginal µ_ 1 _, given independent X and U such that_ dist( _X_ ) = _µ_ 1 _and U_ = Uniform(0 _,_ 1) _, then ∃f_ : _S ×_ [0 _,_ 1] _→ S such that_ dist( _X, f_ ( _X, U_ )) = _µ._

Given a MC, take some explicit representation as _Xn_ +1 = _f_ ( _Xn, ξn_ +1) = _fξn_ +1( _Xn_ ) for IID ( _ξi, i ≥_ 1), _S_ ˆ-valued, where _f_ is continuous _S × S_ ˆ _→ S_ . We want to show dist( _Xn_ ) _→_ some _π_ weakly.


Instead, consider


Here, _Yn_ ( _x_ 0) =d _Xn_ ( _x_ 0).

_If_ we can prove _Yn_ ( _x_ 0) _−−→_ a.s.<sup>some</sup><sup>_Y∞_(</sup><sup>_x_0)as</sup><sup>_n →∞_,thendist(</sup><sup>_Xn_(</sup><sup>_x_0))</sup><sup>_→π_weakly.</sup>

**Example 18.6.** Let ( _Ai, Bi_ ) be IID R<sup>2</sup> -valued. Define a R<sup>1</sup> -valued MC _Xn_ by


For _X_ 0 = _x_ 0,


_LECTURE 18. MARCH 16_

73


The analog for R<sup>_d_</sup> -valued


works. We get a stationary distribution _π_ on R<sup>_d_</sup> .

## **Lecture 19**

---

[← March 14](19-march-14.md) · [Up: contents](index.md) · [March 21 →](21-march-21.md)
