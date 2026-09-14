---
title: Potential theory of Brownian motion
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Potential theory of Brownian motion

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this chapter we develop the key facts of the potential theory of Brownian motion. This theory is centred around the notions of a harmonic function, the energy of a measure, and the capacity of a set. The probabilistic problem at the heart of this chapter is to find the probability that Brownian motion visits a given set.

### **1. The Dirichlet problem revisited**

We now take up the study of the Dirichlet problem again and ask for sharp conditions on the domain which ensure the existence of solutions, which allow us to understand the problem for domains with very irregular boundaries, like for example connected components of the complement of a planar Brownian curve.

In this chapter, stochastic integrals and Itˆo’s formula will be a helpful tool. As a warm-up, we suggest to use these tools to give a probabilistic proof of the mean value property of harmonic functions, see Exercise 8.1.

Recall from Example 3.15 that the existence of a solution of the Dirichlet problem may be in doubt by the fact that Brownian motion started at the boundary _∂U_ may not leave the domain _U_ immediately. Indeed, we show here that this is the only problem that can arise.

Definition 8.1. _A point x ∈ A is called_ **regular** _for the closed set A ⊂_ R<sup>_d_</sup> _if the first hitting time TA_ = inf _{t >_ 0 : _B_ ( _t_ ) _∈ A} satisfies_ P _x{TA_ = 0� = 1 _. A point which is not regular is called_ **irregular** _. ⋄_

Remark 8.2. In the case _d_ = 1 we have already seen that for any starting point _x ∈_ R, almost surely a Brownian motion started in _x_ returns to _x_ in every interval [0 _, ε_ ) with _ε >_ 0. Hence every point is regular for any set containing it. _⋄_

We already know a condition which implies that a point is regular, namely the Poincar´e cone condition introduced in Chapter 3.

Theorem 8.3. _If the domain U ⊂_ R<sup>_d_</sup> _satisfies the Poincar´e cone condition at x ∈ ∂U , then x is regular for the complement of U ._

**Proof.** Suppose _x ∈ ∂U_ satisfies the condition, then there is an open cone _V_ with height _h >_ 0 and angle _α >_ 0 in _U_<sup>c</sup> based at _x_ . Then the first exit time _τU_ for the domain satisfies

P _x{τU ≤ t} ≥_ P _x{B_ ( _t_ ) _∈ V ∩B_ ( _x, h_ ) _} ≥_ P _x{B_ ( _t_ ) _∈ V } −_ P _x{B_ ( _t_ ) _̸ ∈B_ ( _x, h_ ) _},_

217

By Brownian scaling the last term equals P _{B_ (1) _∈ V }−_ P _x{B_ (1) _̸ ∈B_ ( _x, h/√t_ ) _}_ . For _t ↓_ 0 the subtracted term goes to zero, and hence P _x{τU_ = 0 _}_ = lim _t↓_ 0 P _x{τU ≤ t}_ = P _{B_ (1) _∈ V } >_ 0 _._ By Blumenthal’s zero-one law we have P _x{τU_ = 0 _}_ = 1, in other words _x_ is regular for _U_<sup>c</sup> .

Remark 8.4. At the end of this chapter we will be able to improve this and give a sharp condition for a point to be regular, _Wiener’s test_ of regularity. _⋄_

Theorem 8.5 (Dirichlet Problem). _Suppose U ⊂_ R<sup>_d_</sup> _is a bounded domain and ϕ be a continuous function on ∂U . Define τ_ = min _{t ≥_ 0: _B_ ( _t_ ) _∈ ∂U }, and define u_ : _U →_ R _by_


- (a) _A solution to the Dirichlet problem exists if and only if the function u is a solution to the Dirichlet problem with boundary condition ϕ._

- (b) _u is a harmonic function on U with u_ ( _x_ ) = _ϕ_ ( _x_ ) _for all x ∈ ∂U and is continuous at every point x ∈ ∂U that is regular for the complement of U ._

- (c) _If every x ∈ ∂U is regular for the complement of U , then u is the unique continuous function u_ : _U →_ R _which is harmonic on U such that u_ ( _x_ ) = _ϕ_ ( _x_ ) _for all x ∈ ∂U ._

**Proof.** For the proof of (a) let _v_ be any solution of the Dirichlet problem on _U_ with boundary condition _ϕ_ . Define open sets _Un ↑ U_ by _Un_ = � _x ∈ U_ : _| x − y| > n_<sup><u>1</u>forall</sup><sup>_y∈∂U_</sup> � _._ Let _τn_ be the first exit time of _Un_ and _τ_ the first exit time from _U_ , which are stopping times. As ∆ _v_ ( _x_ ) = 0 for all _x ∈ U_ we see from the multidimensional version of Itˆo’s formula that


Note that _∂v/∂xi_ is bounded on the closure of _Un_ , and thus everything is well-defined. The last term vanishes as ∆ _v_ ( _x_ ) = 0 for all _x ∈ U_ . Taking expectations the second term on the right also vanishes, by Exercise 7.1, and we get that


Note that _v_ , and hence the integrand on the left hand side, are bounded. Moreover, it is easy to check using boundedness of _U_ and a reduction to the one-dimensional case, that _τ_ is almost surely finite. Hence, as _t ↑∞_ and _n →∞_ , bounded convergence yields that the left hand side converges to E _x_ [ _v_ ( _B_ ( _τ_ ))] = E _x_ [ _ϕ_ ( _B_ ( _τ_ ))]. The result follows, as the right hand side depends neither on _t_ nor on _n_ .

The harmonicity statement of (b) is included in Theorem 3.8, and _u_ = _ϕ_ on _∂U_ is obvious from the definition. It remains to show the continuity claim. For a regular _x ∈ ∂U_ we now show that if Brownian motion is started at a point in _U_ , which is sufficiently close to _x_ , then with high probability the Brownian motion hits _U_<sup>c</sup> , before leaving a given ball _B_ ( _x, δ_ ).

We start by noting that, for every _t >_ 0 and _η >_ 0 the set


is open. Indeed, if _z ∈ O_ ( _t, η_ ), then for some small _s >_ 0 and _δ >_ 0 and large _M >_ 0, we have P _z_ � _|B_ ( _s_ ) _− z| ≤ M, B_ ( _u_ ) _∈ U_<sup>c</sup> for some _s ≤ u ≤ t_ � _> η_ + _δ._

218

By the Markov property the left hand side above can be written as


Now let _ε >_ 0 so small that _|_ p( _s, z, ξ_ ) _−_ p( _s, y, ξ_ ) _| < δ/L_ ( _B_ (0 _, M_ )) for all _|z − y| < ε_ and _ξ ∈_ R<sup>_d_</sup> . Then we have P _y{τ ≤ t_ � _≥_ P _y_ � _B_ ( _u_ ) _∈ U_<sup>c</sup> for some _s ≤ u ≤ t_ � _> η,_ hence the ball _B_ ( _z, ε_ ) is in _O_ ( _t, η_ ), which therefore must be open. Given _ε >_ 0 and _δ >_ 0 we now choose _t >_ 0 small enough, such that for _τ_<sup>_′_</sup> = inf _{s >_ 0: _B_ ( _s_ ) _̸ ∈ B_ ( _x, δ_ ) _}_ we have P _z_ � _τ_<sup>_′_</sup> _< t_ � _< ε/_ 2 for all _| x−z| < δ/_ 2. By regularity we have _x ∈ O_ ( _t,_ 1 _−ε/_ 2), and hence we can choose 0 _< θ < δ/_ 2 to achieve _B_ ( _x, θ_ ) _⊂ O_ ( _t,_ 1 _− ε/_ 2). We have thus shown that,


To complete the proof, let _ε >_ 0 be arbitrary. Then there is a _δ >_ 0 such that _|ϕ_ ( _x_ ) _− ϕ_ ( _y_ ) _| < ε_ for all _y ∈ ∂U_ with _| x − y| < δ_ . Choose _θ_ as in (1.1). For all _z ∈ U_ with _|z − x| < δ ∧ θ_ we get

_|u_ ( _x_ ) _− u_ ( _z_ ) _|_ = ��E _z_ [ _ϕ_ ( _x_ ) _− ϕ_ ( _B_ ( _τ_ ))]�� _≤_ 2 _∥ϕ∥∞_ P _z_ � _τ_<sup>_′_</sup> _< τ }_ + _ε ≤ ε_ (2 _∥ϕ∥∞_ + 1) _._

As _ε >_ 0 can be arbitrarily small, _u_ is continuous at _x ∈ ∂U_ , and part (c) follows trivially from (b) and the maximum principle.

A further classical problem of partial differential equations, the Poisson problem, is related to Brownian motion in a way quite similar to the Dirichlet problem.

Definition 8.6. _Let U ⊂_ R<sup>_d_</sup> _be a bounded domain and u_ : _U →_ R _be a continuous function, which is twice continuously differentiable on U . Let g_ : _U →_ R _be continuous. Then u is said to be the_ **solution of Poisson’s problem for** _g if u_ ( _x_ ) = 0 _for all x ∈ ∂U and_


Remark 8.7. The probabilistic approach to the Poisson problem will be discussed in Exercises 8.2 and 8.3. We show that, for _g_ bounded, the solution _u_ of Poisson’s problem for _g_ , if it exists, equals


where _T_ := inf _{t >_ 0 : _B_ ( _t_ ) _̸ ∈ U }_ . Conversely, if _g_ is H¨older continuous and every _x ∈ ∂U_ is _⋄_ regular for the complement of _U_ , then the function (1.2) solves the Poisson problem for _g_ .

Remark 8.8. If _u_ solves Poisson’s problem for _g ≡_ 1 in a domain _U ⊂_ R<sup>_d_</sup> , then _u_ ( _x_ ) = E _x_ [ _T_ ] is the average time it takes a Brownian motion started in _x_ to leave the set _U_ . _⋄_

219

### **2. The equilibrium measure**

In Chapter 3 we have studied the distribution of the location of the _first entry_ of a Brownian motion into a closed set Λ, the harmonic measure. In the case of a transient (or killed) Brownian motion there is a natural counterpart to this by looking at the distribution of the position of the _last exit_ from a closed set. This leads to the notion of the _equilibrium measure_ , which we discuss and apply in this section.

To motivate the next steps we first look at a simple random walk _{Xn_ : _n ∈_ N _}_ in _d ≥_ 3. Let _A ⊂_ Z<sup>_d_</sup> be a bounded set, then by transience the last exit time _γ_ = max _{n ∈_ N : _Xn ∈ A}_ is finite on the event that the random walk ever hits _A_ . Note that _γ_ is _not_ a stopping time. Then, for any _x ∈_ Z<sup>_d_</sup> and _y ∈ A_ ,


and introducing the Green’s function _G_ ( _x, y_ ) =<sup>�</sup><sup>_∞_</sup> _k_ =0<sup>P</sup><sup>_x_</sup> � _Xk_ = _y}_ we get, for all _y ∈ A_ , P _x_ � _X_ hits _A_ and _Xγ_ = _y_ � = _G_ ( _x, y_ ) P _y{γ_ = 0 _}._

