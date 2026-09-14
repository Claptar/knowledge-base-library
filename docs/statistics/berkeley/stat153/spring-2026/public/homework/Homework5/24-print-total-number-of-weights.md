---
title: Print total number of weights
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Print total number of weights

**Source:** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```

### Question 7 (5 points): parameter counting

Define a small 1D CNN for waveform classification with the architecture below. Then write code that prints the number of trainable parameters in each layer and the total.

```
Conv1d(1   -> 16, kernel_size=32, stride=4, padding=16)  ->
ReLU -> MaxPool1d(4)
Conv1d(16  -> 32, kernel_size=3,  padding=1)             ->
ReLU -> MaxPool1d(4)
Conv1d(32  -> 64, kernel_size=3,  padding=1)             ->
ReLU -> AdaptiveAvgPool1d(1)
Linear(64 -> 10)
```

Hint: biases count as parameters. A <mark>`Conv1d(in, out, k)`</mark> layer has <mark>`in*out*k + out`</mark> parameters total; <mark>`Linear(a, b)`</mark> has <mark>`a*b + b` .</mark>

```
In [ ]:# Solution for Q7
model = nn.Sequential(
    nn.Conv1d(##FILLIN),
    nn.ReLU(##FILLIN),
    nn.MaxPool1d(##FILLIN),
## ADD The OTHER LAYERS HERE
)
total =0
for name, p in model.named_parameters():
if p.requires_grad:
        print(f"{name:20s} {tuple(p.shape)!s:20s} {p.numel():>6d}")
        total += p.numel()
print(f"{'total':20s} {'':20s} {total:>6d}")

---

[← Print weight tensor shape](23-print-weight-tensor-shape.md) · [Up: contents](index.md) · [Expected (by hand) →](25-expected-by-hand.md)
