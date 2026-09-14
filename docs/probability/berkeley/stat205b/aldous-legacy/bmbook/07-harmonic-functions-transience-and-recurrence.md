---
title: Harmonic functions, transience and recurrence
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Harmonic functions, transience and recurrence

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this chapter we explore the relation of harmonic functions and Brownian motion. This approach will be particularly useful for _d_ -dimensional Brownian motion for _d >_ 1. It allows us to study the fundamental questions of transience and recurrence of Brownian motion, investigate the classical Dirichlet problem of electrostatics, and provide the background for the deeper investigations of probabilistic potential theory, which will follow in Chapter 8.

### **1. Harmonic functions and the Dirichlet problem**

Let _U_ be a **domain** , i.e. a connected open set _U ⊂_ R<sup>_d_</sup> , and _∂U_ be its boundary. Suppose that its closure _U_ is a homogeneous body and its boundary is electrically charged, the charge given by some continuous function _ϕ_ : _∂U →_ R. The _Dirichlet problem_ asks for the voltage _u_ ( _x_ ) at some point _x ∈ U_ . Kirchhoff’s laws state that _u_ must be a _harmonic function_ in _U_ . We therefore start by discussing the basic features of harmonic functions.

Definition 3.1. _Let U ⊂_ R<sup>_d_</sup> _be a domain. A function u_ : _U →_ R _is_ harmonic _(on U ) if it is twice continuously differentiable and, for any x ∈ U ,_


_If instead of the last condition only_ ∆ _u_ ( _x_ ) _≥_ 0 _, then the function u is called_ **subharmonic** _. ⋄_

To begin with we give two useful reformulations of the harmonicity condition, called the **mean value properties** , which do not make explicit reference to differentiability.

Theorem 3.2. _Let U ⊂_ R<sup>_d_</sup> _be a domain and u_ : _U →_ R _measurable and locally bounded. The following conditions are equivalent:_


(ii) _for any ball B_ ( _x, r_ ) _⊂ U ,_


(iii) _for any ball B_ ( _x, r_ ) _⊂ U ,_


_where σx,r is the surface measure on ∂B_ ( _x, r_ ) _._

69

Remark 3.3. We use the following version of Green’s identity,


where _n_ ( _y_ ) is the outward normal vector of the ball at _y_ . The result can also be proved by purely probabilistic means, see Exercise 8.1. _⋄_


**Proof. (ii)** _⇒_ **(iii)** Assume _u_ has the mean value property (ii). Define _ψ_ : (0 _, ∞_ ) _→_ R by


We show that _ψ_ is constant. Indeed, for any _r >_ 0,


Differentiating with respect to _r_ gives _dL_ ( _B_ ( _x,_ 1)) _u_ ( _x_ ) = _ψ_ ( _r_ ), and therefore _ψ_ ( _r_ ) is constant. Now (iii) follows from the well known identity _dL_ ( _B_ ( _x, r_ )) _/r_ = _σx,r_ ( _∂B_ ( _x, r_ )).

**(iii)** _⇒_ **(ii)** Fix _s >_ 0, multiply (ii) by _σx,r_ ( _∂B_ ( _x, r_ )) and integrate over all radii 0 _< r < s_ . **(iii)** _⇒_ **(i)** Suppose _g_ : [0 _, ∞_ ) _→_ [0 _, ∞_ ) is a smooth function with compact support in [0 _, ε_ ) and � _g_ ( _| x|_ ) _dx_ = 1. Integrating (iii) one obtains


for all _x ∈ U_ and sufficiently small _ε >_ 0. As convolution of a smooth function with a bounded function produces a smooth function, we observe that _u_ is infinitely often differentiable in _U_ . Now suppose that ∆ _u̸_ = 0, so that there exists a small ball _B_ ( _x, ε_ ) _⊂ U_ such that either ∆ _u_ ( _x_ ) _>_ 0 on _B_ ( _x, ε_ ), or ∆ _u_ ( _x_ ) _<_ 0 on _B_ ( _x, ε_ ). Using the notation from above, we obtain that


using (1.1). This is a contradiction.

**(i)** _⇒_ **(iii)** Suppose that _u_ is harmonic and _B_ ( _x, r_ ) _⊂ U_ . With the notation from above and (1.1), we obtain that


Hence _ψ_ is constant, and as lim _r↓_ 0 _ψ_ ( _r_ ) = _σ_ 0 _,_ 1( _B_ (0 _,_ 1)) _u_ ( _x_ ), we obtain (iii).

70

Remark 3.4. A twice differentiable function _u_ : _U →_ R is subharmonic if and only if


This can be obtained in a way very similar to Theorem 3.2, see also Exercise 3.1.


An important property satisfied by harmonic, and in fact subharmonic, functions is the maximum principle. This is one of the key principles of analysis.

Theorem 3.5 (Maximum principle). _Suppose u_ : R<sup>_d_</sup> _→_ R _is a function, which is subharmonic on an open connected set U ⊂_ R<sup>_d_</sup> _._

- (i) _If u attains its maximum in U , then u is a constant._

- (ii) _If u is continuous on U_<sup>¯</sup> _and U is bounded, then_


Remark 3.6. If _u_ is harmonic, the theorem may be applied to both _u_ and _−u_ . Hence the conclusions of the theorem also hold with ‘maximum’ replaced by ‘minimum’. _⋄_

**Proof.** (i) Let _M_ be the maximum. Note that _V_ = _{x ∈ U_ : _u_ ( _x_ ) = _M }_ is relatively closed in _U_ . Since _U_ is open, for any _x ∈ V_ , there is a ball _B_ ( _x, r_ ) _⊂ U_ . By the mean-value property of _u_ , see Remark 3.4,


Equality holds everywhere, and as _u_ ( _y_ ) _≤ M_ for all _y ∈B_ ( _x, r_ ), we infer that _u_ ( _y_ ) = _M_ almost everywhere on _B_ ( _x, r_ ). By continuity this implies _B_ ( _x, r_ ) _⊂ V_ . Hence _V_ is also open, and by assumption nonempty. Since _U_ is connected we get that _V_ = _U_ . Therefore, _u_ is constant on _U_ .

(ii) Since _u_ is continuous and _U_<sup>¯</sup> is closed and bounded, _u_ attains a maximum on _U_<sup>¯</sup> . By (i) the maximum has to be attained on _∂U_ .

Corollary 3.7. _Suppose u_ 1 _, u_ 2 : R<sup>_d_</sup> _→_ R _are functions, which are harmonic on a bounded domain U ⊂_ R<sup>_d_</sup> _and continuous on U_<sup>¯</sup> _. If u_ 1 _and u_ 2 _agree on ∂U , then they are identical._

**Proof.** By Theorem 3.5(ii) applied to _u_ 1 _− u_ 2 we obtain that


Hence _u_ 1( _x_ ) _≤ u_ 2( _x_ ) for all _x ∈ U_<sup>¯</sup> . Applying the same argument to _u_ 2 _− u_ 1, one sees that sup _x∈U_ ¯ _{u_ 2( _x_ ) _− u_ 1( _x_ ) _}_ = 0 _._ Hence _u_ 1( _x_ ) = _u_ 2( _x_ ) for all _x ∈ U_<sup>¯</sup> .

We can now formulate the basic fact on which the relationship of Brownian motion and harmonic functions rests.

71

Theorem 3.8. _Suppose U is a domain, {B_ ( _t_ ) : _t ≥_ 0 _} a Brownian motion started inside U and τ_ = _τ_ ( _∂U_ ) = min _{t ≥_ 0 : _B_ ( _t_ ) _∈ ∂U } the first hitting time of its boundary. Let ϕ_ : _∂U →_ R _be measurable, and such that the function u_ : _U →_ R _with_


_is locally bounded. Then u is a harmonic function._

**Proof.** The proof uses only the strong Markov property of Brownian motion and the mean value characterisation of harmonic functions. For a ball _B_ ( _x, δ_ ) _⊂ U_ let _τ_ ˜ = inf _{t >_ 0: _B_ ( _t_ ) _̸ ∈ B_ ( _x, δ_ ) _}_ , then the strong Markov property implies that