This holds also, trivially, for all _y ∈_ Z<sup>_d_</sup> _\ A_ . Summing over all _y ∈_ Z<sup>_d_</sup> gives


The formula allows us to describe the probability of ever hitting a set as a potential with respect to the measure _y �→_ P _y{γ_ = 0 _}_ , which is supported on _A_ . Our aim in this section is to extend this to Brownian motion.

Note that the argument above relied heavily on the transience of the random walk. This is no different in the case of Brownian motion. In order to include the two-dimensional case we ‘kill’ the Brownian motion, either when it exits a large domain or at an independent exponential stopping time. Note that both possibilities preserve the strong Markov property, in the case of exponential killing this is due to the lack-of-memory property of the exponential distribution.

To formally explain our setup we now suppose that _{B_ ( _t_ ) : 0 _≤ t ≤ T }_ is a transient Brownian motion in the sense of Chapter 3. Recall that this means that _{B_ ( _t_ ) : 0 _≤ t ≤ T }_ is a _d_ -dimensional Brownian motion killed at time _T_ , and one of the following three cases holds:

- (1) _d ≥_ 3 and _T_ = _∞_ ,

- (2) _d ≥_ 2 and _T_ is an independent exponential time,

- (3) _d ≥_ 2 and _T_ is the first exit time from a bounded domain _D_ containing 0.

