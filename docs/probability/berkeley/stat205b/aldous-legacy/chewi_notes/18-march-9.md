---
title: March 9
source: https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/chewi_notes.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# March 9

**Source:** [`chewi_notes.pdf`](https://www.stat.berkeley.edu/~aldous/205B/chewi_notes.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **16.1 Renewal Reward Theorem**

**Proposition 16.1.** _Let_ ( _Xn, n ≥_ 0) _be irreducible and positive-recurrent, where π is the stationary distribution. Fix x. Let_ 0 _< S < ∞ be a stopping time such that XS_ = _x a.s. Then,_


_Proof. S_ = _f_ ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ) for some _f_ . Define _S_ 0 = 0, _S_ 1 = _S_ , and


_Rj_ =<sup>�</sup><sup>_S_</sup> _t_ =<sup>_j−_</sup> _Sj_<sup>1</sup> _−_ 1<sup>isthenumberofvisitsto</sup><sup>_y_during[</sup><sup>_Sj−_1</sup><sup>_, Sj_).TheStrongMarkovPropertyimpliesthat</sup> the blocks Λ1 _,_ Λ2 _, . . ._ are IID. Therefore, the ( _R_ 1 _, R_ 2 _, . . ._ ) are IID and the ( _Sj − Sj−_ 1 _, j ≥_ 1) are each IID. By the SLLN,


but we know from the MC Ergodic Theorem, 15.2, that the LHS converges to _π_ ( _y_ ) a.s., so the RHS and _π_ ( _y_ ) are equal.

We can replace the “ _x_ ” by a PM _θ_ . (Use the “general” ergodic theorem.)

### **16.2 Finite Markov Chains: Matrix Theory**

Consider an irreducible, positive-recurrent, aperiodic chain.


63

_LECTURE 16. MARCH 9_

64

If _S_ is finite, then (easy) the convergence is geometrically fast.


(The sum converges.) Assume _zx,y_ =<sup>�</sup><sup>_∞_</sup> _t_ =0<sup>(</sup><sup>_pt_(</sup><sup>_x, y_)</sup><sup>_−π_(</sup><sup>_y_))exists.Thematrix</sup><sup>**Z**isdeterminedby</sup><sup>**P**.How?</sup> Let **I** be the identity matrix and **Π** be the matrix where Π _x,y_ = _πy_ . Saying **_π_ P** = **_π_** means that **ΠP** = **Π** .


so **Z** = ( **I** _−_ **Π** )( **I** _−_ **P** )<sup>_−_1</sup> . . . but **_π_** ( **I** _−_ **P** ) = **0** implies that ( **I** _−_ **P** ) is _not_ invertible. **Z** can be interpreted as a “generalized inverse”. Kemeny-Snell, _Finite Markov Chains_ treats this topic.

Let _Tx_ = min _{n ≥_ 0 : _Xn_ = _x}_ .

_Step 1_ . Let _y̸_ = _x_ . Consider _S_ = min _{t > Ty_ : _Xt_ = _x}_ . 16.1 implies that _π_ ( _y_ )E _xS_ = E _yNTx_ ( _y_ ). Note that E _xS_ = E _xTy_ + E _yTx_ .

##### **Lemma 16.2.**


_Step 2_ : Fix a constant _k_ , and consider _S_ = min _{t ≥ k_ : _Xt_ = _x}_ . 16.1 implies

_π_ ( _y_ )( _k_ + E _ρ_ ( _k_ ) _Tx_ ) = E _x_ [number of visits to _y_ before _k_ ] + E _ρ_ ( _k_ )[number of visits to _y_ before _Tx_ ] _._

Then,


Let _k →∞_ . _ρ_<sup>(</sup><sup>_k_)</sup> _→ π_ , so _π_ ( _y_ )E _πTx_ = _zx,y_ + E _π_ [number of visits to _y_ before _Tx_ ].


##### **Lemma 16.4.**


_Step 3_ . Consider _S_ = min _{n ≥ Ty_ + _k_ : _Xn_ = _x}_ . 16.1 implies that

_π_ ( _y_ )(E _xTy_ + _k_ + E _θ_ ( _k_ ) _Tx_ ) = E _y_ [number of visits to _y_ before _k_ ] + E _θ_ ( _k_ )[number of visits to _y_ before _Tx_ ] _,_


Let _k →∞_ .


Also, 16.3 says _π_ ( _x_ )E _πTx_ = _zx,x_ .

The point of this is:

_LECTURE 16. MARCH 9_

65

##### **Lemma 16.5.**

_π_ ( _y_ )E _xTy_ = _zy,y − zx,y._

**Example 16.6** (Patterns in Coin-Tossing) **.** Fix a sequence, say, _HHTHH_ . Toss a fair coin until we see this pattern. What is the expected number of tosses?

In 205A, we had a martingale proof.

We can use a 32-state MC, ( _Xn, n ≥_ 0), of overlapping 5-tuples. _π_ is uniform, _π_ ( _x_ ) = 1 _/_ 32. Study E _πTx_ for _x_ = _HHTHH_ .

Then,

Then, by the formula,


### **16.3 The MC CLT & Variance of Sums**

Consider a chain on finite _S_ , irreducible and aperiodic, with stationary distribution _π_ . Consider a function _f_ : _S →_ R with _f_<sup>¯</sup> =<sup>�</sup> _i_<sup>_πif_(</sup><sup>_i_) = 0.Write</sup><sup>_St_= �</sup><sup>_t_</sup> _n_ =1<sup>_f_(</sup><sup>_Xn_).Wecanprove(usingIIDblocks)that</sup>


Instead, we will directly study var _St_ . Consider the stationary chain.


_LECTURE 16. MARCH 9_

66

We are using E _π_ [ _f_ ( _Xu_ ) _f_ ( _Xv_ )] = E _π_ [ _f_ ( _X_ 0) _f_ ( _Xs_ )]. Given a stationary process ( _X_ 0 _, X_ 1 _, X_ 2 _, . . ._ ), Kolmogorov extension says that there exists a process ( _Xn, −∞ < n < ∞_ ).

The sum over _s ≥_ 0 of _πx_ ( _p_<sup>(</sup> _x,y_<sup>_s_)</sup><sup>_−π_</sup> _y_<sup>) =</sup><sup>_π_</sup> _x_<sup>_z_</sup> _x,y_<sup>.Thesumover</sup><sup>_s ≤_0is</sup><sup>_π_</sup> _y_<sup>_z_</sup> _y,x_<sup>because</sup>


The sum over _s_ = 0 is _πx_ ( _δx,y − πy_ ).

_Conclusion_ : _σ_<sup>2</sup> ( _t_ ) = _f_<sup>_⊤_</sup> Γ _f_ for Γ _i,j_ = _πizi,j_ + _πjzj,i − πi_ ( _δi,j − πj_ ) (symmetric).

## **Lecture 17**

---

[← March 7](17-march-7.md) · [Up: contents](index.md) · [March 14 →](19-march-14.md)
