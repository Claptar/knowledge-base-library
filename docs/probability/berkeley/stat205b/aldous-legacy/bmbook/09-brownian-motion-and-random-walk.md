---
title: Brownian motion and random walk
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Brownian motion and random walk

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this chapter we discuss some aspects of the relation between random walk and Brownian motion. The first two sections aim to demonstrate the nature of this relation by examples, which are of interest in their own right. These are _first_ the law of the iterated logarithm, which is easier to prove for Brownian motion and can be extended to random walks by an embedding argument, and _second_ a proof that Brownian motion does not have points of increase, which is based on a combinatorial argument for a class of random walks, and then extended to Brownian motion. We then discuss the Skorokhod embedding problem systematically, and give a proof of the Donsker invariance principle based on the Skorokhod embedding. We give a variety of applications of Donsker’s theorem, including the arcsine laws.

### **1. The law of the iterated logarithm**

For a standard linear Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ , although at any given time _t_ and for any open set _U ⊂_ R the probability of the event _{B_ ( _t_ ) _∈ U }_ is positive, over a long time Brownian motion cannot grow arbitrarily fast. We have seen in Corollary 1.11 that, for any small _ε >_ 0, almost surely, there exists _t_ 0 _>_ 0 such that _|B_ ( _t_ ) _| ≤ εt_ for all _t ≥ t_ 0, whereas Proposition 1.23 ensures that for every large _k_ , almost surely, there exist arbitrarily large times _t_ such that _|B_ ( _t_ ) _| ≥ k√t_ . It is therefore natural to ask for the asymptotic _smallest upper envelope_ of the Brownian motion, i.e. for a function _ψ_ : (1 _, ∞_ ) _→_ R such that


The law of the iterated logarithm (whose name comes from the answer to this question but is by now firmly established for this type of upper-envelope results) provides such a ‘gauge’ function, which determines the almost-sure _asymptotic growth_ of a Brownian motion.

A similar problem arises for arbitrary random walks _{Sn_ : _n ≥_ 0 _}_ , where we ask for a sequence ( _an_ : _n ≥_ 0) such that


These two questions are closely related, and we start with an answer to the first one.

Theorem 5.1 (Law of the Iterated Logarithm for Brownian motion). _Suppose {B_ ( _t_ ) : _t ≥_ 0 _} is a standard linear Brownian motion. Then, almost surely,_


121

Remark 5.2. By symmetry it follows that, almost surely,


Hence, for any _ε >_ 0, there exists _t_ 0 such that _|B_ ( _t_ ) _| ≤_ (1 + _ε_ <u>)�2</u> _t_ log log( _t_ ) for any _t ≥ t_ 0, _⋄_ while there exist arbitrarily large times _t_ with _|B_ ( _t_ ) _| ≥_ (1 _− ε_ ) ~~�~~ 2 _t_ log log( _t_ ).


<!-- Start of picture text -->
2500 2500<br>2000 2000<br>ψ(t) = � 2t loglog(t) ψ(t) = � 2t loglog(t)<br>1500 1500<br>1000 1000<br>500 500<br>0 B(t) t 0 B(t) t<br>−500 −500<br>−1000 −1000<br>−1500 −1500<br>−ψ(t) −ψ(t)<br>−2000 −2000<br>−2500 −2500<br>0 2 4 6 8 10 0 2 4 6 8 10<br>x 105 x 105<br><!-- End of picture text -->

Figure 1. The picture on the left shows the asymptotic upper envelope _ψ_ ( _t_ ) = ~~�~~ 2 _t_ log log( _t_ ) and a typical Brownian path indicating that scales where the path comes near to the envelope are very sparse. The picture on the right shows Brownian motion at such a scale. Due to the special nature of this scale the Brownian path (which is implicitly conditioned on the event of ending up near the upper envelope) has features untypical of Brownian paths. See the ‘Notes and Comments’ section for more details.


By Theorem 2.18 the maximum of Brownian motion up to a fixed time _t_ has the same distribution as _|B_ ( _t_ ) _|_ . Therefore


We can use the tail estimate P _{Z > x} ≤ e_<sup>_−x_2</sup><sup>_/_2</sup> for a standard normally distributed _Z_ and _x >_ 1, see Lemma II.3.1, to conclude that, for large _n_ ,


This is summable in _n_ and hence, by the Borel-Cantelli lemma, we get that only finitely many of these events occur. For large _t_ write _q_<sup>_n−_1</sup> _≤ t < q_<sup>_n_</sup> . We have


122

since _ψ_ ( _t_ ) _/t_ is decreasing in _t_ . Thus


Since this holds for any _ε >_ 0 and _q >_ 1 we have proved that lim sup _B_ ( _t_ ) _/ψ_ ( _t_ ) _≤_ 1.

For the lower bound, fix _q >_ 1. In order to use the Borel-Cantelli lemma in the other direction, we need to create a sequence of _independent_ events. Let


We now use Lemma II.3.1 to see that there is a constant _c >_ 0 such that, for large _x_ ,


Using this estimate we get, for some further constant _c >_ ˜ 0,


and therefore<sup>�</sup> _n_<sup>P(</sup><sup>_Dn_) =</sup><sup>_∞_.Thusforinfinitelymany</sup><sup>_n_</sup> _B_ ( _q_<sup>_n_</sup> ) _≥ B_ ( _q_<sup>_n−_1</sup> ) + _ψ_ ( _q_<sup>_n_</sup> _− q_<sup>_n−_1</sup> ) _≥−_ 2 _ψ_ ( _q_<sup>_n−_1</sup> ) + _ψ_ ( _q_<sup>_n_</sup> _− q_<sup>_n−_1</sup> ) _,_

where the second inequality follows from applying the previously proved upper bound to _−B_ ( _q_<sup>_n−_1</sup> ). From the above we get that, for infinitely many _n_ ,


Indeed, to obtain the second inequality first note that


since _ψ_ ( _t_ ) _/√t_ is increasing in _t_ for large _t_ . For the second term we just use the fact that _ψ_ ( _t_ ) _/t_ is decreasing in _t_ . Now (1.1) implies that


and letting _q ↑∞_ concludes the proof of the lower bound.

Corollary 5.3. _Suppose {B_ ( _t_ ) : _t ≥_ 0 _} is a standard Brownian motion. Then, almost surely,_


**Proof.** By Theorem 1.9 the process _{X_ ( _t_ ) : _t ≥_ 0 _}_ defined by _X_ ( _t_ ) = _tB_ (1 _/t_ ) for _t >_ 0 is a standard Brownian motion. Hence, using Theorem 5.1, we get


123

The law of the iterated logarithm is a result which is easier to prove for Brownian motion than for random walks, as scaling arguments can be used to good effect in the proof. We now use an ad hoc argument to obtain a law of the iterated logarithm for simple random walks, i.e. the random walk with increments taking the values _±_ 1 with equal probability, from Theorem 5.1. A version for more general walks will follow with analogous arguments from the embedding techniques of Section 3, see Theorem 5.17.

Theorem 5.4 (Law of the Iterated Logarithm for simple random walk). _Let {Sn_ : _n ≥_ 0 _} be a simple random walk. Then, almost surely,_


We now start the technical work to transfer the result from Brownian motion to simple random walk. The next result shows that the limsup does not change if we only look along a sufficiently dense sequence of random times. We abbreviate _ψ_ ( _t_ ) = �2 _t_ log log( _t_ ).

Lemma 5.5. _If {Tn_ : _n ≥_ 1 _} is a sequence of random times (not necessarily stopping times) satisfying Tn →∞ and Tn_ +1 _/Tn →_ 1 _almost surely, then_


_Furthermore, if Tn/n → a almost surely, then_


**Proof.** The upper bound follows from the upper bound for continuous time without any conditions on _{Tn_ : _n ≥_ 1 _}_ . For the lower bound some restrictions are needed, which prevent us from choosing, for example, _T_ 0 = 0 and _Tn_ = inf _{t > Tn−_ 1 + 1: _B_ ( _t_ ) _< n_<sup><u>1</u></sup><sup>_}_.Ourconditions</sup> _Tn_ +1 _/Tn →_ 1 and _Tn →∞_ make sure that the times are sufficiently dense to rule out this effect. Define, for fixed _q >_ 4,