We use the convention that _D_ = R<sup>_d_</sup> in cases (1),(2). In all cases, transient Brownian motion is a Markov process and, by Proposition 3.29 its transition kernel has a density, which we denote by p<sup>_∗_</sup> ( _t, x, y_ ). Note that in case (2,3) the function p<sup>_∗_</sup> ( _t, x, y_ ) is only a subprobability density

220

because of the killing, indeed it is strictly smaller than the corresponding density without killing. The associated Green’s function


is always well-defined and finite for all _x̸_ = _y_ .

Theorem 8.9 (Last exit formula). _Suppose {B_ ( _t_ ) : 0 _≤ t ≤ T } is a transient Brownian motion and_ Λ _⊂_ R<sup>_d_</sup> _a compact set. Let γ_ = sup � _t ∈_ (0 _, T_ ] : _B_ ( _t_ ) _∈_ Λ� _be the_ last exit time _from_ Λ _, using the convention γ_ = 0 _if the path does not hit_ Λ _. Then there exists a finite measure ν on_ Λ _called the_ **equilibrium measure** _, such that, for any Borel set A ⊂_ Λ _and x ∈ D,_


Remark 8.10. Observe that the equilibrium measure is uniquely determined by the last exit formula above. The proof of Theorem 8.9 is similar to the simple calculation in the discrete _⋄_ case, the equilibrium measure is constructed as limit of the measure _ε_<sup>_−_1</sup> P _y{_ 0 _< γ ≤ ε} dy_ .

**Proof of Theorem 8.9.** Let _Uε_ be a uniform random variable on [0 _, ε_ ], independent of the Brownian motion and the killing time. Then, for any bounded and continuous _f_ : _D →_ R,


Using the notation _ψε_ ( _x_ ) = _ε_<sup>_−_1</sup> P _x{_ 0 _< γ ≤ ε}_ this equals


This means that the subprobability measure _ηε_ defined by


has the density _G_ ( _x, y_ ) _ψε_ ( _y_ ). Therefore also,

(2.1) _G_ ( _x, y_ )<sup>_−_1</sup> _dηε_ ( _y_ ) = _ψε_ ( _y_ ) _dy._

Observe now that, by continuity of the Brownian path, lim _ε↓_ 0 _ηε_ = _η_ 0 in the sense of weak convergence, where the measure _η_ 0 on Λ is defined by


for all Borel sets _A ⊂_ Λ. As, for fixed _x ∈ D_ , the function _y �→ G_ ( _x, y_ )<sup>_−_1</sup> is continuous and bounded on Λ, we infer that, in the sense of weak convergence

lim _ε↓_ 0<sup>_G_(</sup><sup>_x, y_)</sup><sup>_−_1</sup><sup>_dηε_=</sup><sup>_G_(</sup><sup>_x, y_)</sup><sup>_−_1</sup><sup>_dη_0</sup><sup>_._</sup>

221

By (2.1) the measure _ψε_ ( _y_ ) _dy_ therefore converges weakly to a limit measure _ν_ , which does not depend on _x_ , and satisfies _G_ ( _x, y_ )<sup>_−_1</sup> _dη_ 0( _y_ ) = _dν_ ( _y_ ) for all _x ∈ D._ As _η_ 0 has no atom in _x_ we therefore obtain that _dη_ 0( _y_ ) = _G_ ( _x, y_ ) _dν_ ( _y_ ) for all _x ∈ D._ Integrating over any Borel set _A_ gives the statement.

As a first application we give an estimate for the probability that Brownian motion in R<sup>_d_</sup> , for _d ≥_ 3, hits a set contained in an annulus around _x_ .

Corollary 8.11. _Suppose {B_ ( _t_ ) : _t ≥_ 0 _} is Brownian motion in_ R<sup>_d_</sup> _, with d ≥_ 3 _, and_ Λ _⊂B_ ( _x, R_ ) _\ B_ ( _x, r_ ) _is compact. Then_


_where ν is the equilibrium measure on_ Λ _._

**Proof.** By Theorem 8.9 in the case _A_ = Λ we have


Recall that _G_ ( _x, y_ ) = _| x − y|_<sup>2</sup><sup>_−d_</sup> and use that _R_<sup>2</sup><sup>_−d_</sup> _≤ G_ ( _x, y_ ) _≤ r_<sup>2</sup><sup>_−d_</sup> .

Theorem 8.5 makes us interested in statements claiming that the set of irregular points of a set _A_ is small. The following fundamental result will play an important role in the next chapter.

Theorem 8.12. _Suppose A ⊂_ R<sup>_d_</sup> _, d ≥_ 2 _is a closed set and let A_<sup>r</sup> _be the set of regular points for A. Then, for all x ∈_ R<sup>_d_</sup> _,_


_in other words, the set of irregular points is polar for Brownian motion._

For the proof of Theorem 8.12 we have to develop a tool of independent interest, the strong maximum principle. A special case of this is the following statement, from which Theorem 8.12 follows without too much effort.

Theorem 8.13. _Let {B_ ( _t_ ) : _t ≥_ 0 _} be a d-dimensional Brownian motion, and T an independent exponential time. Let_ Λ _⊂_ R<sup>_d_</sup> _be a compact set and define τ_ = inf _{t >_ 0 : _B_ ( _t_ ) _∈_ Λ _}. If for some ϑ <_ 1 _, we have_ P _x_ � _τ < T_ � _≤ ϑ for all x ∈_ Λ _, then_ P _x_ � _τ < T_ � _≤ ϑ for all x ∈_ R<sup>_d_</sup> _._

**Proof of Theorem 8.12.** We can write the set of irregular points of _A_ as a countable union of compact sets


where _T_ ( _n_ ) is an independent exponential time with mean 1 _/n_ and _τ_ ( _A_ ) is the first hitting time of _A_ . It suffices to prove that Brownian motion does not hit any fixed set in the union, so

222

let _ℓ, m, n_ be fixed and take _T_ = _T_ ( _n_ ), _ϑ_ = 1 _−_ 1 _/ℓ_ and a compact set


If _x ∈_ Λ, then, writing _τ_ for the first hitting time of Λ _⊂ A_ ,


for all _x ∈_ Λ and therefore by Theorem 8.13 for all _x ∈_ R<sup>_d_</sup> .

Now suppose _x ∈_ R<sup>_d_</sup> is the arbitrary starting point of a Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ and Λ( _ε_ ) = _{y ∈_ R<sup>_d_</sup> : _|y − z| ≤ ε_ for some _z ∈_ Λ _}_ . Define _τε_ as the first hitting time of Λ( _ε_ ). Clearly, as Λ is closed,


