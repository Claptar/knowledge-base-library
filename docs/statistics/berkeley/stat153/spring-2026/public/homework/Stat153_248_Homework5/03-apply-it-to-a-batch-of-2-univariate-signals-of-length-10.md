---
title: Apply it to a batch of 2 univariate signals of length 10
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_248_Homework5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Apply it to a batch of 2 univariate signals of length 10

**Source:** [`public/homework/Stat153_248_Homework5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_248_Homework5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

x = torch.randn(2, 1, 10) # initialize some random data
out = layer(x) # apply convolutional layer

print("input shape: ", tuple(x.shape))        # expect (2, 1, 10)
print("output shape:", tuple(out.shape))      # expect (2, 4, 8)
print("weight shape:", tuple(layer.weight.shape))  # expect (4, 1, 3)
print("n weight params:", layer.weight.numel())    # expect 12
```

```python

---

[← Build the layer from the worked example](02-build-the-layer-from-the-worked-example.md) · [Up: contents](index.md) · [---- Predict-then-verify ---- →](04------predict-then-verify.md)
