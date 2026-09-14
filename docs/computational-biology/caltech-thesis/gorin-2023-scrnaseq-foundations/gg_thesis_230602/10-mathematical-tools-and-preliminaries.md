---
title: MATHEMATICAL TOOLS AND PRELIMINARIES
source: https://thesis.library.caltech.edu/16062/
source_file: sources/gorin-2023-scrnaseq-foundations/gg_thesis_230602.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# MATHEMATICAL TOOLS AND PRELIMINARIES

**Source:** `gg_thesis_230602.pdf` from [gorin-2023-scrnaseq-foundations](https://thesis.library.caltech.edu/16062/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.1 Common mathematical objects, distributions, and identities 3.1.1 Mathematical objects and key notation**

We generally operate with the following hierarchy of variable spaces:


where N0 denotes the non-negative natural numbers 0 _,_ 1 _,_ 2 _, ..._ ; Z denotes the integers; R denotes the real numbers; and C denotes the complex numbers. We occasionally use R≥0 to denote the non-negative real numbers and R+ to denote the positive real numbers. We typically denote variables on N0 and Z by _𝑥_ , on R by _𝑦_ , and on C by _𝑔_ , _𝑢_ , or _ℎ_ , giving the domains explicitly where necessary. In the context of stochastic processes, the real-valued variables represent the “spatial” degrees of freedom, i.e., the value of the process at a given instant. _𝑧_ is a generic variable. The variable _𝑡_ ∈ R denotes the process time.

Vector quantities are typically set in boldface, e.g., **x** = [ _𝑥_ 1 _, . . . , 𝑥𝑛_ ]<sup>T</sup> ∈ N0<sup>_𝑛_.Matrices</sup> are typically represented by uppercase letters, e.g.,


We use calligraphic fonts for generic mathematical objects; for example, F is used for neural functions, and H represents an operator. L always represents a likelihood, and D always represents some collection of data. Molecular species are also set in calligraphic fonts. Thus, for example, mature mRNA species are defined as X _𝑀_ , their microstates are written as _𝑥𝑀_ , and their actual observed amounts, or the associated random variable, are written as _𝑋𝑀_ ; the underlying mean may be reported as _𝜇𝑀_ and the sample mean as _𝑋 𝑀_ .

In a statistical context, Θ represents generic parameters or parameter vectors. Notation to the effect of Θ<sup>ˆ</sup> represents an estimate of Θ; such estimates are typically, but not always, data-derived (for a counterexample, see Section 5.3). _𝜋_ or _𝝅_ represents compositional quantities, such as cell type fractions. _𝜅_ indexes over cell types or subpopulations.

15

I represents the identity function, which returns unity if its argument is true and zero otherwise. _𝛿_ represents the relevant (discrete or continuous) flavor of degenerate function.

_𝑖_ , _𝑗_ , and _𝑘_ are generic indexing subscripts. _𝑘_ is occasionally used to denote transcriptional burst frequencies, interchangeably with _𝛼_ . Nc denotes the total number of cells, indexed by c. Ng denotes the total number of genes, indexed by g. N denotes the total number of approximating terms, indexed by n. Nk denotes the total number of simulations, indexed by k.

Graph edges and reaction rates are always defined in the source–sink notation, i.e., a rate _𝑐𝑖𝑗_ always represents a species X _𝑖_ giving rise to species X _𝑗_ .

_𝑃_ represents a probability density or mass function used to define a master equation. _𝑝_ represents probability distributions auxiliary to the master equation, e.g., the burst size distribution. _𝑓_ represents generic probability densities.

### **3.1.2 Stochastic process framework**

In the most general case, we study processes that evolve in time over a domain _𝑁_ × N0<sup>_𝑛_× R</sup><sup>_𝑚_</sup> ≥0<sup>.Theinstantaneousstateofsuchaprocessisgivenbyacollection</sup> of variables ( _𝑠,_ **x** _,_ **y** _, 𝑡_ ). Thus, at time _𝑡_ , _𝑠_ gives the component of the state on a size- _𝑁_ finite lattice, **x** on an _𝑛_ -dimensional discrete infinite lattice, and **y** on an _𝑚_ -dimensional continuous space.

The evolution of the state over time may or may not be perfectly predictable at a time _𝑡_ given a set of prescribed initial conditions {( _𝑠_<sup>0</sup> _,_ **x**<sup>0</sup> _,_ **y**<sup>0</sup> _, 𝑡_<sup>0</sup> )}, and a set of physical laws governing the state transitions. Out of physical realism, we typically impose the condition that all of { _𝑡_<sup>0</sup> } ≤ _𝑡_ . If the physical laws are deterministic, we can study the system’s evolution using dynamical systems approaches. However, if they are non-deterministic, we need to invoke the machinery of stochastic processes, and treat the system probabilistically, such that


where _𝑃_ is a probability distribution that generates realizations through the random variables { _𝑆, 𝑋_ 1 _, . . . , 𝑋𝑛,𝑌_ 1 _, . . . ,𝑌𝑚_ }.

A particularly tractable subset of stochastic processes has the _Markov_ property, where


16

where _𝑡_<sup>0</sup> is the largest value in the collection { _𝑡_<sup>0</sup> }, and _𝑠_<sup>0</sup> _,_ **x**<sup>0</sup> _,_ **y**<sup>0</sup> is the associated state. If the Markov property holds, we need only specify the initial condition at a single time _𝑡_<sup>0</sup> to obtain the system’s statistical behavior for all _𝑡> 𝑡_<sup>0</sup> ; we use _𝑡_<sup>0</sup> = 0 with no loss of generality. It is occasionally helpful to go one step further and define a probabilistic rather than deterministic initial condition _𝑃_<sup>0</sup> :


In the current context, it turns out to be mathematically simpler to use a length- _𝑁_ probability vector, such that


### **3.1.3 Generating functions**

This section summarizes the mathematical machinery formalized in [115] by G.G., J.J.V., and L.P. G.G. developed this approach as a generalization of the framework constructed by J.J.V. in [113] by G.G.<sup>∗</sup> , J.J.V.<sup>∗</sup> , M.F., and L.P.

The analysis of stochastic processes typically proceeds through _generating functions_ [95]. In the general case, the generating function (GF) is a length- _𝑁_ vector **G** , such that


where the second line is an abbreviated shorthand for the first. We elide the dependence on time and initial conditions for notational simplicity. The arguments **g** ∈ C<sup>_𝑛_</sup> and **h** ∈ C<sup>_𝑚_</sup> are spectral variables. It is frequently easier to treat the shifted coordinate **u** := **g** − 1. Strictly speaking, the mathematical object **G** is the combination of a probability-generating function (PGF) in the discrete dimensions and a moment-generating function (MGF) in the continuous dimensions. The generic discrete-only PGF is defined and condensed as follows:


17

where _𝑃_ is a probability mass function (PMF).

The generic continuous-only MGF is defined and condensed as follows:


where _𝑃_ is a probability density function (PDF). It is straightforward to see that the MGF can be obtained by evaluating the PGF at arguments _𝑔𝑖_ = _𝑒_<sup>_ℎ𝑖_</sup> . The converse does not hold, because the PGF is only defined for random variables on N0.

When it exists, the generating function allows us to reconstruct properties of the original distribution. First, evaluating a component of the PGF at _𝑔𝑖_ = 1 (or the MGF at _ℎ𝑖_ = 0) marginalizes over dimension _𝑖_ . Second, evaluating the derivatives of the PGF at _𝑔𝑖_ = 1 produces the factorial moments, such that


where _𝑋𝑖_ denotes the random variable with values reported in _𝑥𝑖_ ; similarly, the crossmoments can be obtained by taking mixed derivatives. Analogously, evaluating the derivatives of the MGF at _ℎ𝑖_ = 0 produces the raw moments:


Third, evaluating the derivatives of the PGF at _𝑔𝑖_ = 0 recovers the probability mass function:


where we have assumed that all other dimensions have been marginalized out; joint distributions can be obtained by taking partial derivatives with respect to multiple dimensions.

As generating functions are spectral transforms of the original probability distributions, they inherit many other generic properties of the Fourier transform. These properties are summarized in standard texts [154, 155], and we report them as necessary for derivations.

18

### **3.1.4 Special functions**

To introduce specific functional forms of stochastic processes and their solutions, it is helpful to be aware of _special functions_ commonly encountered in the field. We reproduce their definitions from the standard text by Abramowitz and Stegun [2] without delving into the derivations or functional analysis properties.

The factorial _𝑥_ ! over _𝑥_ ∈ N0 is defined as follows:


such that 0! = 1.

A generalization of the factorial, the gamma function, is defined over _𝑧_ ∈ C:


such that Γ( _𝑥_ + 1) = _𝑥_ ! for _𝑥_ ∈ N0.

The Pochhammer symbol, or rising factorial, is defined over _𝑧_ ∈ C and _𝑛_ ∈ N0:


The binomial coefficient is defined over _𝑧, 𝑥_ ∈ C:


where the second identity holds for _𝑧, 𝑥_ ∈ N0 such that _𝑧_ ≥ _𝑥_ .

The upper incomplete gamma function is defined over _𝑧, 𝑥_ ∈ C:


such that Γ( _𝑧,_ 0) = Γ( _𝑧_ ). Usefully, at integer arguments,


Kummer’s confluent hypergeometric function is defined over _𝑎, 𝑏, 𝑧_ ∈ C:


19

When − _𝑎_ ∈ N, this function can be expressed as a polynomial with a finite number of terms.

The hypergeometric function, or Gauss’s hypergeometric function, is defined over _𝑎, 𝑏, 𝑐, 𝑧_ ∈ C:


Usefully, at negative integer arguments, the summation terminates:


The beta function is defined over _𝑧, 𝑥_ ∈ C:


It is essential to notice that these functions can be defined by recurrence relations; for example, Γ( _𝑛_ + 1) = _𝑛_ Γ( _𝑛_ ). This deceptively simple form suggests a fundamental computational challenge: we would typically like the evaluation to be independent of the particular value of _𝑛_ , requiring methods more sophisticated than applying the definition.

Finally, the principal branch of the Lambert _𝑊_ function, which does not take a combinatorial form, is implicitly defined over _𝑥_ ∈ R+:


### **3.1.5 Continuous distributions**

The current section defines the conventions for common continuous probability distributions. Here, we report the probability density functions and other salient properties. The definitions in this and following sections are largely reproduced from the Johnson texts [154, 155].

The normal, or Gaussian, distribution over _𝑦_ ∈ R is parametrized by its mean _𝜇_ ∈ R and standard deviation _𝜎_ ∈ R+:


The normal distribution is ubiquitous in statistical inference, where it arises as a consequence of the central limit theorem [154], and the study of continuous-valued

20

stochastic processes, where it is used to construct Gaussian processes [265]. In addition, a wide variety of data exploration, analysis, and summary techniques, such as principal component analysis, are tailored to normally-distributed variation [259]. The cumulative distribution function of the standard normal distribution with _𝜇_ = 0 and _𝜎_ = 1 is defined to be Φ( _𝑦_ ).

The lognormal distribution over _𝑦_ ∈ R+ is parametrized by the mean _𝜇𝑙_ ∈ R and standard deviation _𝜎𝑙_ ∈ R+ of the underlying exponentiated normal distribution [51]. With some abuse of terminology, we refer to these parameters as the log-mean and the log-standard deviation.


This distribution has the following mean _𝜇_ and standard deviation _𝜎_ :


Usefully, we can set the parameters to produce a specified set of moments:


The quantile function of the lognormal distribution have the following form:


The bivariate lognormal distribution over _𝑦_ 1 _, 𝑦_ 2 ∈ R+ is parametrized by the means _𝜇_ 1 _𝑙, 𝜇_ 2 _𝑙_ ∈ R, standard deviations _𝜎_ 1 _𝑙, 𝜎_ 2 _𝑙_ ∈ R+, and correlation _𝜌𝑙_ ∈[−1 _,_ 1] of the underlying bivariate normal distribution [51]:


21

The marginal distributions are lognormal with the appropriate parameters. Usefully, we can set the _𝜌𝑙_ to produce a desired correlation _𝜌_ :


In addition, the conditional distribution over _𝑦_ 2, given a particular _𝑦_ 1, is lognormal with parameters


The exponential distribution over _𝑦_ ∈ R+ is parametrized by its scale _𝜃_ ∈ R+ or its rate _𝜂_ = _𝜃_<sup>−1</sup> :


The former parametrization is less common, but more convenient for representing its MGF:


The mean of the exponential distribution is _𝜃_ . This distribution is ubiquitous in the study of Markovian stochastic processes, because exponentially-distributed waiting times are _memoryless_ .

The gamma distribution over _𝑦_ ∈ R+ is parametrized by its shape _𝜈_ ∈ R+ and its scale _𝜃_ or rate _𝜂_ = _𝜃_<sup>−1</sup> :


The former parametrization is convenient for representing its MGF:


The mean of the gamma distribution is _𝜈𝜃_ . The exponential distribution is a special case of the gamma distribution ( _𝜈_ = 1). The Erlang distribution is another special case ( _𝜈_ ∈ N).

22

The continuous uniform distribution over _𝑦_ ∈[ _𝑎, 𝑏_ ] is parametrized by its bounds:


The inverse Gaussian distribution over _𝑦_ ∈ R+ is parametrized by parameters _𝑎, 𝑏_ ∈ R+ [248]:


The Dirac delta, or continuous degenerate, distribution over _𝑦_ ∈ R is defined as follows:


for any function _𝑓_ . Therefore, the delta function’s probability density is a point mass at zero. Translating this function and integrating _𝛿_ ( _𝑡_ − _𝑎_ ) returns _𝑓_ ( _𝑎_ ).

### **3.1.6 Discrete distributions**

Here, we report the probability mass functions of common discrete distributions.

The Poisson distribution over _𝑥_ ∈ N0 is parametrized by its mean _𝜇_ :


Many common discrete distributions arise as Poisson- _𝐷_ mixtures, where _𝐷_ is a mixing distribution that controls the mean. Conceptually,


Usefully, to obtain the PGF of the Poisson mixture at spectral argument _𝑔_ , we can simply evaluate the MGF of the mixing distribution at _𝑔_ − 1. Standard texts report further relationships between the underlying and mixed distributions, which we do not reproduce here [157, 215].

The geometric distribution on _𝑥_ ∈ N0 is a Poisson-exponential mixture. It is parametrized by the scale _𝜃_ ∈ R+ of the underlying exponential distribution:


This parametrization is convenient for representing its PGF. The mean of the geometric distribution is _𝜃_ .

23

The negative binomial distribution on _𝑥_ ∈ N0 is a Poisson-gamma mixture. It can be parametrized by the form of the underlying distribution or by the resulting shape and mean ( _𝜇_ = _𝜈𝜃_ ):


The discrete degenerate distribution supported solely on _𝑥_ = _𝑗_ and zero elsewhere can be represented by a Kronecker delta:


### **3.2 Model selection criteria**

The likelihood of parameters Θ under a proposed distribution _𝑃_ and a data distribution D is simply the total probability of the data:


where we obtain the second line by assuming observations are independent and the third line by assuming they are independent and identically distributed (i.i.d.) [208]. Much of statistical inference consists of investigating and characterizing the behavior of L as a function of Θ, and many of the associated challenges stem from L not being available in closed form.

The likelihood ratio (LR) compares the strength of evidence for various parameters or models Θ _𝐴_ and Θ _𝐵_ , which are treated as point estimates [208]:


The Bayes factor (BF) is used to compare models _𝑀𝐴_ and _𝑀𝐵_ , and takes into account the uncertainty in their associated parameters Θ _𝐴_ and Θ _𝐵_ [38]:


24

In this case, _𝑃_ (D; ·) is the data likelihood and _𝑓_ is the prior. If the prior or the likelihood is Dirac-like, i.e., the parameters are deterministic, the Bayes factor is equivalent to the likelihood ratio.

The Akaike information criterion (AIC) is a penalized likelihood used to compare point estimates of models _𝑘_ at their optimal parameter estimates Θ<sup>ˆ</sup> _𝑘_ [38]:


where _𝜍𝑘_ is the number of estimated model parameters. Usefully, the AIC can be used to compute posterior probabilities for a set of models:


where _𝑤𝜛_ is the _Akaike weight_ of the model _𝜛_ [38].

### **3.3 Distance measures**

The Kullback-Leibler divergence (KLD) between a discrete data distribution D, i.e., a normalized histogram over microstates **x** , and a proposed distribution _𝑃_ is defined as follows:


Evidently, only the observed microstates, with D( **x** ) _>_ 0, contribute to this quantity. The KLD generalizes to continuous distributions, with an integral replacing the summation. If the KLD is high, the distributions are dissimilar. In a statistical context, minimizing the KLD is equivalent to maximizing the likelihood of data under the proposed distribution.

The Jaccard distance _𝑑𝐽_ is defined as follows:


where _𝐴_ and _𝐵_ are sets and | · | represents the set size. If the Jaccard distance is high, the sets have little overlap. Many other distances are discussed in further detail in [73].

25

_C h a p t e r 4_

---

[← TECHNOLOGIES, DESIDERATA, AND AXIOMS](09-technologies-desiderata-and-axioms.md) · [Up: contents](index.md) · [STOCHASTIC MODELS AND SOLUTIONS →](11-stochastic-models-and-solutions.md)