Moreover, by the strong Markov property applied at the stopping time _τε_ and the lack of memory property of exponential random variables,


and letting _ε ↓_ 0 we obtain


As _ϑ <_ 1 this implies P _x_ � _τ ≤ T_ � = 0, and as _T_ is independent of the Brownian motion and can take arbitrarily large values with positive probability, we infer that the Brownian motion started in _x_ never hits Λ.

The idea in the proof of Theorem 8.13 is to use the equilibrium measure _ν_ to express P _x_ � _τ < T_ � as a potential, which means that, denoting the parameter of the exponential by _λ >_ 0,


where _Gλ_ is the Green’s function for the Brownian motion stopped at time _T_ , i.e.


Recall that for any fixed _y_ the function _x �→ Gλ_ ( _x, y_ ) is subharmonic on R<sup>_d_</sup> _\ {y}_ , by Exercise 3.11, and this implies that


is subharmonic on Λ<sup>c</sup> . If _Uλν_ was also continuous on the closure of Λ<sup>c</sup> , then the maximum principle in Theorem 3.5 would tell us that _Uλν_ has its maxima on the boundary _∂_ Λ and this would prove Theorem 8.13. However we do not know the continuity of _Uλν_ on the closure of Λ<sup>c</sup> , so we need a strengthening of the maximum principle.

223

We now let _K_ be a **kernel** , i.e. a measurable function _K_ : R<sup>_d_</sup> _×_ R<sup>_d_</sup> _→_ [0 _, ∞_ ]. Suppose that _x �→ K_ ( _x, y_ ) is subharmonic outside _{y}_ , and that _K_ ( _x, y_ ) is a continuous and decreasing function of the distance _| x − y|_ . For any finite measure _µ_ on the compact set Λ, let


be the potential of _µ_ at _x_ with respect to the kernel _K_ .

Theorem 8.14 (Strong maximum principle). _Then, for any ϑ <_ 1 _, we have the equivalence_


Remark 8.15. Note that this completes the proof of Theorem 8.13 and hence of Theorem 8.12 by applying it to the special case of the kernel _K_ = _Gλ_ and the equilibrium measure. _⋄_

The proof we present relies on a beautiful geometric lemma.

Lemma 8.16. _There is a number N depending only on the dimension d such that the following holds: For every x ∈_ R<sup>_d_</sup> _and every closed set_ Λ _there are N nonoverlapping closed cones V_ 1 _, . . . , VN with vertex x such that, if ξi is a point of_ Λ _∩ Vi closest to x, then any point y ∈_ Λ _with y̸_ = _x is no further to some ξi than to x._


<!-- Start of picture text -->
Λ<br>ξ<br>π<br>3<br>y<br>x<br><!-- End of picture text -->

Figure 1. The geometric argument in Lemma 8.16.

**Proof.** The proof is elementary by looking at Figure 1: Let _N_ be the number of closed cones with circular base, vertex in the origin and opening angle _π/_ 3 needed to cover R<sup>_d_</sup> . Let _V_ be a shift of such a cone with vertex in _x_ , _ξ_ be a point in _V ∩_ Λ which is closest to _x_ , and _y ∈_ Λ be arbitrary. The triangle with vertices in _x_ , _ξ_ and _y_ has at most angle _π/_ 3 at the vertex _x_ , and hence by the geometry of triangles, the distance of _y_ and _ξ_ is no larger than the distance of _y_ and _x_ .

224

**Proof of Theorem 8.14.** Of course, only the implication _⇒_ needs proof. Take _µ_ satisfying _Uµ_ ( _x_ ) _≤ ϑ_ for all _x ∈_ Λ. Note that, by monotone convergence,


Hence, for a given _η >_ 0, by Egoroff’s theorem, there exists a compact subset _F ⊂_ Λ such that, _µ_ ( _F_ ) _> µ_ (Λ) _− η_ and the convergence in (2.2) is uniform on _F_ . If we define _µ_ 1 to be the restriction of _µ_ to _F_ , then we can find, for every _ε >_ 0 some _δ >_ 0 such that


Now let _{xn} ⊂_ R<sup>_d_</sup> be a sequence converging to _x_ 0 _∈ F_ . Then, as the kernel _K_ is bounded on sets bounded away from the diagonal,


We now want to compare _K_ ( _xn, y_ ) with _K_ ( _ξ, y_ ) for _ξ ∈ F_ . Here we use Lemma 8.16 for the point _x_ = _xn_ and obtain _ξ_ 1 _, . . . , ξN ∈ F_ such that


where we have used that _K_ depends only on the distance of the arguments and is decreasing in it. We thus have


As _ε >_ 0 was arbitrary we get


As the converse statement


holds trivially by Fatou’s lemma, we obtain the continuity of _Uµ_ 1 on _F_ . Continuity of _Uµ_ 1 on _F_<sup>c</sup> is obvious from the properties of the kernel, so that we have continuity of _Uµ_ 1 on all of R<sup>_d_</sup> . By the maximum principle, Theorem 3.5, we infer that _Uµ_ 1( _x_ ) _≤ ϑ_ .

To complete the proof let _x̸ ∈_ Λ be arbitrary, and denote its distance to Λ by _ϱ_ . Then _K_ ( _x, y_ ) _≤ C_ ( _ϱ_ ) for all _y ∈_ Λ. Therefore


and the result follows by letting _η ↓_ 0.

225

### **3. Polar sets and capacities**

One of our ideas to measure the size of sets in Chapter 4 was based on the notion of capacity of the set. While this notion appeared to be useful, but maybe a bit artifical at the time, we can now understand its true meaning. This is linked to the notion of polarity, namely whether a set has a positive probability of being hit by a suitably defined random set.

More precisely, we ask, which sets are polar for the range of a Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ . Recall that a Borel set _A ⊂_ R<sup>_d_</sup> is _polar_ for Brownian motion if, for all _x_ ,


In the case _d_ = 1 we already know that only the empty set is polar, whereas by Corollary 2.23 points are polar for Brownian motion in all dimensions _d ≥_ 2. The general characterisation of polar sets requires an extension of the notion of capacities to a bigger class of kernels.