Note that _Dk_ and Ω _k_ are independent events. From Brownian scaling and Lemma II.3.1 it is easy to see that, for a suitable constant _c >_ 0,


Moreover, by scaling, P(Ω _k_ ) =: _cq >_ 0, and _cq_ that does not depend on _k_ . As P( _Dk_<sup>_∗_) =</sup><sup>_cq_P(</sup><sup>_Dk_)</sup> the sum<sup>�</sup> _k_<sup>P(</sup><sup>_D_</sup> 2<sup>_∗_</sup> _k_<sup>)isinfinite.Astheevents</sup><sup>_{D_</sup> 2<sup>_∗_</sup> _k_<sup>:</sup><sup>_k≥_1</sup><sup>_}_areindependent,bytheBorel-</sup> Cantelli lemma, for infinitely many (even) _k_ ,


124

By Remark 5.2, for all sufficiently large _k_ , we have _B_ ( _q_<sup>_k−_1</sup> ) _≥−_ 2 _ψ_ ( _q_<sup>_k−_1</sup> ) and, by easy asymptotics, _ψ_ ( _q_<sup>_k_</sup> _− q_<sup>_k−_1</sup> ) _≥ ψ_ ( _q_<sup>_k_</sup> )(1 _−_<sup><u>1</u></sup> _q_<sup>).Hence,forinfinitelymany</sup><sup>_k_,</sup>


with the right hand side being positive by our choice of _q_ . Now define _n_ ( _k_ ) = min _{n_ : _Tn > q_<sup>_k_</sup> _}_ . Since the ratios _Tn_ +1 _/Tn_ tend to 1, it follows that for any fixed _ε >_ 0, we have _q_<sup>_k_</sup> _≤ Tn_ ( _k_ ) _< q_<sup>_k_</sup> (1 + _ε_ ) for all large _k_ . Thus, for infinitely many _k_ ,


But since � _q_<sup>_k_</sup> _/ψ_ ( _q_<sup>_k_</sup> ) _→_ 0 and _ψ_ ( _q_<sup>_k_</sup> ) _/ψ_ ( _q_<sup>_k_</sup> (1 + _ε_ )) _→_ 1 _/_<sup>_√_</sup> 1 + _ε_ , we conclude that

and since the left hand side does not depend on _q_ and _ε >_ 0 we can let _q ↑∞_ and _ε ↓_ 0 to arrive at the desired conclusion. For the last part, note that if _Tn/n → a_ then _ψ_ ( _Tn_ ) _/ψ_ ( _an_ ) _→_ 1.


Figure 2. Embedding simple random walk into Brownian motion

**Proof of Theorem 5.4.** To prove the law of the iterated logarithm for simple random walk, we let _T_ 0 = 0 and, for _n ≥_ 1,


The times _Tn_ are stopping times for Brownian motion and, hence, by the strong Markov property, the waiting times _Tn − Tn−_ 1 are independent and identically distributed random variables. Obviously, P _{B_ ( _Tn_ ) _−B_ ( _Tn−_ 1) = 1 _}_ = P _{B_ ( _Tn_ ) _−B_ ( _Tn−_ 1) = _−_ 1 _}_ =<sup><u>1</u></sup> 2<sup>_,_and therefore</sup> _{B_ ( _Tn_ ) : _n ≥_ 0 _}_ is a simple random walk. By Theorem 2.45, we have E[ _Tn − Tn−_ 1] = 1, and hence the law of large numbers ensures that _Tn/n_ converges almost surely to 1, and the theorem follows from Lemma 5.5.

125

Remark 5.6. The technique we have used to get Theorem 5.4 from Theorem 5.1 was based on finding an increasing sequence of stopping times _{Tn_ : _n ≥_ 0 _}_ for the Brownian motion, such that _Sn_ = _B_ ( _Tn_ ) defines a simple random walk, while we keep some control over the size of _Tn_ . This ‘embedding technique’ will be extended substantially in Section 3. _⋄_

### **2. Points of increase for random walk and Brownian motion**

A point _t ∈_ (0 _, ∞_ ) is a local point of increase for the function _f_ : (0 _, ∞_ ) _→_ R if for some open interval ( _a, b_ ) containing _t_ we have _f_ ( _s_ ) _≤ f_ ( _t_ ) for all _s ∈_ ( _a, t_ ) and _f_ ( _t_ ) _≤ f_ ( _s_ ) for all _s ∈_ ( _t, b_ ). In this section we show that Brownian motion almost surely has no local points of increase. Our proof uses a combinatorial argument to derive a quantitative result for simple random walks, and then uses this result to study the case of Brownian motion. A crucial tool in the proof is an inequality of Harris [ **Ha60** ], which is of some independent interest.

Theorem 5.7 (Harris’ inequality). _Suppose that X_ = ( _X_ 1 _, . . . , Xd_ ) _is a random variable with values in_ R<sup>_d_</sup> _and independent coordinates. Let f, g_ : R<sup>_d_</sup> _→_ R _be measurable functions, which are nondecreasing in each coordinate. Then,_


_provided the above expectations are well-defined._

**Proof.** One can argue, using the monotone convergence theorem, that it suffices to prove the result when _f_ and _g_ are bounded. We assume _f_ and _g_ are bounded and proceed by induction on the dimension _d_ . Suppose first that _d_ = 1. Note that


Therefore, for _Y_ an independent random variable with the same distribution as _X_ ,


and (2.1) follows easily. Now, suppose (2.1) holds for _d −_ 1. Define


and define _g_ 1 similarly. Note that _f_ 1( _x_ 1) and _g_ 1( _x_ 1) are non-decreasing functions of _x_ 1. Since _f_ and _g_ are bounded, we may apply Fubini’s theorem to write the left hand side of (2.1) as

(2.2)


where _µ_ 1 denotes the law of _X_ 1. The expectation in the integral is at least _f_ 1( _x_ 1) _g_ 1( _x_ 1) by the induction hypothesis. Thus, using the result for the _d_ = 1 case, we can bound (2.2) from below by E[ _f_ 1( _X_ 1)] E[ _g_ 1( _X_ 2)], which equals the right hand side of (2.1), completing the proof.

For the rest of this section, let _X_ 1 _, X_ 2 _, . . ._ be independent random variables with


126

and let _Sk_ =<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_Xi_betheirpartialsums.Denote</sup>

(2.3) _pn_ = P _{Si ≥_ 0 for all 1 _≤ i ≤ n} ._

Then _{Sn_ is a maximum among _S_ 0 _, S_ 1 _, . . . Sn}_ is precisely the event that the reversed random walk given by _Sk_<sup>_′_=</sup><sup>_Xn_+</sup><sup>_. . ._+</sup><sup>_Xn−k_+1is nonnegative for all</sup><sup>_k_= 1</sup><sup>_, . . . , n_.Hence this event also</sup> has probability _pn_ . The following lemma gives the order of magnitude of _pn_ , the proof will be given as Exercise 5.4.

Lemma 5.8. _There are positive constants C_ 1 _and C_ 2 _such that_


The next lemma expresses, in terms of the _pn_ defined in (2.3), the probability that _Sj_ stays between 0 and _Sn_ for _j_ between 0 and _n_ .

Lemma 5.9. _We have p_<sup>2</sup> _n_<sup>_≤_P</sup> �0 _≤ Sj ≤ Sn for all_ 1 _≤ j ≤ n_ � _≤ p_<sup>2</sup> _⌊n/_ 2 _⌋_<sup>_._</sup>

**Proof.** The two events


are independent, since _A_ depends only on _X_ 1 _, . . . , X⌊n/_ 2 _⌋_ and _B_ depends only on the remaining _X⌊n/_ 2 _⌋_ +1 _, . . . , Xn_ . Therefore,

P _{_ 0 _≤ Sj ≤ Sn} ≤_ P( _A ∩ B_ ) = P( _A_ )P( _B_ ) _≤ p_<sup>2</sup> _⌊n/_ 2 _⌋_<sup>_,_</sup>

