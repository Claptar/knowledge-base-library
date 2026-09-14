---
title: 'Appendix II: Background and prerequisites'
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Appendix II: Background and prerequisites

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **1. Convergence of distributions on metric spaces**

In this section we collect the basic facts about convergence in distribution. While this is a familiar concept for real valued random variables, for example in the central limit theorem, we need a more abstract viewpoint, which allows to study convergence in distribution for random variables with values in metric spaces, like for example function spaces.

If random variables _{Xn_ : _n ≥_ 0 _}_ converge in distribution, strictly speaking it is their _distributions_ and not the _random variables_ themselves which converge. This distinguishes convergence in distribution from the types of convergence for random variables, like

- almost sure convergence,

- convergence in probability,

- _L_<sup>1</sup> -convergence (and _L_<sup>_p_</sup> -convergence).

These types of convergence refer to a sequences of random variables _{Xn_ : _n ≥_ 0 _}_ converging to a random variable _X_ on the _same_ probability space. The values of the approximating sequences lead to conclusions about the values of the limit random variable. This is entirely different for _convergence in distribution_ , which we now study. Intuitively if _{Xn_ : _n ≥_ 0 _}_ converges in distribution to _X_ , this just means that the shape of the distributions of _Xn_ for large _n_ is like the shape of the distribution of _X_ . Sample values from _Xn_ allow no inference towards sample values from _X_ and, indeed, there is no need to define _Xn_ and _X_ on the same probability space. In fact, convergence in distribution is only related to the convergence of the distributions of the random variables and not to the random variables themselves.

We start by giving a definition of convergence in distributions for random variables in metric spaces, explore some of its properties and then show that the concept of convergence in distribution for real-valued random variables is consistent with our definition.

Definition 1.1. _Suppose_ ( _E, ρ_ ) _is a metric space and A the Borel-σ-algebra on E. Suppose that Xn and X are E-valued random variables. Then we say that Xn_ converges in distribution _to X, if, for every bounded continuous g_ : _E →_ R _,_


_We write Xn ⇒ X for convergence in distribution. ⋄_

Remark 1.2. If _Xn ⇒ X_ and _g_ : _E →_ R is continuous, then _g_ ( _Xn_ ) _⇒ g_ ( _X_ ). But note that, if _E_ = R and _Xn ⇒ X_ , this does not imply that E[ _Xn_ ] converges to E[ _X_ ], as _g_ ( _x_ ) = _x_ is not a bounded function on R. _⋄_

331

Here is an alternative approach, which shows that convergence in distribution is in fact a convergence _of_ the distributions. The statement of the following proposition is trivial.

Proposition 1.3. _Let Prob_ ( _E_ ) _be the set of probability measures on_ ( _E, A_ ) _. A sequence {Pn_ : _n ≥_ 0 _} ⊂ Prob_ ( _E_ ) _converges weakly to a limit P ∈ Prob_ ( _E_ ) _if, for every continuous, bounded function g_ : _E →_ R _,_


_Then the limit of a convergent sequence is uniquely determined. Suppose that Xn and X are E- valued random variables. Then Xn converges in distribution to X, if and only if the distributions of Xn converge weakly to the distribution of X._

**Proof.** Only the uniqueness of the limit needs proof. If _P_ and _Q_ are two limits of the same sequence, then � _f dP_ = � _f dQ_ for all bounded continuous _f_ : _E →_ R. For every open set _G ⊂ E_ we may choose an increasing sequence _fn_ ( _x_ ) = _nρ_ ( _x, G_<sup>_c_</sup> ) _∧_ 1 of continuous functions converging to 1 _G_ and infer from monotone convergence that _P_ ( _G_ ) = _Q_ ( _G_ ). Now _P_ = _Q_ follows from the Uniqueness theorem for probability measures.

Example 1.4.

- Suppose _E_ = _{_ 1 _, . . . , m}_ is finite and _ρ_ ( _x, y_ ) = 1 _−_ 1 _{x_ = _y}_ . Then _Xn ⇒ X_ if and only if lim _n→∞_ P _{Xn_ = _k}_ = P _{X_ = _k}_ for all _k ∈ E_ .

- Let _E_ = [0 _,_ 1] and _Xn_ = 1 _/n_ almost surely. Then _Xn ⇒ X_ , where _X_ = 0 almost surely. However, note that lim _n→∞_ P _{Xn_ = 0 _}_ = 0 _̸_ = P _{X_ = 0 _}_ = 1.


