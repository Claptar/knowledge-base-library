---
title: PROBLEMS
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/project/givens_hoeting_ch3.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/project/givens_hoeting_ch3.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# PROBLEMS

**Source:** [`project/givens_hoeting_ch3.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/project/givens_hoeting_ch3.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The baseball data introduced in Section 3.3 are available from the website for this book. Problems 3.1–3.4 explore the implications of various algorithm configurations. Treat these problems in the spirit of experiments, trying to identify settings where interesting differences can be observed. Increase the run lengths from those used above to suit the speed of your computer,andlimitthetotalnumberofobjectivefunctionevaluationsineveryrun(effectively the search effort) to a fixed number so that different algorithms and configurations can be compared fairly. Summarize your comparisons and conclusions. Supplement your comments with graphs to illustrate key points.

- **3.1.** Implement a random starts local search algorithm for minimizing the AIC for the baseball salary regression problem. Model your algorithm after Example 3.3.

   - **a.** Change the move strategy from steepest descent to immediate adoption of the first randomly selected downhill neighbor.

   - **b.** Change the algorithm to employ 2-neighborhoods, and compare the results with those of previous runs.

- **3.2.** Implement a tabu algorithm for minimizing the AIC for the baseball salary regression problem. Model your algorithm after Example 3.7.

   - **a.** Compare the effect of using different tabu tenures.

   - **b.** Monitor changes in AIC from one move to the next. Define a new attribute that signals when the AIC change exceeds some value. Allow this attribute to be included on the tabu list, to promote search diversity.

   - **c.** Implement aspiration by influence, overriding the tabu of reversing a low-influence move if a high-influence move is made prior to the reversal. Measure influence with changes in _R_<sup>2</sup> .

**3.5 TABU ALGORITHMS 93**

- **3.3.** Implement simulated annealing for minimizing the AIC for the baseball salary regression problem. Model your algorithm on Example 3.4.

   - **a.** Compare the effects of different cooling schedules (different temperatures and different durations at each temperature).

   - **b.** Compare the effect of a proposal distribution that is discrete uniform over 2-neighborhoods versus one that is discrete uniform over 3-neighborhoods.

- **3.4.** Implement a genetic algorithm for minimizing the AIC for the baseball salary regression problem. Model your algorithm on Example 3.5.

   - **a.** Compare the effects of using different mutation rates.

   - **b.** Compare the effects of using different generation sizes.

   - **c.** Instead of the selection mechanism used in Example 3.5, try the following three mechanisms:

   - **i.** Independent selection of one parent with probability proportional to fitness and the other completely at random

   - **ii.** Independent selection of each parent with probability proportional to fitness

   - **iii.** Tournament selection with _P/_ 5 strata, and/or another number of strata that you prefer

To implement some of these approaches, you may need to scale the fitness function. For example, consider the scaled fitness functions _π_ given by


or


where _a_ and _b_ are chosen so that the mean fitness equals the mean objective function value and the maximum fitness is a user-chosen _c_ times greater than the mean fitness, _f_ is the mean and _s_ is the standard deviation of the unscaled objective function values in the current generation, _z_ is a number generally chosen between 1 and 3, and _v_ is a number slightly larger than 1. Some scalings can sometimes produce negative values for **_ϑ_**<sup>(</sup> _i_<sup>_t_). In such situations, we may apply the transformation</sup>


where _d_<sup>(</sup><sup>_t_)</sup> is the absolute value of the fitness of the worst chromosome in generation _t_ , in the last _k_ generations for some _k_ , or in all preceding generations. Each of these scaling approaches has the capacity to dampen the variation in _f_ , thereby retaining within-generation diversity and increasing the potential to find the global optimum.

Compare and comment on the results for your chosen methods.

- **d.** Apply a steady-state genetic algorithm, with the generation gap _G_ = 1 _/P_ . Compare with the canonical option of distinct, nonoverlapping generations.

**94 CHAPTER 3 COMBINATORIAL OPTIMIZATION**


<!-- Start of picture text -->
12 12<br>6 6<br>1 1<br>1 50 100 1 50 100<br>Individual Individual<br>Locus Locus<br><!-- End of picture text -->

**FIGURE 3.8** Chromosomes for Problem 3.5. Simulated data on 12 loci are available for 100 individuals. For each locus, the source chromosome from the heterozygous parent is encoded in black or white, analogously to Figure 3.1 in Example 3.1. The left panel shows the data arranged according to the true locus ordering, whereas the right panel shows the data arranged by locus label as they would be recorded during data collection.

   - **e.** Implement the following crossover approach, termed _uniform crossover_ [622]: Each locus in the offspring is filled with an allele independently selected at random from the alleles expressed in that position in the parents.

- **3.5.** Consider the genetic mapping example introduced in Example 3.1. Figure 3.8 shows some data for 100 simulated data sequences for a chromosome of length 12. The left panel of this figure shows the data under the true genetic map ordering, and the right panel shows the actual data, with the ordering unknown to the analyst. The data are available from the website for this book.

   - **a.** Apply a random starts local search approach to estimate the genetic map (i.e., the ordering and the genetic distances). Let neighborhoods consist of 20 orderings that differ from the current ordering by randomly swapping the placement of two alleles. Move to the best candidate in the neighborhood, thereby taking a random descent step. Begin with a small number of starts of limited length, to gauge the computational difficulty of the problem; then report the best results you obtained within reasonable limits on the computational burden. Comment on your results, the performance of the algorithm, and ideas for improved search. [Hint: Note that the orderings ( _θj_ 1 _, θj_ 2 _, . . . , θj_ 12 ) and ( _θj_ 12 _, θj_ 11 _, . . . , θj_ 1 ) represent identical chromosomes read from either end.]

   - **b.** Apply an algorithm for random starts local search via steepest descent to estimate the genetic map. Comment on your results and the performance of the algorithm. This problem is computationally demanding and may require a fast computer.

- **3.6.** Consider the genetic mapping data described in Problem 3.5.

   - **a.** Apply a genetic algorithm to estimate the genetic map (i.e., the ordering and the genetic distances). Use the order crossover method. Begin with a small run to gauge the computational difficulty of the problem, then report your results for a run

**3.5 TABU ALGORITHMS 95**

using reasonable limits on the computational burden. Comment on your results, the performance of the algorithm, and ideas for improved search.

   - **b.** Compare the speed of fitness improvements achieved with the order crossover and the edge-recombination crossover strategies.

   - **c.** Attempt any other heuristic search method for these data. Describe your implementation, its speed, and the results.

- **3.7.** The website for this book also includes a second synthetic dataset for a genetic mapping problem. For these data, there are 30 chromosomes. Attempt one or more heuristic search methods for these data. Describe your implementation, the results, and the nature of any problems you encounter. The true ordering used to simulate the data is also given for this dataset. Although the true ordering may not be the MLE, how close is your best ordering to the true ordering? How much larger is this problem than the one examined in the previous problem?

- **3.8.** Thirteen chemical measurements were carried out on each of 178 wines from three regions of Italy [53]. These data are available from the website for this book. Using one or more heuristic search methods from this chapter, partition the wines into three groups for which the total of the within-group sum of squares is minimal. Comment on your work and the results. This is a search problem of size 3<sup>_p_</sup> where _p_ = 178. If you have access to standard cluster analysis routines, check your results using a standard method like that of Hartigan and Wong [317].

---

[← 3.5 TABU ALGORITHMS](06-3-5-tabu-algorithms.md) · [Up: contents](index.md)
