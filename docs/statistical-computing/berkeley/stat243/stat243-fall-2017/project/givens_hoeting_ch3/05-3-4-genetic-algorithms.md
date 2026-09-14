---
title: 3.4 GENETIC ALGORITHMS
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/project/givens_hoeting_ch3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/project/givens_hoeting_ch3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3.4 GENETIC ALGORITHMS

**Source:** [`project/givens_hoeting_ch3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/project/givens_hoeting_ch3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Annealing is not the only natural process successfully exploited as a metaphor to solve optimization problems. _Genetic algorithms_ mimic the process of Darwinian natural selection. Candidate solutions to a maximization problem are envisioned as biological organisms represented by their genetic code. The fitness of an organism is analogous to the quality of a candidate solution. Breeding among highly fit organisms provides the bestopportunitytopassalongdesirableattributestofuturegenerations,whilebreeding among less fit organisms (and rare genetic mutations) ensures population diversity. Over time, the organisms in the population should evolve to become increasingly fit, thereby providing a set of increasingly good candidate solutions to the optimization problem. The pioneering development of genetic algorithms was done by Holland [333]. Other useful references include [17, 138, 200, 262, 464, 531, 533, 661].

We revert now to our standard description of optimization as maximization, where we seek the maximum of _f_ ( **_θ_** ) with respect to **_θ_** ∈ **_�_** . In statistical applications of genetic algorithms, _f_ is often a joint log profile likelihood function.

### **3.4.1 Definitions and the Canonical Algorithm**

**_3.4.1.1 Basic Definitions_** In Example 3.1 above, some genetics terminology was introduced. Here we discuss additional terminology needed to study genetic algorithms.

In a genetic algorithm, every candidate solution corresponds to an _individual_ , or _organism_ , and every organism is completely described by its genetic code. Individuals are assumed to have one _chromosome_ . A chromosome is a sequence of _C_ symbols, each of which consists of a single choice from a predetermined alphabet. The most basic alphabet is the binary alphabet, {0 _,_ 1}, in which case a chromosome of length _C_ = 9 might look like 100110001. The _C_ elements of the chromosome are the _genes_ . The values that might be stored in a gene (i.e., the elements of the alphabet) are _alleles_ . The position of a gene in the chromosome is its _locus_ .

**76 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

The information encoded in an individual’s chromosome is its _genotype_ . We will represent a chromosome or its genotype as **_ϑ_** . The expression of the genotype in the organism itself is its _phenotype_ . For optimization problems, phenotypes are candidate solutions and genotypes are encodings: Each genotype, **_ϑ_** , encodes a phenotype, **_θ_** , using the chosen allele alphabet.

Geneticalgorithmsareiterative,withiterationsindexedby _t_ .Unlikethemethods previously discussed in this chapter, genetic algorithms track more than one candidate solution simultaneously. Let the _t_ th _generation_ consist of a collection of _P_ organisms, **_ϑ_**<sup>(</sup> 1<sup>_t_)</sup><sup>_, . . . ,_</sup><sup>**_ϑ_**</sup> _P_<sup>(</sup><sup>_t_). This population of size</sup><sup>_P_at generation</sup><sup>_t_corresponds to a collection of</sup> candidate solutions, **_θ_**<sup>(</sup> 1<sup>_t_)</sup><sup>_, . . . ,_</sup><sup>**_θ_**</sup> _P_<sup>(</sup><sup>_t_).</sup>

Darwinian natural selection favors organisms with high _fitness_ . The fitness of an organism **_ϑ_**<sup>(</sup> _i_<sup>_t_)</sup> depends on the corresponding _f_ ( **_θ_**<sup>(</sup> _i_<sup>_t_)).Ahigh-qualitycandidate</sup> solution has a high value of the objective function and a high fitness. As generations progress, organisms inherit from their parents bits of genetic code that are associated with high fitness if fit parents are predominantly selected for breeding. An _offspring_ is a new organism inserted in the ( _t_ + 1)th generation to replace a member of the _t_ th generation; the offspring’s chromosome is determined from those of two _parent_ chromosomes belonging to the _t_ th generation.

To illustrate some of these ideas, consider a regression model selection problem with 9 predictors. Assume that an intercept will be included in any model. The genotype of any model can then be written as a chromosome of length 9. For example, the chromosome **_ϑ_**<sup>(</sup> _i_<sup>_t_)</sup> = 100110001 is a genotype corresponding the phenotype of a model containing only the fitted parameters for the intercept and predictors 1, 4, 5, and 9.

Another genotype is **_ϑ_**<sup>(</sup> _j_<sup>_t_)=110100110.Noticethat</sup><sup>**_ϑ_**</sup> _i_<sup>(</sup><sup>_t_)</sup> and **_ϑ_**<sup>(</sup> _j_<sup>_t_)</sup> share some common genes. A _schema_ is any subcollection of genes. In this example, the two chromosomes share the schema 1*01*****, where * represents a wildcard: The allele in that locus is ignored. (These two chromosomes also share the schemata **<sup>01</sup> *****<sup>, 1</sup> *<sup>01</sup> *<sup>0</sup> ***<sup>, and others.) The significance of schemata is that they encode</sup> modest bits of genetic information that may be transferred as a unit from parent to offspring. If a schema is associated with a phenotypic feature that induces high values of the objective function, then the inheritance of this schema by individuals in future generations promotes optimization.

**_3.4.1.2 Selection Mechanisms and Genetic Operators_** Breeding drives most genetic change. The process by which parents are chosen to produce offspring is called the _selection mechanism_ . One simple approach is to select one parent with probability proportional to fitness and to select the other parent completely at random. Another approach is to select each parent independently with probability proportional to fitness. Section 3.4.2.2 describes some of the most frequently used selection mechanisms.

After two parents from the _t_ th generation have been selected for breeding, their chromosomes are combined in some way that allows schemata from each parent to be inherited by their offspring, who become members of generation _t_ + 1. The methods for producing offspring chromosomes from chosen parent chromosomes are _genetic operators_ .

**77**

**3.4 GENETIC ALGORITHMS**


<!-- Start of picture text -->
Generation Generation<br>t t + 1<br>1 1 0 1 1 0 1 1 0 1 1 0<br>0 1 0 0 1 0 0 1 0 0 1 1<br>1 0 1 1 1 0 1 1 1 1 1 1<br>0 0 0 1 0 1 1 0 0 1 0 0<br>Selection Crossover Mutation<br>Fitness at t<br><!-- End of picture text -->

**FIGURE 3.5** An example of generation production in a genetic algorithm for a population of size _P_ = 4 with chromosomes of length _C_ = 3. Crossovers are illustrated by boxing portions of some chromosomes. Mutation is indicated by an underlined gene in the final column.

A fundamental genetic operator is _crossover_ . One of the simplest crossover methods is to select a random position between two adjacent loci and split both parent chromosomes at this position. Glue the left chromosome segment from one parent to the right segment from the other parent to form an offspring chromosome. The remaining segments can be combined to form a second offspring or discarded. For example, suppose the two parents are 100110001 and 110100110. If the random split point is between the third and fourth loci, then the potential offspring are 100100110 and 110110001. Note that in this example, both offspring inherit the schema 1*01*****. Crossover is the key to a genetic algorithm—it allows good features of two candidate solutions to be combined. Some more complicated crossover operators are discussed in Section 3.4.2.3.

_Mutation_ is another important genetic operator. Mutation changes an offspring chromosome by randomly introducing one or more alleles in loci where those alleles are not seen in the corresponding loci of either parent chromosome. For example, if crossover produced 100100110 from the parents mentioned above, subsequent mutation might yield 101100110. Note that the third gene was 0 in both parents and therefore crossover alone was guaranteed to retain the schema **0******. Mutation, however, provides a way to escape this constraint, thereby promoting search diversification and providing a way to escape from local maxima.

Mutation is usually applied after breeding. In the simplest implementation, each gene has an independent probability, _μ_ , of mutating, and the new allele is chosen completely at random from the genetic alphabet. If _μ_ is too low, many potentially good innovations will be missed; if _μ_ is too high, the algorithm’s ability to learn over time will be degraded, because excessive random variation will disturb the fitness selectivity of parents and the inheritance of desirable schemata.

To summarize, genetic algorithms proceed by producing generations of individuals. The ( _t_ + 1)th generation is produced as follows. First the individuals in generation _t_ are ranked and selected according to fitness. Then crossover and mutation are applied to these selected individuals to produce generation _t_ + 1. Figure 3.5 is a small example of the production of a generation of four individuals with three chromosomes per individual and binary chromosome encoding. In generation _t_ , individual 110 has the highest fitness among its generation and is chosen twice in the

**78 CHAPTER 3 COMBINATORIAL OPTIMIZATION**


<!-- Start of picture text -->
400<br>300<br>200<br>100<br>0 50 100<br>Generation<br>Negative AIC<br><!-- End of picture text -->

**FIGURE 3.6** Results of a genetic algorithm for Example 3.5.

selection stage. In the crossover stage, the selected individuals are paired off so that each pair recombines to generate two new individuals. In the mutation stage, a low mutation rate is applied. In this example, only one mutation occurs. The completion of these steps yields the new generation.

**Example 3.5 (Baseball Salaries, Continued)** The results of applying a simple genetic algorithm to the variable selection problem for the baseball data introduced in Example 3.3 are shown in Figure 3.6. One hundred generations of size _P_ = 20 were used. Binary inclusion–exclusion alleles were used for each possible predictor, yielding chromosomes of length _C_ = 27. The starting generation consisted of purely random individuals. A rank-based fitness function was used; see Equation (3.9). One parent was selected with probability proportional to this fitness; the other parent was selected independently, purely at random. Breeding employed simple crossover. A 1% mutation rate was randomly applied independently to each locus. The horizontal axis in Figure 3.6 corresponds to generation. The AIC values for all 20 individuals in each generation are plotted. The best model found included predictors 2, 3, 6, 8, 10, 13, 14, 15, 16, 24, 25, and 26, yielding an AIC of −418 _._ 95. This matches the best model found using random starts local search (Table 3.2). Darwinian survival of the fittest is clearly illustrated in this figure: The 20 random starting individuals rapidly coalesce into 3 effective subspecies, with the best of these quickly overwhelming the rest and slowly improving thereafter. The best model was first found in generation 60. □

**_3.4.1.3 Allele Alphabets and Genotypic Representation_** The binary alphabet for alleles was introduced in the pioneering work of Holland [333] and continues to be very prevalent in recent research. The theoretical behavior of the algorithm and the relative performance of various genetic operators and other algorithmic variations are better understood for binary chromosomes than for other choices.

**3.4 GENETIC ALGORITHMS 79**

For many optimization problems, it is possible to construct a binary encoding of solutions. For example, consider the univariate optimization of _f_ ( _θ_ ) = 100 − ( _θ_ − 4)<sup>2</sup> on the range _θ_ ∈ [1 _,_ 12 _._ 999] = [ _a_ 1 _, a_ 2]. Suppose that we represent a number in [ _a_ 1 _, a_ 2] as


where _b_ is a binary number of _d_ digits and the decimal() function converts from base 2 to base 10. If _c_ decimal places of accuracy are required, then _d_ must be chosen to satisfy


In our example, 14 binary digits are required for accuracy to 3 decimal places, and _b_ = 01000000000000 maps to _θ_ = 4 _._ 000 using Equation (3.7).

Insomecases,suchastheregressionmodelselectionproblem,abinary-encoded chromosome may be very natural. In others, however, the encoding seems forced, as it does above. For _f_ ( _θ_ ) = 100 − ( _θ_ − 4)<sup>2</sup> , the chromosome _ϑ_ = 01000000000000 ( _θ_ = 4 _._ 000) is optimal. However, chromosomes that are genetically close to this, such as 10000000000000 ( _θ_ = 7 _._ 000) and 00000000000000 ( _θ_ = 1 _._ 000), have phenotypes that are not close to _θ_ = 4 _._ 000. On the other hand, the genotype 00111111111111 has phenotype very close to 4.000 even though the genotype is very different than 01000000000000. Chromosomes that are similar in genotype may have very different phenotypes. Thus, a small mutation may move to a drastically different region of solution space, and a crossover may produce offspring whose phenotypes bear little resemblance to either parent. To resolve such difficulties, a different encoding scheme or modified genetic operators may be required (see Section 3.4.2.3).

Animportantalternativetobinaryrepresentationarisesinpermutationproblems of size _p_ , like the traveling salesman problem. In such cases, a natural chromosome is a permutation of the integers 1 _, . . . , p_ , for example, **_ϑ_** = 752631948 when _p_ = 9. Since such chromosomes must obey the requirement that each integer appear in exactly one locus, some changes to standard genetic operators will be required. Strategies for dealing with permutation chromosomes are discussed in Section 3.4.2.3.

**_3.4.1.4 Initialization, Termination, and Parameter Values_** Genetic algorithms are usually initialized with a first generation of purely random individuals.

The size of the generation, _P_ , affects the speed, convergence behavior, and solution quality of the algorithm. Large values of _P_ are to be preferred, if feasible, because they provide a more diverse genetic pool from which to generate offspring, thereby diversifying the search and discouraging premature convergence. For binary encoding of chromosomes, one suggestion is to choose _P_ to satisfy _C_ ≤ _P_ ≤ 2 _C_ , where _C_ is the chromosome length [8]. For permutation chromosomes, the range 2 _C_ ≤ _P_ ≤ 20 _C_ has been suggested [335]. In most real applications, population sizes haverangedbetween10and200[566],althoughareviewofempiricalstudiessuggests that _P_ can often be as small as 30 [531].

**80 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

Mutation rates are typically very low, in the neighborhood of 1%. Theoretical work and empirical studies have supported a rate of 1 _/C_ [464], and another investigation suggested that the rate should be nearly proportional to 1 _/_ ( _P_ ~~√~~ _C_ ) [571]. Nevertheless, a fixed rate independent of _P_ and _C_ is a common choice.

The termination criterion for a genetic algorithm is frequently just a maximum number of iterations chosen to limit computing time. One might instead consider stopping when the genetic diversity within chromosomes in the current generation is sufficiently low [17].

### **3.4.2 Variations**

In this section we survey a number of methodological variations that may offer improved performance. These include alterations to the fitness function, selection mechanism, genetic operators, and other aspects of the basic algorithm.

**_3.4.2.1 Fitness_** In a canonical genetic algorithm, the fitness of an organism is often taken to be the objective function value of its phenotype, perhaps scaled by the mean objective function value in its generation. It is tempting to simply equate the objective function value _f_ ( **_θ_** ) to the fitness because the fittest individual then corresponds to the maximum likelihood solution. However, directly equating an organism’s fitness to the objective function value for its corresponding phenotype is usually naive in that other choices yield superior optimization performance. Instead, let _φ_ ( **_ϑ_** ) denote the value of a _fitness function_ that describes the fitness of a chromosome. The fitness function will depend on the objective function _f_ , but will not equal it. This increased flexibility can be exploited to enhance search effectiveness.

A problem seen in some applications of genetic algorithms is excessively fast convergence to a poor local optimum. This can occur when a few of the very best individuals dominate the breeding and their offspring saturate subsequent generations. In this case, each subsequent generation consists of genetically similar individuals that lack the genetic diversity needed to produce offspring that might typify other, more profitable regions of solution space. This problem is especially troublesome if it occurs directly after initialization, when nearly all individuals have very low fitness. A few chromosomes that are more fit than the rest can then pull the algorithm to an unfavorable local maximum. This problem is analogous to entrapment near an uncompetitive local maximum, which is also a concern for the other search methods discussed earlier in this chapter.

Selective pressure must be balanced carefully, however, because genetic algorithms can be slow to find a very good optimum. It is therefore important to maintain firm selective pressure without allowing a few individuals to cause premature convergence. To do this, the fitness function can be designed to reduce the impact of large variations in _f_ .

A common approach is to ignore the values of _f_ ( **_θ_**<sup>(</sup> _i_<sup>_t_)) and use only their ranks</sup> [18, 532, 660]. For example, one could set


**3.4 GENETIC ALGORITHMS 81**

where _ri_ is the rank of _f_ ( **_θ_**<sup>(</sup> _i_<sup>_t_)) among generation</sup><sup>_t_. This strategy gives the chromosome</sup> corresponding to the median quality candidate a selection probability of 1 _/P_ , and the best chromosome has probability 2 _/_ ( _P_ + 1), roughly double that for the median. Rank-based methods are attractive in that they retain a key feature of any successful genetic algorithm—selectivity based on relative fitness—while discouraging premature convergence and other difficulties caused by the actual form of _f_ , which can be somewhat arbitrary [660]. Some less common fitness function formulations involving scaling and transforming _f_ are mentioned in [262].

**_3.4.2.2 Selection Mechanisms and Updating Generations_** Previously, in Section 3.4.1.2, we mentioned only simple approaches to selecting parents on the basis of fitness. Selecting parents on the basis of fitness ranks (Section 3.4.2.1) is far more common than using selection probabilities proportional to fitness.

Another common approach is _tournament selection_ [204, 263, 264]. In this approach, the set of chromosomes in generation _t_ is randomly partitioned into _k_ disjoint subsets of equal size (perhaps with a few remaining chromosomes temporarily ignored). The best individual in each group is chosen as a parent. Additional random partitionings are carried out until sufficient parents have been generated. Parents are then paired randomly for breeding. This approach ensures that the best individual will breed _P_ times, the median individual will breed once on average, and the worst individual will not breed at all. The approaches of proportional selection, ranking, and tournament selection apply increasing selective pressure, in that order. Higher selective pressure is generally associated with superior performance, as long as premature entrapment in local optima can be avoided [17].

Populations can be partially updated. The _generation gap_ , _G_ , is a proportion of the generation to be replaced by generated offspring [146]. Thus, _G_ = 1 corresponds to a canonical genetic algorithm with distinct, nonoverlapping generations. At the other extreme, _G_ = 1 _/P_ corresponds to incremental updating of the population one offspringatatime.Inthiscase,a _steady-state_ geneticalgorithmproducesoneoffspring at a time to replace the least fit (or some random relatively unfit) individual [661]. Such a process typically exhibits more variance and higher selective pressure than a standard approach.

When _G <_ 1, performance can sometimes be enhanced with a selection mechanism that departs somewhat from the Darwinian analogy. For example, an _elitist_ strategy would place an exact copy of the current fittest individual in the next generation, thereby ensuring the survival of the best current solution [146]. When _G_ = 1 _/P_ , each offspring could replace a chromosome randomly selected from those with belowaverage fitness [5].

Deterministic selection strategies have been proposed to eliminate sampling variability [19, 464]. We see no compelling need to eliminate the randomness inherent in the selection mechanism.

One important consideration when generating or updating a population is whether to allow duplicate individuals in the population. Dealing with duplicate individuals wastes computing resources, and it potentially distorts the parent selection criterion by giving duplicated chromosomes more chances to produce offspring [138].

**82 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

**_3.4.2.3 Genetic Operators and Permutation Chromosomes_** To increase genetic mixing, it is possible to choose more than one crossover point. If two crossover points are chosen, the gene sequence between them can be swapped between parents to create offspring. Such multipoint crossover can improve performance [54, 187].

Many other approaches for transferring genes from parents to offspring have been suggested. For example, each offspring gene could be filled with an allele randomly selected from the alleles expressed in that position in the parents. In this case, the parental origins of adjacent genes could be independent [4, 622] or correlated [602], with strength of correlation controlling the degree to which offspring resemble a single parent.

In some problems, a different allele alphabet may be more reasonable. Allele alphabets with many more than two elements have been investigated [13, 138, 524, 534]. For some problems, genetic algorithms using a floating-point alphabet have outperformed algorithms using the binary alphabet [138, 346, 463]. Methods known as messy genetic algorithms employ variable-length encoding with genetic operators that adapt to changing length [265–267]. Gray coding is another alternative encoding that is particularly useful for real-valued objective functions that have a bounded number of optima [662].

When a nonbinary allele alphabet is adopted, modifications to other aspects of the genetic algorithm, particularly to the genetic operators, is often necessary and even fruitful. Nowhere is this more evident than when permutation chromosomes are used. Recall that Section 3.4.1.3 introduced a special chromosome encoding for permutation optimization problems. For such problems (like the traveling salesman problem), it is natural to write a chromosome as a permutation of the integers 1 _, . . . , n_ . New genetic operators are needed then to ensure that each generation contains only valid permutation chromosomes.

For example, let _p_ = 9, and consider the crossover operator. From two parent chromosomes 752631948 and 912386754 and a crossover point between the second and third loci, standard crossover would produce offspring 752386754 and 912631948. Both of these are invalid permutation chromosomes, because both contain some duplicate alleles.

A remedy is _order crossover_ [623]. A random collection of loci is chosen, and the order in which the alleles in these loci appear in one parent is imposed on the same alleles in the other parent to produce one offspring. The roles of the parents can be switched to produce a second offspring. This operator attempts to respect relative positions of alleles. For example, consider the parents 752631948 and 912386754, and suppose that the fourth, sixth, and seventh loci are randomly chosen. In the first parent, the alleles in these loci are 6, 1, and 9. We must rearrange the 6, 1, and 9 alleles in the second parent to impose this order. The remaining alleles in the second parent are **238*754. Inserting 6, 1, and 9 in this order yields 612389754 as the offspring. Reversing the roles of the parents yields a second offspring 352671948.

Many other crossover operators for permutation chromosomes have been proposed[135,136,138,268,464,492,587].Mostarefocusedonthepositionsofindividual genes. However, for problems like the traveling salesman problem, such operators have the undesirable tendency to destroy links between cities in the parent tours. The

**3.4 GENETIC ALGORITHMS 83**

**TABLE 3.3** Edge tables showing the cities linked to or from each allele in either parent for each of the first three steps of edge recombination crossover. Beneath each column is the offspring chromosome resulting from each step.

||Step 1|S|tep 2|Step 3|
|---|---|---|---|---|
|City|Links|City|Links|City<br>Links|
|1|3, 9, 2|1|3, 2|1<br>3, 2|
|2|5, 6, 1, 3|2|5, 6, 1, 3|2<br>5, 6, 1, 3|
|3|6, 1, 2, 8|3|6, 1, 2, 8|3<br>6, 1, 2, 8|
|4|9, 8, 5|4|8, 5|4<br>Used|
|5|7, 2, 4|5|7, 2, 4|5<br>7, 2|
|6|2, 3, 8, 7|6|2, 3, 8, 7|6<br>2, 3, 8, 7|
|7|8, 5, 6|7|8, 5, 6|7<br>8, 5, 6|
|8|4, 7, 3, 6|8|4, 7, 3, 6|8<br>7, 3, 6|
|9|1, 4|9|Used|9<br>Used|
||**9**********|**94***|**********|**945********|


desirability of a candidate solution is a direct function of these links. Breaking links is effectively an unintentional source of mutation. _Edge-recombination crossover_ has been proposed to produce offspring that contain only links present in at least one parent [663, 664].

We use the traveling salesman problem to explain edge-recombination crossover. The operator proceeds through the following steps.

**1.** We first construct an edge table that stores all the links that lead into and out of each city in either parent. For our two parents, 752631948 and 912386754, the result is shown in the leftmost portion of Table 3.3. Note that the number of links into and out of each city in either parent will always be at least two and no more than four. Also, recall that a tour returns to its starting city, so, for example, the first parent justifies listing 7 as a link from 8.

**2.** To begin creating an offspring, we choose between the initial cities of the two parents. In our example, the choices are cities 7 and 9. If the parents’ initial cities have the same number of links, then the choice is made randomly. Otherwise, choose the initial city from the parent whose initial city has fewer links. In our example, this yields 9********.

**3.** We must now link onward from allele 9. From the leftmost column of the edge table, we find that allele 9 has two links: 1 and 4. We want to chose between these by selecting the city with the fewest links. To do this, we first update the edge table by deleting all references to allele 9, yielding the center portion of Table 3.3. Since cities 1 and 4 both have two remaining links, we choose randomly between 1 and 4. If 4 is the choice, then the offspring is updated to 94*******.

**4.** There are two possible links onward from city 4: cities 5 and 8. Updating the edge table to produce the rightmost portion of Table 3.3, we find that city 5 has

**84 CHAPTER 3 COMBINATORIAL OPTIMIZATION**

the fewest remaining links. Therefore, we choose city 5. The partial offspring is now 945******.

Continuing this process might yield the offspring 945786312 by the following steps: select 7; select 8; select 6; randomly select 3 from the choices of 2 and 3; randomly select 1 from the choices of 1 and 2; select 2.

Note that in each step a city is chosen among those with the fewest links. If, instead, links were chosen uniformly at random, cities would be more likely to be left without a continuing edge. Since tours are circuital, the preference for a city with few links does not introduce any sort of bias in offspring generation.

An alternative _edge assembly_ strategy has been found to be extremely effective in some problems [477].

Mutation of permutation chromosomes is not as difficult as crossover. A simple mutation operator is to randomly exchange two genes in the chromosome [531]. Alternatively, the elements in a short random segment of the chromosome can be randomly permuted [138].

### **3.4.3 Initialization and Parameter Values**

Although traditionally a genetic algorithm is initiated with a generation of purely random individuals, heuristic approaches to constructing individuals with good or diverse fitness have been suggested as an improvement on random starts [138, 531].

Equal sizes for subsequent generations are not required. Population fitness usually improves very rapidly during the early generations of a genetic algorithm. In order to discourage premature convergence and promote search diversity, it may be desirable to use a somewhat large generation size _P_ for early generations. If _P_ is fixed at too large a value, however, the entire algorithm may be too slow for practical use. Once the algorithm has made significant progress toward the optimum, important improving moves most often come from high-quality individuals; low-quality individuals are increasingly marginalized. Therefore, it has been suggested that _P_ may be decreased progressively as iterations continue [677]. However, rank-based selection mechanisms are more commonly employed as an effective way to slow convergence.

It can be also useful to allow a variable mutation rate that is inversely proportional to the population diversity [531]. This provides a stimulus to promote search diversity as generations become less diverse. Several authors suggest other methods for allowing the probabilities of mutation and crossover and other parameters of the genetic algorithm to vary adaptively over time in manners that may encourage search diversity [54, 137, 138, 464].

### **3.4.4 Convergence**

The convergence properties of genetic algorithms are beyond the scope of this chapter, but several important ideas are worth mentioning.

Much of the early analysis about why genetic algorithms work was based on the notion of schemata [262, 333]. Such work is based on a canonical genetic algorithm with binary chromosome encoding, selection of each parent with probability proportional to fitness, simple crossover applied every time parents are paired, and mutation

**3.5 TABU ALGORITHMS 85**

randomly applied to each gene independently with probability _μ_ . For this setting, the _schema theorem_ provides a lower bound on the expected number of instances of a schema in generation _t_ + 1, given that it was present in generation _t_ .

The schema theorem shows that a short, low-order schema (i.e., one specifying only a few nearby alleles) will enjoy increased expected representation in the next generation if the average fitness of chromosomes containing that schema in the generation at time _t_ exceeds the average fitness of all chromosomes in the generation. A longer and/or more complex schema will require higher relative fitness to have the same expectation. Proponents of schema theory argue that convergence to globally competitive candidate solutions can be explained by how genetic algorithms simultaneously juxtapose many short low-order schemata of potentially high fitness, thereby promoting propagation of advantageous schemata.

More recently, the schema theorem and convergence arguments based upon it have become more controversial. Traditional emphasis on the number of instances of a schema that propagate to the next generation and on the average fitness of chromosomes containing that schema is somewhat misguided. What matters far more is which particular chromosomes containing that schema are propagated. Further, the schema theorem overemphasizes the importance of schemata: in fact it applies equally well to any arbitrary subsets of **_�_** . Finally, the notion that genetic algorithms succeed because they implicitly simultaneously allocate search effort to many schemata-defined regions of **_�_** has been substantially discredited [647]. An authoritative exposition of the mathematical theory of genetic algorithms is given by Vose [646]. Other helpful treatments include [200, 533].

Genetic algorithms are not the only optimization strategy that can be motivated by analogy to a complex biological system. For example, _particle swarm_ optimization also creates and updates a population of candidate solutions [372, 373, 594]. The locations of these solutions within the search space evolve through simple rules that can be viewed as reflecting cooperation and competition between individuals analogous to the movement of birds in a flock. Over a sequence of iterations, each individual adjusts its location (i.e., candidate solution) based on its own flying experience and those of its companions.

---

[← 3.3 SIMULATED ANNEALING](04-3-3-simulated-annealing.md) · [Up: contents](index.md) · [3.5 TABU ALGORITHMS →](06-3-5-tabu-algorithms.md)
