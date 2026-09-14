---
title: Stochastic integrals and applications
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Stochastic integrals and applications

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this chapter we first construct an integral with respect to Brownian motion. Amongst the applications are the conformal invariance of Brownian motion, a short look at windings of Brownian motion, the Tanaka formula for Brownian local times, and the Feynman-Kac formula.

### **1. Stochastic integrals with respect to Brownian motion**

**1.1. Construction of the stochastic integral.** We look at a Brownian motion in dimension one _{B_ ( _t_ ) : _t ≥_ 0 _}_ considered as a random continuous function. As we have found in Theorem 1.35, this function is almost surely of unbounded variation, which is why we cannot use _Lebesgue-Stieltjes integration_ to define integrals of the form �0 _t_<sup>_f_(</sup><sup>_s_)</sup><sup>_dB_(</sup><sup>_s_).Thereishow-</sup> ever an escape from this dilemma, if one is willing to take advantage of the fact that Brownian motions are _random_ functions and therefore one can make use of weaker forms of limits. This is the idea of _stochastic integration_ .

Before explaining the procedure, we have a look at a reasonable class of integrands, as we would like to admit random functions as integrands, too. At a first reading, the reader might prefer to think of deterministic integrands only and skip the next couple of paragraphs until we begin the construction of the integral after the proof of Lemma 7.2.

A suitable class of random integrands is the class of _progressively measurable processes_ . We denote by (Ω _, A,_ P) the probability space on which our Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ is defined and suppose that ( _F_ ( _t_ ) : _t ≥_ 0) is a filtration to which the Brownian motion is adapted such that the strong Markov property holds.

Because we also want the integral up to time _t_ to be adapted to our filtration, we assume that the filtration ( _F_ ( _t_ ) : _t ≥_ 0) is **complete** , i.e. contains all sets of probability zero in _A_ . Note that every filtration can be completed simply by adding all these sets and that the completion preserves the strong Markov property.

Definition 7.1. _A process {X_ ( _t, ω_ ) : _t ≥_ 0 _, ω ∈_ Ω _} is called_ **progressively measurable** _if for each t ≥_ 0 _the mapping X_ : [0 _, t_ ] _×_ Ω _→_ R _is measurable with respect to the σ-algebra ⋄_ B([0 _, t_ ]) _× F_ ( _t_ ) _._

Lemma 7.2. _Any processes {X_ ( _t_ ): _t ≥_ 0 _}, which is adapted and either right- or left-continuous is also progressively measurable._

183

**Proof.** Assume that _{X_ ( _t_ ): _t ≥_ 0 _}_ is right-continuous. Fix _t >_ 0. For a positive integer _n_ and 0 _≤ s ≤ t_ define _Xn_ (0 _, ω_ ) = _X_ (0 _, ω_ ) and


The mapping ( _s, ω_ ) _�→ Xn_ ( _s, ω_ ) is B([0 _, t_ ]) _⊗F_ ( _t_ ) measurable. By right-continuity we have lim _n↑∞ Xn_ ( _s, ω_ ) = _X_ ( _s, ω_ ) for all _s ∈_ [0 _, t_ ] and _ω ∈_ Ω, hence the limit map ( _s, ω_ ) _�→ X_ ( _s, ω_ ) is also B([0 _, t_ ]) _⊗F_ ( _t_ ) measurable, proving progressive measurability. The left-continuous case is analogous.

The construction of the integrals is quite straightforward. We start by integrating progressively measurable step processes _{H_ ( _t, ω_ ) : _t ≥_ 0 _, ω ∈_ Ω _}_ of the form


In complete analogy to the classical case we define the integral as


Now let _H_ be a progressively measurable process satisfying E �0 _∞_<sup>_H_(</sup><sup>_s_)2</sup><sup>_ds<∞_.Suppose</sup><sup>_H_</sup> can be approximated by a family of progressively measurable step processes _Hn_ , _n ≥_ 1, then we define


At this stage we focus on _L_<sup>2</sup> -convergence, though we shall see later that the stochastic integral can also be constructed as an almost sure limit, see Remark 7.7. For the approximation of _H_ by progressively measurable step processes we look at the norm


What we have to show now to complete the definition is that,

- (1) every progressively measurable process satisfying E �0 _∞_<sup>_H_(</sup><sup>_s_)2</sup><sup>_ds < ∞_canbeapproxi-</sup> mated in the _∥· ∥_ 2 norm by progressively measurable step processes,

- (2) for each approximating sequence the limit in (1.1) exists,

- (3) and this limit does not depend on the choice of the approximating step processes.

This is what we check now, beginning with item (1).

Lemma 7.3. _For every progressively measurable process {H_ ( _s, ω_ ) : _s ≥_ 0 _, ω ∈_ Ω _} satisfying_ E �0 _∞_<sup>_H_(</sup><sup>_s_)2</sup><sup>_ds<∞thereexistsasequence{Hn_:</sup><sup>_n∈_N</sup><sup>_}ofprogressivelymeasurablestep_</sup> _processes such that_ lim _n→∞ ∥Hn − H∥_ 2 = 0 _._

184

**Proof.** The strategy is to approximate the progressively measurable process successively by

- a bounded progressively measurable process,

- a bounded, almost surely continuous progressively measurable process,

- and finally, by a progressively measurable step process.

Let _{H_ ( _s, ω_ ) : _s ≥_ 0 _, ω ∈_ Ω _}_ be a progressively measurable process with _∥H∥_ 2 _< ∞_ . We _first_ define the cut-off at a fixed time _n >_ 0 by letting _Hn_ ( _s, ω_ ) = _H_ ( _s, ω_ ) for _s ≤ n_ and _Hn_ ( _s, ω_ ) = 0 otherwise. Clearly lim _n↑∞ ∥Hn − H∥_ 2 = 0 _._

_Second_ , we approximate any progressively measurable _H_ on a finite interval by truncating its values, i.e. for large _n_ we define _Hn_ by letting _Hn_ ( _s, ω_ ) = _H_ ( _s, ω_ ) _∧ n_ . Clearly _Hn_ is progressively measurable and lim _n↑∞ ∥Hn − H∥_ 2 = 0 _._

_Third_ , we approximate any uniformly bounded progressively measurable _H_ by a bounded, almost-surely continuous, progressively measurable process. Let _h_ = 1 _/n_ and, using the convention _H_ ( _s, ω_ ) = _H_ (0 _, ω_ ) for _s <_ 0 we define


Because we only take an average over the past, _Hn_ is again progressively measurable. It is almost surely continuous and it is a well-known fact that, for every _ω ∈_ Ωand almost every _s ∈_ [0 _, t_ ],


Since _H_ is uniformly bounded (and using progressive measurability) we can take expectations and an average over time, and obtain from the bounded convergence theorem that


Finally, a bounded, almost-surely continuous, progressively measurable process can be approximated by a step process _Hn_ by taking _Hn_ ( _s, ω_ ) = _H_ ( _j/n, ω_ ) for _j/n ≤ s <_ ( _j_ + 1) _/n_ . These functions are again progressively measurable and one easily sees lim _n↑∞ ∥Hn − H∥_ 2 = 0 _._ This completes the approximation.

The following lemma describes the crucial property of the integral of step processes.

Lemma 7.4. _Let H be a progressively measurable step process and_ E �0 _∞_<sup>_H_(</sup><sup>_s_)2</sup><sup>_ds < ∞,then_</sup>


185

**Proof.** We use the Markov property to see that, for every progressively measurable step process _H_ =<sup>�</sup><sup>_k_</sup> _i_ =1<sup>_Ai_1(</sup><sup>_a_</sup> _i_<sup>_,a_</sup> _i_ +1<sup>]</sup><sup>_,_</sup>


Corollary 7.5. _Suppose {Hn_ : _n ∈_ N _} is a sequence of progressively measurable step processes such that_


_then_


**Proof.** Because the difference of two step processes is again a step process, Lemma 7.4 can be applied to _Hn − Hm_ and this gives the statement.

The following theorem addresses issues (2) and (3), thus completing our construction of the stochastic integral.

Theorem 7.6. _Suppose {Hn_ : _n ∈_ N _} is a sequence of progressively measurable step processes and H a progressively measurable process such that_


_then_


_exists and is independent of the choice of {Hn_ : _n ∈_ N _}. Moreover, we have_

(1.2)


186

Remark 7.7. If the sequence of step processes is chosen such that


**Proof of Theorem 7.6.** By the triangle inequality _{Hn_ : _n ∈_ N _}_ satisfies the assumption of Corollary 7.5, and hence _{_ �0 _∞_<sup>_Hn_(</sup><sup>_s_)</sup><sup>_dB_(</sup><sup>_s_):</sup><sup>_n∈_N</sup><sup>_}_isaCauchysequenceinL2(P).By</sup> completeness of this space, the limit exists, and Corollary 7.5 also shows that the limit is independent of the choice of the approximating sequence. The last statement follows from Lemma 7.4, applied to _Hn_ , by taking the limit _n →∞_ .

Finally, we describe the stochastic integral as a stochastic process in time. The crucial property of this process are continuity and the _martingale property_ stated in the next theorem.