Theorem 1.5. _Suppose a sequence {Xn_ : _n ≥_ 0 _} of random variables converges almost surely to a random variable X (of course, all on the same probability space). Then Xn converges in distribution to X._

**Proof.** Suppose _g_ is bounded and continuous. The _g_ ( _Xn_ ) converges almost surely to _g_ ( _X_ ). As the sequence is bounded it is also uniformly integrable, hence convergence holds also in the _L_<sup>1</sup> -sense and this implies convergence of the expectations, i.e. E[ _g_ ( _Xn_ )] _→_ E[ _g_ ( _X_ )].

Theorem 1.6 (Portmanteau theorem). _The following statements are equivalent_

- (i) _Xn ⇒ X._

- (ii) _For all closed sets K ⊂ E,_ lim sup _n→∞_ P _{Xn ∈ K} ≤_ P _{X ∈ K}._

- (iii) _For all open sets G ⊂ E,_ lim inf _n→∞_ P _{Xn ∈ G} ≥_ P _{X ∈ G}._

- (iv) _For all Borel sets A ⊂ E with_ P _{X ∈ ∂A}_ = 0 _,_ lim _n→∞_ P _{Xn ∈ A}_ = P _{X ∈ A}._

- (v) _For all bounded measurable functions g_ : _E →_ R _with_ P _{g is discontinuous at X}_ = 0 _we have_ E[ _g_ ( _Xn_ )] _→_ E[ _g_ ( _X_ )] _._

332

**Proof. (i)** _⇒_ **(ii)** Let _gn_ ( _x_ ) = 1 _−_ ( _nρ_ ( _x, K_ ) _∧_ 1), which is continuous and bounded, is 1 on _K_ and converges pointwise to 1 _K_ . Then, for every _n_ ,


Let _n →∞_ . The integrand on the right hand side is bounded by 1 and converges pointwise and hence in the _L_<sup>1</sup> -sense to 1 _K_ ( _X_ ).

**(ii)** _⇒_ **(iii)** Follows from 1 _G_ = 1 _−_ 1 _K_ for the closed set _K_ = _G_<sup>_c_</sup> .

**(iii)** _⇒_ **(iv)** Let _G_ be the interior and _K_ the closure of _A_ . Then, by assumption, P _{X ∈ G}_ = P _{X ∈ K}_ = P _{X ∈ A}_ and we may use (iii) and (ii) (which follows immediately from (iii)) to get


**(iv)** _⇒_ **(v)** From (iv) we infer that the convergence holds for _g_ of the form _g_ ( _x_ ) =<sup>�</sup><sup>_N_</sup> _n_ =1<sup>_an_1</sup><sup>_An_</sup> where _An_ satisfies P _{X ∈ An}_ = 0. Let us call such functions elementary. Given _g_ as in (v) we observe that for every _a < b_ with possibly a countable set of exceptions


Indeed, if _X ∈ ∂{x_ : _g_ ( _x_ ) _∈_ ( _a, b_ ] _}_ then either _g_ is discontinuous in _X_ or _g_ ( _X_ ) = _a_ or _g_ ( _X_ ) = _b_ . The first event has probability zero and so have the last two except possibly for a countable set of values of _a, b_ . By decomposing the real axis in small suitable intervals we thus obtain an increasing sequence _gn_ and a decreasing sequence _hn_ of elementary functions both converging pointwise to _g_ . Now, for all _k_ ,


and the right sides converge, as _k →∞_ , by bounded convergence, to E[ _g_ ( _X_ )]. **(v)** _⇒_ **(i)** This is trivial.

To remember the directions of the inequalities in the Portmanteau theorem it is useful to recall the last example _Xn_ = 1 _/n →_ 0 and choose _G_ = (0 _,_ 1) and _K_ = _{_ 0 _}_ to obtain cases where the opposite inequalities fail.

We now show that the convergence of distribution as defined here agrees with the familiar concept in the case of real random variables.

Theorem 1.7 (Helly-Bray theorem). _Let Xn and X be real valued random variables and define the associated distribution functions Fn_ ( _x_ ) = P _{Xn ≤ x} and F_ ( _x_ ) = P _{X ≤ x}. Then the following assertions are equivalent._

- (a) _Xn converges in distribution to X,_ (b) _n_ lim _→∞_<sup>_Fn_(</sup><sup>_x_) =</sup><sup>_F_(</sup><sup>_x_)</sup><sup>_forallxsuchthatFiscontinuousinx._</sup>

333

**Proof.** (a) _⇒_ (b) Use property (iv) for the set _A_ = ( _−∞, x_ ].

