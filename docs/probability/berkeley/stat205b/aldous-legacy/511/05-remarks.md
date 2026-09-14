---
title: Remarks.
source: https://www.stat.berkeley.edu/~aldous/205B/511.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/511.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Remarks.

**Source:** [`511.pdf`](https://www.stat.berkeley.edu/~aldous/205B/511.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(i) The notation in (5.15–16) may be a bit confusing:


is not the backward process, and does not converge.

(ii) We use the algebraic tail condition to bound the probabilities of the exceptional sets in Proposition 5.1, that is, the sets where (5.12) and (5.13) fail. These probability bounds give the exponential rate of convergence in Theorem 5.1. With a little more effort, the optimal _r_ can be computed explicitly, in terms of the mean and variance of log _Kf_ , and the shape parameter _β_ in (5.2). If an exponential rate is not needed, it is enough to assume that log(1 + _Kf_ ) and log �1 + _ρ_ [ _f_ ( _x_ 0) _, x_ 0]� are _L_ 1.

ITERATED RANDOM FUNCTIONS

23

(iii) Furstenberg (1963) uses the backward iteration to study products of random matrices. He considers the action of a matrix group on projective space and shows that there is a unique stationary distribution, which can be represented as a convergent backward iteration. Convergence is proved by martingale arguments. It seems worthwhile to study the domain of this method.

(iv) Let (X, B) be a measurable space and let _K_ ( _x, dy_ ) be a Markov kernel on (X, B). When is there a family _{fθ_ : _θ ∈_ Θ _}_ and a probability _µ_ on Θ such that the Markov chain induced by these iterated random mappings has transitions _K_ ( _x, dy_ )? This construction is always possible if (X, B) is “Polish”, that is, a Borel subset of a complete separable metric space. See, for instance, Kifer (1986). The leading special case has X = [0 _,_ 1]. Then Θ can also be taken as the unit interval, and _µ_ as Lebesgue measure; _K_ ( _x, dy_ ) can be described by its distribution function _F_ ( _x, y_ ) = _K_ ( _x,_ [0 _, y_ ]). Let _G_ ( _x, ·_ ) be the inverse of _F_ ( _x, ·_ ). If _U_ is uniform, _G_ ( _x, U_ ) is distributed as _K_ ( _x, dy_ ). Finally, let _fθ_ ( _x_ ) = _G_ ( _x, θ_ ). Verification is routine, and the general case follows from the special case by standard tricks.

The question is more subtle—and the regularity conditions much more technical—if it is required that the _fθ_ ( _·_ ) be continuous. Blumenthal and Corson (1970) show that if X is a connected, locally connected, compact space, and _x → K_ ( _x, ·_ ) is continuous (weak star), and the support of _K_ ( _x, ·_ ) is X for all _x_ , then there is a probability measure on the Borel sets of the continuous functions from X to X which induces the kernel _K_ . Quas (1991) gives sufficient conditions for representation by smooth functions when X is a smooth manifold. A survey of these and related results appears in Dubischar (1997).

**6. More examples.** Autoregressive processes are an important feature of many statistical models, and can usefully be viewed as iterated random functions; the construction will be sketched here. We learned the trick from Anderson (1959), but he attributes it to Yule. Further examples and counterexamples to illustrate the theory are given in Section 6.2; Section 6.3 revisits the example discussed in Section 2.1.

**6.1. Autoregressive processes.** Let _S_ = R, the real line. Let _a_ be a real number with 0 _< a <_ 1 and let _µ_ be a probability measure on R. For present purposes, an autoregression is a Markov process on R with the following law of motion: starting from _x ∈_ R, the chain picks _ξ_ according to _µ_ and moves to _ax_ + _ξ_ . Conditions (5.1) and (5.3) are obvious: if _f_ ( _x_ ) = _ax_ + _ξ_ , then _Kf_ = _a_ . For condition (5.2), we need to assume for instance that if _ξ_ has distribution _µ_ , there are positive, finite constants _α, β_ with _P_ ( _|ξ| > u_ ) _< α/u_<sup>_β_</sup> for all _u >_ 0. If _ξi_ are independent with common distribution _µ_ , the forward process starting from _x_ has _X_ 0( _x_ ) = _x_ ,

_X_ 1( _x_ ) = _ax_ + _ξ_ 1 _, X_ 2( _x_ ) = _a_<sup>2</sup> _x_ + _aξ_ 1 + _ξ_ 2 _, X_ 3( _x_ ) = _a_<sup>3</sup> _x_ + _a_<sup>2</sup> _ξ_ 1 + _aξ_ 2 + _ξ_ 3 _,_

and so forth. This process converges in law, but does not converge almost surely: at stage _n_ , new randomness is introduced by _ξn_ . The backward process starting from _x_ looks at first glance much the same: _Y_ 0( _x_ ) = _x_ ,

_Y_ 1( _x_ ) = _ax_ + _ξ_ 1 _, Y_ 2( _x_ ) = _a_<sup>2</sup> _x_ + _ξ_ 1 + _aξ_ 2 _, Y_ 3( _x_ ) = _a_<sup>3</sup> _x_ + _ξ_ 1 + _aξ_ 2 + _a_<sup>2</sup> _ξ_ 3 _,_

24

PERSI DIACONIS AND DAVID FREEDMAN

and so forth. But this process converges a.s., because the new randomness introduced by _ξn_ is damped by _a_<sup>_n_</sup> . The stationary autoregressive process may be realized as


Each _Wm_ is obtained by doing the backward iteration on _{ξm, ξm−_ 1 _, ξm−_ 2 _, . . . }_ . Equation (5.6) is the generalization. With the usual Euclidean distance, the constant _Ax_ in Theorem 5.1 must depend on the starting state _x_ . For a particularly brutal illustration, take _ξi ≡_ 0.

**6.2. Without regularity conditions.** This section gives some examples to indicate what can happen without our regularity conditions.

**Example 6.1.** This example shows that some sort of contracting property is needed to get a result like Theorem 5.1. Let _S_ = [0 _,_ 1]. Arithmetic is to be done modulo 1: for instance, 2 _× ._ 71 = _._ 42. Let


and _µ{f }_ = _µ{g}_ = 1 _/_ 2. The forward and the backward process can both be represented as

_Xn_ = 2<sup>_ξ_1+</sup><sup>_···_+</sup><sup>_ξn_</sup> _x_ mod 1 _,_

the _ξn_ being independent and taking values 0 or 1 with probability 1 _/_ 2 each; _x_ is the starting point. Clearly, the backward process converges only if the starting point is a binary rational. Furthermore, there are infinitely many distinct stationary probabilities: if _ζ_ 1 _, ζ_ 2 _, . . ._ is a stationary 0–1 valued process, then the law of<sup>�</sup> _i_<sup>_ζi/_2</sup><sup>_i_</sup> is stationary for our chain. Since _Kf_ = 1 and _Kg_ = 2, condition (5.3) fails. Figure 6 plots _Xn_ against _n_ for _n_ = 0 _, . . . ,_ 100, with linear interpolation.

Figure 6. Iterated random functions on the unit interval. With probability 1 _/_ 2, the chain stands pat; with probability 1 _/_ 2, the chain moves from _x_ to 2 _x_ modulo 1. The forward and backward process are the same, and do not converge.


<!-- Start of picture text -->
1.00<br>0.75<br>0.50<br>0.25<br>0.00<br>0 25 50 75 100<br><!-- End of picture text -->

ITERATED RANDOM FUNCTIONS

25

**Remark.** Figure 6 involves on the order of 50 doublings, so numerical accuracy is needed to 50 binary digits, or 16 decimal places in _x_ . That is about the limit of double-precision computer packages like MATLAB a PC. If, say, 1,000 iterations are wanted, accuracy to 150 decimal places would be needed. The work-around is easy. Code the states _x_ as long strings of 0’s or 1’s, and do binary arithmetic. For plotting, convert to decimals: only the first 10 bits in _Xn_ will matter.

**Example 6.2.** This example has a unique stationary distribution but the backward process does not converge. Let _S_ be the integers mod _N_ . Let


with _µ{f }_ = _µ{g}_ = 1 _/_ 2. The forward and the backward process can both be represented as

_Xn_ = _ξ_ 1 + _· · ·_ + _ξn_ + _x_ mod _N,_

the _ξn_ being independent and taking values 0 or 1 with probability 1 _/_ 2 each. Clearly, the backward process does not converge. On the other hand, the chain is aperiodic and irreducible, so there is a unique stationary distribution (the uniform), and there is an exponential rate of convergence. Let _ρ_ ( _i, j_ ) be the least _k_ = 0 _,_ 1 _, . . ._ such that _i_ + _k_ = _j_ or _j_ + _k_ = _i_ . Then _ρ_ is a metric: the distance between two points is the minimal number of steps it takes to get from one to the other, where steps can be taken in either direction. Relative to this metric, _f_ and _g_ are Lipschitz, with _Kf_ = _Kg_ = 1; condition (5.3) is violated.

The next example shows another sort of pathology when condition (5.3) holds but (5.1–2) fail.

**Example 6.3.** The state space _S_ is [0 _, ∞_ ). Let the random variable _ξ_ have a symmetric stable distribution with index _α >_ 1; see Samorodnitsky and Taqqu (1994) or Zolotarev (1986). Let _µ_ be the law of _e_<sup>_ξ−_1</sup> . Consider a Markov chain that moves from _x ∈_ [0 _, ∞_ ) by choosing _K_ at random from _µ_ and going to _Kx_ . Then 0 is a fixed point and the unique stationary distribution concentrates at 0. If _ξi_ are i.i.d. symmetric stable with index _α_ , the forward and the backward process process can both be represented as


_Xn →_ 0 almost surely as _n →∞_ , by the strong law of large numbers. On the other hand, the Prokhorov distance between _L_ ( _Xn_ ) and _δ_ 0 is of order 1 _/n_<sup>_α−_1</sup> , by Lemmas 6.1 and 6.2 below. In particular, exponential rates of convergence do not obtain. Condition (5.3) holds: � log _K dµ_ = _−_ 1. However, (5.1) fails, and so does (5.2) for _x_ 0 _̸_ = 0.

**Lemma 6.1.** _Let δ_ 0 _be point mass at_ 0 _, and let_ Φ _be a continuous probability measure on_ (0 _, ∞_ ) _._

- (i) _There is a unique ε_ 0 _with_ 0 _< ε_ 0 _<_ 1 _and_ Φ( _ε_ 0 _, ∞_ ) = _ε_ 0 _._

- (ii) Φ( _ε, ∞_ ) _< ε for ε > ε_ 0 _._

- (iii) _ρ_ ( _δ_ 0 _,_ Φ) = _ε_ 0 _._

PERSI DIACONIS AND DAVID FREEDMAN

26

Proof. Claims (i) and (ii) are easy to verify. For (iii), we need to compute the infimum of _ε_ such that for all compact _C_ ,


and


If 0 _∈/ C_ , then (6.1) is vacuous. If 0 _∈ C_ , then (6.1) is equivalent to 1 _− ε <_ Φ( _Cε_ ). Furthermore, 0 _∈ C_ entails [0 _, ε_ ) _⊂ Cε_ . And _Cε_ = [0 _, ε_ ) when _C_ = _{_ 0 _}_ . Thus, (6.1) for all compact _C_ is equivalent to


Likewise, if 0 _∈ Cε_ , then (6.2) is vacuous. If 0 _∈/ Cε_ then (6.2) is equivalent to Φ( _C_ ) _< ε_ . But 0 _∈/ Cε_ iff _C ⊂_ [ _ε, ∞_ ). Thus, (6.2) for all compact _C_ is also equivalent to (6.3). Now (iii) follows from (ii). Q.E.D.

**Lemma 6.2.** _Let U be a symmetric stable random varible with index α >_ 1 _. Let n be a large positive integer. The Prokhorov distance between δ_ 0 _and the law of_ exp( _−n_ + _n_<sup>1</sup><sup>_/α_</sup> _U_ ) _is of order_ 1 _/n_<sup>_α−_1</sup> _._

Proof. This follows from Lemma 6.1, since _P {U > u} ∼_ 1 _/u_<sup>_α_</sup> . Q.E.D.

**Remark.** Something can be done even when all the Lipschitz constants are 1, provided the functions are genuinely contracting on a recurrent set. For instance, Steinsaltz (1997, 1998) considers a Markov chain on R that moves by choosing one of the following two functions at random:


These functions have Lipschitz constant 1. But, as a team, they are genuinely contracting on the interval [ _−_ 2 _,_ 2]. This interval is recurrent. Indeed, from large negative _x_ , the chain moves 2 units to the right and 1 unit to the left with equal probabilities; the reverse holds for large positive _x_ . Thus, when the chain is near _±∞_ , it drifts back toward 0. Steinsaltz has some general theory, and other examples.

**6.3. The Beta walk.** The state space _S_ is the closed unit interval [0,1]. Let Φ be a probability measure on _S_ , and let 0 _< p <_ 1. Consider a chain with the following transition probabilities. Starting from _x ∈_ [0 _,_ 1], the chain goes left with probability _p_ and right with probability 1 _− p_ . To move, it picks _u_ from Φ. If the move is to the left, the chain goes to _ux_ ; if to the right, it goes to _x_ + _u_ (1 _− x_ ) = _x_ + _u − ux_ . Call Φ the “moving measure”. If Φ is Beta( _α, α_ ), call the chain a “Beta walk”. The

ITERATED RANDOM FUNCTIONS

27

example in Section 2.1 was a Beta walk with _p_ = 1 _/_ 2 and _α_ = 1 _/_ 2. We extend the terminology a little: Beta(0 _,_ 0) puts mass 1 _/_ 2 at 0 and 1; Beta( _∞, ∞_ ) puts mass 1 at 1 _/_ 2.

These examples fit into the framework of Theorem 5.1: _p_ and Φ probabilize the set of linear maps that shrink the unit interval—

- either toward 0, when the map sends _x_ to _ux_ ,

- or toward 1, when the map sends _x_ to _x_ + _u − ux_ .

All the Lipschitz constants are 1 or smaller. Conditions (5.1–2–3) are obvious, and there is exponential convergence to the unique stationary distribution. In the balance of this section, we prove the following theorem.

**Theorem 6.1.** _Suppose S_ = [0 _,_ 1] _, p_ = 1 _/_ 2 _, and the move measure_ Φ _is Beta_ ( _α, α_ ) _. Let α_<sup>_′_</sup> = _α/_ ( _α_ +1) _; when α_ = _∞, let α_<sup>_′_</sup> = 1 _. If α is_ 0 _,_ 1 _, or ∞, then the stationary distribution of the Beta walk is Beta_ ( _α_<sup>_′_</sup> _, α_<sup>_′_</sup> ) _. For any other value of α, the stationary distribution is symmetric and has the same first three moments as Beta_ ( _α_<sup>_′_</sup> _, α_<sup>_′_</sup> ) _but a different fourth moment: in particular, the stationary distribution is not Beta._

**Remarks.** The second moment of Beta( _a, a_ ) is ( _a_ + 1) _/_ (4 _a_ + 2), which determines _a_ ; that is why agreement on 3 moments and discrepancy on the 4th shows the stationary measure not to be Beta. As will be seen, the discrepancy is remarkably small—on the order of 10<sup>_−_4</sup> when _α_ = 1 _/_ 3, and that is about as big as it gets.

The proof of the next lemma is omitted. The first term in the integral corresponds to a leftward move, taken with probability _p_ ; the second, to a rightward move; compare (2.1).

**Lemma 6.3.** _If the move measure_ Φ _has density φ, and the starting state is chosen from a density ψ, the density of the position after one move is_


The next result too is standard. Suppose _X_ is Beta( _a, b_ ). Then


The second equality follows from the recursion Γ( _x_ +1) = _x_ Γ( _x_ ): there are _n_ factors in the numerator and in the denominator.

**Corollary 6.1.** _If X is Beta_ ( _a, a_ ) _, then_


PERSI DIACONIS AND DAVID FREEDMAN

28

---

[← Remarks.](04-remarks.md) · [Up: contents](index.md) · [The proof of Theorem 6.1. →](06-the-proof-of-theorem-6-1.md)