Definition 7.8. _Suppose {H_ ( _s, ω_ ): _s ≥_ 0 _, ω ∈_ Ω _} is progressively measurable with_ E �0 _t_<sup>_H_(</sup><sup>_s, ω_)2</sup><sup>_ds < ∞.Definetheprogressivelymeasurableprocess{Ht_(</sup><sup>_s, ω_):</sup><sup>_s ≥_0</sup><sup>_, ω∈_Ω</sup><sup>_}by_</sup> _H_<sup>_t_</sup> ( _s, ω_ ) = _H_ ( _s, ω_ ) 1 _{s ≤ t} ._

_Then the_ **stochastic integral up to** _t is defined as,_


Definition 7.9. _We say that a stochastic process {X_ ( _t_ ): _t ≥_ 0 _} is a_ **modification** _of a ⋄ process {Y_ ( _t_ ): _t ≥_ 0 _} if, for every t ≥_ 0 _, we have_ P _{X_ ( _t_ ) = _Y_ ( _t_ ) _}_ = 1 _._

Theorem 7.10. _Suppose the process {H_ ( _s, ω_ ): _s ≥_ 0 _, ω ∈_ Ω _} is progressively measurable with_


_Then there exists an almost surely continuous modification of {_ �0 _t_<sup>_H_(</sup><sup>_s_)</sup><sup>_dB_(</sup><sup>_s_):</sup><sup>_t≥_0</sup><sup>_}.More-_</sup> _over, this process is a martingale and hence_


187

**Proof.** Fix a large integer _t_ 0 and let _Hn_ be a sequence of step processes such that _∥Hn − H_<sup>_t_0</sup> _∥_ 2 _→_ 0, and therefore


Obviously, for any _s ≤ t_ the random variable �0 _s_<sup>_Hn_(</sup><sup>_u_)</sup><sup>_dB_(</sup><sup>_u_)is</sup><sup>_F_(</sup><sup>_s_)-measurableand</sup> � _st_<sup>_Hn_(</sup><sup>_u_)</sup><sup>_dB_(</sup><sup>_u_)isindependentof</sup><sup>_F_(</sup><sup>_s_),meaningthattheprocess</sup>


is a martingale, for every _n_ . For any 0 _≤ t ≤ t_ 0 define


so that _{X_ ( _t_ ) : 0 _≤ t ≤ t_ 0 _}_ is also a martingale and


By Doob’s maximal inequality, Proposition 2.39, for _p_ = 2,

which converges to zero, as _n →∞_ . This implies, in particular, that almost surely, the process _{X_ ( _t_ ) : 0 _≤ t ≤ t_ 0 _}_ is a uniform limit of continuous processes, and hence continuous. For fixed 0 _≤ t ≤ t_ 0, by taking _L_<sup>2</sup> -limits from the step process approximation, the random variable �0 _t_<sup>_H_(</sup><sup>_s_)</sup><sup>_dB_(</sup><sup>_s_) is</sup><sup>_F_(</sup><sup>_t_)-measurable and</sup> � _tt_ 0<sup>_H_(</sup><sup>_s_)</sup><sup>_dB_(</sup><sup>_s_) is independent of</sup><sup>_F_(</sup><sup>_t_) with zero</sup> expectation. Therefore �0 _t_<sup>_H_(</sup><sup>_s_)</sup><sup>_dB_(</sup><sup>_s_)isaconditionalexpectationof</sup><sup>_X_(</sup><sup>_t_0)given</sup><sup>_F_(</sup><sup>_t_),hence</sup> coinciding with _X_ ( _t_ ) almost surely.

We now have a basic stochastic integral at our disposal. Obviously, a lot of bells and whistles can be added to this construction, but we refrain from doing so and keep focused on the essential properties and eventually on the applications to Brownian motion.

**1.2. Itˆo’s formula.** For stochastic integration Itˆo’s formula plays the same role as the fundamental theorem of calculus for classical integration. Let _f_ be continuously differentiable and _x_ : [0 _, ∞_ ) _→_ R, then the fundamental theorem can be written as


and this formula holds when _x_ is continuous and of bounded variation. Itˆo’s formula offers an analogue of this for the case that _x_ is a Brownian motion. The crucial difference is that a third term enters, which makes the existence of a second derivative of _f_ necessary. The next result, a key step in the derivation of this formula, is an extension of Exercise 1.14.

188

Theorem 7.11. _Suppose f_ : R _→_ R _is continuous, t >_ 0 _, and_ 0 = _t_ (1 _n_ ) _< . . . < t_ ( _nn_ ) = _t are partitions of the interval_ [0 _, t_ ] _, such that the mesh converges to zero. Then, in probability,_


**Proof.** Let _T_ be the first exit time from a compact interval. It suffices to prove the statement for Brownian motion stopped at _T_ , as the interval may be chosen to make P _{T < t}_ arbitrarily small. By continuity of _f_ and the definition of the Riemann integral, almost surely,


It thus suffices to show that


Recall that _{B_ ( _t_ )<sup>2</sup> _− t_ : _t ≥_ 0 _}_ is a martingale, by Lemma 2.43, and hence, for all _r ≤ s_ , E�� _B_ ( _s_ ) _− B_ ( _r_ )�2 _−_ ( _s − r_ ) �� _F_ ( _r_ )� = 0 _._

This allows us to simplify the previous expression as follows,


We can now bound _f_ by its maximum on the compact interval, and multiplying out the square and dropping a negative cross term we get an upper bound, which is a constant multiple of


Using Brownian scaling on the first term, we see that this expression is bounded by a constant multiple of


where ∆( _n_ ) denotes the mesh, which goes to zero. This completes the proof.

We are now able to formulate and prove a first version of Itˆo’s formula.

Theorem 7.12 (Itˆo’s formula I). _Let f_ : R _→_ R _be twice continuously differentiable such that_ E �0 _t_<sup>_f ′_�</sup> _B_ ( _s_ )�2 _ds < ∞ for some t >_ 0 _. Then, almost surely, for all_ 0 _≤ s ≤ t,_


189

**Proof.** We denote the modulus of continuity of _f_<sup>_′′_</sup> on [ _−M, M_ ] by


Then, by Taylor’s formula, for any _x, y ∈_ [ _−M, M_ ] with _|x − y| < δ_ ,

�� _f_ ( _y_ ) _− f_ ( _x_ ) _− f ′_ ( _x_ )( _y − x_ ) _−_ 21<sup>_f ′′_(</sup><sup>_x_)(</sup><sup>_y −x_)2��</sup><sup>_≤ω_(</sup><sup>_δ, M_) (</sup><sup>_y −x_)2</sup><sup>_._</sup> Now, for any sequence 0 = _t_ 1 _< . . . < tn_ = _t_ with _δB_ := max1 _≤i≤n−_ 1 �� _B_ ( _ti_ +1) _− B_ ( _ti_ )�� and _MB_ = max0 _≤s≤t |B_ ( _s_ ) _|_ , we get


Note that the first sum is simply _f_ ( _B_ ( _t_ )) _− f_ ( _B_ (0)). By the definition of the stochastic integral and Theorem 7.11 we can choose a sequence of partitions with mesh going to zero, such that, almost surely, the first subtracted term on the left converges to �0 _t_<sup>_f ′_�</sup> _B_ ( _s_ )� _dB_ ( _s_ ), the second subtracted term converges to<sup><u>1</u></sup> 2 �0 _t_<sup>_f ′′_�</sup> _B_ ( _s_ )� _ds_ , and the sum on the right hand side converges to _t_ . By continuity of the Brownian path _ω_ ( _δB, MB_ ) converges almost surely to zero. This proves Itˆo’s formula for fixed _t_ , or indeed almost surely for all rational times 0 _≤ s ≤ t_ . As all the terms in Itˆo’s formula are continuous almost surely, we get the result simultaneously for all 0 _≤ s ≤ t_ .

Next, we provide an enhanced version of Itˆo’s formula, which allows the function _f_ to depend not only on the position of Brownian motion, but also on a second argument, which is assumed to be increasing in time.

Theorem 7.13 (Itˆo’s formula II). _Suppose {ζ_ ( _s_ ): _s ≥_ 0 _} is an increasing, continuous adapted stochastic process. Let f_ : R _×_ R _→_ R _be twice continuously differentiable in the x-coordiante, and once continuously differentiable in the y-coordinate. Assume that_


_for some t >_ 0 _. Then, almost surely, for all_ 0 _≤ s ≤ t,_


190

**Proof.** To begin with, we inspect the proof of Theorem 7.11 and see that it carries over without difficulty to the situation, when _f_ is allowed to depend additionally on an adapted process _{ζ_ ( _s_ ): _s ≥_ 0 _}_ , i.e. we have for any partitions 0 = _t_ (1 _n_ ) _< . . . < t_ ( _nn_ ) = _t_ with mesh going to zero, in probability,


We denote the modulus of continuity of _∂yf_ by


and the modulus of continuity of _∂xxf_ by


Now take _x, x_ 0 _, y, y_ 0 _∈_ [ _−M, M_ ] with _|x − x_ 0 _| ∧|y − y_ 0 _| < δ_ . By the mean value theorem, there exists a value _y_ ˜ _∈_ [ _−M, M_ ] with the property that _|y_ ˜ _− y| ∧|y_ ˜ _− y_ 0 _| < δ_ such that


and hence


Taylor’s formula implies that

�� _f_ ( _x, y_ 0) _− f_ ( _x_ 0 _, y_ 0) _− ∂xf_ ( _x_ 0 _, y_ 0)( _x − x_ 0) _−_ <u>12</u><sup>_∂xxf_(</sup><sup>_x_0</sup><sup>_, y_0)(</sup><sup>_x −x_0)2��</sup><sup>_≤ω_2(</sup><sup>_δ, M_)(</sup><sup>_x −x_0)2</sup><sup>_._</sup>

