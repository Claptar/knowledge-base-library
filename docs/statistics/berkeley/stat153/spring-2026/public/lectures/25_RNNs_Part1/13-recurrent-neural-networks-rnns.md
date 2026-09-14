---
title: Recurrent neural networks (RNNs)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/25_RNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Recurrent neural networks (RNNs)

**Source:** [`public/lectures/25_RNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Only process one input at a time (unlike feed-forward and convolutional networks)

   - This reduces the number of weights by a lot (efficient!)

- But contain **memory** of previous inputs (stored in the hidden state)

   - Allows RNNs to capture dependencies across time

---

[← Recurrence vs. “feed-forward”](12-recurrence-vs-feed-forward.md) · [Up: contents](index.md) · [Recurrent neural networks (RNNs) →](14-recurrent-neural-networks-rnns.md)