Definition 8.17. _Suppose A ⊂_ R<sup>_d_</sup> _is a Borel set and K_ : R<sup>_d_</sup> _×_ R<sup>_d_</sup> _→_ [0 _, ∞_ ] _is a kernel. Then the K-energy of a measure µ is defined to be_


_and the K-capacity of A is defined as_


Remark 8.18. In most of our applications the kernels are of the form _K_ ( _x, y_ ) = _f_ ( _| x − y|_ ) for some decreasing function _f_ : [0 _, ∞_ ) _→_ [0 _, ∞_ ]. In this case we simply write _If_ instead of _IK_ and call this the _f_ -energy. We also write Cap _f_ instead of Cap _K_ and call this the _f_ -capacity. _⋄_

Theorem 8.19 (Kakutani’s theorem). _A closed set_ Λ _is polar for d-dimensional Brownian motion if and only if it has zero f -capacity for the_ **radial potential** _f defined by_


Remark 8.20. We call the kernel _K_ ( _x, y_ ) = _f_ ( _|x − y|_ ), where _f_ is the radial potential, the **potential kernel** . Up to constants, it agrees with the Green kernel in _d ≥_ 3. _⋄_

Instead of proving Kakutani’s theorem directly, we aim for a stronger result, which gives, for compact sets Λ _⊂_ R<sup>_d_</sup> , a quantitative estimate of


in terms of capacities. However, even if _d_ = 3 and _T_ = _∞_ , one cannot expect that


226

for the radial potential _f_ in Theorem 8.19. Observe, for example, that the left hand side depends strongly on the starting point of Brownian motion, whereas the right hand side is translation invariant. Similarly, if Brownian motion is starting at the origin, the left hand side is invariant under scaling, i.e. remains the same when Λ is replaced by _λ_ Λ for any _λ >_ 0, whereas the right hand side is not. For a direct comparison of hitting probabilities and capacities, it is therefore necessary to use a capacity function with respect to a scale-invariant modification of the Green kernel _G_ , called the _Martin kernel_ , which we now introduce.

We again look at all transient Brownian motions, recall the setup from Section 3.2. All we need is the following property, which is easy to verify directly from the form of the Green’s function _G_ in case (1). For the other two cases we give a conceptual proof.

Proposition 8.21. _For every compact set_ Λ _⊂ D ⊂_ R<sup>_d_</sup> _there exists a constant C depending only on_ Λ _such that, for all x, y ∈_ Λ _and sufficiently small ε >_ 0 _,_


**Proof.** Fix a compact set Λ _⊂ D_ and _ε >_ 0 smaller than one tenth of the distance of Λ and _D_<sup>c</sup> and let _x, y ∈_ Λ. We abbreviate


We first assume that _| x − y| >_ 4 _ε_ and show that in this case


from which our claim easily follows.

The function _G_ ( _· , y_ ) is harmonic on _D \{y}_ . Hence, with _τ_ = inf _{_ 0 _< t ≤ T_ : _B_ ( _t_ ) _̸ ∈B_ ( _x,_ 2 _ε_ ) _}_ we note that, for all _x_ � _∈B_ ( _x, ε_ ),


This is the average of _G_ ( _· , y_ ) with respect to the harmonic measure _µ∂B_ ( _x,_ 2 _ε_ )( _x,_ � _·_ ). This measure has a density with respect to the uniform measure on the sphere _∂B_ ( _x,_ 2 _ε_ ), which is bounded from zero and infinity by absolute constants. In the cases (1),(3) this can be seen directly from Poisson’s formula. Therefore _G_ ( _x, y_ � ) _≤ CG_ ( _x, y_ ) and repetition of this argument, introducing now _y_ � _∈B_ ( _y, ε_ ) and fixing _x_ � gives the claim.

Now look at the case _| x − y| ≤_ 4 _ε_ . We first observe that, for some constant _c >_ 0, _G_ ( _x, y_ ) _≥ cε_<sup>2</sup><sup>_−d_</sup> , which is obvious in all cases. Now let _z ∈B_ ( _x, ε_ ). Decomposing the Brownian path on its first exit time _τ_ from _B_ ( _x,_ 8 _ε_ ) and denoting the uniform distribution on _∂B_ ( _x,_ 8 _ε_ ) by _ϖ_ we obtain for constants _C_ 1 _, C_ 2 _>_ 0,


227

where we have used (3.2). A similar decomposition gives that � _G_ ( _w, y_ ) _dϖ_ ( _w_ ) _≤ C_ 3 _G_ ( _x, y_ ) and putting all facts together gives _hε_ ( _z, y_ ) _≤ C_ 4 _ε_<sup>_d_</sup> _G_ ( _x, y_ ), as required.

Definition 8.22. _We define the Martin kernel M_ : _D × D →_ [0 _, ∞_ ] _by_


_and otherwise by M_ ( _x, x_ ) = _∞._


The following theorem shows that (in all three cases of transient Brownian motions) Martin capacity is indeed a good estimate of the hitting probability.

Theorem 8.23. _Let {B_ ( _t_ ) : 0 _≤ t ≤ T } be a transient Brownian motion and A ⊂ D closed. Then_


**Proof.** Let _µ_ be the (possibly defective) distribution of _B_ ( _τ_ ) for the stopping time _τ_ = inf _{_ 0 _< t ≤ T_ : _B_ ( _t_ ) _∈ A}_ . Note that the total mass of _µ_ is

(3.4) _µ_ ( _A_ ) = P0 _{τ ≤ T }_ = P0 _{B_ ( _t_ ) _∈ A_ for some 0 _< t ≤ T }._

The idea for the upper bound is that if the harmonic measure _µ_ is nontrivial, it is an obvious candidate for a measure of finite _M_ -energy. Recall from the definition of the Green’s function, for any _y ∈ D_ ,


By the strong Markov property applied to the first hitting time _τ_ of _A_ ,


Integrating over _t_ and using Fubini’s theorem yields


Combining this with (3.5) we infer that


Dividing by _L_ ( _B_ (0 _, ε_ )) and letting _ε ↓_ 0 we obtain


228

i.e. � _A_<sup>_M_(</sup><sup>_x, y_)</sup><sup>_dµ_(</sup><sup>_x_)</sup><sup>_≤_1forall</sup><sup>_y∈D_.Therefore,</sup><sup>_IM_(</sup><sup>_µ_)</sup><sup>_≤µ_(</sup><sup>_A_)andthusifweuse</sup><sup>_µ/µ_(</sup><sup>_A_)as</sup> a probability measure we get