Combining the last two formulas using the triangle inequality, we get that


and


We get from (1.5),


191

We can choose a sequence of partitions with mesh going to zero, such that, almost surely, the following convergence statements hold,

- the first sum on the left converges to �0 _t_<sup>_∂xf_</sup> � _B_ ( _s_ ) _, ζ_ ( _s_ )� _dB_ ( _s_ ) by the definition of the stochastic integral,

- _•_ the second sum on the left converges to �0 _t_<sup>_∂yf_</sup> � _B_ ( _s_ ) _, ζ_ ( _s_ )� _dζ_ ( _s_ ) by definition of the Stieltjes integral,

- _•_ the third sum on the left converges to 2<sup><u>1</u></sup> �0 _t_<sup>_∂xxf_</sup> � _B_ ( _s_ ) _, ζ_ ( _s_ )� _ds_ by (1.4),

- the sum on the right hand side converges to _t_ by Theorem 7.11.

By continuity of the Brownian path _ω_ 1( _δ, M_ ) and _ω_ 2( _δ, M_ ) converge almost surely to zero. This proves the enhanced Itˆo’s formula for fixed _t_ , and looking at rationals and exploiting continuity as before, we get the result simultaneously for all 0 _≤ s ≤ t_ .

With exactly the same technique, we obtain a version of Itˆo’s formula for higher dimensional Brownian motion. The detailed proof will be an exercise, see Exercise 7.3. To give a pleasant formulation, we introduce some notation for functions _f_ : R<sup>_d_+</sup><sup>_m_</sup> _→_ R, where we interpret the argument as two vectors, _x ∈_ R<sup>_d_</sup> and _y ∈_ R<sup>_m_</sup> . We write _∂j_ for the partial derivative in direction of the _j_ th coordinate, and


for the vector of derivatives in the directions of _x_ , respectively _y_ . For integrals we use the scalar product notation


and


Finally, for the Laplacian in the _x_ -variable we write


Theorem 7.14 (Multidimensional Itˆo’s formula). _Let {B_ ( _t_ ) : _t ≥_ 0 _} be a d-dimensional Brownian motion and suppose {ζ_ ( _s_ ): _s ≥_ 0 _} is a continuous, adapted stochastic process with values in_ R<sup>_m_</sup> _and increasing components. Let f_ : R<sup>_d_+</sup><sup>_m_</sup> _→_ R _be such that the partial derivatives ∂if and ∂jkf exist for all_ 1 _≤ j, k ≤ d,_ 1 _≤ i ≤ d_ + _m and are continuous. If, for some t >_ 0 _,_


192

_then, almost surely, for all_ 0 _≤ s ≤ t,_


Remark 7.15. As the Itˆo formula holds almost surely simultaneously for all times _s ∈_ [0 _, t_ ], it also holds for stopping times bounded by _t_ . Suppose now that _f_ : _U →_ R satisfies the differentiability conditions on an open set _U_ , and _K ⊂ U_ is compact. Then there exists _f_<sup>_∗_</sup> : R<sup>_m_</sup> _→_ R with _f_<sup>_∗_</sup> = _f_ on _K_ , which satisfies the conditions of Theorem 7.14. Let _T_ be the first exit time from _K_ . Applying Theorem 7.14 to _f_<sup>_∗_</sup> yields (1.6) for _f_ , almost surely, for all times _s ∧ T_ , for _s ≤ t_ . _⋄_

To appreciate the following discussion, we introduce a localisation of the notion of a martingale.

Definition 7.16. _An adapted stochastic process {X_ ( _t_ ): 0 _≤ t ≤ T } is called a_ **local martingale** _if there exist stopping times Tn, which are almost surely increasing to T , such ⋄ that {X_ ( _t ∧ Tn_ ): _t ≥_ 0 _} is a martingale, for every n._

The following theorem is a substantial extension of Corollary 2.49.

Theorem 7.17. _Let D ⊂_ R<sup>_d_</sup> _be a domain and f_ : _D →_ R _be harmonic on D. Suppose that {B_ ( _t_ ): 0 _≤ t ≤ T } is a Brownian motion started inside D and stopped at the time T when it first exits the domain D._


**Proof.** Suppose that _Kn_ , _n ∈_ N, is an increasing sequence of compact sets whose union is _D_ , and let _Tn_ be the associated exit times. By Theorem 7.14 in conjunction with Remark 7.15,


whence _{f_ � _B_ ( _t ∧ Tn_ )� : _t ≥_ 0 _}_ is a martingale, which proves (a). Obviously, almost surely,


193

For any _t ≥_ 0, the process _{f_ ( _B_ ( _t ∧ Tn_ )) : _n ∈_ N _}_ is a discrete-time martingale by the optional stopping theorem. By our integrability assumption,


so that the martingale is _L_<sup>2</sup> -bounded and convergence in (1.7) holds in the _L_<sup>1</sup> -sense. Taking limits in the equation


first for _m ↑∞_ , then _n ↑∞_ , gives


This shows that _{f_ ( _B_ ( _t ∧ T_ )) : _t ≥_ 0 _}_ is a martingale and completes the proof.

Example 7.18. The radially symmetric functions (related to the radial potential),


are harmonic on the domain R<sup>_d_</sup> _\ {_ 0 _}_ . For a _d_ -dimensional Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ with _B_ (0) _̸_ = 0, the process _{f_ ( _B_ ( _t_ )): _t ≥_ 0 _}_ is however not a martingale. Indeed, it is a straightforward calculation to verify that


and


contradicting the martingale property. Hence the integrability condition in Theorem 7.17(b) cannot be dropped without replacement, a local martingale is not necessarily a martingale. _⋄_

### **2. Conformal invariance and winding numbers**

We now focus on planar Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ and formulate an invariance property which is at the heart of the role of Brownian motion in the context of planar random curves. Throughout this section we use the identification of R<sup>2</sup> and C and use complex notation when it is convenient.

To motivate the main result suppose that _f_ : C _→_ C is **analytic** , i.e. everywhere complex differentiable, and write _f_ = _f_ 1 + **i** _f_ 2 for the decomposition of _f_ into a real and an imaginary part. Then, by the Cauchy-Riemann equations _∂_ 1 _f_ 1 = _∂_ 2 _f_ 2 and _∂_ 2 _f_ 1 = _−∂_ 1 _f_ 2, we have ∆ _f_ 1 = ∆ _f_ 2 = 0. Then Itˆo’s formula (if applicable) states that almost surely, for every _t ≥_ 0,


194

where _dB_ ( _s_ ) is short for _dB_ 1( _s_ ) + **i** _dB_ 2( _s_ ) with _B_ ( _s_ ) = _B_ 1( _s_ ) + **i** _B_ 2( _s_ ). The right hand side defines a continuous process with independent increments, and it is at least plausible that they are Gaussian. Moreover, its expectation vanishes and


suggesting that _{f_ ( _B_ ( _t_ )) : _t ≥_ 0 _}_ is a Brownian motion ‘travelling’ with the modified speed


To turn this heuristic into a powerful theorem we allow the function to be an analytic map _f_ : _U → V_ between domains in the plane. Recall that such a map is called **conformal** if it is a bijection.

Theorem 7.19. _Let U be a domain in the complex plane, x ∈ U , and let f_ : _U → V be analytic. Let {B_ ( _t_ ) : _t ≥_ 0 _} be a planar Brownian motion started in x and_


_its first exit time from the domain U . Then the process {f_ ( _B_ ( _t_ )) : 0 _≤ t ≤ τU } is a timechanged Brownian motion, i.e. there exists a planar Brownian motion {B_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _} such that, for any t ∈_ [0 _, τU_ ) _,_


_If, additionally, f is conformal, then ζ_ ( _τU_ ) _is the first exit time from V by {B_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _}._

Remark 7.20. Note that, as _f_ is complex differentiable, the derivative _Df_ ( _x_ ) is just multiplication by a complex number _f_<sup>_′_</sup> ( _x_ ), and _f_ can be approximated locally around _x_ by its tangent _z �→ f_ ( _x_ ) + _f_<sup>_′_</sup> ( _x_ )( _z − x_ ). The derivative of the time change is


Remark 7.21. The famous _Riemann mapping theorem_ states that for any pair of simply connected open sets _U, V_ ⊊C there exists a conformal mapping _f_ : _U → V_ , see [ **Ru86** , 14.8]. This ensures that there are plenty of examples for Theorem 7.19. _⋄_

_⋄_

**Proof.** Note first that the derivative of _f_ is nonzero except for an at most countable set of points, which does not have a limit point in _U_ . As this set is not hit by Brownian motion, we may remove it from _U_ and note that the resulting set is still open We may therefore assume that _f_ has nonvanishing derivative everywhere on _U_ .

We may also assume, without loss of generality, that _f_ is a mapping between _bounded_ domains. Otherwise choose _Un ⊂ Kn ⊂ U_ such that _Un_ is open with<sup>�</sup> _Un_ = _U_ and _Kn_ is compact, which implies that _Vn_ = _f_ ( _Un_ ) is bounded. Then _{f_ ( _B_ ( _t_ )) : _t ≤ τUn}_ is a time-changed Brownian motion for all _n_ , and this extends immediately to _{f_ ( _B_ ( _t_ )) : _t ≤ τU }_ .

