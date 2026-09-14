---
title: 3 Coalescent simulation (6.878 only, 10pts)
source: https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/
source_file: sources/ocw-6047/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Coalescent simulation (6.878 only, 10pts)

**Source:** `psets/04-questions.pdf` from [ocw-6047](https://ocw.mit.edu/courses/6-047-computational-biology-fall-2015/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem, we will simulate the coalescent process. Recall this is the time-reverse of the Wright–Fisher process.

- (a) Write a program to simulate the coalescent process on a population of N alleles. Track the times of coalescent events starting from the initial generation until all alleles coalesce to a single ancestor. If we are tracking k lineages, you should report k − 1 coalescent events.

Recall that the Wright–Fisher process assumes each allele in the next generation is sampled independently from all alleles in the current generation. We are now interested in the reverse, so we instead need to sample parents in the previous generation uniformly at random with replacement. Note we are interested in the identities of the parents and not their ancestral alleles.

Run 1,000 trials with a population size of N = 500. Report the mean and standard deviation of the number of generations between coalescent events of k = 2, 3, and 4 lineages.

- (b) Recall the waiting time between coalescent events is approximately exponentially distributed with parameter λ. For each value of k, what is the value of λ given N = 500?

Given this distribution, the mean waiting time and its standard deviation are both 1/λ. How do these expected values compare to your observed values? If your observed values are different, give an explanation of what could have caused the differences.

- (c) Extend your simulator to model sexual reproduction.

Assume a fixed number of females F (and therefore M = N − F males) in each generation and that each chromosome in the next generation is selected in the following way: sample a male and female to mate uniformly at random, then sample one of the two alleles uniformly at random. Your simulation should do the reverse: sample a father and mother and then pick one at random as the ancestor for each allele.

Run 1,000 trials with F = 100 and M = 400. Do your results agree with the coalescent approximation? Justify your answer as in (b).

Can you extend the coalescent approximation to more accurately reflect this model of sexual reproduction? Do your results agree with this new approximation?

3

MIT OpenCourseWare http://ocw.mit.edu

6.047 / 6.878 / HST.507 Computational Biology Fall 2015

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 2 Finding eQTLs (20pts)](03-2-finding-eqtls-20pts.md) · [Up: contents](index.md)
