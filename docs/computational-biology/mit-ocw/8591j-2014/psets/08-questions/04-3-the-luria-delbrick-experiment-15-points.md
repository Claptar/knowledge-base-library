---
title: 3 The Luria-Delbrick experiment (15 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/08-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 The Luria-Delbrick experiment (15 points)

**Source:** `psets/08-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Up to now we have focused on evolutionary dynamics, that is, how deterministic process (selection) and stochastic process (genetic drift, clonal interference) act on genetic variation of a population and infuence the outcome of evolution. In this problem, we will look at another important aspect of evolution: mutation. Mutations generate genetic variation in a population and provide the raw materials for selection.

In 1943, Max Delbrick and Salvador E. Luria published a landmark paper<sup>1</sup> for which they were awarded the Nobel Prize. In this paper, they combined experiment and quantitative analysis to address an important question: do genetic mutations arise in the absence of selection, or in response to selction? In their experiment, they created a large collection of replicate cultures of a strain of bacteria E. coli which was not resistant to a phage strain they used. Each bacterial culture was allowed to grow for some generations and then challagend by exposure to the phage. The phage would kill all non-resistant bacteria within a generation time of bacteria. In the end, the number of resistant bacteria that survived the phage challenge was counted for each culture, so they arrived at an empirical distribution of the number of resistant bacteria from many replicate cultures.

The goal of their experiment was to fnd out which of the two competing hypothesis is true: 1) "Mutation": bacterial cells in the culture spontaneously mutated from "sentivie" to "resistant" with a small probability during their growth, even in the absence of phage. 2) "Acquired hereditary

> IS. E. Luria and M. Delbruck. Mutations of bacteria from virus sensitivity to virus resistance. Genetics 28: 491 (1943).

2

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 8

immunity": after encounter of the phage, bacterial cells have a small probability to survive the phage challenge and the acquired resistance can be inheribted by the ofsprings. Luria and Delbruck analyzed the distribution of the number of resistant bacteria in their experiment and showed that the data support the "Mutation" hypothesis. Let's see how this can be done.

a. [6 points] **COMPUTATION** "Mutation" hypothesis. Imagine a set of _C_ cultures (separate fasks) each containing _N_ 0 bacteria cells initially. Assume that all cells in a culture divide at the same time, and that every time a cell divides there is a small probability _α_ = 2 _·_ 10<sup>_−_9</sup> that one of the daughter cells will mutate to become resistant to phage attack. Assume that the initial population has no resistant mutants, and that the progeny of resistant cells are all resistant (no reverse mutation). \e also assume that both the mutant and the wild-type bacteria grow at the same rate (no cost for resistance). For _C_ = 500 cultures, each with _N_ 0 = 200 cells initially, fnd the number of cultures with _m_ resistant mutant cells after _T_ = 21 doublings (generations). Plot a histogram for _m_ . Compute the sample mean and sample variance of the distribution of number of resistant bacteria<sup>2</sup> .

Hint: \hat is the distribution of number of new mutants that appear at generation _k_ , with population size _Nk_ = _N_ 02<sup>_k_</sup> ? You can draw from this distribution at each generation to decide how many mutants are introduced into the population. The brute force approach of simulating the mutation process by generating a random variable for each cell at each generation is not recommended here because it takes too much time for 21 generations. However, if you are determined to try that you might want to use a higher mutation rate _α_ = 2 _·_ 10<sup>_−_7</sup> and stop after _T_ = 15 generations.

- b. [6 points] "Acquired hereditary immunity" hypothesis. Now we assume there is no spontaneous "mutation", instead there is a small probability _β_ that a bacterial cell would acquire resistance after exposure to phage. Starting with _N_ 0 = 200 initially, the bacteria are exposed to phage after _T_ = 21 doublings. \hat is the distribution of the number of resisant bacteria _m_ in this case? Express the distribution in terms of the given paramters.

- c. [3 points] Based on the above analysis, how would you use the empirical distribution of number of resistance bacteria in the Luria-Delbruck experiment to distinguish the two hypothesis?

Feedback (+1 Extra Credit)

> 2The exact distribution, named Luria-Delbruck distribution, was analytically derived in the paper.

3

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 2 COMPUTATION Simulation of clonal interference (20 points)](03-2-computation-simulation-of-clonal-interference-20-points.md) · [Up: contents](index.md)