195

The main argument of the proof is based on stochastic integration. Recall that the CauchyRiemann equations imply that the vectors _∇f_ 1 and _∇f_ 2 are orthogonal and _|∇f_ 1 _|_ = _|∇f_ 2 _|_ = _|f_<sup>_′_</sup> _|_ . We start by defining for each _t ≥_ 0, a stopping time


which represents the inverse of the time change. Let _{B_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _}_ be a Brownian motion independent of _{B_ ( _t_ ) : _t ≥_ 0 _}_ , and define a process _{W_ ( _t_ ) : _t ≥_ 0 _}_ by


In rough words, at the random time _ζ_ ( _τU_ ) an independent Brownian motion is attached at the endpoint of the process _{f_ ( _B_ ( _σ_ ( _t_ ))) : 0 _≤ t ≤ ζ_ ( _τU_ ) _}_ . Denote by _G_ ( _t_ ) the _σ_ -algebra generated by _{W_ ( _s_ ) : _s ≤ t}_ . It suffices to prove that the process _{W_ ( _t_ ) : _t ≥_ 0 _}_ is a Brownian motion. It is obvious that the process is continuous almost surely and hence it suffices to show that its finite dimensional marginal distributions coincide with those of a Brownian motion. Recalling the Laplace transform of the bivariate normal distribution, this is equivalent to showing that, for any 0 _≤ s ≤ t_ and _λ ∈_ C,


where we have used _⟨· , · ⟩_ to denote the scalar product. This follows directly once we show that, for _x ∈ U_ ,


For simplicity of notation we may assume _s_ = 0. For the proof we first evaluate the expectation with respect to the independent Brownian motion _{B_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _}_ inside, which gives

E� _e_<sup>_⟨λ,W_(</sup><sup>_t_)</sup><sup>_⟩_��</sup> _W_ (0) = _f_ ( _x_ )� = E _x_ exp � _⟨λ, f_ ( _B_ ( _σ_ ( _t_ ) _∧ τU_ ))� +<sup><u>1</u></sup> 2<sup>_|λ|_2 �</sup> _t − ζ_ ( _σ_ ( _t_ ) _∧ τU_ )�<sup>�</sup> _._

We use the multidimensional Itˆo’s formula for the bounded mapping


which is defined on _U ×_ R, see Remark 7.15. To prepare this, note that _∂iie_<sup>_g_</sup> = [ _∂iig_ + ( _∂ig_ )<sup>2</sup> _e_<sup>_g_</sup> ] and hence

(2.2) ∆ _e_<sup>_g_</sup> = [∆ _g_ + _|∇g|_<sup>2</sup> ] _e_<sup>_g_</sup> _._

For _g_ = _⟨λ, f ⟩_ we have _∇g_ =<sup>�2</sup> _i_ =1<sup>_λi∇fi_,whichimplies</sup><sup>_|∇g|_2=</sup><sup>_|λ|_2</sup><sup>_|f ′|_2asthevectors</sup><sup>_∇fi_</sup> are orthogonal with norm _|f_<sup>_′_</sup> _|_ . Moreover, ∆ _g_ = 0 by the analyticity of _f_ . Applying (2.2) gives


Moreover, we have


We now let _Un_ = _{x ∈ U_ : _| x − y| ≥ n_<sup><u>1</u>forall</sup><sup>_y∈∂U}_.Then</sup><sup>_|f ′_(</sup><sup>_x_)</sup><sup>_|_isboundedawayfrom</sup> zero on _Un_ and therefore the stopping time _T_ = _σ_ ( _t_ ) _∧ τUn_ is bounded. The multidimensional

196

version of Itˆo’s formula gives, almost surely,


Looking back at the two preparatory displays and recalling that _dζ_ ( _u_ ) = _|f_<sup>_′_</sup> ( _B_ ( _u_ )) _|_<sup>2</sup> _du_ we see that the two terms in the second line cancel each other. Making use of bounded convergence and the fact that the stochastic integral has zero expectation, see Exercise 7.1, we obtain that


This shows (2.1) and completes the proof.

As a first application we look at harmonic measure and exploit its conformal invariance in order to calculate it explicitly in a special case.

Theorem 7.22. _Suppose U, V ⊂_ R<sup>2</sup> _are domains and f_ : _U_<sup>¯</sup> _→ V_<sup>¯</sup> _is continuous and maps U conformally into V ._

(a) _If x ∈ U , then µ∂U_ ( _x, ·_ ) _◦ f_<sup>_−_1</sup> = _µ∂V_ ( _f_ ( _x_ ) _, ·_ ) _._

- (b) _Suppose additionally that U_ = _K_<sup>c</sup> _and V_ = _L_<sup>c</sup> _are the complement of compact sets and_ lim _x→∞ f_ ( _x_ ) = _∞. Then_


**Proof.** (a) follows from Theorem 7.19 together with the continuity of _f_ on _U_<sup>¯</sup> , which ensures that the first hitting point of _∂U_ by a Brownian motion is mapped onto the first hitting point of _∂V_ by its conformal image. For (b) tahe the limit _x →∞_ and recall Theorem 3.45.

Example 7.23. We find the harmonic measure from infinity on the unit interval


Starting point is the harmonic measure on the circle _∂B_ (0 _,_ 1), which we know is the uniform distribution _ϖ_ . Let _U_ be the complement of the unit ball _B_ (0 _,_ 1) and _V_ the complement of the interval [ _−,_ 1 _,_ 1], and take the conformal mapping


which satisfies our conditions. Hence _ϖ◦f_<sup>_−_1</sup> is the harmonic measure on [ _−_ 1 _,_ 1]. If _z_ = _x_ + **i** _y_ = cos _θ_ + **i** sin _θ ∈ ∂B_ (0 _,_ 1), then _|f_<sup>_′_</sup> ( _z_ ) _|_<sup>2</sup> = sin<sup>2</sup> _θ_ , and hence _|f_<sup>_′_</sup> ( _z_ ) _|_ = _|y|_ = _√_ 1 _− x_<sup>2</sup> . Recalling that every _x ∈_ [ _−_ 1 _,_ 1] has two preimages, we get that the density of _ϖ ◦ f_<sup>_−_1</sup> at _x_ = cos _θ_ is


197

Mapping _V_ via _z �→ z_<sup>2</sup> onto the complement of [0 _,_ 1], noting that _|f_<sup>_′_</sup> ( _z_ ) _|_ = 2 _|z|_ and that again we have two preimages, we obtain that the harmonic measure on [0 _,_ 1] is


_⋄_ which is the Beta(<sup><u>1</u></sup> 2<sup>_,_</sup> 2<sup><u>1</u>)distribution.</sup>

As a further important application of conformal invariance we calculate the probability that a planar Brownian motion exits a cone before leaving a disc, see Figure 1.


<!-- Start of picture text -->
r<br>1<br>0 x<br><!-- End of picture text -->

Figure 1. The Brownian path does not exit the cone before leaving the disc.

Theorem 7.24. _Let α ∈_ (0 _,_ 2 _π_ ] _and denote by W_ [ _α_ ] _an open cone with vertex in the origin, symmetric about the x-axis, with opening angle α. Let {B_ ( _t_ ) : _t ≥_ 0 _} be planar Brownian motion started in x_ = (1 _,_ 0) _, and denote T_ ( _r_ ) = inf _{t ≥_ 0 : _|B_ ( _t_ ) _|_ = _r}. Then, for r >_ 1 _,_


**Proof.** For ease of notation we identify R<sup>2</sup> with the complex plane. In the first step we use the conformal map _f_ : _W_ [ _α_ ] _→ W_ [ _π_ ] defined by _f_ ( _x_ ) = _x_<sup>_π/α_</sup> to map the cone onto a halfspace. Let _B_<sup>_∗_</sup> = _f ◦ B_ , which by conformal invariance is a time-changed Brownian motion started in the point _B_<sup>_∗_</sup> (0) = 1. We thus have that


It therefore suffices to show the result in the case _α_ = _π_ . So let _{B_ ( _t_ ) : _t ≥_ 0 _}_ be a Brownian motion started in _B_ (0) = 1 and look at the stopping time _S_ = min _{t ≥_ 0 : Re( _B_ ( _t_ )) _≤_ 0 _}_ . We use reflection on the imaginary axis, i.e. for _f_ ( _x, y_ ) = ( _−x, y_ ) we let


Then _B_<sup>�</sup> is a Brownian motion started in _B_<sup>�</sup> (0) = 1 and, for _T_<sup>�</sup> ( _r_ ) = inf _{t ≥_ 0 : _|B_<sup>�</sup> ( _t_ ) _|_ = _r}_ , P _{_ Re( _B_ ( _T_ ( _r_ ))) _>_ 0 _}_ = P _{_ Re( _B_ ( _T_ ( _r_ ))) _>_ 0 _, T_ ( _r_ ) _< S}_ + P _{_ Re( _B_ ( _T_ ( _r_ ))) _>_ 0 _, T_ ( _r_ ) _> S}_ = P _{T_ ( _r_ ) _< S}_ + P _{_ Re( _B_<sup>�</sup> ( _T_<sup>�</sup> ( _r_ ))) _<_ 0 _}._

198

As _{T_ ( _r_ ) _< S}_ is the event whose probability we need to bound, it just remains to find


