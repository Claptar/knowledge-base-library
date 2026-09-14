---
title: Fit the model
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureTwentyFour153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fit the model

**Source:** [`CodeLectureTwentyFour153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureTwentyFour153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

armod = AR1Model()
optimizer = optim.Adam(armod.parameters(), lr=0.001)

for epoch in range(4000):
    loss, loglike = armod(ylogdiff_tensor)
    optimizer.zero_grad() #removes previously calculated gradients
    loss.backward() #calculates gradients
    optimizer.step() #updates parameters using gradients

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: phi0={armod.phi0.item():.4f}, phi1={armod.phi1.item():.4f}, sigma={torch.exp(armod.log_sigma).item():.4f}, loss={loss.item():.4f}")
```

```
Epoch 0: phi0=-0.0010, phi1=-0.0010, sigma=0.9990, loss=686.6678
Epoch 100: phi0=-0.0012, phi1=-0.0996, sigma=0.9050, loss=638.2626
Epoch 200: phi0=-0.0013, phi1=-0.1913, sigma=0.8231, loss=595.9210
Epoch 300: phi0=-0.0013, phi1=-0.2703, sigma=0.7529, loss=561.3080
Epoch 400: phi0=-0.0014, phi1=-0.3307, sigma=0.6942, loss=535.2979
Epoch 500: phi0=-0.0014, phi1=-0.3691, sigma=0.6464, loss=517.4683
Epoch 600: phi0=-0.0014, phi1=-0.3880, sigma=0.6091, loss=506.3111
Epoch 700: phi0=-0.0014, phi1=-0.3948, sigma=0.5812, loss=499.9816
Epoch 800: phi0=-0.0014, phi1=-0.3965, sigma=0.5612, loss=496.7854
Epoch 900: phi0=-0.0014, phi1=-0.3969, sigma=0.5478, loss=495.3693
Epoch 1000: phi0=-0.0014, phi1=-0.3969, sigma=0.5393, loss=494.8214
Epoch 1100: phi0=-0.0014, phi1=-0.3969, sigma=0.5342, loss=494.6358
Epoch 1200: phi0=-0.0014, phi1=-0.3970, sigma=0.5313, loss=494.5806
Epoch 1300: phi0=-0.0014, phi1=-0.3970, sigma=0.5298, loss=494.5661
Epoch 1400: phi0=-0.0014, phi1=-0.3970, sigma=0.5291, loss=494.5627
Epoch 1500: phi0=-0.0014, phi1=-0.3970, sigma=0.5287, loss=494.5620
Epoch 1600: phi0=-0.0014, phi1=-0.3970, sigma=0.5286, loss=494.5619
Epoch 1700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 1800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 1900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2000: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2100: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2200: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2300: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2400: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2500: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2600: phi0=-0.0015, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3000: phi0=-0.0015, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3100: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3200: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3300: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3400: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3500: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 3600: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 3900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
```

```python
ar1_pars = np.array([armod.phi0.detach().numpy(), armod.phi1.detach().numpy(), np.exp(2*armod.log_sigma.detach().numpy())]) #mu, theta and sigma^2
print(np.column_stack([armod_ARIMA.params, ar1_pars]))
```

```
[[-0.00102183 -0.00142138]
 [-0.39696193 -0.39696237]
 [ 0.27927876  0.27927739]]
```

It is possible to extend these methods to fit AR($p$) and MA($q$) for more general $p$ and $q$ using PyTorch. The PyTorch method seems to work just as well as ARIMA. Note that the AR code works much faster than the MA code. This is because the it takes longer to write the likelihood for the MA model comapared to the AR model.

## Nonlinear AutoRegression

### Example One

We fit the NonLinear AR(1) model to a simulated dataset generated using the following equation:
\begin{equation*}
   y_t = \frac{2 y_{t-1}}{1 + 0.8 y_{t-1}^2} + \epsilon_t
\end{equation*}
where $\epsilon_t \overset{\text{i.i.d}}{\sim} \text{uniform}(-1, 1)$.

```python
n = 450
rng = np.random.default_rng(seed = 40)
eps = rng.uniform(low = -1.0, high = 1.0, size = n)

y_sim = np.full(n, 0, dtype = float)
for i in range(1, n):
    y_sim[i] = ((2*y_sim[i-1])/(1 + 0.8 * (y_sim[i-1] ** 2))) + eps[i]

plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

This dataset is generated as $y_t = g(y_{t-1}) + \epsilon_t$ where $g(x) := 2x/(1 + 0.8 x^2)$. The function $g$ is plotted below.

```python
def g(x):
    return 2 * x / (1 + 0.8 * x**2)

x_vals = np.linspace(-2, 2, 400)
y_vals = g(x_vals)

---

[← Model Fitting using PyTorch](01-model-fitting-using-pytorch.md) · [Up: contents](index.md) · [Plot the function →](03-plot-the-function.md)
