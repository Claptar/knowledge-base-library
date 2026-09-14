---
title: STOCHASTIC MODELS AND SOLUTIONS
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# STOCHASTIC MODELS AND SOLUTIONS

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

...as one judge said to the other,

‘Be just and if you can’t be just be arbitrary.’

_Naked Lunch_

William S. Burroughs

### **<u>4.1 Motivations for model classes</u>**

This section adapts a portion of [115] by G.G., J.J.V., and L.P. This motivating discussion was written by G.G.

We begin by defining the biological variables of interest. We seek to develop a theoretical framework that can accommodate a wide variety of biological phenomena. This is a modeling challenge that involves a series of trade-offs. On one hand, we would like to represent a broad range of phenomena; on the other, if the scope is _too_ broad, the mathematical form becomes intractable. We restrict our analysis to a fairly general class of systems which afford a reasonably compact representation and can be solved by quadrature.

In brief, we care about models with interacting _microscopic_ , _mesoscopic_ , and _macroscopic_ degrees of freedom. These “model scales” are defined with respect to their treatment of stochasticity. Microscopic models account for the flow of probability between discrete states, and are formalized by chemical master equations (CMEs). Mesoscopic models approximate the discrete states by a continuum, and are formalized by equivalent stochastic differential equations (SDEs) or Fokker-Planck equations (FPEs). Macroscopic models omit stochasticity altogether, and are formalized by ordinary differential equations (ODEs). As discussed in [236, 294], certain regimes of microscopic models can be effectively approximated by mesoand macroscopic dynamics. These approximations rely on strong assumptions regarding the “important” sources of stochasticity in the system, and can often be derived through perturbative approximations [297].

26


Figure 4.1: The biophysical and chemical phenomena of interest, as well as the relationships between their generating functions.

**a.** The biological phenomena of interest: cell influx and efflux into a tissue observed by sequencing; the time-dependent transcriptional regulation of one or more genes; downstream continuous and discrete processes.

**b.** The technical phenomena of interest: the encapsulation of cells and cell debris; cDNA library construction; the loss of information in transcript identification (GF: generating function).

**c.** The structure of the full generating function of the system in **a** and **b** : to obtain the solution, we variously compose, integrate, and multiply the generating functions of the constituent processes.

### **4.2 Models of RNA processing and transcriptional noise**