(b) _⇒_ (a) We choose a dense sequence _{xn}_ with P _{X_ = _xn}_ = 0 and note that every open set _G ⊂_ R can be written as the countable union of disjoint intervals _Ik_ = ( _ak, bk_ ] with _ak, bk_ chosen from the sequence. We have


Hence, for all _N_ ,


and as _N →∞_ the last term converges to P _{X ∈ G}_ .

Finally, we note the useful fact that for nonnegative random variables _Xn_ , rather then testing convergence of E[ _f_ ( _Xn_ )] for _all_ continuous bounded functions _f_ , it suffices to consider functions of a rather simple form.


_if an only if, for any λ_ 1 _, . . . , λm ≥_ 0 _,_


The function _φ_ ( _λ_ 1 _, . . . , λm_ ) = E[exp _{−_<sup>�</sup><sup>_m_</sup> _j_ =1<sup>_λjXj}_]iscalledtheLaplacetransformof</sup> ( _X_ 1 _, . . . , Xm_ ) and thus the proposition states in other words that the convergence of nonnegative random vectors is equivalent to convergence of their Laplace transforms. The proof, usually done by approximation, can be found in...

### **2. Gaussian random variables**

In this section we have collected the facts about Gaussian random vectors, which are used in this book. We start with a useful estimate for standard normal random variables, which is quite precise for large _x_ .

Lemma 3.1. _Suppose X is standard normally distributed. Then, for all x >_ 0 _,_


**Proof.** The right inequality is obtained by the estimate


For the left inequality we define


334

Observe that _f_ (0) _<_ 0 and lim _x→∞ f_ ( _x_ ) = 0. Moreover,


which is positive for _x >_ 0, by the first part. Hence _f_ ( _x_ ) _≤_ 0, proving the lemma.

We now look more closely at random vectors with normally distributed components. Our motivation is that they arise, for example, as vectors consisting of the increments of a Brownian motion. Let us clarify some terminology.

Definition 3.2. _A random variable X_ = ( _X_ 1 _, . . . , Xd_ )<sup>T</sup> _with values in_ R<sup>_d_</sup> _has the d_ -dimensional standard Gaussian distribution _if its d coordinates are standard normally distributed and independent. ⋄_

More general Gaussian distributions can be derived as linear images of standard Gaussians. Recall, e.g. from Definition 1.2 in Chapter 1, that a random variable _Y_ with values in R<sup>_d_</sup> is called _Gaussian_ if there exists an _m_ -dimensional standard Gaussian _X_ , an _d × m_ matrix _A_ , and a _d_ dimensional vector _b_ such that _Y_<sup>T</sup> = _AX_ + _b_ . The _covariance matrix_ of the (column) vector _Y_ is then given by


where the expectations are defined componentwise.

Our next lemma shows that applying an orthogonal _d×d_ matrix does not change the distribution of a standard Gaussian random vector, and in particular that the standard Gaussian distribution is rotationally invariant. We write _Id_ for the _d × d_ identity matrix.

Lemma 3.3. _If A is an orthogonal d × d matrix, i.e. AA_<sup>T</sup> = _Id, and X is a d-dimensional standard Gaussian vector, then AX is also a d-dimensional standard Gaussian vector._

**Proof.** As the coordinates of _X_ are independent, standard normally distributed, _X_ has a density


where _| · |_ is the Euclidean norm. The density of _AX_ is (by the transformation rule) _f_ ( _A_<sup>_−_1</sup> _x_ ) _|_ det( _A_<sup>_−_1</sup> ) _|_ . The determinant is 1 and, since orthogonal matrices preserve the Euclidean norm, the density of _X_ is invariant under _A_ .

Corollary 3.4. _Let X_ 1 _and X_ 2 _be independent and normally distributed with expectation_ 0 _and variance σ_<sup>2</sup> _>_ 0 _. Then X_ 1 + _X_ 2 _and X_ 1 _− X_ 2 _are independent and normally distributed with expectation_ 0 _and variance_ 2 _σ_<sup>2</sup> _._

**Proof.** The vector ( _X_ 1 _/σ, X_ 2 _/σ_ )<sup>T</sup> is standard Gaussian by assumption. Look at


335

This is an orthogonal matrix and applying it to our vector yields (( _X_ 1 + _X_ 2) _/_ ( _√_ 2 _σ_ ) _,_ ( _X_ 1 _− X_ 2) _/_ ( _√_ 2 _σ_ )), which thus must have independent standard normal coordinates.

The next proposition shows that the distribution of a Gaussian random vector is determined by its expectation and covariance matrix.

