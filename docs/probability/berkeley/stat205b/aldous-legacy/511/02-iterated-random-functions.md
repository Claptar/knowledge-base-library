---
title: ITERATED RANDOM FUNCTIONS
source: https://www.stat.berkeley.edu/~aldous/205B/511.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/511.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# ITERATED RANDOM FUNCTIONS

**Source:** [`511.pdf`](https://www.stat.berkeley.edu/~aldous/205B/511.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Persi Diaconis Department of Mathematics & ORIE Cornell University Ithaca, NY 14853

David Freedman Department of Statistics University of California Berkeley, CA 94720

`A bstract.` Iterated random functions are used to draw pictures or simulate large Ising models, among other applications. They offer a method for studying the steady state distribution of a Markov chain, and give useful bounds on rates of convergence in a variety of examples. The present paper surveys the field and presents some new examples. There is a simple unifying idea: the iterates of random Lipschitz functions converge if the functions are contracting on the average.

**1. Introduction.** The applied probability literature is nowadays quite daunting. Even relatively simple topics, like Markov chains, have generated enormous complexity. This paper describes a simple idea that helps to unify many arguments in Markov chains, simulation algorithms, control theory, queuing, and other branches of applied probability. The idea is that Markov chains can be constructed by iterating random functions on the state space _S_ . More specifically, there is a family _{fθ_ : _θ ∈_ Θ _}_ of functions that map _S_ into itself, and a probability distribution _µ_ on Θ. If the chain is at _x ∈ S_ , it moves by choosing _θ_ at random from _µ_ , and going to _fθ_ ( _x_ ). For now, _µ_ does not depend on _x_ .

The process can be written as _X_ 0 = _x_ 0 _, X_ 1 = _fθ_ 1( _x_ 0) _, X_ 2 = ( _fθ_ 2 _◦ fθ_ 1)( _x_ 0) _, . . ._ , with _◦_ for composition of functions. Inductively,


where _θ_ 1 _, θ_ 2 _, . . ._ are independent draws from _µ_ . The Markov property is clear: given the present position of the chain, the conditional distribution of the future does not depend on the past.

_Key words and phrases._ Products of random matrices, iterated function systems, coupling from the past.

Typeset by _AMS_ -TEX

1

2 PERSI DIACONIS AND DAVID FREEDMAN

We are interested in situations where there is a stationary probability distribution _π_ on _S_ with

_P {Xn ∈ A} → π_ ( _A_ ) as _n →∞._

For example, suppose _S_ is the real line R, and there are just two functions,


where _a_ is given and 0 _< a <_ 1. In present notation, Θ = _{_ + _, −}_ ; suppose _µ_ (+) = _µ_ ( _−_ ) = 1 _/_ 2. The process moves linearly,


where _ξn_ = _±_ 1 with probability 1 _/_ 2. The stationary distribution has an explicit representation, as the law of


The random series on the right converges to a finite limit because 0 _< a <_ 1. Plainly, the distribution of _Y∞_ is unchanged if _Y∞_ is multiplied by _a_ and then a new _ξ_ is added: that is stationarity. The series representation (1.3) can therefore be used to study the stationary distribution; however, many mysteries remain, even for this simple case (Section 2.5).

There are a wealth of examples based on affine maps in _d_ -dimensional Euclidean space. The basic chain is


where the ( _An, Bn_ ) are independent and identically distributed; _An_ is a _d × d_ matrix and _Bn_ is _d ×_ 1 vector. Section 2 surveys this area. Section 2.3 presents an interesting application for _d_ = 2: with an appropriately chosen finite distribution for ( _An, Bn_ ), the Markov chain can be used to draw pictures of fractal objects like ferns, clouds, or fire. Section 3 describes finite state spaces where the backward iterations can be explicitly tested to see if they have converged. The lead example is the “coupling from the past” algorithm of Propp and Wilson (1996, 1998), which allows simulation for previously intractable distributions, such as the Ising model on a large grid.

Section 4 gives examples from queuing theory. Section 5 introduces some rigor, and explains a unifying theme. Suppose that _S_ is a complete separable metric space. Write _ρ_ for the metric. Suppose that each _fθ_ is Lipschitz: for some _Kθ_ and all _x, y ∈ S_ ,


For _x_ 0 _∈ S_ , define the “forward iteration” starting from _X_ 0 = _x_ 0 by


ITERATED RANDOM FUNCTIONS 3

_θ_ 1 _, θ_ 2 _, . . ._ being independent draws from a probability _µ_ on Θ; this is just a rewrite of equation (1.1). Define the “backward iteration” as

(1.4) _Yn_ +1 = ( _fθ_ 1 _◦ fθ_ 2 _◦· · · ◦ fθn_ +1)( _x_ 0) _._

Of course, _Yn_ has the same distribution as _Xn_ for each _n_ . However, the forward process _{Xn_ : _n_ = 0 _,_ 1 _,_ 2 _, . . . }_ has very different behavior from the backward process _{Yn_ : _n_ = 0 _,_ 1 _,_ 2 _, . . . }_ : the forward process moves ergodically through _S_ , while the backward process converges to a limit. (Naturally, there are assumptions.) The next theorem, proved in Section 5.2, shows that if _fθ_ is contracting on average, then _{Xn}_ has a unique stationary distribution _π_ . The “induced Markov chain” in the theorem is the forward process _Xn_ . The kernel _Pn_ ( _x, dy_ ) is the law of _Xn_ given that _X_ 0 = _x_ , and the Prokhorov metric is used for the distance between two probabilities on _S_ . This metric will be defined in Section 5.1; it is denoted “ _ρ_ ”, like the metric on _S_ . (Section 5.1 also takes care of the measure-theoretic details.)

**Theorem 1.** _Let_ ( _S, ρ_ ) _be a complete separable metric space. Let {fθ_ : _θ ∈_ Θ _} be a family of Lipschitz functions on S, and let µ be a probability distribution on_ Θ _. Suppose that_ � _Kθ µ_ ( _dθ_ ) _< ∞,_ � _ρ_ [ _fθ_ ( _x_ 0) _, x_ 0] _µ_ ( _dθ_ ) _< ∞ for some x_ 0 _∈ S, and_ � log _Kθ µ_ ( _dθ_ ) _<_ 0 _._

- (i) _The induced Markov chain has a unique stationary distribution π._

- (ii) _ρ_ [ _Pn_ ( _x, ·_ ) _, π_ ] _≤ Axr_<sup>_n_</sup> _for constants Ax and r with_ 0 _< Ax < ∞ and_

   - 0 _< r <_ 1 _; this bound holds for all times n and all starting states x._

- (iii) _The constant r does not depend on n or x; the constant Ax does not depend on n, and Ax < a_ + _bρ_ ( _x, x_ 0) _where_ 0 _< a, b < ∞._

The condition that � log _Kθ µ_ ( _dθ_ ) _<_ 0 makes _Kθ <_ 1 for typical _θ_ , and formalizes the notion of “contracting on average”. The key step in proving Theorem 1 is proving convergence of the backward iterations (1.4).

**Proposition 1.** _Under the regularity conditions of Theorem 1, the backward iterations converge almost surely to a limit, at an exponential rate. The limit has the unique stationary distribution π._

(A sequence of random variables _Xn_ converges “almost surely” if the exceptional set—where _Xn_ fails to converge—has probability 0.)

The queuing-theory examples in Section 4 are interesting for several reasons: in particular, the backward iterations converge although the functions are not contracting on average. Section 6 has some examples that illustrate the theorem, and show why the regularity conditions are needed. Section 7 extends the theory to cover Dirichlet random measures, the states of the Markov chain being probabilities on some underlying space (like the real line). Closed-form expressions can sometimes be given for the distribution of the mean of a random pick from the Dirichlet; Section 7.3 has examples.

Previous surveys on iterated random functions include Chamayou and Letac (1991) as well as Letac (1986). The texts by Baccelli and Br´emaud (1994), Brandt

PERSI DIACONIS AND DAVID FREEDMAN

4

et al. (1990), and Duflo (1997) may all be seen as developments of the random iterations idea; Meyn and Tweedie (1993) frequently use random iterations to illustrate the general theory.

**2. Affine functions.** This paper got started when we were trying to understand a simple Markov chain on the unit interval, described in Section 2.1. Section 2.2 discusses some general theory for recursions in R<sup>_d_</sup> of the form _Xn_ +1 = _An_ +1 _Xn_ + _Bn_ +1, where the _{An}_ are random matrices and _{Bn}_ are random vectors. (In strict mathematical terminology, the function _X → AX_ + _B_ is “affine” rather than linear when _B̸_ = 0.) Under suitable regularity conditions, these matrix recursions are shown to have unique stationary distributions. With affine functions, the conditions are virtually necessary and sufficient. The theory is applied to draw fractal ferns (among other objects) in Section 2.3. Moments and tail probabilities of the stationary distributions are discussed in Section 2.4. Sections 2.5–6 are about the “fine structure”: how smooth are the stationary distributions?

**2.1. Motivating example.** A simple example motivated our study—a Markov chain whose state space _S_ = (0 _,_ 1) is the open unit interval. If the chain is at _x_ , it picks one of the two intervals (0 _, x_ ) or ( _x,_ 1) with equal probability 1 _/_ 2, and then moves to a random _y_ in the chosen interval. The transition density is


As usual, 1 _A_ ( _y_ ) = 1 or 0, according as _y ∈ A_ or _y ∈/ A_ . The first term in the sum corresponds to a leftward move from _x_ ; the second, to a rightward move.

Did this chain have a stationary distribution? If so, could the distribution be identified? Those were our two basic questions. After some initial floundering, we saw that the chain could be represented as the iteration of random functions


with _u_ chosen uniformly on (0 _,_ 1) and _φ, ψ_ chosen with probability 1 _/_ 2 each.

Theorem 1 shows there is a unique stationary distribution. We identified this distribution by guesswork, but there is a systematic method. Begin by assuming that the stationary distribution has a density _f_ ( _x_ ). From (2.1),


Differentiation gives


so


ITERATED RANDOM FUNCTIONS

5

This argument is heuristic, but it is easy to check that the “arcsine density” displayed in (2.3) satisfies equation (2.2)—and must therefore be stationary. The constant _π_ = 3 _._ 14 _. . ._ makes � _f_ ( _y_ ) _dy_ = 1; the name comes about because


Figure 1 illustrates the difference between the backward process (left hand panel, convergence) and the forward process (right hand panel, ergodic behavior). Position at time _n_ is plotted against _n_ = 0 _, . . . ,_ 100, with linear interpolation. Both processes start from _x_ 0 = 1 _/_ 3 and use the same random functions to move. The order in which the functions are composed is the only difference. In the left hand panel, the limit 0 _._ 236 _. . ._ is random because it depends on the functions being iterated; but the limit does not depend on the starting point _x_ 0.

Figure 1. The left hand panel shows convergence of the backward process; the right hand panel shows ergodic behavior by the forward process.


<!-- Start of picture text -->
1.00 1.00<br>0.75 0.75<br>0.50 0.50<br>0.25 0.25<br>0.00 0.00<br>0 25 50 75 100 0 25 50 75 100<br><!-- End of picture text -->

**Remarks.** Suppose 0 _< p <_ 1 and _q_ = 1 _− p_ . The same argument shows that choosing (0 _, x_ ) with probability _p_ and ( _x,_ 1) with probability _q_ leads to a Beta( _q, p_ ) stationary distribution, with density _Cx_<sup>_q−_1</sup> (1 _− x_ )<sup>_p−_1</sup> on (0 _,_ 1). The normalizing constant is _C_ = Γ( _q_ + _p_ ) _/_ [Γ( _q_ )Γ( _p_ )], where Γ is Euler’s gamma function. In our example, _q_ + _p_ = 1, so Γ( _q_ + _p_ ) = Γ(1) = 1.

Although we will not pursue this idea, the probability _p_ of moving to (0 _, x_ ) from _x_ can even be allowed to depend on _x_ . For example if _p_ ( _x_ ) = _x_ , the stationary distribution is uniform. However, Theorem 1 is not in force when _p_ ( _x_ ) depends on _x_ . For instance, if _p_ ( _x_ ) = 1 _− x_ , the process converges to 0 or 1 almost surely: if the starting state is _x_ , the chance of converging to 1 is _x_ . (The process is a martingale, and convergence follows from standard theorems.) Theorem 1 can be extended to cover _µ_ that depend on _x_ , but further conditions are needed.

PERSI DIACONIS AND DAVID FREEDMAN

6

Many of the constructions in this paper involve the Beta distribution. Figure 2 plots some of the densities. The stationary density (2.3) in our lead example is Beta(<sup><u>1</u></sup> 2<sup>_,_</sup><sup><u>1</u></sup> 2<sup>)—thebowl-shapedcurveintherighthandpanel;wereturntothisex-</sup> ample in Section 6.3.

Figure 2. The Beta distribution. The left hand panel plots the Beta(1,3)density (heavy line) and the Beta(5,2)-density (light line). The right hand panel plots the Beta(<sup><u>1</u></sup> 2<sup>_,_</sup><sup><u>1</u></sup> 2<sup>)-density(heavyline)andtheBeta(10,10)density</sup> (light line).


<!-- Start of picture text -->
4 4<br>3 3<br>2 2<br>1 1<br>0 0<br>.00 .25 .50 .75 1.00 .00 .25 .50 .75 1.00<br><!-- End of picture text -->

**2.2. Matrix recursions.** Matrix recursions have been used in a host of modeling efforts; see, for instance, Priestley (1988). To define things in R<sup>_d_</sup> , let _X_ 0 = _x_ 0 _∈_ R<sup>_d_</sup> , and


with ( _An, Bn_ ) being i.i.d.; _An_ is a _d × d_ matrix and _Bn_ is a _d ×_ 1 vector: i.i.d. is the usual short-hand for “independent and identically distributed”. Autoregressive processes like (2.4) will be discussed again in Section 6.1. Under suitable regularity conditions, the stationary distribution can be represented as the law of


Indeed, suppose this sum converges a.s. to a finite limit. The distribution is unchanged if a fresh ( _A, B_ ) pair is chosen, the sum is multiplied by _A_ , and then _B_ is added: that is stationarity.

The notation may be a bit perplexing: _An, Bn, A, B_ are all random rather than deterministic, and “a.s.” is short-hand for “almost surely”: the sum converges except for an event of probability 0. Conditions for convergence have been sharpened over the years; roughly, _An_ must be a contraction “on average”. Following work by Vervaat (1979) and Brandt (1986), definitive results were achieved by Bougerol and Picard (1992). To state the result, let _∥∥_ be a matrix norm on R<sup>_d_</sup> . Suppose that ( _An, Bn_ ) are i.i.d. for _n_ = 1 _,_ 2 _, . . ._ , with


where _x_<sup>+</sup> = _x_ when _x >_ 0 and _x_<sup>+</sup> = 0 when _x <_ 0. A subspace _L_ of R<sup>_d_</sup> is “invariant” if _P {X_ 1 _∈ L|X_ 0 = _x}_ = 1 for all _x ∈ L_ .

ITERATED RANDOM FUNCTIONS

7

**Theorem 2.1.** _Assume (2.6) and define the Markov chain Xn by (2.4). Suppose that the only invariant subspace of_ R<sup>_d_</sup> _is_ R<sup>_d_</sup> _itself. The infinite random series_


_converges a.s. to a finite limit if and only if_


_If (2.8) holds, the distribution of (2.7) is the unique invariant distribution for the Markov chain Xn._

The moment assumptions in Theorem 2.1 cannot be essentially weakened; see Goldie and Maller (1997). Of course, the Markov chain (2.4) can be defined when _An_ is expanding rather than contracting, but different normings are required for convergence. Anderson (1959) and Rachev-Samorodnitzky (1995) prove central limit theorems in the non-contractive case. On a lighter note, Embree and Trefethen (1998) use this machinery with _d_ = 2 to study Fibonacci sequences with random signs and a damping parameter _β_ , so _Xn_ +1 = _Xn ± βXn−_ 1.

**2.3. Fractal images.** This section shows how iterated random affine maps can be used to draw pictures in two dimensions. Fix ( _a_ 1 _, b_ 1) _, . . . ,_ ( _ak, bk_ ). Each _ai_ is a 2 _×_ 2 contraction, while _bi_ is a 2 _×_ 1 vector: _fi_ ( _x_ ) = _aix_ + _bi_ is the associated affine map of the plane into itself, which is Lipschitz because _ai_ is a contraction. Fix positive weights _w_ 1 _, . . . , wk_ , with _w_ 1 + _· · ·_ + _wk_ = 1. These ingredients specify a Markov chain _{Xn}_ moving through R<sup>2</sup> . Starting at _x_ , the chain proceeds by choosing _i_ at random with probability _wi_ and moving to _fi_ ( _x_ ).

Remarkably enough, given a target image, one can often solve for _{ai, bi, wi}_ so that the collection of points _{X_ 1 _, . . . , XN }_ forms a reasonable likeness of the target, at least with high probability. The technique is based on work of Dubins and Freedman (1966), Hutchinson (1981), and Diaconis and Shahshahani (1986). It has been developed further by Barnsley and Elton (1988) as well as Barnsley (1993), and is now widely used.

We outline the procedure. Theorem 1 applies, so there is a unique stationary distribution, call it _π_ . Let _δx_ stand for point mass at _x_ : that is, _δx_ ( _A_ ) = 1 if _x ∈ A_ and _δx_ ( _A_ ) = 0 if _x ∈/ A_ . According to standard theorems, the empirical distribution of _{X_ 1 _, . . . , XN }_ converges to _π_ :


Convergence is almost sure, in the weak-star topology. For any bounded continuous function _f_ on R<sup>2</sup> ,


PERSI DIACONIS AND DAVID FREEDMAN

8

See, for instance, Breiman (1960). In short, the pattern generated by the points _{X_ 1 _, . . . , XN }_ looks like _π_ when _N_ is large.

The parameters _{ai, bi, wi}_ must be chosen so that _π_ represents the target image. Here is one of the early algorithms. Suppose a picture is given as black and white points on an _m×m_ grid. Corresponding to this picture there is a discrete probability measure _ν_ on the plane, which assigns mass 1 _/b_ to each black point and mass 0 to each white point, _b_ being the number of black points. We want the stationary _π_ to approximate _ν_ . Stationarity implies that for any bounded continuous function _f_ on R<sup>2</sup> ,


The next idea is to replace � _fdπ_ on the right side of (2.9) by � _fdν_ :


For appropriate _f_ ’s, we get a system of equations that can be solved—at least approximately—for _{ai, bi, wi}_ . For instance, take _f_ to be linear or a low-order polynomial (and ignore complications due to unboundedness). In (2.10), the unknowns are the _ai, bi, wi_ . The equations are linear in the _w_ ’s but nonlinear in the other unknowns. Exact solutions cannot be expected in general, because _ν_ will be discrete while _π_ will be continuous. Still, the program is carried out by Diaconis and Shahshahani (1986) and by many later authors; see Barnsley (1993) for a recent bibliography. Also see Fisher (1994).

Figure 3. A fern drawn by a Markov chain

Figure 3 shows a picture of a fern. The parameters were suggested by Crownover (1995): _N_ = 10000, _k_ = 2, _w_ 1 = _._ 2993, _w_ 2 = _._ 7007, and


9

ITERATED RANDOM FUNCTIONS


**2.4. Tail behavior.** We turn now to the tail behavior of the stationary distribution. Some information can be gleaned from the moments, and invariance gives a recursion. We discuss (a bit informally) the case _d_ = 1. Let ( _An, Bn_ ) be i.i.d. pairs of real-valued random variables. Define the Markov chain _{Xn}_ by (2.4), and suppose the chain starts from its stationary distribution _π_ . Write _L_ ( _X_ ) for the law of _X_ . Then _L_ ( _X_ 1) = _L_ ( _A_ 1 _X_ 0 + _B_ 1), which implies _E_ ( _X_ 0) = _E_ ( _X_ 1) = _E_ ( _A_ 1) _E_ ( _X_ 0) + _E_ ( _B_ 1); so _E_ ( _X_ 0) = _E_ ( _B_ 1) _/_ [1 _− E_ ( _A_ 1)]. Similar expressions can be derived for higher moments and _d >_ 1. See, for instance, Vervaat (1979) or Diaconis and Shashahani (1986); also see (6.4) below.

Moments may not exist, or may not capture relevant aspects of tail behavior. Under suitable regularity conditions, Kesten (1973) obtained estimates for the tail probabilities of the stationary _π_ . For instance, when _d_ = 1, he shows there is a positive real number _κ_ such that _π_ ( _t, ∞_ ) _≈ C_ + _/t_<sup>_κ_</sup> and _π_ ( _−∞, −t_ ) _≈ C−/t_<sup>_κ_</sup> as _t →∞_ . Goldie (1991) gives a different proof of Kesten’s theorem and computes _C±_ ; also see Babillot et al. (1997). Of course, there is still more to understand. For example, if _An_ is uniform on [0 _,_ 1], _Zn_ is independent Cauchy, and _Bn_ = (1 _− An_ ) _Zn_ , the stationary distribution for _{Xn}_ is Cauchy. Thus, the conclusions of Kesten’s theorem hold—although the assumptions do not. Section 7.3 contains other examples of this sort. It would be nice to have a theory that handles tail behavior in such examples.

**2.5. Fine Structure.** Even with an explicit representation for the stationary distribution, there are still many questions. Consider the chain described by equation (1.2). As in (1.3), the stationary distribution is the law of


the _ξn_ being i.i.d. with _P_ ( _ξn_ = _±_ 1) = 1 _/_ 2. We may ask about the “type” of _π_ : is this measure discrete, continuous but singular, or absolutely continuous? (The terminology is reviewed below.) By the “law of pure types”, mixtures cannot arise; and discrete measures can be ruled out too. See Jessen and Wintner (1935).

If _a_ = 1 _/_ 2, then _π_ is just Lebesgue measure on [ _−_ 2 _,_ 2]. If 0 _< a <_ 1 _/_ 2, then _π_ is singular. Indeed,


takes on at most 2<sup>_N_</sup> distinct values. For the remainder term,


Hence, _π_ concentrates on a set of of intervals of total length 2<sup>_N_</sup> _a_<sup>_N_</sup> _/_ (1 _− a_ ), which tends to 0 as _N_ gets large—because _a <_ 1 _/_ 2.

It is natural to guess that _π_ is absolutely continuous for _a >_ 1 _/_ 2. However, this is false. For example, if _a_ = ( _√_ 5 _−_ 1) _/_ 2 = _._ 618 _. . ._ , then _π_ is singular: see

PERSI DIACONIS AND DAVID FREEDMAN

10

Erd¨os (1939, 1940). Which values of _a_ give singular _π_ ’s? This problem has been actively studied for 50 years, with no end in sight. See Garsia (1962) for a review of the classical work. There was a real breakthrough when Solomyak (1995) proved that _π_ is absolutely continuous for almost all values of _a_ in [1 _/_ 2 _,_ 1]; also see Peres and Solomyak (1996, 1998).

**2.6. Terminology.** A “discrete” probability assigns measure 1 to a countable set of points, while a “continuous” probability assigns measure 0 to every point. A “singular” probability assigns measure 1 to a set of Lebesgue measure 0. By contrast, an “absolutely continuous” probability has a density with respect to Lebesgue measure. Textbook examples like the Binomial and Poisson distributions are discrete; the Normal, Cauchy, and Beta distributions are absolutely continuous. Ordering the rationals in [0 _,_ 1] and putting mass 1 _/_ 2<sup>_n_</sup> on the _n_ th rational gives you an interesting discrete probability. The uniform distribution on the Cantor set in [0 _,_ 1] is continuous but singular.

**3. The Propp-Wilson Algorithm.** This remarkable algorithm does exact Monte Carlo sampling from distributions on huge finite state spaces. Let _S_ be the state space and let _π_ be a probability on _S_ . The objective is to make a random pick from _π_ , on the computer. When _S_ is large and _π_ is complicated, the project can be quite difficult and the backward iteration is a valuable tool.

To begin with, there is a family of functions _{fθ_ : _θ ∈_ Θ _}_ from _S_ to _S_ and a probability _µ_ on Θ, so that _π_ is the stationary distribution of the forward chain on _S_ . In other words, for each _t ∈ S_ ,


These functions will be constructed below. In some cases, the Metropolis algorithm is useful (Metropolis et al., 1953). In the present case, as will be seen, the Gibbs sampler is the construction to use. The probability _µ_ on Θ will be called the “move measure”: the chain moves by picking _θ_ from _µ_ and going from _s ∈ S_ to _fθ_ ( _s_ ). If the construction is successful, the backward iterations


will converge almost surely to a limiting random variable whose distribution is _π_ . (A sequence in _S_ converges if it is eventually constant, and _θ_ 1 _, θ_ 2 _, . . ._ are independent draws from the move measure _µ_ on Θ.)

Convergence is easier to check if there is monotonicity. Suppose _S_ is a partially ordered set; write _s < t_ if _s_ precedes _t_ . Suppose too there is a smallest element 0 and a largest element 1. With partial orderings, the existence of a largest element is an additional assumption, even for a finite set; likewise for smallest. Finally, suppose that each _fθ_ is monotone: _s < t_ implies _fθ_ ( _s_ ) _≤ fθ_ ( _t_ ). Now convergence is forced if, for some _n_ ,


ITERATED RANDOM FUNCTIONS

11

This takes a moment to verify. Among other things, convergence would not be forced if we had equality on the forward iteration.

Propp and Wilson (1996, 1998) turn these observations into a practical algorithm for choosing a point at random from _π_ . They make a sequence _θ_ 1 _, θ_ 2 _, θ_ 3 _, . . ._ of independent picks from the move measure _µ_ in (3.1), and compute the backward iterations (3.2). At each stage, they check to see if (3.3) holds. If so, the common value—of the left side and the right side—is a pick from the exact stationary distribution _π_ . The algorithm generates a random element of _S_ whose distribution is the sought-for _π_ itself, rather than an approximation to _π_ ; there is an explicit test for convergence; and in many situations, convergence takes place quite rapidly. These three features are what make the algorithm so remarkable.

By way of example, take the Ising model on an _n × n_ grid; a reference is Kinderman and Snell (1980). The state space _S_ consists of all functions _s_ from _{_ 1 _, . . . , n} × {_ 1 _, . . . , n}_ to _{−_ 1 _,_ +1 _}_ . The standard (barbaric) notation has _S_ = _{±_ 1 _}_<sup>[</sup><sup>_n_]</sup><sup>_×_[</sup><sup>_n_]</sup> . In the partial order, _s < t_ iff _sij ≤ tij_ for all positions ( _i, j_ ) in the grid, and _s̸_ = _t_ . A boundary condition may be imposed, for instance, that _s_ = +1 on the perimeter of the grid. The minimal state is _−_ 1 at all the unconstrained positions; the maximal state is +1 at all the unconstrained positions.

The probability distribution to be simulated is


Here, _β_ is a positive real number and _Cβ_ is a normalizing constant—which is quite hard to compute if _n_ is large. In the exponent, _H_ ( _s_ ) counts sign changes. Algebraically,


The indices _i, j, k, ℓ_ run from 1 to _n_ , and the position ( _i, j_ ) must be adjacent to ( _k, ℓ_ ): for instance, the position (2 _,_ 2) is adjacent to (2 _,_ 3) but not to (3 _,_ 3).

A “single site heat bath”(a specialized version of the Gibbs sampler) is used to construct a chain with limiting distribution _π_ . From state _s_ , the chain moves by picking a site ( _i, j_ ) on the grid


and re-randomizing the value at ( _i, j_ ). More specifically, let _sij_ + agree with _s_ at all sites other than ( _i, j_ ); let _sij_ + = +1 at ( _i, j_ ). Likewise, _sij−_ agrees with _s_ at all sites other than ( _i, j_ ), but _sij−_ = _−_ 1 at ( _i, j_ ). Let


and _π_ ( _−_ ) = 1 _− π_ (+). The chance of moving to _sij_ + from _s_ is _π_ (+); the chance of moving to _sij−_ is _π_ ( _−_ ). In other words, the chance of re-randomizing to +1 at ( _i, j_ ) is _π_ (+). This chance is computable because the ugly constant _Cβ_ has canceled out.

PERSI DIACONIS AND DAVID FREEDMAN

12

In principle, _π_ (+) and _π_ ( _−_ ) depend on the site ( _i, j_ ) and on values of _s_ at sites other than ( _i, j_ ); we write _π_ ( _± | i j s_ ) when this matters. Of course, _π_ (+) is just the conditional _π_ -probability that _sij_ = +, given the values of _s_ at all other sites. As it turns out, only the sites adjacent to ( _i, j_ ) affect _π_ (+), because the values of _s_ at more remote sites just cancel:


The sum is over the sites ( _k, ℓ_ ) adjacent to ( _i, j_ ). Equation (3.6) is in essence the “Markov random field” property for the Ising model.

The single site heat bath can be cycled through sites ( _i, j_ ) on the grid, or the site can be chosen at random. We follow the latter course, although the former is computationally more efficient. The algorithm is implemented using the backward iteration. The random functions are _fθ_ ( _s_ ). Here, _s ∈ S_ is a state in the Ising model while _θ_ = ( _i, j, u_ ) consists of a position ( _i, j_ ) in the grid and a real number _u_ with 0 _< u <_ 1. The position is randomly chosen in the grid, and _u_ is random over (0 _,_ 1). The function _f_ is defined as follows: _s_<sup>_′_</sup> = _fiju_ ( _s_ ) agrees with _s_ except at position ( _i, j_ ). There, _s_<sup>_′_</sup> _ij_<sup>= +1if</sup><sup>_u < π_(+),and</sup><sup>_s′_</sup> _ij_<sup>=</sup><sup>_−_1otherwise.</sup> Two things must be verified:

- (i) _π_ is stationary, and

- (ii) _fθ_ is monotone.

Stationarity is obvious. For monotonicity, fix a site ( _i, j_ ), two states _s, t_ with _s ≤ t_ , and _u ∈_ (0 _,_ 1). Clearly, _fiju_ ( _s_ ) _≤ fiju_ ( _t_ ) except perhaps at ( _i, j_ ). At this special site, we must prove


But the two conditional probabilities in (3.7) can be evaluated by (3.6), and


The condition _β >_ 0 makes _fθ_ monotone increasing rather than monotone decreasing. The backward iteration completes after a finite, random number of steps, essentially by Theorem 1. Completion can be tested explicitly using (3.3). And the algorithm makes a random pick from _π_ itself, rather than an approximation to _π_ .

There are many variations on the Propp-Wilson algorithm, including some for point processes: see Mo/ller (1998) or H¨aggstr¨om et al. (1998). A novel alternative is proposed by Fill (1998), who includes a survey of recent literature and a warning about biases due to aborted runs. There are no general bounds on the time to “coupling”, which occurs when (3.3) is satisfied: chains starting from 0 and from 1, but using the same _θ_ ’s, would have to agree from that time onwards. Experiments show that coupling generally takes place quite rapidly for the Ising model with _β_ below a critical value, but quite slowly for larger _β_ ’s. Propp and Wilson (1996)

ITERATED RANDOM FUNCTIONS

13

have algorithms that work reasonably well for all values of _β_ —even above the critical value—and for grids up to size 2100 _×_ 2100. For more discussion, and a comparison of the Metropolis algorithm with the Gibbs sampler, see H¨aggstr¨om and Nelander (1998).

Brown and Diaconis (1997) show that a host of Markov chains for shuffling and random tilings are monotone. These chains arise from hyperplane walks of Bidigare, Hanlon and Rockmore (1997). The analysis gives reasonably sharp bounds on time to coupling. Monotonicity techniques can be used for infinite state spaces too. For instance, such techniques have been developed by Borovkov (1984) and Borovkov and Foss (1992) to analyze complex queuing networks—our next topic.

**4. Queuing theory.** The existence of stationary distributions in queuing theory can often be proved using iterated random functions. There is an interesting twist, because the functions are generally not strict contractions, even on average. We give an example, and pointers to a voluminous literature. In one relatively simple model, the G/G/1 queue, customers arrive at a queue with i.i.d. interarrival times _U_ 1 _, U_ 2 _, . . . ._ The arrival times are the partial sums 0 _, U_ 1 _, U_ 1 + _U_ 2 _, . . . ._ The _j_ th customer has service time _Vj_ ; these too are i.i.d., and independent of the arrival times. Let _Wj_ be the waiting time of the _j_ th customer—the time before service starts. By definition, _W_ 0 = 0. For _j >_ 0, the _Wj_ satisfy the recursion


Indeed, the _j_ th customer arrives at time _Tj_ = _U_ 1 + _· · ·_ + _Uj_ and waits time _Wj_ , finishing service at time _Tj_ + _Wj_ + _Vj_ . The _j_ +1st customer arrives at time _Tj_ + _Uj_ +1. If _Tj_ + _Uj_ +1 _> Tj_ + _Wj_ + _Vj_ , then _Wj_ +1 = 0; otherwise, _Wj_ +1 = _Wj_ + _Vj − Uj_ +1. The waiting-time process _{ Wj_ : _j_ = 0 _,_ 1 _, . . . }_ can therefore be generated by iterating the random functions


The parameter _θ_ should be chosen at random from _µ_ = _L_ ( _Vj − Uj_ +1), which is a probability on the real line R.

The function _fθ_ is a weak contraction but not a strict contraction: the Lipschitz constant is 1. Although Theorem 1 does not apply, the backward iteration still gives the stationary distribution. Indeed, the backward iteration starting from 0 can be written as


Now there is a magical identity:


This identity holds for any real numbers _θ_ 1 _, . . . , θn_ . Feller (1971, p. 272) asks the reader to prove (4.4) by induction, and _n_ = 1 is trivial. Separating the cases _y ≤_ 0

14 PERSI DIACONIS AND DAVID FREEDMAN

and _y >_ 0, one checks that ( _x_ + _y_<sup>+</sup> )<sup>+</sup> = max _{_ 0 _, x, x_ + _y}_ . That does _n_ = 2. Now put _θ_ 2 for _x_ and _θ_ 3 for _y_ :


That does _n_ = 3. And so forth. If the starting point is _x_ rather than 0, you just need to replace _θn_ in (4.4) by _θn_ + _x_ .

In the queuing model, _{Uj}_ are i.i.d. by assumption, as are _{Vj}_ ; and the _U_ ’s are independent of the _V_ ’s. Set _Xj_ = _Vj −Uj_ +1 for _j_ = 1 _,_ 2 _, . . ._ . So the _Xj_ are i.i.d. too. It is easily seen—given (4.3–4)—that the Markov chain _{Wj_ : _j_ = 0 _,_ 1 _, . . . , ∞}_ has for its stationary distribution the law of


provided the limit is finite a.s.

Many authors now use the condition _E_ ( _X_ 1) _<_ 0 to insure convergence, via the strong law of large numbers: _X_ 1 + _· · ·_ + _Xj ≈ jE_ ( _X_ 1) _→−∞_ a.s., so the maximum of the partial sums is finite a.s. In a remarkable paper, Spitzer (1956) showed that no moment assumptions are needed.

**Theorem 4.1.** _Suppose the random variables X_ 1 _, X_ 2 _, . . . are i.i.d. The limit in (4.5) is finite a.s. if and only if_


_Under this condition, the limit in (4.5) has an infinitely divisible distribution with characteristic function_


_where ψj_ ( _t_ ) = _E{_ exp[ _it_ ( _X_ 1 + _· · ·_ + _Xj_ )<sup>+</sup> ] _} and_ exp _x_ = _e_<sup>_x_</sup> _._

The “G/G/1” in the G/G/1 queue stands for general arrival times, general service times, and one server: “general” means that _L_ ( _Uj_ ) and _L_ ( _Vj_ ) are not restricted to parametric families. The recent queuing literature contains many elaborations, including for instance queues with multiple servers and different disciplines; see Baccelli (1992) among others. There are surveys by Borovkov (1984) or Baccelli and Br´emaud (1994). One remarkable achievement is the development of a sort of linear algebra for the real numbers under the operation ( _x, y_ ) _→_ max _{x, y}_ and _x → x_<sup>+</sup> . The book by Baccelli et al. (1992) gives many applications; queues are discussed in Chapter 7. The random-iterations idea helps to unify the arguments.

ITERATED RANDOM FUNCTIONS

15

**5. Rigor.** This section gives a more formal account of the basic setup; then Theorem 1 is proved in Section 5.2. The theorem and the main intermediate results are known: see Arnold and Crauel (1992), Barnsley and Elton (1988), Dubins and Freedman (1966), Duflo (1997), Elton (1990), or Hutchinson (1981). Even so, the self-contained proofs given here may be of some interest.

**5.1. Background.** Let ( _S, ρ_ ) be a complete, separable metric space. Then _f ∈_ Lip _K_ if _f_ is a mapping of _S_ into itself, with _ρ_ [ _f_ ( _x_ ) _, f_ ( _y_ )] _≤ Kρ_ ( _x, y_ ). The least such _K_ is _Kf_ . If _f_ is constant, then _Kf_ = 0. If _f ∈_ Lip _K_ for some _K < ∞_ , then _f_ is “Lipschitz”; otherwise, _Kf_ = _∞_ . Of course, these definitions are relative to _ρ_ . We pause for the measure theory. Let _S_ 0 be a countable dense subset of _S_ , and let _X_ be the set of all mappings from _S_ 0 into _S_ . We endow _X_ with the product topology and product _σ_ -field. Plainly, _X_ is a complete separable metric space. Let _X_ be the space of Lipschitz functions on _S_ . The following lemma puts a measurable structure on _X_ .

---

[← 3 May 1998](01-3-may-1998.md) · [Up: contents](index.md) · [Lemma 5.1. →](03-lemma-5-1.md)