where _ϖx,δ_ is the uniform distribution on the sphere _∂B_ ( _x, δ_ ). Therefore, _u_ has the mean value property and hence it is harmonic on _U_ by Theorem 3.2.

Definition 3.9. _Let U be a domain in_ R<sup>_d_</sup> _and let ∂U be its boundary. Suppose ϕ_ : _∂U →_ R _is a continuous function on its boundary. A continuous function v_ : _U →_ R _is a_ **solution to the Dirichlet problem** _with boundary value ϕ, if it is harmonic on U and v_ ( _x_ ) = _ϕ_ ( _x_ ) _for x ∈ ∂U . ⋄_

The Dirichlet problem was posed by Gauss in 1840. In fact Gauss thought he showed that there is always a solution, but his reasoning was wrong and Zaremba in 1911 and Lebesgue in 1924 gave counterexamples. However, if the domain is sufficiently nice there is a solution, as we will see below.

Definition 3.10. _Let U ⊂_ R<sup>_d_</sup> _be a domain. We say that U satisfies the_ **Poincar´e cone condition** _at x ∈ ∂U if there exists a cone V based at x with opening angle α >_ 0 _, and h >_ 0 _⋄ such that V ∩B_ ( _x, h_ ) _⊂ U_<sup>c</sup> _._

The following lemma, which is illustrated by Figure 1, will prepare us to solve the Dirichlet problem for ‘nice’ domains. Recall that we denote, for any open or closed set _A ⊂_ R<sup>_d_</sup> , by _τ_ ( _A_ ) the first hitting time of the set _A_ by Brownian motion, _τ_ ( _A_ ) = inf _{t ≥_ 0: _B_ ( _t_ ) _∈ A}._

Lemma 3.11. _Let_ 0 _< α <_ 2 _π and C_ 0( _α_ ) _⊂_ R<sup>_d_</sup> _is a cone based at the origin with opening angle α, and_


_Then a <_ 1 _and, for any positive integer k and h_<sup>_′_</sup> _>_ 0 _, we have_


_for all x, z ∈_ R<sup>_d_</sup> _with | x − z| <_ 2<sup>_−k_</sup> _h_<sup>_′_</sup> _, where Cz_ ( _α_ ) _is a cone based at z with opening angle α._

72


<!-- Start of picture text -->
B(t) x 2 22 �������������������������������������������������������������������������������������������������������������������������� −k−k+2−k+1 �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� �������������������������������������������������������������������������������������������������������������������������� C (a)0<br><!-- End of picture text -->

Figure 1. Brownian motion avoiding a cone

**Proof.** Obviously _a <_ 1. If _x ∈B_ (0 _,_ 2<sup>_−k_</sup> ) then by the strong Markov property P _x_ � _τ_ ( _∂B_ (0 _,_ 1)) _< τ_ ( _C_ 0( _α_ ))�


Therefore, for any positive integer _k_ and _h_<sup>_′_</sup> _>_ 0, we have by scaling P _x_ � _τ_ ( _∂B_ ( _z, h_<sup>_′_</sup> )) _< τ_ ( _Cz_ ( _α_ ))� _≤ a_<sup>_k_</sup> _,_ for all _x_ with _| x − z| <_ 2<sup>_−k_</sup> _h_<sup>_′_</sup> .

Theorem 3.12 (Dirichlet Problem). _Suppose U ⊂_ R<sup>_d_</sup> _is a bounded domain such that every boundary point satisfies the Poincar´e cone condition, and suppose_ _<u>ϕ</u> is a continuous function on ∂U . Let τ_ ( _∂U_ ) = inf _{t >_ 0: _B_ ( _t_ ) _∈ ∂U }. Then the function u_ : _U →_ R _given by_


<!-- Start of picture text -->
is the unique continuous function harmonic on U with u ( x ) =  ϕ ( x ) for all x ∈ ∂U .<br><!-- End of picture text -->

**Proof.** The uniqueness claim follows from Corollary 3.7. The function _u_ is bounded and hence harmonic on _U_ by Theorem 3.8. It remains to show that the Poincar´e cone condition implies the boundary condition. Fix _z ∈ ∂U_ , then there is a cone _Cz_ ( _α_ ) based at _z_ with angle _α >_ 0 with _Cz_ ( _α_ ) _∩B_ ( _z, h_ ) _⊂ U_<sup>_c_</sup> . By Lemma 3.11, for any positive integer _k_ and _h_<sup>_′_</sup> _>_ 0, we have


for all _x_ with _| x − z| <_ 2<sup>_−k_</sup> _h_<sup>_′_</sup> . Given _ε >_ 0, there is a 0 _< δ ≤ h_ such that _|ϕ_ ( _y_ ) _− ϕ_ ( _z_ ) _| < ε_ for all _y ∈ ∂U_ with _|y − z| < δ_ . For all _x ∈ U_ with _|z − x| <_ 2<sup>_−k_</sup> _δ_ ,

If the Brownian motion hits the cone _Cz_ ( _α_ ), which is outside the domain _U_ , before the sphere _∂B_ ( _z, δ_ ), then _|z − B_ ( _τ_ ( _∂U_ )) _| < δ_ , and _ϕ_ ( _B_ ( _τ_ ( _∂U_ ))) is close to _ϕ_ ( _z_ ). The complement has

73

small probability. More precisely, (1.4) is bounded above by


This implies that _u_ is continuous on _U_ .

Remark 3.13. If the Poincar´e cone condition holds at every boundary point, we can simulate the solution of the Dirichlet problem by running many independent Brownian motions, starting in _x ∈ U_ until they hit the boundary of _U_ and letting _u_ ( _x_ ) be the average of the values of _ϕ_ on the hitting points. _⋄_

Remark 3.14. In Chapter 8 we will improve the results on the Dirichlet problem significantly and give sharp criteria for the existence of solutions. _⋄_

To justify the introduction of conditions on the domain we now give an example where the function _u_ of Theorem 3.12 fails to solve the Dirichlet problem.

Example 3.15. Take a solution _v_ : _B_ (0 _,_ 1) _→_ R of the Dirichlet problem on the planar disc _B_ (0 _,_ 1) with boundary condition _ϕ_ : _∂B_ (0 _,_ 1) _→_ R. Let _U_ = _{x ∈_ R<sup>2</sup> : 0 _< | x| <_ 1 _}_ be the punctured disc. We claim that _u_ ( _x_ ) = E _x_ � _ϕ_ ( _B_ ( _τ_ ( _∂U_ )))� fails to solve the Dirichlet problem on _U_ with boundary condition _ϕ_ : _∂B_ (0 _,_ 1) _∪{_ 0 _} →_ R if _ϕ_ (0) _̸_ = _v_ (0). Indeed, as planar Brownian motion does not hit points, by Corollary 2.23, the first hitting time _τ_ of _∂U_ = _∂B_ (0 _,_ 1) _∪{_ 0 _}_ agrees almost surely with the first hitting time of _∂B_ (0 _,_ 1). Then, by _⋄_ Theorem 3.12, _u_ (0) = E0[ _ϕ_ ( _B_ ( _τ_ ))] = _v_ (0) _̸_ = _ϕ_ (0).

We now show how the techniques we have developed so far can be used to prove a classical result from harmonic analysis, Liouville’s theorem, by probabilistic means. The proof uses the reflection principle for higher-dimensional Brownian motion.

Theorem 3.16 (Liouville’s theorem). _Any bounded harmonic function on_ R<sup>_d_</sup> _is constant._

**Proof.** Let _u_ : R<sup>_d_</sup> _→_ [ _−M, M_ ] be a harmonic function, _x_ , _y_ two distinct points in R<sup>_d_</sup> , and _H_ the hyperplane so that the reflection in _H_ takes _x_ to _y_ . Let _{B_ ( _t_ ) : _t ≥_ 0 _}_ be Brownian motion started at _x_ , and _{B_ ( _t_ ): _t ≥_ 0 _}_ its reflection in _H_ . Let _τ_ ( _H_ ) = min _{t_ : _B_ ( _t_ ) _∈ H}_ and note that

(1.5) _{B_ ( _t_ ): _t ≥ τ_ ( _H_ ) _}_ =d _{B_ ( _t_ ): _t ≥ τ_ ( _H_ ) _}._

