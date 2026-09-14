---
title: Plot the function
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the function

**Source:** [`CodeLectureTwentyFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(x_vals, y_vals)
plt.title(r'$g(x) = \frac{2x}{1 + 0.8x^2}$')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We will fit the model (below $x_t = y_{t-1}$)
\begin{equation*}
  \mu_t = \beta_0 + \beta_1 x_t + \beta_2 (x_t - c_1)_+ + \dots +
  \beta_{k+1} (x_t - c_k)_+.
\end{equation*}
This model is represented by the following class (this is the same function as the piecewise linear trend model).

```python
class PiecewiseLinearModel(nn.Module):
    def __init__(self, knots_init, beta_init):
        super().__init__()
        self.num_knots = len(knots_init)
        self.beta = nn.Parameter(torch.tensor(beta_init, dtype=torch.float32))
        self.knots = nn.Parameter(torch.tensor(knots_init, dtype=torch.float32))

    def forward(self, x):
        knots_sorted, _ = torch.sort(self.knots)
        out = self.beta[0] + self.beta[1] * x
        for j in range(self.num_knots):
            out += self.beta[j + 2] * torch.relu(x - knots_sorted[j])
        return out
```

We create tensors for $x$ and $y$ below.

```python
y_reg = y_sim[1:]
x_reg = y_sim[0:(n-1)]

y_torch = torch.tensor(y_reg, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_reg, dtype = torch.float32).unsqueeze(1)
```

Below we find initial values for $c_1, \dots, c_k$ and $\beta_0, \beta_1, \dots, \beta_{k+1}$.

```python
k = 6
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_reg, quantile_levels)

n_reg = len(y_reg)
X = np.column_stack([np.ones(n_reg), x_reg])
for j in range(k):
    xc = ((x_reg > knots_init[j]).astype(float))*(x_reg - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(y_reg, X).fit()
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.54280223 -1.02805822 -0.60360061 -0.09440788  0.61283012  1.2719812 ]
[-2.31279716 -0.66056549  0.83205759  0.42017211  0.77300214  0.83540066
 -2.59891684  0.37725608]
```

Below we fit the model and estimate parameters.

```python
nar = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
optimizer = optim.Adam(nar.parameters(), lr = 0.01)
loss_fn = nn.MSELoss()

for epoch in range(10000):
    optimizer.zero_grad()
    y_pred = nar(x_torch)
    loss = loss_fn(y_pred, y_torch)
    loss.backward()
    optimizer.step()
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
#Run this code a few times to be sure of convergence.
```

```
Epoch 0, Loss: 0.3186
Epoch 100, Loss: 0.3166
Epoch 200, Loss: 0.3163
Epoch 300, Loss: 0.3162
Epoch 400, Loss: 0.3161
Epoch 500, Loss: 0.3161
Epoch 600, Loss: 0.3161
Epoch 700, Loss: 0.3161
Epoch 800, Loss: 0.3161
Epoch 900, Loss: 0.3161
Epoch 1000, Loss: 0.3161
Epoch 1100, Loss: 0.3161
Epoch 1200, Loss: 0.3161
Epoch 1300, Loss: 0.3161
Epoch 1400, Loss: 0.3161
Epoch 1500, Loss: 0.3161
Epoch 1600, Loss: 0.3161
Epoch 1700, Loss: 0.3161
Epoch 1800, Loss: 0.3161
Epoch 1900, Loss: 0.3161
Epoch 2000, Loss: 0.3161
Epoch 2100, Loss: 0.3161
Epoch 2200, Loss: 0.3161
Epoch 2300, Loss: 0.3161
Epoch 2400, Loss: 0.3161
Epoch 2500, Loss: 0.3161
Epoch 2600, Loss: 0.3161
Epoch 2700, Loss: 0.3161
Epoch 2800, Loss: 0.3161
Epoch 2900, Loss: 0.3161
Epoch 3000, Loss: 0.3161
Epoch 3100, Loss: 0.3161
Epoch 3200, Loss: 0.3161
Epoch 3300, Loss: 0.3161
Epoch 3400, Loss: 0.3161
Epoch 3500, Loss: 0.3161
Epoch 3600, Loss: 0.3161
Epoch 3700, Loss: 0.3161
Epoch 3800, Loss: 0.3161
Epoch 3900, Loss: 0.3161
Epoch 4000, Loss: 0.3161
Epoch 4100, Loss: 0.3161
Epoch 4200, Loss: 0.3161
Epoch 4300, Loss: 0.3161
Epoch 4400, Loss: 0.3161
Epoch 4500, Loss: 0.3161
Epoch 4600, Loss: 0.3161
Epoch 4700, Loss: 0.3161
Epoch 4800, Loss: 0.3161
Epoch 4900, Loss: 0.3161
Epoch 5000, Loss: 0.3161
Epoch 5100, Loss: 0.3161
Epoch 5200, Loss: 0.3161
Epoch 5300, Loss: 0.3161
Epoch 5400, Loss: 0.3161
Epoch 5500, Loss: 0.3161
Epoch 5600, Loss: 0.3161
Epoch 5700, Loss: 0.3161
Epoch 5800, Loss: 0.3161
Epoch 5900, Loss: 0.3161
Epoch 6000, Loss: 0.3161
Epoch 6100, Loss: 0.3161
Epoch 6200, Loss: 0.3161
Epoch 6300, Loss: 0.3161
Epoch 6400, Loss: 0.3161
Epoch 6500, Loss: 0.3161
Epoch 6600, Loss: 0.3161
Epoch 6700, Loss: 0.3161
Epoch 6800, Loss: 0.3161
Epoch 6900, Loss: 0.3161
Epoch 7000, Loss: 0.3161
Epoch 7100, Loss: 0.3161
Epoch 7200, Loss: 0.3161
Epoch 7300, Loss: 0.3161
Epoch 7400, Loss: 0.3161
Epoch 7500, Loss: 0.3161
Epoch 7600, Loss: 0.3161
Epoch 7700, Loss: 0.3161
Epoch 7800, Loss: 0.3161
Epoch 7900, Loss: 0.3161
Epoch 8000, Loss: 0.3161
Epoch 8100, Loss: 0.3161
Epoch 8200, Loss: 0.3161
Epoch 8300, Loss: 0.3161
Epoch 8400, Loss: 0.3161
Epoch 8500, Loss: 0.3161
Epoch 8600, Loss: 0.3161
Epoch 8700, Loss: 0.3161
Epoch 8800, Loss: 0.3161
Epoch 8900, Loss: 0.3161
Epoch 9000, Loss: 0.3161
Epoch 9100, Loss: 0.3161
Epoch 9200, Loss: 0.3161
Epoch 9300, Loss: 0.3161
Epoch 9400, Loss: 0.3161
Epoch 9500, Loss: 0.3161
Epoch 9600, Loss: 0.3161
Epoch 9700, Loss: 0.3161
Epoch 9800, Loss: 0.3161
Epoch 9900, Loss: 0.3161
```

Below we plot the function $g$ and the estimated function $\hat{g}$.

```python
x_vals_torch = torch.tensor(x_vals, dtype = torch.float32).unsqueeze(1)
ghat_nar = nar(x_vals_torch).detach().numpy()

---

[← Fit the model](02-fit-the-model.md) · [Up: contents](index.md) · [Plot the function →](04-plot-the-function.md)
