---
title: First fix the number of knots
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# First fix the number of knots

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

k = 4

quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
knots_init = np.quantile(x_scaled, quantile_levels)

n = len(y_scaled)
X = np.column_stack([np.ones(n), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float)) * (x_scaled - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(y_scaled, X).fit()

beta_init = md_init.params.values

print(knots_init)
print(beta_init)
```

```
[-1.03549894 -0.34516631  0.34516631  1.03549894]
[ 2.26579783  1.87350378 -4.48916248  4.49298465 -0.7894067   1.68596401]
```

Now the $\beta$ coefficients are of the same scale.

```python
md_nn = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
```

```python
optimizer = optim.Adam(md_nn.parameters(), lr = 0.01)
loss_fn = nn.MSELoss()

for epoch in range(20000):
    # Zero out gradients
    optimizer.zero_grad()

    # Compute loss
    y_pred = md_nn(x_torch)
    loss = loss_fn(y_pred, y_torch)

    # Compute gradient
    loss.backward()

    # Update parameters
    optimizer.step()

    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
```

```
Epoch 0, Loss: 0.1118
Epoch 1000, Loss: 0.0671
Epoch 2000, Loss: 0.0653
Epoch 3000, Loss: 0.0641
Epoch 4000, Loss: 0.0639
Epoch 5000, Loss: 0.0637
Epoch 6000, Loss: 0.0637
Epoch 7000, Loss: 0.0637
Epoch 8000, Loss: 0.0637
Epoch 9000, Loss: 0.0637
Epoch 10000, Loss: 0.0636
Epoch 11000, Loss: 0.0636
Epoch 12000, Loss: 0.0637
Epoch 13000, Loss: 0.0637
Epoch 14000, Loss: 0.0636
Epoch 15000, Loss: 0.0636
Epoch 16000, Loss: 0.0637
Epoch 17000, Loss: 0.0637
Epoch 18000, Loss: 0.0637
Epoch 19000, Loss: 0.0636
```

Now the convergence is much faster (after about 8000 iterations). Let us plot the fitted values on the original scale.

```python
nn_fits_2 = md_nn(x_torch).detach().numpy()
nn_fits_original_scale_2 = (nn_fits_2 * np.std(y_raw)) + np.mean(y_raw)

plt.figure(figsize = (12, 6))
plt.plot(x_raw, y_raw, color = 'blue', label = 'Data')
plt.plot(x_raw, nn_fits_original_scale_2, color = 'red', label = 'PyTorch Fitted Values (applied on rescaled data)')
plt.plot(x_raw, nn_fits_1, color = 'green', label = 'PyTorch Fitted Values (directly applied on original scale)')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The fit is the same as what we got by running the code on the original raw data. But the convergence of the algorithm is much faster with scaling. This is why scaling is almost always recommended.

## More Model Fitting using PyTorch

In Lecture 24, we showed how PyTorch can be used for parameter estimation in the following models:
1. $y_t = \beta_0 + \beta_1 x_t + \beta_2 (x_t - c_1)_+ + \dots + \beta_{k+1} (x_t - c_k)_+ + \epsilon_t$
2. $y_t = \mu + \epsilon_t + \theta \epsilon_{t-1}$ (with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$)
3. $y_t = \phi_0 + \phi_1 y_{t-1} + \epsilon_t$ (with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$)

Today we shall discuss the variance model, and spectrum model (from Lectures 14-15) and use PyTorch to fit the parameters.

### Variance Model

The variance model is simply $y_t \overset{\text{ind}}{\sim} N(0, \tau_t^2)$. We have seen from Lecture 14 that the negative log-likelihood is:
\begin{align*}
   \sum_{t=1}^n \left(\log \tau_t + \frac{y_t^2}{2 \tau^2_t} \right).
\end{align*}
We reparametrize and write the objective function in terms of $\alpha_t = \log \tau_t$ to get:
\begin{align*}
  \sum_{t=1}^n \left(\alpha_t + \frac{y_t^2}{2} e^{-2 \alpha_t} \right).
\end{align*}
We also saw in Lecture 14 that unconstrained minimization of this negative log-likelihood with respect to $\alpha_t$ gives $\alpha_t = \log |y_t|$, which is complete overfitting in this model.  To prevent overfitting, we can consider the following model for $\alpha_t$:
\begin{align*}
   \alpha_t = \beta_0 + \beta_1 t + \beta_2 (t - c_1)_+ + \dots + \beta_{k+1} (t - c_k)_+.
\end{align*}
If $k$ is small, then overfitting is prevented, and we would get useful estimates. The optimization problem now is to minimize the above negative log-likelihood when $\alpha_t$ is of the above form. When $k$ is small, we will not change the objective function by including a regularization penalty.

First let us create a simulation setting for fitting this model. We shall use one of the simulation settings from Lecture 14.

```python

---

[← but is detached from the computation graph.](11-but-is-detached-from-the-computation-graph.md) · [Up: contents](index.md) · [the following is the true alphat function →](13-the-following-is-the-true-alphat-function.md)