By Brownian scaling we may assume that the Brownian motion is started at _B_ (0) = 1 _/r_ and _T_ = min _{t ≥_ 0 : _|B_ ( _t_ ) _|_ = 1 _}_ . We apply the conformal map


which is a M¨obius transformation mapping the starting point of the Brownian motion to the origin and fixing the point 1. As this maps the segment _{z ∈ ∂B_ (0 _,_ 1) : Re( _z_ ) _<_ 0 _}_ onto a segment of length 2 arctan<sup>_<u>r</u>_2</sup> 2<sup>_−_</sup> _r_<sup><u>1</u></sup> we obtain the result.

The next result represents planar Brownian motion in polar coordinates. Again we identify R<sup>2</sup> with the complex plane.

Theorem 7.25 (Skew-product representation). _Suppose {B_ ( _t_ ) : _t ≥_ 0 _} is a planar Brownian motion with B_ (0) = 1 _. Then there exist two independent linear Brownian motions {Wi_ ( _t_ ) : _t ≥_ 0 _}, for i_ = 1 _,_ 2 _, such that_


_where_


Remark 7.26. By the result, both the logarithm of the radius, and the continuous determination of the angle of a planar Brownian motion are time-changed Brownian motions. The time-change itself depends only on the radius of the motion and ensures that the angle changes slowly away from the origin, but rapidly near the origin. _⋄_

**Proof.** Note first that _H_ ( _t_ ) itself is well-defined by Corollary 2.23. Moreover, the claimed equality for _H_ ( _t_ ) follows easily from the fact that both sides have the same value at _t_ = 0 and the same derivative. Let _{W_ ( _t_ ) : _t ≥_ 0 _}_ be planar Brownian motion and _W_ ( _t_ ) = _W_ 1( _t_ ) + **i** _W_ 2( _t_ ) its decomposition into real and imaginary part. By Theorem 7.19,


where _{B_ ( _t_ ) : _t ≥_ 0 _}_ is a planar Brownian motion and


By definition _H_ is the inverse function of _ζ_ . Hence, using (2.3) for _t_ = _H_ ( _s_ ), we get

_B_ ( _s_ ) = exp � _W_ ( _H_ ( _s_ ))� = exp � _W_ 1( _H_ ( _s_ )) + **i** _W_ 2( _H_ ( _s_ ))� _,_

which is the desired result.

199

Example 7.27. By the skew-product representation, for a planar Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ , we have log _|B_ ( _t_ ) _|_ = _W_ 1( _H_ ( _t_ )) and hence the process _{_ log _|B_ ( _t_ ) _|_ : _t ≥_ 0 _}_ is a time-changed Brownian motion in dimension one. However, recall from Example 7.18 that it is _not_ a martingale. _⋄_

For further applications, we need to study the asymptotics of the random clock _H_ ( _t_ ) more carefully. To state the next result let _{W_ 1( _t_ ) : _t ≥_ 0 _}_ be a linear Brownian motion as in Theorem 7.25 and, for _a >_ 0, let _{W_ 1<sup>_a_(</sup><sup>_t_):</sup><sup>_t≥_0</sup><sup>_}_betheBrownianmotiongivenby</sup><sup>_W a_</sup> 1<sup>(</sup><sup>_t_)=</sup> _a_<sup>_−_1</sup> _W_ 1( _a_<sup>2</sup> _t_ ). For each such Brownian motion we look at the first hitting time of level _b_ ,


Theorem 7.28. _For every ε >_ 0 _we have_


The proof uses the following simple fact, sometimes known as _Laplace’s method_ . Lemma 7.29. _For any continuous f_ : [0 _, t_ ] _→_ R _and t >_ 0 _,_


**Proof.** The upper bound is obvious, by replacing _f_ by its maximum. For the lower bound, let _s ∈_ [0 _, t_ ] be a point where the maximum is taken. We use continuity to find, for any _ε >_ 0, some 0 _< δ <_ 1 such that _f_ ( _r_ ) _≥ f_ ( _s_ ) _− ε_ for all _r ∈_ ( _s − δ, s_ + _δ_ ). Restricting the limit to this interval gives a lower bound of max0 _≤s≤t f_ ( _s_ ) _−ε_ , and the result follows as _ε >_ 0 was arbitrary.

**Proof of Theorem 7.28.** By scaling one may assume that _W_ 1(0) = 0. We abbreviate _a_ = _a_ ( _t_ ) = 2<sup><u>1</u>log</sup><sup>_t_.Aswehave,forany</sup><sup>_δ>_0,</sup>


200

recalling that _a_ =<sup><u>1</u></sup> 2<sup>log</sup><sup>_t_.Notenowthat</sup>


and the right hand side has the same distribution as

Laplace’s method gives that, almost surely,

Hence,


This proves (2.4). In the same way one can show that


and this completes the proof.

Remark 7.30. As _{W_ 1<sup>_a_(</sup><sup>_t_):</sup><sup>_t≥_0</sup><sup>_}_isaBrownianmotionforevery</sup><sup>_a>_0,thelawof</sup><sup>_T a_</sup> 1<sup>does</sup> not depend on _a >_ 0. Therefore, Theorem 7.28 implies that