Harmonicity implies that E _x_ [ _u_ ( _B_ ( _t_ ))] = _u_ ( _x_ ) and decomposing the above into _t < τ_ ( _H_ ) and _t ≥ τ_ ( _H_ ) we get


A similar equality holds for _u_ ( _y_ ). Now, using (1.5),

_|u_ ( _x_ ) _− u_ ( _y_ ) _|_ = ��E� _u_ ( _B_ ( _t_ )) 1 _{t<τ_ ( _H_ ) _}_ � _−_ E� _u_ ( _B_ ( _t_ )) 1 _{t<τ_ ( _H_ ) _}_ ��� _≤_ 2 _M_ P _{t < τ_ ( _H_ ) _} →_ 0 _,_

as _t →∞_ . Thus _u_ ( _x_ ) = _u_ ( _y_ ), and since _x_ and _y_ were chosen arbitrarily, _u_ must be constant.

74

**2. Recurrence and transience of Brownian motion**

A Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ in dimension _d_ is called _transient_ if


Note that the event _{_ lim _t↑∞ |B_ ( _t_ ) _|_ = _∞}_ is a tail event and hence, by Kolmogorov’s zero-one law, it must have probability zero or one. In this section we decide in which dimensions _d_ the Brownian motion is transient, and in which it is not. This question is intimately related to the exit probabilities of the Brownian motion from an annulus: Suppose the motion starts at a point _x_ inside an annulus


What is the probability that the Brownian motion hits _∂B_ (0 _, r_ ) before _∂B_ (0 _, R_ )? The answer is given in terms of harmonic functions on the annulus and is therefore closely related to the Dirichlet problem.

To find explicit solutions _u_ : _A_<sup>¯</sup> _→_ R of the Dirichlet problem on an annulus it is first reasonable to assume that _u_ is spherically symmetric, i.e. there is a function _ψ_ : [ _r, R_ ] _→_ R such that _u_ ( _x_ ) = _ψ_ ( _| x|_<sup>2</sup> ). We can express derivatives of _u_ in terms of _ψ_ as


Therefore, ∆ _u_ = 0 means


Letting _y_ = _| x|_<sup>2</sup> _>_ 0 we can write this as


This is solved by every _ψ_ satisfying _ψ_<sup>_′_</sup> ( _y_ ) = _y_<sup>_−d/_2</sup> and thus ∆ _u_ = 0 holds on _{| x|̸_ = 0 _}_ for


We write _u_ ( _r_ ) for the value of _u_ ( _x_ ) for all _x ∈ ∂B_ (0 _, r_ ). Now define stopping times

_Tr_ = _τ_ ( _∂B_ (0 _, r_ )) = inf _{t >_ 0 : _|B_ ( _t_ ) _|_ = _r}_ for _r >_ 0 _,_

and denote by _T_ = _Tr ∧ TR_ the first exit time from _A_ . By Theorem 3.12 we have _u_ ( _x_ ) = E _x_ � _u_ ( _B_ ( _T_ ))� = _u_ ( _r_ )P _x{Tr < TR}_ + _u_ ( _R_ )(1 _−_ P _x{Tr < TR}_ ) _._

This formula can be solved


and we get an explicit solution for the exit problem.

75

Theorem 3.17. _Suppose {B_ ( _t_ ) : _t ≥_ 0 _} is a Brownian motion in dimension d ≥_ 1 _started in x ∈ A_ := _{x ∈_ R<sup>_d_</sup> : _r ≤| x| ≤ R}_

_inside an annulus A with radii_ 0 _< r < R < ∞. Then,_


Letting _R ↑∞_ in Theorem 3.17 leads to the following corollary.

Corollary 3.18. _For any x̸ ∈B_ (0 _, r_ ) _, we have_


We now apply this to the problem of _recurrence_ and _transience_ of Brownian motion in various dimensions. Generally speaking, we call a Markov process _{X_ ( _t_ ): _t ≥_ 0 _}_ with values in R<sup>_d_</sup>

- **point recurrent** , if for every _x ∈_ R<sup>_d_</sup> , almost surely, there is a (random) sequence _tn ↑∞_ such that _X_ ( _tn_ ) = _x_ for all _n ∈_ N,

- **neighbourhood recurrent** , if, for every _x ∈_ R<sup>_d_</sup> and _ε >_ 0, almost surely, there exists a (random) sequence _tn ↑∞_ such that _X_ ( _tn_ ) _∈B_ ( _x, ε_ ) for all _n ∈_ N.

- **transient** , if it converges to infinity almost surely.

Theorem 3.19. _Brownian motion is_

- _point recurrent in dimension d_ = 1 _,_

- _neighbourhood recurrent, but not point recurrent, in d_ = 2 _,_

- _transient in dimension d ≥_ 3 _._

**Proof.** We leave the case _d_ = 1 as Exercise 3.3, and look at dimension _d_ = 2. Fix _ε >_ 0 and _x ∈_ R<sup>_d_</sup> . By Corollary 3.18 and shift-invariance the stopping time _t_ 1 = inf _{t >_ 0: _B_ ( _t_ ) _∈ B_ ( _x, ε_ ) _}_ is almost surely finite. Using the strong Markov property at time _t_ 1 + 1 we see that this also applies to _t_ 2 = inf _{t > t_ 1 + 1: _B_ ( _t_ ) _∈B_ ( _x, ε_ ) _}_ , and continuing like this, we obtain a sequence of times _tn ↑∞_ such that, almost surely, _B_ ( _tn_ ) _∈B_ ( _x, ε_ ) for all _n ∈_ N. Taking a union over a countable family of small balls, which form a basis of the Eulidean topology, implies that in _d_ = 2 Brownian motion is neighbourhood recurrent. Recall from Corollary 2.23 that planar Brownian motion does not hit points, hence it cannot be point recurrent.

It remains to show that Brownian motion is transient in dimensions _d ≥_ 3. Look at the events _An_ := _{|B_ ( _t_ ) _| > n_ for all _t ≥ Tn_ 3 _}._ Recall from Proposition 1.23 that _Tn_ 3 _< ∞_ almost surely. By the strong Markov property, for every _n ≥|x|_<sup>1</sup><sup>_/_3</sup> ,


76

Note that the right hand side is summable, and hence the Borel-Cantelli lemma shows that only finitely many of the events _A_<sup>c</sup> _n_<sup>occur,which implies that</sup><sup>_|B_(</sup><sup>_t_)</sup><sup>_|_diverges to infinity,almost</sup> surely, and hence that Brownian motion in _d ≥_ 3 is transient.

Remark 3.20. Neighbourhood recurrence, in particular, implies that the path of a planar _⋄_ Brownian motion (running for an infinite amount of time) is dense in the plane.

We now have a qualitative look at the transience of Brownian motion in R<sup>_d_</sup> , _d ≥_ 3, and ask for the speed of escape to infinity. This material is slightly more advanced and can be skipped on first reading.

Consider a standard Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ in R<sup>_d_</sup> , for _d ≥_ 3, and fix a sequence _tn ↑∞_ . For any _ε >_ 0, by Fatou’s lemma,


By the Hewitt Savage zero-one law, the probability on the left-hand side must therefore be one, whence


This statement is refined by the Dvoretzky-Erd˝os test.

Theorem* 3.21 (Dvoretzky-Erd˝os test). _Let {B_ ( _t_ ): _t ≥_ 0 _} be Brownian motion in_ R<sup>_d_</sup> _for d ≥_ 3 _and f_ : (0 _, ∞_ ) _→_ (0 _, ∞_ ) _increasing. Then_


_Conversely, if the integral diverges, then_ lim inf _|B_ ( _t_ ) _|/f_ ( _t_ ) = 0 _almost surely. t↑∞_

For the proof we first recall two generally useful tools. The first is an easy case of the PaleyZygmund inequality, see Exercise 3.4 for the full statement.

Lemma 3.22 (Paley-Zygmund inequality). _For any nonnegative random variable X with_ E[ _X_<sup>2</sup> ] _< ∞,_


**Proof.** The Cauchy-Schwarz inequality gives


and the required inequality follows immediately.

77

The second tool is a version of the Borel-Cantelli lemma, which allows some dependence of the events. This is known as the Kochen-Stone lemma, and is a consequence of the Paley-Zygmund inequality, see Exercise 3.5 or [ **FG97** ].

