---
title: Receptive field
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Receptive field

The **receptive field** of an output unit is the number of input positions that unit depends on. It is a property of the architecture and does not change with input length.

For a single conv layer with kernel size $k$, each output unit sees $k$ consecutive input positions, so the receptive field is $k$.

When you stack conv layers, the receptive field grows. Let's consider two 1D conv layers, each with kernel size $k = 3$:

* One unit in layer 2 sees 3 consecutive units in layer 1.
* Each of those 3 layer-1 units sees 3 consecutive units in the input.
* The leftmost layer-1 unit covers input positions $0, 1, 2$. The rightmost covers $2, 3, 4$.
* So a single layer-2 unit depends on input positions $0$ through $4$ — a receptive field of 5.

In general, for $n$ stacked conv layers with kernel size $k$ (stride 1):

$$\text{RF}_n = n(k - 1) + 1.$$

Two 3×3 layers $\to$ RF = 5. Three 3×3 layers $\to$ RF = 7. This is why deep networks built from small kernels can still cover large input regions: receptive field grows linearly with depth. On the left, we have 3 1D conv layers with kernel size $k = 3$, on the right, 3 1D conv layers with kernel size $k = 5$:

Note that receptive field is **different from output length**. Output length tells you how many positions remain after the convolutions; receptive field tells you, for one of those output positions, how many input positions contributed to it. Both involve $(k - 1)$ terms but they answer different questions.

```python
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
```

```python
torch.manual_seed(0)
np.random.seed(0)
```

---

[← Collaborated with](01-collaborated-with.md) · [Up: contents](index.md) · [Part 0: Warm-up →](03-part-0-warm-up.md)
