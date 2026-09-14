---
title: Print total number of weights
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Print total number of weights

**Source:** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

### Question 7 (5 points): parameter counting

Define a small 1D CNN for waveform classification with the architecture below. Then write code that prints the number of *trainable* parameters in each layer and the total.

```
Conv1d(1   -> 16, kernel_size=32, stride=4, padding=16)  -> ReLU -> MaxPool1d(4)
Conv1d(16  -> 32, kernel_size=3,  padding=1)             -> ReLU -> MaxPool1d(4)
Conv1d(32  -> 64, kernel_size=3,  padding=1)             -> ReLU -> AdaptiveAvgPool1d(1)
Linear(64 -> 10)
```

Hint: biases count as parameters. A `Conv1d(in, out, k)` layer has `in*out*k + out` parameters total; `Linear(a, b)` has `a*b + b`.

```python

---

[← Print weight tensor shape](26-print-weight-tensor-shape.md) · [Up: contents](index.md) · [Solution for Q7 →](28-solution-for-q7.md)