Lemma 3.23. _Suppose E_ 1 _, E_ 2 _, . . . are events with_


_Then, with positive probability, infinitely many of the events take place._

A core estimate in the proof of the Dvoretzky-Erd˝os test is the following lemma, which is based on the hitting probabilities of the previous paragraphs.

Lemma 3.24. _There exists a constant C_ 1 _>_ 0 _depending only on the dimension d such that, for any ρ >_ 0 _, we have_


**Proof.** We use Corollary 3.18 for the probability that the motion started at time one hits _B_ (0 _, ρ_ ), to see that


By considering the integration domains _|y_ + _x| ≥|y|_ and _|y_ + _x| ≤|y|_ separately, it is easy to see that the integral on the right is uniformly bounded in _x_ .

**Proof of Theorem 3.21.** Define events


By Brownian scaling, monotonicity of _f_ , and Lemma 3.24,


Now assume that the integral converges, or equivalently, that


Then the Borel Cantelli lemma and (2.3) imply that, almost surely, the set _{t >_ 0 : _|B_ ( _t_ ) _| ≤ f_ ( _t_ ) _}_ is bounded. Since (2.3) also applies to any constant multiple of _f_ in place of _f_ , it follows that lim inf _t↑∞ |B_ ( _t_ ) _|/f_ ( _t_ ) = _∞_ almost surely.

For the converse, suppose that the integral diverges, whence


78

In view of (2.2), we may assume that _f_ ( _t_ ) _< √t_ for all large enough _t_ . Changing _f_ on a finite interval, we may assume that this inequality holds for all _t >_ 0. For _ρ ∈_ (0 _,_ 1), consider the random variable _Iρ_ = �12<sup>1</sup><sup>_{|B_(</sup><sup>_t_)</sup><sup>_| ≤ρ}_.Sincethedensityof</sup><sup>_|B_(</sup><sup>_t_)</sup><sup>_|_</sup> on the unit ball is bounded from above and also away from zero for _t ∈_ [1 _,_ 2], we infer that


for suitable constants depending only on the dimension. To complement this by an estimate of the second moment, we use the Markov property to see that


where the inner expectation is with respect to a Brownian motion _{B_<sup>˜</sup> ( _t_ ): _t ≥_ 0 _}_ started in the fixed point _B_ ( _t_ ), whereas the outer expectation is with respect to _B_ ( _t_ ). We analyse the dependence of the inner expectation on the starting point. Given _x̸_ = 0, we let _T_ = inf _{t >_ 0: _|B_ ( _t_ ) _|_ = _x}_ and use the strong Markov property to see that


so that the expectation is maximal if the process is started at the origin. Hence we obtain that


Moreover, by Brownian scaling, we obtain


where the finiteness of the constant _C_ 4 is easily checked by substituting _sx_<sup>2</sup> for _s_ in the inner integral. In summary, we have E[ _Iρ_<sup>2]</sup><sup>_≤_2</sup><sup>_C_3</sup><sup>_C_4</sup><sup>_ρd_+2.BythePaley-Zygmundinequality,fora</sup> suitable constant _C_ 5 _>_ 0,


Now choose _ρ_ = _f_ (2<sup>_n_</sup> )2<sup>_−n/_2</sup> , which is smaller than one, as _f_ ( _t_ ) _< √t_ . By Brownian scaling and monotonicity of _f_ , we have


79

so<sup>�</sup> _n_<sup>P(</sup><sup>_An_)=</sup><sup>_∞_by(2.4).For</sup><sup>_m<n −_1,theMarkovpropertyattime2</sup><sup>_n−_1,Brownian</sup> scaling and Lemma 3.24 yield that


From this we get that


The Kochen-Stone lemma now yields that P _{An_ infinitely often _} >_ 0, whence by the Hewitt-Savage 0-1-law this probability is 1. Thus the set _{t >_ 0: _|B_ ( _t_ ) _| ≤ f_ ( _t_ ) _}_ is almost surely unbounded. Since (2.4) also applies to _εf_ in place of _f_ for any _ε >_ 0, it follows that lim inf _t↑∞ |B_ ( _t_ ) _|/f_ ( _t_ ) = _∞_ almost surely

### **3. Occupation measures and Green’s functions**

We now address the following question: Given a bounded domain _U ⊂_ R<sup>_d_</sup> , how much time does Brownian motion spend in _U_ ? Our first result states that for a linear Brownian motion running for a finite amount of time, this time is comparable to the Lebesgue measure of _U_ .

Theorem 3.25. _Let {B_ ( _s_ ): _s ≥_ 0 _} be a linear Brownian motion and t >_ 0 _. Define the occupation measure µt by_


_Then, almost surely, µt is absolutely continuous with respect to the Lebesgue measure._

**Proof.** By Lebesgue’s theorem absolute continuity with respect to the Lebesgue measure means that, for _µt_ -almost very _x ∈_ R,


To see this we use first Fatou’s lemma and then Fubini’s theorem,


80

and this implies that


This implies that _µt_ is absolutely continuous with respect to _L_ .

We now turn to higher dimensions _d ≥_ 2. A first simple result shows that whether the overall time spent in a bounded set is finite or not depends just on transience or recurrence of the process.

Theorem 3.26. _Let U ⊂_ R<sup>_d_</sup> _be a nonempty bounded open set and x ∈_ R<sup>_d_</sup> _arbitrary._


**Proof.** As _U_ is contained in a ball and contains a ball, it suffices to show this for balls. By shifting, we can even restrict to balls _U_ = _B_ (0 _, r_ ) centred in the origin. Let us start with the first claim. We let _d ≤_ 2 and let _G_ = _B_ (0 _,_ 2 _r_ ). Let _T_ 0 = 0 and, for all _k ≥_ 1, let

_Sk_ = inf _{t > Tk−_ 1 : _B_ ( _t_ ) _∈ U }_ and _Tk_ = inf _{t > Sk_ : _B_ ( _t_ ) _̸ ∈ G}._

Recall that, almost surely, these stopping times are finite. From the strong Markov property we infer, for _k ≥_ 1,


by rotation invariance. The second expression does not depend on _k_ , so that the random variables


are independent and identically distributed. As they are not identically zero, but nonnegative, they have positive expectation and, by the strong law of large numbers we infer


which proves the first claim. For the second claim, we first look at Brownian motion started in the origin and obtain, making good use of Fubini’s theorem and denoting by p : [0 _, ∞_ ) _×_ R<sup>_d_</sup> _×_ R<sup>_d_</sup> _→_ [0 _,_ 1] the transition density of Brownian motion,


81

Now we can use the substitution _t_ = _ρ_<sup>2</sup> _/s_ and obtain, for a suitable constant _C_ ( _d_ ) _< ∞_ ,


For start in an arbitrary _x̸_ = 0, we look at a Brownian motion started in 0 and a stopping time _T_ , which is the first hitting time of the sphere _∂B_ (0 _, | x|_ ). Using spherical symmetry and the strong Markov property we obtain


In the case when Brownian motion is transient it is interesting to ask further for the expected time the process spends in a bounded open set. In order not to confine this discussion to the case _d ≥_ 3 we introduce suitable stopping rules for Brownian motion in _d_ = 2.

Definition 3.27. _Suppose that {B_ ( _t_ ) : 0 _≤ t ≤ T } is a d-dimensional Brownian motion and one of the following three cases holds:_

(1) _d ≥_ 3 _and T_ = _∞,_


(3) _d ≥_ 2 _and T is the first exit time from a bounded domain D containing_ 0 _._

_We use the convention that D_ = R<sup>_d_</sup> _in cases (1), (2). We refer to these three cases by saying ⋄ that {B_ ( _t_ ) : 0 _≤ t ≤ T } is a_ **transient Brownian motion** _._

Remark 3.28. For a transient Brownian motion _{B_ ( _t_ ) : 0 _≤ t ≤ T }_ , given _F_<sup>+</sup> ( _t_ ), on the event _{B_ ( _t_ ) = _y, t < T }_ , the process _{B_ ( _s_ + _t_ ) : 0 _≤ s ≤ T }_ is again a transient Brownian motion of the same type, started in _y_ . We do not consider Brownian motion stopped at a _fixed_ time, because this model lacks exactly this form of the Markov property. _⋄_

