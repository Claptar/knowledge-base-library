---
title: 7 Lecture 7
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes210BSpring2018.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Lecture 7

**Source:** [`FullNotes210BSpring2018.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes210BSpring2018.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The next main topic in the class is chaining. Before we go to chaining, we shall review the topics that were covered last week by Chi and Max.

We are discussing the problem of controlling:


The symmetrization technique introduced last week allows us to bound the above as:


where _ϵ_ 1 _, . . . , ϵn_ are independent Rademacher random variables which are also independent of _X_ 1 _, . . . , Xn_ . The expectation on the right hand side above is with respect to both _ϵ_ 1 _, . . . , ϵn_ and _X_ 1 _, . . . , Xn_ . To control the expectation on the right hand side above, one usually works conditionally on _X_ 1 _, . . . , Xn_ . The conditional expectation is then of the form


33

for a subset _T_ of R<sup>_n_</sup> . _Rn_ ( _T_ ) is easier to handle because the expectation is with respect to _ϵ_ 1 _, . . . , ϵn_ which have a particularly simple distribution (i.i.d Rademachers).

In Lecture 5, we have seen the following elementary bound on _Rn_ ( _T_ ).

**Proposition 7.1.** _Suppose T is a finite subset of_ R<sup>_n_</sup> _with cardinality |T |. Then_


_for a universal constant C._

The bound given by (40) has some shortcomings. It does not give anything when _T_ is infinite. Even when _T_ is finite, the bound is weak in some special situations. For example, when


for some fixed points _x_ 1 _< · · · < xn_ in R, then it is easy to check that _|T |_ = _n_ + 1 so that the bound (40) gives


It turns out that for this particular _T_ , the logarithmic term log( _n_ + 1) is redundant and that _Rn_ ( _T_ ) is of the order _Cn_<sup>_−_1</sup><sup>_/_2</sup> . The bound on _Rn_ ( _T_ ) derived from chaining will be of the form _C/n_<sup>_−_1</sup><sup>_/_2</sup> . The extra logarithmic factor is because of the inefficiency of (40).

In spite of these drawbacks, the bound (40) is important and crucially used for deriving the chaining bound. Before proceeding further, we shall provide a proof of Proposition 7.1. This proof will be slightly different from the way it was proved last week. We shall actually prove a stronger version of (40).

**Proposition 7.2.** _Let T be a finite set and let {Xt, t ∈ T } be a stochastic process. Suppose that for every t ∈ T and u ≥_ 0 _, the inequality_


_holds. Here_ Σ _is a fixed positive real number. Then, for a universal positive constant C, we have_


**Remark 7.1.** _Note that Proposition 7.2 is indeed a generalization of Proposition 7.1. This is because for Xt_ :=<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ϵiti(witht ∈T),Hoeffding’sinequalityassuresthat_(260)</sup><sup>_holdswith_</sup>


_Proposition 7.2 holds for every set of random variables Xt satisfying_ (260) _so in addition to Xt_ =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_ϵiti,_</sup> _it also holds for Xt ∼ N_ (0 _, σ_<sup>2</sup> ) _with σ ≤_ Σ _._

_Proof of Proposition 7.2._ Because


we can control E max _t∈T |Xt|_ by bounding the tail probability


34

for every _u ≥_ 0. For this, write


This bound is good for large _u_ but not so good for small _u_ (it is quite bad for _u_ = 0 for example). It is therefore good to use it only for _u ≥ u_ 0 for some _u_ 0 to be specified later. This gives


One can try to minimize the above term over _u_ 0. A simpler strategy is to realize that the large term here is 2 _|T |_ so one can choose _u_ 0 to kill this term by setting


This gives


which proves the result.

It is not hard to construct examples where the bound given by Proposition 7.2 is loose. For example, it is loose when the tail bound (260) is loose for many _t ∈ T_ (this can happen for instance when _Xt ∼ N_ (0 _, σ_<sup>2</sup> ) for some _σ_<sup>2</sup> that is much smaller than Σ<sup>2</sup> ). It can also be loose when many of the _Xt_<sup>_′s_areclosetoeach</sup> other: for instance, in the extreme case when max _t∈T |Xt| ≈ Xt_ 0 for a single _t_ 0 _∈ T_ , the bound in (42) is loose by a factor of log _|T |_ .

However there exist examples where the bound in (42) is tight. The simplest example is the following. Suppose _Xt, t ∈ T_ are independently distributed as _N_ (0 _,_ Σ<sup>2</sup> ). Then it can be shown that


for a positive constant _c_ . Therefore, in this case, (42) is tight up to a constant factor. I will leave the proof of the above inequality as a homework exercise. This example means that Proposition 7.2 cannot be improved without additional assumptions on the process _{Xt, t ∈ T }_ . Chaining gives improved bounds for E max _t∈T |Xt|_ under an assumption on _{Xt, t ∈ T }_ that is different from (260). The assumption (260) pertains to the marginal distribution of each _Xt_ but does not say anything about how close _Xt_ is to another _Xs_ etc. In contrast, for chaining, one assumes the existence of a metric _d_ on _T_ such that


Under this assumption, chaining provides a bound on E max _t∈T |Xt|_ which involves the metric properties of ( _T, d_ ). Before proceeding to chaining, let us recall the notions of covering and packing numbers of a metric space.

35

## **7.1 Review of Covering and Packing numbers**

Let ( _T, d_ ) be a metric or pseudometric space. Covering and packing numbers are defined as follows.

**Definition 7.3** (Covering Numbers) **.** _For a subset F of T and δ >_ 0 _, the δ-covering number of F is denoted by NT_ ( _δ, F, d_ ) _and is defined as the smallest number of closed δ-balls needed to cover F . In other words, NT_ ( _δ, F, d_ ) _is the smallest N for which there exist points t_ 1 _, . . . , tN ∈ T with_ min1 _≤i≤N d_ ( _t, ti_ ) _≤ δ for each t ∈ F . The set of centers {ti} is called a δ-net for F . The logarithm of NT_ ( _δ, F, d_ ) _is called the δ-metric entropy of F ._

**Remark 7.2.** _Note that the centers t_ 1 _, . . . , tN are not constrained to be in F . This is related to the presence of the subscript T in the definition NT_ ( _δ, F, d_ ) _of the covering numbers of F . If we regard F as a metric space in its own right, not just as a subset of T , then the covering numbers NF_ ( _δ, F, d_ ) _might be larger because the centers ti would then be forced to lie in F . It is an easy exercise to prove that NF_ (2 _δ, F, d_ ) _≤ NT_ ( _δ, F, d_ ) _and the extra factor of_ 2 _would usually be of little consequence._

If _NT_ ( _δ, T, d_ ) _< ∞_ for every _δ >_ 0, we say that _T_ is totally bounded.

The notion of covering numbers is closely related to that of packing numbers which are defined next.

**Definition 7.4.** _For δ >_ 0 _, the δ-packing number of F is defined as the largest N for which there exist points t_ 1 _, . . . , tN ∈ F with d_ ( _ti, tj_ ) _> δ for every i̸_ = _j (these points t_ 1 _, . . . , tN are said to be δ-separated). The δ-packing number will be denoted by M_ ( _δ, F, d_ ) _._

Because of the following result (proved in last lecture), we shall treat covering and packing numbers as roughly the same.

**Lemma 7.5.** _For every δ >_ 0 _, we have_


Below we see some examples where explicit bounds for covering/packing numbers are possible. It is useful to be aware of these results.

### **7.1.1 Euclidean/Parametric Covering Numbers**

**Proposition 7.6.** _For R >_ 0 _, let_


_denote the ball of radius R centered at a point a. ∥·∥ here is the usual Euclidean norm. Then, for every ϵ >_ 0 _, we have_


_and_


_where d denotes the usual Euclidean metric._

These bounds are simple to prove (proved in last lecture) and the proofs are based on volume comparison (as a result, these bounds are often referred to as volumetric bounds). The following is an immediate corollary of (44)

36

**Corollary 7.7.** _Suppose S ⊆_ R<sup>_k_</sup> _is contained in some ball of radius R. Then_


_with d denoting the usual Euclidean metric._

The above result implies that the covering numbers of bounded sets in R<sup>_k_</sup> grow as _ϵ_<sup>_−k_</sup> . Equivalently, the **metric entropy** of sets in R<sup>_k_</sup> grows as _k_ log(1 _/ϵ_ ). If _k_ is constant, then the metric entropy grows logarithmically with 1 _/ϵ_ . The same conclusion can often be drawn for function classes that are indexed by a bounded set in R<sup>_k_</sup> provided the mapping between the index and the function is smooth. The following proposition provides one way of making this precise.

**Proposition 7.8.** _Let_ Θ _⊆_ R<sup>_k_</sup> _be a non-empty bounded subset with Euclidean diameter D and let F_ := _{fθ_ : _θ ∈_ Θ _} be a class of functions on X indexed by_ Θ _such that for some nonnegative function_ Γ : _X →_ R _, we have_


_for all x ∈X and θ_ 1 _, θ_ 2 _∈_ Θ _. Here ∥·∥ denotes the usual Euclidean norm on_ R<sup>_k_</sup> _._

_Fix a probability measure Q on X and let d denote the pseudometric on F defined by_


_Then, for every ϵ >_ 0 _,_


Function classes whose covering numbers grow as _ϵ_<sup>_−k_</sup> (or whose metric entropy grows as log(1 _/ϵ_ )) will often be referred to as _parametric_ or _Euclidean_ or _finite-dimensional_ .

### **7.1.2 Nonparametric Function Classes**

Nonparametric function classes are much more massive in comparison to parametric classes in the sense that their metric entropy grows as a polynomial in (1 _/ϵ_ ). Some standard examples of nonparametric functions classes are provided below.

### **7.1.3 One-dimensional smoothness classes**

Fix _α >_ 0. Let _β_ denote the largest integer that is **strictly** smaller than _α_ . For example, if _α_ = 5, then _β_ = 4 and if _α_ = 5 _._ 2, then _β_ = 5.

The class _Sα_ is defined to consist of functions _f_ on [0 _,_ 1] that satisfy all the following properties:

1. _f_ is continuous on [0 _,_ 1].

2. _f_ is differentiable _β_ times on (0 _,_ 1).

3. _|f_<sup>(</sup><sup>_k_)</sup> ( _x_ ) _| ≤_ 1 for all _k_ = 0 _, . . . , β_ and _x ∈_ [0 _,_ 1] where _f_<sup>(0)</sup> ( _x_ ) := _f_ ( _x_ ).

4. _|f_<sup>(</sup><sup>_β_)</sup> ( _x_ ) _− f_<sup>(</sup><sup>_β_)</sup> ( _y_ ) _| ≤|x − y|_<sup>_α−β_</sup> for all _x, y ∈_ (0 _,_ 1).

37

Let _ρ_ denote the supremum metric on _Sα_ defined by


The following result shows that the metric entropy of _Sα_ grows as _ϵ_<sup>_−_1</sup><sup>_/α_</sup> . Its proof can be found in Dudley [6, Chapter 8].

**Theorem 7.9.** _There exist positive constants ϵ_ 0 _, C_ 1 _and C_ 2 _denpending on α alone such that for all ϵ >_ 0 _, we have_


Thus the _ϵ_ -metric entropy (logarithm of the _ϵ_ -covering number) of the smoothness class _Sα_ in one dimension grows as _ϵ_<sup>_−_1</sup><sup>_/α_</sup> . Here _α_ denotes the degree of smoothness (the higher _α_ is, the smoother the functions in _Sα_ ). When _α_ = 1, the class _Sα_ consists of all bounded 1-Lipschitz functions on [0 _,_ 1].

### **7.1.4 One-dimensional Monotone Functions**

Let _M_ denote the class of all functions _f_ on [0 _,_ 1] such that

1. _f_ is nondecreasing on [0 _,_ 1]

2. _|f_ ( _x_ ) _| ≤_ 1 for all _x ∈_ [0 _,_ 1].

For a probability measure _Q_ on [0 _,_ 1], let _ρQ_ denote the metric on _M_ given by


Then it can be proved that


for every probability measure _Q_ on [0 _,_ 1]. There exist probability measures _Q_ for which a lower bound of exp( _C_ 2 _/ϵ_ ) also holds on the packing number. Comparing this result with Theorem 7.9, it is clear that the covering numbers of _M_ are comparable to the smoothness class _S_ 1 i.e., _Sα_ with _α_ = 1. Thus bounded monotone functions have the same metric entropy as bounded Lipschitz functions even though monotone functions need not be continuous.

### **7.1.5 Multidimensional smoothness classes**

As in the one-dimensional case, let _α >_ 0 and _β_ is the largest integer that is strictly smaller than _α_ .

For a vector _p_ = ( _p_ 1 _, . . . , pd_ ) consisting of nonnegative integers _p_ 1 _, . . . , pd_ , let _⟨p⟩_ := _p_ 1 + _· · ·_ + _pd_ . Let


The class _Sα,d_ is defined to consist of all functions _f_ on [0 _,_ 1]<sup>_d_</sup> that satisfy:

1. _f_ is continuous on [0 _,_ 1]<sup>_d_</sup> .

2. All partial derivatives _D_<sup>_p_</sup> of _f_ exist on (0 _,_ 1)<sup>_d_</sup> for _⟨p⟩≤ β_ .

3. _|D_<sup>_p_</sup> ( _x_ ) _| ≤_ 1 for all _p_ with _⟨p⟩≤ β_ and _x ∈_ [0 _,_ 1]<sup>_d_</sup> .

38

4. _|D_<sup>_p_</sup> _f_ ( _x_ ) _− D_<sup>_p_</sup> _f_ ( _y_ ) _| ≤|x − y|_<sup>_α−β_</sup> for all _p_ with _⟨p⟩_ = _β_ and _x, y ∈_ (0 _,_ 1)<sup>_d_</sup> .

Once again, we consider the supremum metric defined by _ρ_ ( _f, g_ ) := sup _x∈_ [0 _,_ 1] _d |f_ ( _x_ ) _− g_ ( _x_ ) _|_ .

**Theorem 7.10.** _There exist positive constants C_ 1 _and C_ 2 _depending only on α and the dimension d such that for all ϵ >_ 0 _, we have_


Thus the metric entropy of a smoothness class of functions with smoothness _α_ and dimension _d_ scales as _ϵ_<sup>_−d/α_</sup> . This grows as _d_ increases and goes down as _α_ increases.

### **7.1.6 Bounded Lipschitz Convex Functions**

Let _C_ denote the class of all functions _f_ on 0 _,_ 1]<sup>_d_</sup> such that

1. _f_ is convex on [0 _,_ 1]<sup>_d_</sup> .

2. _|f_ ( _x_ ) _| ≤_ 1 for all _x ∈_ [0 _,_ 1]<sup>_d_</sup>


It can then be showed that ( _ρ_ is the supremum metric on [0 _,_ 1]<sup>_d_</sup> ):


where _C_ 1 and _C_ 2 depend on _d_ alone. Comparing this to Theorem 7.10, it is clear that, in terms of metric entropy, _C_ is comparable to the smoothness class _Sd,_ 2. This is interesting because convex functions are not necessarily twice differentiable in the usual sense. Yet, they possess the regularity of second order smoothness in terms of metric entropy.

---

[← 6 Lecture 6](07-6-lecture-6.md) · [Up: contents](index.md) · [8 Lecture 8 →](09-8-lecture-8.md)