which proves the upper bound.

For the lower bound, we let _f_ ( _x_ 1 _, . . . , xn_ ) = 1 if all the partial sums _x_ 1 + _. . ._ + _xk_ for _k_ = 1 _, . . . , n_ are nonnegative, and _f_ ( _x_ 1 _, . . . , xn_ ) = 0 otherwise. Also, define _g_ ( _x_ 1 _, . . . , xn_ ) = _f_ ( _xn, . . . , x_ 1). Then _f_ and _g_ are nondecreasing in each component. By Harris’ inequality, for _X_ = ( _X_ 1 _, . . . , Xn_ ),


Also,


which proves the lower bound.

Definition 5.10.

- (a) _A sequence s_ 0 _, s_ 1 _, . . . , sn of reals has a (global)_ **point of increase** _at k ∈{_ 0 _, . . . , n}, if si ≤ sk for i_ = 0 _,_ 1 _, . . . , k −_ 1 _and sk ≤ sj for j_ = _k_ + 1 _, . . . , n._

- (b) _A real-valued function f has a_ **global point of increase in the interval** ( _a, b_ ) _if there is a point t ∈_ ( _a, b_ ) _such that f_ ( _s_ ) _≤ f_ ( _t_ ) _for all s ∈_ ( _a, t_ ) _and f_ ( _t_ ) _≤ f_ ( _s_ ) _for all s ∈_ ( _t, b_ ) _. t is a_ **local point of increase** _if it is a global point of increase in some interval. ⋄_

127

Theorem 5.11. _Let S_ 0 _, S_ 1 _, . . . , Sn be a simple random walk. Then_


_for all n >_ 1 _, where C does not depend on n._

The key to Theorem 5.11 is the following upper bound, which holds for more general random walks. It will be proved as Exercise 5.5.

Lemma 5.12. _For any random walk {Sj_ : _j ≥_ 0 _} on the line,_


Remark 5.13. Equation (2.4) is easy to interpret: The expected number of points of increase by time _⌊n/_ 2 _⌋_ is the numerator in (2.4), and given that there is at least one such point, the expected number is bounded below by the denominator; hence twice the ratio of these expectations bounds the required probability. _⋄_

**Proof of Theorem 5.11.** To bound the numerator in (2.4), we can use symmetry to deduce from Lemma 5.8 that


which is bounded above because the last sum is _O_ ( _n_<sup>1</sup><sup>_/_2</sup> ). Since Lemma 5.8 implies that the denominator in (2.4) is at least _C_ 1<sup>2log</sup><sup>_⌊n/_2</sup><sup>_⌋_,thiscompletestheproof.</sup>

We now see how we can use embedding ideas to pass from the result about _simple_ random walks to the result about Brownian motion.

Theorem 5.14. _Brownian motion almost surely has no local points of increase._

**Proof.** To deduce this, it suffices to apply Theorem 5.11 to a _simple_ random walk on the integers. Indeed, it clearly suffices to show that the Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ almost surely has no global points of increase in a fixed time interval ( _a, b_ ) with rational endpoints. Sampling the Brownian motion when it visits a lattice yields a simple random walk; by refining the lattice, we may make this walk as long as we wish, which will complete the proof.

More precisely, for any vertical spacing _h >_ 0 define _τ_ 0 to be the first _t ≥ a_ such that _B_ ( _t_ ) is an integral multiple of _h_ , and for _i ≥_ 0 let _τi_ +1 be the minimal _t ≥ τi_ such that _|B_ ( _t_ ) _− B_ ( _τi_ ) _|_ = _h_ . Define _Nb_ = max _{k ∈_ Z : _τk ≤ b}_ . For integers _i_ satisfying 0 _≤ i ≤ Nb_ , define


128

Then _{Si_ : _i_ = 1 _, . . . , Nb}_ is a finite portion of a simple random walk. If the Brownian motion has a (global) point of increase _t_ 0 in ( _a, b_ ) at _t_ , and if _k_ is an integer such that _τk−_ 1 _≤ t_ 0 _≤ τk_ , then this random walk has points of increase at _k −_ 1 and _k_ . If _t_ 0 _∈_ ( _a_ + _ε, b − ε_ ), for some _ε >_ 0, such a _k_ is guaranteed to exist if _|B_ ( _a_ + _ε_ ) _− B_ ( _a_ ) _| > h_ and _|B_ ( _b − ε_ ) _− B_ ( _b_ ) _| > h_ . Therefore, for all _n_ ,


Note that _Nb ≤ n_ implies _|B_ ( _b_ ) _− B_ ( _a_ ) _| ≤_ ( _n_ + 1) _h_ , so


where _Z_ has a standard normal distribution. Since _S_ 0 _, . . . , Sm_ , conditioned on _Nb_ = _m_ is a finite portion of a simple random walk, it follows from Theorem 5.11 that for some constant _C_ , we have


Thus, the probability in (2.5) can be made arbitrarily small by first taking _n_ large and then picking _h >_ 0 sufficiently small. Finally, let _ε ↓_ 0 to complete the proof.

### **3. The Skorokhod embedding problem**

In the proof of Theorem 5.4 we have made use of the fact that there exists a stopping time _T_ for linear Brownian motion with the property that E[ _T_ ] _< ∞_ and the law of _B_ ( _T_ ) is the uniform distribution on _{−_ 1 _,_ 1 _}_ . To use the same method for random walks _{Sn_ : _n ∈_ N _}_ with general increments, it would be necessary to find, for a given random variable _X_ representing an increment, a stopping time _T_ with E[ _T_ ] _< ∞_ , such that _B_ ( _T_ ) has the law of _X_ .

This problem is called the _Skorokhod embedding problem_ . By Wald’s lemmas, Theorem 2.40 and Theorem 2.44, for any integrable stopping time _T_ , we have


so that the Skorokhod embedding problem can only be solved for random variables _X_ with mean zero and finite second moment. However, these are the only restrictions, as the following result shows.

129

Theorem 5.15 (Skorokhod embedding theorem). _Suppose that {B_ ( _t_ ) : _t ≥_ 0 _} is a standard Brownian motion and that X is a real valued random variable with E_ [ _X_ ] = 0 _and E_ [ _X_<sup>2</sup> ] _< ∞. Then there exists a stopping time T , with respect to the natural filtration_ ( _F_ ( _t_ ) : _t ≥_ 0) _of the Brownian motion, such that B_ ( _T_ ) _has the law of X and_ E[ _T_ ] = _E_ [ _X_<sup>2</sup> ] _._

Example 5.16. Assume that _X_ may take two values _a < b_ . In order that _E_ [ _X_ ] = 0 we must have _a <_ 0 _< b_ and _P {X_ = _a}_ = _b/_ ( _b − a_ ) and _P {X_ = _b}_ = _−a/_ ( _b − a_ ). We have seen in Theorem 2.45 that, for the stopping time _T_ = inf _{t_ : _B_ ( _t_ ) _̸ ∈_ ( _a, b_ ) _}_ the random variable _B_ ( _T_ ) _⋄_ has the same distribution as _X_ , and that E[ _T_ ] = _−ab_ is finite.

Note that the Skorokhod embedding theorem allows us to use the arguments developed for the proof of the law of the iterated logarithm for simple random walks, Theorem 5.4, and obtain a much more general result.

Theorem 5.17 (Hartman-Wintner law of the iterated logarithm). _Let {Sn_ : _n ∈_ N _} be a random walk with increments Sn − Sn−_ 1 _of zero mean and finite variance σ_<sup>2</sup> _. Then_


We now present two proofs of the Skorokhod embedding theorem, which actually represent different constructions of the required stopping times. Both approaches, Dubins’ embedding, and the Az´ema-Yor embedding are very elegant and have their own merits.

**3.1. The Dubins’ embedding theorem.** The first one, due to Dubins [ **Du68** ], is particularly simple and based on the notion of binary splitting martingales. We say that a martingale _{Xn_ : _n ∈_ N _}_ is **binary splitting** if, whenever for some _x_ 0 _, . . . , xn ∈_ R the event