Proposition 3.29. _For transient Brownian motion {B_ ( _t_ ) : 0 _≤ t ≤ T } there exists a transition_ ( _sub-_ ) _density_ p<sup>_∗_</sup> : [0 _, ∞_ ) _×_ R<sup>_d_</sup> _×_ R<sup>_d_</sup> _→_ [0 _,_ 1] _such that, for any t >_ 0 _,_


_Moreover, for all t ≥_ 0 _and L-almost every x, y ∈ D we have_ p<sup>_∗_</sup> ( _t, x, y_ ) = p<sup>_∗_</sup> ( _t, y, x_ ) _._

**Proof.** Fix _t_ throughout the proof. For the existence of the density, by the Radon-Nikodym theorem, it suffices to check that P _x{B_ ( _t_ ) _∈ A_ and _t ≤ T }_ = 0 _,_ if _A_ is a Borel set of Lebesgue measure zero. This is obvious, by just dropping the requirement _t ≤ T_ , and recalling that _B_ ( _t_ ) is normally distributed. If _d ≥_ 3 and _T_ = _∞_ , or if _d ≥_ 2 and _T_ is independent, exponentially distributed symmetry is obvious.

Hence we can now concentrate on the case _d ≥_ 2 and a bounded domain _D_ . We fix a compact set _K ⊂ D_ and define, for every _x ∈ K_ and _n ∈_ N, a measure _µ_<sup>(</sup> _x_<sup>_n_)</sup> on the Borel sets _A ⊂ D_ , ( _n_ ) _µx_<sup>(</sup><sup>_A_) = P</sup><sup>_x_</sup> � _B_ ( 2<sup>_<u>ktn</u>_)</sup><sup>_∈K_forall</sup><sup>_k_= 0</sup><sup>_, . . . ,_2</sup><sup>_n_and</sup><sup>_B_(</sup><sup>_t_)</sup><sup>_∈A_</sup> � _._

82

Then _µ_<sup>(</sup> _x_<sup>_n_)</sup> has a density


where _z_ 0 = _x_ , _z_ 2 _n_ = _y_ and p is the transition density of _d_ -dimensional Brownian motion. As p is symmetric in the space variables, so is p<sup>_∗_</sup> _n_<sup>forevery</sup><sup>_n_.Notethatp</sup><sup>_∗_</sup> _n_<sup>isdecreasingin</sup><sup>_n_.</sup> From the monotone convergence theorem one can see that p<sup>_∗_</sup> _K_<sup>(</sup><sup>_t, x, y_):=lim p</sup><sup>_∗_</sup> _n_<sup>(</sup><sup>_t, x, y_)isa</sup> transition subdensity of Brownian motion stopped upon leaving _K_ . The symmetry of p<sup>_∗_</sup> _n_<sup>gives</sup> p<sup>_∗_</sup> _K_<sup>(</sup><sup>_t, x, y_)=p</sup><sup>_∗_</sup> _K_<sup>(</sup><sup>_t, y, x_).Choosinganincreasingsequenceofcompactsetsexhausting</sup><sup>_U_and</sup> taking a monotone limit yields a symmetric version p<sup>_∗_</sup> ( _t, x, y_ ) of the transition density.

Definition 3.30. _For transient Brownian motion {B_ ( _t_ ) : 0 _≤ t ≤ T } we define the_ **Green’s function** _G_ : R<sup>_d_</sup> _×_ R<sup>_d_</sup> _→_ [0 _, ∞_ ] _by_


_The Green’s function is also called the_ **Green kernel** _. Sometimes it is also called the_ potential kernel _, but we shall reserve this terminus for a closely related concept, see Remark 8.20. ⋄_

In probabilistic terms _G_ is the density of the _expected_ occupation measure for the transient Brownian motion started in _x_ .

Theorem 3.31. _If f_ : R<sup>_d_</sup> _→_ [0 _, ∞_ ] _is measurable, then_


**Proof.** Fubini’s theorem implies


by definition of the Green’s function.

In case (1), i.e. if _T_ = _∞_ , Green’s function can be calculated explicitly.

Theorem 3.32. _If d ≥_ 3 _and T_ = _∞, then_


83

**Proof.** Assume _d ≥_ 3 and use the substitution _s_ = _| x − y|_<sup>2</sup> _/_ 2 _t_ to obtain,


where Γ( _x_ ) = �0 _∞_<sup>_sx−_1</sup><sup>_e−s ds_istheGammafunction.Thisprovesthat</sup><sup>_G_hasthegivenform</sup> and the calculation above also shows that the integral is infinite if _d ≤_ 2.

In case (2), if Brownian motion is stopped at an independent exponential time, one can find the asymptotics of _G_ ( _x, y_ ) for _x → y_ .

Theorem 3.33. _If d_ = 2 _and T is an independent exponential time with parameter λ >_ 0 _, then_


**Proof.** Note that the transition sub-density of Brownian motion stopped at an independent exponential time with parameter _λ >_ 0 equals


where p is the transition density for (unstopped) Brownian motion. Hence


We thus get _Gλ_ ( _x − y_ ) = _G_ 1( _√λ_ ( _x − y_ )) and may assume without loss of generality that _λ_ = 1. Then


For an upper bound we use that, for _|x − y| ≤_ 1, that


This gives, with 0 _< γ_ := _−_


from which the upper bound follows. For the lower bound we use


and thus


84

We now explore some of the major analytic properties of Green’s function.

Theorem 3.34. _In all three cases of transient Brownian motion in d ≥_ 2 _, the Green’s function has the following properties:_

- (i) _G_ ( _x, y_ ) _is finite if x̸_ = _y._

- (ii) _G_ ( _x, y_ ) = _G_ ( _y, x_ ) _for all x, y ∈ D._

- (iii) _for any y ∈ D the Green’s function G_ ( _· , y_ ) _is harmonic on D \ {y}._

This result is easy in the case _d ≥_ 3, _T_ = _∞_ , where the Green’s function is explicitly known by Theorem 3.32. We therefore focus on the case _d_ = 2 and prepare the proof by two lemmas, which are of some independent interest.

Lemma 3.35. _If d_ = 2 _, for x, z ∈_ R<sup>2</sup> _with |x − z|_ = 1 _,_


_where_ p _is the transition kernel for the (unstopped) Brownian motion._

**Proof.** For _|x − z|_ = 1, we obtain


and by changing the order of integration this equals


which completes the proof.

Lemma 3.36. _Let D ⊂_ R<sup>2</sup> _be a bounded domain and x, y ∈ D. Then with u_ ( _x_ ) = 2 log _|x|,_


_where τ is the first exit time from D._

**Proof.** Let _f_ : _D →_ [0 _, ∞_ ) be continuous with compact support. Picking _v ∈ ∂B_ (0 _,_ 1), we obtain for any _x ∈ D_ ,


85

This implies the statament for every _x ∈ D_ and almost every _y ∈ D_ . It remains to show that we can choose a version of the density p<sup>_∗_</sup> ( _t, · , ·_ ) such that the statement holds for _every x, y ∈ D_ . Indeed, let


Integrating over all _y ∈ A_ gives that this is indeed a transition density for the stopped process. Moreover, adding and subtracting p( _t, x, x_ + _v_ ) = p( _t, B_ ( _τ_ ) _, B_ ( _τ_ ) + _v_ ) on the right hand side and integrating over _t ∈_ (0 _, ∞_ ) yields the statement for the Green’s function associated to this particular choice of transition kernel p<sup>_∗_</sup> , which therefore holds for all _x, y ∈ D_ .

**Proof of Theorem 3.34.** We first look at properties (i), (ii) and continuity of _G_ ( _· , y_ ) on _D \ {y}_ . These three properties are obvious in the case _d ≥_ 3, _T_ = _∞_ , by the explicit form of the Green’s function uncovered in Theorem 3.32. If Brownian motion is stopped at an independent exponential time, it is easy to see from p<sup>_∗_</sup> ( _t, x, y_ ) = _e_<sup>_−λt_</sup> p( _t, x, y_ ) that the Green’s function is finite everywhere except on the diagonal ∆= _{_ ( _x, y_ ): _x_ = _y}_ , and symmetric. Moreover, continuity is easy to check using dominated convergence. We can therefore focus on the case where the Brownian motion is stopped upon leaving a bounded domain _D_ .