which by (3.4) yields the upper bound on the probability of hitting _A_ .

To obtain a lower bound for this probability, a second moment estimate is used. It is easily seen that the Martin capacity of _A_ is the supremum of the capacities of its compact subsets, so we may assume that _A_ is a compact subset of the domain _D \ {_ 0 _}_ . We take _ε >_ 0 smaller than half the distance of _A_ to _D_<sup>c</sup> _∪{_ 0 _}_ . For _x, y ∈ A_ let


denote the expected time which a Brownian motion started in _x_ spends in the ball _B_ ( _y, ε_ ). Also define


Given a probability measure _ν_ on _A_ , and _ε >_ 0, consider the random variable


Clearly E0 _Zε_ = 1. By symmetry, the second moment of _Zε_ can be written as


Observe that, for all fixed _x, y ∈ A_ we have lim _ε↓_ 0 _L_ ( _B_ (0 _, ε_ ))<sup>_−_1</sup> _hε_<sup>_∗_(</sup><sup>_x, y_)=</sup><sup>_G_(</sup><sup>_x, y_)and</sup> lim _ε↓_ 0 _L_ ( _B_ (0 _, ε_ ))<sup>_−_1</sup> _hε_ (0 _, y_ ) = _G_ (0 _, y_ ). Moreover, by (3.1) and the fact that _G_ (0 _, y_ ) is bounded from zero and infinity for all _y ∈ A_ , for some constant _C_ ,


Hence, if _ν_ is a measure of finite energy, we can use dominated convergence and obtain,


Clearly, the hitting probability P _{∃t >_ 0 _, y ∈ A_ such that _B_ ( _t_ ) _∈B_ ( _y, ε_ ) _}_ is at least


229

where we have used the Paley-Zygmund inequality in the second step. Compactness of _A_ , together with transience and continuity of Brownian motion, imply that if the Brownian path visits every _ε_ -neighbourhood of the compact set _A_ then it intersects _A_ itself. Therefore, by (3.7),


Since this is true for all probability measures _ν_ on _A_ , we get the desired conclusion.

Remark 8.24. The right-hand inequality in (3.3) can be an equality: look at the case _d_ = 3, _T_ = _∞_ , our case (1), and take a sphere in R<sup>_d_</sup> centred at the origin, which has hitting probability and capacity both equal to one. Exercise 8.5 shows that the constant 1/2 on the left cannot be increased. _⋄_

**Proof of Theorem 8.19.** It suffices, by taking countable unions, to consider compact sets Λ which have positive distance from the origin.

First consider the case _d_ = 3. Then _G_ (0 _, x_ ) is bounded away from zero and infinity. Hence the set Λ is polar if and only if its _f_ -capacity vanishes, where _f_ ( _ε_ ) = _ε_<sup>_d−_2</sup> .

In the case _d_ = 2 we choose a ball _B_ (0 _, R_ ) containing Λ. By Exercise 3.13 the Green’s function for Brownian motion stopped upon leaving _B_ (0 _, R_ ) is given as


Again _G_<sup>(</sup><sup>_R_)</sup> (0 _, y_ ) is bounded over all _y ∈_ Λ, and so is the second summand of _G_<sup>(</sup><sup>_R_)</sup> ( _x, y_ ). Hence only the contribution from _−_ log _| x − y|_ decides about finiteness of the energy of a probability measure. Therefore, any measure with finite Martin energy has finite _f_ -energy for _f_ ( _ε_ ) = _−_ log(1 _/ε_ ), and vice versa. This completes the proof.

The estimates in Theorem 8.23 are valid beyond the Brownian motion case. The following proposition, which has a very similar proof to Theorem 8.23, shows that one has an analogous result in a discrete setup. We will see a surprising application of this in Chapter 9.

Proposition 8.25. _Let {Xn_ : _n ∈_ N _} be a transient Markov chain on a countable state space S, and set_


_Then for any initial state ρ and any subset_ Λ _of S,_


**Proof.** To prove the right-hand inequality, we may assume that the hitting probability is positive. Let _τ_ = inf _{n_ : _Xn ∈_ Λ _}_ and let _ν_ be the measure _ν_ ( _A_ ) = P _ρ{τ < ∞_ and _Xτ ∈ A}_ .

230

In general, _ν_ is a sub-probability measure, as _τ_ may be infinite. By the Markov property, for _y ∈_ Λ,


whence �Λ<sup>_M_(</sup><sup>_x, y_)</sup><sup>_dν_(</sup><sup>_x_)=1</sup><sup>_._Therefore</sup><sup>_IM_(</sup><sup>_ν_)=</sup><sup>_ν_(Λ),</sup><sup>_IM_</sup> � _ν/ν_ (Λ)� = [ _ν_ (Λ)]<sup>_−_1</sup> ; consequently, since _ν/ν_ (Λ) is a probability measure, Cap _M_ (Λ) _≥ ν_ (Λ) = P _ρ_ � _{Xn}_ hits Λ� _._

This yields one inequality. Note that the Markov property was used here.

For the reverse inequality, we use the second moment method. Given a probability measure _µ_ on Λ, set


E _ρ_ [ _Z_ ] = 1, and the second moment satisfies


Observe that


Recall from Corollary 8.11 that we have already seen estimates for the probability that Brownian motion hits a set, which were given in terms of the total mass of the equilibrium measure. The following theorem reveals the relationship between the equilibrium measure and capacities.

Theorem 8.26. _Let_ Λ _⊂_ R<sup>_d_</sup> _be a nonpolar, compact set and G_ : R<sup>_d_</sup> _×_ R<sup>_d_</sup> _→_ [0 _, ∞_ ] _the Green’s function of a transient Brownian motion. Then_


_where ν is the equilibrium measure of_ Λ _._

231

Remark 8.27. If Λ is polar, we have Cap _G_ (Λ) = 0 = _ν_ (Λ). Otherwise, this shows that the probability measure _ν/ν_ (Λ) minimizes the _G_ -energy over the set of all probability measures on Λ.

For the proof we first note that, for the Green’s function _G_ of a transient Brownian motion, the _G_ -energy of a _signed_ measure is always nonnegative.

Lemma 8.28. _Let µ, ν finite measures on_ R<sup>_d_</sup> _and G the Green’s function G of a transient Brownian motion. Then, for σ_ = _µ − ν, we have_


