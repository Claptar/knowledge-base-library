---
title: Plot the function
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFour153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyFour153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the function

**Source:** [`CodeLectureTwentyFour153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFour153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (12, 6))
plt.plot(x_vals, y_vals)
plt.title(r'$g(x) = \frac{2x}{1 + 0.8x^2}$')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us first fit the usual AR(1) model, and look at the predictions.

```python
ar = ARIMA(y_sim, order = (1, 0, 0)).fit()
print(ar.summary())
n_y = len(y_sim)
tme = range(1, n_y+1)
k_future = 100 #number of future points for prediction
tme_future = range(n_y+1, n_y+k_future+1)
fcast = ar.get_prediction(start = n_y, end = n_y+k_future-1).predicted_mean
plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast (AR(1))', color = 'green')
plt.axvline(x=n_y, color='gray', linestyle='--')
plt.legend()
plt.show()
```

```
SARIMAX Results
==============================================================================
Dep. Variable:                      y   No. Observations:                  195
Model:                 ARIMA(1, 0, 0)   Log Likelihood                -197.447
Date:                Fri, 25 Apr 2025   AIC                            400.893
Time:                        18:50:36   BIC                            410.712
Sample:                             0   HQIC                           404.869
                                - 195
Covariance Type:                  opg
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.1165      0.277     -0.420      0.675      -0.660       0.427
ar.L1          0.8268      0.041     20.335      0.000       0.747       0.906
sigma2         0.4410      0.056      7.826      0.000       0.331       0.551
===================================================================================
Ljung-Box (L1) (Q):                   5.47   Jarque-Bera (JB):                 4.50
Prob(Q):                              0.02   Prob(JB):                         0.11
Heteroskedasticity (H):               1.15   Skew:                             0.11
Prob(H) (two-sided):                  0.57   Kurtosis:                         2.29
===================================================================================

Warnings:
[1] Covariance matrix calculated using the outer product of gradients (complex-step).
```

*(1 figure omitted — see the original notebook.)*

Next we will fit the nonlinear AR(1) model using PyTorch.

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

```python
y_reg = y_sim[1:]
x_reg = y_sim[0:(n-1)]

y_torch = torch.tensor(y_reg, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_reg, dtype = torch.float32).unsqueeze(1)
```

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
[-1.47418868 -1.05574615 -0.65832485 -0.09346269  0.70088161  1.39251632]
[-2.48088937 -0.77905517  1.14589238  0.11575653  0.79468018  0.80873226
 -2.52554882  0.48737735]
```

```python
nar = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
```

```python
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
Epoch 0, Loss: 0.3025
Epoch 100, Loss: 0.2982
Epoch 200, Loss: 0.2980
Epoch 300, Loss: 0.2979
Epoch 400, Loss: 0.2978
Epoch 500, Loss: 0.2977
Epoch 600, Loss: 0.2976
Epoch 700, Loss: 0.2976
Epoch 800, Loss: 0.2975
Epoch 900, Loss: 0.2975
Epoch 1000, Loss: 0.2974
Epoch 1100, Loss: 0.2974
Epoch 1200, Loss: 0.2974
Epoch 1300, Loss: 0.2973
Epoch 1400, Loss: 0.2973
Epoch 1500, Loss: 0.2973
Epoch 1600, Loss: 0.2972
Epoch 1700, Loss: 0.2972
Epoch 1800, Loss: 0.2972
Epoch 1900, Loss: 0.2972
Epoch 2000, Loss: 0.2972
Epoch 2100, Loss: 0.2972
Epoch 2200, Loss: 0.2971
Epoch 2300, Loss: 0.2971
Epoch 2400, Loss: 0.2971
Epoch 2500, Loss: 0.2971
Epoch 2600, Loss: 0.2971
Epoch 2700, Loss: 0.2971
Epoch 2800, Loss: 0.2971
Epoch 2900, Loss: 0.2971
Epoch 3000, Loss: 0.2971
Epoch 3100, Loss: 0.2971
Epoch 3200, Loss: 0.2971
Epoch 3300, Loss: 0.2971
Epoch 3400, Loss: 0.2971
Epoch 3500, Loss: 0.2971
Epoch 3600, Loss: 0.2971
Epoch 3700, Loss: 0.2971
Epoch 3800, Loss: 0.2971
Epoch 3900, Loss: 0.2971
Epoch 4000, Loss: 0.2971
Epoch 4100, Loss: 0.2971
Epoch 4200, Loss: 0.2971
Epoch 4300, Loss: 0.2971
Epoch 4400, Loss: 0.2971
Epoch 4500, Loss: 0.2971
Epoch 4600, Loss: 0.2971
Epoch 4700, Loss: 0.2971
Epoch 4800, Loss: 0.2971
Epoch 4900, Loss: 0.2971
Epoch 5000, Loss: 0.2971
Epoch 5100, Loss: 0.2971
Epoch 5200, Loss: 0.2971
Epoch 5300, Loss: 0.2971
Epoch 5400, Loss: 0.2971
Epoch 5500, Loss: 0.2971
Epoch 5600, Loss: 0.2971
Epoch 5700, Loss: 0.2971
Epoch 5800, Loss: 0.2971
Epoch 5900, Loss: 0.2971
Epoch 6000, Loss: 0.2971
Epoch 6100, Loss: 0.2971
Epoch 6200, Loss: 0.2971
Epoch 6300, Loss: 0.2971
Epoch 6400, Loss: 0.2971
Epoch 6500, Loss: 0.2971
Epoch 6600, Loss: 0.2971
Epoch 6700, Loss: 0.2971
Epoch 6800, Loss: 0.2971
Epoch 6900, Loss: 0.2971
Epoch 7000, Loss: 0.2971
Epoch 7100, Loss: 0.2971
Epoch 7200, Loss: 0.2971
Epoch 7300, Loss: 0.2971
Epoch 7400, Loss: 0.2971
Epoch 7500, Loss: 0.2971
Epoch 7600, Loss: 0.2971
Epoch 7700, Loss: 0.2971
Epoch 7800, Loss: 0.2971
Epoch 7900, Loss: 0.2971
Epoch 8000, Loss: 0.2971
Epoch 8100, Loss: 0.2971
Epoch 8200, Loss: 0.2971
Epoch 8300, Loss: 0.2971
Epoch 8400, Loss: 0.2971
Epoch 8500, Loss: 0.2971
Epoch 8600, Loss: 0.2971
Epoch 8700, Loss: 0.2971
Epoch 8800, Loss: 0.2971
Epoch 8900, Loss: 0.2971
Epoch 9000, Loss: 0.2971
Epoch 9100, Loss: 0.2971
Epoch 9200, Loss: 0.2971
Epoch 9300, Loss: 0.2971
Epoch 9400, Loss: 0.2971
Epoch 9500, Loss: 0.2971
Epoch 9600, Loss: 0.2971
Epoch 9700, Loss: 0.2971
Epoch 9800, Loss: 0.2971
Epoch 9900, Loss: 0.2971
```

Below we compute the predictions given by the nonlinear AR model.

```python
last_val = torch.tensor([[y_sim[-1]]], dtype = torch.float32)
future_preds = []
for _ in range(k_future):
    next_val = nar(last_val)
    future_preds.append(next_val.item())
    last_val = next_val.detach()
future_preds_array = np.array(future_preds)
```

We also compute predictions using the actual function $g$ which generated the data.

```python
last_val = torch.tensor([[y_sim[-1]]], dtype = torch.float32)
actual_preds = []
for _ in range(k_future):
    next_val = ((2*last_val)/(1 + 0.8 * (last_val ** 2)))
    actual_preds.append(next_val.item())
    last_val = next_val.detach()
actual_preds_array = np.array(actual_preds)
```

```python
n_y = len(y_sim)
tme = range(1, n_y+1)
tme_future = range(n_y+1, n_y+k_future+1)
fcast = ar.get_prediction(start = n_y, end = n_y+k_future-1).predicted_mean
plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast (AR(1))', color = 'green')
plt.plot(tme_future, future_preds_array, label = 'Forecast - NAR', color = 'red')
plt.plot(tme_future, actual_preds_array, label = 'Forecast - True NAR', color = 'black')
plt.axvline(x=n_y, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Model Fitting using PyTorch](01-model-fitting-using-pytorch.md) · [Up: contents](index.md)