has positive probability, the random variable _Xn_ +1 conditioned on _A_ ( _x_ 0 _, . . . , xn_ ) is supported on at most two values.

Lemma 5.18. _Let X be a random variable with E_ [ _X_<sup>2</sup> ] _< ∞. Then there is binary splitting martingale {Xn_ : _n ∈_ N _} such that Xn → X almost surely and in L_<sup>2</sup> _._

**Proof.** We define the martingale _{Xn_ : _n ∈_ N _}_ and the associated filtration ( _Gn_ : _n ∈_ N) recursively. Let _G_ 0 be the trivial _σ_ -algebra and _X_ 0 = _EX_ . Define the random variable _ξ_ 0 by


For any _n >_ 0, let _Gn_ = _σ{ξ_ 0 _, . . . , ξn−_ 1 _}_ and _Xn_ = _E_ [ _X | Gn_ ]. Also define the random variable _ξn_ by


130


<!-- Start of picture text -->
4<br>3<br>2<br>−2<br>−3<br>−4<br><!-- End of picture text -->

Figure 3. Dubins’ embedding for the uniform distribution on _{−_ 4 _, −_ 2 _,_ 0 _,_ 2 _,_ 4 _}_ : First go until you hit _{−_ 3 _,_ 3 _}_ , in this picture you hit _−_ 3. Given that, continue until you hit either _−_ 2 or _−_ 4, in this picture you hit _−_ 2. Hence _B_ ( _T_ ) = _−_ 2 for this sample.

Note that _Gn_ is generated by a partition _Pn_ into 2<sup>_n_</sup> sets, each of which has the form _A_ ( _x_ 0 _, . . . , xn_ ). As each element of _Pn_ is a union of two elements of _Pn_ +1, the martingale _{Xn_ : _n ∈_ N _}_ is binary splitting. Also we have, for example as in Appendix II.(3.1), that


Hence _{Xn_ : _n ∈_ N _}_ is bounded in _L_<sup>2</sup> and, from the convergence theorem for _L_<sup>2</sup> -bounded martingales and L´evy’s upward theorem, see Theorems II.4.12 and II.4.9, we get


where _G∞_ = _σ_ �� _i∞_ =0<sup>_Gi_</sup> � _._ To conclude the proof we have to show that _X_ = _X∞_ almost surely. We claim that, almost surely,

(3.1)


Indeed, if _X_ ( _ω_ ) = _X∞_ ( _ω_ ) this is trivial. If _X_ ( _ω_ ) _< X∞_ ( _ω_ ) then for some large enough _N_ we have _X_ ( _ω_ ) _< Xn_ ( _ω_ ) for any _n > N_ , hence _ξn_ = _−_ 1 and (3.1) holds. Similarly, if _X_ ( _ω_ ) _> X∞_ ( _ω_ ) then _ξn_ = 1 for _n > N_ and so (3.1) holds.

Using that _ξn_ is _Gn_ +1-measurable, we find that


Recall that if _Yn → Y_ almost surely, and _{Yn_ : _n_ = 0 _,_ 1 _, · · · }_ is _L_<sup>2</sup> -bounded, then _EYn → EY_ (see, for example, the discussion of uniform integrability in Appendix II.3). Hence, as the left hand side of (3.1) is _L_<sup>2</sup> -bounded, we conclude that _E|X − X∞|_ = 0.

131

**Proof of Theorem 5.15.** From Lemma 5.18 we take a binary splitting martingale _{Xn_ : _n ∈_ N _}_ such that _Xn → X_ almost surely and in _L_<sup>2</sup> . Recall from the example preceding this proof that if _X_ is supported on a set two elements _{−a, b}_ for some _a, b >_ 0 then _T_ = inf _{t_ : _B_ ( _t_ ) _∈{−a, b}}_ is the required stopping time. Hence, as _Xn_ conditioned on _A_ ( _x_ 0 _, . . . , xn−_ 1) is supported on at most two values it is clear we can find a sequence of stopping times _T_ 0 _≤ T_ 1 _≤ . . ._ such that _B_ ( _Tn_ ) is distributed as _Xn_ and E _Tn_ = _E_ [ _Xn_<sup>2].As</sup><sup>_Tn_isanincreasingsequence,</sup> we have _Tn ↑ T_ almost surely for some stopping time _T_ . Also, by the monotone convergence theorem


As _B_ ( _Tn_ ) converges in distribution to _X_ by our construction, and converges almost surely to _B_ ( _T_ ) by continuity of the Brownian sample paths, we conclude that _B_ ( _T_ ) is distributed as _X_ .

**3.2. The Az´ema-Yor embedding theorem.** In this section we discuss a second solution to the Skorokhod embedding problem with a more explicit construction of the stopping times. Theorem* 5.19 (Az´ema-Yor embedding theorem). _Suppose that X is a real valued random variable with E_ [ _X_ ] = 0 _and E_ [ _X_<sup>2</sup> ] _< ∞. Let_


_and_ Ψ( _x_ ) = 0 _otherwise. For a Brownian motion {B_ ( _t_ ) : _t ≥_ 0 _} let {M_ ( _t_ ) : _t ≥_ 0 _} be the maximum process and define a stopping time τ by_


_Then_ E[ _τ_ ] = _E_ [ _X_<sup>2</sup> ] _and B_ ( _τ_ ) _has the same law as X._


<!-- Start of picture text -->
M (t)<br>B(t) T<br>Ψ −1 (M (t))<br>0 10 20 30 40 50<br><!-- End of picture text -->

Figure 4. The Az´ema-Yor embedding: the path is stopped when the Brownian motion hits the level Ψ<sup>_−_1</sup> ( _M_ ( _t_ )), where Ψ<sup>_−_1</sup> ( _x_ ) = sup _{b_ : Ψ( _b_ ) _≤ x}_ .

132

We proceed in three steps. In the first step we formulate an embedding for random variables taking only finitely many values.

Lemma 5.20. _Suppose the random variable X takes only finitely many values_


_Then T_ = _Tn−_ 1 _satisfies_ E[ _T_ ] = _E_ [ _X_<sup>2</sup> ] _and B_ ( _T_ ) _has the same law as X._


<!-- Start of picture text -->
2 y =x4    5<br>y3<br>y2<br>1 x4<br>y1<br>0 x3<br>−1 x2<br>−2 x1<br>T1 T2 T =T3 4<br><!-- End of picture text -->

Figure 5. The Az´ema-Yor embedding for the uniform distribution on the set _{−_ 2 _, −_ 1 _,_ 0 _,_ 1 _,_ 2 _}_ . The drawn path samples the value _B_ ( _T_ ) = 0 with _T_ = _T_ 4.

**Proof.** First observe that _yi ≥ xi_ +1 and equality holds if and only if _i_ = _n −_ 1. We have E[ _Tn−_ 1] _< ∞_ , by Theorem 2.45, and E[ _Tn−_ 1] = E[ _B_ ( _Tn−_ 1)<sup>2</sup> ], from Theorem 2.44. For _i_ = 1 _, . . . , n −_ 1 define random variables


Note that _Y_ 1 has expectation zero and takes on the two values _x_ 1 _, y_ 1. For _i ≥_ 2, given _Yi−_ 1 = _yi−_ 1, the random variable _Yi_ takes the values _xi, yi_ and has expectation _yi−_ 1. Given _Yi−_ 1 = _xj_ , _j ≤ i −_ 1 we have _Yi_ = _xj_ . Note that _Yn−_ 1 = _X_ . We now argue that


Clearly, _B_ ( _T_ 1) can take only the values _x_ 1 _, y_ 1 and has expectation zero, hence the law of _B_ ( _T_ 1) agrees with the law of _Y_ 1. For _i ≥_ 2, given _B_ ( _Ti−_ 1) = _yi−_ 1, the random variable _B_ ( _Ti_ ) takes the values _xi, yi_ and has expectation _yi−_ 1. Given _B_ ( _Ti−_ 1) = _xj_ where _j ≤ i −_ 1, we have _B_ ( _Ti_ ) = _xj_ . Hence the two tuples have the same law and, in particular, _B_ ( _Tn−_ 1) has the same law as _X_ .