**Proof.** From the Chapman-Kolmogorov equation we have


Integrating with respect to _dσ_ ( _x_ ) _dσ_ ( _y_ ) and using the symmetry of p<sup>_∗_</sup> ( _t, · , ·_ ) gives


Integrating now over time gives the result.

**Proof of Theorem 8.26.** Let _ν_ be the equilibrium measure and define _ϕ_ ( _x_ ) = � _G_ ( _x, y_ ) _dν_ ( _y_ ) _._ By the last exit formula, Theorem 8.9, _ϕ_ ( _x_ ) is the probability that a Brownian motion started at _x_ hits Λ before time _T_ . Hence _ϕ_ ( _x_ ) _≤_ 1 for every _x_ and, if _x_ is a regular point for Λ, then _ϕ_ ( _x_ ) = 1. Also by the last exit formula, because irregular points are never hit by a Brownian motion, see Theorem 8.12, we have _ϕ_ ( _x_ ) = 1 for _ν_ -almost every point. This implies that


Suppose now that _µ_ is an arbitrary measure on Λ with _µ_ (Λ) = _ν_ (Λ) and assume that _µ_ has finite energy. Note that _µ_ does not charge the set of irregular points, as otherwise this set would have positive capacity and would be nonpolar by Theorem 8.23. Then, starting with Lemma 8.28 and using also the symmetry of _G_ ,


using in the last step that _ϕ_ ( _y_ ) = 1 on the set of regular points, and thus _µ_ -almost everywhere. This implies that _IG_ ( _µ_ ) _≥ ν_ (Λ) = _IG_ ( _ν_ ), so that _ν/ν_ (Λ) is a minimiser in the definition of Cap _G_ . This completes the proof.

232

### **4. Wiener’s test of regularity**

In this section we concentrate on _d ≥_ 3 and find a sharp criterion for a point to be regular for a closed set Λ _⊂_ R<sup>_d_</sup> . This criterion is given in terms of the capacity of the intersection of Λ with annuli, or shells, concentric about _x_ .

To fix some notation let _k > ℓ_ be integers and _x ∈_ R<sup>_d_</sup> , and define the annulus


Abbreviate _Ax_ ( _k_ ) := _Ax_ ( _k_ + 1 _, k_ ) and let


We aim to prove the following result.

Theorem 8.29 (Wiener’s test). _A point x ∈_ R<sup>_d_</sup> _is regular for the closed set_ Λ _⊂_ R<sup>_d_</sup> _, d ≥_ 3 _, if and only if_


_where Cd−_ 2 _is the Riesz_ ( _d −_ 2) _-capacity introduced in Definition 4.3._

In the proof, we may assume, without loss of generality, that _x_ = 0. We start the proof with an easy observation.

Lemma 8.30. _There exists a constant c >_ 0 _, which depends only on the dimension d, such that, for all k, we have_


**Proof.** Observe that, as _z ∈ A_<sup>_k_</sup> 0<sup>implies2</sup><sup>_−k−_1</sup><sup>_≤|z|≤_2</sup><sup>_−k_,weobtainthestatementby</sup> estimating the denominator in the Martin kernel _M_ .

The crucial step in the proof is a quantitative estimate, from which Wiener’s test follows quickly. Lemma 8.31. _There exists a constant c >_ 0 _, depending only on the dimension d, such that_


**Proof.** For the _upper_ bound we look at the event _D_ ( _j_ ) that a Brownian motion started in 0 hits Λ<sup>_j_</sup> 0<sup>.Then,usingTheorem8.23,wegetP0</sup> � _D_ ( _j_ )� _≤_ Cap _M_ �Λ<sup>_j_</sup> 0� _._ Therefore


and this completes the proof of the upper bound.

For the _lower_ bound we look at the event _E_ ( _z, j_ ) that a Brownian motion started in some point _z ∈ ∂B_ (0 _,_ 2<sup>_−j_</sup> ) and stopped upon hitting _∂B_ (0 _,_ 2<sup>_−j_+4</sup> ) hits Λ<sup>_j_</sup> 0<sup>_−_2</sup> . Again we use either

233

Theorem 8.23, or Corollary 8.11 in conjunction with Theorem 8.26, to get, for constants _c_ 1 _, c_ 2 _>_ 0 depending only on the dimension _d_ ,


and, for any _y ∈ ∂B_ (0 _,_ 2<sup>_−j_+4</sup> ),

Therefore, for a constant _c >_ 0 depending only on the dimension _d_ ,

Now divide _{ℓ, . . . , k −_ 1 _}_ into four subsets such that each subset _I_ satisfies _|i − j| ≥_ 4 for all _i̸_ = _j ∈ I_ . Choose a subset _I_ which satisfies


Now we have with _τj_ = inf _{t ≥_ 0 : _|B_ ( _t_ ) _|_ = 2<sup>_−j_</sup> _}_ ,


using the estimate log(1 _− x_ ) _≤−x_ in the last step. The lower bound, with _c_ = _C/_ 4, now follows from (4.1) and Lemma 8.30 when we pass to the complement.

**Proof of Wiener’s test.** Suppose<sup>�</sup><sup>_∞_</sup> _k_ =1<sup>2</sup><sup>_k_(</sup><sup>_d−_2)</sup><sup>_Cd−_2</sup> �Λ<sup>_k_</sup> 0� = _∞._ Therefore, by Lemma 8.31 and Lemma 8.30, for all _k ∈_ N,


Since points are polar, for any _ε, δ >_ 0 there exists a large _k_ such that


Combining these two facts we get for the first hitting time _τ_ = _τ_ (Λ) of the set Λ,


As _ε, δ >_ 0 were arbitrary, the point 0 must be regular.

234


Hence, by the Borel Cantelli lemma, almost surely there exists a ball _B_ (0 _, ε_ ) such that _{B_ ( _t_ ) : _t ≥_ 0 _}_ does not hit _B_ (0 _, ε_ ) _∩_ Λ. By continuity we therefore must have inf _{t >_ 0: _B_ ( _t_ ) _∈_ Λ _} >_ 0 almost surely, hence the point 0 is irregular.


<!-- Start of picture text -->
x2, x3<br>1<br>G<br>-1 0 1 x1<br>-1 Λ<br><!-- End of picture text -->

Figure 2. Lebesgue’s thorn.

