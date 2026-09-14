---
title: Intersections and self-intersections of Brownian paths
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Intersections and self-intersections of Brownian paths

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this chapter we study multiple points of _d_ -dimensional Brownian motion. We shall see, for example, in which dimensions the Brownian path has double points and explore how many double points there are. This chapter also contains some of the highlights of the book: a proof that planar Brownian motion has points of infinite multiplicity, the intersection equivalence of Brownian motion and percolation limit sets, and the surprising dimension-doubling theorem of Kaufman.

### **1. Intersection of paths: existence and Hausdorff dimension**

**1.1. Existence of inetrsections.** Suppose that _{B_ 1( _t_ ) : _t ≥_ 0 _}_ and _{B_ 2( _t_ ) : _t ≥_ 0 _}_ are two independent _d_ -dimensional Brownian motions started in arbitrary points. The question we ask in this section is, in which dimensions the ranges, or paths, of the two motions have a nontrivial intersection, in other words whether there exist times _t_ 1 _, t_ 2 _>_ 0 such that _B_ 1( _t_ 1) = _B_ 2( _t_ 2). As this question is trivial if _d_ = 1 we assume _d ≥_ 2 throughout this section.

We have developed the tools to decide this question in Chapter 4 and Chapter 8. Keeping the path _{B_ 1( _t_ ) : _t ≥_ 0 _}_ fixed, we have to decide whether it is a polar set for the second Brownian motion. By Kakutani’s theorem, Theorem 8.19, this question depends on its capacity with respect to the potential kernel. As the capacity is again related to Hausdorff measure and dimension, the results of Chapter 4 are crucial in the proof of the following result.

Theorem 9.1.

- (a) _For d ≥_ 4 _, almost surely, two independent Brownian paths in_ R<sup>_d_</sup> _have an empty intersection, except for a possible common starting point._

- (b) _For d ≤_ 3 _, almost surely, the intersection S of two independent Brownian paths in_ R<sup>_d_</sup> _is nontrivial, i.e. contains points other than a possible common starting point._

Remark 9.2. In the case _d ≤_ 3, if the Brownian paths are started in the same point, then _⋄_ almost surely, the paths intersect before any positive time _t >_ 0, see Exercise 9.1 (a).

239

**Proof of (a).** Note that it suffices to look at one Brownian motion and show that its path is, almost surely, a set of capacity zero with respect to the potential kernel. If _d ≥_ 4, the capacity with respect to the potential kernel is a multiple of the Riesz ( _d −_ 2)-capacity. By Theorem 4.27 this capacity is zero for sets of finite ( _d −_ 2)-dimensional Hausdorff measure. Now note that if _d ≥_ 5 the dimension of a Brownian path is two, and hence strictly smaller than _d −_ 2, so that the ( _d −_ 2)-dimensional Hausdorff measure is zero, which shows that the capacity must be zero. If _d_ = 4 the situation is only marginally more complicated, although the dimension of the Brownian path is 2 = _d −_ 2 and the simple argument above does not apply. However, we know from (1.1) in Chapter 4 that _H_<sup>2</sup> ( _B_ [0 _,_ 1]) _< ∞_ almost surely, which implies that Cap2( _B_ [0 _,_ 1]) = 0 by Theorem 4.27. This implies that an independent Brownian motion almost surely does not hit either of the segments _B_ [ _n, n_ + 1], and therefore avoids the path entirely.

**Proof of (b).** If _d_ = 3, the capacity with respect to the potential kernel is a multiple of the Riesz 1-capacity. As the Hausdorff dimension of a path is two, this capacity is positive by Theorem 4.36. Therefore two Brownian paths in _d_ = 3 intersect with positive probability.

Suppose now the two Brownian motions start in different points, we may assume that one is the origin and the other one is denoted _x_ . By rotational invariance, the probability that the paths do not intersect depends only on _|x|_ , and by Brownian scaling we see that it is completely independent of the choice of _x̸_ = 0. Denote this probability by _q_ and, given any _ε >_ 0, choose a large time _t_ such that


Then, using the Markov property,


As _ε >_ 0 was arbitrary, we get _q ≤ q_<sup>2</sup> , and as we know that _q <_ 1 we obtain that _q_ = 0. This shows that two Brownian paths started in different points intersect almost surely. If they start in the same point, by the Markov property,


as required to complete the argument in the case _d_ = 3. A path in _d ≤_ 2 is the projection of a three dimensional path on a lower dimensional subspace, hence if two paths in _d_ = 3 intersect almost surely, then so do two paths in _d_ = 2.

It is equally natural to ask, for integers _p >_ 2 and _d ≤_ 3, whether a collection of _p_ independent _d_ -dimensional Brownian motions


intersect, i.e. whether there exist times _t_ 1 _, . . . , tp >_ 0 such that _B_ 1( _t_ 1) = _· · ·_ = _Bp_ ( _tp_ ).

240

Theorem 9.3.

- (a) _For d ≥_ 3 _, almost surely, three independent Brownian paths in_ R<sup>_d_</sup> _have an empty intersection, except for a possible common starting point._

- (b) _For d_ = 2 _, almost surely, the intersection S of any finite number p of independent Brownian paths in_ R<sup>_d_</sup> _is nontrivial, i.e. contains points other than a possible common starting point._

In the light of our discussion of the case _p_ = 2, it is natural to approach the question about the existence of intersections of _p_ paths, by asking for the Hausdorff dimension and measure of the intersection of _p −_ 1 paths. This leads to an easy proof of (a).

Lemma 9.4. _Suppose S is the intersection of the ranges of two Brownian motions in d_ = 3 _. Then, almost surely, for every compact set_ Λ _⊂_ R<sup>3</sup> _not containing the starting points of the Brownian motions, we have_


**Proof.** Fix a cube Cube _⊂_ R<sup>3</sup> of unit sidelength not containing the starting points. It suffices to show that, almost surely, _H_<sup>1</sup> ( _S ∩_ Cube) _< ∞_ . For this purpose let C _n_ be the collection of dyadic subcubes of Cube of sidelength 2<sup>_−n_</sup> , and I _n_ be the collection of cubes in C _n_ which are hit by both motions. By our hitting estimates, Theorem 3.17, there exists _C >_ 0 such that, for any cube _E ∈_ C _n_ ,


Now, for every _n_ , the collection I _n_ is a covering of _S_ , and


Therefore, by Fatou’s lemma, we obtain


Hence, almost surely, for arbitrarily large values of _n_ we have a covering of _S ∩_ Cube by sets of diameter at most _√_ 32<sup>_−n_</sup> with 1-value no more than _C√_ 3. We infer from this that _H_<sup>1</sup> ( _S ∩_ Cube) _≤ C√_ 3 almost surely, and this completes the proof.

**Proof of Theorem 9.3 (a).** It suffices to show that, for any cube Cube of unit sidelength, which does not contain the origin, we have Cap1( _S ∩_ Cube) = 0. This follows directly from Lemma 9.4 and the energy method, Theorem 4.27.

241

For Theorem 9.3 (b) it would suffice to show that the Hausdorff dimension of the set


is positive in the case _d_ = 2. In fact, it is a natural question to ask for the Hausdorff dimension of the intersection of Brownian paths in any case when the set is nonempty. The problem was raised by Itˆo and McKean in their influential book [ **IM74** ], and has since been resolved by Taylor [ **Ta66** ] and Fristedt [ **Fr67** ]. The nontrivial problem of finding lower bounds for the Hausdorff dimension of the intersection sets is best approached using the technique of _stochastic co-dimension_ , which we discuss now.

**1.2. Stochastic co-dimension and percolation limit sets.** Given a set _A_ , the idea behind the stochastic co-dimension approach is to take a suitable random test set Θ, and check whether P _{_ Θ _∩ A̸_ = _∅}_ is zero or positve. In the latter case this indicates that the set is large, and we should therefore get a lower bound on the dimension of _A_ . A natural choice of such a random test set would be the range of Brownian motion. Recall that, for example in the case _d_ = 3, if P _{_ Range _∩ A̸_ = _∅} >_ 0 is positive, this implies that dim _A ≥_ 1.

Of course, in order to turn this idea into a systematic technique for finding lower bounds for the Hausdorff dimension, an entire family of test sets is needed to tune the size of the test set in order to give sharp bounds. For this purpose, Taylor [ **Ta66** ] used stable processes instead of Brownian motion. This is not the easiest way and also limited, because stable processes only exist across a limited range of parameters. The approach we use in this book is based on using the family of percolation limit sets as test sets.

Suppose that _C ⊂_ R<sup>_d_</sup> is a fixed compact unit cube. We denote by C _n_ the collection of compact dyadic subcubes (relative to _C_ ) of sidelength 2<sup>_−n_</sup> . We also let


Given _γ ∈_ [0 _, d_ ] we construct a random compact set Γ[ _γ_ ] _⊂ C_ inductively as follows: We keep each of the 2<sup>_d_</sup> compact cubes in C1 independently with probability _p_ = 2<sup>_−γ_</sup> . Let S1 be the collection of cubes kept in this procedure and S(1) their union. Pass from S _n_ to S _n_ +1 by keeping each cube of C _n_ +1, which is not contained in a previously rejected cube, independently with probability _p_ . Denote by S =<sup>�</sup><sup>_∞_</sup> _n_ =1<sup>S</sup><sup>_n_andletS(</sup><sup>_n_+ 1)betheunionofthecubesin</sup> S _n_ +1. Then the random set


is called a **percolation limit set** . The usefulness of percolation limit sets in fractal geometry comes from the following theorem.

242

Theorem 9.5 (Hawkes 1981). _For every γ ∈_ [0 _, d_ ] _and every closed set A ⊂ C the following properties hold_

- (i) _if_ dim _A < γ, then almost surely, A ∩_ Γ[ _γ_ ] = _∅,_

- (ii) _if_ dim _A > γ, then A ∩_ Γ[ _γ_ ] _̸_ = _∅ with positive probability,_

- (iii) _if_ dim _A > γ, then_


Remark 9.6. Observe that the first part of the theorem gives a _lower_ bound _γ_ for the Hausdorff dimension of a set _A_ , if we can show that _A ∩_ Γ[ _γ_ ] _̸_ = _∅_ with positive probability. As with so many ideas in fractal geometry one of the roots of this method lies in the study of trees, more _⋄_ precisely percolation on trees, see [ **Ly90** ].

Remark 9.7.

- (a) There is a close kinship of the stochastic co-dimension technique and the energy method: A set _A_ is called _polar for the percolation limit set_ , if


We shall see in Theorem 9.18 that a set is polar for the percolation limit set if and only if it has _γ_ -capacity zero.

- (b) For _d ≥_ 3, the criterion for polarity of a percolation limit set with _γ_ = _d −_ 2 therefore agrees with the criterion for the polarity for Brownian motion. This ‘equivalence’ between percolation limit sets and Brownian motion has a quantitative strengthening which is discussed in Section 2 of this chapter. _⋄_

