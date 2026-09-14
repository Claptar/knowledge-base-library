---
title: Spin glasses
source: https://www.stat.berkeley.edu/~aldous/205B/austin_arrays.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/austin_arrays.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Spin glasses

**Source:** [`austin_arrays.pdf`](https://www.stat.berkeley.edu/~aldous/205B/austin_arrays.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **11 Introduction to spin glasses**

Some terminology from physics:

‘ **Glass** ’: a material which is hard and inflexible (like a solid) but is not completely ordered or lattice-like in its microscropic structure (thus, unlike a crystal or simple metals).

‘ **Spin** ’: pertaining to the magnetic spins of ions in a material.

‘ **Spin glass** ’: a material, effectively solid, which contains some irregular distribution of magnetizable ions.

Basic laboratory examples: Cadmium telluride (a non-magnetizable crystalline compound of cadmium and tellurium) doped with some easily-magnetized atoms, e.g. of iron or nickel.

Spin glasses are complicated because the magnetic interactions between ions depend heavily on the exact distance between them, the irregular distances in a spin glass give rise to irregular interactions and hence a locally highly-complicated response to an external magnetic field.

33

#### **The basic model**

In order to model a spin glass, consider the state space _{−_ 1 _,_ 1 _}_<sup>_N_</sup> , where an element _σ_ = ( _σn_ ) _n≤N_ is interpreted as an assignment of spins to each of _N_ magnetic ions. In this model each spin can only be either ‘up’ or ‘down’; more sophisticated models might use (S<sup>2</sup> )<sup>_N_</sup> or suchlike.

Basic procedure of modelling in statistical physics: determine (from physical considerations) a ‘Hamiltonian’


with the interpretation that _H_ ( _σ_ ) is the internal magnetic energy of the system when it is in state _σ_ . Now suppose the material interacts with its environment at some temperature _T_ , so that its state keeps changing due to microscopic interactions. Then the basic prescription from thermodynamics is that the _proportion of time spent in different states_ is given by the **Gibbs measure at temperature** _T_ :


where _β_ := 1 _/T_ and


is the normalizing constant, which is called the **partition function** .

Following standard practice in physics, we will sometimes use _⟨−⟩β_ to denote an average over any number of independent states drawn from _γβ_ . For instance, if _f_ : ( _{−_ 1 _,_ 1 _}_<sup>_N_</sup> )<sup>2</sup> _−→_ R then


Subscripts such as ‘ _β_ ’ may also be dropped when this can cause no confusion. When several independently-chosen states are invoked, as here, they are sometimes referred to as ‘replicas’.

In most sensible models, _Z_ ( _β_ ) is exponentially large as a function of _N_ , and the quantity of greatest interest is the first-order behaviour of the exponent. For this reason one now defines the **free energy** to be the quantity


34

In order to understand the material in thermal equilibrium, one wishes to describe the measure _γβ_ or the quantity _F_ ( _β_ ) as well as possible.

The key feature of a spin glass is that different pairs of spins interact in very different ways. This is reflected by a Hamiltonian of the form


in which the interaction constants _gij_ vary irregularly with the pair _{i, j}_ and can take either sign, so some pairs prefer to be aligned and some anti-aligned. Notice that among three indices _i_ , _j_ and _k_ , it can happen that two pairs prefer alignment but the third prefers anti-alignment, or that all three prefer anti-alignment, in which case the assignment of spins that minimizes _H_ may be far from obvious. This phenomenon (and extension to larger numbers of indices) is called **frustration** .

In realistic models, the indices _i, j_ are locations in space, and one assumes that _gi,j_ = 0 if _|i − j|_ is large. The irregularity appears for nearby _i, j_ . Among nonzero interactions, a simple way to produce a spin glass model is to _choose the interaction constants themselves at random_ (so now there are two levels of randomness involved). The basic model here is the Edwards-Anderson model [MPV87]. Almost nothing is known rigorously about this model.

To simplify, one can consider a mean field model, in which one ignores the spatial locations of the spins. Most classical is the **Sherrington-Kirkpatrick (‘SK’) model** (see the papers of Sherrington and Kirkpatrick in [MPV87]): let _gij_ be independent standard Gaussians on some background probability space (Ω _, F,_ P), and let _H_ be the random function


The normalization is chosen so that each of the random variables _H_ ( _σ_ ) has variance _N_ , which turns out to be the regime of greatest interest. This model is still very complicated, but recent work has thrown considerable light onto its structure.

An even simpler toy model, which nevertheless begins to show some interesting behaviour, is the **Random Energy Model (‘REM’) model** , introduced by Derrida [Der81]. In this case one lets the values _H_ ( _σ_ ) be centred Gaussians of variance _N_ and all simply independent for different _σ_ .

Having chosen one of these models, let _γβ,N_ be the random Gibbs measure on _{−_ 1 _,_ 1 _}_<sup>_N_</sup> resulting from this Hamiltonian, and let _FN_ ( _β_ ) be the **expected free**

35

**energy** :


**Basic (vague) question:** What are the values of _FN_ ( _β_ ) or the typical structure of _γβ,N_ as functions of these random interactions?

Recommended reading: [ASS07, Tal03, Pan10, Pan12, Panar]. A new version of Talagrand’s comprehensive book [Tal03] is in preparation, with Volume 1 already available [Tal11]. The classic physicists’ text on spin glasses is [MPV87].

#### **Connection to random optimization**

When physicists choose to study a mean-field model of a situation which in the real world involves some spatial variation, they do so simply because the mean-field model is simpler. Their hope is that it will still reveal some non-trivial structure which can then suggest fruitful questions to ask about a more realistic model. For instance, the Curie-Weiss model exhibits a phase transition much like the Ising model in two or three dimensions.

In fact, it remains contentious whether the SK model is worthwhile as a toy version of spatially-extended models. However, it was quickly realized that mean-field spin glass models have a much more solid connection with random optimization.

Consider again the random function _H_ : _{−_ 1 _,_ 1 _}_<sup>_N_</sup> _−→_ R defined in (10). When _β_ is large, the Gibbs measure _γβ,N_ , for which _γβ,N {σ}_ is proportional to exp( _−βH_ ( _σ_ )), should be concentrated on those configurations _σ ∈{−_ 1 _,_ 1 _}_<sup>_N_</sup> where ( _−H_ ( _σ_ )) is large<sup>3</sup> . Also, trivial estimates give


and hence


Dividing by _β_ and letting _β −→∞_ , we conclude that


> 3Unfortunately the sign conventions of statistical physics mean that we will be working with

> ( _−H_ ), rather that _H_ , throughout this discussion of optimization.

36

with a rate of convergence that does not depend on _N_ . Therefore we may take expectations, let _N −→∞_ and change the order of the limits, and hence obtain


where _F_ ( _β_ ) is the limiting free energy introduced above. Moreover, in many cases the random quantity _N_<sup><u>1</u>max</sup><sup>_σ_(</sup><sup>_−H_(</sup><sup>_σ_)) is known to concentrate around this limit-</sup> ing value as _N −→∞_ as a result of Gaussian concentration phenomena.

Thus, if we have a formula for _F_ ( _β_ ), then this gives a formula for the leadingorder behaviour of the random optimization problem max _σ_ ( _−H_ ( _σ_ )). This amounts to determining the maximum over _σ_ of a typical instance of the random function


(dropping a minus-sign now, since _−gij_ =d _gij_ ). This is an instance of the classical _Dean’s problem_ : given a population of individuals _{_ 1 _,_ 2 _, . . . , N }_ in which the like or dislike between individuals _i_ and _j_ is given by the (positive or negative) value _gij_ , the Dean would like to separate them into two classes (which will correspond to _{i_ : _σi_ = 1 _}_ and _{i_ : _σi_ = _−_ 1 _}_ ) so that the overall level of comfort is maximized: that is, s/he needs the optimum way to put pairs that like each other into the same class, and pairs that dislike each other into different classes.

Amazingly, a good enough understanding of the SK model allows one to give an expression for _F_ ( _β_ ) (albeit very complicated), so that in principle one could actually estimate lim _β−→∞ F_ ( _β_ ) _/β_ this way and so obtain the correct constant _c_ in the estimate


The expression for _F_ ( _β_ ) is called the Parisi formula, and is given later in these notes. Although not simple, it can be estimated numerically, and using this the physicists made the prediction that _c_ (exists and) is approximately 0 _._ 7633 _. . ._ . The Parisi formula is now known rigorously [Tal06, Panar], so this is now a theorem up to the quality of those numerical methods.

What’s more, the exact distribution of the random coefficients _gij_ is not essential for this calculation. Provided these r.v.s have mean zero, have variance one and have bounded third moments, the resulting behaviour of the free energy as _N −→∞_ will be the same: see Carmona and Hu [CH06].

37

This means that other random variants of the Dean’s problem can be solved this way. Perhaps the most classical is an instance of MAX-CUT (whose exact solution for deterministic graphs is NP-complete in general). In this case the pairwise interactions _gij_ are not Gaussian, but take two values according to the adjacency matrix of an Erd˝os-R´enyi random graph _G_ ( _N, p_ ), with those two values chosen to give mean zero and variance one. A concentration argument shows that the expected best cut must cut _N_<sup>2</sup> _p/_ 4 + o( _N_<sup>2</sup> ) of the edges, but analysis of this spin-glass model gives a value for the next term. The prediction of the physicists is that for this random MAX-CUT problem one has


where again _c_ = 0 _._ 7633 _. . ._ . With the rigorous proof fo the Parisi formula, this, too, is now a theorem, up to the quality of some numerical methods. See [MPV87, Chapter IX] for a more complete account of applications to random optimization.

### **12 Describing asymptotic structure**

We return to our basic questions about the SK model. As shown in the previous section, the application to random optimization will be served by having a good enough asymptotic formula for _FN_ ( _β_ ). However, we will see that this problem is intimately related to understanding the geometry of the Gibbs measures _γβ,N_ .

First we must decide in what terms to try to describe _γβ,N_ . The basic idea here is that two configurations _σ, σ_<sup>_′_</sup> _∈{−_ 1 _,_ 1 _}_<sup>_N_</sup> are similar if they agree in most coordinates. More formally, this means that they are close in Hamming metric, or, equivalently, in any of the metrics inherited by regarding _{−_ 1 _,_ 1 _}_<sup>_N_</sup> as a subset of _ℓ_<sup>_N_</sup> _p_<sup>(i.e., R</sup><sup>_N_with the</sup><sup>_ℓp_-norm) for any fixed choice of</sup><sup>_p ∈_[1</sup><sup>_, ∞_).</sup>

In fact, in this setting it is most natural to think of _{−_ 1 _,_ 1 _}_<sup>_N_</sup> as a subset of _ℓ_<sup>_N_</sup> 2<sup>,becausethatspacecapturesthestructureoftherandomvariables</sup><sup>_H_(</sup><sup>_σ_),and</sup> specifically their covariances. To see this, compute


Since E( _gijgi′j′_ ) is zero unless _ij_ = _i_<sup>_′_</sup> _j_<sup>_′_</sup> , because the interactions are independent, this simplifies to


38


So the covariances of the random function _H_ are given by the structure of _{−_ 1 _,_ 1 _}_<sup>_N_</sup> as a subset of Hilbert space; in particular, the problems of estimating the structure of _γβ,N_ and the value of _FN_ ( _β_ ) are unchanged if we change _{−_ 1 _,_ 1 _}_<sup>_N_</sup> by a rigid rotation in _ℓ_<sup>_N_</sup> 2<sup>.Motivatedbythis,wewillthinkof</sup><sup>_γβ,N_asarandom</sup> probability measure on a Hilbert space, and try to give a ‘coarse’ description of it as such.

By a ‘coarse’ description of _γβ,N_ , we really want an idea of the limiting behaviour of _γβ,N_ as _N −→∞_ in terms of some meaningful notion of convergence for random probability measures on Hilbert spaces. Since we really care only about the structure of _γβ,N_ up to orthogonal rotations of _ℓ_ 2<sup>_N_, convergence of the associ-</sup> ated Gram-de Finetti matrices obtained by sampling offers an ideal such notion:

Do the random measures _γβ,N_ sampling-converge, and if so what is their limit?

### **13 More tools: facts about Gaussians**

Before proceeding with spin glasses, we need to describe two basic tools from the study of Guassian processes. The first is a concentration inequality; see, for instance, Ledoux [Led01].

**Proposition 13.1** _Suppose that F_ : R<sup>_M_</sup> _−→_ R _is a function such that_


_and let g_ = ( _g_ 1 _, . . . , gM_ ) _be a sequence of independent standard Gaussian r.v.s. Then for each t >_ 0 _we have_


Our main application of this is to the free energy _N_<sup><u>1</u>log</sup><sup>_ZN_(</sup><sup>_β_), whose expecta-</sup> tion is _FN_ ( _β_ ) (equation (11)). In the case of the SK model with Hamiltonian (10), a little calculus gives


(regarding _gi,j_ as just a variable here, rather than a sample from a Gaussian), where we recall that the notation ‘ _⟨−⟩β,N_ ’ refers to an average over any number of independently-drawn samples from _γβ,N_ ; see the discussion around equation (9). From this one easily deduces that _FN_ ( _β_ ) is ( _β/√N_ )-Lipschitz as a function of ( _gi,j_ ) _i,j_ . Using this in Proposition 13.1, we conclude that


Similarly, in the case of the REM we may write _H_ ( _σ_ ) = _√Ngσ_ , where each _gσ_ will be drawn independently from a standard Gaussian. Therefore in this case one obtains


which again gives a Lipschitz constant of at most _β/√N_ , and so the same concentration inequality (12).

The second tool we introduce here is Gaussian integration by parts. This simple piece of calculus has become ubiquitous in the study of spin glass models, as well as many others in statistical physics.

**Proposition 13.2 (Gaussian integration by parts)** _If g is a centred Gaussian r.v. and F_ : R _−→_ R _is smooth and of moderate growth at ∞ (polynomial growth is fine), then_


This follows by a basic integration by parts using the density of the Gaussian, since


In the study of spin glasses, Gaussian integration by parts is often used as part of ‘Gaussian interpolation’. Suppose _g_ and _g_<sup>_′_</sup> are _M_ -dimensional Gaussian r.v.s with different variance-covariance matrices, _F_ : R<sup>_M_</sup> _−→_ R is a continuously differentiable function which does not grow too fast near _∞_ , and one wishes to compare the expectations E _F_ ( _g_ ) and E _F_ ( _g_<sup>_′_</sup> ). To use the interpolation method, one chooses an interpolating family of _M_ -dimensional Gaussian r.v.s _gt_ with _t ∈_ [0 _,_ 1]

40

such that _g_ 0 =d _g_ and _g_ 1 =d _g′_ , and then uses Gaussian integration by parts to evaluate (or at least estimate)


Of course, there are many possibly ways to choose the interpolating family, and often the success of the method depends on a very clever choice; this is why Talagrand calls it the ‘smart path method’. One of its earliest successes was the following basic result of Guerra and Toninelli; see [GT02] for the smart choice of path.

**Lemma 13.3** _In the Sherrington-Kirkpatrick model at a fixed value of β,_


Using Fekete’s Lemma, this has the crucial consequence that lim _N −→∞ FN_ ( _β_ ) exists for all _β_ .

### **14 The Aizenman-Sims-Starr scheme and the Parisi formula**

Suppose that _γβ,N_ is known to sampling-converge to some limiting random measure _γβ_ . Building on a calculational method of Guerra [Gue03], Aizenman, Sims and Starr [ASS07] showed how this _γβ_ then provides a formula for the limiting free energy _F_ ( _β_ ). This insight made it possible to put Parisi’s original predictions about the SK model (see below) into a more general mathematical framework, and is the basis for an approach to the Parisi formula via understanding the geometry of _γβ_ .

The first idea here is to write


with _Ai_ = E log _Zi_ +1 _−_ E log _Zi_ . If one can show that these quantities _Ai_ tend to a constant, then of course _FN_ will also tend to that constant. In a sense, this realizes _FN_ as the ‘logarithmic increment’ in the growing sequence of partition functions _ZN_ .

41

So now let us try to compare E log _ZN_ with E log _ZN_ +1. First, identify _{−_ 1 _,_ 1 _}_<sup>_N_+1</sup> with _{−_ 1 _,_ 1 _}_<sup>_N_</sup> _× {−_ 1 _,_ 1 _}_ , and for ( _σ, ε_ ) _∈{−_ 1 _,_ 1 _}_<sup>_N_</sup> _× {−_ 1 _,_ 1 _}_ write


where


and


It is easy to show that the last term in this decomposition of _HN_ +1 makes asymptotically negligible contribution to _FN_ , so we now ignore it. Next, _HN_<sup>_′_(</sup><sup>_σ_) is</sup> almost the same as _HN_ ( _σ_ ): only the coefficient is slightly wrong. Since a sum of two independent Gaussians is still Gaussians, as random variables we can correct this with a small extra term:


where


where the _gij_<sup>_′_are new independent standard Gaussians.</sup>

Notice that if we condition on _gij_ for _i, j ≤ N_ , then (13) and (14) define two two further independent Gaussian processes on _{−_ 1 _,_ 1 _}_<sup>_N_</sup> with covariances given by


With a little analysis one can show that the multiplicative factor of _NN_ +1<sup>isalso</sup> unimportant here.

42

Having set up this notation, our desired comparison becomes


Letting _ZN_<sup>_′_:=�</sup> _σ_<sup>exp(</sup><sup>_−βH_</sup> _N_<sup>_′_(</sup><sup>_σ_)),wemayaddandsubtractE log</sup><sup>_Z_</sup> _N_<sup>_′_inthe</sup> above to obtain


where _γβ,N_<sup>_′_is the random Gibbs measure on</sup><sup>_{−_1</sup><sup>_,_1</sup><sup>_}N_corresponding to the Hamil-</sup> tonian _HN_<sup>_′_(which is not conceptually different from the Gibbs measure for</sup><sup>_HN_),</sup> and where the expectation is in both _γβ,N_<sup>_′_andtheindependentrandomvariables</sup> _zN_ ( _σ_ ), _yN_ ( _σ_ ).

Importantly, one can (at least formally) make sense of this last expression for _any_ random Hilbert space measure _γ_ . Suppose _γ_ is such a measure, say on the unit ball _B_ of a Hilbert space. We need independent Gaussian random linear functionals


Provided _γ_ and its support are not too irregular, one can construct such random functionals using the theory of Gaussian Hilbert spaces, essentially uniquely. In

43

terms of these one may now write down the analog of the above expression:


where E<sup>_′_</sup> denotes expectation in all of the random data _γ_ , _z_ and _y_ (ignoring issues of integrability here). Since the laws of _z_ and _y_ are determined by their covariances, this quantity is really a functional of the law of the random measure _γ_ . We will write it as Φ(law _γ_ ).

The usefulness of this is as follows: if we can describe a sampling-limit random measure _γβ_ for _γβ,N_<sup>_′_,thenatleastheuristicallyitshouldfollowthat</sup><sup>_AN_tendsto</sup> the limiting value Φ(law _γβ_ ). This isn’t quite immediate, since one must prove that the sampling-convergence _γβ,N_<sup>_′−→γβ_is strong enough to imply the convergence</sup> of these Φ-values. However, that continuity can be proved using more machinery from Gaussian processes: it is implied by the following, which is Theorem 1.3 in [Panar].

**Theorem 14.1** _For each ε >_ 0 _, there are n ≥_ 1 _and a continuous function Fε_ : [ _−_ 1 _,_ 1]<sup>_n_2</sup> _−→_ R _such that_


_for all random measures γ on B._

Thus, if we knew the sampling convergence of _γβ,N_<sup>_′_to</sup><sup>_γβ_, it would follow that</sup>


This is the precise sense in which a good enough understanding of the asymptotic structure of _γβ,N_ (or, to be precise, the very-similar _γβ,N_<sup>_′_) would give the asymp-</sup> totic value of _FN_ ( _β_ ).

Unfortunately, this convergence is not known. However, recent work of Panchenko has yielded results almost as good: with some tweaking, the possible subsequential sampling-limits of the sequence ( _γβ,N_<sup>_′_)</sup><sup>_N≥_1have been restricted to a very precise</sup> family called the Ruelle Probability Cascades. This restriction is enough to express lim _N −→∞ FN_ ( _β_ ) in terms of a rather more concrete variational problem. If we temporarily hide some important technical issues, an overview of the argument is as follows. For a proper treatment of these and related ideas, see [ASS07, AC, Pan12].

44

Let _M_ denote the space of all laws of random probability measures on _B_ , and let _M_ lim _⊆M_ be the set of subsequential limits of the sequence ( _γβ,N_<sup>_′_)</sup><sup>_N≥_1(all</sup> taken up to random orthogonal rotations, in view of Proposition 8.3). The definition of _AN_ certainly gives


so in view of the above reasoning this implies


On the other hand, for any _M ≥_ 1, similar steps to the above allow one to express the difference


as a (slightly more complicated) functional Φ _M_ applied to the random Gibbs measure _γβ,M,N_<sup>_′′_with Hamiltonian</sup>


This new measure _γβ,M,N_<sup>_′′_should still be very close to</sup><sup>_γ_</sup> _β,N_<sup>_′_if</sup><sup>_N≫M_.</sup>

For this functional, Aizenman, Sims and Starr showed in [ASS07] that one can prove the inequality

Φ _M_ (law _γβ,N,M_<sup>_′′_)</sup><sup>_≤_Φ</sup><sup>_M_(law</sup><sup>_γ_)</sup>

for any other random measure _γ_ on _B_ . Their proof uses a clever interpolation method based on Gaussian integration by parts, abstracted from a crucial earlier insight of Guerra [Gue03], which will not be explained here.

For a certain special subclass of laws _M_ ss _⊆M_ referred to as ‘stochastically stable’ (which will not be defined here), one has Φ _M_ = _M_ Φ, and hence if law _γ ∈ M_ ss then


Note this seems to go the other way from (16).

However, the Ruelle Probability Cascades _are_ all stochastically stable, so Panchenko’s results essentially give _M_ lim _⊆M_ ss. Therefore we may combine the above inequalities to deduce


45

where this infimum really runs only over the Ruelle Probability Cascades. For those special random measures, the functional Φ may be written out rather more explicitly, giving the famous Parisi formula:

**Theorem 14.2 (The Parisi formula, formulated as in [ASS07])** _As N −→∞, the random quantities FN_ ( _β_ ) _converge in probability to the deterministic quantity_


_where the infimum is taken over all right continuous non-decreasing functions_ [0 _,_ 1] _−→_ [0 _,_ 1] _, where_


_and where f_ ( _q, y_ ; _ϕ_ ) _for_ ( _q, y_ ) _∈_ [0 _,_ 1]<sup>2</sup> _is the solution to the PDE_


_subject to the boundary condition_


This extraordinary conclusion was contained among Parisi’s original predictions for this model. Before Panchenko was able to complete the program outlined above, the Parisi formula was first proved by Talagrand in [Tal06] using a different set of very subtle estimates (still mostly obtained from the Gaussian interpolation method). However, that earlier proof of Talagrand does not give so much information on the structure of the Gibbs measures, and I will not discussed it further here.

The Parisi formula still looks very complicated. What is important to understand, however, is that neither the PDE nor the variational problem over _ϕ_ that are involved in it is too difficult to approximate numerically, and so this gives a relatively ‘simple’ way to estimate lim _N −→∞ FN_ ( _β_ ), and hence also _N_<sup><u>1</u>max</sup><sup>_σ_(</sup><sup>_−HN_(</sup><sup>_σ_)).</sup> By contrast, directly estimating this maximum for a computer simulation of the random variables _H_ is prohibitively difficult for even moderately large _N_ . (On the other hand, it is still largely open to understand rigorously how continuous is the functional _P_ ( _ϕ, β_ ) in its argument _ϕ_ .)

46

Several important technical points have been ignored in the above discussion. Perhaps the most serious is that Panchenko does not prove that all limits of the sequence ( _γβ,N_<sup>_′_)</sup><sup>_N≥_1 are Ruelle Probability Cascades for the Sherrington-Kirkpatrick</sup> Hamiltonian itself. Rather, he proves that this holds ‘typically’ in a small neighbourhood of that Hamiltonian for an infinite-dimensional family of perturbations of it. This will be explained in a little more detail below in connexion with the Ghirlanda-Guerra identities, which are the principal ingredient in Panchenko’s proof. The key point is that one can find such perturbations such that:

- on the one hand, they do satisfy all of these identities, so that Panchenko’s argument gives the Ruelle-Probability-Cascade result;

- but on the other, they are asymptotically close enough to the unperturbed Sherrington-Kirkpatrick Hamiltonian that their specific free energies have the same leading-order behaviour in _N_ , so that they still give the correct evaluation of lim _N −→∞ FN_ ( _β_ ) for the Sherrington-Kirkpatrick model itself.

The last two sections of these notes will offer a rough discussion of the GhirlandaGuerra identities and their key geometric consequence: ultrametricity.

### **15 The Ghirlanda-Guerra identities and ultrametricity**

#### **The Parisi ansatz**

In addition to his formula, Parisi also predicted the salient asymptotic features of the structure of the measures _γβ,N_ as _N −→∞_ . This structure is now known to obtain for certain perturbations of the SK model, as mentioned above.

To introduce these, let _H_<sup>pert</sup> : _{−_ 1 _,_ 1 _}_<sup>_N_</sup> _−→_ R be a random function, independent from _H_ , of the form


for some choice of ( _xp_ ) _p≥_ 1 _∈_ [0 _,_ 1]<sup>N</sup> , and where all the coefficients _gi_ 1 _,...,ip_ are independent standard Gaussians. Using this, form the combined Hamiltonian


for some sequence of coefficients _sN_ .

47

Of course, the rather off-putting formula in (17) need not be seen as a natural model in its own right<sup>4</sup> , but as a convenient choice of a very general function which provides many extra parameters that we can tweak as needed. Note, for instance, that the spin-flip symmetry is broken if there are nonzero terms for any odd _p_ .

Now, the point is that if the coefficients _sN_ are small enough then one can show that this perturbation has only a higher-order effect on the free energy: to be precise,


Therefore, if we can evaluate the asymptotic behaviour of _FN_<sup>pert</sup> ( _β_ ) as _N −→∞_ for such _sN_ , this still answers the first main question about the SK model. On the other hand, it turns out that for a generic choice of the coefficients _xp_ , all the unwanted symmetry is broken, and the resulting Gibbs measures have a very special structure.

This is described by the ‘Ruelle Probability Cascades’, which we will not introduce carefully here, but their important qualitative features are given in the following theorem:

**Theorem 15.1 (The Parisi ansatz)** _For almost every_ ( _x_ 1 _, x_ 2 _, . . ._ ) _∈_ [0 _,_ 1]<sup>N</sup> _, every subsequential limit γ of the random measures γβ,N has the following properties:_

- _γ is supported on the sphere {ξ ∈ ℓ_ 2 : _∥ξ∥_ = _q_<sup>_∗_</sup> ( _β_ ) _} for some non-random q_<sup>_∗_</sup> ( _β_ ) _∈_ [0 _,_ 1] _,_

- _(Talagrand’s positivity principle) if ξ_ 1 _, ξ_ 2 _are drawn independently from γ, then ξ_ 1 _· ξ_ 2 _≥_ 0 _a.s._

- _the support of γ is an ultrametric subset Y of the radius-q∗_ ( _β_ ) _sphere._

The deepest and most surprising part of this result is that the random measure _γ_ is supported on an ultrametric subset of _B_ , and it turns out that once this is known, the rest of the structure can be deduced fairly directly. This was known as the ‘Parisi ultrametricity conjecture’, and was the last piece of the above theorem to fall into place in the recent work [Pan13].

> 4Although it has been studied as such; it is called the **mixed** _p_ **-spin model** .

48

Recall that a metric space ( _Y, dY_ ) is **ultrametric** if the triangle inequality may be strengthened to


If _Y_ is contained in a sphere of constant radius _q_<sup>_∗_</sup> in a Hilbert space H, as in the case above, then this ultrametric inequality implies a very explicit ‘heirarchical’ structure. If we assume also that the distances between points of _Y_ assume only finitely many different values, it may be described as follows. There are

- a rooted tree _T_ of constant depth _d_ , say,

- a sequence of values


- and pairwise-orthogonal vectors _ξuv ∈_ H for every edge _uv_ of _T_ such that _∥ξuv∥_ = _qi_<sup>2</sup><sup>_−q_</sup> _i_<sup>2</sup> _−_ 1<sup>if</sup><sup>_uv_connects levels</sup><sup>_i −_1 and</sup><sup>_i_of</sup><sup>_T_,</sup> ~~�~~

such that _Y_ is the image of the set of leaves _∂T_ under following map _ϕ_ : _∂T −→_ H:


where _v_ 0 _v_ 1 _· · · vd−_ 1 _v_ is the path from the root to _v_ in _T_ . Now _Y_ is determined up to isometry by _T_ and the lengths _qi_ . If _Y_ has infinitely many possible interpoint distances, then one needs a slightly more complicated version of this picture. See [Pan12] for a more careful discussion of ultrametricity.

It is easy to see that the full Parisi ansatz cannot hold for the Hamiltonian (10) by itself. Whatever the values of _gi,j_ , that Hamiltonian is always invariant under the ‘spin-flip’ symmetry ( _σi_ ) _i �→_ ( _−σi_ ) _i_ , from which it follows easily that any nontrivial limit random measure would violate Talagrand’s positivity principle. This spin-flip symmetry is actually obscuring some other structure of importance, and so one must at least perturb the model so far as to break this symmetry, and then try to understand the resulting perturbed Gibbs measures. This situation would be very similar to how the symmetric Gibbs measures for the low-temperature Ising model on Z<sup>2</sup> should be understood as a convex combination of two asymmetric Gibbs measures

So some perturbation to the SK Hamiltonian is needed for the Parisi ansatz, but it is still open whether one really needs the whole infinite-dimensional family introduced above.

49

#### **From concentration results to the Ghirlanda-Guerra identities**

The point of embarkation for obtaining the Ghirlanda-Guerra identities for the SK model is a very basic principle concerning Gibbs measures. It can also be illustrated on the REM. Suppose now that _H_ : _{−_ 1 _,_ 1 _}_<sup>_N_</sup> _−→_ R is the random Hamiltonian in either of these models, and form the resulting family of Gibbs measures


Let Φ( _β_ ) = log _Z_ ( _β_ ), so _FN_ ( _β_ ) = E _N_<sup><u>1</u>Φ(</sup><sup>_β_).</sup>

Now, on the one hand, applying H¨older’s inequality to _Z_ ( _β_ ) with _β_ 1 _, β_ 2 _≥_ 0 and 0 _≤ t ≤_ 1 gives


hence convexity:


On the other, basic calculus gives


Another differentiation gives


With only this in hand, one concludes that for any interval [ _a, b_ ] _⊆_ [0 _, ∞_ ),


50

This inequality has remarkable consequences in case _H_ already takes large values: if _∥H∥∞_ is large, it tells us that Var _γβ_ ( _H_ ) is not much larger than _∥H∥∞_ for most values of _<u>β</u> ∈_ [ _a, b_ ]. Therefore, one expects the fluctuations of _H_ to be typically O( ~~�~~ _∥H∥∞_ ) (where ‘typically’ refers to _γβ_ ). On the other hand, if _H_ is not too irregular then one often finds that _|H|_ itself typically takes values comparable to _∥H∥∞_ , so that _its fluctuations are much smaller than its typical values_ . This applies in the case of the SK model and REM, because there we expect _H_ ( _σ_ ) to have values of order _N_ for most _σ_ , and one can show that its maximum is typically not too much larger than this (see [Tal03, Proposition 1.1.3]).

Now recall that in either of the models of interest, _H_ is a centred Gaussian random field on _{−_ 1 _,_ 1 _}_<sup>_N_</sup> , and that an appeal to the concentration inequality of Proposition 13.1 gives (12). This tells us that the random function _N_ <u>1</u><sup>Φ</sup><sup>_N_(</sup><sup>_β_)is</sup> very close to the deterministic function _FN_ ( _β_ ) as _N −→∞_ . Since these are also convex functions, one can turn this into an approximation between their derivatives. Working out the details of these estimates in these particular models, the upshot of this is the estimate


This is explained more carefully as Theorem 2.12.1 in [Tal03].

Now let _ν_ = _νβ,N_ be the (deterministic) measure E _⟨−⟩β,N_ . The above implies that for any fixed interval [ _a, b_ ], for most _β ∈_ [ _a, b_ ] the quantity _H/N_ : _{−_ 1 _,_ 1 _}_<sup>_N_</sup> _−→_ R must be very highly concentrated under the measure _νβ,N_ . Using this, with a little care one can extract a _β_ in any chosen interval and a subsequence of these measures such that for any functions _fN_ : ( _{−_ 1 _,_ 1 _}_<sup>_N_</sup> )<sup>_m_</sup> _−→_ [ _−_ 1 _,_ 1] one must have


uniformly in the choice of _fN_ .

Applying Guassian integration by parts to this apparently simple phenomenon has far-reaching consequences. On the one hand, for any function _f_ we find that


51

where


This is obtained by applying Proposition 13.2 for each tuple ( _σ_<sup>1</sup> _, . . . , σ_<sup>_m_</sup> ) separately to the function


Since ( _H_ ( _σ_ )) _σ_ is a centred Gaussian process, we can perform the integration by parts in the Gaussian r.v. _H_ ( _σ_<sup>1</sup> ) with the orthogonal Gaussian process held fixed.

Similarly one can compute that


(where in both the SK model and the REM the quantity _σ_<sup>1</sup> _· σ_<sup>1</sup> is actually constant, i.e. the same for every _σ_<sup>1</sup> ).

Substituting these into (18) and taking a subsequential limit gives


where now _ν_ := E _⟨−⟩_ refers to the subsequential sampling-limit random measure _γ_ . These are the **Ghirlanda-Guerra identities** .

In fact, these are only the first in a large family of identities. If _γ_ is a random Hilbert space measure and _ν_ = E _⟨−⟩_ as before, then _γ_ satisfies the **extended Ghirlanda-Guerra identities** if


for all bounded continuous functions _f_ and all _p ≥_ 1. Equivalently, this asserts that if one first chooses _γ_ itself at random, and then chooses _σ_<sup>1</sup> _, σ_<sup>2</sup> _, . . ._ independently

52

at random from _γ_ , then conditionally on _σ_<sup>1</sup> , ..., _σ_<sup>_m_</sup> the inner product _σ_<sup>1</sup> _· σ_<sup>_m_+1</sup> has distribution


When these extended identities are satisfied, one can show that they give all the desired control over the structure of _γ_ . One needs the large family of perturbations to the SK Hamiltonian that were introduced previously in order to find parameter values at which all of these identities hold simultaneously; we will not explain this further here, but see [Panar, Chapter 3].

### **16 Obtaining consequences from Ghirlanda-Guerra**

#### **Ultrametricity and the Ruelle Probability Cascades**

The heart of Panchenko’s breakthrough [Pan13] is a proof that the extended GhirlandaGuerra identities imply the ultrametricity part of Theorem 15.1. That proof is difficult and a little long, so we will not broach it here, except to report a simple geometric feature of independent interest. To prove ultrametricity, Panchenko actually shows that the Ghirlanda-Guerra identities imply the following property for the support of the limiting Gibbs measure:

**Proposition 16.1 (See proof of Theorem 2.13 in [Panar])** _Suppose that Y ⊆_ H _is a closed subset of a Hilbert space with the following property:_


_then there are ‘duplicates’ ξ_ 1<sup>_′, ξ_</sup> 2<sup>_′, ..., ξ_</sup> _m_<sup>_′∈Yand also ξ_</sup> _m_<sup>_′′∈Ysuch_</sup> _that_


_and_


_Then Y is ultrametric._

53

The proof of this rests on a careful application of the Cauchy-Schwartz inequality to the average of a large sequence of such duplicates. If one starts with a non-ultrametric triangle, one can produce a distance that must be negative, and hence a contradiction. Note that the above condition is certainly not _necessary_ for ultrametric subsets of a Hilbert space: for example, it cannot be satisfied by any finite ultrametric subset.

Once ultrametricity is known, it remains to describe _Y_ exactly in terms of a tree _T_ and distances _qi_ (or some version of these data for general ultrametrics), as discussed at the beginning of the previous section; and then to describe the distribution of the random measure _γβ_ supported on _Y_ . The structure of Ruelle Probability Cascades finally appears in the latter step, and is also deduced from the Ghirlanda-Guerra identities once ultrametricity is known. We will not explain these carefully here (again, [Pan12, Panar] give good introductions), but to give some of the flavour we will discuss the analogous problem in the much simpler, toy situation of the REM.

#### **Solving the REM**

Assume we know that the limiting random probability measure _γ_ of the REM satisfies the extended Ghirlanda-Guerra identities. For the REM the quantities _σ · σ_<sup>_′_</sup> between different states can take only two values, since for this model


(so _σ · σ_<sup>_′_</sup> is not now the inner product coming from regarding _{−_ 1 _,_ 1 _}_<sup>_N_</sup> as a subset of _ℓ_<sup>_N_</sup> 2<sup>).This property clearly persists for the limiting measure</sup><sup>_γ_, so it follows that</sup> the random measure _γ_ is a.s. supported on a sequence of orthogonal elements of its auxiliary Hilbert space H. However, this means that in this case the extended Ghirlanda-Guerra identities reduce to the following principle:

If we choose _γ_ at random and then choose elements _ξ_ 1, _ξ_ 2, ...i.i.d. from _γ_ , , then having chosen _ξ_ 1 _, . . . , ξm_ , the probability that _ξm_ +1 = _ξ_ 1 (i.e., that _ξ_ 1 _· ξm_ +1 = 1, not 0) is


where _p_ is the overall probability that two vectors _ξ_ and _ξ_<sup>_′_</sup> drawn in this process will be equal.

54

Considering only the process that determines whether _ξm_ +1 agrees with one of _ξ_ 1, . . . , _ξm_ or is distinct from all of them, this reveals a random partition of N as _m_ increases, and now we recognize it: provided 0 _< p <_ 1, it is the Chinese Restaurant Process with parameter _α_ = 1 _− p_ (recall formula (7)).

Therefore, in the case of the REM, provided it turns out that 0 _< α <_ 1, the random weights of the limiting random measure _γ_ follow the random mass partition PD( _α,_ 0) with this _α_ . A separate analysis can now be given to show that _α ∈_ (0 _,_ 1) when _β >_ 2<sup>_√_</sup> log 2, and then


(see Chapter 1 of [Tal03]). On the other hand, when _β ≤_ 2<sup>_√_</sup> log 2 (corresponding to high temperature in the physical interpretation), it works out that _p_ = 1, _α_ = 0, and the limiting probability measure _γ_ simply collapses to a Dirac mass at 0.

### **References**

- [AC] L.-P. Arguin and S. Chatterjee. Random overlap structures: properties and applications to spin glasses. Preprint, available online at arXiv.org: 1011.1823.

- [Ald] David J. Aldous. More uses of exchangeability: representations of complex random structures. to appear in _Probability and Mathematical Genetics: Papers in Honour of Sir John Kingman_ .

- [Ald81] David J. Aldous. Representations for partially exchangeable arrays of random variables. _J. Multivariate Anal._ , 11(4):581–598, 1981.

- [Ald82] David J. Aldous. On exchangeability and conditional independence. In _Exchangeability in probability and statistics (Rome, 1981)_ , pages 165– 170. North-Holland, Amsterdam, 1982.

- [Ald85] David J. Aldous. Exchangeability and related topics. In _Ecole d’´et´e de_<sup>_´_</sup> _probabilit´es de Saint-Flour, XIII—1983_ , volume 1117 of _Lecture Notes in Math._ , pages 1–198. Springer, Berlin, 1985.

- [ASS07] Michael Aizenman, Robert Sims, and Shannon L. Starr. Mean-field spin glass models from the cavity-ROSt perspective. In _Prospects in mathematical physics_ , volume 437 of _Contemp. Math._ , pages 1–30. Amer. Math. Soc., Providence, RI, 2007.

55

- [Aus08] Tim Austin. On exchangeable random variables and the statistics of large graphs and hypergraphs. _Probability Surveys_ , (5):80–145, 2008.

- [Ber06] Jean Bertoin. _Random fragmentation and coagulation processes_ , volume 102 of _Cambridge Studies in Advanced Mathematics_ . Cambridge University Press, Cambridge, 2006.

- [CH06] Philippe Carmona and Yueyun Hu. Universality in SherringtonKirkpatrick’s spin glass model. _Ann. Inst. H. Poincar´e Probab. Statist._ , 42(2):215–222, 2006.

- [Con90] John B. Conway. _A course in functional analysis_ , volume 96 of _Graduate Texts in Mathematics_ . Springer-Verlag, New York, second edition, 1990.

- [Der81] Bernard Derrida. Random-energy model: an exactly solvable model of disordered systems. _Phys. Rev. B (3)_ , 24(5):2613–2626, 1981.

- [DF80] P. Diaconis and D. Freedman. Finite exchangeable sequences. _Ann. Probab._ , 8(4):745–764, 1980.

- [DJ07] Persi Diaconis and Svante Janson. Graph limits and exchangeable random graphs. Preprint; available online at arXiv.org: math.PR math.CO/0712.2749, 2007.

- [DS82] L. N. Dovbysh and V. N. Sudakov. Gram-de Finetti matrices. _Zap. Nauchn. Sem. Leningrad. Otdel. Mat. Inst. Steklov. (LOMI)_ , 119:77–86, 238, 244–245, 1982. Problems of the theory of probability distribution, VII.

- [FT85] D. H. Fremlin and M. Talagrand. Subgraphs of random graphs. _Trans. Amer. Math. Soc._ , 291(2):551–582, 1985.

- [Gro99] Mikhael Gromov. _Metric Structures for Riemannian and NonRiemannian Spaces_ . Birkh¨auser, Boston, 1999.

- [GT02] Francesco Guerra and Fabio Lucio Toninelli. The thermodynamic limit in mean field spin glass models. _Comm. Math. Phys._ , 230(1):71–79, 2002.

- [Gue03] Francesco Guerra. Broken replica symmetry bounds in the mean field spin glass model. _Comm. Math. Phys._ , 233(1):1–12, 2003.

56

- [Hes86] K. Hestir. The Aldous representation theorem and weakly exchangeable non-negative definite arrays. Ph.D. dissertation, Statistic Dept., Univ. of California, Berkeley, 1986.

- [Hoo79] David N. Hoover. Relations on probability spaces and arrays of random variables. 1979.

- [Hoo82] David N. Hoover. Row-columns exchangeability and a generalized model for exchangeability. In _Exchangeability in probability and statistics (Rome, 1981)_ , pages 281–291, Amsterdam, 1982. North-Holland.

- [Kal89] Olav Kallenberg. On the representation theorem for exchangeable arrays. _J. Multivariate Anal._ , 30(1):137–154, 1989.

- [Kal92] Olav Kallenberg. Symmetries on random arrays and set-indexed processes. _J. Theoret. Probab._ , 5(4):727–765, 1992.

- [Kal02] Olav Kallenberg. _Foundations of modern probability_ . Probability and its Applications (New York). Springer-Verlag, New York, second edition, 2002.

- [Kal89] Olav Kallenberg. On the representation theorem for exchangeable arrays. _J. Multivariate Anal._ , 30(1):137–154, 1989.

- [Kal05] Olav Kallenberg. _Probabilistic symmetries and invariance principles_ . Probability and its Applications (New York). Springer, New York, 2005.

- [Kin78a] J. F. C. Kingman. The representation of partition structures. _J. London Math. Soc. (2)_ , 18(2):374–380, 1978.

- [Kin78b] J. F. C. Kingman. Uses of exchangeability. _Ann. Probability_ , 6(2):183– 197, 1978.

- [Led01] Michel Ledoux. _The concentration of measure phenomenon_ , volume 89 of _Mathematical Surveys and Monographs_ . American Mathematical Society, Providence, RI, 2001.

- [LS06] L´aszl´o Lov´asz and Bal´azs Szegedy. Limits of dense graph sequences. _J. Combin. Theory Ser. B_ , 96(6):933–957, 2006.

- [MPV87] Marc M´ezard, Giorgio Parisi, and Miguel Angel Virasoro. _Spin glass theory and beyond_ , volume 9 of _World Scientific Lecture Notes in Physics_ . World Scientific Publishing Co. Inc., Teaneck, NJ, 1987.

- [Pan10] Dmitry Panchenko. On the Dovbysh-Sudakov representation result. _Elec. Commun. in Probab._ , 15:330–338, 2010.

57

- [Pan12] Dmitry Panchenko. The Sherrington-Kirkpatrick model: an overview. _J. Stat. Phys._ , 149(2):632–383, 2012.

- [Pan13] Dmitry Panchenko. The Parisi ultrametricity conjecture. _Ann. of Math. (2)_ , 177(1):383–393, 2013.

- [Panar] Dmitry Panchenko. _The Sherrington-Kirkpatrick model_ . Springer Monographs in Mathematics. To appear.

- [Pit95] Jim Pitman. Exchangeable and partially exchangeable random partitions. _Probab. Theory Related Fields_ , 102(2):145–158, 1995.

- [PY97] Jim Pitman and Marc Yor. The two-parameter Poisson-Dirichlet distribution derived from a stable subordinator. _Ann. Probab._ , 25(2):855–900, 1997.

- [Tal03] Michel Talagrand. _Spin glasses: a challenge for mathematicians_ , volume 46 of _Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics]_ . Springer-Verlag, Berlin, 2003. Cavity and mean field models.

- [Tal06] Michel Talagrand. The Parisi formula. _Ann. of Math. (2)_ , 163(1):221– 263, 2006.

- [Tal11] Michel Talagrand. _Mean field models for spin glasses. Volume I_ , volume 54 of _Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics]_ . Springer-Verlag, Berlin, 2011. Basic examples.

Courant Institute of Mathematical Sciences New York University New York, NY 10012, USA tim@cims.nyu.edu http://www.cims.nyu.edu/˜tim

58

---

[← Exchangeability Theory](02-exchangeability-theory.md) · [Up: contents](index.md)
