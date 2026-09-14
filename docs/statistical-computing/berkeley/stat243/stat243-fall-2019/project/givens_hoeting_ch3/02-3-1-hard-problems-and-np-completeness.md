---
title: 3.1 HARD PROBLEMS AND NP-COMPLETENESS
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/project/givens_hoeting_ch3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/project/givens_hoeting_ch3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.1 HARD PROBLEMS AND NP-COMPLETENESS

**Source:** [`project/givens_hoeting_ch3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/project/givens_hoeting_ch3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Hard optimization problems are generally combinatorial in nature. In such problems, _p_ items may be combined or sequenced in a very large number of ways, and each choice corresponds to one element in the space of possible solutions. Maximization requires a search of this very large space.

For example, consider the _traveling salesman problem_ . In this problem, the salesman must visit each of _p_ cities exactly once and return to his point of origin, using the shortest total travel distance. We seek to minimize the total travel distance over all possible routes (i.e., maximize the negative distance). If the distance between two cities does not depend on the direction traveled between them, then there are

> _Computational Statistics_ , Second Edition. Geof H. Givens and Jennifer A. Hoeting. © 2013 John Wiley & Sons, Inc. Published 2013 by John Wiley & Sons, Inc.

**59**

**60 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

( _p_ − 1)! _/_ 2 possible routes (since the point of origin and direction of travel are arbitrary). Note that any tour corresponds to a permutation of the integers 1 _, . . . , p_ , which specifies the sequence in which the cities are visited.

To consider the difficulty of such problems, it is useful to discuss the number of steps required for an algorithm to solve it, where steps are simple operations like arithmetic,comparisons,andbranching.Thenumberofoperationsdepends,ofcourse, on the size of the problem posed. In general the size of a problem may be specified as the number of inputs needed to pose it. The traveling salesman problem is posed by specifying _p_ city locations to be sequenced. The difficulty of a particular size- _p_ problem is characterized by the number of operations required to solve it in the worst case using the best known algorithm.

The number of operations is only a rough notion, because it varies with implementation language and strategy. It is conventional, however, to bound the number of operations using the notation _O_ ( _h_ ( _p_ )). If _h_ ( _p_ ) is polynomial in _p_ , an algorithm is said to be polynomial.

Although the actual running time on a computer depends on the speed of the computer, we generally equate the number of operations and the execution time by relying on the simplifying assumption that all basic operations take the same amount of time (one unit). Then we may make meaningful comparisons of algorithm speeds even though the absolute scale is meaningless.

Consider two problems of size _p_ = 20. Suppose that the first problem can be solved in polynomial time [say _O_ ( _p_<sup>2</sup> ) operations], and the solution requires 1 minute on your office computer. Then the size-21 problem could be solved in just a few seconds more. The size-25 problem can be solved in 1.57 minutes, size 30 in 2.25 minutes, and size 50 in 6.25 minutes. Suppose the second problem is _O_ ( _p_ !) and requires 1 minute for size 20. Then it would take 21 minutes for size 21, 12.1 years (6,375,600 minutes) for size 25, 207 million years for size 30, and 2 _._ 4 × 10<sup>40</sup> years for size 50. Similarly, if an _O_ ( _p_ !) traveling salesman problem of size 20 could be solved in 1 minute, it would require far longer than the lifetime of the universe to determine the optimal path for the traveling salesman to make a tour of the 50 U.S. state capitals. Furthermore, obtaining a computer that is 1000 times faster would barely reduce the difficulty. The conclusion is stark: Some optimization problems are simply too hard. The complexity of a polynomial problem—even for large _p_ and high polynomial order—is dwarfed by the complexity of a quite small nonpolynomial problem.

The theory of problem complexity is discussed in [214, 497]. For us to discuss this issue further, we must make a formal distinction between _optimization_ (i.e., search) problems and _decision_ (i.e., recognition) problems. Thus far, we have considered optimization problems of the form: “Find the value of **_θ_** ∈ **_�_** that maximizes _f_ ( **_θ_** ).” The decision counterpart to this is: “Is there a **_θ_** ∈ **_�_** for which _f_ ( **_θ_** ) _> c_ , for a fixed number _c_ ?” Clearly there is a close relationship between these two versions of the problem. In principle, we could solve the optimization problem by repeatedly solving the decision problem for strategically chosen values of _c_ .

Decision problems that can be solved in polynomial time [e.g., _O_ ( _p_<sup>_k_</sup> ) operations for _p_ inputs and constant _k_ ] are generally considered to be efficiently solvable [214]. These problems belong to the class denoted P. Once any polynomial–time algorithm has been identified for a problem, the order of the polynomial is often quickly reduced

**3.1 HARD PROBLEMS AND NP-COMPLETENESS 61**

to practical levels [497]. Decision problems for which a given solution can be checked in polynomial time are called NP problems. Clearly a problem in P is in NP. However, there seem to be many decision problems, like the traveling salesman problem, that are much easier to check than they are to solve. In fact, there are many NP problems for which no polynomial–time solution has ever been developed. Many NP problems have been proven to belong to a special class for which a polynomial algorithm found to solve one such problem could be used to solve all such problems. This is the class of NP-complete problems. There are other problems at least as difficult, for which a polynomial algorithm—if found—would be known to provide a solution to all NPcomplete problems, even though the problem itself is not proven to be NP-complete. These are NP-hard problems. There are also many combinatorial decision problems that are difficult and probably NP-complete or NP-hard although they haven’t been proven to be in these classes. Finally, optimization problems are no easier than their decision counterparts, and we may classify optimization problems using the same categories listed above.

It has been shown that if there is a polynomial algorithm for any NP-complete problem, then there are polynomial algorithms for all NP-complete problems. The utter failure of scientists to develop a polynomial algorithm for any NP-complete problem motivates the popular conjecture that there cannot be any polynomial algorithm for any NP-complete problem. Proof (or counterexample) of this conjecture is one of the great unsolved problems in mathematics.

This leads us to the realization that there are optimization problems that are inherently too difficult to solve exactly by traditional means. Many problems in bioinformatics, experimental design, and nonparametric statistical modeling, for example, require combinatorial optimization.

### **3.1.1 Examples**

Statisticians have been slow to realize how frequently combinatorial optimization problems are encountered in mainstream statistical model-fitting efforts. Below we give two examples. In general, when fitting a model requires optimal decisions about the inclusion, exclusion, or arrangement of a number of parameters in a set of possible parameters, combinatorial optimization problems arise frequently.

**Example 3.1 (Genetic Mapping)** Genetic data for individuals and groups of related individuals are often analyzed in ways that present highly complex combinatorial optimization problems. For example, consider the problem of locating genes on a chromosome, known as the genetic mapping problem.

The genes, or more generally genetic markers, of interest in a chromosome can be represented as a sequence of symbols. The position of each symbol along the chromosome is called its _locus_ . The symbols indicate genes or genetic markers, and the particular content stored at a locus is an _allele_ .

Diploid species like humans have pairs of chromosomes and hence two alleles at any locus. An individual is _homozygous_ at a locus if the two alleles are identical at this locus; otherwise the individual is _heterozygous_ . In either case, each parent contributes one allele at each locus of an offspring’s chromosome pair. There are

**62 CHAPTER 3 COMBINATORIAL OPTIMIZATION**


<!-- Start of picture text -->
Parent’s Chromosome Parent’s Contribution<br>to Offspring<br>0 0 0 0 0<br>0 0 0 1 1<br>1 1 1 1 1 Meiosis<br><!-- End of picture text -->

**FIGURE 3.1** During meiosis, a crossover occurs between the third and fourth loci. The zeros and ones indicate the origin of each allele in the contributed chromosome. Only one parental contribution is shown, for simplicity.

two possible contributions from any parent, because the parent has two alleles at the corresponding locus in his/her chromosome pair. Although each parent allele has a 50% chance of being contributed to the offspring, the contributions from a particular parent are not made independently at random. Instead, the contribution by a parent consists of a chromosome built during _meiosis_ from segments of each chromosome in the parent’s pair of chromosomes. These segments will contain several loci. When the source of the alleles on the contributed chromosome changes from one chromosome of the parent’s pair to the other one, a _crossover_ is said to have occurred. Figure 3.1 illustrates a crossover occurring during meiosis, forming the chromosome contributed to the offspring by one parent. This method of contribution means that alleles whose loci are closer together on one of the parent’s chromosomes are more likely to appear together on the chromosome contributed by that parent.

When the alleles at two loci of a parent’s chromosome appear jointly on the contributed chromosome more frequently than would be expected by chance alone, they are said to be _linked_ . When the alleles at two different loci of a parent’s chromosome do not both appear in the contributed chromosome, a _recombination_ has occurred between the loci. The frequency of recombinations determines the degree of linkage between two loci: Infrequent recombination corresponds to strong linkage. The degree of linkage, or _map distance_ , between two loci corresponds to the expected number of crossovers between the two loci.

A genetic map of _p_ markers consists of an ordering of their loci and a list of distances or probabilities of recombination between adjacent loci. Assign to each locus a label, _ℓ_ , for _ℓ_ = 1 _, . . . , p_ . The ordering component of the map, denoted **_θ_** = ( _θ_ 1 _, . . . , θp_ ), describes the arrangement of the _p_ locus labels in order of their positions along the chromosome, with _θj_ = _ℓ_ if the locus labeled _ℓ_ lies at the _j_ th position along the chromosome. Thus, **_θ_** is a permutation of the integers 1 _, . . . , p_ . The other component of a genetic map is a list of distances between adjacent loci. Denote the probability of recombination between adjacent loci _θj_ and _θj_ +1 as _d_ ( _θj, θj_ +1). This amounts to the map distance between these loci. Figure 3.2 illustrates this notation.

Such a map can be estimated by observing the alleles at the _p_ loci for a sample of _n_ chromosomes generated during the meiosis from a parent that is heterozygous at all _p_ loci. Each such chromosome can be represented by a sequence of zeros and ones, indicating the origin of each allele in the contributed parent. For example, the chromosome depicted on the right side of Figure 3.1 can be denoted 00011, because

**3.1 HARD PROBLEMS AND NP-COMPLETENESS 63**


<!-- Start of picture text -->
Position, j 1 2 3 4<br>θ j = θ 1 = 3 θ 2 = 1 θ 3 = 4 θ 4 = 2<br>Locus Label, 3 1 4 2<br>Distance, d( θ j , θ j+1) d(3 , 1) d(1 , 4) d(4 , 2)<br><!-- End of picture text -->

**FIGURE 3.2** Notation for gene mapping example with _p_ = 4 loci. The loci are labeled in boxes at their positions along the chromosome. The correct sequential ordering of loci is defined by the _θj_ values. Distances between loci are given by _d_ ( _θj, θj_ +1) for _j_ = 1 _, . . . ,_ 3.

the first three alleles originate from the first chromosome of the parent and the final two alleles originate from the second chromosome of the parent.

Lettherandomvariable _Xi,θj_ denotetheoriginofthealleleinthelocuslabeled _θj_ forthe _i_ thchromosomegeneratedduringmeiosis.Thedatasetconsistsofobservations, _xi,θj_ , of these random variables. Thus, a recombination for two adjacent markers has been observed in the _i_ th case if �� _xi,θj_ − _xi,θj_ +1 �� = 1, and no recombination has been observed if �� _xi,θj_ − _xi,θj_ +1 �� = 0. If recombination events are assumed to occur independently in each interval, the probability of a given map is


Given an ordering **_θ_** , the MLEs for the recombination probabilities are easily found to be


Given _d_ ( _θj, θj_ +1), the number of recombinations between the loci in positions _j_ and _j_ + 1 is<sup>�</sup><sup>_n_</sup> _i_ =1<sup>|</sup><sup>_Xi,θ_</sup> _j_<sup>−</sup><sup>_Xi,θ_</sup> _j_ +1<sup>|, which has a Bin(</sup><sup>_n, d_(</sup><sup>_θj, θj_+1)) distribution. We can</sup> compute the profile likelihood for **_θ_** by adding the log likelihoods of the _p_ − 1 sets of adjacent loci and replacing each _d_ ( _θj, θj_ +1) by its conditional maximum likelihood estimate _d_<sup>ˆ</sup> ( _θj, θj_ +1). Let **d**<sup>ˆ</sup> ( **_θ_** ) compute these maximum likelihood estimates for any **_θ_** . Then the profile likelihood for **_θ_** is


**64 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

where _T_ ( _θj, θj_ +1) is defined to be zero if _d_<sup>ˆ</sup> ( _θj, θj_ +1) is zero or one. Then the maximum likelihood genetic map is obtained by maximizing (3.3) over all permutations **_θ_** . Note that (3.3) constitutes a sum of terms _T_ ( _θj, θj_ +1) whose values depend on only two loci. Suppose that all possible pairs of loci are enumerated, and the value _T_ ( _i, j_ ) is computed for every _i_ and _j_ where 1 ≤ _i < j_ ≤ _p_ . There are _p_ ( _p_ − 1) _/_ 2 such values of _T_ ( _i, j_ ). The profile log likelihood can then be computed rapidly for any permutation **_θ_** by summing the necessary values of _T_ ( _i, j_ ).

However, finding the maximum likelihood genetic map requires maximizing the profile likelihood by searching over all _p_ ! _/_ 2 possible permutations. This is a variant of the traveling salesman problem, where each genetic marker corresponds to a city and the distance between cities _i_ and _j_ is _T_ ( _i, j_ ). The salesman’s tour may start at any city and terminates in the last city visited. A tour and its reverse are equivalent. There are no known algorithms for solving general traveling salesman problems in polynomial time.

Further details and extensions of this example are considered in [215, 572]. □

**Example 3.2 (Variable Selection in Regression)** Consider a multiple linear regression problem with _p_ potential predictor variables. A fundamental step in regression is selection of a suitable model. Given a dependent variable _Y_ and a set of candidate predictors _x_ 1 _, x_ 2 _, . . . , xp_ , we must find the best model of the form _Y_ = _β_ 0 +<sup>�</sup><sup>_s_</sup> _j_ =1<sup>_βi_</sup> _j_<sup>_xi_</sup> _j_<sup>+</sup><sup>_ϵ_, where {</sup><sup>_i_1</sup><sup>_, . . . , is_} is a subset of {1</sup><sup>_, . . . , p_} and</sup><sup>_ϵ_denotes</sup> a random error. The notion of what model is best may have any of several meanings. Suppose that the goal is to use the Akaike information criterion (AIC) to select the best model [7, 86]. We seek to find the subset of predictors that minimizes the fitted model AIC,


where _N_ is the sample size, _s_ is the number of predictors in the model, and RSS is the sum of squared residuals. Alternatively, suppose that Bayesian regression is performed, say with the normal-gamma conjugate class of priors **_β_** ∼ _N_ ( **_μ_** _, σ_<sup>2</sup> **V** ) and _νλ/σ_<sup>2</sup> ∼ _χν_<sup>2. In this case, one might seek to find the subset of predictors corresponding</sup> to the model that maximizes the posterior model probability [527].

In either case, the variable selection problem requires an optimization over a space of 2<sup>_p_+1</sup> possible models, since each variable and the intercept may be included or omitted. It also requires estimating the best _βij_ for each of the 2<sup>_p_+1</sup> possible models, but this step is easy for any given model. Although a search algorithm that is more efficient than exhaustive search has been developed to optimize some classical regression model selection criteria, it is practical only for fairly small _p_ [213, 465]. We know of no efficient general algorithm to find the global optimum (i.e., the single best model) for either the AIC or the Bayesian goals. □

### **3.1.2 Need for Heuristics**

The existence of such challenging problems requires a new perspective on optimization. It is necessary to abandon algorithms that are guaranteed to find the global

**3.2 LOCAL SEARCH 65**

maximum (under suitable conditions) but will never succeed within a practical time limit. Instead we turn to algorithms that can find a good local maximum within tolerable time.

Such algorithms are sometimes called heuristics. They are intended to find a _globally competitive_ candidate solution (i.e., a nearly optimal one), with an explicit trade of global optimality for speed. The two primary features of such heuristics are

**1.** iterative improvement of a current candidate solution, and

**2.** limitation of the search to a local neighborhood at any particular iteration. These two characteristics embody the heuristic strategy of _local search_ , which we address first.

No single heuristic will work well in all problems. In fact, there is no search algorithm whose performance is better than another when performance is averaged over the set of all possible discrete functions [576, 672]. There is clearly a motivation to adopt different heuristics for different problems. Thus we continue beyond local search to examine _simulated annealing_ , _genetic algorithms_ , and _tabu algorithms_ .

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [3.2 LOCAL SEARCH →](03-3-2-local-search.md)