**Proof of (i) in Hawkes’ theorem.** The proof of part (i) is based on the _first moment method_ , which means that we essentially only have to calculate an expectation. Because dim _A < γ_ there exists, for every _ε >_ 0, a covering of _A_ by countably many sets _D_ 1 _, D_ 2 _, . . ._ with � _∞i_ =1<sup>_|Di|γ<ε_.Aseachsetiscontainedinnomorethanaconstantnumberofdyadiccubes</sup> of smaller diameter, we may even assume that _D_ 1 _, D_ 2 _, . . . ∈_ C. Suppose that the sidelength of _Di_ is 2<sup>_−n_</sup> , then the probability that _Di ∈_ S _n_ is 2<sup>_−nγ_</sup> . By picking from _D_ 1 _, D_ 2 _, . . ._ those cubes which are in S we get a covering of _A ∩_ Γ[ _γ_ ]. Let _N_ be the number of cubes picked in this procedure, then


As this holds for all _ε >_ 0 we infer that, almost surely, we have _A ∩_ Γ[ _γ_ ] = _∅_ .

243

**Proof of (ii) in Hawkes’ theorem.** The proof of part (ii) is based on the _second moment method_ , which means that a variance has to be calculated. We also use the nontrivial part of Frostman’s lemma in the form of Theorem 4.36, which states that, as dim _A > γ_ , there exists a probability measure _µ_ on _A_ such that _Iγ_ ( _µ_ ) _< ∞_ .

Now let _n_ be a positive integer and define the random variables


Note that _Yn >_ 0 implies S( _n_ ) _∩ A̸_ = _∅_ and, by compactness, if _Yn >_ 0 for all _n_ we even have _A ∩_ Γ[ _γ_ ] _̸_ = _∅_ . As _Yn_ +1 _>_ 0 implies _Yn >_ 0, we get that


It therefore suffices to give a positive lower bound for P _{Yn >_ 0 _}_ independent of _n_ . A straightforward calculation gives for the first moment E[ _Yn_ ] =<sup>�</sup> _C∈_ C _n_<sup>_µ_(</sup><sup>_C_)=1.Forthe</sup> second moment we find


The latter probability depends on the dyadic distance of the cubes _C_ and _D_ : if 2<sup>_−m_</sup> is the sidelength of the smallest dyadic cube which contains both _C_ and _D_ , then the probability in question is 2<sup>_−_2</sup><sup>_γ_(</sup><sup>_n−m_)</sup> 2<sup>_−γm_</sup> . The value _m_ can be estimated in terms of the Euclidean distance of the cubes, indeed if _x ∈ C_ and _y ∈ D_ then


This gives a handle to estimate the second moment in terms of the energy of _µ_ . We find that


Plugging these moment estimates into the easy form of the Paley-Zygmund inequality, Lemma 3.22, gives P _{Yn >_ 0 _} ≥ d_<sup>_−γ/_2</sup> _Iγ_ ( _µ_ )<sup>_−_1</sup> _,_ as required.

**Proof of (iii) in Hawkes’ theorem.** For part (iii) note that the intersection Γ[ _γ_ ] _∩_ Γ[ _δ_ ] of two independent percolation limit sets has the same distribution as Γ[ _γ_ + _δ_ ]. Suppose first that _δ >_ dim _A − γ_ . Then, by part (i), _A ∩_ Γ[ _γ_ ] _∩_ Γ[ _δ_ ] = _∅_ almost surely, and hence, by part (ii), dim _A ∩_ Γ[ _γ_ ] _≤ δ_ almost surely. Letting _δ ↓_ dim _A − γ_ completes the proof of part (a).

Now suppose that _δ <_ dim _A − γ_ . Then, with positive probability, ( _A ∩_ Γ[ _γ_ ]) _∩_ Γ[ _δ_ ] _̸_ = _∅_ , by part (ii). And using again part (i) we get that dim _A ∩_ Γ[ _γ_ ] _≥ δ_ with positive probability, completing the proof of part (b).

244

**1.3. Hausdorff dimension of intersections.** We can now use the stochastic codimension approach to find the Hausdorff dimension of the intersection of two Brownian paths, whenever it is nonempty. Note that the following theorem also implies Theorem 9.3 (b).

Theorem 9.8. _Suppose d ≥_ 2 _and p ≥_ 2 _are integers sucht that p_ ( _d −_ 1) _< d. Suppose that {B_ 1( _t_ ) : _t ≥_ 0 _}, . . . , {Bp_ ( _t_ ) : _t ≥_ 0 _}_

_are p independent d-dimensional Brownian motions. Let_ Range _i be the range of {Bi_ ( _t_ ) : _t ≥_ 0 _} for_ 1 _≤ i ≤ p. Then, almost surely,_


Remark 9.9. A good way to make this result plausible is by recalling the situation for the intersection of linear subspaces of R<sup>_d_</sup> : If the spaces are in general position, then the co-dimension of the intersection is the sum of the co-dimensions of the subspaces. As the Hausdorff dimension of a Brownian path is two, the plausible codimension of the intersection of _p_ paths is _p_ ( _d −_ 2), _⋄_ and hence the dimension is _d − p_ ( _d −_ 2).

Remark 9.10. Under assumption of the theorem, if the Brownian paths are started in the same point, then almost surely, dim( _B_ 1[0 _, t_ 1] _∩· · · ∩ Bp_ [0 _, tp_ ]) = _d − p_ ( _d −_ 2) _,_ for any _t_ 1 _, . . . , tp >_ 0, _⋄_ see Exercise 9.1 (b).

Note that, by Lemma 9.4, we have dim(Range1 _∩_ Range2) _≤_ 1 if _d_ = 3, and hence only the lower bounds in Theorem 9.8 remain to be proved. For these we use the stochastic codimension method, but first we provide a useful zero-one law.

Lemma 9.11. _For any γ >_ 0 _the probability of the event_


_is either zero or one, and independent of the starting points of the Brownian motions._

**Proof.** For _t ∈_ (0 _, ∞_ ] denote by


and let


We start by considering the case that all Brownian motions start at the origin. Then, by monotonicity of the events,


The event on the left hand side is in the germ- _σ_ -algebra and hence, by Blumenthal’s zero-one law, has probability zero or one. By scaling, however, _p_ ( _t_ ) does not depend on _t_ at all, so we have either _p_ ( _t_ ) = 0 for all _t >_ 0 or _p_ ( _t_ ) = 1 for all _t >_ 0.

245

In the first case we note that, by the Markov property applied at times _t_ 1 _, . . . , tp_ ,


where _µ_ is the product of _p_ independent centred, normally distributed random variables with variances _t_ . Therefore P _{_ dim _S_ ( _∞_ ) _≥ γ}_ = 0 for _Lpd_ -almost every vector of starting points. Finally, for an arbitrary configuration of starting points,


A completely analogous argument can be carried out for the second case.

**Proof of Theorem 9.8.** First we look at _d_ = 3 and _p_ = 2. Suppose _γ <_ 1 is arbitrary, and pick _β >_ 1 such that _γ_ + _β <_ 2. Let Γ[ _γ_ ] and Γ[ _β_ ] by two independent percolation limit sets, indepedendent of the Brownian motions. Note that then Γ[ _γ_ ] _∩_ Γ[ _β_ ] is a percolation limit set with parameter _γ_ + _β_ . Hence, by Theorem 9.5 (ii) and the fact that dim(Range1) = 2 _> γ_ + _β_ , we have


Interpreting Γ[ _β_ ] as the test set and using Theorem 9.5 (i) we obtain


As _β >_ 1, given this event, the set Range1 _∩_ Γ[ _γ_ ] has positive capacity with respect to the potential kernel in R<sup>3</sup> and is therefore nonpolar with respect to the independent Brownian motion _{B_ 2( _t_ ): _t ≥_ 0 _}_ . We therefore have


Using Theorem 9.5 (i) we infer that dim(Range1 _∩_ Range2) _≥ γ_ with positive probability. Lemma 9.11 shows that this must in fact hold almost surely, and the result follows as _γ <_ 1 was arbitrary.

Second we look at _d_ = 3 and any _p ≥_ 2. Suppose _γ <_ 2 is arbitrary, and pick _β_ 1 _, . . . , βp >_ 0 such that _γ_ + _β_ 1 + _· · ·_ + _βp <_ 2. Let Γ[ _γ_ ] and Γ[ _β_ 1] _, . . . ,_ Γ[ _βp_ ] be independent percolation limit sets, indepedendent of the _p_ Brownian motions. Note that then


is a percolation limit set with parameter _γ_ + _β_ 1 + _· · ·_ + _βp_ . Hence, by Theorem 9.5 (ii) and the fact that dim(Range1) = 2 _> γ_ + _β_ 1 + _· · ·_ + _βp_ , we have


246

Interpreting Γ[ _βp_ ] as the test set and using Theorem 9.5 (i) we obtain


As _βp >_ 0, given this event, the set


has positive capacity with respect to the potential kernel in R<sup>2</sup> and is therefore nonpolar with respect to the independent Brownian motion _{B_ 2( _t_ ): _t ≥_ 0 _}_ . We therefore have


Iterating this procedure _p −_ 1 times we obtain


Using Theorem 9.5 (i) we infer that dim(<sup>�</sup><sup>_p_</sup> _i_ =1<sup>Range</sup> _i_<sup>)</sup> _≥ γ_ with positive probability. Lemma 9.11 shows that this must in fact hold almost surely, and the result follows as _γ <_ 2 was arbitrary.

### **2. Intersection equivalence of Brownian motion and percolation limit sets**

The idea of quantitative estimates of hitting probabilities, has a natural extension: two random sets may be called _intersection-equivalent_ , if their hitting probabilities for a large class of test sets are comparable. This concept of equivalence allows surprising relationships between random sets which, at first sight, might not have much in common. In this section we establish intersection-equivalence between Brownian motion and suitably defined percolation limit sets, and use this to characterise the polar sets for the intersection of Brownian paths.

We start the discussion by formalising the idea of intersection-equivalence.

Definition 9.12. _Two random closed sets A and B in_ R<sup>_d_</sup> _are_ **intersection-equivalent** _in the compact set U , if there exist two positive constants c, C such that, for any closed set_ Λ _⊂ U ,_ (2.1) _c_ P _{A ∩_ Λ _̸_ = _∅} ≤_ P _{B ∩_ Λ _̸_ = _∅} ≤ C_ P _{A ∩_ Λ _̸_ = _∅}._

_Using the symbol a ≍ b to indicate that the ratio of a and b is bounded from above and below by positive constants which do not depend on_ Λ _we can write this as_


Remark 9.13. Let _G_ be the collection of all closed subsets of R<sup>_d_</sup> . Formally, we define a random closed set as a mapping _A_ : Ω _→G_ such that, for every compact Λ _⊂_ R<sup>_d_</sup> , the set _⋄ {ω_ : _A_ ( _ω_ ) _∩_ Λ = _∅}_ is measurable.

247

The philosophy of the main result of this section is that we would like to find a class of particularly simple sets, which are intersection-equivalent to the paths of transient Brownian motion. If these sets are easier to study, we can ‘translate’ easy results about the simple sets into hard ones for Brownian motion.

A good candidate for these simple sets are percolation limit sets: they have excellent features of _self-similarity_ and _independence_ between the fine structures in different parts. Many of their properties can be obtained from classical facts about Galton-Watson branching processes.