Proposition 3.5. _If X and Y are d-dimensional Gaussian vectors with_ E _X_ = E _Y and_ Cov( _X_ ) = Cov( _Y_ ) _, then X and Y have the same distribution._

**Proof.** It is sufficient to consider the case E _X_ = E _Y_ = 0. By definition, there are standard Gaussian random vectors _X_ 1 and _X_ 2 and matrices _A_ and _B_ with _X_ = _AX_ 1 and _Y_ = _BX_ 2. By adding columns of zeros to _A_ or _B_ , if necessary, we can assume that _X_ 1 and _X_ 2 are both _k_ -vectors, for some _k_ , and _A, B_ are both _d × k_ matrices. Let _A_ and _B_ be the vector subspaces of R<sup>_k_</sup> generated by the row vectors of _A_ and _B_ , respectively. To simplify notation assume that the first _l ≤ d_ row vectors of _A_ form a basis of _A_ . Define the linear map _L_ : _A →B_ by


Here _Ai_ is the _i_<sup>th</sup> row vector of _A_ , and _Bi_ is the _i_<sup>th</sup> row vector of _B_ . Our aim is to show that _L_ is an orthogonal isomorphism and then use the previous proposition. Let us first show that _L_ is an isomorphism. Our covariance assumption gives that _AA_<sup>T</sup> = _BB_<sup>T</sup> . Assume there is a vector _v_ 1 _A_ 1 + _. . . vlAl_ whose image is 0. Then the _d_ -vector


satisfies _vB_ = 0. Hence


We conclude that _vA_ = 0. Hence _L_ is injective and dim _A ≤_ dim _B_ . Interchanging the roles of _A_ and _B_ gives that _L_ is an isomorphism. As the entry ( _i, j_ ) of _AA_<sup>T</sup> = _BB_<sup>T</sup> is the scalar product of _Ai_ and _Aj_ as well as _Bi_ and _Bj_ , the mapping _L_ is orthogonal. We can extend it on the orthocomplement of _A_ to an orthogonal map _L_ : R<sup>_k_</sup> _→_ R<sup>_k_</sup> (or an orthogonal _k × k_ -matrix). Then _X_ = _AX_ 1 and _Y_ = _BX_ 2 = _AL_<sup>T</sup> _X_ 2. As _L_<sup>T</sup> _X_ 2 is standard Gaussian, by Lemma 3.3, _X_ and _Y_ have the same distribution.

In particular, comparing a _d_ -dimensional Gaussian vector with Cov( _X_ ) = _Id_ with a Gaussian vector with _d_ independent entries and the same expectation, we obtain the following fact.

Corollary 3.6. _A Gaussian random vector X has independent entries if and only if its covariance matrix is diagonal. In other words, the entries in a Gaussian vector are uncorrelated if and only if they are independent._

We now show that the Gaussian nature of a random vector is preserved under taking limits.

Proposition 3.7. _Suppose {Xn_ : _n ∈_ N _} is a sequence of Gaussian random vectors and_ lim _n Xn_ = _X, almost surely. If b_ := lim _n→∞_ E _Xn and C_ := lim _n→∞_ Cov _Xn exist, then X is Gaussian with mean b and covariance matrix C._

336

**Proof.** A variant of the argument in Proposition 3.5 shows that _Xn_ converges in law to a Gaussian random vector with mean _b_ and covariance matrix _C_ . As almost sure convergence implies convergence of the associated distributions, this must be the law of _X_ .

Lemma 3.8. _Suppose X, Y are independent and normally distributed with mean zero and variance σ_<sup>2</sup> _, then X_<sup>2</sup> + _Y_<sup>2</sup> _is exponentially distributed with mean_ 2 _σ_<sup>2</sup> _._

**Proof.** For any bounded, measurable _f_ : R _→_ R we have, using polar coordinates,


where _Z_ is exponential with mean 2 _σ_<sup>2</sup> .

### **3. Martingales in discrete time**

In this section we recall the essentials from the theory of martingales in discrete time. A more thorough introduction to this delightful subject is Williams [ **Wi91** ].

Definition 4.1. _A_ filtration ( _Fn_ : _n ≥_ 0) _is an increasing sequence_


_of σ-algebras. Let {Xn_ : _n ≥_ 0 _} be a stochastic process in discrete time and_ ( _Fn_ : _n ≥_ 0) _be a filtration. The process is a_ martingale _relative to the filtration if, for all n ≥_ 0 _,_

_• Xn is measurable with respect to Fn,_


_If we have ‘≥’ in the last condition, then {Xn_ : _n ≥_ 0 _} is called a_ submartingale _, if ‘≤’ holds it is called a_ supermartingale _. ⋄_

