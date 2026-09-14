---
title: 4 Stochastic Simulations of the Error Threshold (17 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/09-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Stochastic Simulations of the Error Threshold (17 points)

**Source:** `psets/09-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, you will perform stochastic simulations to demonstrate the error threshold concept in fnite populations. Let's consider a population of _N_ individuals, each having a genome of length _L_ . Each position of the genome can be in either of the two states: 0 or 1 . Every time an individual reproduces, at each position a mutation from 0 to 1 or from 1 to 0 can occur with probability _µ_ . The ftness of a particular sequence is

> 3R Axelrod and WD Hamilton. The evolution of cooperation. Science 211: 1390-1396 (1981)

3

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 9


where _s_ 0 is a constant and _gl_ is the state of the position _l_ in the genome (either 0 or 1 ).

- a. [1 point] For _s_ 0 = 0 , what is the steady state distribution of the number of mutations in a given genome? \hat is the mean?

- b. [2 points] \hat is the condition on _N_ , _L_ and _s_ 0 that makes all the mutations non­neutral? \hy is it important that mutations are not neutral?

- c. [4 points] **COMPUTATION** For _N_ = 50 , _L_ = 10 and _s_ 0 = 1 , perform stochastic simulations (Moran process) with various mutation rates ( 0 _._ 005 , 0 _._ 05 , 0 _._ 2 , 0 _._ 5 mutations per position per generation). �emember that after a benefcial mutation has been acquired, the reverse mutation may occur. Plot several trajectories of the mean ftness of the population. Make sure that the trajectories approach a steady state.

- d. [2 points] Is the error threshold located in the regime of clonal interference?

- e. [3 points] For the mutation rates higher than the error threshold, what is the steady state ftness mean? \ith the decrease of the mutation rate, how do you expect the steady state mean ftness to change?

Now, consider another ftness function


- f. [2 points] \here are the two ftness peaks located?

- g. [3 points] **COMPUTATION** Start the simulations at the highest peak. Use the mutation rates of 0 _._ 05 _,_ 0 _._ 075 and 0 _._ 1 per position per generation and run the simulation for 10000 replications. Plot the average amount of the mutations in the population as a function of time. Interpret the results.

---

[← 3 Repeated Prisoner's Dilemma (12 points)](04-3-repeated-prisoner-s-dilemma-12-points.md) · [Up: contents](index.md) · [5 Conditioned Response vs. Direct Response: Anticipation of Sugars in E. coli (19 points) →](06-5-conditioned-response-vs-direct-response-anticipation-of-su.md)