133

In the second step, we show that the stopping time we have constructed in Lemma 5.20 agrees with the stopping time _τ_ in the Az´ema-Yor embedding.

Lemma 5.21. _The stopping time T constructed in Lemma 5.20 and the stopping time τ in Theorem 5.19 are equal._

**Proof.** Suppose that _B_ ( _Tn−_ 1) = _xi_ , and hence Ψ( _B_ ( _Tn−_ 1)) = _yi−_ 1. If _i ≤ n −_ 1, then _i_ is minimal with the property that _B_ ( _Ti_ ) = _· · ·_ = _B_ ( _Tn−_ 1) _,_ and thus _B_ ( _Ti−_ 1) _̸_ = _B_ ( _Ti_ ). Hence _M_ ( _Tn−_ 1) _≥ yi−_ 1. If _i_ = _n_ we also have _M_ ( _Tn−_ 1) = _xn ≥ yi−_ 1, which implies in any case that _τ ≤ T_ . Conversely, if _Ti−_ 1 _≤ t < Ti_ then _B_ ( _t_ ) _∈_ ( _xi, yi_ ) and this implies _M_ ( _t_ ) _< yi ≤_ Ψ( _B_ ( _t_ )). Hence _τ ≥ T_ , and altogether we have seen that _T_ = _τ_ .

This completes the proof of Theorem 5.19 for random variables taking finitely many values. The general case follows from a limiting procedure, which is left as Exercise 5.9.

### **4. The Donsker invariance principle**

Let _{Xn_ : _n ≥_ 0 _}_ be a sequence of independent and identically distributed random variables and assume that they are normalized, so that E[ _Xn_ ] = 0 and Var( _Xn_ ) = 1. This assumption is no loss of generality for _Xn_ with finite variance, since we can always consider the normalization


We look at the _random walk_ generated by the sequence


and interpolate linearly between the integer points, i.e.


This defines a random function _S ∈C_ [0 _, ∞_ ). We now define a sequence _{Sn_<sup>_∗_:</sup><sup>_n ≥_1</sup><sup>_}_of random</sup> functions in _C_ [0 _,_ 1] by


Theorem 5.22 (Donsker’s Invariance Principle). _On the space C_ [0 _,_ 1] _of continuous functions on the unit interval with the metric induced by the sup-norm, the sequence {Sn_<sup>_∗_:</sup><sup>_n≥_1</sup><sup>_}_</sup> _converges in distribution to a standard Brownian motion {B_ ( _t_ ) : _t ∈_ [0 _,_ 1] _}._

Remark 5.23. Donsker’s invariance principle is also called the _functional central limit theorem_ . The name _invariance principle_ comes from the fact that the limit in Theorem 5.22 does not depend on the choice of the exact distribution of the normalised random variables _Xn_ . _⋄_

The idea of the proof is to construct the random variables _X_ 1 _, X_ 2 _, X_ 3 _, . . ._ on the same probability space as the Brownian motion in such a way that _{Sn_<sup>_∗_:</sup><sup>_n≥_1</sup><sup>_}_iswithhighprobabilityclose</sup> to a scaling of this Brownian motion.

134

Lemma 5.24. _Suppose that {B_ ( _t_ ): _t ≥_ 0 _} a linear Brownian motion. Then, for any random variable X with mean zero and variance one, there exists a sequence of stopping times_

0 = _T_ 0 _≤ T_ 1 _≤ T_ 2 _≤ T_ 3 _≤ . . ._

_with respect to the Brownian motion, such that_

- (a) _the sequence {B_ ( _Tn_ ): _n ≥_ 0 _} has the distribution of the random walk with increments given by the law of X,_


**Proof.** Using Skorokhod embedding, we define _T_ 1 to be a stopping time with E[ _T_ 1] = 1 such that _B_ ( _T_ 1) = _X_ in distribution. By the strong Markov property,


is a Brownian motion and independent of _F_<sup>+</sup> ( _T_ 1) and, in particular, of ( _T_ 1 _, B_ ( _T_ 1)). Hence we can define a stopping time _T_ 2<sup>_′_for the Brownian motion</sup><sup>_{B_2(</sup><sup>_t_):</sup><sup>_t ≥_0</sup><sup>_}_such that E[</sup><sup>_T ′_</sup> 2<sup>] = 1 such</sup> that _B_ ( _T_ 2<sup>_′_) =</sup><sup>_X_in distribution.Then</sup><sup>_T_2=</sup><sup>_T_1+</sup><sup>_T ′_</sup> 2<sup>is a stopping time for the original Brownian</sup> motion with E[ _T_ 2] = 2, such that _B_ ( _T_ 2) is the second value in a random walk with increments given by the law of _X_ . We can proceed inductively to get a sequence 0 = _T_ 0 _≤ T_ 1 _≤ T_ 2 _≤ T_ 3 _< . . ._ such that _Sn_ = _B_ ( _Tn_ ) is the embedded random walk, and E[ _Tn_ ] = _n_ .

Abbreviate _Wn_ ( _t_ ) =<sup>_B_</sup> _~~√~~_<sup><u>(</u></sup><sup>_nt_</sup> _<u>n</u>_<sup><u>)</u>and let</sup><sup>_An_be the event that there exists</sup><sup>_t ∈_[0</sup><sup>_,_1) such that</sup><sup>_|S_</sup> _n_<sup>_∗_(</sup><sup>_t_)</sup><sup>_−_</sup> _Wn_ ( _t_ ) _| > ε_ . We have to show that P( _An_ ) _→_ 0. Let _k_ = _k_ ( _t_ ) be the unique integer with ( _k −_ 1) _/n ≤ t < k/n_ . Because _Sn_<sup>_∗_islinearonsuchanintervalwehave</sup>


As _Sk_ = _B_ ( _Tk_ ) =<sup>_√_</sup> _<u>nWn</u>_ ( _Tk/n_ ), we obtain


Note that the probability of (4.1) does not depend on _n_ . Choosing _δ >_ 0 small, we can make this probability as small as we wish, since Brownian motion is uniformly continuous on [0 _,_ 2]. It remains to show that for arbitrary, fixed _δ >_ 0, the probability of (4.2) converges to zero as _n →∞_ . To prove this we use that


135

This is Kolmogorov’s law of large numbers for the sequence _{Tk − Tk−_ 1 _}_ of independent identically distributed random variables with mean 1. Observe that for every sequence _{an}_ of reals one has


This is a matter of plain (deterministic) arithmetic and eaqsily checked. Hence we have,

(4.3)


Now recall that _t ∈_ [( _k −_ 1) _/n, k/n_ ) and let _n >_ 2 _/δ_ . Then


and by (4.3) both summands converge to 0.

**Proof of the Donsker invariance principle.** Choose the sequence of stopping times as in Lemma 5.24 and recall from the scaling property of Brownian motion that the random functions _{Wn_ ( _t_ ): 0 _≤ t ≤_ 1 _}_ given by _Wn_ ( _t_ ) = _B_ ( _nt_ ) _/_<sup>_√_</sup> _<u>n</u>_ are standard Brownian motions. Suppose that _K ⊂C_ [0 _,_ 1] is closed and define


Then P _{Sn_<sup>_∗∈K} ≤_P</sup><sup>_{Wn∈K_[</sup><sup>_ε_]</sup><sup>_}_+ P</sup><sup>_{∥S_</sup> _n_<sup>_∗−Wn∥_sup</sup><sup>_> ε} ._As</sup><sup>_n →∞_,thesecondtermgoes</sup> to 0, whereas the first term does not depnd on _n_ and is equal to P _{B ∈ K_ [ _ε_ ] _}_ for a Brownian motion _B_ . As _K_ is closed we have


Putting these facts together, we obtain lim sup _n→∞_ P _{Sn_<sup>_∗∈K}≤_P</sup><sup>_{B∈K}_,whichis</sup> condition (ii) in the Portmanteau theorem, Theorem II.1.6. Hence Donsker’s invariance principle is proved.