Remark 4.2. Note that for a submartingale E[ _Xn_ +1] _≥_ E[ _Xn_ ], for a supermartingale E[ _Xn_ +1] _≤ ⋄_ E[ _Xn_ ], and hence for a martingale we have E[ _Xn_ +1] = E[ _Xn_ ] _._

Loosely speaking, a stopping time is a random time such that the knowledge about a random process at time _n_ suffices to determine whether the stopping time has happened at time _n_ or not. Here is a formal definition.

Definition 4.3. _A random variable T with values in {_ 0 _,_ 1 _,_ 2 _, . . .} ∪{∞} is called a_ stopping _⋄_ time _if {T ≤ n}_ = _{ω_ : _T_ ( _ω_ ) _≤ n} ∈Fn for all n ≥_ 0 _._

337

If _{Xn_ : _n ≥_ 0 _}_ is a supermartingale and _T_ a stopping time, then it is easy to check that the process

_{Xn_<sup>_T_:</sup><sup>_n ≥_0</sup><sup>_}_</sup> defined by _Xn_<sup>_T_=</sup><sup>_XT∧n_</sup>

is a supermartingale. If _{Xn_ : _n ≥_ 0 _}_ is a martingale, then both _{Xn_ : _n ≥_ 0 _}_ and _{−Xn_ : _n ≥_ 0 _}_ are supermartingales and, hence, we have,


Doob’s optional stopping theorem gives criteria when, letting _n ↑∞_ , we obtain E[ _XT_ ] = E[ _X_ 0].

Theorem 4.4 (Doob’s optional stopping theorem). _Let T be a stopping time and X a martingale. Then XT is integrable and_ E� _XT_ � = E� _X_ 0� _, if one of the following conditions hold:_

- (1) _T is bounded, i.e. there is N such that T < N almost surely;_

- (2) _{Xn_<sup>_T_:</sup><sup>_n≥_0</sup><sup>_}isdominatedbyanintegrablerandomvariableZ,i.e.|Xn∧T|≤Zfor_</sup> _all n ≥_ 0 _almost surely;_

- (3) E[ _T_ ] _< ∞ and there is K >_ 0 _such that_ sup _n |Xn − Xn−_ 1 _| ≤ K._

**Proof.** Recall that E[ _XT ∧n − X_ 0] = 0. The result follows in case (1) by choosing _n_ = _N_ . In case (2) let _n →∞_ and use dominated convergence. In case (3) observe that _|XT ∧n − X_ 0 _|_ = _|_<sup>�</sup><sup>_T_</sup> _k_ =1<sup>_∧n_(</sup><sup>_Xk−Xk−_1)</sup><sup>_|≤KT._Byassumption</sup><sup>_KT_isanintegrablefunctionand</sup> dominated convergence can be used again.

Doob’s famous forward convergence theorem gives a sufficient condition for the almost sure convergence of supermartingales to a limiting random variable. See [ **Wi91** , 11.5] for the proof.

Theorem 4.5 (Doob’s supermartingale convergence theorem). _Let {Xn_ : _n ≥_ 0 _} be a supermartingale, which is bounded in L_<sup>1</sup> _, i.e. there is K >_ 0 _such that_ E _|Xn| ≤ K for all n. Then there exists an integrable random variable X on the same probability space such that_


Remark 4.6. Note that if _{Xn_ : _n ≥_ 0 _}_ is nonnegative, we have E[ _|Xn|_ ] = E[ _Xn_ ] _≤_ E[ _X_ 0] := _K_ and thus _Xn_ is automatically bounded in _L_<sup>1</sup> and lim _n→∞ Xn_ = _X_ exists. _⋄_

A key question is when the almost sure convergence in the supermartingale convergence theorem can be replaced by _L_<sup>1</sup> -convergence (which in contrast to almost sure convergence implies convergence of expectations). A necessary and sufficient criterion for this is _uniform integrability_ . A stochastic process _{Xn_ : _n ≥_ 0 _}_ is called _uniformly integrable_ if, for every _ε >_ 0, there exists _K >_ 0 such that


Sufficient criteria for uniform integrability are

338

- _{Xn_ : _n ≥_ 0 _}_ is dominated by an integrable random variable,

- _{Xn_ : _n ≥_ 0 _}_ is _L_<sup>_p_</sup> -bounded for some _p >_ 1,

- _{Xn_ : _n ≥_ 0 _}_ is _L_<sup>1</sup> -convergent.

