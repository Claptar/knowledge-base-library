---
title: Motivation
source: https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/bmbook.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Motivation

**Source:** [`bmbook.pdf`](https://www.stat.berkeley.edu/~aldous/205B/bmbook.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Much of probability theory is devoted to describing the _macroscopic picture_ emerging in random systems defined by a host of _microscopic random effects_ . Brownian motion is the macroscopic picture emerging from a particle moving randomly in _d_ -dimensional space. On the microscopic level, at any time step, the particle receives a random displacement, caused for example by other particles hitting it or by an external force, so that, if its position at time zero is _S_ 0, its position at time _n_ is given as _Sn_ = _S_ 0 +<sup>�</sup><sup>_n_</sup> _i_ =1<sup>_Xi,_wherethedisplacements</sup><sup>_X_1</sup><sup>_, X_2</sup><sup>_, X_3</sup><sup>_, . . ._are</sup> assumed to be independent, identically distributed random variables with values in R<sup>_d_</sup> . The process _{Sn_ : _n ≥_ 0 _}_ is a random walk, the displacements represent the microscopic inputs. When we think about the macroscopic picture, what we mean is questions such as:

- Does _Sn_ drift to infinity?

- Does _Sn_ return to the neighbourhood of the origin infinitely often?

- What is the speed of growth of max _{|S_ 1 _|, . . . , |Sn|}_ as _n →∞_ ?

- What is the asymptotic number of windings of _{Sn_ : _n ≥_ 0 _}_ around the origin?

It turns out that not all the features of the microscopic inputs contribute to the macroscopic picture. Indeed, if they exist, only the _mean_ and _covariance_ of the displacements are shaping the picture. In other words, all random walks whose displacements have the same mean and covariance matrix give rise to same macroscopic process, and even the assumption that the displacements have to be independent and identically distributed can be substantially relaxed. This effect is called _universality_ , and the macroscopic process is often called a _universal object_ . It is a common approach in probability to study various phenomena through the associated universal objects.

Any continuous time stochastic process _{B_ ( _t_ ) : _t ≥_ 0 _}_ describing the macroscopic features of a random walk should have the following properties:

- (1) for all times 0 _≤ t_ 1 _≤ t_ 2 _≤ . . . ≤ tn_ the random variables

   - _B_ ( _tn_ ) _− B_ ( _tn−_ 1) _, B_ ( _tn−_ 1) _− B_ ( _tn−_ 2) _, . . . , B_ ( _t_ 2) _− B_ ( _t_ 1)

are independent; we say that the process has _independent increments_ ,

- (2) the distribution of the increment _B_ ( _t_ + _h_ ) _− B_ ( _t_ ) does not depend on _t_ ; we say that the process has _stationary increments_ ,

- (3) the process _{B_ ( _t_ ) : _t ≥_ 0 _}_ has almost surely continuous paths.

It follows (with some work) from the central limit theorem that these features imply that there exists a vector _µ ∈_ R<sup>_d_</sup> and a matrix Σ _∈_ R<sup>_d×d_</sup> such that

- (4) for every _t ≥_ 0 and _h ≥_ 0 the increment _B_ ( _t_ + _h_ ) _− B_ ( _t_ ) is multivariate normally distributed with mean _hµ_ and covariance matrix _h_ ΣΣ<sup>T</sup> .

13

Hence any process with the features (1)-(3) above is characterised by just three parameters,

- the _initial distribution_ , i.e. the law of _B_ (0),

- the _drift vector µ_ ,

- the _diffusion matrix_ Σ.

We call the process _{B_ ( _t_ ) : _t ≥_ 0 _}_ a _Brownian motion_ if the drift vector is zero, and the diffusion matrix is the identity. If _B_ (0) = 0, i.e. the motion is started at the origin, we use the term _standard Brownian motion_ .

Suppose we have a standard Brownian motion _{B_ ( _t_ ) : _t ≥_ 0 _}_ . If _X_ is a random variable with values in R<sup>_d_</sup> , _µ_ a vector in R<sup>_d_</sup> and Σ a _d × d_ matrix, then it is easy to check that _{B_<sup>˜</sup> ( _t_ ) : _t ≥_ 0 _}_ given by


is a process with the properties (1)-(4) with initial distribution _X_ , drift vector _µ_ and diffusion matrix Σ. Hence the macroscopic picture emerging from a random walk can be fully described by a standard Brownian motion.


0 50 100 150 200 Figure 1. The range _{B_ ( _t_ ) : 0 _≤ t ≤_ 1 _}_ of a planar Brownian motion

In _Chapter 1_ we start exploring Brownian motion by looking at dimension _d_ = 1. Here Brownian motion is a random continuous function and we ask about its _regularity_ , for example:

- For which parameters _α_ is the random function _B_ : [0 _,_ 1] _→_ R _α_ -H¨older continuous?

- Is the random function _B_ : [0 _,_ 1] _→_ R differentiable?

The surprising answer to the second question was given by Paley, Wiener and Zygmund in 1933: Almost surely, the random function _B_ : [0 _,_ 1] _→_ R is _nowhere_ differentiable! This is particularly interesting, as it is not easy to construct a continuous, nowhere differentiable function without the help of randomness. We will give a modern proof of the Paley, Wiener and Zygmund theorem, see Theorem 1.30.

14

In _Chapter 2_ we move to general dimension _d_ . We shall explore the strong Markov property, which roughly says that at suitable random times Brownian motion starts afresh. Among the facts we derive are: Almost surely,

- the set of all points visited by Brownian motion in _d_ = 2 has area zero,

- the set of times when Brownian motion in _d_ = 1 revisits the origin is uncountable.

Besides these sample path properties, the strong Markov property is also the key to some fascinating distributional identities. It enables us to understand, for example,

- the process _{M_ ( _t_ ): _t ≥_ 0 _}_ of the running maxima _M_ ( _t_ ) = max0 _≤s≤t B_ ( _s_ ) of a onedimensional Brownian motion,

- the process _{Ta_ : _a ≥_ 0 _}_ of the first hitting times _Ta_ = inf _{t ≥_ 0: _B_ ( _t_ ) = _a}_ of level _a_ of a one-dimensional Brownian motion,

- the process of the vertical first hitting positions by a two-dimensional Brownian motion of the lines _{_ ( _x, y_ ) _∈_ R<sup>2</sup> : _x_ = _a}_ , as a function of _a_ .

In _Chapter 3_ we start exploring the rich relations of Brownian motion to harmonic analysis. To motivate this relation by a discrete analogue, suppose that _{Sn_ : _n ∈_ N _}_ is a simple, symmetric random walk in Z<sup>2</sup> started at some _x ∈_ Z<sup>2</sup> . Here simple and symmetric means that the increments take each of the values (0 _,_ 1) _,_ (1 _,_ 0) _,_ (0 _, −_ 1) _,_ ( _−_ 1 _,_ 0) with probability 4<sup><u>1</u>.Suppose</sup> that _A ⊂_ Z<sup>2</sup> is a bounded subset of the two-dimensional lattice and let _∂A_ be the set of all vertices in Z<sup>2</sup> _\ A_ which are adjacent to a vertex in _A_ . Let _T_ = inf � _n ≥_ 0: _Sn̸ ∈ A}_ be the first exit time from _A_ . Suppose moreover that _ϕ_ : _∂A →_ R is given and define _f_ : _A ∪ ∂A →_ R _, f_ ( _x_ ) = E� _ϕ_ ( _ST_ ) �� _S_ 0 = _x_ � _._