We introduce percolation limit sets with _generation dependent_ retention probabilities. Denote by C _n_ the compact dyadic cubes of sidelength 2<sup>_−n_</sup> . For any sequence _p_ 1 _, p_ 2 _, . . ._ in (0 _,_ 1) we define families S _n_ of compact dyadic cubes inductively by including any cube in C _n_ which is not contained in a previously rejected cube, independently with probability _pn_ . Define


to be the **percolation limit set** for the sequence _p_ 1 _, p_ 2 _, . . ._ .

To find a suitable sequence of retention probabilities we compare the hitting probabilities of dyadic cubes by a percolation limit set on the one hand and a transient Brownian on the other. (This is obviously necessary to establish intersection-equivalence). We assume that percolation is performed in a cube Cube at positive distance from the origin, at which a transient Brownian motion is started. Supposing for the moment that the retention probabilities are such that the survival probability of any retained cube is bounded from below, for any cube _Q ∈_ C _n_ , the hitting estimates for the percolation limit set are


By Theorem 8.23, on the other hand,


for the radial potential


where we have chosen basis 2 for the logarithm for convenience of this argument. When we choose the sequence _p_ 1 _, p_ 2 _, . . ._ of retention probabilities such that _p_ 1 _· · · pn_ = 1 _/f_ (2<sup>_−n_</sup> ). More explicitly, we choose _p_ 1 = 2<sup>2</sup><sup>_−d_</sup> and, for _n ≥_ 2,


The retention probabilities are constant for _d ≥_ 3, but generation dependent for _d_ = 2.

Theorem 9.14. _Let {B_ ( _t_ ): 0 _≤ t ≤ T } denote transient Brownian motion started in the origin, and_ Cube _⊂_ R<sup>_d_</sup> _a compact cube of unit sidelength not containing the origin. Let_ Γ _be a percolation limit set in_ Cube _with retention probabilities chosen as in_ (2.2) _. Then the range of the Brownian motion is intersection-equivalent to the percolation limit set_ Γ _in the cube_ Cube _._

248

Before discussing the proof, we look at an application of Theorem 9.14 to our understanding of Brownian motion. We first make two easy observations.

Lemma 9.15. _Suppose that A_ 1 _, . . . , Ak, F_ 1 _, . . . , Fk are independent random closed sets, with Ai intersection-equivalent to Fi for_ 1 _≤ i ≤ k. Then A_ 1 _∩ A_ 2 _∩ . . . ∩ Ak is intersection-equivalent to F_ 1 _∩ F_ 2 _∩ . . . ∩ Fk._

**Proof.** By induction, we can reduce this to the case _k_ = 2. It then clearly suffices to show that _A_ 1 _∩ A_ 2 is intersection-equivalent to _F_ 1 _∩ A_ 2. This is done by conditioning on _A_ 2,


Lemma 9.16. _For independent percolation limit sets_ Γ1 _and_ Γ2 _with retention probabilities p_ 1 _, p_ 2 _, . . . and q_ 1 _, q_ 2 _, . . ., respectively, their intersection_ Γ1 _∩_ Γ2 _is a percolation limit set with retention probabilities p_ 1 _q_ 1 _, p_ 2 _q_ 2 _, . . .._

**Proof.** This is obvious from the definition of percolation limit sets and independence.

These results enable us to recover the results about existence of intersection of Brownian paths from the survival criteria of Galton-Watson trees. As an example look at the intersection of two Brownian paths in R<sup>_d_</sup> , _d ≥_ 3. By Theorem 9.14 and Lemma 9.15, the intersection of these paths is intersection-equivalent (in any unit cube not containing the starting points) to the intersection of two independent percolation limit sets with constant retention parameters _p_ = 2<sup>2</sup><sup>_−d_</sup> . This intersection, by Lemma 9.16, is another percolation limit set, but now with parameter _p_<sup>2</sup> = 2<sup>4</sup><sup>_−_2</sup><sup>_d_</sup> . Now observe that this set has a positive probability of being nonempty if and only if a Galton-Watson process with binomial offspring distribution with parameters _n_ = 2<sup>_d_</sup> and _p_ = 2<sup>4</sup><sup>_−_2</sup><sup>_d_</sup> has a positive survival probability. This is the case if and only if the mean offspring number _np_ strictly exceeds 1, i.e. if 4 _− d >_ 0. In other words, in _d_ = 3 the two paths intersect with positive probability, in all higher dimensions they almost surely do not intersect.

We now give the proof of Theorem 9.14. A key rˆole in the proof is played by a fundamental result of R. Lyons concerning survival probabilities of general trees under the percolation process, which has great formal similarity with the quantitative hitting estimates for Brownian paths of Theorem 8.23.

Recall the notation for trees from Page 112. As usual we define, for any kernel _K_ : _∂T × ∂T →_ [0 _, ∞_ ], the _K_ -energy of the measure _µ_ on _∂T_ as


and the _K_ -capacity of the boundary of the tree by


249

Given a sequence _p_ 1 _, p_ 2 _, . . ._ of probabilities, _percolation_ on _T_ is obtained by removing each edge of _T_ of order _n_ independently with probability 1 _− pn_ and retaining it otherwise, with mutual independence among edges. Say that a ray _ξ_ **survives the percolation** if all the edges on _ξ_ are retained, and say that the tree boundary _∂T_ survives if some ray of _T_ survives.

Theorem 9.17 (Lyons). _If percolation with retention probabilities p_ 1 _, p_ 2 _, . . . is performed on a rooted tree T , then_


**Proof.** For two vertices _v, w_ we write _v ↔ w_ if the shortest path between the vertices is retained in the percolation. We also write _v ↔ ∂T_ if a ray through vertex _v_ survives the percolation and _v ↔ Tn_ if there is a self-avoiding path of retained edges connecting _v_ to a vertex of generation _n_ . Note that _K_ ( _x, y_ ) = P _{ρ ↔ x ∧ y}_<sup>_−_1</sup> by definition of the kernel _K_ . By the finiteness of the degrees,


We start with the left inequality in (2.3) and consider the case of a finite tree _T_ first. We extend the definition of the boundary _∂T_ to finite trees by letting _∂T_ be the set of leaves, i.e., the vertices with no offspring. Let _µ_ be a probability measure on _∂T_ and set


Thus,


Using the Paley-Zygmund inequality in the second step, we obtain


The left-hand side does not depend on _µ_ , so optimising the right-hand side over _µ_ yields


250

which proves the lower bound for finite trees. For _T_ infinite, let _µ_ be any probability measure on _∂T_ . This induces a probability measure _µ_ � on the set _Tn_ , consisting of those vertices which become leaves when the tree _T_ is cut off after the _n_<sup>th</sup> generation, by letting


By the finite case considered above,


Each ray _ξ_ must pass through some vertex _x ∈ Tn_ . This implies that _K_ ( _x, y_ ) _≤ K_ ( _ξ, η_ ) for _x ∈ ξ_ and _y ∈ η_ . Therefore,


Hence P _{ρ ↔ Tn} ≥ IK_ ( _µ_ )<sup>_−_1</sup> for any probability measure _µ_ on _∂T_ . Optimising over _µ_ and passing to the limit as _n →∞_ , we get P _{ρ ↔ ∂T } ≥_ Cap _K_ ( _∂T_ ) _._

It remains to prove the right-hand inequality in (2.3). Assume first that _T_ is finite. There is a Markov chain _{Vk_ : _k ∈_ N _}_ hiding here: Suppose the offspring of each individual is ordered from left to right, and note that this imposes a natural order on all vertices of the tree by saying that _x_ is to the left of _y_ if there are siblings _v_ , _w_ with _v_ to the left of _w_ , such that _x_ is a descendant of _v_ and _y_ is a descendant of _w_ . The random set of leaves that survive the percolation may thus be enumerated from left to right as _V_ 1 _, V_ 2 _, . . . , Vr_ . The key observation is that the random sequence _ρ, V_ 1 _, V_ 2 _, . . . , Vr,_ ∆ _,_ ∆ _, . . ._ is a Markov chain on the state space _∂T ∪{ρ,_ ∆ _}_ , where _ρ_ is the root and ∆is a formal absorbing cemetery.

Indeed, given that _Vk_ = _x_ , all the edges on the unique path from _ρ_ to _x_ are retained, so that survival of leaves to the right of _x_ is determined by the edges strictly to the right of the path from _ρ_ to _x_ , and is thus conditionally independent of _V_ 1 _, . . . , Vk−_ 1, see Figure 1.

This verifies the Markov property, so Proposition 8.25 may be applied. The transition probabilities for the Markov chain above are complicated, but it is easy to write down the Green kernel _G_ . For any vertex _x_ let `path` ( _x_ ) be the set of edges on the shortest path from _ρ_ to _x_ . Clearly, _G_ ( _ρ, y_ ) equals the probability that _y_ survives percolation, so


If _x_ is to the left of _y_ , then _G_ ( _x, y_ ) is equal to the probability that the range of the Markov chain contains _y_ given that it contains _x_ , which is just the probability of _y_ surviving given that _x_ survives. Therefore,


and hence


251


<!-- Start of picture text -->
ρ<br><!-- End of picture text -->

Figure 1. The Markov chain embedded in the tree.

Now _G_ ( _x, y_ ) = 0 for _x_ on the right of _y_ ; thus (keeping the diagonal in mind)

_K_ ( _x, y_ ) _≤ M_ ( _x, y_ ) + _M_ ( _y, x_ )

for all _x, y ∈ ∂T_ , and therefore _IK_ ( _µ_ ) _≤_ 2 _IM_ ( _µ_ ) _._ Now apply Proposition 8.25 to Λ = _∂T_ :

Cap _K_ ( _∂T_ ) _≥_<sup><u>1</u></sup> 2<sup>Cap</sup><sup>_M_(</sup><sup>_∂T_)</sup><sup>_≥_</sup><sup><u>1</u></sup> 2<sup>P</sup> � _{Vk_ : _k ∈_ N _}_ hits _∂T_ � = 2<sup><u>1</u>P</sup><sup>_{ρ ↔∂T} ._</sup>

This establishes the upper bound for finite _T_ . The inequality for general _T_ follows from the finite case by taking limits.

The main remaining task is to translate Lyons’ theorem, Theorem 9.17 into hitting estimates for percolation limit sets using a ‘tree representation’ as in Figure 2, and relating the capacity of the tree boundary to the capacity of the percolation limit set.

Theorem 9.18. _Let_ Γ _be a percolation limit set in the unit cube_ Cube _with retention parameters p_ 1 _, p_ 2 _, . . .. Then, for any closed set_ Λ _⊂_ Cube _we have_


_for any decreasing f satisfying f_ (2<sup>_−k_</sup> ) = _p_ 1<sup>_−_1</sup><sup>_· · · p−_</sup> _k_<sup>1</sup><sup>_._</sup>

Remark 9.19. This result extends parts (i) and (ii) in Hawkes’ theorem, Theorem 9.5, in two ways: It includes generation dependent retention and gives a quantitative estimate. _⋄_

The key to this lemma is the following representation for the _f_ -energy of a measure.

252