The following lemma is proved in [ **Wi91** , 13.7].

Lemma 4.7. _Any stochastic process {Xn_ : _n ≥_ 0 _}, which is uniformly integrable and almost surely convergent, converges also in the L_<sup>1</sup> _-sense._

The next result is one of the highlights of martingale theory.

Theorem 4.8 (Martingale closure theorem). _Suppose that the martingale {Xn_ : _n ≥_ 0 _} is uniformly integrable. Then there is an integrable random variable X such that_

_n_ lim _→∞_<sup>_Xn_=</sup><sup>_XalmostsurelyandinL_1</sup><sup>_._</sup>

_Moreover, Xn_ = E[ _X | Fn_ ] _for every n ≥_ 0 _._

**Proof.** Uniform integrability implies that _{Xn_ : _n ≥_ 0 _}_ is _L_<sup>1</sup> -bounded and thus, by the martingale convergence theorem, almost surely convergent to an integrable random variable _X_ . Convergence in the _L_<sup>1</sup> -sense follow from Lemma II.4.7. To check the last assertion, we note that _Xn_ is _Fn_ -measurable and let _F ∈Fn_ . For all _m ≥ n_ we have, by the martingale property, � _F_<sup>_Xm d_P=</sup> � _F_<sup>_Xn d_P</sup><sup>_._Welet</sup><sup>_m→∞_.Then</sup><sup>_|_</sup> � _F_<sup>_Xm d_P</sup><sup>_−_</sup> � _F_<sup>_X d_P</sup><sup>_|≤_</sup> � _|Xm − X| d_ P _→_ 0 _,_ hence we obtain � _F_<sup>_X d_P =</sup> � _F_<sup>_Xn d_P,asrequired.</sup>

There is a natural converse to the martingale closure theorem, see [ **Wi91** , 14.2] for the proof. Theorem 4.9 (L´evy’s upward theorem). _Suppose that X is an integrable random variable and Xn_ = E[ _X | Fn_ ] _. Then {Xn_ : _n ≥_ 0 _} is a uniformly integrable martingale and_

_n_ lim _→∞_<sup>_Xn_= E</sup> � _X | F∞_ � _almost surely and in L_<sup>1</sup> _,_

_where F∞_ = �� _n∞_ =1<sup>_Fn_</sup> � _is the smallest σ-algebra containing the entire filtration._

There is also a convergence theorem for ‘reverse’ martingales, which is called L´evy’s downward theorem and is a natural partner to the upward theorem, see [ **Wi91** , 14.4] for the proof.

Theorem 4.10 (L´evy’s downward theorem). _Suppose that_ ( _Gn_ : _n ∈_ N) _is a collection of σ-algebras such that_


_An integrable process {Xn_ : _n ∈_ N _} is a_ **reverse martingale** _if almost surely,_


_Then_


339

An important consequence of Theorems II.4.4 and II.4.8 is that the martingale property holds for well-behaved stopping times. For a stopping time _T_ define _FT_ to be the _σ_ -algebra of events _A_ with _A ∩{T ≤ n} ∈Fn_ . Observe that _XT_ is _FT_ -measurable.

Theorem 4.11 (Optional sampling theorem). _If the martingale {Xn_ : _t ≥_ 0 _} is uniformly integrable, then for all stopping times_ 0 _≤ S ≤ T we have_ E[ _XT_ �� _FS_ ] = _XS almost surely._

**Proof.** By the martingale closure theorem, _Xn_<sup>_T_</sup> converges to _XT_ in _L_<sup>1</sup> and E[ _XT | Fn_ ] = _XT ∧n_ = _Xn_<sup>_T_.</sup> Dividing _XT_ in its positive and its nonpositive part if necessary, we may assume that _XT ≥_ 0 and therefore _Xn_<sup>_T≥_0almostsurely.Takingconditional</sup> expectation with respect to _FS∧n_ gives E� _XT_ �� _FS∧n_ � = _XS∧n_ . Now let _A ∈FS_ . We have to show that E[ _XT_ 1 _A_ ] = E[ _XS_ 1 _A_ ] _._ Note first that _A ∩{S ≤ n} ∈FS∧k_ . Hence, we get E[ _XT_ 1 _{A ∩{S ≤ n}}_ ] = E[ _XS∧n_ 1 _{A ∩{S ≤ n}}_ ] = E[ _XS_ 1 _{A ∩{S ≤ n}}_ ]. Letting _n ↑∞_ and using monotone convergence gives the required result.

Of considerable practical importance are martingales _{Xn_ : _t ≥_ 0 _}_ , which are _square integrable_ . Note that in this case we can calculate, for _m ≥ n_ ,


