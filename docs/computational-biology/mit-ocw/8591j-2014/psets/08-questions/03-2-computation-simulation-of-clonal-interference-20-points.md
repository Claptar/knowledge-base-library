---
title: 2 COMPUTATION Simulation of clonal interference (20 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/08-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 COMPUTATION Simulation of clonal interference (20 points)

**Source:** `psets/08-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The simulations in this problem take a long time to run Please plan accordingl.

Consider a population of size _N_ subject to benefcial mutations that are distributed exponentially with a characteristic magnitude of _s_ 0 = 0 _._ 01 .

- a. [8 points] Simulate Moran process with a single mutant starting in the population. In each run, the selective advantage of this mutant should be sampled from an exponential distribution. For _N_ = 10 and _N_ = 1000 , draw a histogram of the selective advantage of mutants that eventually take over the population, and compare it with your analytical estimation in the previous problem.

- b. [8 points] \hen there are multiple mutants competing at the same time, we encounter clonal interference. Now include clonal interference by allowing a probability _µ_ (the mutation rate) of generating a new benefcial mutation. For simplicity, we do not allow mutants to acquire secondary benefcial mutations. Each time when a non-mutant is chosen to divide, there is a probability _µ_ that the daughter cell will gain a benefcial mutation sampled from the exponential distribution. For _N_ = 10 and _N_ = 1000 , draw histograms of the selective advantage of mutants that eventually take over the population with _µ_ = 10<sup>_−_5</sup> , 10<sup>_−_4</sup> , 10<sup>_−_3</sup> , and 10<sup>_−_2</sup> .

- c. [4 points] How is the distribution of fxed benefcial mutations changed in the presence of clonal interference? At what regime is the distribution in part a still a good approximation?

---

[← 1 Evolution in Finite Populations (15 points)](02-1-evolution-in-finite-populations-15-points.md) · [Up: contents](index.md) · [3 The Luria-Delbrick experiment (15 points) →](04-3-the-luria-delbrick-experiment-15-points.md)