First let _d_ = 2. Lemma 3.35 gives, for _x̸_ = _y_ , that _G_ ( _x, y_ ) _< ∞_ . However, we have E _x_ [ _−_ 1 _/_ (2 _π_ ) _u_ ( _B_ ( _τ_ ) _− x_ )] _< ∞_ , hence _G_ ( _x, x_ ) = _∞_ by Lemma 3.36. If _x ∈ D_ , then _G_ ( _x, ·_ ) is continuous on _D \{x}_ , because the right hand side of the equation in Lemma 3.36 is continuous. Similarly, if _y ∈ D_ the right hand side is continuous in _x_ on _D \ {y}_ , as E _x_ [ _u_ ( _B_ ( _τ_ ) _− y_ )] is harmonic in _x_ . Hence _G_ ( _· , x_ ) is also continuous on _D \ {x}_ . The symmetry follows from the almost-everywhere symmetry of p<sup>_∗_</sup> ( _t, · , ·_ ) together with the continuity.

Next, if _d ≥_ 3 we can carry out the same proof replacing _−_ 1 _/_ (2 _π_ ) _u_ ( _x, y_ ) by _ℓ_ ( _x, y_ ) = _c_ ( _d_ ) _|x − y|_<sup>2</sup><sup>_−d_</sup> . In fact the arguments become significantly easier because


and there is no need to subtract a ‘renormalisation’ term. Finally, we show property (iii) in all cases. Define


We prove that _Gε_ ( _· , y_ ) satisfies the mean value property on _D \ B_ ( _y, ε_ ), i.e.

The result follows from this since, using continuity of _G_ , for _x, y ∈ D_ with _|x − y| > r_ ,


where the last equality follows from the bounded convergence theorem.

86

Fix _x̸_ = _y_ in _D_ , let 0 _< r < | x−y|_ and let _ε < | x−y|−r_ . Denote _τ_ = _T ∧_ inf _{t_ : _|B_ ( _t_ ) _−x|_ = _r}_ . As a Brownian motion started in _x_ spends no time in _B_ ( _y, ε_ ) before time _τ_ , we can write


where the inner expectation is with respect to a Brownian motion _{B_<sup>˜</sup> ( _t_ ): _t ≥_ 0 _}_ started in the fixed point _B_ ( _τ_ ), whereas the outer expectation is with respect to _B_ ( _τ_ ). By the strong Markov property and since, given _τ < T_ , the random variable _B_ ( _τ_ ) is uniformly distributed on _∂B_ ( _x, r_ ), by rotational symmetry, we conclude,


so that _Gε_ satisfies the mean value property and hence is harmonic by Theorem 3.2.

Remark 3.37. Suppose _d ≥_ 3 and _T_ = _∞_ . Let _K_ be a compact set and _µ_ a measure on _∂K_ . Then


is a harmonic function on _K_<sup>c</sup> . This can be verified easily from the harmonicity of _G_ ( _· , y_ ) and the mean value property. Physically, _u_ ( _x_ ) is the electrostatic (or Newtonian) potential at _x_ resulting from a charge represented by _µ_ . In particular, the Green function _G_ ( _· , y_ ) can be interpreted as the electrostatic potential induced by a unit charge in the point _y_ . An interesting question is whether every positive harmonic function on _K_<sup>c</sup> can be represented in such a way by a suitable _µ_ . We will come back to this question in Chapter 8. _⋄_

### **4. The harmonic measure**

A particularly appealing way of writing the harmonic function _u_ in Theorem 3.8 is in terms of the harmonic measure on _∂U_ . Definition 3.38. _Let {B_ ( _t_ ): _t ≥_ 0 _} be a d-dimensional Brownian motion, d ≥_ 2 _, started in some point x and fix a closed set A ⊂_ R<sup>_d_</sup> _. Define a measure µA_ ( _x, ·_ ) _by_


_for B ⊂ A Borel. In other words, µA_ ( _x, ·_ ) _is the distribution of the first hitting point of A, and the total mass of the measure is the probability that a Brownian motion started in x ever hits the set A. The harmonic measure is supported by ∂A. ⋄_

87

The following corollary is only an equivalent reformulation of Theorem 3.12.

Corollary 3.39. _If the Poincar´e cone condition is satisfied at every point x ∈ ∂U on the boundary of a bounded domain U , then the solution of the Dirichlet problem with boundary condition ϕ_ : _∂U →_ R _, can be written as_


Remark 3.40. Of course, the harmonicity of _u_ does not rely on the Poincar´e cone condition. In fact, by Theorem 3.8, for any compact _A ⊂_ R<sup>_d_</sup> and Borel set _B ⊂ ∂A_ , the function _⋄ x �→ µA_ ( _x, B_ ) is harmonic on _A_<sup>c</sup> .

Besides its value in the discussion of the Dirichlet problem, the harmonic measure is also interesting in its own right, as it intuitively weighs the points of _A_ according to their accessibility from _x_ . We now show that the measures _µA_ ( _x, ·_ ) for different values of _x ∈ A_<sup>c</sup> are mutually absolutely continuous. This is a form of the famous _Harnack principle_ .

Theorem 3.41 (Harnack principle). _Suppose A ⊂_ R<sup>_d_</sup> _is compact and x, y are in the unbounded component of A_<sup>c</sup> _. Then µA_ ( _x, ·_ ) _≪ µA_ ( _y, ·_ ) _._

**Proof.** Given _B ⊂ ∂A_ Borel, by Remark 3.40, the mapping _x �→ µA_ ( _x, B_ ) is a harmonic function on _A_<sup>c</sup> . If it takes the value zero for some _y ∈ A_<sup>c</sup> , then _y_ is a minimum and the maximum principle, Theorem 3.5, together with the subsequent remark, imply that _µA_ ( _x, B_ ) = 0 for all _x ∈ A_<sup>c</sup> , as required.

The Harnack principle allows to formulate the following definition.

Definition 3.42. _A compact set A is called_ **nonpolar for Brownian motion** _, or simply_ **nonpolar** _, if µA_ ( _x, A_ ) _>_ 0 _for one (and hence for all) x ∈ A_<sup>c</sup> _. Otherwise, the set A is called_ **polar for Brownian motion** _. ⋄_

We now give an explicit formula for the harmonic measures on the unit sphere _∂B_ (0 _,_ 1). Note that if _x_ = 0 then the distribution of _B_ ( _τ_ ) is (by symmetry) the uniform distribution, but if _x_ is another point it is an interesting problem to determine this distribution in terms of a probability density.

Theorem 3.43 (Poisson’s formula). _Suppose that A ⊂ ∂B_ (0 _,_ 1) _is a Borel subset of the unit sphere for d ≥_ 2 _. Let ϖ denote the uniform distribution on the unit sphere. Then, for all x̸ ∈ ∂B_ (0 _,_ 1) _,_


Remark 3.44. The density appearing in the theorem is usually called the _Poisson kernel_ and appears frequently in potential theory. _⋄_

88

**Proof.** We start by looking at the case _| x| <_ 1. To prove the theorem we indeed show that for every bounded measurable _f_ : R<sup>_d_</sup> _→_ R we have


which on the one hand implies the formula by choosing indicator functions, on the other hand, by the monotone class theorem, see e.g. [ **Du95** , Chapter 5, (1.5)], it suffices to show this for smooth functions. To prove (4.1) we recall Theorem 3.12, which tells us that we just have to show that the right hand side as a function in _x ∈B_ (0 _,_ 1) defines a solution of the Dirichlet problem on _B_ (0 _,_ 1) with boundary value _f_ .

To check this, one first checks that<sup>1</sup><sup>_−| x|_2</sup> _| x−y|_<sup>_d_is harmonic in</sup><sup>_x_on</sup><sup>_B_(0</sup><sup>_,_1), which is a straightforward</sup> calculation, and then argues that it is allowed to differentiate twice under the integral sign. To check the boundary condition first look at the case _f ≡_ 1, in which case we have to show that, for all _x ∈B_ (0 _,_ 1),