Figure 2. Percolation limit set and associated tree

Lemma 9.20. _Suppose f_ : (0 _, ∞_ ) _→_ (0 _, ∞_ ) _is a decreasing function, and denote h_ ( _n_ ) = _f_ (2<sup>_−n_</sup> ) _− f_ (2<sup>1</sup><sup>_−n_</sup> ) _for n ≥_ 1 _, and h_ (0) = _f_ (1) _. Then, for any measure µ on the unit cube_ [0 _,_ 1)<sup>_d_</sup> _,_


_where the implied constants depend only on d._

**Proof of the lower bound in Lemma 9.20.** Fix an integer _ℓ_ such that _√d ≤_ 2<sup>_ℓ_</sup> . For any _x, y ∈_ [0 _,_ 1]<sup>_d_</sup> we write _n_ ( _x, y_ ) = max � _n_ : _x, y ∈ D_ for some _D ∈_ D _n_ � _._ Note that _n_ ( _x, y_ ) = _n_ + _ℓ_ implies _| x − y| ≤ √d_ 2<sup>_−n−ℓ_</sup> _≤_ 2<sup>_−n_</sup> and hence _f_ ( _| x − y|_ ) _≥ f_ (2<sup>_−n_</sup> ). We thus get


Rearranging the sum and using this _ℓ_ times, we obtain that


which is our statement with _c_ = 2<sup>_−dℓ_</sup> .

253

**Proof of the upper bound in Lemma 9.20.** For 2<sup>1</sup><sup>_−n_</sup> _≥| x − y| >_ 2<sup>_−n_</sup> , we have


and hence we can decompose the integral as


For cubes _Q_ 1 _, Q_ 2 _∈_ D _n_ we write _Q_ 1 _∼ Q_ 2 is they are either adjacent or they agree (though note that _∼_ is not an equivalence relation). Then


using the inequality of the geometric and arithmetic mean in the last step. As, for each cube, the number of adjacent or identical dyadic cubes of the same sidelength is 3<sup>_d_</sup> , we obtain that


using (2.4) from above. This completes the proof of the upper bound.

**Proof.** Denote the coordinatewise minimum of Cube by _x_ . We employ the canonical mapping _R_ from the boundary of a 2<sup>_d_</sup> -ary tree Υ, where every vertex has 2<sup>_d_</sup> children, to the cube Cube. Formally, label the edges from each vertex to its children in a one-to-one manner with the vectors in Θ = _{_ 0 _,_ 1 _}_<sup>_d_</sup> . Then the boundary _∂_ Υ is identified with the sequence space Θ<sup>Z+</sup> and we define _R_ : _∂_ Υ = Θ<sup>Z+</sup> _→_ Cube by


We now use the representation given in Lemma 9.20 to relate the _K_ -energy of a measure _µ_ on _∂T_ (with _K_ as in Theorem 9.17) to the _f_ -energy of its image measure _µ ◦R_<sup>_−_1</sup> on Cube, showing that


254

where the implied constants depend only on the dimension _d_ . Indeed the _K_ -energy of a measure _µ_ on _∂T_ satisfies, by definition,


whereas the _f_ -energy of the measure _µ ◦R_<sup>_−_1</sup> satisfies, by Lemma 9.20,


where