Example 8.32. The following example is due to Lebesgue [ **Le24** ], and is usually called **Lebesgue’s thorn** . For any _α >_ 1 we define an open subset _G ⊂_ ( _−_ 1 _,_ 1)<sup>3</sup> with a _cusp_ at zero by


with _f_ ( _x_ ) = _x_<sup>_α_</sup> , see Figure 2. Now the origin is an _irregular_ point for Λ = _G_<sup>c</sup> . For the proof it suffices, by Wiener’s test, to check that the series<sup>�</sup><sup>_∞_</sup> _k_ =1<sup>2</sup><sup>_kC_1</sup> �Λ<sup>_k_</sup> 0� converges. Note that, for any probability measure _µ_ on Λ<sup>_k_</sup> 0<sup>,wehave</sup><sup>_I_1(</sup><sup>_µ_)</sup><sup>_≥_2</sup><sup>_αk_and,hence,</sup>


verifying Wiener’s test of irregularity.


235

### **Exercises**

Exercise 8.1 ( _∗_ ). Let _U ⊂_ R<sup>_d_</sup> be a domain and _u_ : _U →_ R subharmonic. Use Itˆo’s formula to show that, for any ball _B_ ( _x, r_ ) _⊂ U_ ,


Exercise 8.2 ( _∗_ ). Suppose _g_ is bounded and _u_ a solution of Poisson’s problem for _g_ . Show that this solution has the form


where _T_ := inf _{t >_ 0 : _B_ ( _t_ ) _̸ ∈ U }_ . Observe that his implies that the solution, if it exists, is always uniquely determined.

Exercise 8.3. Let


where _T_ := inf _{t >_ 0 : _B_ ( _t_ ) _̸ ∈ U }_ . Show that,


- if every _x ∈ ∂U_ is regular for the complement of _U_ , then _u_ ( _x_ ) = 0 for all _x ∈ ∂U_ .

Exercise 8.4. Suppose Λ _⊂_ R<sup>_d_</sup> , for _d ≥_ 3, is compact and _γ_ the last exit time from Λ defined as in Theorem 8.9. Show that


Exercise 8.5. For _d ≥_ 3 consider the spherical shell


Show that lim _R→∞_ Cap _M_ (Λ _R_ ) = 2 _._

236


Let _M_ ( _s, t_ ) = _K_ ( _s, t_ ) _/K_ (0 _, t_ ), then for any subset Λ of [0 _, ∞_ ),


237

### **Notes and Comments**

The proof of the last exit formula is taken from Chung’s beautiful paper [ **Ch73** ], but the existence of an energy minimizing measure is a much older fact. For the case of the Newtonian potential ( _d_ = 3) it was determined by Gauss as the charge distribution on the surface of a conductor which minimises the electrostatic energy. Classically, the equilibrium measure is defined as the measure _ν_ on Λ that maximizes _ν_ (Λ) among those with potential bounded by one. Then _ν/ν_ (Λ) is the energy minimizing probability measure, see [ **Ca67** ]. Rigorous results and extensions to general Riesz-potentials are due to Frostman in his ground-breaking thesis [ **Fr35** ]. Our discussion of the strong maximum principle follows Carleson [ **Ca67** ]. Bass [ **Ba95** ] describes an alternative approach.

Characterising the polar sets for Brownian motion is related to the following question: for which sets _A ⊂_ R<sup>_d_</sup> are there nontrivial bounded harmonic functions on R<sup>_d_</sup> _\ A_ ? Such sets are called _removable_ for bounded harmonic functions. Consider the simplest case first. When _A_ is the empty set, it is obviously polar, and by Liouville’s theorem there is no bounded harmonic function on its complement. Nevanlinna (about 1920) proved that for _d ≥_ 3 there exist non-constant bounded harmonic functions on R<sup>_d_</sup> _\ A_ if and only if Cap _G_ ( _A_ ) _>_ 0, where _G_ ( _x, y_ ) = _f_ ( _|x−y|_ ) for the radial potential _f_ as before. Just to make this result more plausible, note that the function _h_ ( _x_ ) = � _G_ ( _x, y_ ) _µ_ ( _dy_ ), where _µ_ is a measure on _A_ of finite _G_ -energy, would make a good candidate for such a function, see Theorem 3.34.

Loosely speaking, _G_ -capacity measures whether a set _A_ is big enough to hide a pole of a harmonic function inside. Recall from Theorem 4.36 that dim _A > d −_ 2 implies existence of such functions, and dim _A < d −_ 2 implies nonexistence. Kakutani (1944) showed that there exist bounded harmonic functions on R<sup>_d_</sup> _\ A_ if and only if _A_ is polar for Brownian motion. Kakutani’s theorem is proved in [ **Ka44a** ]. The precise hitting estimates we give are fairly recent, our proof is a variant of the original proof by Benjamini, Pemantle and Peres in [ **BPP95** ]. Proposition 8.25 goes back to the same paper.

An interesting question is which subsets of a compact sets are charged by the harmonic measure _µA_ . Clearly _µA_ does not charge polar sets, and in particular, in _d ≥_ 3, we have _µA_ ( _B_ ) = 0 for all Borel sets with dim( _B_ ) _< d −_ 2. In the plane, by a famous theorem of Makarov, see [ **Ma85** ], we have that

- any set _B_ of dimension _<_ 1 has _µA_ ( _B_ ) = 0,

- there is a set _S ⊂ A_ with dim _S_ = 1 such that _µA_ ( _S_<sup>c</sup> ) = 0.

However, the outer boundary, which supports the harmonic measure, may have a dimension much bigger than one. An interesting question arising in the context of self-avoiding curves asks for the dimension of the outer boundary of the image _B_ [0 _,_ 1] of a Brownian motion. Based on scaling arguments from polymer physics, Benoit Mandelbrot conjectured in 1982 that this set should have fractal dimension 4 _/_ 3. Bishop, Jones, Pemantle, and Peres [ **BJPP97** ] showed that that the outer boundary has dimension _>_ 1. In 2001 Mandelbrot’s conjecture was finally proved by Lawler, Schramm and Werner [ **LSW01** ].

238

### CHAPTER 9

---

[← Stochastic integrals and applications](11-stochastic-integrals-and-applications.md) · [Up: contents](index.md) · [Intersections and self-intersections of Brownian paths →](13-intersections-and-self-intersections-of-brownian-paths.md)
