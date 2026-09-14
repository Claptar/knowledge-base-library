---
title: Apply it to a batch of 2 univariate signals of length 10
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf
source_file: sources/berkeley-stat153/spring-2026/public/homework/Homework5.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Apply it to a batch of 2 univariate signals of length 10

**Source:** [`public/homework/Homework5.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Homework5.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

x = torch.randn(2,1,10)# initialize some random data
out = layer(x)# apply convolutional layer
print("input shape: ", tuple(x.shape))# expect (2, 1, 10)
print("output shape:", tuple(out.shape))# expect (2, 4, 8)
print("weight shape:", tuple(layer.weight.shape))# expect (4, 1, 3)
print("n weight params:", layer.weight.numel())# expect 12
```

```
In [ ]:# ---- Predict-then-verify ----

---

[← Stat 153/248 - Homework 5 - YOUR NAME HERE](01-stat-153-248---homework-5---your-name-here.md) · [Up: contents](index.md) · [Before running the lines below, predict →](03-before-running-the-lines-below-predict.md)