by our assumptions on _f_ . Now _R_<sup>_−_1</sup> ( _D_ ) is contained in no more than 3<sup>_d_</sup> sets of the form _{ξ ∈ ∂T_ : _v ∈ ξ_ �, for _|v|_ = _k_ , in such a way that over all cubes _D ∈_ D _k_ no such set is used in more than 3<sup>_d_</sup> covers. Conversely each set _R_<sup>_−_1</sup> ( _D_ ) contains an individual set of this form entirely, so that we obtain (2.5).

As any measure _ν_ on _R_ ( _∂T_ ) _⊂_ Cube can be written as _µ ◦R_<sup>_−_1</sup> for an appropriate measure _µ_ on _∂T_ it follows from (2.5) that Cap _K_ ( _∂T_ ) _≍_ Cap _f_ ( _R_ ( _∂T_ )) _._ Any closed set Λ in the unit cube Cube can be written as the image _R_ ( _∂T_ ) of the boundary of some subtree _T_ of the regular 2<sup>_d_</sup> -ary tree. We perform percolation with retention parameters _p_ 1 _, p_ 2 _, . . ._ on this tree. Then, by Theorem 9.17,


**Proof of Theorem 9.14.** As the cube Cube has positive distance to the starting point of Brownian motion, we can remove the denominator and smaller order terms from the Martin kernel in Theorem 8.23, as in the proof of Theorem 8.19. We thus obtain


where _f_ is the radial potential. For the choice of retention probabilities in (2.2) we can apply Theorem 9.18, which implies


and combining the two displays gives the result.

255

The intersection-equivalence approach enables us to characterise the polar sets for the intersection of _p_ independent Brownian motions in R<sup>_d_</sup> and give a quantitative estimate of the hitting probabilities.

Theorem 9.21. _Let B_ 1 _, . . . , Bp be independent Brownian motions in_ R<sup>_d_</sup> _starting in arbitrary fixed points and suppose p_ ( _d −_ 2) _< d. Let_


_Then, for any closed set_ Λ _, we have_


_where f is the radial potential._

**Proof.** We may assume that Λ is contained in a unit cube at positive distance from the starting points. Let Γ be a percolation limit set in that cube, with retention probabilities _p_ 1 _, p_ 2 _, . . ._ satisfying _p_ 1 _· · · pn_ = 1 _/f_<sup>_p_</sup> (2<sup>_−n_</sup> ). By Theorem 9.14 and Lemma 9.15, the random set _S_ is intersection-equivalent to Γ in that cube. Theorem 9.18 characterises the polar sets for Γ, completing the argument.

### **3. Multiple points of Brownian paths**

The results of the previous section also provide the complete answer to the question of the existence of _p_ -fold multiple points of _d_ -dimensional Brownian motion. This is achived by

Theorem 9.22. _Suppose d ≥_ 2 _and {B_ ( _t_ ) : _t ∈_ [0 _,_ 1] _} is a d-dimensional Brownian motion. Then, almost surely,_

- _if d ≥_ 4 _no double points exist, i.e. Brownian motion is injective,_

- _if d_ = 3 _double points exist, but triple points fail to exist,_

- _if d_ = 2 _points of any finite multiplicity exist._

**Proof.** To show _nonexistence_ of double points in _d ≥_ 4 we divide, for every _n ∈_ N the interval [0 _,_ 1) into 2<sup>_n_</sup> equal subintervals of the form [ _k_ 2<sup>_−n_</sup> _,_ ( _k_ + 1)2<sup>_−n_</sup> ). Note that, for all _s, t ∈_ [0 _,_ 1) with _s < t_ there exists a unique _n ∈_ N and _k ∈{_ 1 _, . . . ,_ 2<sup>_n_</sup> _−_ 1 _}_ with _s ∈_ [( _k −_ 1)2<sup>_−n_</sup> _, k_ 2<sup>_−n_</sup> ) and _t ∈_ [ _k_ 2<sup>_−n_</sup> _,_ ( _k_ + 1)2<sup>_−n_</sup> ), see Figure 3.

The Brownian motions _{B_ 1( _t_ ) : 0 _≤ t ≤_ 2<sup>_−n_</sup> _}_ and _{B_ 2( _t_ ) : 0 _≤ t ≤_ 2<sup>_−n_</sup> _}_ given by


are independent and hence, by Theorem 9.1, they do not intersect, almost surely. Hence for each pair [( _k −_ 1)2<sup>_−n_</sup> _, k_ 2<sup>_−n_</sup> ), [ _k_ 2<sup>_−n_</sup> _,_ ( _k_ + 1)2<sup>_−n_</sup> ) of intervals, almost surely, there is no _s ∈_ [( _k −_ 1)2<sup>_−n_</sup> _, k_ 2<sup>_−n_</sup> ) and _t ∈_ [ _k_ 2<sup>_−n_</sup> _,_ ( _k_ +1)2<sup>_−n_</sup> ) with _B_ ( _s_ ) = _B_ ( _t_ ). As this holds almost surely simultaneously for all pairs of intervals and all _n_ , we note that there exists no _s, t ∈_ [0 _,_ 1) with _s̸_ = _t_ but _B_ ( _s_ ) = _B_ ( _t_ ).

256


<!-- Start of picture text -->
s<br>1<br>3/4<br>1/2<br>1/4<br>t<br>0 1/4 1/2 3/4 1<br><!-- End of picture text -->

Figure 3. Exhausting the triangle _{_ ( _s, t_ ) _∈_ [0 _,_ 1)<sup>2</sup> _, s < t}_ by squares of the form [( _k −_ 1)2<sup>_−n_</sup> _, k_ 2<sup>_−n_</sup> ) _×_ [ _k_ 2<sup>_n_</sup> _,_ ( _k_ + 1)2<sup>_n_</sup> ).

To show _existence_ of double points in _d ≤_ 3 we fix an arbitrary pair of adjacent intervals, say

[( _k −_ 1)2<sup>_−n_</sup> _, k_ 2<sup>_−n_</sup> ) and [ _k_ 2<sup>_−n_</sup> _,_ ( _k_ + 1)2<sup>_−n_</sup> ) _._

We apply Theorem 9.1 in conjunction with Remark 9.2, to the independent Brownian motions _{B_ 1( _t_ ) : 0 _≤ t ≤_ 2<sup>_−n_</sup> _}_ and _{B_ 2( _t_ ) : 0 _≤ t ≤_ 2<sup>_−n_</sup> _}_ given by


to see that, almost surely, the two ranges intersect.

To show nonexistence of triple points in _d_ = 3 we observe that it suffices to show that for any four rationals 0 _< α_ 1 _< α_ 2 _< α_ 3 _< α_ 4 _<_ 1, almost surely there is no 0 _< s < α_ 1, _α_ 2 _< t < α_ 3, _α_ 4 _< u <_ 1 with _B_ ( _s_ ) = _B_ ( _t_ ) = _B_ ( _u_ ).

Fix four rationals as above and denote by _µ_ the law of the vector


Obviously this law has a bounded density with respect to a vector ( _X_ 1 _, X_ 2 _, X_ 3 _, X_ 4) of independent standard normal random variables with variances _α_ 1 _, α_ 2 _, α_ 3 _, α_ 4. Denoting the upper bound by _C >_ 0, we obtain


where the last expectation is with respect to the vector ( _X_ 1 _, X_ 2 _, X_ 3 _, X_ 4). It is easy to see, for example from L´evy’s construction of Brownian motion on an interval, that this expectation

257

equals


where _B_ 1 _, B_ 2 _, B_ 3 are three independent Brownian motions. Hence Theorem 9.3 shows that the probability is zero, and therefore there are no triple points of Brownian motion in _d_ = 3.

To show the existence of _p_ -multiple points in R<sup>2</sup> fix numbers


and let _µ_ the law of the vector


This law has a density with respect to a vector ( _X_ 1 _, . . . , X_ 2 _p_ ) of independent standard normal random variables with variances _α_ 1 _, . . . α_ 2 _p_ , which is bounded from below, say by _c >_ 0. Hence, with _α_ 0 := 0,


where the last expectation is with respect to the vector ( _X_ 1 _, . . . , X_ 2 _p_ ). The last exepctation equals


Hence, for every _ε >_ 0, _p_ -fold self-intersections of the Brownian path occur before time _ε_ with positive probability. By Brownian scaling this probability does not depend on _ε >_ 0, and therefore also the event that _p_ -fold self-intersection occur before any positive time has positive probability. As this event is in the germ- _σ_ -algebra, Blumenthal’s zero-one law implies that its probaility must be one, which completes the proof.

Theorem 9.23. _Let {B_ ( _t_ ) : 0 _≤ t ≤_ 1 _} be a planar Brownian motion. Then, almost surely, for every positive integer p, there exists points x ∈_ R<sup>2</sup> _which are visited_ exactly _p times by the Brownian motion._

**Proof.** Note first that it suffices to show this with positive probability. Indeed, by Brownian scaling, the probability that the path _{B_ ( _t_ ) : 0 _≤ t ≤ r}_ has points of multiplicity exactly _p_ does not depend on _r_ . By Blumenthal’s zero-one law it therefore must be zero or one.

258

The idea of the proof is now to construct a set Λ such that Cap _f p_ (Λ) _>_ 0 but Cap _f p_ +1(Λ) = 0 for the radial potential _f_ . By Exercise 9.2 the first condition implies that the probability that Λ contains a _p_ -fold multiple point is positive. The second conditon ensures that it almost surely does not contain a _p_ + 1-fold multiple point. Hence the _p_ -multiple points found in Λ must be strictly _p_ -multiple.

We construct the set Λ by iteration, starting from a compact unit cube Cube. In the _n_<sup>th</sup> construction step we divide each cube retained in the previous step into its four nonoverlapping dyadic subcubes and retain only one of them, say the bottom left cube, except at the steps with number


when we retain all four subcubes. The number _k_ ( _n_ ) of times within the first _n_ steps when we have retained all four cubes satisfies _k_ ( _n_ ) _≍_ (log _n_ ) log 4<sup>_<u>p</u>_</sup><sup><u>+1</u>.DenotingbyS</sup><sup>_n_thesetofalldyadic</sup> cubes retained in the _n_<sup>th</sup> step, we define the compact set


The calculation of the capacity of Λ will be based on the formula given in Lemma 9.20. Observe that, if _f_<sup>_p_</sup> ( _ε_ ) = log<sup>_p_</sup> (1 _/ε_ ) is the _p_<sup>th</sup> power of the 2-dimensional radial potential, then the associated function is


Note that the number _g_ ( _n_ ) of cubes kept in the first _n_ steps of the construction satisfies _g_ ( _n_ ) _≍ n_<sup>_p_+1</sup> . By our construction<sup>�</sup><sup>_∞_</sup> _n_ =0<sup>_np−_1</sup><sup>_g_(</sup><sup>_n_)</sup><sup>_−_1</sup><sup>_<∞_,but�</sup><sup>_∞_</sup> _n_ =0<sup>_np g_(</sup><sup>_n_)</sup><sup>_−_1=</sup><sup>_∞_.Forthe</sup> measure _µ_ distributing the unit mass equally among the retained cubes of the same sidelength (hence giving mass _g_ ( _n_ )<sup>_−_1</sup> to each retained cube), we have


and hence Cap _f p_ (Λ) _>_ 0. For the converse statement, note that the equidistributing measure _µ_ minimises the sum<sup>�</sup> _Q∈_ D _n_<sup>_ν_(</sup><sup>_Q_)2overallprobabilitymeasures</sup><sup>_ν_chargingonlytheretained</sup> cubes. Hence, for any probability measure on Λ,


verifying that Cap _f p_ +1(Λ) = 0. This completes the proof.

Knowing that planar Brownian motion has points of arbitrarily large _finite_ multiplicity, it is an interesting question whether there are points of _infinite_ multiplicity.

Theorem* 9.24. _Let {B_ ( _t_ ) : _t ≥_ 0 _} be a planar Brownian motion. Then, almost surely, there exists a point x ∈_ R<sup>2</sup> _such that the set {t ≥_ 0 : _B_ ( _t_ ) = _x} is uncountable._

259

The rest of this section is devoted to the proof of this nontrivial result and will not be used in the remainder of the book. It may be skipped on first reading.

Let us first describe the rough strategy of the proof: We start with a double point, i.e. some _s_ 1 _< s_ 2 such that _B_ ( _s_ 1) = _B_ ( _s_ 2) and suppose _s_ 1 and _s_ 2 are not too close. Forgetting that such times are necessarily random times, we could argue that for a small _ε_ 1 _>_ 0 the four independent Brownian motions


which all start in the origin, have a point of intersection with probability one. Hence there existed a quadruple point, i.e. times _t_ 1 _< t_ 2 _< t_ 3 _< t_ 4 with _B_ ( _t_ 1) = _B_ ( _t_ 2) = _B_ ( _t_ 3) = _B_ ( _t_ 4).

Again under the false assumption that these times are fixed, we could iterate this argument with a very small _ε_ 2. Inductively we would construct a sequence _xn_ of points of multiplicity 2<sup>_n_</sup> converging to some _x_ . Consider the set of times where Brownian motion visits this point. In the closure of each of the 2<sup>_n_</sup> disjoint time intervals of length _εn_ , on which the 2<sup>_n_</sup> Brownian motions of the _n_<sup>th</sup> stage are defined, there is a time _t_ with _B_ ( _t_ ) = _x_ . Hence there must be at least as many such times as rays in a binary tree, i.e. uncountably many.

While this idea is nice, it cannot be applied directly: we cannot choose the intersection times as stopping times, or even fixed times, for our Brownian motions. In the proof we therefore replace the intersection times by the hitting times of small balls, which are stopping times. However when moving from stage _n_ to stage _n_ + 1 we only have a 2<sup>_n_+1</sup> -fold intersection with _positive_ probability, not with probability one. We therefore need to do this simultaneously for many balls and obtain a high probability of intersection by an additional _law of large numbers_ effect.

Throughout the proof we use the following notation. For any open or closed sets _A_ 1 _, A_ 2 _, . . ._ and a Brownian motion _B_ : [0 _, ∞_ ) _→_ R<sup>2</sup> define stopping times


where, as usual, the infimum over the empty set is set to infinity. We say the Brownian motion _upcrosses the shell B_ ( _x,_ 2 _r_ ) _\ B_ ( _x, r_ ) _twice_ before a stopping time _T_ if,


We call the paths of Brownian motion between times _τ_ ( _B_ ( _x, r_ )) and _τ_ ( _B_ ( _x, r_ ) _, B_ ( _x,_ 2 _r_ )<sup>_c_</sup> ) and between times _τ_ ( _B_ ( _x, r_ ) _, B_ ( _x,_ 2 _r_ )<sup>_c_</sup> _, B_ ( _x, r_ )) and _τ_ ( _B_ ( _x, r_ ) _, B_ ( _x,_ 2 _r_ )<sup>_c_</sup> _, B_ ( _x, r_ ) _, B_ ( _x,_ 2 _r_ )<sup>_c_</sup> ) the _upcrossing excursions_ , see Figure 4.

From now on let _T_ be the first exit time of Brownian motion from the unit ball. Recall the following fact from Theorem 8.23 and the discussion of the Martin kernels in Chapter 8.

Lemma 9.25. _Let_ 1 _< m < n be two integers and B be a ball of radius_ 2<sup>_−n_</sup> _with centre at distance at least_ 2<sup>_−m_</sup> _and at most_ 2<sup>1</sup><sup>_−m_</sup> _from the origin. Then, for sufficiently large m, we have_


260


<!-- Start of picture text -->
B<br>(2)<br>B<br>B (1)<br><!-- End of picture text -->

Figure 4. The path _B_ : [0 _, ∞_ ) _→_ R<sup>2</sup> upcrosses the shell twice; the upcrossing excursions are bold and marked _B_<sup>(1)</sup> , _B_<sup>(2)</sup> .

Recall from Theorem 3.43 that the density of _B_ ( _T_ ) under P _z_ is given by the Poisson kernel, which is


Lemma 9.26. _Consider Brownian motion started at z ∈B_ (0 _, r_ ) _where r <_ 1 _, and stopped at time T when it exits the unit ball. Let τ ≤ T be a stopping time, and let A ∈F_ ( _τ_ ) _. Then we have_


**Proof.** (i) Let _I ⊂ ∂B_ (0 _,_ 1) be a Borel set. Using the strong Markov property in the second step, we get


As a function of _I_ , both sides of the equation define a finite measure with total mass P _z_ ( _A_ ). Comparing the densities of the measures with respect to the surface measure on _∂B_ (0 _,_ 1) gives

P _z_ � _A_ �� _B_ ( _T_ )� _P_ ( _z, B_ ( _T_ )) = P _z_ ( _A_ ) E _z_ � _P_ ( _B_ ( _τ_ ) _, B_ ( _T_ )) �� _A_ � _._

(ii) The assumption of this part and (i) imply that the ratio P _z_ ( _A|B_ ( _T_ )) _/_ P _z_ ( _A_ ) can be written as an average of ratios _P_ ( _u, w_ ) _/P_ ( _z, w_ ) where _w_ = _B_ ( _T_ ) _∈ ∂B_ (0 _,_ 1) and _u, z ∈B_ (0 _, r_ ). The assertion follows by finding the minimum and maximum of _P_ ( _u, w_ ) as _u_ ranges over _B_ (0 _, r_ ).

The following lemma, concerning the common upcrossings of _L_ Brownian excursions, will be the engine driving the proof of Theorem 9.24.

261

Lemma 9.27. _Let n >_ 5 _and let {x_ 1 _, . . . , x_ 4 _n−_ 5 _} be points such that the balls B_ ( _xi,_ 2<sup>1</sup><sup>_−n_</sup> ) _are disjoint and contained in the shell {z_ : <u>14</u><sup>_≤|z|≤_</sup> <u>34</u><sup>_}.ConsiderLindependentBrownian_</sup> _upcrossing excursions W_ 1 _, . . . , WL, started at prescribed points on ∂B_ (0 _,_ 1) _and stopped when they reach ∂B_ (0 _,_ 2) _. Let S denote the number of centres xi,_ 1 _≤ i ≤_ 4<sup>_n−_5</sup> _such that the shell B_ ( _xi,_ 2<sup>_−n_+1</sup> ) _\ B_ ( _xi,_ 2<sup>_−n_</sup> ) _is upcrossed twice by each of W_ 1 _, . . . , WL. Then there exists constants c, c∗ >_ 0 _such that_


_Moreover, the same estimate (with a suitable constant c∗) is valid if we condition on the end points of the excursions W_ 1 _, . . . , WL._

**Proof of Lemma 9.27.** By Lemma 9.25, for any _z ∈ ∂B_ (0 _,_ 1), the probability of Brownian motion starting at _z_ hitting the ball _B_ ( _xi,_ 2<sup>_−n_</sup> ) before reaching _∂B_ (0 _,_ 2) is at least 21 _n_<sup>,andthe</sup> probability of the second upcrossing excursion of _B_ ( _xi,_ 2<sup>_−n_+1</sup> ) _\ B_ ( _xi,_ 2<sup>_−n_</sup> ), when starting at _∂B_ ( _xi,_ 2<sup>1</sup><sup>_−n_</sup> ) is at least 1 _/_ 2. Thus (3.2) E _S ≥_ 4<sup>_n−_5</sup> (4 _n_ )<sup>_−L_</sup> _._ We now estimate the second moment of _S_ . Consider a pair of centres _xi, xj_ such that 2<sup>_−m_</sup> _≤ |xi − xj| ≤_ 2<sup>1</sup><sup>_−m_</sup> for some _m < n −_ 1. For each _k ≤ L_ , let _Vk_ = _Vk_ ( _xi, xj_ ) denote the event that the balls _B_ ( _xi,_ 2<sup>_−n_</sup> ) and _B_ ( _xj,_ 2<sup>_−n_</sup> ) are both visited by _Wk_ . Given that _B_ ( _xi,_ 2<sup>_−n_</sup> ) is reached first, the conditional probability that _Wk_ will also visit _B_ ( _xj,_ 2<sup>_−n_</sup> ) is at most<sup><u>2</u></sup> _n_<sup>_<u>m</u>_.Weconclude</sup> that P( _Vk_ ) _≤_<sup><u>4</u></sup> _n_<sup>_<u>m</u>_2whence</sup>

(3.2)


For each _m < n −_ 1 and _i ≤_ 4<sup>_n−_5</sup> , the number of centres _xj_ such that 2<sup>_−m_</sup> _≤|xi − xj| ≤_ 2<sup>1</sup><sup>_−m_</sup> is at most 4<sup>_n−m_</sup> . We deduce that there exists _C_ 1 _>_ 0 such that

### (3.3)


where the last inequality follows, e.g., from taking _x_ = 1 _/_ 4 in the binomial identity


Now (3.2), (3.3) and the Paley-Zygmund inequality yield (3.1). The final statement of the lemma follows from Lemma 9 _._ 26.

**Proof of Theorem 9.24.** Fix an increasing sequence _{ni_ : _i ≥_ 1 _}_ to be chosen later, and let _Nℓ_ =<sup>�</sup><sup>_ℓ_</sup> _i_ =1<sup>_ni_.Denote</sup><sup>_qi_=4</sup><sup>_ni−_5and</sup><sup>_Qi_=4</sup><sup>_Ni−_5</sup><sup>_i_.Webeginbyconstructinga</sup> nested sequence of centres which we associate with a forest, i.e. a collection of trees, in the following manner. The first level of the forest consists of _Q_ 1 centres, _{x_ 1<sup>(1)</sup><sup>_, . . . , x_(1)</sup> _Q_ 1<sup>_}_,chosen</sup> such that the balls _{B_ ( _x_<sup>(1)</sup> _k_<sup>_,_2</sup><sup>_−N_1+1):1</sup><sup>_≤k≤Q_1</sup><sup>_}_aredisjointandcontainedintheannulus</sup> _{z_ : 4<sup><u>1</u></sup><sup>_≤|z| ≤_</sup> 4<sup><u>3</u></sup><sup>_}_.</sup>

262

Continue this construction recursively. For _ℓ>_ 1 suppose that level _ℓ −_ 1 of the forest has been constructed. Level _ℓ_ consists of _Qℓ_ vertices _{x_ 1<sup>(</sup><sup>_ℓ_)</sup><sup>_, . . . , x_(</sup> _Q_<sup>_ℓ_</sup> _ℓ_<sup>)</sup><sup>_}_.Eachvertex</sup><sup>_x_</sup> _i_<sup>(</sup><sup>_ℓ−_1)</sup> , 1 _≤ i ≤ Qℓ−_ 1, at level _ℓ −_ 1 has _qℓ_ children _{x_<sup>(</sup> _j_<sup>_ℓ_)</sup> : ( _i −_ 1) _qℓ < j ≤ iqℓ}_ at level _ℓ_ ; the balls of radius 2<sup>_−Nℓ_+1</sup> around these children are disjoint and contained in the annulus


Recall that _T_ = inf _{t >_ 0 : _|B_ ( _t_ ) _|_ = 1 _}_ . We say that a level one vertex _x_<sup>(1)</sup> _k survived_ if Brownian motion upcrosses the shell _B_ ( _x_<sup>(1)</sup> _k_<sup>_,_2</sup><sup>_−N_1+1)</sup><sup>_\ B_(</sup><sup>_x_(1)</sup> _k_<sup>_,_2</sup><sup>_−N_1) twice before</sup><sup>_T_.A vertex at</sup> the second level _x_<sup>(2)</sup> _k_ is said to have _survived_ if its parent vertex survived, and in each upcrossing excursion of its parent, Brownian motion upcrosses the shell _B_ ( _x_<sup>(2)</sup> _k_<sup>_,_2</sup><sup>_−N_2+1)</sup><sup>_\B_(</sup><sup>_x_(2)</sup> _k_<sup>_,_2</sup><sup>_−N_2) twice.</sup> Recursively, we say a vertex _x_<sup>(</sup> _k_<sup>_ℓ_),atlevel</sup><sup>_ℓ_oftheforest,</sup><sup>_survived_ifitsparentvertexsurvived,</sup> and in each of the 2<sup>_ℓ−_1</sup> upcrossing excursions of its parent, Brownian motion upcrosses the shell _ball_ ( _xk_<sup>(</sup><sup>_ℓ_)</sup><sup>_,_2</sup><sup>_−Nℓ_+1)</sup><sup>_\B_(</sup><sup>_x_(</sup> _k_<sup>_ℓ_)</sup><sup>_,_2</sup><sup>_−Nℓ_) twice.Also, for any</sup><sup>_ℓ≥_1 , let</sup><sup>_Sℓ_denote the number of vertices</sup> at level _ℓ_ of the forest that survived.

_<u>∗</u>_ Using the notation of Lemma 9.27, denote Γ _ℓ_ = 4<sup>_nℓ_</sup> ( _c/nℓ_ )<sup>_L_</sup> and _pℓ_ =<sup>_c_</sup> _L_<sup>_L_</sup> !<sup>.where</sup><sup>_L_=</sup><sup>_L_(</sup><sup>_ℓ_) = 2</sup><sup>_ℓ−_1.</sup> Lemma 9.27 with _n_ = _n_ 1 states that


For _ℓ>_ 1, the same lemma, and independence of excursions in disjoint shells given their endpoints, yield


By picking _nℓ_ large enough, we can ensure that _pℓ_ +1Γ _ℓ > ℓ_ , whence the right-hand side of (3.5) is summable in _ℓ_ . Consequently


Thus with probability at least _α_ , there is a nested sequence of closed balls _B_ ( _xk_<sup>(</sup><sup>_ℓ_</sup> (<sup>)</sup> _ℓ_ )<sup>_,_2</sup><sup>_−Nℓ_)for</sup> _ℓ_ = 1 _,_ 2 _, . . ._ such that all their centres survive. The intersection of such a nested sequence yields a point visited by Brownian motion uncountably many times before it exits the unit disk.

Let _Hr_ denote the event that Brownian motion, killed on exiting _B_ (0 _, r_ ), has a point of uncountable multiplicity. As explained above, (3.6) implies that P( _H_ 1) _≥ α >_ 0. By Brownian scaling, P( _Hr_ ) does not depend on _r_ , whence


The Blumenthal zero-one law implies that this intersection has probability 1, so there are points of uncountable multiplicity almost surely.

263

### **4. Kaufman’s dimension doubling theorem**

In Theorem 4.37 we have seen that _d_ -dimensional Brownian motion maps any set of dimension _α_ almost surely into a set of dimension 2 _α_ . Surprisingly, by a famous result of Kaufman, the dimension doubling property holds almost surely _simultaneously_ for all sets.

Theorem 9.28 (Kaufman 1969). _Let {B_ ( _t_ ) : _t ≥_ 0 _} be Brownian motion in dimension d ≥_ 2 _. Almost surely, for any A ⊂_ [0 _, ∞_ ) _, we have_


The power of this result lies in the fact that the dimension doubling formula can now be applied to arbitrary random sets. As a first application we ask, how big the sets


of times mapped by _d_ -dimensional Brownian motion onto the same point _x_ can possibly be. We have seen so far in this chapter and Theorem 6.38 that, almost surely,

- in dimension _d ≥_ 4 all sets _T_ ( _x_ ) consist of at most one point,

- in dimension _d_ = 3 all sets _T_ ( _x_ ) consist of at most two points,

- in dimension _d_ = 2 at least one of the sets _T_ ( _x_ ) is uncountable,

- in dimension _d_ = 1 all sets _T_ ( _x_ ) have at least Hausdorff dimension<sup><u>1</u></sup> 2<sup>.</sup>

We now use Kaufman’s theorem to determine the Hausdorff dimension of the sets _T_ ( _x_ ) in the case of planar and linear Brownian motion.

Corollary 9.29. _Suppose {B_ ( _t_ ): _t ≥_ 0 _} is a planar Brownian motion. Then, almost surely, for all x ∈_ R<sup>2</sup> _, we have_ dim _T_ ( _x_ ) = 0 _._


Corollary 9.30. _Suppose {B_ ( _t_ ): _t ≥_ 0 _} is a linear Brownian motion. Then, almost surely, for all x ∈_ R _, we have_ dim _T_ ( _x_ ) = 2<sup><u>1</u></sup><sup>_._</sup>

**Proof.** The lower bound was shown in Theorem 6.38. For the upper bound let _{W_ ( _t_ ) : _t ≥_ 0 _}_ be a Brownian motion independent of _{B_ ( _t_ ) : _t ≥_ 0 _}_ . Applying Kaufman’s theorem for the planar Brownian motion given by _B_<sup>�</sup> ( _t_ ) = ( _B_ ( _t_ ) _, W_ ( _t_ )) we get, almost surely, dim _T_ ( _x_ ) = dim _B_<sup>�</sup><sup>_−_1</sup> ( _{x} ×_ R) _≤_<sup><u>1</u></sup> 2<sup>dim(</sup><sup>_{x} ×_R) =</sup><sup><u>1</u></sup> 2<sup>_._</sup>

We now prove Kaufman’s theorem, first in the case _d ≥_ 3. Note first that dim _B_ ( _A_ ) _≤_ 2 dim _A_ holds in all dimensions and for all sets _A ⊂_ [0 _, ∞_ ) if _{B_ ( _t_ ) : _t ≥_ 0 _}_ is _α_ -H¨older continuous for any _α <_ <u>12</u><sup>.</sup> By Corollary 1.20 this holds almost surely. Hence only the lower bound dim _B_ ( _A_ ) _≥_ 2 dim _A_ requires proof. The crucial idea here is that one uses a standardised covering of _B_ ( _A_ ) by dyadic cubes and ensures that, simultaneously for all possible covering cubes the preimages allow an efficient covering. An upper bound for dim _A_ follows by selecting from the coverings of all preimages.

264

Lemma 9.31. _Consider a cube Q ⊂_ R<sup>_d_</sup> _centred at a point x and having diameter_ 2 _r. Let {B_ ( _t_ ) : _t ≥_ 0 _} be d-dimensional Brownian motion, with d ≥_ 3 _. Define recursively_


_with the usual convention that_ inf _∅_ = _∞. Then there exists_ 0 _< θ <_ 1 _depending only on the dimension d, such that_ P _z{τn_<sup>_Q_</sup> +1<sup>_< ∞} ≤θnforallz∈_R2</sup><sup>_andn ∈_N</sup><sup>_._</sup>

**Proof.** It is sufficient to show that for some _θ_ as above,


But the quantity on the left can be bounded from below by

P _z_ � _τk_<sup>_Q_</sup> +1<sup>=</sup><sup>_∞_</sup> �� _|B_ ( _τ Qk_<sup>+</sup><sup>_r_2)</sup><sup>_−x| >_2</sup><sup>_r, τ Q_</sup> _k_<sup>_< ∞_</sup> �P _z_ � _|B_ ( _τk_<sup>_Q_+</sup><sup>_r_2)</sup><sup>_−x| >_2</sup><sup>_r_</sup> �� _τ Qk_<sup>_< ∞_</sup> �

The second factor is clearly positive, by the strong Markov property, and the first is also positive since Brownian motion is transient in _d ≥_ 3. Both probabilities are invariant under changing the scaling factor _r_ .

Lemma 9.32. _Let_ C _m denote the set of dyadic cubes of side length_ 2<sup>_−m_</sup> _inside_ [ _−_<sup><u>1</u></sup> 2<sup>_,_</sup><sup><u>1</u></sup> 2<sup>]</sup><sup>_d.Almost_</sup> _surely there exists a random variable C_ = _C_ ( _ω_ ) _so that for all m and for all cubes Q ∈_ C _m we have τ_<sup>_Q_</sup> _⌈mC_ +1 _⌉_<sup>=</sup><sup>_∞._</sup>

**Proof.** From Lemma 9.31 we get that


Now choose _c_ so large that 2<sup>_d_</sup> _θ_<sup>_c_</sup> _<_ 1. Then, by the Borel-Cantelli lemma, for all but finitely many _m_ we have _τ⌈_<sup>_Q_</sup> _cm_ +1 _⌉_ +1<sup>=</sup><sup>_∞_forall</sup><sup>_Q ∈_C</sup><sup>_m_.Finally,wecanchoosearandom</sup><sup>_C_(</sup><sup>_ω_)</sup><sup>_> c_to</sup> handle the finitely many exceptional cubes.

**Proof of Theorem 9.28 for** _d ≥_ 3 **.** As mentioned before we can focus on the ‘ _≥_ ’ direction. We fix _L_ and show that, almost surely, for all subsets _S_ of [ _−L, L_ ]<sup>_d_</sup> we have


Applying this to _S_ = _B_ ( _A_ ) _∩_ [ _−L, L_ ]<sup>_d_</sup> successively for a countable unbounded set of _L_ we get the desired conclusion. By scaling, it is sufficient to prove (4.1) for _L_ = 1 _/_ 2. The idea now is to verify (4.1) for all paths satisfying Lemma 9.32 using completely deterministic reasoning. As this set of paths has full measure, this verifies the statement.

Hence fix a path _{B_ ( _t_ ) : _t ≥_ 0 _}_ satisfying Lemma 9.32 for a constant _C >_ 0. If _β >_ dim _S_ and _ε >_ 0 there exists a covering of _S_ by binary cubes _{Qj_ : _j ∈_ N _} ⊂_<sup>�</sup><sup>_∞_</sup> _m_ =1<sup>C</sup><sup>_m_suchthat</sup> � _|Qj|β < ε_ . If _Nm_ denotes the number of cubes from C _m_ in such a covering, then


265

Consider the inverse image of these cubes under _{B_ ( _t_ ) : _t ≥_ 0 _}_ . Since we chose this path so that Corollary 9.32 is satisfied, this yields a covering of _B_<sup>_−_1</sup> ( _S_ ), which for each _m ≥_ 1 uses at most _CmNm_ intervals of length _r_<sup>2</sup> = _d_ 2<sup>_−_2</sup><sup>_m_</sup> .

For _γ > β_ we can bound the _γ/_ 2-dimensional Hausdorff content of _B_<sup>_−_1</sup> ( _S_ ) from above by


This can be made small by choosing a suitable _ε >_ 0. Thus _B_<sup>_−_1</sup> ( _S_ ) has Hausdorff dimension at most _γ/_ 2 for all _γ > β >_ dim _S_ , and therefore dim _B_<sup>_−_1</sup> ( _S_ ) _≤_ dim _S/_ 2 _._

In _d_ = 2 we cannot rely on transience of Brownian motion. To get around this problem, we can look at the Brownian path up to a stopping time. A convenient choice of stopping time for this purpose is _τR_<sup>_∗_=min</sup> � _t_ : _|B_ ( _t_ ) _|_ = _R_ � _._ For the two dimensional version of Kaufman’s theorem it is sufficient to show that, almost surely,


Lemma 9.31 has to be changed accordingly.

Lemma 9.33. _Consider a cube Q ⊂_ R<sup>2</sup> _centred at a point x and having diameter_ 2 _r, and assume that the cube Q is inside the ball of radius R about_ 0 _. Let {B_ ( _t_ ) : _t ≥_ 0 _} be planar Brownian motion. Define τk_<sup>_Qasin(4.1),andassumethatthecubeQisinsidetheballofradiusRabout_</sup> _the origin. Then there exists c_ = _c_ ( _R_ ) _>_ 0 _such that, with_ 2<sup>_−m−_1</sup> _< r <_ 2<sup>_−m_</sup> _, for any z ∈_ R<sup>2</sup> _,_


This is at least _c/m_ for some _c >_ 0 which depends on _R_ only.

The bound (4.2) on P _{τk_<sup>_Q< ∞}_intwodimensionsisworsebyalinearfactorthanthebound</sup> in higher dimensions. This, however, does not make a significant difference in the proof of the two dimensional version of Theorem 9.28, which can now be completed in the same way.

There is also a version of Kaufman’s theorem for Brownian motion in dimension one.

Theorem 9.34. _Suppose {B_ ( _t_ ) : _t ≥_ 0 _} is a linear Brownian motion. Then, almost surely, for all nonempty closed sets S ⊂_ R _, we have_


266

Remark 9.35. Note that here it is essential to run Brownian motion on an unbounded time interval. For example, for the point _x_ = max0 _≤t≤_ 1 _B_ ( _t_ ) the set _{t ∈_ [0 _,_ 1] : _B_ ( _t_ ) = _x}_ is a singleton almost surely. The restriction to closed sets comes from the Frostman lemma, which we have proved for closed sets only, and can be relaxed accordingly. _⋄_

**Proof.** For the proof of the upper bound let _{W_ ( _t_ ) : _t ≥_ 0 _}_ be a Brownian motion independent of _{B_ ( _t_ ) : _t ≥_ 0 _}_ . Applying Kaufman’s theorem for the planar Brownian motion given by _B_<sup>�</sup> ( _t_ ) = ( _B_ ( _t_ ) _, W_ ( _t_ )) we get almost surely, for all _S ⊂_ R,


where we have used the straightforward fact that dim( _S ×_ R) = 1 + dim _S_ .

The lower bound requires a more complicated argument, based on Frostman’s lemma. For this purpose we may suppose that _S ⊂_ ( _−M, M_ ) is closed and dim _S > α_ . Then there exists a measure _µ_ supported by _S_ such that


Let _ℓ_<sup>_a_</sup> be the measure with cumulative distribution function given by the local time at level _a_ . Let _ν_ be the measure on _B_<sup>_−_1</sup> ( _S_ ) given by


Then, by Theorem 6.18, one can find a constant _C >_ 0 such that


for all _a ∈_ [ _−M, M_ ] and 0 _< r <_ 1. By H¨older continuity of Brownian motion there exists, for given _ε >_ 0, a constant _c >_ 0 such that, for every _x ∈_ [0 _,_ 1],


From this we get the estimate


Hence, by the mass distribution principle, we get the lower bound _α/_ 2 + 1 _/_ 2 _− ε_ (1 + _α_ ) for the dimension and the result follows when _ε ↓_ 0 and _α ↑_ dim _S_ .

As briefly remarked in the discussion following Theorem 4.37, Brownian motion is also ‘capacitydoubling’. This fact holds for a very general class of kernels, we give an elegant proof of this fact here.

Theorem 9.36. _Let {B_ ( _t_ ) : _t ∈_ [0 _,_ 1] _} be d-dimensional Brownian motion and A ⊂_ [0 _,_ 1] _a closed set. Suppose f is decreasing and there is a constant C >_ 0 _with_


267


Remark 9.37. Condition (4.3) is only used in the ‘only if’ part of the statement. Note that if _⋄ f_ ( _x_ ) = _x_<sup>_α_</sup> is a power law, then (4.3) holds if and only if 2 _α < d_ .

**Proof.** We start with the ‘only if’ direction, which is easier. Suppose Cap _f_ ( _A_ ) _>_ 0. This implies that there is a mass distribution _µ_ on _A_ such that the _f_ -energy of _µ_ is finite. Then _µ ◦ B_<sup>_−_1</sup> is a mass distribution on _B_ ( _A_ ) and we will show that it has finite _f ◦ φ_ -energy. Indeed,


Hence,


where _X_ is a _d_ -dimensional standard normal random variable. Using polar coordinates and the monotonicity of _f_ we get, for a constant _κ_ ( _d_ ) depending only on the dimension,


By (4.3) the bracket on the right hand side is bounded by a constant independent of _|s − t|_ , and hence E[ _If ◦φ_ ( _µ ◦ B_<sup>_−_1</sup> )] _< ∞_ , which in particular implies _If ◦φ_ ( _µ_ ) _< ∞_ almost surely.

The difficulty in the ‘if’ direction is that a measure on _B_ ( _A_ ) with finite _f ◦φ_ -energy cannot easily be transported backwards onto _A_ . To circumvent this problem we use the characterisation of capacity in terms of polarity with respect to percolation limit sets, recall Theorem 9.18.

Fix a unit cube Cube such that Cap _f ◦φ_ ( _B_ ( _A_ ) _∩_ Cube) _>_ 0 with positive probability, and let Γ be a percolation limit set with retention probabilities associated to the decreasing function _f_ ( _x_<sup>2</sup> _/_ 4) as in Theorem 9.18, which is independent of Brownian motion. Then, by Theorem 9.18, we have _B_ ( _A_ ) _∩_ Γ _̸_ = _∅_ with positive probability. Define a random variable


which is finite with positive probability. Hence the measure _µ_ given by


is a mass distribution on _A_ . We shall show that it has finite _f_ -energy, which completes the proof. Again we use the polarity criterion of Theorem 9.18 to do this. Let S _n_ =<sup>�</sup> _S∈_ S _n_<sup>_S_be the</sup> union of all cubes retained in the construction up to step _n_ . Then, by looking at the retention probability of any fixed point in Cube, we have, for any _s ∈ A_ ,


268

Conversely, by a first entrance decomposition,


Given _B_ ( _t_ ) _∈_ S _n_ and<sup>_√_</sup> _s − t ≤_ 2<sup>_−n_+</sup><sup>_k_</sup> for some _k ∈{_ 0 _, . . . , n}_ , the probability that _B_ ( _s_ ) and _B_ ( _t_ ) are contained in the same dyadic cube _Q ∈_ C _n−k_ is bounded from below by a constant. Given this event, we know that _Q_ is retained in the percolation (otherwise we could not have _B_ ( _t_ ) _∈_ S _n_ ) and the probability that the cube in C _n_ , that contains _B_ ( _s_ ), is retained in the percolation is at least _pn−k_ +1 _· · · pn_ . Therefore


Finiteness of the _f_ -energy follows by comparing this with (4.4), cancelling the factor 1 _/f ◦ φ_ (2<sup>_−n−_1</sup> ), integrating over _µ_ ( _ds_ ), and letting _n →∞_ . This completes the proof.

269

### **Exercises**

Exercise 9.1.

- (a) Suppose that _{B_ 1( _t_ ): _t ≥_ 0 _}, {B_ 2( _t_ ): _t ≥_ 0 _}_ are independent standard Brownian motions in R<sup>3</sup> . Then, almost surely, _B_ 1[0 _, t_ ] _∩ B_ 2[0 _, t_ ] _̸_ = _∅_ for any _t >_ 0.

- (b) Suppose that _{B_ 1( _t_ ): _t ≥_ 0 _}, . . . , {Bp_ ( _t_ ): _t ≥_ 0 _}_ are _p_ independent standard Brownian motions in R<sup>_d_</sup> , and _d > d_ ( _p −_ 2). Then, almost surely, dim � _B_ 1[0 _, t_ 1] _∩· · · ∩ Bp_ [0 _, tp_ ]� = _d − p_ ( _d −_ 2) for any _t_ 1 _, . . . , tp >_ 0.

Exercise 9.2 ( _∗_ ). For a _d_ -dimensional Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ we denote by _S_ ( _p_ ) = � _x ∈_ R<sup>_d_</sup> : _∃_ 0 _< t_ 1 _< · · · < tp <_ 1 with _x_ = _B_ ( _t_ 1) = _· · ·_ = _B_ ( _tp_ )� the set of _p_ -fold multiple points. Show that, for _d > p_ ( _d −_ 2),

- (a) dim _S_ ( _p_ ) = _d − p_ ( _d −_ 2), almost surely.

- (b) for any closed set Λ, we have

P� _S_ ( _p_ ) _∩_ Λ _̸_ = _∅_ � _>_ 0 if and only if Cap _f p_ (Λ) _>_ 0 _,_ where the decreasing function _f_ is the radial potential.

Exercise 9.3.

- (a) Let _A_ be a set of rooted trees. We say that _A_ is _inherited_ if every finite tree is in _A_ , and if _T ∈ A_ and _v ∈ V_ is a vertex of the tree then the tree _T_ ( _v_ ), consisting of all successors of _v_ , is in _A_ .

Prove the _Galton-Watson 0–1 law_ : For a Galton-Watson tree, conditional on survival, every inherited set has probability zero or one.

- (b) Show that for the percolation limit sets Γ[ _γ_ ] _⊂_ R<sup>_d_</sup> with 0 _< γ < d_ we have


Exercise 9.4 ( _∗_ ). Consider a standard Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ and let _A_ 1 _, A_ 2 _⊂_ [0 _, ∞_ ). (a) Show that if dim( _A_ 1 _× A_ 2) _<_ 1 _/_ 2 then P _{B_ ( _A_ 1) intersects _B_ ( _A_ 2) _}_ = 0.

270

- (b) Derive the same conclusion under the weaker assumption that _A_ 1 _× A_ 2 has vanishing 1 _/_ 2-dimensional Hausdorff measure.

- (c) Show that if Cap1 _/_ 2( _A_ 1 _× A_ 2) _>_ 0, then P _{B_ ( _A_ 1) intersects _B_ ( _A_ 2) _} >_ 0.

- (d) Find a set _A ⊂_ [0 _, ∞_ ) such that the probability that _{B_ ( _t_ ): _t ≥_ 0 _}_ is one-to-one on _A_ is strictly between zero and one.

Exercise 9.5 ( _∗_ ). Let _{B_ ( _t_ ): 0 _≤ t ≤_ 1 _}_ be a planar Brownian motion. For every _a ∈_ R define the sets

_S_ ( _a_ ) = _{y ∈_ R : ( _a, y_ ) _∈ B_ [0 _, t_ ] _},_

the vertical slices of the path. Show that, almost surely,


for every _a ∈_ (min _{x_ : ( _x, y_ ) _∈ B_ [0 _, t_ ] _},_ max _{x_ : ( _x, y_ ) _∈ B_ [0 _, t_ ] _}_ ).

Exercise 9.6. Let _{B_ ( _t_ ) : _t ≥_ 0 _}_ be Brownian motion in dimension _d ≥_ 2.

Show that, almost surely, for any _A ⊂_ [0 _, ∞_ ), we have

dimM _B_ ( _A_ ) = 2 dimM _A_ and <u>dim</u> ~~M~~<sup>_B_(</sup><sup>_A_) = 2 dim</sup> ~~M~~<sup>_A ._</sup>

271

### **Notes and Comments**

The question whether there exist _p_ -multiple points of a _d_ -dimensional Brownian motion was solved in various stages in the early 1950s. First, L´evy showed in [ **Le40** ] that almost all paths of a planar Brownian motion have double points, and Kakutani [ **Ka44a** ] showed that if _n ≥_ 5 almost no paths have double points. The cases of _d_ = 3 _,_ 4 where added by Dvoretzky, Erd˝os and Kakutani in [ **DEK50** ] and the same authors showed in [ **DEK54** ] that planar Brownian motion has points of arbitrary multiplicity. Finally, Dvoretzky, Erd˝os, Kakutani and Taylor showed in [ **DEKT57** ] that there are no triple points in _d_ = 3. Clearly the existence of _p_ -fold multiple points is essentially equivalent to the problem whether _p_ independent Brownian motions have a common intersection.

The problem of finding the Hausdorff dimension of the set of _p_ -fold multiple points in the plane, and of double points in R<sup>3</sup> , was still open when Itˆo and McKean wrote their influential book on the sample paths of diffusions, see [ **IM74** , p. 261] in 1964, but was solved soon after by Taylor [ **Ta66** ] and Fristedt [ **Fr67** ]. Perkins and Taylor [ **PT88** ] provide fine results when Brownian paths in higher dimensions ‘come close’ to self-intersecting. The method of stochastic codimension, which we use to find these dimensions, is due to Taylor [ **Ta66** ], who used the range of stable processes as ‘test sets’. The restriction of the stable indices to the range _α ∈_ (0 _,_ 2] leads to complications, which can be overcome by a projection method of Fristedt [ **Fr67** ] or by using multiparameter processes [ **Kh02** ]. The use of percolation limit sets as test sets is much more recent and due to Khoshnevisan, Peres and Xiao [ **KPX00** ], though similar ideas are used in the context of trees ar least since the pioneering work of Lyons [ **Ly90** ]. The latter paper is also the essential source for our proof of Hawkes’ theorem.

Some very elegant proofs of these classical facts were given later: Rosen [ **Ro83** ] provides a local time approach, and Kahane [ **Ka86** ] proves a general formula for the intersection of independent random sets satisfying suitable conditions. The bottom line of Kahane’s approach is that the formula ‘codimension of the intersection is equal to the sum of codimensions of the intersected sets’ which is well-known from linear subspaces in general position can be extended to the Hausdorff dimension of a large class of random sets, which includes the paths of Brownian motion, see also [ **Fa97a, Ma95** ].

The intersection equivalence approach we describe in Section 2 is taken from [ **Pe96a** ], [ **Pe96b** ]. The proof of Lyons’ theorem we give is taken from [ **BPP95** ]. See [ **Ly92** , Theorem 2.1] for the original proof.

Hendricks and Taylor conjectured in 1976 a characterisation of the polar sets for the multiple points of a Brownian motion or a more general Markov process, which included the statement of Theorem 9.21. Sufficiency of the capacity criterion in Theorem 9.21 was proved by Evans [ **Ev87a, Ev87b** ] and independently by Tongring [ **To88** ], see also Le Gall, Rosen and Shieh [ **LRS89** ]. The full equivalence was later proved in a much more general setting by Fitzsimmons and Salisbury [ **FS89** ]. A quantitative treatment of the question, which sets contain double points of Brownian motion is given in [ **PP07** ].

272

Points of multiplicity strictly _n_ where identified by Adelman and Dvoretzky [ **AD85** ] and the result is also an immediate consequence of the exact Hausdorff gauge function identified by Le Gall [ **LG86** ].

The existence of points of infinite multiplicity in the planar case was first stated in [ **DEK58** ] though their proof seems to have a gap. Le Gall [ **LG87** ] proves a stronger result: Two sets _A, B ⊂_ R are said to be of the same _order type_ if there exists an increasing homeomorphism _φ_ of R such that _φ_ ( _A_ ) = _B_ . Le Gall shows that, for any totally disconnected, compact _A ⊂_ R, almost surely there exists a point _x ∈_ R<sup>2</sup> such that the set _{t ≥_ 0 : _B_ ( _t_ ) = _x}_ has the same order type as _A_ . In particular, there exist points of countably infinite and uncountable multiplicity. Le Gall’s proof is based on the properties of natural measures on the intersection of Brownian paths. Our proof avoids this and seems to be new, though it uses arguments of Le Gall’s proof as well as some techniques from [ **KM05** ].

Substantial generalisations of Exercise 9.4 can be found in papers by Khoshnevisan [ **Kh99** ] and Khoshnevisan and Xiao [ **KX05** ]. For example, in [ **Kh99** , Theorem 8.2] it is shown that the condition in part (c) is an equivalence.

Kaufman proved his dimension doubling theorem in [ **Ka69** ]. The version for Brownian motion in dimension one is due to Serlet [ **Se95** ].

The capacity-doubling result in the given generality is new, but Khoshnevisan and Xiao [ **KX05** , Question 1.1, Theorem 7.1] prove the special case when _f_ is a power law using a different method. Their argument is based on the investigation of additive L´evy processes and works for a class of processes much more general than Brownian motion. Theorem 9.36 does not hold uniformly for all sets _A_ . Examples can be constructed along the lines in [ **PT87** ].

In this book we do not construct a measure on the intersection of _p_ Brownian paths. However this is possible and yields the _intersection local time_ first studied by Geman, Horowitz and Rosen [ **GHR84** ], see also [ **Ro83** ]. This quantity plays a key role in the analysis of Brownian paths and [ **LG91** ] gives a very accessible account of the state of research in 1991, which is still worth reading. Recent research deals with fine Hausdorff dimension properties of the intersections, see for example [ **KM02, KM05** ].

273

### CHAPTER 10

---

[← Potential theory of Brownian motion](12-potential-theory-of-brownian-motion.md) · [Up: contents](index.md) · [Exceptional sets for Brownian motion →](14-exceptional-sets-for-brownian-motion.md)
