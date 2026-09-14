---
title: 1.2 Evolving Probabilities
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/lectures/01-slides.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1.2 Evolving Probabilities

**Source:** `lectures/01-slides.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

As organisms reproduce the underlying genetic information is passed on to subsequent generation. The copying of the genetic content is not perfect, and leads to a diverse and evolving population of organisms after many generations. The changes are stochastic, and are thus appropriately described by evolving probability distributions. After motivating such evolving probabilities in the contexts of DNA and populations, we introduce the mathematical tools for treating them.

### **1.2.1 Mutations**

Consider the flow of information from DNA, transcribed to messenger RNA, and eventually translated to an amino acid chain. Suppose we begin with the DNA fragment

### ATT CGC ATG _,_

which when unwound and transcribed to mRNA, appears as the complementary messenger chain


The protein building machinery (ribosome) translates this to a _peptide_ chain consisting of a leucine, an alanine, and a tyrosine molecule, symbolically,


Suppose, however, that a replication mistake causes the DNA strand’s last “letter” to change. Instead of ATG, the last codon now reads ATC, which is a “stop signal”

### Leu Ala STOP _._

Such a mutation, let’s say in the middle of a protein chain, will stop the translation process. The mutation is _deleterious_ and the off-spring will not survive. However, as a result of the

3

redundancy in the genetic code, there are also mutations that are _synonymous,_ in that they do not change the amino acid which eventually results. Because these synonymous mutations do not affect the biological viability of the organism, we can find genes whose exact DNA varies from individual to individual. This has opened up the field of DNA “fingerprinting”: blood can be matched to the person who shed it by comparing such _single nucleotide polymorphisms_ (SNPs). Non-synonymous mutations are not necessarily deleterious and may lead to viable off-spring.

### **1.2.2 Classical Genetics**

The study of heredity began long before the molecular structure of DNA was understood. Several thousand years of experience breeding animals and plants led, eventually, to the idea that hereditary characteristics are passed along from parents to offspring in units, which are termed _genes._

Classical genetics states that some genes are _dominant_ and others _recessive._ For example, suppose we have a certain “heredity unit” symbolized as _A_ 1 whose presence in an individual leads to brown eyes. A variant gene, _A_ 2, sometimes appears in the population; individuals carrying it grow up with blue eyes. Humans, among other _diploid_ organisms, carry two genes for each trait, which are called _alleles._ According to the classical concept of dominance, having one dominant allele outweighs the presence of a recessive one. Brown eyes turn out to be dominant in humans, so a person with an _A_ 1 _A_ 2 mix of alleles has brown irises, just like one whose alleles read _A_ 1 _A_ 1. Only an _A_ 2 _A_ 2 individual develops blue irises.

### **1.2.3 Master Equation**

Let us consider the evolution of probabilities in the context of the simplified model introduced earlier of _N_ independently distributed sites. We model mutations by assuming that at subsequent time-steps (generations) each site may change its state (independent of the other sites), say from _α_ to _β_ with a _transition probability πβα_ . The _q × q_ such elements form the _transition probability matrix_<sup>_←→_</sup> _π_ . (Without the assumption that the sites evolve independently, we would have constructed a much larger ( _q_<sup>_N_</sup> _× q_<sup>_N_</sup> ) matrix<sup>_←→_</sup> Π . With the assumption of independence, this larger matrix is a direct product of transition matrices for individual sites, i.e.<sup>_←→_</sup> Π =<sup>_←→_</sup> _π_ 1 _⊗_<sup>_←→_</sup> _π_ 2 _⊗· · · ⊗_<sup>_←→_</sup> _π N_ .) Using the transition probability matrix, we can track the evolution of the probabilities as


where the last identity is obtained by recursion, assuming that the transition probability matrix remains the same.

Probabilities must be normalized to unity, and thus the transition probabilities are constrained by


4

The last expression formalizes the statement that in probability to stay in the same state is the complement of the probabilities to make a change. Using this result, we can rewrite Eq. (1.9) as


In many circumstances of interest the probabilities change slowly and continuously over time, in which case we introduce a small time interval between subsequent events, and write


In the limit of small ∆ _t_ , [ _pα_ ( _τ_ + 1) _− pα_ ( _τ_ )] _/_ ∆ _t ≈ dpα/dt_ , while


are the off-diagonal elements of the matrix<sup>_←→_</sup> _R_ of _transition probability rates_ . The diagonal elements of the matrix describe the depletion rate of a particular state, and by conservation of probability must satisfy, as in Eq. (1.10),


We thus arrive at


which is known as the _Master equation_ .

### **1.2.4 Steady state**

Because of the conservation of probability in Eqs. (1.10) and (1.14), the transition probability matrix<sup>_←→_</sup> _π_ , and by extension the rate matrix<sup>_←→_</sup> _R_ have a left-eingenvector<sup>_←−_</sup> _v_<sup>_∗_</sup> = (1 _,_ 1 _, · · · ,_ 1) with eigenvalues of unity and zero respectively, i.e.


For each eigenvalue there is both a left eigenvector and a right eigenvector. The matrices _←→ π_ and<sup>_←→_</sup> _R_ thus must also have a right-eigenvector<sup>_−→_</sup> _p_<sup>_∗_</sup> such that


The elements of the vector<sup>_−→_</sup> _p_<sup>_∗_</sup> represent the _steady state probabilities_ for the process. These probabilities no longer change with time. The other eigenvalues of the matrix determine how an initial vector of probabilities approaches this steady state.

5

As a simple example, let us consider a _binary_ sequence (i.e. _m_ = 2) with independent states _A_ 1 or _A_ 2 at each site.<sup>1</sup> Let us assume that the state _A_ 1 can “mutate” to _A_ 2 at a rate _µ_ 2, while state _A_ 2 may change to _A_ 1 with a rate _µ_ 1. The probabilities _p_ 1( _t_ ) and _p_ 2( _t_ ) now evolve in time as


The above 2 _×_ 2 transition rate matrix has the following two eigenvectors


As anticipated, there is an eigenvector<sup>_−→_</sup> _p_<sup>_∗_</sup> with eigenvalue of zero; the elements of this vector are normalized to add to unity, as required for probabilities. We have not normalized the second eigenvector, whose eigenvalue _−_ ( _µ_ 1 + _µ_ 2) determines the rate of approach to steady state.

To make this explicit, let us start with a sequence that is purely _A_ 1, i.e. with _p_ 1 = 1 and _p_ 2 = 0 at _t_ = 0. The formal solution to the linear differential equation (1.18) is


Decomposing the initial state as a sum over the eigenvectors, and noting the action of the rate matrix on each eigenvector from Eq. (1.19), we find


At long times the probabilities to find state _A_ 1 or _A_ 2 are in the ratios _µ_ 1 to _µ_ 2 as dictated by the steady state eigenvector. The rate at which the probabilities converge to this steady steady is determined by the eigenvalue _−_ ( _µ_ 1 + _µ_ 2).

### **1.2.5 Mutating Population**

The previous example of a binary sequence of length _N_ can be recast and interpreted in terms of the evolution of a population as follows. Let us assume that _A_ 1 and _A_ 2 denote two forms of a particular allele. In each generation each individual is replaced by an offspring that mostly retains its progenitor’s allele, but may mutate to the other form at some rate. In this model the total population size is fixed to _N_ , while the sub-populations _N_ 1 and _N_ 2

> 1Clearly with the assumption of independence we are really treating independent sites, and the insistence on a sequence may appear frivolous. The advantage of this perspective, however, will become apparent in the next section.

6

may vary. A particular state of the population is thus described by _N_ 1 = _n_ and _N_ 2 = _N − n_ , and since _n_ = 0 _,_ 1 _, · · · , N_ there are _N_ + 1 possible states. At a particular time, the system may be in any one of these states with probability _p_ ( _n, t_ ), and we would like to follow the evolution of these probabilities.

After an individual replication event ( _A_ 1 to _A_ 1 at rate _−µ_ 2, _A_ 1 to _A_ 2 at rate _µ_ 2, _A_ 2 to _A_ 1 at rate _µ_ 1, or _A_ 2 to _A_ 2 at rate _−µ_ 1), the number _N_ either stays the same, or changes by unity. Thus the transition rate matrix only has non-zero terms along or adjoining to the diagonal. For example


where the former indicates that a population of _n_ + 1 _A_ 1s can decrease by one if any one of them mutates to _A_ 2, while the population a population with _n−_ 1 _A_ 1s increases by one if any of _A_ 2s mutates to _A_ 1. The diagonal terms are obtained from the normalization condition in Eq. (1.14) resulting in the Master equation

_dp_ <u>(</u> _n, t_ <u>)</u> = _µ_ 2( _n_ + 1) _p_ ( _n_ + 1) + _µ_ 1( _N − n_ + 1) _p_ ( _n −_ 1) _− µ_ 2 _np_ ( _n_ ) _− µ_ 1( _N − n_ ) _p_ ( _n_ ) _,_ (1.23) _dt_ for 0 _< n < N_ , and with boundary terms


### **1.2.6 Enzymatic reaction**

The appeal of the formalism introduced above is that the same concepts and mathematical formulas apply to a host of different situations. For example consider the reactions


where the enzyme E facilitates the conversion of A to B at a rate _a_<sup>_′_</sup> , and the backward reaction at rate _b_<sup>_′_</sup> . In a well mixed system, the numbers _NA_ and _NB_ = _N − NA_ of the two species evolve according to the “mean-field” equation


where _a_ = _NEa_<sup>_′_</sup> and _b_ = _NEb_<sup>_′_</sup> . In this approximation, the fluctuations are ignored and the mean numbers of constituents evolve to the steady state with _NA_<sup>_∗/N_</sup> _B_<sup>_∗_=</sup><sup>_b/a_.</sup>

However, in a system where the number of particles is small, for example for a variety of proteins within a cell, the mean number may not be representative, and the entire distribution is relevant. The probability to find a state with _NA_ = _n_ and _NB_ = _N − NA_ , then evolves precisely according to Eq. (1.23) introduced above in the context of mutating populations. From the equivalence of this equation to the independently evolving binary states, we know that the final steady steady state solution also describes a chain of binary

7

elements independently distributed with probabilities _p_<sup>_∗_</sup> _A_<sup>=</sup><sup>_b/_(</sup><sup>_a_+</sup><sup>_b_)and</sup><sup>_p∗_</sup> _B_<sup>=</sup><sup>_a/_(</sup><sup>_a_+</sup><sup>_b_).</sup> Hence, the steady state solution to the complicated looking set of equations (1.23) is simply


In fact, we can follow the full evolution of the probability to this state, starting let’s say with an initial state that is all A.

8

������������������ ������������������

������������������������������������������������

�����������

��������������������������������������������������������������������������������������������������

---

[← 1.1 Probability & Information](01-1-1-probability-information.md) · [Up: contents](index.md)
