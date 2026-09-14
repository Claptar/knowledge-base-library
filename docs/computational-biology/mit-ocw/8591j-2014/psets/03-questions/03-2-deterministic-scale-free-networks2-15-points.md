---
title: 2 Deterministic scale-free networks2 (15 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Deterministic scale-free networks2 (15 points)

**Source:** `psets/03-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In this problem you will study the degree distribution and clustering properties of deterministic scale-free networks. Consider the following procedure of generating a deterministic network:

- _t_ = _−_ 1 Start from a single edge connecting two nodes.

- _t_ = 0 Add one more node, and connect it to the two existing nodes.

- _t_ = _n_ For every edge of the graph add a new node and connect it to the nodes of the corresponding edge.


© American Physical Society. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

- a. Are preferential attachment and/or growth incorporated into this model?

- b. How many nodes are added at _t_ = _n_ ? \hat are the degrees _k_ of these nodes?

- c. How does the degree _k_ of the node change over time?

- d. The clustering coefcient of the node<sup>3</sup> _C_ depends on the degree of the node in a scale-free manner: _C_ ( _k_ ) ' _k_<sup>_−β_</sup> . Find _β_ by deriving the rule of how the clustering coefcient of the node changes over time and using the result of part (c).

> ITsai et al. Robust, Tunable Biological Oscillations from Interlinked Positive and Negative Feedback Loops. Science, 321, 126-129 (2008)

> 2SN Dorogovtsev et al. Pseudofractal scale-free web. Physical Review E, 65, 066122 (2002)

> 3The defnition of the clustering coefcient can be found on p.259 of Alon's book.

3

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 3

- e. One can design a scale-free network with _β_ = 0 . \hich properties of the network discussed in this problem make _β_ nonzero?

- f. \hile _k_ in this problem can only have discrete values, for this part of the problem we will work in the continuous limit. Thus, the probability that a given node has degree _k ∈_ [ _k_ 0 _, k_ 0 + _δ_ ( _k_ 0)] can be written as

_P_ ( _k_ 0 _≤ k < k_ 0 + _δ_ ( _k_ 0)) = _ρ_ ( _k_ 0) _δ_ ( _k_ 0)

where probability density of the degree distribution of the nodes, _ρ_ ( _k_ ) , is proportional to _k_<sup>_−γ_</sup> . Find _γ_ by counting the number of nodes with the degree _k_ . (Hint : don't forget that _δ_ is a function of _k_ .) Does _γ_ depend on time?

---

[← 1 Circadian Clocks (30 points)](02-1-circadian-clocks-30-points.md) · [Up: contents](index.md) · [3 Network Motifs in Transcription Networks (5 points) →](04-3-network-motifs-in-transcription-networks-5-points.md)
