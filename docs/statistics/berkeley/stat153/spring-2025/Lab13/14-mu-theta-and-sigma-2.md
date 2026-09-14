---
title: mu, theta and sigma^2
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab13.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# mu, theta and sigma^2

**Source:** [`Lab13.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(np.column_stack([armod_ARIMA.params, ar1_pars]))
```

```
[[-0.00102183 -0.00127035]
 [-0.39696193 -0.39696154]
 [ 0.27927876  0.27927745]]
```

It is possible to extend these methods to fit AR($p$) and MA($q$) for more general $p$ and $q$ using PyTorch. The PyTorch seems to work just as well as ARIMA. In the above, the PyTorch seems to take much longer time but this is only because we are running the method for a few thousand epochs. The actual convergence seems to have happened much earlier.

---

[← Fit the model](13-fit-the-model.md) · [Up: contents](index.md)