Then it easy to see that,


where we write _x ∼ y_ if _x_ and _y_ are adjacent on the lattice Z<sup>2</sup> . This means that the value _f_ ( _x_ ) is the mean over all the values at the adjacent vertices. A function with this property is called _discrete harmonic_ , and we have solved the (easy) problem of finding the discrete harmonic function on _A ∪ ∂A_ with given boundary values _ϕ_ on _∂A_ . A more challenging problem, which we solve in Chapter 3, is the corresponding continuous problem, called the _Dirichlet problem_ . For its formulation, fix a connected open set _U ⊂_ R<sup>2</sup> with nice boundary, and let _ϕ_ : _∂U →_ R be continuous. The harmonic functions _f_ : _U →_ R on the domain _U_ are characterised by the differential equation


The Dirichlet problem is to find, for a given domain _U_ and boundary data _ϕ_ , a continuous function _f_ : _U ∪ ∂U →_ R, which is harmonic on _U_ and agrees with _ϕ_ on _∂U_ . In Theorem 3.12 we show that the unique solution of this problem is given as


15


Figure 2. Brownian motion and the Dirichlet problem

where _{B_ ( _t_ ) : _t ≥_ 0 _}_ is a Brownian motion and _T_ = inf _{t ≥_ 0 : _B_ ( _t_ ) _̸ ∈ U }_ is the first exit time from _U_ . We shall exploit this result, for example, to show exactly in which dimensions a particle following a Brownian motion drifts to infinity, see Theorem 3.19.

