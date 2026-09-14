---
title: Backpropagation
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/25_RNNs_Part1.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Backpropagation

**Source:** [`public/lectures/25_RNNs_Part1.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/25_RNNs_Part1.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Efficiently compute gradients of a loss with respect to model parameters

- A neural network is a composition of differentiable functions. For a FF network with _L_ layers:

   - _hℓ_ = _fℓ_ ( _hℓ_ −1; _Wℓ_ ), ℒ= Loss(̂ _y_ , _y_ )

- <sup>To train by gradient descent we need</sup> ∂ _L_ /∂ _Wℓ_ for every layer index _ℓ_

---

[← How do we train an RNN?](17-how-do-we-train-an-rnn.md) · [Up: contents](index.md) · [Backpropagation: Two passes →](19-backpropagation-two-passes.md)