We use Theorem 3.12 to show this. Indeed, observe that _I_ (0) = 1, _I_ is invariant under rotation and ∆ _I_ = 0 on _B_ (0 _,_ 1), by the first part. Now let _x ∈B_ (0 _,_ 1) with _| x|_ = _r <_ 1 and let _τ_ := inf _{t_ : _|B_ ( _t_ ) _| > r}_ . By Theorem 3.12,


using rotation invariance in the second step. Hence _I ≡_ 1. Now we show that the right hand side in the theorem can be extended continuously to all points _y ∈ ∂B_ (0 _,_ 1) by _f_ ( _y_ ). We write _D_ 0 for _∂B_ (0 _,_ 1) with a _δ_ -neighbourhood _B_ ( _y, δ_ ) removed and _D_ 1 = _∂B_ (0 _,_ 1) _\ D_ 0. We have, using that _I ≡_ 1, for all _x ∈B_ ( _y, δ/_ 2) _∩ U_ ,


For fixed _δ >_ 0 the first term goes to 0 as _x → y_ by dominated convergence, whereas the second can be made arbitrarily small by choice of _δ_ . This completes the proof if _x ∈B_ (0 _,_ 1).

If _| x| >_ 1 we use _inversion at the unit circle_ to transfer the problem to the case studied before. By a straightforward calculation, one can check that a function _u_ : _B_ (0 _,_ 1) c _→_ R is harmonic if and only if its inversion _u_<sup>_∗_</sup> : _B_ (0 _,_ 1) _\ {_ 0 _} →_ R defined by


is harmonic. Now suppose that _<u>f</u>_ : _∂B_ (0 _,_ 1) _→ R_ is a smooth function on the boundary. Then define a harmonic function _u_ : _B_ (0 _,_ 1) c _→_ R by


89

Then _u_<sup>_∗_</sup> : _B_ (0 _,_ 1) _\ {_ 0 _} →_ R is bounded and harmonic. By Exercise 3.8 we can extend it to the origin, so that the extension is harmonic on _B_ (0 _,_ 1). In fact, this extension is obviously given by _u_<sup>_∗_</sup> (0) = � _ϕ dϖ_ . The harmonic extension is continuous on the closure, with boundary values given by _f_ . Hence it agrees with the function of the first part, and _u_ = _u_<sup>_∗∗_</sup> must be its inversion, which gives the claimed formula.

We now fix a compact nonpolar set _A ⊂_ R<sup>_d_</sup> , and look at the harmonic measure _µA_ ( _x, ·_ ) when _x →∞_ . The first task is to make sure that this object is well-defined.

Theorem 3.45. _Let A ⊂_ R<sup>_d_</sup> _be a compact, nonpolar set, then there exists a probability measure µA on A, given by_


_This measure is called the_ **harmonic measure** _(from infinity)._

Remark 3.46. The harmonic measure weighs the points of _A_ according to their accessibility from infinity. It is naturally supported by the _outer boundary_ of _A_ , which is the boundary of _⋄_ the infinite connected component of R<sup>_d_</sup> _\ A_ .

The proof is prepared by a lemma, which is yet another example how the strong Markov property can be exploited to great effect.

Lemma 3.47. _For A ⊂_ R<sup>_d_</sup> _compact and nonpolar and every ε >_ 0 _, there exists a large R >_ 0 _such that, for all x ∈ ∂B_ (0 _, R_ ) _and any hyperplane H ⊂_ R<sup>_d_</sup> _containing the origin,_


**Proof.** Pick a radius _r >_ 0 such that _A ⊂B_ (0 _, r_ ) and note from Remark 3.40 that _x �→_ P _x{τ_ ( _A_ ) _< ∞}_ is harmonic on _A_<sup>c</sup> . Therefore the minimum of this function on the compact set _∂B_ (0 _, r_ ) is positive, say _δ >_ 0. It therefore suffices to show that


Now there exists an absolute constant _q <_ 1 such that, for any _x ∈ ∂B_ (0 _,_ 2) and hyperplane _H_ ,


Let _k_ be large enough to ensure that _q_<sup>_k_</sup> _< εδ_ . Then, by the strong Markov property and Brownian scaling,


90

Iterating this and letting _R_ = _r_ 2<sup>_k_</sup> gives


as required to complete the proof.

**Proof of Theorem 3.45.** Let _x, y ∈ ∂B_ (0 _, r_ ) and _H_ be the hyperplane through the origin, which is orthogonal to _x − y_ . If _{B_ ( _t_ ) : _t ≥_ 0 _}_ is a Brownian motion started in _x_ , define _{B_ ( _t_ ) : _t ≥_ 0 _}_ the Brownian motion started in _y_ , obtained by defining _B_ ( _t_ ) as the reflection of _B_ ( _t_ ) at _H_ , for all times _t ≤ τ_ ( _H_ ), and _B_ ( _t_ ) = _B_ ( _t_ ) for all _t ≥ τ_ ( _H_ ). This coupling gives, for every _ε >_ 0 and sufficiently large _r_ ,


using Lemma 3.47 for the last inequality. In particular, we get _|µA_ ( _x, A_ ) _−µA_ ( _y, A_ ) _| ≤ εµA_ ( _x, A_ ). Next, let _|z| > r_ and apply the strong Markov property to obtain


We note that _µA_ ( _z, A_ ) = � _µB_ (0 _,r_ )( _z, dy_ ) _µA_ ( _y, A_ ) _≤_ (1 + _ε_ ) _µB_ (0 _,r_ )( _z, B_ (0 _, r_ )) _µA_ ( _x, A_ ), which leads to the estimate


and the same estimate can be performed with the roles of _x_ and _z_ reversed. As _ε >_ 0 was arbitrary, this implies that _µA_ ( _x, B_ ) _/µA_ ( _x, A_ ) converges as _x →∞_ .

Example 3.48. For any ball _B_ ( _x, r_ ) we have _µB_ ( _x,r_ ) = _ϖx,r_ , the uniform distribution. Indeed, _ϖx,r_ ( _·_ ) = _c_ ( _R_ ) � _∂B_ ( _x,R_ )<sup>_µB_(</sup><sup>_x,r_)(</sup><sup>_y,·_)</sup><sup>_dϖx,R_(</sup><sup>_y_),forall</sup><sup>_R>r_andasuitableconstant</sup><sup>_C_(</sup><sup>_R_),as</sup> the two balls are concentric, and both sides of the equation are rotationally invariant measures _⋄_ on the sphere _∂B_ ( _x, r_ ). Letting _R ↑∞_ , we obtain from Theorem 3.45, that _ϖx,r_ = _µB_ ( _x,r_ ).

The following surprising proposition shows that the harmonic measure from infinity can also be obtained without this limiting procedure.

Theorem 3.49. _Let A ⊂_ R<sup>_d_</sup> _be compact and suppose B_ ( _x, r_ ) _⊃ A, let ϖx,r be the uniform distribution on ∂B_ ( _x, r_ ) _. Then we have, for any Borel set B ⊂ A,_


91

Remark 3.50. The surprising fact here is that the right hand side does _not depend_ on the _⋄_ choice of the ball _B_ ( _x, r_ ).

The crucial observation behind this result is that, starting a Brownian motion in a uniformly chosen point on the boundary of a sphere, the first hitting point of any ball inside that sphere, if it exists, is again uniformly distributed, see Figure 2.


<!-- Start of picture text -->
���������������������������� ���������������������������� ���������������������������� ���������������������������� ���������������������������� ���������������������������� ����������������������������<br>Starting Brownian motion uniformly on the big circle, the distribution<br>point on the small circle is also uniform.<br> ⊂B ( y, s ) and B ⊂ ∂BB ( x, r ) Borel. Then<br>� µB ( x,r )( a, B )  ϖy,s ( da )<br>� µB ( x,r )( a, B ( x, r ))  ϖy,s ( da ) =  ϖx,r ( B ) .<br><!-- End of picture text -->

Figure 2. Starting Brownian motion uniformly on the big circle, the distribution of the first hitting point on the small circle is also uniform.

Lemma 3.51. _Let B_ ( _x, r_ ) _⊂B_ ( _y, s_ ) _and B ⊂ ∂BB_ ( _x, r_ ) _Borel. Then_