so that _{Xn_<sup>2:</sup><sup>_t ≥_0</sup><sup>_}_isasubmartingale.</sup>

Theorem 4.12 (Convergence theorem for _L_<sup>2</sup> -bounded martingales). _Suppose that the martingale {Xn_ : _t ≥_ 0 _} is L_<sup>2</sup> _-bounded. Then there is a random variable X such that_


**Proof.** From (3.1) and _L_<sup>2</sup> -boundedness of _{Xn_ : _t ≥_ 0 _}_ it is easy to see that, for _m ≥ n_ ,


Recall that _L_<sup>2</sup> -boundedness implies _L_<sup>1</sup> -boundedness, and hence, by the martingale convergence theorem, _Xn_ converges almost surely to an integrable random variable _X_ . Letting _m ↑∞_ and using Fatou’s lemma in the last display, gives _L_<sup>2</sup> -convergence.

We now discuss two _martingale inequalities_ that have important counterparts in the continuous setting. The first one is Doob’s weak maximal inequality.

Theorem 4.13 (Doob’s weak maximal inequality). _Let {Xj_ : _j ≥_ 0 _} be a submartingale and denote Mn_ := max1 _≤j≤n Xj. Then, for all λ >_ 0 _,_


340

**Proof.** Define the stopping time


Note that _{Mn ≥ λ}_ = _{Xτ ≥ λ}_ . This implies


and the result follows once we demonstrate E _Xτ_ 1 _{Mn ≥ λ} ≤_ E _Xn_ 1 _{Mn ≥ λ}_ . But, as _τ_ is bounded by _n_ and _X_<sup>_τ_</sup> is a submartingale, we have E[ _Xτ_ ] _≤_ E[ _Xn_ ], which implies that

E� _Xτ_ 1 _{Mn < λ}_ � + E� _Xτ_ 1 _{Mn ≥ λ}_ � _≤_ E� _Xn_ 1 _{Mn < λ}_ � + E� _Xn_ 1 _{Mn ≥ λ}_ � _._ by definition of _τ_ , we have _Xττ_ 1 _{MnMnn < λ}}_ = _Xnn_ 1 _{MnMnn < λ}}_ , this reduces to E� _Xτ_ 1 _{Mn ≥ λ}_ � _≤_ E� _Xn_ 1 _{Mn ≥ λ}_ � _,_

Because, by definition of _τ_ , we have _Xττ_ 1 _{MnMnn < λ}}_ = _Xnn_ 1 _{MnMnn < λ}}_ , this reduces to

and this concludes the proof.

The most useful martingale inequality for us is Doob’s _L_<sup>_p_</sup> -maximal inequality.

Theorem 4.14 (Doob’s _L_<sup>_p_</sup> maximal inequality). _Suppose {Xn_ : _n ≥_ 0 _} is a submartingale. Let Mn_ = max1 _≤k≤n Xk and p >_ 1 _. Then_


We make use of the following lemma, which allows us to compare the _L_<sup>_p_</sup> -norms of two nonnegative random variables.

Lemma 4.15. _Suppose nonnegative random variables X and Y satisfy, for all λ >_ 0 _,_

_λ_ P _{Y ≥ λ} ≤_ E[ _X_ 1 _{Y ≥ λ}_ ] _._

_Then, for all p >_ 1 _,_


**Proof.** Using the fact that _X ≥_ 0 and _x_<sup>_p_</sup> = �0 _x_<sup>_pλp−_1</sup><sup>_dλ_,wecanexpressE[</sup><sup>_Xp_]asadouble</sup> integral and apply Fubini’s theorem,


Similarly, using the hypothesis,


We can rewrite the right hand side, using Fubini’s theorem again, and then integrating _pλ_<sup>_p−_2</sup> and using H¨older’s inequality with _q_ = _p/_ ( _p −_ 1),


341

Altogether, this gives E[ _Y_<sup>_p_</sup> ] _≤ q_ (E[ _X_<sup>_p_</sup> ])<sup>1</sup><sup>_/p_</sup> (E[ _Y_<sup>_p_</sup> ])<sup>1</sup><sup>_/q_</sup> So, assuming E[ _Y_<sup>_p_</sup> ] _< ∞_ , the above inequality gives,


from which the result follows by raising both sides to the _p_<sup>th</sup> power. In general, if E[ _Y_<sup>_p_</sup> ] = _∞_ , then for any _n ∈_ N, the random variable _Yn_ = _Y ∧ n_ satisfies the hypothesis of the lemma, and the result follows by letting _n ↑∞_ and applying the monotone convergence theorem.