Below and in the following section we harvest a range of results for random walks, which we can transfer from Brownian motion by means of Donsker’s invariance principle. Readers unfamiliar with the nature of convergence in distribution are recommended to look at the appendix, Chapter II.1.

Theorem 5.25. _Suppose that {Xk_ : _k ≥_ 1 _} is a sequence of independent, identically distributed random variables with_ E[ _X_ 1] = 0 _and_ 0 _<_ E[ _X_ 1<sup>2] =</sup><sup>_σ_2</sup><sup>_< ∞.Let{Sn_:</sup><sup>_n ≥_0</sup><sup>_}betheassociated_</sup> _random walk and_


136

_its maximal value up to time n. Then, for all x ≥_ 0 _,_


**Proof.** By scaling we can assume that _σ_<sup>2</sup> = 1. Suppose now that _g_ : R _→_ R is a continuous bounded function. Define a function _G_ : _C_ [0 _,_ 1] _→_ R by


and note that _G_ is continuous and bounded. Then, by definition,

and


Hence, by Donsker’s invariance principle,


From the Portmanteau theorem, Theorem II.1.6, and the reflection principle, Theorem 2.18, we infer


and the latter probability is the given integral.

### **5. The arcsine laws**

We now discuss the two famous arcsine laws for Brownian motion and also for random walks. Their name comes from the **arcsine distribution** , which is the distribution on (0 _,_ 1) which has the density


The cumulative distribution function of an arcsine distributed random variable _X_ is therefore given by


The _first arcsine law_ describes the law of the last passage over level zero by a Brownian motion or random walk running for finite time. In the case of a Brownian motion we shall find this law by a smart calculation, and then Donsker’s invariance principle will allow us to transfer the result to random walks. Observe that the following result is surprising: the rightmost zero of Brownian motion in the interval (0 _,_ 1) is most likely to be near zero or one, see Figure 6.

137


<!-- Start of picture text -->
3.5<br>3<br>2.5<br>2<br>1.5<br>1<br>0.5<br>0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1<br><!-- End of picture text -->

Figure 6. The density of the arcsine distribution is concentrated near the boundary values 0 and 1.

Theorem 5.26 (First arcsine law for Brownian motion). _Let {B_ ( _t_ ) : _t ≥_ 0 _} be a standard linear Brownian motion. Then,_

- (a) _the random variable L_ = sup � _t ∈_ [0 _,_ 1] : _B_ ( _t_ ) = 0� _, the last zero of Brownian motion in_ [0 _,_ 1] _, is arcsine distributed, and_

- (b) _the random variable M ∈_ [0 _,_ 1] _, which is uniquely determined by B_ ( _M_ ) = max _s∈_ [0 _,_ 1] _B_ ( _s_ ) _, is arcsine distributed._

**Proof.** The discussion of local extrema in Chapter 2.1 has shown that there is indeed a unique maximum, and hence _M_ is well-defined. Moreover Theorem 2.31 shows that _M_ , which is the last zero of the process _{M_ ( _t_ ) _− B_ ( _t_ ) : _t ≥_ 0 _}_ has the same law as _L_ . Hence it suffices to prove part (b).

Recall that _{M_ ( _t_ ) : 0 _≤ t ≤_ 1 _}_ is defined by _M_ ( _t_ ) = max0 _≤s≤t B_ ( _s_ ). For _s ∈_ [0 _,_ 1],


where _{M_ 1( _t_ ) : 0 _≤ t ≤_ 1 _}_ is the maximum process of the Brownian motion _{B_ 1( _t_ ) : _t ≥_ 0 _}_ , which is given by _B_ 1( _t_ ) = _B_ ( _s − t_ ) _− B_ ( _s_ ), and _{M_ 2( _t_ ) : 0 _≤ t ≤_ 1 _}_ is the maximum process of the independent Brownian motion _{B_ 2( _t_ ) : 0 _≤ s ≤_ 1 _}_ , which is given by _B_ 2( _t_ ) = _B_ ( _s_ + _t_ ) _− B_ ( _s_ ). Since, by Theorem 2.18, for any fixed _t_ , the random variable _M_ ( _t_ ) has the same law as _|B_ ( _t_ ) _|_ , we have


138

Using the scaling invariance of Brownian motion we can express this in terms of a pair of two independent standard normal random variables _Z_ 1 and _Z_ 2 , by


In polar coordinates, ( _Z_ 1 _, Z_ 2) = ( _R_ cos _θ, R_ sin _θ_ ) pointwise. The fact that the random variable _θ_ is uniformly distributed on [0 _,_ 2 _π_ ] follows from Lemma II.3.3 in the appendix. So the last quantity becomes