**Proof.** By Example 3.48 we have _ϖy,s_ = _µB_ ( _y,s_ ) and hence, for the normalization constant _c_ ( _R_ ) = 1 _/_ � _µB_ ( _y,s_ )( _a, B_ ( _y, s_ )) _ϖx,R_ ( _da_ ), we have


Hence, for any _B ⊂B_ ( _x, r_ ) Borel, using the Markov property in the second step,


because _B_ ( _x, R_ ) and _B_ ( _x, r_ ) are concentric. By substituting _B_ = _B_ ( _x, r_ ) into the equation, we see that the limit must be equal to the stated constant.

92

**Proof of Theorem 3.49.** Assume that _B_ ( _x, r_ ) and _B_ ( _y, s_ ) are two balls containing _A_ . We may then find a ball _B_ ( _z, t_ ) containing both these balls. Using Lemma 3.51 and the strong Markov property applied to the first hitting of _B_ ( _x, r_ ) we obtain, for any Borel set _B ⊂ A_ ,


for suitable constants _c_ 1 _, c_ 2 depending only on the choice of the balls. Choosing _B_ = _A_ gives the normalisation constant


and this shows that the right hand side in Theorem 3.49 is independent of the choice of the enclosing ball. It therefore must stay constant when its radius goes to infinity, thus completing the proof.

93

### **Exercises**

Exercise 3.1. Show that, if _u_ : _U →_ R is subharmonic, then


Conversely, show that any twice differentiable function _u_ : _U →_ R satisfying (1.2) is subharmonic. Also give an example of a discontinuous function _u_ satisfying (1.2).

Exercise 3.2 ( _∗_ ). Suppose _u_ : _B_ ( _x, r_ ) _→_ R is harmonic and bounded by _M_ . Show that the _k_<sup>th</sup> order partial derivatives are bounded by a constant multiple of _Mr_<sup>_−k_</sup> .

Exercise 3.3. Prove the case _d_ = 1 in Theorem 3.19.

Exercise 3.4 ( _∗_ ). Prove the strong form of the _Paley-Zygmund inequality_ : For any nonnegative random variable _X_ with E[ _X_<sup>2</sup> ] _< ∞_ and _λ ∈_ [0 _,_ 1),


Exercise 3.5. Prove the _Kochen-Stone lemma_ :

Suppose _E_ 1 _, E_ 2 _, . . ._ are events with


Then, with positive probability, infinitely many of the events take place. **Hint.** Apply the Paley-Zygmund inequality to _X_ = lim inf _n→∞_ 1 _En_ .

Exercise 3.6 ( _∗_ ). Suppose that _u_ is a radial harmonic function on the annulus _D_ = _{x ∈_ R<sup>_d_</sup> : _r < | x| < R}_ , where radial means _u_ ( _x_ ) = _u_ ˜( _| x|_ ) for some function _u_ ˜ : ( _r, R_ ) _→ R_ and all _x_ . Suppose further that _u_ is continuous on _D_<sup>¯</sup> . Show that,

- if _d ≥_ 3, there exist constants _a_ and _b_ such that _u_ ( _x_ ) = _a_ + _b| x|_<sup>2</sup><sup>_−d_</sup> ;

- if _d_ = 2, there exist constants _a_ and _b_ such that _u_ ( _x_ ) = _a_ + _b_ log _| x|_ .

Exercise 3.7 ( _∗_ ). Show that any positive harmonic function on R<sup>_d_</sup> is constant.

94

Exercise 3.8 ( _∗_ ). Let _D ⊂_ R<sup>_d_</sup> be a domain and _x ∈ D_ . Suppose _u_ : _D \ {x} →_ R is bounded and harmonic. Show that there exists a unique harmonic continuation _u_ : _D →_ R.


Conversely, if the integral diverges, then lim inf _t↓_ 0 _|B_ ( _t_ ) _|/f_ ( _t_ ) = 0 almost surely.

Exercise 3.10. Show that, if _d ≥_ 3 and _T_ is an independent exponential time with parameter _λ >_ 0, then


where _c_ ( _d_ ) is as in Theorem 3.32.

Exercise 3.11. Show that

- if _d ≥_ 2 and _T_ exponential time with parameter _λ >_ 0, then _G_ ( _· , y_ ) is subharmonic on R<sup>_d_</sup> _\ {y}_ ;

- if _d ≥_ 2 and _T_ the first exit time from the domain _D_ , then _G_ ( _· , y_ ) is harmonic on _D \ {y}_ .

Exercise 3.12 ( _∗_ ). Show that if _D_ is a bounded domain, than _G_ : _D × D \_ ∆is continuous, where ∆= _{_ ( _x, x_ ) : _x ∈ D}_ is the diagonal.

Exercise 3.13 ( _∗_ ). Find the Green’s function for the planar Brownian motion stopped when leaving the domain _B_ (0 _, r_ ).

Exercise 3.14 ( _∗_ ). Suppose _x, y̸ ∈ B_ (0 _, r_ ) and _A ⊂B_ (0 _, r_ ) is a compact, nonpolar set. Show that _µA_ ( _x, ·_ ) and _µA_ ( _y, ·_ ) are mutually absolutely continuous with a density bounded away from zero and infinity.

95

### **Notes and Comments**

Gauss discusses the Dirichlet problem in [ **Ga40** ] in a paper on electrostatics. Examples which show that a solution may not exist for certain domains were given by Zaremba [ **Za11** ] and Lebesgue [ **Le24** ]. Zaremba’s example is the punctured disk we discuss in Example 3.15, and Lebesgue’s example is the thorn, which we will discuss in Example 8.32. For domains with smooth boundary the problem was solved by Poincar´e [ **Po90** ].

Bachelier [ **Ba00, Ba01** ] was the first to note a connection of Brownian motion and the Laplace operator. The first probabilistic approaches to the Dirichlet problem were made by Phillips and Wiener [ **PW23** ] and Courant, Friedrichs and Lewy [ **CFL28** ]. These proofs used probability in a discrete setting and approximation. The treatment of the Dirichlet problem using Brownian motion and the probabilistic definition of the harmonic measure are due to the pioneering work of Kakutani [ **Ka44a, Ka44b, Ka45** ]. A current survey of probabilistic methods in analysis can be found in the book of Bass [ **Ba95** ], see also Port and Stone [ **PS78** ] for a classical reference.

P´olya [ **Po21** ] discovered that a simple symmetric random walk on Z<sup>_d_</sup> is recurrent for _d ≤_ 2 and transient otherwise. His result was later extended to Brownian motion by L´evy [ **Le40** ] and Kakutani [ **Ka44a** ]. Neighbourhood recurrence implies, in particular, that the path of a planar Brownian motion (running for an infinite amount of time) is dense in the plane. A more subtle question is whether in _d ≥_ 3 all orthogonal projections of a _d_ -dimensional Brownian motion are neighbourhood recurrent, or equivalently whether there is an infinite cylinder avoided by its range. In fact, an avoided cylinder does exist almost surely. This result is due to Adelman, Burdzy and Pemantle [ **ABP98** ]. The Dvoretzky-Erd˝os test is originally from [ **DE51** ] and more information and additional references can be found in [ **Pr90** ]. There is also an analogous result for planar Brownian motion (with shrinking balls) which is due to Spitzer [ **Sp58** ].

Green introduced the function named after him in [ **Gr28** ]. Its probabilistic interpretation appears in Kac’s paper [ **Ka51** ] and is investigated thoroughly by Hunt [ **Hu56** <u>].</u> Quite a lot can be said about the transition densities: p<sup>_∗_</sup> ( _t, · , ·_ ) is jointly continuous on _D × D_ and symmetric in the space variables. Moreover, p<sup>_∗_</sup> ( _t, x, y_ ) vanishes if either _x_ or _y_ is on the boundary of _D_ , if this boundary is sufficiently regular. This is, of course, only nontrivial in case (3) and full proofs for this case can be found in [ **Ba95** ] or [ **PS78** ].

96

### CHAPTER 4

---

[← Brownian motion as a strong Markov process](06-brownian-motion-as-a-strong-markov-process.md) · [Up: contents](index.md) · [Hausdorff dimension: Techniques and applications →](08-hausdorff-dimension-techniques-and-applications.md)