**Proof of Theorem 4.14.** If _{Xn_ : _n ≥_ 0 _}_ is a submartingale, so is _{|Xn|_ : _n ≥_ 0 _}_ . Hence we may assume in the proof that _Xn ≥_ 0. By Doob’s weak maximal inequality,


and applying Lemma 4.15 with _X_ = _Xn_ and _Y_ = _Mn_ gives the result.

### **4. The max-flow min-cut theorem**

Here we give a short proof of a famous result of graph theory, the _max-flow min-cut theorem_ of Ford and Fulkerson [ **FF56** ] in the special case of infinite trees.

Theorem 5.1 (Max-flow min-cut theorem).


**Proof.** The proof is a festival of compactness arguments.

First observe that on the left hand side the infimum is indeed a maximum, because if _{θn}_ is a sequence of flows with capacities _C_ , then at every edge we have a bounded sequence _{θn_ ( _e_ ) _}_ and by the diagonal argument we may pass to a subsequence such that lim _θn_ ( _e_ ) exists simultaneously for all _e ∈ E_ . This limit is obviously again a flow with capacities _C_ .

Secondly observe that every cutset Π contains a finite subset Π<sup>_′_</sup> _⊂_ Π, which is still a cutset. Indeed, if this was not the case, we had for every positive integer _j_ a ray _e_<sup>_j_</sup> 1<sup>_, ej_</sup> 2<sup>_, ej_</sup> 3<sup>_, . . ._with</sup> _e_<sup>_j_</sup> _i̸_<sup>_∈_Πforall</sup><sup>_i≤j_.Bythediagonalargumentwefindasequence</sup><sup>_jk_andedges</sup><sup>_el_oforder</sup> _l_ such that _e_<sup>_jk_</sup> _l_ = _el_ for all _k ≥ l_ . Then _e_ 1 _, e_ 2 _, . . ._ is a ray and _el̸ ∈_ Π for all _l_ , which is a contradiction.

Now let _θ_ be a flow with capacities _C_ and Π an arbitrary cutset. We let _A_ be the set of vertices _v_ such that there is a sequence of edges _e_ 1 _, . . . , en̸ ∈_ Π with _e_ 1 = ( _ρ, v_ 1), _en_ = ( _vn−_ 1 _, v_ ) and _ej_ = ( _vj−_ 1 _, vj_ ). By our previous observation this set is finite. Let


342

Then, using the definition of a flow and finiteness of all sums,


This proves the first inequality.

For the reverse inequality we restrict attention to finite trees. Let _Tn_ be the tree consisting of all vertices _Vn_ and edges _En_ of order _≤ n_ and look at cutsets Π consisting of vertices in _En_ . A flow of strength _c >_ 0 through the tree _Tn_ with capacities _C_ is a mapping _θ_ : _En →_ [0 _, c_ ] such that


Once we have this, we get a sequence ( _θn_ ) of flows in _Tn_ with capacities _C_ and strength at least _c_ = min _{_<sup>�</sup> _e∈_ Π<sup>_C_(</sup><sup>_e_):Πacutsetin</sup><sup>_T}_.Byusingthediagonalargumentoncemorewecan</sup> get a subsequence such that the limits of _θn_ ( _e_ ) exist for every edge, and the result is a flow _θ_ with capacities _C_ and strength at least _c_ , as required.

To prove (4.1) let _θ_ be a flow of maximal strength _c_ with capacities _C_ in _Tn_ and call a sequence _ρ_ = _v_ 0 _, v_ 1 _, . . . , vn_ with ( _vi, vi_ +1) _∈ En_ an _augmenting sequence_ if _θ_ ( _vi, vi_ +1) _< C_ ( _vi, vi_ +1). If there are augmenting sequences, we can construct a flow _θ_<sup>�</sup> of strength _> c_ by just increasing the flow through every edge of the augmenting sequence by a sufficiently small _ε >_ 0. As _θ_ was maximal this is a contradiction. Hence there is a minimal cutset Π consisting entirely of edges in _En_ with _θ_ ( _e_ ) _≥ C_ ( _e_ ). Let _A_ , as above, be the collection of all edges which are connected to the root by edges not in Π. As before, we have


where in the penultimate step we use minimality. This proves (4.1) and finishes the proof.

343

---

[← Appendix I: Hints and solutions for selected exercises](15-appendix-i-hints-and-solutions-for-selected-exercises.md) · [Up: contents](index.md) · [Index →](17-index.md)
