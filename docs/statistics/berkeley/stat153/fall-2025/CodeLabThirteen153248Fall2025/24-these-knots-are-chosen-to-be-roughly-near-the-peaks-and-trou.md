---
title: these knots are chosen to be roughly near the peaks and troughs
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# these knots are chosen to be roughly near the peaks and troughs

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

X = np.column_stack([np.ones(m), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float))*(x_scaled-knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(np.log(pgram), X).fit()

#print(md_init.summary())
#print(md_init.params)
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.69774938 -1.64924225 -1.61112951 -1.57301677 -1.53490403 -1.49679129
 -1.45521375 -1.38591786]
[ 207.99767796  121.68086542 -237.90477858  200.25534348 -231.28621121
  208.44914151 -136.58094635   94.09095751  -50.99202009   31.30034846]
```

```python
#y_torch = torch.tensor(pgram/np.std(pgram), dtype = torch.float32).unsqueeze(1)
y_torch = torch.tensor(pgram, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)

md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.001)

for epoch in range(20000):
    optimizer.zero_grad()

    y_pred = md_PiecewiseLinear(x_torch)
    #loss = loss_fn(y_pred, y_torch)
    loss = torch.sum( y_pred + y_torch * torch.exp(- y_pred) )

    loss.backward() # calulates gradients

    optimizer.step() # updates parameters using gradients

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

---

[← Find peaks](23-find-peaks.md) · [Up: contents](index.md) · [Run this code a few times to be sure of convergence. →](25-run-this-code-a-few-times-to-be-sure-of-convergence.md)