In _Chapter 4_ we provide one of the major tools in our study of Brownian motion, the concept of Hausdorff dimension, and show how it can be applied in the context of Brownian motion. Indeed, when describing the sample paths of a Brownian motion one frequently encounters questions of the size of a given set: How big is the set of all points visited by a Brownian motion in the plane? How big is the set of double-points of a planar Brownian motion? How big is the set of times where Brownian motion visits a given set, say a point?

For an example, let _{B_ ( _t_ ) : _t ≥_ 0 _}_ be Brownian motion on the real line and look at


the set of its zeros. Although _t �→ B_ ( _t_ ) is a continuous function, Zero is an infinite set. This set is _big_ , as it is an uncountable set without isolated points. However, it is also _small_ in the sense that its Lebesgue measure, denoted _L_ , is zero. Indeed, we have by Fubini’s theorem:


Zero is a fractal set and we show in Theorem 4.24 that its Hausdorff dimension is 1 _/_ 2.

In _Chapter 5_ we explore the relationship of random walk and Brownian motion. There are two natural ways to relate random walks directly to Brownian motion: Assume _d_ = 1 for the moment and let _X_ be an arbitrary random variable, for simplicity with E _X_ = 0 and Var _X_ = 1.

- _Random walks can be embedded into Brownian motion._ The idea is that, given any centred distribution with finite variance, one can define a sequence _T_ 1 _< T_ 2 _< · · ·_ of (stopping) times for Brownian motion of controllable size, such that _{Sn_ : _n ≥_ 1 _}_ given by _Sn_ = _B_ ( _Tn_ ) is a random walk with increments distributed like _X_ . We say that the random walk is _embedded_ in Brownian motion.

16

- _Random walk paths converge in distribution to Brownian motion paths._ The main result is Donsker’s invariance principle, which states that, for the random walk _{Sk_ : _k ∈_ N _}_ with increments distributed like _X_ , the law of the random curve obtained by connecting the points _Sk/_<sup>_√_</sup> _<u>n</u>_ in order _k_ = 1 _,_ 2 _, . . . , n_ linearly in 1 _/n_ time units converges in law to Brownian motion.

These two principles allow us to answer a lot of questions about random walks by looking at Brownian motion instead. Why can this be advantageous? First, in many cases the fact that Brownian motion is a continuous time process is an advantage over discrete time random walks. For example, as we discuss in the next paragraph, Brownian motion has scaling invariance properties, which can be a powerful tool in the study of its path properties. Second, even in cases where the discrete, combinatorial structures of a simple random walk model are the right tool in the proof of a statement, the translation into a Brownian motion setting frequently helps extending the result from a specific random walk, e.g. the simple random walk on the integers, where _Xi_ takes values _±_ 1, to a wider range of random walks. In Chapter 5 we give several examples how results about Brownian motion can be exploited for random walks.

In _Chapter 6_ we look again at Brownian motion in dimension _d_ = 1. In this case the occupation measure _µt_ of the Brownian motion, defined by


has a density. To see this use first Fatou’s lemma and then Fubini’s theorem,


Using that the density of a standard normal random variable _X_ is bounded by one, we get


and this implies that


Hence


By the Radon-Nikodym this implies that a density _{L_<sup>_a_</sup> ( _t_ ): _a ∈_ R _}_ exists, which we call the _Brownian local time_ . We shall construct this density by probabilistic means, show that it is jointly continuous in _a_ and _t_ , and characterise it as a stochastic process.

17

One of the most important invariance properties of Brownian motion is _conformal invariance_ , which we discuss in _Chapter 7_ . To make this plausible think of an angle-preserving linear mapping _L_ : R<sup>_d_</sup> _→_ R<sup>_d_</sup> , like a rotation followed by multiplication by _a_ . Take a random walk started in zero with increments of mean zero and covariance matrix the identity, and look at its image under _L_ . This image is again a random walk and its increments are distributed like _LX_ . Appropriately rescaled as in Donsker’s invariance principle, both random walks converge, the first to a Brownian motion, the second to a process satisfying our conditions (1)–(4), but with a slightly different covariance matrix. This process can be identified as a time-changed Brownian motion

_{B_ ( _a_<sup>2</sup> _t_ ) : _t ≥_ 0 _}._

This easy observation has a deeper, local counterpart for planar Brownian motion: Suppose that _φ_ : _U → V_ is a conformal mapping of a simply connected domain _U ⊂_ R<sup>2</sup> onto a domain _V ⊂_ R<sup>2</sup> . Conformal mappings are locally angle-preserving and the Riemann mapping theorem of complex analysis tells us that a lot of these mappings exist.


Figure 3. A conformal mapping of Brownian paths