It follows by differentiating that _M_ has density ( _π_

For random walks the first arc-sine law takes the form of a limit theorem, as the length of the walk tends to infinity.

Proposition 5.27 (Arcsine law for the last sign-change). _Suppose that {Xk_ : _k ≥_ 1 _} is a sequence of independent, identically distributed random variables with_ E[ _X_ 1] = 0 _and_ 0 _<_ E[ _X_ 1<sup>2] =</sup><sup>_σ_2</sup><sup>_< ∞.Let{Sn_:</sup><sup>_n ≥_0</sup><sup>_}betheassociatedrandomwalkand_</sup>


_the last time the random walk changes its sign before time n. Then, for all x ∈_ (0 _,_ 1) _,_


**Proof.** The strategy of proof is to use Theorem 5.26, and apply Donsker’s invariance principle to extend the result to random walks. As _Nn_ is unchanged under scaling of the random walk we may assume that _σ_<sup>2</sup> = 1. Define a bounded function _g_ on _C_ [0 _,_ 1] by


It is clear that _g_ ( _Sn_<sup>_∗_)differsfrom</sup><sup>_Nn/n_byaterm,whichisboundedby1</sup><sup>_/n_andtherefore</sup> vanishes asymptotically. Hence Donsker’s invariance principle would imply convergence of _Nn/n_ in distribution to _g_ ( _B_ ) = sup _{t ≤_ 1 : _B_ ( _t_ ) = 0 _}_ — if _g_ was continuous. _g_ is _not_ continuous, but we show that _g_ is continuous on the set _C_ of all _f ∈C_ [0 _,_ 1] such that _f_ takes positive and negative values in every neighbourhood of every zero and _f_ (1) _̸_ = 0. As, by Theorem 2.25, Brownian motion is almost surely in _C_ , we get from property (v) in the Portmanteau theorem, Theorem II.1.6, and by Donsker’s invariance principle, that, for every continuous bounded _h_ : R _→_ R,

_n_ lim _→∞_<sup>E</sup> � _h_ � _Nnn_ �� = _n_ lim _→∞_<sup>E</sup> � _h ◦ g_ ( _Sn_<sup>_∗_)</sup> � = E� _h ◦ g_ ( _B_ )� = E� _h_ (sup _{t ≤_ 1 : _B_ ( _t_ ) = 0 _}_ )� _,_

which completes the proof subject to the claim. To see that _g_ is continuous on _C_ , let _ε >_ 0 be given and _f ∈C_ . Let


139

and choose _δ_ 1 such that

( _−δ_ 1 _, δ_ 1) _⊂ f_ ( _g_ ( _f_ ) _− ε, g_ ( _f_ ) + _ε_ ) _._

Let 0 _< δ < δ_ 0 _∧ δ_ 1. If now _∥h − f ∥∞ < δ_ , then _h_ has no zero in ( _g_ ( _f_ ) + _ε,_ 1], but has a zero in ( _g_ ( _f_ ) _− ε, g_ ( _f_ ) + _ε_ ), because there are _s, t ∈_ ( _g_ ( _f_ ) _− ε, g_ ( _f_ ) + _ε_ ) with _h_ ( _t_ ) _<_ 0 and _h_ ( _s_ ) _>_ 0. Thus _|g_ ( _h_ ) _− g_ ( _f_ ) _| < ε_ . This shows that _g_ is continuous on _C_ .

There is a second arcsine law for Brownian motion, which describes the law of the random variable _L_ � _t ∈_ [0 _,_ 1] : _B_ ( _t_ ) _>_ 0� _,_ the time spent by Brownian motion above the _x_ -axis. This statement is much harder to derive directly for Brownian motion, though we will do this using more sophisticated tools in Chapter 8. At this stage we can use random walks to derive the result for Brownian motion.

Theorem 5.28 (Second arcsine law for Brownian motion). _Let {B_ ( _t_ ) : _t ≥_ 0 _} be a standard linear Brownian motion. Then, L_ � _t ∈_ [0 _,_ 1] : _B_ ( _t_ ) _>_ 0� _, is arcsine distributed._

The idea is to prove a direct relationship between the first maximum and the number of positive terms for a _simple_ random walk by a combinatorial argument, and then transfer this to Brownian motion using Donsker’s theorem.

Lemma 5.29 (Richard’s lemma). _Let {Sk_ : _k_ = 1 _, . . . , n} be a simple, symmetric random walk on the integers. Then_


**Proof.** Let _Xk_ = _Sk − Sk−_ 1 for each _k ∈{_ 1 _, . . . , n}_ . We rearrange the tuple ( _X_ 1 _, . . . , Xn_ ) by

- placing first in _decreasing_ order of _k_ the terms _Xk_ for which _Sk >_ 0,

_•_ and then in _increasing_ order of _k_ the _Xk_ for which _Sk ≤_ 0.

Denote the new tuple by


and let _S_<sup>�</sup> _k_ be the associated _k_<sup>th</sup> partial sum. We first show that


Indeed, suppose first that all partial sums are nonpositive, then trivially the conditional distributions are the same. Next condition on the fact that _k_ is the position of the last positive _Sk_ . Note that under this condition the tuples ( _X_ 1 _, . . . , Xk_ ) and ( _Xk_ +1 _, . . . , Xn_ ) are still independent. Moreover, the ( _X_ 1 _, . . . , Xk_ ) are independent and identically distributed random variables conditioned on the total sum being one, and therefore they are exchangeable. Hence the conditional law of of the vector ( _Xk, X_ 1 _, . . . , Xk−_ 1) is the same. Repeating this argument now for ( _X_ 1 _, . . . , Xk−_ 1) we see after finitely many steps that the two tuples have the same law.

Hence _{S_<sup>�</sup> _k_ : _k_ = 1 _, . . . , n}_ is a random walk and we now check by induction on _n_ that


Indeed, this holds trivially for _n_ = 1. When _Xn_ +1 is appended there are two possibilities:

140

- if _Sn_ +1 _>_ 0, then _X_<sup>�</sup> 1 = _Xn_ +1 and the position of the leftmost maximum in _{S_<sup>�</sup> _k_ : _k_ = 0 _, . . . , n}_ is shifted by one position to the right.

- if _Sn_ +1 _≤_ 0, then _X_<sup>�</sup> _n_ +1 = _Xn_ +1 and the position of the leftmost maximum in _{S_<sup>�</sup> _k_ : _k_ = 0 _, . . . , n}_ remains the same.

This completes the induction step and proves the lemma.

**Proof of Theorem 5.28.** Starting point is (5.1). First look at the right hand side of the equation, which divided by _n_ can be written as _g_ ( _Sn_<sup>_∗_) for the function</sup><sup>_g_:</sup><sup>_C_[0</sup><sup>_,_1]</sup><sup>_→_[0</sup><sup>_,_1] defined</sup> by


The function _g_ is continuous in every _f ∈C_ [0 _,_ 1] which has a unique maximum, hence almost everywhere with respect to the Wiener measure. Hence, by combining Donsker’s theorem and the Portmanteau theorem, the right hand side in (5.1) divided by _n_ converges to the distribution of _g_ ( _B_ ), which by Theorem 5.26 is the arcsine distribution.

Similarly, the left hand side of (5.1) can be approximated by _h_ ( _Sn_<sup>_∗_) for the function</sup><sup>_h_:</sup><sup>_C_[0</sup><sup>_,_1]</sup><sup>_→_</sup> [0 _,_ 1] defined by _. h_ ( _f_ ) = _L{t ∈_ [0 _,_ 1] : _f_ ( _t_ ) _>_ 0�

The approximation error is bounded by


which converges to zero. The function _h_ is obviously continuous in every _f ∈C_ [0 _,_ 1] with the property that


which again is equivalent to _L{t ∈_ [0 _,_ 1] : _f_ ( _t_ ) = 0� = 0 _,_ a property which Brownian motion has almost surely. Hence, by combining Donsker’s theorem and the Portmanteau theorem again, the left hand side in (5.1) divided by _n_ converges to the distribution of


and this completes the argument.

Remark 5.30. The second arcsine law for general random walks follows from this using, by now, familiar arguments, see Exercise 5.10. _⋄_

141

### **Exercises**

Exercise 5.1 ( _∗_ ). Suppose _{B_ ( _t_ ): _t ≥_ 0 _}_ is a standard linear Brownian motion. Show that


Exercise 5.2 ( _∗_ ). Derive from Theorem 5.1 that, for a _d_ -dimensional Brownian motion,


Exercise 5.3 ( _∗_ ). Suppose _{B_ ( _t_ ): _t ≥_ 0 _}_ is a linear Brownian motion and _τ_ the first hitting time of level 1. Show that, almost surely,


Exercise 5.4 ( _∗_ ). Show that there are positive constants _C_ 1 and _C_ 2 such that


**Hint.** For simple random walk a _reflection principle_ holds in quite the same way as for Brownian motion. The key to the proof is to verify that


where _Sn_<sup>_∗_istherandomwalkreflectedatthestoppingtime</sup><sup>_τ−_1= min</sup><sup>_{k_:</sup><sup>_Sk_=</sup><sup>_−_1</sup><sup>_}_.</sup>

Exercise 5.5 ( _∗_ ). Prove that, for any random walk _{Sj_ : _j ≥_ 0 _}_ on the line,


where _p_ 0 _, . . . , pn_ are as in (2.3).

142


If _A_ and _B_ are increasing events, show that


i.e. _A_ and _B_ are positively correlated.

Exercise 5.7 ( _∗_ ). Show that we can obtain a lower bound on the probability that a random walk has a point of increase that differs from the upper bound only by a constant factor. More precisely, for any random walk on the line,


where _p_ 0 _, . . . , pn_ are as in (2.3).

Exercise 5.8. Suppose _X_ 1 _, . . . , Xn_ are independent and identically distributed and consider their ordered relabeling given by _X_ (1) _≥ X_ (2) _≥ . . . ≥ X_ ( _n_ ) . Show that


provided these expectations are well-defined.

Exercise 5.9 ( _∗_ ). Given a centred random variable _X_ , show that there exist centred random variables _Xn_ taking only finitely many values, such that _Xn_ converges to _X_ in law and, for Ψ _n_ ( _x_ ) = _E_ � _Xn_ �� _Xn ≥ x_ �, the embedding stopping times


converge almost surely to _τ_ . Infer that _B_ ( _τ_ ) has the same law as _X_ , and E[ _τ_ ] = E[ _X_<sup>2</sup> ].

Exercise 5.10. Suppose that _{Xk_ : _k ≥_ 1 _}_ is a sequence of independent, identically distributed random variables with E[ _X_ 1] = 0, P _{X_ 1 = 0 _}_ = 0 and 0 _<_ E[ _X_ 1<sup>2] =</sup><sup>_σ_2</sup><sup>_< ∞_.Let</sup><sup>_{Sn_:</sup><sup>_n ≥_0</sup><sup>_}_</sup> be the associated random walk and


the number of positive values of the random walk before time _n_ . Then, for all _x ∈_ (0 _,_ 1),


143

### **Notes and Comments**

Historically, the law of the iterated logarithm was first proved for simple random walk by Khinchin [ **Kh23, Kh24** ] and later generalised to other random walks by Kolmogorov [ **Ko29** ] and Hartman and Wintner [ **HW41** ]. The original arguments of Kolmogorov, Hartman and Wintner were extremely difficult, and a lot of authors have since provided more accessible proofs, see, for example, de Acosta [ **dA83** ]. For Brownian motion the law of the iterated logarithm is also due to Khinchin [ **Kh33** ]. The idea of using embedding arguments to transfer the result from the Brownian motion to the random walk case is due to Strassen [ **St64** ]. For a survey of laws of the iterated logarithm, see [ **Bi86** ].

An extension of the law of the iterated logarithm is Strassen’s law, which is first proved in [ **St64** ]. If a standard Brownian motion on the interval [0 _, t_ ] is rescaled by a factor 1 _/t_ in time and a factor �2 _t_ log log(1 _/t_ ) in space, the set of limit points in _C_ [0 _,_ 1] are exactly the functions _f_ with _f_ (0) = 0 and �01<sup>(</sup><sup>_f ′_(</sup><sup>_t_))2</sup><sup>_dt≤_1.Strassen’slawalsoexplainstheapproximateformofthe</sup> curve in the right half of Figure 5.1. Any function in this class with _f_ (1) = 1 satisfies


which implies that _f_<sup>_′_</sup> ( _t_ ) is constant and thus _f_ ( _t_ ) = _t_ for all _t ∈_ (0 _,_ 1). Therefore, for large _t_ , the Brownian path conditioned on ending near to its upper envelope resembles a straight line in the sup-norm, as can be seen in Figure 5.1.

The nonincrease phenomenon, which is described in Theorem 5.11, holds for arbitrary symmetric random walks, and can thus be viewed as a combinatorial consequence of fluctuations in random sums. Indeed, our argument shows this — subject to a generalisation of Lemma 5.8. The latter result holds if the increments _Xi_ have a symmetric distribution, or if the increments have mean zero and finite variance, see e.g. Feller [ **Fe66** , Section XII.8]. Dvoretzky, Erd˝os and Kakutani [ **DEK61** ] were the first to prove that Brownian motion almost surely has no local points of increase. Knight [ **Kn81** ] and Berman [ **Be83** ] noted that this follows from properties of the local time of Brownian motion; direct proofs were given by Adelman [ **Ad85** ] and Burdzy [ **Bu90** ]. The proof we give is taken from [ **Pe96c** ].

A higher-dimensional analogue of this question is whether, for Brownian motion in the plane, there exists a line such that the Brownian motion path, projected onto that line, has a global point of increase, or equivalently whether the Brownian motion path admits cut lines. We say a line _ℓ_ is a _cut line_ for the Brownian motion if, for some _t_ 0 _∈_ (0 _,_ 1) with _B_ ( _t_ 0) _∈ ℓ_ , the points _B_ ( _t_ ) lies on one side of _ℓ_ for all _t ∈_ [0 _, t_ 0) and on the other side of _ℓ_ for all _t ∈_ ( _t_ 0 _,_ 1]. It was proved by Bass and Burdzy [ **BB97** ] that planar Brownian motion almost surely does _not_ have cut lines. Burdzy [ **Bu89** ], with a correction to the proof in [ **Bu95** ], however showed that Brownian motion in the plane almost surely does have _cut points_ , which are points _B_ ( _t_ ) such that the Brownian motion path with the point _B_ ( _t_ ) removed is disconnected. It was conjectured that the Hausdorff dimension of the set of cut points is 3 _/_ 4. This conjecture has recently been proved by Lawler, Schramm and Werner [ **LSW01** ], see also [ **La96a** ].

144

For Brownian motion in three dimensions, there almost surely exist cut planes, where we say _P_ is a _cut plane_ if for some _t_ , the set _{B_ ( _s_ ): 0 _< s < t}_ lies on one side of the plane and the set _{B_ ( _s_ ): 1 _> s > t}_ on the other side. This result, original due to Pemantle, is also described in Bass and Burdzy [ **BB97** ]. An argument of Evans, which is closely related to material we discuss in the final section of Chapter 10, shows that the set of times corresponding to cut planes has Hausdorff dimension zero.

Pemantle [ **Pe97** ] has shown that the range of planar Brownian motion almost surely does not cover any straight line segment. Which curves can and which cannot be covered by a Brownian motion path is, in general, an open question. Also unknown is the minimal Hausdorff dimension of curves contained in the range of planar Brownian motion, though it is known that it contains a curve of Hausdorff dimension 4/3, namely its outer boundary, see [ **LSW01** ].

Harris’ inequality was discovered by Harris [ **Ha60** ] and is also known as _FKG inequality_ in recognition of the work of Fortuin, Kasteleyn and Ginibre [ **FKG71** ] who extended the original inequality beyond the case of product measures. ‘Correlation inequalities’ like these play an extremely important role in percolation theory and spatial statistical physics. Exercise 5.8 indicates the important role of this idea in the investigation of order statistics, see Lehmann [ **Le66** ] and Bickel [ **Bi67** ] for further discussion and applications.

The Skorokhod embedding problem is a classic, which still leads to some attractive research. The first embedding theorem is due to Skorokhod [ **Sk65** ]. The Russian original of this work appeared in 1961 and the Dubins embedding, which we have presented is not much younger, see [ **Du68** ]. Our presentation, based on the idea of binary splitting martingales, follows Neveu [ **Ne75** , Ex. II.7, p 34] and we thank Jim Pitman for directing us to this reference. Another classic embedding technique is Root’s embedding, see [ **Ro69** ]. The Az´ema-Yor embedding was first described in [ **AY79** ], but we follow Meilijson [ **Me83** ] in the proof. One of the attractive features of the Az´ema-Yor embedding is that, among all stopping times _T_ with E _T < ∞_ which represent a given random variable _X_ , it maximizes the max0 _≤t≤T B_ ( _t_ ). Generalisation of the embedding problem to more general classes of probability laws require different forms of minimality for the embedding stopping time, or more general processes in which one embeds. A survey of current developments is [ **Ob04** ].

The idea of an invariance principle that allows to transfer limit theorems from special cases to general random walks can be traced to Erd˝os and Kac [ **EK46, EK47** ]. The first general result of this nature is due to Donsker [ **Do51** ] following an idea of Doob [ **Do49** ]. Besides the embedding technique carried out in our proof, there is also a popular alternative proof, which goes back to Prohorov [ **Pr56** ]. Suppose that a subsequence of _{Sn_<sup>_∗_:</sup><sup>_n≥_1</sup><sup>_}_convergesin</sup> distribution to a limit _X_ . This limit is a continuous random function, which is easily seen to have stationary, independent increments, which have expectation zero and variance equal to their length. By a general result this implies that _X_ is a Brownian motion. So Brownian motion is the only possible limit point of the sequence _{Sn_<sup>_∗_:</sup><sup>_n ≥_1</sup><sup>_}_.Thedifficultpartofthis</sup> proof is now to show that every subsequence of _{Sn_<sup>_∗_:</sup><sup>_n ≥_1</sup><sup>_}_has a convergent subsubsequence,</sup> the _tightness property_ . Many interesting applications and extensions of Donsker’s theorem can be found in [ **Bi68** ].

145

An important class of extensions of Donsker’s theorem are the strong approximation theorems which were provided by Skorokhod [ **Sk65** ] and Strassen [ **St64** ]. In these results the Brownian motion and the random walk are constructed on the same probability space in such a way that they are close almost surely. An optimal result in this direction is the famous paper of Koml´os, Major and Tusn´ady [ **KMT75** ]. For an exposition of their work and applications, see [ **CR81** ].

The arcsine laws for Brownian motion were first proved by L´evy in [ **Le39, Le48** ]. The proof of the first law, which we give here, follows Kallenberg [ **Ka02** ]. This law can also be proved by a direct calculation, which however is slightly longer, see for example [ **Du95** ]. Our proof of the second arcsine law goes back to an idea of Baxter [ **Ba62** ].

146

### CHAPTER 6

---

[← Hausdorff dimension: Techniques and applications](08-hausdorff-dimension-techniques-and-applications.md) · [Up: contents](index.md) · [Brownian local time →](10-brownian-local-time.md)
