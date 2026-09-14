---
title: Solution for Q7
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Solution for Q7

**Source:** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

model = nn.Sequential(
    nn.Conv1d(##FILLIN),
    nn.ReLU(##FILLIN),
    nn.MaxPool1d(##FILLIN),
    ## ADD The OTHER LAYERS HERE
)

total = 0
for name, p in model.named_parameters():
    if p.requires_grad:
        print(f"{name:20s} {tuple(p.shape)!s:20s} {p.numel():>6d}")
        total += p.numel()
print(f"{'total':20s} {'':20s} {total:>6d}")

---

[← Print total number of weights](27-print-total-number-of-weights.md) · [Up: contents](index.md) · [Expected (by hand) →](29-expected-by-hand.md)