Suppose that _{B_ ( _t_ ) : _t ≥_ 0 _}_ is a standard Brownian motion started in some point _x ∈ U_ and _τ_ = inf _{t >_ 0: _B_ ( _t_ ) _∈/ U }_ is the first exit time of the path from the domain _U_ . Then it turns out that the image process _{φ_ ( _B_ ( _t_ )) : 0 _≤ t ≤ τ }_ is a _time-changed_ Brownian motion in the domain _V_ , stopped when it leaves _V_ . In order to prove this we have to develop a little bit of the theory of stochastic integration with respect to a Brownian motion, and we shall give a lot of further applications of this tool in Chapter 7.

In _Chapter 8_ we develop the potential theory of Brownian motion. The problem which is the motivation behind this is, given a compact set _A ⊂_ R<sup>_d_</sup> , to find the probability that a Brownian motion _{B_ ( _t_ ): _t ≥_ 0 _}_ hits the set _A_ , i.e. that there exists _t >_ 0 with _B_ ( _t_ ) _∈ A_ . This problem will be answered in the best possible way by Theorem 8.23, which is modern extension of a classical result of Kakutani: The hitting probability can be approximated by the capacity of _A_ with respect to the Martin kernel up to a factor of two.

With a wide range of tools at our hand, in _Chapter 9_ we study the self-intersections of Brownian motion: For example, a point _x ∈_ R<sup>_d_</sup> is called a double point of _{B_ ( _t_ ): _t ≥_ 0 _}_ if there exist

18

times 0 _< t_ 1 _< t_ 2 such that _B_ ( _t_ 1) = _B_ ( _t_ 2) = _x_ . In which dimensions does Brownian motion have double points? How big is the set of double points? We show that, almost surely,

- in dimensions _d ≥_ 4 no double points exist,

- in dimension _d_ = 3 (and _d_ = 1) double points exist and the set of double points has Hausdorff dimension one,

- in dimension _d_ = 2 double points exists and the set of double points has Hausdorff dimension two.

In dimension _d_ = 2 we find a surprisingly complex situation: While every point _x ∈_ R<sup>2</sup> is almost surely not visited by a Brownian motion, there exist (random) points in the plane, which are visited infinitely often, even uncountably often. This result, Theorem 9.24, is one of the highlights of this book.

_Chapter 10_ deals with exceptional points for Brownian motion and Hausdorff dimension spectra of families of exceptional points. To explain an example, we look at a Brownian motion in the plane run for one time unit, which is a continuous curve _{B_ ( _t_ ) : _t ∈_ [0 _,_ 1] _}_ . If _x_ = _B_ ( _t_ ) _∈_ R<sup>2</sup> , for some 0 _< t <_ 1, is a point on the curve one can use polar coordinates centred in _x_ to define for every time interval ( _t_ + _ε,_ 1) the number of windings the curve performs around _x_ in this time interval, with counterclockwise windings having a positive and clockwise windings having a negative sign. Denoting this number by _θ_ ( _ε_ ), we obtain in Chapter 7 that, almost surely,


In other words, for any point on the curve, almost surely, the Brownian motion performs an infinite number of full windings in both directions.

Still, there exist random points on the curve, which are exceptional in the sense that Brownian motion performs no windings around them at all. This follows from an easy geometric argument: Take a point in R<sup>2</sup> with coordinates ( _x_ 1 _, x_ 2) such that


i.e. a point which is the leftmost on the intersection of the Brownian curve and the line _{_ ( _z, y_ ): _z ∈_ R _}_ , for some _x_ 2 _∈_ R. Then Brownian motion does not perform any full windings around ( _x_ 1 _, x_ 2), as this would necessarily imply that it crosses the half-line _{_ ( _x, x_ 2): _x < x_ 2 _}_ , contradicting the minimality of _x_ 1.

One can ask for a more extreme deviation from typical behaviour: A point _x_ = _B_ ( _t_ ) is an _α_ -cone point if the Brownian curve is contained in an open cone with tip in _x_ = ( _x_ 1 _, x_ 2), central axis _{_ ( _x_ 1 _, x_ ): _x > x_ 2 _}_ and opening angle _α_ . Note that the points described in the previous paragraph are 2 _π_ -cone points in this sense. We show that _α_ -cone points exist exactly if _α ∈_ [ _π,_ 2 _π_ ], and prove that for every such _α_ , almost surely,


This is an example of a Hausdorff dimension spectrum, a topic which has been at the centre of some research activity at the beginning of the current millennium.

19

### CHAPTER 1

---

[← List of frequently used notation](03-list-of-frequently-used-notation.md) · [Up: contents](index.md) · [Definition and first properties of Brownian motion →](05-definition-and-first-properties-of-brownian-motion.md)