This section summarizes the mathematical machinery formalized in [115] by G.G., J.J.V., and L.P. G.G. developed this approach as a generalization of the framework constructed by G.G. and J.J.V. in [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P., as well as by J.J.V. in [299], among other publications. The description was written by G.G. and J.J.V.

Our treatment of stochastic systems considers gene state interconversion, as well as the production and processing of macromolecules such as RNA and proteins, which could treated as discrete or continuous variables depending on their concentration. We allow zero- and first-order reactions, including state-dependent bursting, interconversion, degradation, and catalysis. However, we disallow higher-order reactions, including feedback regulation. In addition, we allow various macro- and mesoscopic layers of regulation, such as state- and time-dependent variation in

27

### transcription rates.

By setting up and writing out the relevant master equations, it turns out to be most natural by far to formalize the systems in terms of _𝑁_ categorical degrees of freedom, corresponding to gene states, _𝑛_ discrete ones, corresponding to low-copy number molecular species, and _𝑚_ continuous ones, corresponding to transcription rates or high-concentration species. By omitting regulation, we can split the systems into distinct “upstream” and “downstream” components. As a consequence of the _Poisson representation_ , which establishes isomorphisms between discrete and continuous stochastic processes [94], the precise meaning of the “downstream” components ceases to matter: discrete and continuous degrees of freedom can be treated using the same mathematical tools. Formally, the discrete components are Poisson mixtures of the continuous processes (as in Equation 3.40).

This conceptualization happens to be particularly useful under a particular combination of assumptions (mass action kinetics, no regulation) and goals (computing dataset likelihoods). However, others alternatives are available. For example, the discrete degrees of freedom have been studied in the language of queuing theory [166, 257]. The analysis of continuous stochastic processes owes a great deal to mathematical finance [265]. The distinctions between model scales may even be translated into the language of quantum physics [5, 211, 299]: categorical states are mutually exclusive and follow fermion-like statistics; discrete states are unconstrained and follow boson-like statistics; continuous states are fundamentally classical. This conceptualization is in its nascence, but may well lead to useful and widespread mathematical tools in the future. Under the assumptions and goals we adopt, we have found that the Poisson representation approach we adopt, which exploits the properties of partial differential equations, provides the best balance of computational and analytical tractability in the multi-modal context.

### **4.2.1 Master equation definitions**

The categorical variable, denoted by _𝑠_ ∈{1 _, ..., 𝑁_ }, represents the instantaneous state of a multi-state gene. By assuming that the state interconversions are Markovian and independent of all other components of the system, we can define _𝐻𝑖𝑗_ , the rates of transitioning from state _𝑖_ to state _𝑗_ :


These rates can be summarized in the state transition matrix _𝐻_ ∈ R≥<sup>_𝑁_</sup> 0<sup>×</sup><sup>_𝑁_, such that</sup> _𝐻𝑖𝑖_ = −<sup>�</sup> _𝑗_ ≠ _𝑖_<sup>_𝐻_</sup> _𝑖𝑗_<sup>and�</sup> _𝑗_<sup>_𝐻_</sup> _𝑖𝑗_<sup>=0toenforcetheconservationofprobability.This</sup>

28

set of transitions can be represented by a finite master equation, which tracks the probabilities of each state _𝑠_ at a time _𝑡_ :


As this system is expressed in terms of a differential equation for an arbitrary time _𝑡_ , the relation holds for time-dependent _𝐻_ . For simplicity, we assume that _𝐻_ is deterministic and independent of other variables. For a review of CMEs, we recommend [95, 295, 297, 315, 336].

The nonnegative discrete variables, denoted by **x** ∈ N0<sup>_𝑛_,representmolecularcopy</sup> numbers. We assume that _𝑛_ molecular species participate in four classes of transitions, and can summarize their effect by considering their reaction schema and effect on _𝑥𝑖_ , the number of molecules of species _𝑖_ :


First, species _𝑖_ can be converted to species _𝑗_ with rate _𝑐𝑖𝑗 𝑥𝑖_ . Second, species _𝑖_ can spontaneously degrade with rate _𝑐𝑖_ 0 _𝑥𝑖_ . These classes of monomolecular transitions, which either maintain or reduce the total number of molecules in the system, can be summarized in the matrix _𝐶_<sup>_𝑑𝑑_</sup> ∈ R<sup>_𝑛_×</sup><sup>_𝑛_</sup> , such that _𝐶𝑖𝑗_<sup>_𝑑𝑑_=</sup><sup>_𝑐𝑖𝑗_and</sup><sup>_𝐶_</sup> _𝑖𝑖_<sup>_𝑑𝑑_= −</sup><sup>_𝑐𝑖_0−�</sup> _𝑗_ ≠ _𝑖_<sup>_𝑐_</sup> _𝑖𝑗_<sup>;</sup> ( _𝐶_<sup>_𝑑𝑑_</sup> )<sup>T</sup> is the matrix governing the associated reaction rate equations [146]. Third, species _𝑖_ participate in autocatalysis at the rate _𝑞𝑖𝑖_ , or catalysis of species _𝑗_ at the rate _𝑞𝑖𝑗_ . These reactions can be summarized by the matrix _𝑄_<sup>_𝑑_</sup> ∈ R<sup>_𝑛_</sup> ≥<sup>×</sup> 0<sup>_𝑛_,suchthat</sup> _𝑄_<sup>_𝑑_</sup> _𝑖𝑗_<sup>=</sup><sup>_𝑞𝑖𝑗_.</sup>

Finally, molecules can be produced through a variety of reaction channels, indexed by _𝜔_ . In the general case, a transcriptional event — a _burst_ of production — simultaneously creates molecules of _ℓ𝜔_ discrete species { _𝑖_ 1 _, ..., 𝑖ℓ𝜔_ }. We assume bursts are described by a Poisson arrival process, with burst frequency _𝛼𝜔_<sup>_𝑑_and the nontrivial</sup> _ℓ𝜔_ -variate joint distribution _𝑝𝜔_<sup>_𝑑_(</sup><sup>**z**)ofnon-negativeburstsizes{</sup><sup>_𝐵𝑖_</sup> 1<sup>_,_· · ·</sup><sup>_, 𝐵ℓ_</sup> _𝜔_<sup>}.In</sup> other words, _𝑝𝜔_<sup>_𝑑_(</sup><sup>**z**) is well-defined over all non-negative</sup><sup>**z**, but its value is identically</sup> zero whenever any component _𝑧𝑖 >_ 0, for all _𝑖_ ∉ { _𝑖_ 1 _, ..., 𝑖ℓ𝜔_ }. The burst frequency and distribution may vary with gene state _𝑠_ .

29

This formulation includes the trivial case of Poisson point process production of species _𝑖_ , for which _ℓ𝜔_ = 1 and _𝑝𝜔_<sup>_𝑑_(</sup><sup>**z**)=</sup><sup>_𝛿𝑖𝑗_, the degenerate distribution located at</sup> unity for species _𝑖_ and zero for all other species.

This mass action model, which tracks molecule counts, can be represented by an equivalent discrete chemical master equation, which tracks the probability of each microstate **x** :


For simplicity of notation, species that do not occur in a reaction are elided from the master equation probability terms.

As in Equation 4.2, this master equation holds even if the rates are time-dependent. For tractability, we assume only _𝛼𝜔_<sup>_𝑑_and</sup><sup>_𝑝_</sup> _𝜔_<sup>_𝑑_can vary over time.Since the form of</sup> these functions is arbitrary deterministic, the dynamics of these variables represent unspecified macroscopic processes.

The nonnegative continuous variables, denoted by **y** ∈ R<sup>_𝑚_</sup> ≥0<sup>,represent mesoscopic</sup> concentrations or coarsely-modeled noise sources. We assume that these variables are governed by Ornstein–Uhlenbeck-type stochastic differential equations:


where **y** _𝑡_ is a realization of the process, **W** _𝑡_ is an w-dimensional Brownian motion, and **L** _𝜔_ is a subordinator. For a review of SDEs, we recommend [23, 57, 95, 236, 295, 297, 336].

The matrix _𝐶_<sup>_𝑐𝑐_</sup> ∈ R<sup>_𝑚_×</sup><sup>_𝑚_</sup> sets the mean-reversion terms. In other words, a nonzero entry _𝐶𝑖𝑗_<sup>_𝑐𝑐_impliesthatthelevelofspecies</sup><sup>_𝑖_isproportionaltoinfluxintospecies</sup> _𝑗_ . The operator Q<sup>_𝑐_</sup> ( **y** _𝑡_ ) : R<sup>_𝑚_</sup> ≥0<sup>→R</sup><sup>_𝑚_</sup> ≥0<sup>×w</sup> sets the level of noise. For simplicity, we

30

assume the noise term takes the form of an uncoupled square-root diffusion, such that w = _𝑚_ and Q<sup>_𝑐_</sup> ( **y** _𝑡_ ) = diag( _𝝈_ ⊙<sup>~~√~~</sup> **<u>y</u>** _𝑡_ ). The symbol ⊙ denotes the elementwise, or Hadamard, product of two vectors, the square root should be interpreted as elementwise, and all elements of the constant volatility vector _𝝈_ are non-negative. Although this choice of Q<sup>_𝑐_</sup> is somewhat restrictive, it produces a particularly simple diffusion tensor Σ:


where the square _𝝈_<sup>2</sup> should be interpreted as elementwise.

We assume that each **L** _𝜔_ only includes drift or compound Poisson terms. The drift terms have the form _𝛼𝑖_<sup>_𝑐𝛿𝑖𝑗𝑡_.Toslightlylightenthenotation,wecanaggregateall</sup> drift terms under _𝜔_ = 1 _,_ · · · _, 𝑚_ as { _𝛼_ 1<sup>_𝑐𝑑𝑡,_· · ·</sup><sup>_, 𝛼_</sup> _𝑚_<sup>_𝑐𝑑𝑡_}; some of these entries may be</sup> zero. The compound Poisson terms have the form<sup>�N</sup> _𝑘_ =<sup>_𝜔_</sup> 0<sup>(</sup><sup>_𝑡_)(</sup><sup>**B**</sup><sup>_𝜔_)</sup><sup>_𝑘_[43], such that N</sup><sup>_𝜔_(</sup><sup>_𝑡_)</sup> is a Poisson random variable with mean _𝛼𝜔_<sup>_𝑐𝑡_and{(</sup><sup>**B**</sup><sup>_𝜔_)</sup><sup>_𝑘_}isasetofindependent</sup> and identically distributed realizations of the random variable **B** _𝜔_ . This random variable has a nontrivial _ℓ𝜔_ -variate joint density _𝑝𝜔_<sup>_𝑐_(</sup><sup>**z**)on R</sup><sup>_𝑚_</sup> ≥0<sup>, with the remaining</sup> _𝑚_ − _ℓ𝜔_ dimensions concentrated at zero. We note that this formulation entails a slight abuse of notation, as _𝜔_ is used to index over discrete burst processes as well as continuous drift and jump components.

This formulation can be reframed as a Fokker-Planck equation [236], which tracks the probability density of each microstate **y** :


As above, we assume that only the components of **L** _𝜔_ can vary in time.

In addition to these discrete- and continuous-only terms, we need to account for these components’ interactions. For example, we may want to represent the production of a discrete species controlled by a continuous variable, e.g., a time-varying transcription rate:


This reaction has the rate _𝑦𝑖𝐶𝑖𝑗_<sup>_𝑐𝑑_.This class of reactions can be summarized in the</sup> matrix _𝐶_<sup>_𝑐𝑑_</sup> ∈ R<sup>_𝑚_</sup> ≥0<sup>×</sup><sup>_𝑛_.In other words, this class of reactions contributes the following</sup>

31

terms to the overall master equation:


Finally, we may want to represent the production of a continuous species from a discrete one, e.g., the rapid translation of high-abundance protein from lowabundance RNA [31]. This class of reactions simply adds a term proportional to ( _𝐶_<sup>_𝑑𝑐_</sup> )<sup>T</sup> **x** _𝑑𝑡_ to the expression for _𝑑_ **y** _𝑡_ . The matrix _𝐶_<sup>_𝑑𝑐_</sup> ∈ R<sup>_𝑛_</sup> ≥<sup>×</sup> 0<sup>_𝑚_</sup> contains the relevant rates, such that _𝐶𝑖𝑗_<sup>_𝑑𝑐_is the rate of producing the continuous species</sup><sup>_𝑗_from discrete</sup> species _𝑖_ . Therefore, we append a set of drift-like terms to the Fokker-Planck equation:


To construct the full master equation, we need to define a system of _𝑁_ coupled equations. To do so, we essentially add Equations 4.2, 4.4, 4.7, 4.9, and 4.10, replacing all instances of _𝑃_ with **P** ( _𝑠,_ **x** _,_ **y** _, 𝑡_ ). However, to account for differences in transcription between gene states, we allow the _𝜔_ -associated terms to vary with _𝑠_ . The full master equation is reported in Equation A.1.

### **4.2.2 Approaches to solution**

We have defined a class of master equations. To evaluate likelihoods and statistically characterize data, we need to calculate the probabilities of observations under a particular model and set of parameters. There are essentially four approaches to this problem.

### **4.2.2.1 Simulation**

In principle, we can approximate solutions by simulation, as discussed in Section 5.5. If _𝑚_ = 0, we can use the usual form of Gillespie’s stochastic simulation algorithm [98] (as in Section 5.5.1); if _𝑚>_ 0, we can use somewhat more sophisticated schema (Section 5.5.2). If we perform Nk simulations of a fully discrete system, indexed by k, the probability _𝑃_ ( _𝑠,_ **x** ) can be approximated by


32

where I is the indicator function and ( _𝑆, 𝑋_ 1 _, . . . , 𝑋𝑛_ )k are the process values at time _𝑡_ in the kth realization. Although this method can be used when no other alternatives exist [110], it converges with the usual Monte Carlo rate of Nk<sup>−1/2</sup> [193], which is generally unacceptably slow, and impractical even for modest _𝑛_ . In addition, the Gillespie approach is fundamentally “coupled”: if we are interested in a subset of downstream distributions, we need to simulate the entire system, including the upstream reactions.

### **4.2.2.2 Matrix algorithms**

Instead of considering trajectories, we can exploit the fact that the discrete terms of the master equation (Equation A.1) can be represented by matrix multiplication:


where _𝐴_ is infinite-dimensional and **P** now contains entries for all _𝑠_ and **x** . By truncating _𝐴_ to a finite-dimensional matrix _𝐴_<sup>˜</sup> , we can obtain a reasonably accurate approximation to **P** :


This is the finite state projection (FSP) algorithm [203]. If only the stationary distribution is of interest, the determination of **P**<sup>˜</sup> is equivalent to the determination of the nullspace of _𝐴_<sup>˜</sup> [118].

This approach is generic, and works for any combination of reactions. However, the matrix _𝐴_<sup>˜</sup> tends to be fairly large, and making the procedure tractable often involves a considerable degree of computational design [304]; in addition, the matrix operations have cubic time complexity, which is somewhat restrictive. More fundamentally, the FSP approach retains the “coupling” feature of the stochastic simulation algorithm: even if we only care about a certain marginal, we may need to explicitly represent all species and reactions. Finally, the probability distributions are somewhat challenging to integrate with other stochastic phenomena: for example, FSP cannot directly represent technical noise that occurs in the sequencing process, as in Section 4.4, and requires dedicated manipulation of **P**<sup>˜</sup> .

### **4.2.2.3 Exact analysis**

In some very narrow cases, the CME can be exactly solved by sheer ingenuity, e.g., by using an _ansatz_ for the probability mass function [299]. For example, if we are

33

interested in the steady state of the simple birth–death process


we can write down its master equation


and notice that the steady-state probability flux equation


can be satisfied by substituting _𝑃_ with the Poisson distribution. For more complicated processes, we can obtain a partial differential equation equivalent to the master equation (Appendix A) and exactly solve it, either by using an _ansatz_ [31], a perturbative expansion [301], or somewhat brute-force calculation and judicious use of special functions [125, 144, 299]. This approach is, however, typically only practical for some combination of _𝑁_ = 2, _𝑛_ = 1, or _𝑡_ →∞. It is also challenging to apply systematically: for example, even if _𝑛_ = 1 is tractable, _𝑛>_ 1 is typically not.

### **4.2.3 Semi-analytical spectral solution**

We would like a more generic strategy. It turns out that the most straightforward way to evaluate the CME is to _almost_ solve it, obtain a numerically tractable ODE, then use standard numerical packages to solve this ODE [299].

The master equation is fairly cumbersome and challenging to analyze directly. Therefore, analysis has to proceed by spectral methods (Section 3.1.3), which recast the probabilistic master equation into a deterministic partial differential equation (PDE) with respect to categorical variable _𝑠_ , discrete spectral variables **g** , and continuous spectral variables **h** . By computing the generating function of both sides of Equation A.1 (Appendix A), we find that the master equation is equivalent to a much more compact PDE system:


This formulation relies on defining the unified variables encoded in a vector **u** :


34

as well as unified matrices:


By way of analogy, we sometimes use _𝑄_<sup>_𝑐_</sup> to indicate the diffusion tensor<sup><u>1</u></sup> 2<sup>diag</sup><sup>_𝝈_2.</sup> Each entry of the length- _𝑁_ vector function A consists of the burst and drift terms:


The vector _𝜶_<sup>_𝑑_</sup> _𝑠_<sup>containsthefrequenciesofalldiscreteburstprocessesforstate</sup><sup>_𝑠_.</sup> The first _𝑚_ entries of _𝜶_<sup>_𝑐_</sup> _𝑠_<sup>containthecontinuousspecies’driftsinstate</sup><sup>_𝑠_.</sup> The remaining entries contain the corresponding rates of continuous burst processes. _𝜶𝑠_ aggregates these quantities. The vector function **F** _𝑠_ contains the joint PGFs of the discrete burst processes, and only depends on the first _𝑛_ variables. The vector function **M** _𝑠_ contains the drift terms, as well as the joint MGFs of the continuous burst processes, and only depends on the last _𝑚_ variables. The parameters of the M _𝑠_ operator may vary in time.

To obtain the generating function at _𝑡_ , we apply the method of characteristics. First, we calculate the characteristics parametrized by the scalar variable s:


This is the “downstream” ODE, which governs abundances in isolation from production and regulation.

Therefore, **G** is governed by the following system of ordinary differential equations:


To obtain **G** at _𝑡_ , we integrate this system from s = _𝑡_ to s = 0. We use **G**<sup>0</sup> ( **U** ( _𝑡_ )) as the initial condition, where **G**<sup>0</sup> is the generating function of the initial distribution. This is the “upstream” ODE, which governs the full generating function.

In the general case, evaluating this system requires two applications of quadrature: first, solving the _𝑛_ + _𝑚_ -dimensional downstream system to obtain the values of characteristics **U** at a set of grid points over [0 _, 𝑡_ ], and then solving the _𝑁_ -dimensional upstream system to obtain the value of the generating function.

35

### **4.2.3.1 Implications**

The unified treatment of continuous and discrete variables warrants dedicated mention. As discussed above, it represents an application of the Poisson representation; we can readily interconvert between equivalent continuous and discrete processes. Although the resulting problems are equally challenging, we can occasionally use standard results from the study of continuous processes in finance to solve seemingly unrelated biological problems without performing any new calculations. We use three case studies to illustrate the capabilities of this approach in Section A.8.3.

Some special cases afford simpler solutions. If _𝐷_ ≠ 0, the downstream ODE takes a Riccati-like form and generally resists exact analysis [200]. However, if _𝐷_ = 0, the system takes the tractable linear form


where the columns of _𝑉_ contain the eigenvectors of _𝐶_ . This identity holds only when all eigenvalues of _𝐶_ are distinct. When they are not, **U** can be obtained analogously using generalized eigenvectors, which are a combination of polynomial and exponential functions [280]. Practically, this case only requires one application of quadrature.

If, in addition, _𝑁_ = 1, the upstream ODE reduces to a single integral:


where _𝜙_ := log _𝐺_ , _𝜙_<sup>0</sup> = log _𝐺_<sup>0</sup> , and the generating function _𝐺_ is no longer boldfaced because only a single gene state exists.

Finally, if A is a linear operator _𝑎_ 1 _𝑢_ 1 +· · ·+ _𝑎𝑛_ + _𝑚𝑢𝑛_ + _𝑚_ , the system is in the drift-only regime; no bursting occurs. In this case, the system reduces to


where _𝑈𝑖_ are the components of **U** . As each _𝑈𝑖_ is, in turn, a weighted sum of _𝑢𝑖_ , the second term of the log-generating function is given by a sum of fairly simple convolutions that scale as ∫0 _𝑡_<sup>_𝑎𝑖_(</sup><sup>_𝑡_−s)</sup><sup>_𝑒_−</sup><sup>_𝜆𝑗_s</sup><sup>_𝑑_s.</sup> This system corresponds to the _constitutive_ transcription process.

36

Finally, in the simplest case, if all eigenvalues of _𝐶_ are negative, the transient part of Equation 4.25 vanishes as _𝑡_ →∞ and the stationary log-generating function is a linear combination of _𝑢𝑖_ . This implies that the discrete distributions of the constitutive transcription process converge to multivariate independent Poisson [146].

### **4.3 Challenges of broader model classes**

### **4.3.1 Regulation**

This section summarizes some investigations undertaken during the writing of [115] by G.G., J.J.V., and L.P. This derivation was performed by G.G.

Thus far, we have omitted regulation. We can begin with fairly simple schema of the following form:


i.e., state transitions catalyzed by species X _𝑘_ . _𝑅𝑘_ is a stochastic regulation matrix analogous to _𝐻_ . This class of reactions leads to the following partial differential equation system, quite similar to Equation 4.17:


As discussed in Section A.7, the coupling of “upstream” and “downstream” degrees of freedom through the regulation matrices _𝑅𝑘_ renders this problem intractable. Although this class of systems has been studied previously [141, 143, 301], and considerable ingenuity has been applied to obtain exact solutions, it is as of yet unclear whether generic strategies for solving regulation problems exist.

### **4.3.2 Non-Markov processes**

This section is based on unpublished revisions to [114] by G.G., S.Y., and L.P. This theoretical discussion was derived and written by G.G.

In the discrete context, the vector function **U** is not arbitrary: it “correctly” propagates the initial molecule distribution into the future. In other words, if the initial condition of Equation 4.22 is degenerate, with **G**<sup>0</sup> ( **u** ) = _𝛿𝑖𝑗_ ( _𝑢 𝑗_ + 1), there exists a single molecule of species X _𝑖_ at _𝑡_ = 0. If, in addition, no production occurs and H = 0, the generating function is trivial, and yields


i.e., **U** is simply the shifted generating function of the system distribution, conditional on having a single molecule at _𝑡_ = 0. In the special case of _𝐷_ = 0, the entries of **U**

37

are generalized survival functions:


In other words, each _𝑈𝑖_ is a weighted sum of _𝑢 𝑗_ ; the weights are precisely the time-dependent conditional distributions _𝑃_ ( _𝑥 𝑗_ = 1 _, 𝑡_ | _𝑥𝑖_ = 1 _,_ 0).

It turns out that we the formulation is modular: we can use _any_ **U** that represents such a conditional distribution to encode non-Markovian downstream dynamics. To do so, we define an integral operator C with the following non-Markovian cases:


In this notation, _𝐹𝑖_<sup>′is the survival function of X</sup><sup>_𝑖_and</sup><sup>_𝑓𝑖_is the waiting time probability</sup> density function [154]. The variable _𝑡_<sup>∗</sup> indicates the time at which the reaction fires. In the Markovian case, the degradation characteristic is identical, but multiple conversion routes may compete<sup>1</sup> , yielding


where _𝑗_ indexes over the products of isomerization. When the reaction network comprises a directed acyclic graph, Equation 4.30 can be applied to compute characteristics directly<sup>2</sup> .

Usefully, when the species X _𝑖_ remains in the system for a deterministic duration _𝜏_ before being converted to X _𝑗_ , we find that its characteristic is given by the remarkably simple equation


Although this approach produces the correct solutions, the simplest way to prove it is far from clear. In addition, conceptualizing **U** as a collection of survival functions is useful when _𝐷_ = 0 but misleading when _𝐷_ ≠ 0; however, the catalytic case does not afford a simple solution strategy, and we do not consider it further.

38

### **4.4 Models of the experimental process**

This section summarizes the mathematical machinery formalized in [115] by G.G., J.J.V., and L.P. G.G. developed this approach as a generalization of the framework constructed by G.G. in [112] by G.G., M.F., T.C., and L.P., and by G.G. in [107] by G.G. and L.P.

### **4.4.1 Snapshot sampling**

To rigorously fit transient data, we need to posit just _how_ a snapshot of cells may capture multiple cell states, such that some states are the progenitors of others. The solution is not yet clear, and multiple reasonable explanations exist; for example, we may suppose that the differentiation process “lags” in certain cells (in the vein of the models of variability proposed in [270] for development and in [220, 245] for the cell cycle). In other words, all cells are captured at a time _𝑡_ since the beginning of a process, but _𝐻_ and A have different time dependence for different cells. Although such an explanatory model can be instantiated, it may be too challenging to fit. Further, it does not appear to be compatible with processes that operate continuously; the choice of _𝑡_ becomes somewhat challenging to motivate. We propose that the simplest model for observations relies on minimal synchronization between the biology and the experimental process. To mathematically formalize it, we take inspiration from the theory of reactor modeling in chemical engineering [88, 237]. A cell enters a medium; this entrance triggers a chemical signal that begins a transient process. The dynamics of this transient process are only dependent on time since receiving the signal, and identical between cells. After a delay, the cells exit the medium. In this framework, sequencing is the uniform random sampling of cells present within this medium. Although this formulation is admittedly simplistic — it excludes the cell cycle and stochastic driving — it allows us to take the first steps with a systematic study of using snapshot data to fit transient stochastic processes. This toy model is numerically tractable, which is useful for its simulation and characterization, and possesses a stationary state invariant with the time at which the experiment is performed, which is useful for biological admissibility and realism.

Therefore, to marginalize over _𝑡_ , we need to augment the model with an additional property: the relationship between time along a transient process and the probability of capturing a cell. In the parlance of reactor engineering, this relationship is given by the internal-age distribution _𝑓_ . The simulations of transient processes in [29, 168] implicitly adopt this model and assume a particular functional form of _𝑓_ . We might

39

suppose cells enter the observation window at _𝑡_ = 0 and leave it at _𝑡_ = _𝑇_ , with a Dirac residence time distribution _𝛿_ ( _𝑡_ − _𝑇_ ) and uniform sampling throughout this window. The resulting age distribution is uniform, with _𝑓_ = _𝑇_<sup>−1</sup> , and formally corresponds to the ideal plug flow reactor (PFR) architecture [88]. As _𝑇_ →∞, we obtain the _𝑡_ →∞ ergodic limit, if such a limit exists. On the other hand, if _𝑓_ → _𝛿_ ( _𝑡_ − _𝑇_ ), we recover the instantaneous distribution at time _𝑇_ ; this limit formally corresponds to the batch reactor (BR).

To obtain the generating function for the cells inside a tissue, we represent the tissue as a reactor, specify its influx and efflux properties, and solve for the internalage distribution _𝑓_ . This internal-age distribution yields the occupation measure of the process times, as discussed in [112], and induces the following reactor-wide generating function:


We have marginalized over the instantaneous gene state _𝑠_ because this variable is typically not observable.

### **4.4.2 Droplet encapsulation noise**

The generating function _𝐺_ describes the biological variability due to molecular processes, transcriptional driving, and the capture of cells from a reaction medium. However, single-cell RNA sequencing does not quantify cells — it quantifies _barcodes_ . Cells are randomly encapsulated into droplets with barcoded beads; to avoid the formation of “doublets,” with two cells per droplet, the microfluidic protocols typically have a fairly low encapsulation rate. If we assume that a droplet may have either zero or one cells, we obtain the following generating function for the distribution of RNA on a per-barcode level:


where _𝐺_ bc is the PGF of the Bernoulli distribution, with _𝑝_ 1 = _𝑝_ the probability of capturing a single cell and _𝑝_ 0 = 1 − _𝑝_ that of capturing none. Analogously, if we assume that doublets can occur, and the encapsulation of cells is i.i.d., we find


40

where _𝐺_ bc is now the PGF of the binomial distribution. It is straightforward to extend this to the unconstrained case, with per-cell encapsulation _rate 𝜆_ , and obtain the analogous expression


where _𝐺_ bc is the PGF of the Poisson distribution.

However, even empty droplets typically contain some “background” molecules. Removing the empty droplets by filtering for cells with relatively high expression, as well as correcting for the background, is a standard part of sequencing workflows [87, 187, 256, 322, 323]. To model the joint distribution of biological and background RNA, we need to instantiate a mechanistic hypothesis about its source. The simplest hypothesis consists of two parts. First, we impose the _pseudobulk_ interpretation of background: we assume that a fraction of the cells loaded in the library construction step are lysed, and produce a pool of loose molecules. Next, we assume that these molecules are free to be encapsulated into the droplets in an i.i.d. fashion. This implies the Poisson functional form for the distribution of debris entering each droplet:


where _𝑐_ is some shared constant that reflects the pool size and the rate of diffusion, whereas _𝜇𝑖_ =<sup>_<u>𝜕𝐺</u>_</sup> _𝜕𝑢𝑖_ ��� _𝑢𝑖_ =0<sup>is the expectation of species</sup><sup>_𝑖_over the entire cell population.</sup> This simplest model assumes that all cells are equally likely to lyse and release their contents; if this assumption is violated, _𝜇𝑖_ needs to be obtained by computing an expectation with respect to a measure biased toward the less stable cells. Finally, the full per-droplet distribution of molecules is


i.e., each droplet contains contributions from the encapsulated cells, as well as the background. With some abuse of notation, we note that the first argument denotes composition, whereas the second denotes functional dependence.

### **4.4.3 Library construction and sequencing noise**

We cannot observe the biological molecule content of each droplet: we are restricted to analyzing counts of complementary DNA (cDNA). In a typical dual-index 3<sup>′</sup> microfluidic workflow (e.g., the commercialized 10x chemistry [332]), these cDNA are

41

quantified by the following sequence of reactions. First, a synthetic primer captures a poly(A) stretch in RNA, which may be an endogenous molecule or a synthetic tag [268]. The primer contains a poly(dT) oligonucleotide, a sequencing primer, a cell barcode, and a unique molecular identifier (UMI). Next, reverse transcriptase (RTase) attaches to the RNA-primer complex and synthesizes the complementary strand. When the first strand is complete, a template-switching oligonucleotide (TSO) attaches to the end, allowing RT to synthesize the second strand of cDNA. After library construction, the droplet emulsion is broken, producing a pool of long cDNA; polymerase chain reaction (PCR) is used to amplify this pool. The long cDNA molecules are enzymatically fragmented, and another sequencing primer is attached at the end of the molecule that formerly contained the TSO. Finally, another round of PCR amplifies the pool and appends sample indices and Illumina adaptors to both sides of the molecule. The pool of cDNA is loaded onto a sequencing machine and sequenced from both sides, producing two reads. One read contains the barcode and UMI bases, whereas the other contains partial information about the 3<sup>′</sup> end of the molecule, beginning at the fragmentation site. This sequence of reactions represents the ideal-case scenario, and the products may well include artifacts due to off-target reactions [1].

To understand the effect of technical variability on the per-barcode distributions, we need to summarize this workflow in a mechanistic model. First, we assume that the library preparation reactions occur in an i.i.d. fashion relative to each RNA molecule in the droplet, allowing us to construct a separate description of technical noise for each discrete molecular species indexed by _𝑖_ . At this stage, we omit the modeling of continuous species. As we quantify the number of UMIs, we can considerably simplify the description by splitting the workflow into the initial cDNA synthesis and all downstream steps. For the cDNA synthesis, we may choose one of two models:


In the first model, the formation of a UMI-tagged cDNA T _𝑖_ is non-sequestering, and the template RNA X _𝑖_ can participate in further cDNA synthesis. In other words, a single RNA molecule can produce more than one cDNA with distinct UMIs. In the second model, the cDNA synthesis is sequestering, and each RNA can template at most one cDNA with a particular UMI. For the downstream steps, if we assume the PCR and sequencing steps produce results that are reasonably faithful to their

42

templates, we are essentially restricted to a single model:


In other words, the sequence of steps after the formation of cDNA T _𝑖_ may lose some UMIs, but it cannot create them. Aggregating these steps, we find the shifted per-molecule generating function for technical noise:


where _𝜆𝑖_ = _𝜆𝑖,𝑐 𝑝𝑖,𝑝_ and _𝑝𝑖_ = _𝑝𝑖,𝑐 𝑝𝑖,𝑝_ . _𝜆𝑖,𝑐_ is the overall Poisson rate of the catalytic production of cDNA T _𝑖_ with distinct UMIs, _𝑝𝑖,𝑐_ is the probability of producing a single cDNA T _𝑖_ in a non-catalytic fashion, and _𝑝𝑖,𝑝_ is the probability of retaining a molecule of T _𝑖_ through the PCR steps. It is straightforward to use a Taylor expansion to observe that the limit _𝜆𝑖,𝑐_ ≪ 1 yields the Bernoulli form: if non-sequestering sequencing is relatively slow or inefficient, the probability of obtaining multiple cDNA from a single RNA is low, and the mathematically simpler Bernoulli noise form approximately holds.

Using the properties of PGFs, we find that the overall generating function is given by a simple composition, plugging in _𝐺𝑡𝑖_ for _𝑔𝑖_ :


where we use the _𝐺_ tot( **u** ) parametrization, and each entry of **G** _𝑡_<sup>∗contains the shifted</sup> generating function _𝐺𝑡𝑖_<sup>∗for a particular species</sup><sup>_𝑖_.</sup>

Finally, the reads associated with each cDNA T are not always uniquely identifiable: for example, the sequence content is typically sufficient to identify the gene, but if a read only covers an exonic portion of the gene, it is impossible to distinguish whether or not the original molecule has been spliced [80]. To correctly represent this ambiguity, we need to transform the arguments of the generating function from a length- _𝑛_ vector to a length 𝓃-vector, such that 𝓃 is the total number of mutually distinguishable classes of molecules. The simplest form of this transformation is a linear categorical partition:


where 𝒫<sup>_𝑎_</sup> is an _𝑛_ × 𝓃 ambiguity matrix with 𝒫 _𝑖,_<sup>_𝑎_</sup> 𝒾<sup>giving the probability of molecule</sup> _𝑖_ being identifiable in the equivalence class 𝒾. We assume that each molecule can be

43

assigned to at least one class, implying<sup>�</sup> 𝒾<sup>𝒫</sup> _𝑖,_<sup>_𝑎_</sup> 𝒾<sup>= 1.In principle, only the constraint</sup> �𝒾<sup>𝒫</sup> _𝑖,_<sup>_𝑎_</sup> 𝒾<sup>≤1 is mandatory,but the loss of molecules can be equivalently reframed</sup> as a technical noise component in **G** _𝑡_<sup>∗.</sup>

We discuss the general case of this model component in Section B.2. In summary, the entries of 𝒫<sup>_𝑎_</sup> are challenging to identify, but it may be possible to exploit genomic information, polymer physics, and orthogonal long-read sequencing data to construct it from first principles. This formulation admits several special cases. For example, if we cannot distinguish any distinct species at all and can only quantify the total RNA content, 𝓃 = 1 and 𝒫 _𝑖,_<sup>_𝑎_</sup> 𝒾<sup>= 1 for each</sup><sup>_𝑖_.Then we yield</sup>


On the other hand, if all species are perfectly identifiable, we yield 𝓃 = _𝑛_ and 𝒫<sup>_𝑎_</sup> = _𝐼𝑛_ , the _𝑛_ -dimensional identity matrix. If, say, we have _𝑛_ = 2 but 𝓃 = 3, as in the case of nascent, mature, and ambiguous molecules described in [80, 168], we yield


where ℊ1 and ℊ2 correspond to two unambiguously identifiable species, whereas ℊ3 corresponds to ambiguous cDNA which may have come from either source. In the general case, we find


where each entry of the vector **G** _𝑎_ contains the generating function of the relevant categorical distribution that governs how species _𝑖_ is parsed as one of the 𝓃 identifiable species:


Therefore, the overall GF takes the following form:


44

### **4.5 A unified framework for scRNA-seq stochasticity**

We can summarize this entire theoretical machinery for Markovian processes as follows:


In the non-Markovian case, we use the methods in Section 4.3.2 to compute **U** .

### **4.6 Commonly encountered processes**

This section is a brief summary of the supplement of [106] by G.G. and L.P. G.G. performed the derivations.

Although this framework is quite generic, we typically focus on the stationary distributions of a small number of two-stage memoryless processes. These processes are hypotheses which attempt to represent the joint nascent and mature distributions in single-cell RNA sequencing datasets. These models have _𝑁_ = 1, _𝑛_ = 2, and _𝑚_ = 0, and may optionally be endowed with technical noise. Here, we report their kinetics and distributions.

### **4.6.1 Constitutive model**

The constitutive transcription model is the simplest nontrivial two-stage representation of RNA generation and processing. It includes the following kinetics:


where _𝑘_ is the transcription rate, _𝛽_ is the splicing rate, and _𝛾_ is the degradation rate. This yields the operators and characteristics


45

with all other operators set to zero. If _𝛾_ = _𝛽_ , the system degenerates and yields _𝑈𝑁_ ( **u** _,_ s) = _𝑒_<sup>−</sup><sup>_𝛾_s</sup> ( _𝑢𝑁_ + _𝛾𝑢𝑀_ s). This formulation induces the following stationary generating function:


The joint distribution of this model is bivariate Poisson:


where _𝜇𝑁_ = _𝑘_ / _𝛽_ and _𝜇𝑀_ = _𝑘_ / _𝛾_ . At steady state, we can set _𝑘_ to unity with no loss of generality.

### **4.6.2 Bursty model**

The two-stage _bursty_ transcription model includes the following kinetics [261]:


with stochastic burst sizes _𝐵_ drawn from a geometric distribution with scale _𝑏_ :


This formulation induces the following stationary generating function:


This integral is not available in closed form, but it is easy to show that the nascent marginal has negative binomial distribution with shape _𝑘_ / _𝛽_ and scale _𝑏_ . At steady state, we can set _𝑘_ to unity with no loss of generality.

### **4.6.3 Extrinsic noise model**

The _extrinsic_ transcription model accounts for non-Poisson statistics by proposing that the transcription rate varies between cells<sup>3</sup> . It includes the following kinetics:


46

where _𝑘_ is the transcription rate drawn from a gamma distribution with shape _𝜈_ and scale _𝜃_ , _𝛽_ is the splicing rate, and _𝛾_ is the degradation rate. This yields the operators and characteristics


with all others set to zero. This formulation induces the constitutive stationary generating function conditional on a particular value of _𝑘_ :


where the fourth line follows from recognizing the third line is the momentgenerating function of the mixing distribution _𝑓𝐾_ , evaluated at a particular argument. The joint distribution of this model is bivariate negative binomial [83]:


where _𝜇𝐾_ = _𝜈𝜃_ , _𝜇𝑁_ = _𝜇𝐾_ / _𝛽_ , and _𝜇𝑀_ = _𝜇𝐾_ / _𝛾_ . In addition, each marginal follows the negative binomial distribution with shape _𝜈_ and the corresponding mean. At steady state, we can set _𝜃_ to unity with no loss of generality.

### **4.6.4 Technical noise models**

To compute the distributions under the sequestering Bernoulli model of library construction, we make the substitutions


47

|Model|_𝜇𝑁_|_𝜇𝑀_|_𝐹_<sup>′</sup><br>_𝑁_|_𝐹_<sup>′</sup><br>_𝑀_|Cov_𝑁𝑀_|
|---|---|---|---|---|---|
|Constitutive|1<br>_𝛽_|1<br>_𝛾_|0|0|0|
|Bursty|_𝑏_<br>_𝛽_|_𝑏_<br>_𝛾_|_𝑏_<br>|_𝑏𝛽_<br>_𝛽_+_𝛾_<br>|_𝑏_<sup>2</sup><br>_𝛽_+_𝛾_|
|Extrinsic|_𝜈_<br>_𝛽_|_𝜈_<br>_𝛾_|1<br>_𝛽_|1<br>_𝛾_|_𝜈_<br>_𝛽𝛾_|


Table 4.1: Lower moments of the three common models without technical noise.

|Model|_𝜇𝑁_<br>|_𝜇𝑀_<br>|_𝐹_<sup>′</sup><br>_𝑁_||_𝐹_<sup>′</sup><br>_𝑀_|Cov_𝑁𝑀_|
|---|---|---|---|---|---|---|
|Constitutive|_𝜆𝑁_<br>_𝛽_|_𝜆𝑀_<br>_𝛾_|_𝜆𝑁_||_𝜆𝑀_|0|
|Bursty|_𝑏𝜆𝑁_<br>_𝛽_|_𝑏𝜆𝑀_<br>_𝛾_|_𝜆𝑁_(1+_𝑏_)<br><br>|_𝜆𝑀_<br>�|1+ <sup>_𝑏𝛽_</sup><br>_𝛽_+_𝛾_<br>�<br><br>|_𝑏_<sup>2</sup>_𝜆𝑁𝜆𝑀_<br>_𝛽_+_𝛾_|
|Extrinsic|_𝜈𝜆𝑁_<br>_𝛽_|_𝜈𝜆𝑀_<br>_𝛾_|_𝜆𝑁_<br>�<br>1+ <sup>1</sup><br>_𝛽_<br>�|_𝜆𝑀_|�<br>1+ <sup>1</sup><br>_𝛾_<br>�|_𝜈𝜆𝑁𝜆𝑀_<br>_𝛽𝛾_|


Table 4.2: Lower moments of the three models under Poisson noise.

To compute the distributions under the non-sequestering Poisson model of library construction, we make the substitutions


### **4.6.5 Moment identities**

By differentiating the generating functions, it is straightforward to obtain the lower moments of the resulting distributions (Section 3.1.3). In Tables 4.1 and 4.2, we report the lower moments for the underlying biological distributions and the noisecorrupted distributions. The variances are reported in terms of the shifted Fano factor _𝐹𝑖_<sup>′:=</sup><sup>_𝜎_</sup> _𝑖_<sup>2/</sup><sup>_𝜇𝑖_−1, which produces the most compact representations.</sup>

48

_C h a p t e r 5_

---

[← MATHEMATICAL TOOLS AND PRELIMINARIES](10-mathematical-tools-and-preliminaries.md) · [Up: contents](index.md) · [COMPUTATIONAL CONSIDERATIONS →](12-computational-considerations.md)