where _T_ 1 = inf _{s ≥_ 0 : _W_ ( _s_ ) = 1�. The distribution of _T_ 1 is, by Theorem 2.32 given by the _⋄_ density (2 _πs_<sup>3</sup> )<sup>_−_1</sup><sup>_/_2</sup> exp( _−_ 1 _/_ (2 _s_ )).

We now determine the asymptotic law of the winding numbers _θ_ ( _t_ ) = _W_ 2( _H_ ( _t_ )), as _t →∞_ . Theorem 7.31 (Spitzer’s law). _For any x ∈_ R _,_


Hence, by Theorem 7.28, for _a_ = _a_ ( _t_ ) =<sup><u>1</u></sup> 2<sup>log</sup><sup>_t_,</sup>


201

The law of the random variable _W_ 2<sup>_a_(</sup><sup>_T a_</sup> 1<sup>) does not depend on the choice of</sup><sup>_a_.By Theorem 2.33,</sup> see also Exercise 7.4, it is Cauchy distributed.

### **3. Tanaka’s formula and Brownian local time**

In this section we establish a deep connection between Itˆo’s formula and Brownian local times for linear Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ . The basic idea is to give an analogue of Itˆo’s formula for the function _f_ : R _→_ R, _f_ ( _t_ ) = _| t − a|_ . Note that this function is not twice continuously differentiable, so Itˆo’s formula cannot be applied directly.

To see what we are aiming at, let’s apply Itˆo’s formula informally. We have in the distributional sense that _f_<sup>_′_</sup> ( _x_ ) = sign( _x − a_ ) and _f_<sup>_′′_</sup> ( _x_ ) = 2 _δa_ . Hence Itˆo’s formula would give


The last integral can be interpreted as the time spent by Brownian motion at level _a_ and hence it is natural to expect that it is the local time _L_<sup>_a_</sup> ( _t_ ). Tanaka’s formula confirms this intuition.

Theorem 7.32 (Tanaka’s formula). _Let {B_ ( _t_ ) : _t ≥_ 0 _} be linear Brownian motion. Then, for every a ∈_ R _, almost surely, for all t >_ 0 _,_


_where_ sign _x_ = 1 _{x>_ 0 _} −_ 1 _{x≤_ 0 _}._

Remark 7.33. To explore the relation of Tanaka’s and Itˆo’s formula further, suppose that _f_ : R _→_ R is twice differentiable such that _f_<sup>_′_</sup> has compact support, but do not assume that _f_<sup>_′′_</sup> is continuous. Then, for a suitable constant _c_ ,


and, for a suitable constant _b_ ,


Integrating Tanaka’s formula with respect to<sup><u>1</u></sup> 2<sup>_f ′′_(</sup><sup>_a_)</sup><sup>_da_andexchangingthisintegralwiththe</sup> stochastic integral, which is justified by Exercise 7.7 below, gives


By Theorem 6.17 the last term equals<sup><u>1</u></sup> 2 �0 _t_<sup>_f ′′_�</sup> _B_ ( _s_ )� _ds_ . Hence, we learn that Itˆo’s formula does not require the continuity requirement for the second derivative. _⋄_

202

For the proof of the Tanaka formula we define


and show that this defines a density of the occupation measure.

Lemma 7.34. _For every t ≥_ 0 _and a ∈_ R _, almost surely,_


**Proof.** Using the strong Markov property the statement can be reduced to the case _a_ = 0. The main idea of the proof is now to use convolution to make _| x|_ smooth, and then use Itˆo’s formula for the smooth function.

For this purpose, recall that, for any _δ >_ 0 we can find smooth functions _g, h_ : R _→_ [0 _,_ 1] with compact support such that _g ≤_ 1 (0 _,_ 1) _≤ h_ and � _g_ = 1 _− δ_ , � _h_ = 1 + _δ_ . This reduces the problem to showing that


for _g_ : R _→_ [0 _,_ 1] smooth, with compact support in [0 _, ∞_ ) and � _g_ = 1. Let


Now we let _ε ↓_ 0 for each term. The sequence of probability measures _ε_<sup>_−_1</sup> _g_ ( _ε_<sup>_−_1</sup> _z_ ) _dz_ converges weakly to _δ_ 0, which implies that _fε_ ( _x_ ) _→| x|_ for all _x_ . From the definition of _fε_ we infer that all functions _fε_ are Lipschitz with Lipschitz constant one. Hence, given _δ >_ 0 and a compact interval _I_ = [ _a, b_ ], we can find finitely many points _a_ = _x_ 1 _< . . . < xn_ = _b_ with _xk_ +1 _− xk < δ/_ 3. There exists _ε_ 0 _>_ 0 such that _|fε_ ( _xk_ ) _−| xk|| < δ/_ 3 for all 0 _< ε < ε_ 0. Then, for all _x ∈ I_ there is _xk ≤ x ≤ xk_ +1 and


In other words, _fε_ ( _x_ ) _→| x|_ uniformly on compact intervals. Given _δ >_ 0 one can find _M_ such that _|B_ ( _s_ ) _| ≤ M_ on [0 _, t_ ] with probability exceeding 1 _− δ_ . On this event we have


This ensures convergence in probability of the first two terms on the left hand side of (3.1). To deal with the third term, we differentiate _fε_ and get


Now we use the isometry property (1.2) to infer that

203

The right hand side converges to zero, by the bounded convergence theorem. Hence we have shown that, in probability,


**Proof of Theorem 7.32.** Convergence in probability implies that a subsequence converges almost surely and hence, for every _t_ , we obtain from Lemma 7.34 that, almost surely, the process _{L_<sup>˜</sup><sup>_a_</sup> ( _t_ ): _a ∈_ R _}_ is a density of the occupation measure. From Theorem 6.17 we therefore get that _L_<sup>˜</sup><sup>_a_</sup> ( _t_ ) = _L_<sup>_a_</sup> ( _t_ ) for almost every _a ∈_ R. Averaging over _t_ gives that, almost surely,


As the random field _{L_<sup>_a_</sup> ( _t_ ): _t ≥_ 0 _, a ∈_ R _}_ is continuous by Theorem 6.18, it therefore is a continuous modification of _{L_<sup>˜</sup><sup>_a_</sup> ( _t_ ): _t ≥_ 0 _, a ∈_ R _}_ . In particular, for every _a_ , almost surely, the process _{L_<sup>_a_</sup> ( _t_ ): _t ≥_ 0 _}_ agrees with _{L_<sup>˜</sup><sup>_a_</sup> ( _t_ ): _t ≥_ 0 _}_ .

Corollary 7.35. _For every a ∈_ R _, almost surely, for all t ≥_ 0 _,_

_and_


**Proof.** The right sides in these formulas add up to _L_<sup>_a_</sup> ( _t_ ), while their difference is zero.

We now use Tanka’s formula to prove L´evy’s theorem describing the joint law of the modulus and local time of a Brownian motion.

Theorem 7.36 (L´evy). _The processes_


_have the same distribution._

Remark 7.37. This result extends both Theorem 2.31 where it was shown that the processes _{|B_ ( _t_ ) _|_ : _t ≥_ 0 _}_ and _{M_ ( _t_ ) _− B_ ( _t_ ) : _t ≥_ 0 _}_ have the same distribution, and Theorem 6.10 where it was shown that _{L_<sup>0</sup> ( _t_ ) : _t ≥_ 0 _}_ and _{M_ ( _t_ ) : _t ≥_ 0 _}_ have the same distribution. Exercise 6.2 suggests an alternative proof using random walk methods. _⋄_

204

As a preparation for the proof we find the law of the process given by integrating the sign of a Brownian motion with respect to that Brownian motion.

Lemma 7.38. _For every a ∈_ R _, the process {W_ ( _t_ ) : _t ≥_ 0 _} given by_


_is a standard Brownian motion._

**Proof.** Assume, without loss of generality, that _a <_ 0. Suppose that _T_ = inf _{t >_ 0 : _B_ ( _t_ ) = _a}_ . Then _W_ ( _t_ ) = _B_ ( _t_ ) for all _t ≤ T_ and hence _{W_ ( _t_ ) : 0 _≤ t ≤ T }_ is a (stopped) Brownian motion. By the strong Markov property the process _{B_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _}_ given by _B_<sup>�</sup> ( _t_ ) = _B_ ( _t_ + _T_ ) _−a_ is a Brownian motion started in the origin, which is independent of _{W_ ( _t_ ) : 0 _≤ t ≤ T }_ . As

_W_ ( _t_ + _T_ ) = _W_ ( _T_ ) + sign( _B_ ( _s_ ) _− a_ ) _dB_ ( _s_ ) = _B_ ( _T_ ) + sign( _B_<sup>�</sup> ( _s_ )) _dB_<sup>�</sup> ( _s_ ) _,_ � _Tt_ + _T_ �0 _t_

it suffices to show that the second term is a Brownian motion to complete the proof. Hence we may henceforth assume that _a_ = 0.

Now fix 0 _≤ s < t_ and recall that _W_ ( _t_ ) _− W_ ( _s_ ) is independent of _F_ ( _s_ ). For the proof it hence suffices to show that _W_ ( _t_ ) _−W_ ( _s_ ) has a centred normal distribution with variance _t−s_ . Choose _s_ = _t_ (1 _n_ ) _< . . . < tn_ ( _n_ ) = _t_ with mesh ∆( _n_ ) _↓_ 0, and approximate the progressively measurable process _H_ ( _u_ ) = sign( _B_ ( _u_ )) by the step processes


It follows from the fact that the zero set of Brownian motion is a closed set of measure zero, that lim E � _st_<sup>(</sup><sup>_Hn_(</sup><sup>_u_)</sup><sup>_−H_(</sup><sup>_u_))2</sup><sup>_du_= 0,andhence</sup>


From the independence of the Brownian increments and elementary properties of the normal distribution, one can see that the random variables on the right all have a centred normal distribution with variance _t − s_ . Hence this also applies to the limit _W_ ( _t_ ) _− W_ ( _s_ ).

**Proof of Theorem 7.36.** By Tanaka’s formula we have


Define a standard Brownian motion _{W_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _}_ by


and let _{M_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _}_ be the associated maximum process. We show that � _M_ ( _t_ ) = _L_<sup>0</sup> ( _t_ ) for all _t ≥_ 0 _,_

205

which implies that _{_ ( _|B_ ( _t_ ) _|, L_<sup>0</sup> ( _t_ )) : _t ≥_ 0 _}_ and _{_ ( _M_<sup>�</sup> ( _t_ ) _−W_<sup>�</sup> ( _t_ ) _, M_<sup>�</sup> ( _t_ )) : _t ≥_ 0 _}_ agree pointwise, and the result follows as the latter process agrees in distribution with

_{_ ( _M_ ( _t_ ) _− B_ ( _t_ ) _, M_ ( _t_ )) : _t ≥_ 0 _}._

To show that _M_<sup>�</sup> ( _t_ ) = _L_<sup>0</sup> ( _t_ ) we first note that

_W_ �( _s_ ) = _L_<sup>0</sup> ( _s_ ) _−|B_ ( _s_ ) _| ≤ L_<sup>0</sup> ( _s_ ) _,_

and hence, taking the maximum over all _s ≤ t_ , we get _M_<sup>�</sup> ( _t_ ) _≤ L_<sup>0</sup> ( _t_ ). On the other hand, the process _{L_<sup>0</sup> ( _t_ ) : _t ≥_ 0 _}_ increases only on the set _{t_ : _B_ ( _t_ ) = 0 _}_ and on this set we have _L_<sup>0</sup> ( _t_ ) = _W_<sup>�</sup> ( _t_ ) _≤ M_<sup>�</sup> ( _t_ ). Hence the proof is complete, since _{M_<sup>�</sup> ( _t_ ) : _t ≥_ 0 _}_ is increasing.

### **4. Feynman-Kac formulas and applications**

In this section we answer some natural questions about Brownian motion that involve time. For example, we find the probability that linear Brownian motion exits a given interval by a fixed time. Our main tool is the close relationship between the expectation of certain functionals of the Brownian path and the heat equation with dissipation term. This goes under the name of _Feynman-Kac formula_ , and the theorems that make up this theory establish a strong link between parabolic partial differential equations and Brownian motion.

Definition 7.39. _Let U ⊂_ R<sup>_d_</sup> _be either open and bounded, or U_ = R<sup>_d_</sup> _. A twice differentiable function u_ : (0 _, ∞_ ) _× U →_ [0 _, ∞_ ) _is said to solve the_ **heat equation with heat dissipation rate** _V_ : _U →_ R _and initial condition f_ : _U →_ [0 _, ∞_ ) _on U if we have_


_where the Laplacian_ ∆ _x acts on the space variables x._


Remark 7.40. The solution _u_ ( _t, x_ ) describes the temperature at time _t_ at _x_ for a heat flow with _cooling_ with rate _−V_ ( _x_ ) on the set _{x ∈ U_ : _V_ ( _x_ ) _<_ 0 _}_ , and _heating_ with rate _V_ ( _x_ ) on the set _{x ∈ U_ : _V_ ( _x_ ) _>_ 0 _}_ , where the initial temperature distribution is given by _f_ ( _x_ ) and the boundary of _U_ is kept at zero temperature. _⋄_

Instead of going for the most general results linking the heat equation to Brownian motion, we give some of the more basic forms of the Feynman-Kac formula together with applications. Our first theorem in this spirit, an existence result for the heat equation in the case _U_ = R<sup>_d_</sup> , will lead to a new, more analytic proof of the second arcsine law, Theorem 5.28.

206

Theorem 7.41. _Suppose V_ : R<sup>_d_</sup> _→_ R _is bounded. Then u_ : [0 _, ∞_ ) _×_ R<sup>_d_</sup> _→_ R _defined by_


_solves the heat equation on_ R<sup>_d_</sup> _with dissipation rate V and initial condition one._

**Proof.** The easiest proof is by a direct calculation. Expand the exponential in a power series, then the terms in the expansion are _a_ 0( _x_ ) := 1 and, for _n ≥_ 1,


with the conventions _x_ 0 = _x_ , _t_ 0 = 0 and _tn_ +1 = _t_ . Differentiating with respect to _t_ and using _∂t_ p( _t, x_ 1 _, x_ 2) = 2<sup><u>1</u>∆</sup><sup>_x_p(</sup><sup>_t, x_1</sup><sup>_, x_2),weget</sup>


Analogously, _∂t∂_<sup>_an_(</sup><sup>_x_)=</sup> <u>12</u><sup>∆</sup><sup>_x an_(</sup><sup>_x_)+</sup><sup>_V_(</sup><sup>_x_)</sup><sup>_an−_1(</sup><sup>_x_).</sup> Adding up all these terms, and noting that differentiation under the summation sign is allowed, verifies the validity of the differential equation. The requirement on the initial condition follows easily from the boundedness of _V_ .

As an application we give a proof of the second arcsine law, Theorem 5.28, which does not rely on the first arcsine law. We use Theorem 7.41 with _V_ ( _x_ ) = _λ_ 1 [0 _,∞_ )( _x_ ). Then


solves

_∂tu_ ( _t, x_ ) =<sup><u>1</u></sup> 2<sup>_∂xxu_(</sup><sup>_t, x_)</sup><sup>_−λ_1[0</sup><sup>_,∞_)(</sup><sup>_x_)</sup><sup>_u_(</sup><sup>_t, x_)</sup><sup>_,_</sup> _u_ (0 _, x_ ) = 1 for all _x ∈_ R.

To turn this partial differential equation into an ordinary differential equations, we take the Laplace transform


207

which satisfies the equation


This can be rewritten as


Solving these two linear ordinary differential equations gives


As _g_ must remain bounded as _ρ ↑∞_ , we must have _A_ = _D_ = 0. Moreover, _g_ must be continuously differentiable in zero, hence _C_ and _B_ can be calculated from matching conditions. After an elementary calculation we obtain


On the other hand, with


we have, using Brownian scaling in the second step,


Now we let _ρ_ = 1 and from

and the expansions

and

we get for the moments of _X_ (1), by a comparison of coefficients,


which implies that _X_ (1) is arcsine distributed.

Our second version of the Feynman-Kac formula is a uniqueness result for the case of zero dissipation rate, which will allow us the express the probability that linear Brownian motion exits an interval before a fixed time _t_ in two different ways.

208

Theorem 7.42. _If u is a bounded, twice continuously differentiable solution of the heat equation on the domain U , with zero dissipation rate and continuous initial condition f , then_


_where τ is the first exit time from the domain U ._

**Proof.** The proof is based on Itˆo’s formula, Theorem 7.14, and Remark 7.15. We let _K ⊂ U_ be compact and denote by _σ_ the first exit time from _K_ . Fixing _t >_ 0 and applying Itˆo’s formula with _f_ ( _x, y_ ) = _u_ ( _t − y, x_ ) and _ζ_ ( _s_ ) = _s_ gives, for all _s < t_ ,


As _u_ solves the heat equation, the last two terms on the right cancel. Hence, taking expectations,

E _x_ � _u_ ( _t − s ∧ σ, B_ ( _s ∧ σ_ ))� = E _x_ � _u_ ( _t, B_ (0))� = _u_ ( _t, x_ ) _,_

using that the stochastic integral has vanishing expectation. Exhausting _U_ by compact sets, i.e. letting _σ ↑ τ_ , leads to E _x_ [ _u_ ( _t − s, B_ ( _s_ )) 1 _{s < τ }_ ] = _u_ ( _t, x_ ). Taking a limit _s ↑ t_ gives the required result.

As an application of Theorem 7.42 we calculate the probability that a linear Brownian motion stays, up to time _t_ , within an interval. As a warm-up we suggest to look at Exercise 7.8 where the easy case of a half-open interval is treated. Here we focus on intervals [ _a, b_ ], for _a <_ 0 _< b_ , and give two different formulas for the probability of staying in [ _a, b_ ] up to time _t_ . To motivate the first formula, we start with a heuristic approach, which gives the correct result, and then base the rigorous proof on the Feynman-Kac formula.

For our heuristics we think of the transition (sub–)density, _qt_ : [0 _, a_ ] _×_ [0 _, a_ ] _→_ [0 _,_ 1] of a Brownian motion, which is killed upon leaving the interval [0 _, a_ ]. In a first approximation we subtract from the transition density p( _t, x, y_ ) of an unkilled Brownian motion the transition density for all the paths that reach level 0. By the reflection principle (applied to the first hitting time of level 0) the latter is equal to p( _t, x, −y_ ).

We then subtract the transition density of all the paths that reach level _a_ , which, again by the reflection principle, equals p( _t, x,_ 2 _a − y_ ), then add again the density of all the paths that reach level 0 after hitting _a_ , as these have already been subtracted in the first step. This gives the approximation term p( _t, x, y_ ) _−_ p( _t, x, −y_ ) _−_ p( _t, x,_ 2 _a − y_ ) + p( _t, x,_ 2 _a_ + _y_ ).

Of course the iteration does not stop here (for example we have double-counted paths that reach level 0 after hitting _a_ ). Eventually we have to consider an infinite series of alternating reflections at levels 0 and _a_ to obtain the density


209

Integrating this over _y ∈_ [0 _, a_ ] makes the following theorem plausible.

Theorem 7.43. _Let_ 0 _< x < a. Then_


_where_ Φ( _x_ ) _is the distribution function of a standard normal distribution._

**Proof.** The left hand side in (4.2) agrees with the right hand side in Theorem 7.42 for _U_ = (0 _, a_ ) and _f_ = 1. The series on the right hand side is absolutely convergent, and hence satisfies the boundary conditions at _x_ = 0 and _x_ = _a_ . It is also not difficult to verify that it is bounded. Elementary calculus gives


and similarly for the other summands. Hence termwise differentiation shows that the right hand side satisfies the heat equation. To see that the initial condition is fulfilled, note that (as _t ↓_ 0) the sums over all _k >_ 0 converge to zero by cancellation, and the sum over all _k <_ 0 obviously converge to zero. Among the four terms belonging to _k_ = 0, two terms with positive sign and one term with negative sign converge to one, whereas one term converges to zero.

The solution of the heat equation is not in the form one would get by a na¨ıve separation of variables approach. This approach yields a different, equally valuable, expression for the probability of interest. Indeed, writing _u_ ( _t, x_ ) = _v_ ( _t_ ) _w_ ( _x_ ) one expects _w_ to be an eigenfunction of 2<sup><u>1</u></sup><sup>_∂xx_on(0</sup><sup>_, a_)withzeroboundaryconditions.Theseeigenfunctionsare</sup>


with eigenvalues _−k_<sup>2</sup> _π_<sup>2</sup> _/_ (2 _a_<sup>2</sup> ). As we are only interested in solutions symmetric about _a/_ 2 only the cosine terms will contribute For _v_ we are looking for the eigenfunctions of _∂t_ with the same eigenvalues, which are


and considering the initial condition (and shifting the cosine by _π/_ 2) leads to the solution


Therefore (4.3) is an alternative representation of the probability in (4.2). For practical purposes this series is more useful when _t_ is large, as the convergence is faster, whereas the series in the theorem converges fast only for small values of _t >_ 0.

210

We now prove an elliptic, or time-stationary, version of the Feynman-Kac formula. This will enable us to describe the distribution of the total time spent by a transient Brownian motion in unit ball in terms of a Laplace transfrom.

Theorem 7.44. _Let d ≥_ 3 _and V_ : R<sup>_d_</sup> _→_ [0 _, ∞_ ) _be bounded. Define_


_Then h_ : R<sup>_d_</sup> _→_ [0 _, ∞_ ) _satisfies the equation_


Remark 7.45. Informally, the integral equation in Theorem 7.44 implies<sup><u>1</u></sup> 2<sup>∆</sup><sup>_h_=</sup><sup>_V h_,whichis</sup> also what one gets from letting _t ↑∞_ in Theorem 7.41. See also Exercise 2.18 for a converse result in a similar spirit. _⋄_

**Proof.** Define the ‘resolvent operator’


Using the fundamental theorem of calculus in the second step we obtain


Using Fubini’s theorem and the Markov property, we may continue with


The function _h_ is related to the resolvent operator by the equation


for the Green’s function _G_ ( _x, y_ ) = (2 _π_ )<sup>_−_1</sup> _|x − y|_<sup>_−_2</sup> , as claimed.

We use Theorem 7.44 to prove the three-dimensional case of the Ciesielski-Taylor identity, one of the most surprising identities about Brownian motion. Key to this is the following proposition.

211

Proposition 7.46. _For a standard Brownian motion {B_ ( _t_ ): _t ≥_ 0 _} in dimension three let T_ = �0 _∞_<sup>1</sup><sup>_{B_(</sup><sup>_t_)</sup><sup>_∈B_(0</sup><sup>_,_1)</sup><sup>_}bethetotaloccupationtimeoftheunitball.Then_</sup>


Clearly, we are looking for a rotationally symmetric function _h_ . The integral on the right can therefore be split into two parts: First, the integral over _B_ (0 _, |x|_ ), which is the Newtonian potential due to a symmetric mass distribution on _B_ (0 _, |x|_ ) and therefore remains unchanged if the same mass is concentrated at the origin. Second, the integral over _B_ (0 _,_ 1) _\ B_ (0 _, |x|_ ), which is harmonic on the open ball _B_ (0 _, |x|_ ) with constant value on the boundary, so itself is constant. Hence, for _x ∈B_ (0 _,_ 1), to


With _u_ ( _r_ ) = _rh_ ( _x_ ) for _|x|_ = _r_ we have, for 0 _< r <_ 1,


and by differentiation _u_<sup>_′′_</sup> = 2 _λu_ on (0 _,_ 1). Hence

The boundary conditions _u_ (0) = 0 and _u_<sup>_′_</sup> (1) = 1 give _B_ = _−A_ and


Then


as required to complete the proof.

Theorem 7.47 (Ciesielski-Taylor identity). _The first exit time from the unit ball by a standard Brownian motion in dimension one and the total occupation time of the unit ball by a standard Brownianian motion in dimension d_ = 3 _have the same distribution._

**Proof.** The Laplace transform of the first exit time from the unit interval ( _−_ 1 _,_ 1) is given in Exercise 2.16. It coincides with the Laplace transform of _T_ given in Proposition 7.46. Hence the two distributions coincide.

212

### **Exercises**

Exercise 7.1 ( _∗_ ). Suppose _{H_ ( _s, ω_ ): _s ≥_ 0 _, ω ∈_ Ω _}_ is progressively measurable and _{B_ ( _t_ ): _t ≥_ 0 _}_ a linear Brownian motion. Show that for any stopping time _T_ with


we have


Exercise 7.2. Suppose that _f_ : [0 _,_ 1] _→_ R is in the Cameron-Martin space, i.e. _f_ ( _t_ ) = �0 _t_<sup>_f ′_(</sup><sup>_s_)</sup><sup>_ds_</sup> for all _t ∈_ [0 _,_ 1] and _f_<sup>_′_</sup> _∈ L_<sup>2</sup> (0 _,_ 1). Then, almost surely,


Exercise 7.3 ( _∗_ ). Give the details of the proof of the multidimensional Itˆo formula, Theorem 7.14.

Exercise 7.4 ( _∗_ ). Give an alternative proof of Theorem 2.33 based on a conformal mapping of the halfplanes _{_ ( _x, y_ ): _x > t}_ onto the unit disk, which exploits our knowledge of harmonic measure on spheres.

Exercise 7.5 ( _∗_ ). Let _{B_ ( _t_ ): _t ≥_ 0 _}_ be a planar Brownian motion. Show that, if _θ_ ( _t_ ) is the continuous determination of the angle of _B_ ( _t_ ), we have, almost surely,


Exercise 7.6. Formalise and prove the statement that, for every _ε >_ 0, a planar Brownian motion winds around its starting point infinitely often in any time interval [0 _, ε_ ].

213

Exercise 7.7 ( _∗_ ). Show that under suitable conditions, stochastic integrals and ordinary integrals can be interchanged: Suppose _h_ : R _→_ [0 _, ∞_ ) is a continuous function with compact support. Then, almost surely,


**Hint.** Write the outer integral on the left hand side as a limit of Riemann sums. For this purpose it is useful to know that, by Tanaka’s formula and continuity of the local times, the integrand has a continuous modification.

Exercise 7.8.

- (a) Show that the function _u_ : (0 _, ∞_ ) _×_ (0 _, ∞_ ) _→_ R given by


solves the heat equation on the domain (0 _, ∞_ ) with zero dissipation rate and constant initial condition _f_ = 1.

- (b) Infer from this that, for _x >_ 0,


- (c) Explain how the result of (b) could have been obtained from the reflection principle.

Exercise 7.9. Prove the Erd˝os-Kac theorem: Let _X_ 1 _, X_ 2 _, . . ._ be a sequence of independent identically distributed random variables with mean zero and variance one. Let _Sn_ = _X_ 1 + _· · ·_ + _Xn_ and _Tn_ = max _{|S_ 1 _|, . . . , |Sn|}_ . Then


214

### **Notes and Comments**

The first stochastic integral with a random integrand was defined by Itˆo [ **It44** ] but stochastic integrals with respect to Brownian motion with deterministic integrands were known to Paley, Wiener and Zygmund already in 1933, see [ **PWZ33** ]. Our stochastic integral is by far not the most general construction possible, the complete theory of Itˆo integration is one of the cornerstones of modern probability. Interesting further material can be found, for example, in the books [ **CW90** ], [ **RW00** ] or [ **Du96** ].

Itˆo’s formula, first proved in [ **It51** ], plays a central role in stochastic analysis, quite like the fundamental theorem of calculus does in real analysis. The version we give is designed to minimise the technical effort to get to the desired applications, but a lot more can be said if the discussion is extended to the concept of semimartingales, the references in the previous paragraph provide the background for this.

Conformal invariance was known to L´evy and a sketch of a proof is given in the book [ **Le48** ]. It is interesting to note that this fact does not extend to higher dimensions _d ≥_ 3. There are not many nontrivial conformally invariant maps anyway, but essentially the only one, inversion on a sphere, fails. This is easy to see, as the image of Brownian motion stopped on the boundary of the punctured domain _B_ (0 _,_ 1) _\ {_ 0 _}_ has zero probability of not hitting _B_ (0 _,_ 1).

There is rich interaction between complex analysis and Brownian motion, which relies on conformal invariance. The conformal invariance of harmonic measure, which we proved in Theorem 7.22, is not easy to obtain by purely analytical means. Another result from complex analysis, which can be proved effectively using Brownian motion is Picard’s theorem, see Davis [ **Da75** ]. The theorem states that a nonconstant entire function has a range which omits at most one point from the complex plane. Only very recently a completely new perspective on conformal invariance has opened up through the theory of conformally invariant random curves developed by Lawler, Schramm, and Werner, see e.g. [ **We04** ]. The skew-product representation has many nice applications, for more examples see [ **LG91** ], which also served as the backbone of our exposition. The first result about the windings of Brownian motion is Spitzer’s law, first proved by F. Spitzer in [ **Sp58** ]. There are plenty of extensions including pathwise laws [ **Sh98, M¨o02** ], windings around more than one point, and joint laws of windings and other functionals [ **PY86** ]. A discussion of some problems related to this can be found in [ **Yo92** ].

Tanaka’s formula offers many fruitful openings, among them the theory of local times for semimartingales, which is presented in [ **RY94** ]. The formula goes back to the paper by Tanaka [ **Ta63** ]. Alternative to our approach, Tanaka’s formula can be taken as a definition of Brownian local time. Then continuity can be obtained from the Kolmogorov-Centsov<sup>ˇ</sup> theorem and moment estimates based on the Burkholder-Davis-Gundy inequalities, see for example the book by Karatzas and Shreve [ **KS88** ].

215

The Feynman-Kac formula is a classical application in stochastic calculus, which is discussed in more detail in [ **KS88** ]. It can be exploited to obtain an enormous variety of distributional properties of Brownian motion, see [ **BS02** ] for (literally!) thousands of examples. The converse, application of Brownian motion to study equations, is of course equally natural. Del Moral [ **DM04** ] gives an impressive account of the wide applicability of this formula and its variants.

The identity between the two formulas describing the probability that a Brownian motion stays between two barriers serves as a standard example for the Poisson summation formula, see [ **Fe66** , X.5 and XIX.5]. According to Feller it was discovered originally in connection with Jacobi’s theory of transformations of theta functions, see Landau [ **La09** , Satz 277].

The ‘iterated reflection’ argument, which we have used to determine the transition density of a Brownian motion with absorbing barriers may also be used to determine transition densities for a Brownian motion which is reflected at the barriers, see [ **Fe66** , X.5]. In higher dimensions Brownian motion reflected at the boundaries of a domain is an interesting subject, not least because of its connections to partial differential equations with Neumann boundary conditions, see, for example, [ **Br76** ].

The Erd˝os-Kac law plays an important rˆole for the Kolmogorov-Smirnov test known from nonparametric statistics, see e.g. [ **Fe68** ]. Plenty of proofs of the arcsine law are known: Besides the two provided in this book, there is also an approach of Kac [ **Ka51** ] based on the Meyer-Tanaka formula, and Rogers and Williams [ **RW00** , III.24] provide a proof based on local time theory.

The Ciesielski-Taylor identity was found by Ciesielski and Taylor in 1962 by an explicit calculation, see [ **CT62** ]. It extends to arbitrary dimensions _d_ , stating that the law of the exit times from the unit ball by a standard Brownian motion in dimension _d_ equals the law of the total occupation time in the unit ball by the standard Brownian motion in dimension _d_ + 2. Our argument is taken from [ **Sp64** ], see also [ **RW00** , III.20]. Many proofs of this fact are known, see for example [ **Yo92** ], but none provides a geometrically intuitive explanation and it may well be that none exists.

216

### CHAPTER 8

---

[← Brownian local time](10-brownian-local-time.md) · [Up: contents](index.md) · [Potential theory of Brownian motion →](12-potential-theory-of-brownian-motion.md)
