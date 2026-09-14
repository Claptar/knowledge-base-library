---
title: 2 Adaptation in a Sharply Peaked Fitness Landscape (10 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/09-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Adaptation in a Sharply Peaked Fitness Landscape (10 points)

**Source:** `psets/09-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You will use the quasispecies equation to explore adaptation in a sharply peaked ftness landscape. In this simple model, you will fnd that there exists a critical mutation rate _uc_ such that if the mutation rate _µ_ of the population is larger than _µc_ then the fttest sequence cannot be maintained in the population.

Consider a species with a genome of length _L_ and the mutation rate per nucleotide _µ_ . The probability that a sequence replicates itself without any mutations is _q_ = (1 _− µ_ )<sup>_L_</sup> . Our sharply peaked ftness landscape will be constructed as follows: there is a single ft sequence (the master sequence), _xM_ , that has ftness _r >_ 1 , and all other sequences have ftness 1 . \e will group all the other sequences together into a single variable called _xO_ . Assume that at time _t_ = 0 the population only consists of ft individuals ( _xM_ = 1 ). The approximate quasispecies equation reads:


- a. Some terms have been neglected to acquire the approximate quasispecies equation. Explain what these terms are and why it is reasonable to neglect them.

- b. Use the equations above to show that in order to maintain the fttest sequence, _rq_ should be larger than 1 .

- c. Assume that the ftness advantage of the master sequence is neither too large nor too small, so that _log_ ( _r_ ) _≈_ 1 . Show that this means that _µc ≈ L_ <u>1</u> .

---

[← 1 Quasispecies Equation (12 points)](02-1-quasispecies-equation-12-points.md) · [Up: contents](index.md) · [3 Repeated Prisoner's Dilemma (12 points) →](04-3-repeated-prisoner-s-dilemma-12-points.md)
