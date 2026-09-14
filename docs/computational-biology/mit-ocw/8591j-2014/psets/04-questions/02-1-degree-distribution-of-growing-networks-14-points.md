---
title: 1 Degree distribution of growing networks (14 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/04-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Degree distribution of growing networks (14 points)

**Source:** `psets/04-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**COMPUTATION** In this problem, we will perform simulations to explore the degree distribution of growing networks with and without preferential attachment. For the preferential attachment, we assume that the probability Π that a new node will be connected to an existing node _i_ depends on the degree of the existing node _ki_ (i.e. the number of connections to other nodes in the network), in the following manner:


In the simulations, set _α_ = 1 , _m_ 0 = 1 , _m_ = 1 , _t >_ 10<sup>4</sup> . The symbols follow the notations in the scalelfree network paper that we studied in class<sup>1</sup> . (Hint : In this problem, you don't have to keep track of the entire network topology, i.e. which node is connected to which.)

a. For both networks that grow with and without preferential attachment,

   1. Plot a histogram of degrees of all the nodes, on logllinear and logllog scales.

   2. \hat is the mean degree? \hat is the degree of the most connected node?

   3. \hat kind of distribution do you observe?

   4. Estimate the parameters of the observed distributions.

- b. Simulate and plot histograms for _α_ = 2 , _α_ = 0 _._ 5 . How are they diferent from the _α_ = 1 case?

---

[← Problem Set 4](01-problem-set-4.md) · [Up: contents](index.md) · [2 The Feed-Forward Loop (12 points) →](03-2-the-feed-forward-loop-12-points.md)
