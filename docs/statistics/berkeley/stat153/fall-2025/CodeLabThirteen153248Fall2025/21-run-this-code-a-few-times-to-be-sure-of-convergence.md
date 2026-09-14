---
title: Run this code a few times to be sure of convergence.
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Run this code a few times to be sure of convergence.

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```

```
Epoch 0, Loss: 1230.7987
Epoch 1000, Loss: 1200.7444
Epoch 2000, Loss: 1199.7701
Epoch 3000, Loss: 1199.2241
Epoch 4000, Loss: 1198.9481
Epoch 5000, Loss: 1198.8514
Epoch 6000, Loss: 1198.7220
Epoch 7000, Loss: 1198.5948
Epoch 8000, Loss: 1198.5424
Epoch 9000, Loss: 1198.5123
Epoch 10000, Loss: 1198.4650
Epoch 11000, Loss: 1198.2202
Epoch 12000, Loss: 1198.0922
Epoch 13000, Loss: 1198.0574
Epoch 14000, Loss: 1197.9463
Epoch 15000, Loss: 1197.9348
Epoch 16000, Loss: 1197.8220
Epoch 17000, Loss: 1197.7927
Epoch 18000, Loss: 1197.7850
Epoch 19000, Loss: 1197.7164
```

```python
#alpha_est = md_PiecewiseLinear(x_torch).detach().numpy() + np.log(np.std(pgram))
alpha_est = md_PiecewiseLinear(x_torch).detach().numpy()
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram), label = 'Log Periodogram', color = 'lightblue')
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.title('Logarithm of Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Let us compare this estimate with our previous method (from Lectures 14-15).

```python
import cvxpy as cp
#import mosek

def spectrum_estimator_lasso(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)
    alpha = cp.Variable(m)

    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)

    problem = cp.Problem(objective)
    problem.solve()
    #problem.solve(solver = cp.MOSEK)
    return alpha.value, freq
```

```python
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 10)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
plt.plot(freq, np.log(pgram))
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "CVXPy LASSO Estimate")
plt.plot(freqs, alpha_est, color = 'red', label = 'PyTorch Estimate')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The estimates are clearly reasonably close to each other.

### Example 2: Earthquake Data

Below is an example where this PyTorch method does not quite seem to work. This is for the earthquake dataset that we previously used in Lecture 15.
This dataset is from the Mathworks (MATLAB) tutorial "Practical Introduction to Frequency-Domain Analysis" (see [this link](https://www.mathworks.com/help/signal/ug/practical-introduction-to-frequency-domain-analysis.html)). From this matlab tutorial: *Active Mass Driver (AMD) control systems are used to reduce vibration in a building under an earthquake. An active mass driver is placed on the top floor of the building and, based on displacement and acceleration measurements of the building floors, a control system sends signals to the driver so that the mass moves to attenuate ground disturbances. Acceleration measurements were recorded on the first floor of a three story test structure under earthquake conditions. Measurements were taken without the active mass driver control system (open loop condition), and with the active control system (closed loop condition).*

We will use the data on the open loop condition.

```python
from scipy.io import loadmat
mat_dict = loadmat('quakevibration.mat')
print(mat_dict.keys())

gfloor1OL_array = mat_dict['gfloor1OL']
print(gfloor1OL_array.shape)

y = gfloor1OL_array.ravel()

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.title('Ground Floor Acceleration Measurements (Open Loop)')
plt.xlabel('Time (milliseconds)')
plt.ylabel('Acceleration (in/s^2)')
plt.show()
```

```
dict_keys(['__header__', '__version__', '__globals__', 'gfloor1OL', 'gfloor1CL'])
(10000, 1)
```

*(1 figure omitted — see the original notebook.)*

The periodogram is given by:

```python
n = len(y)
freqs, pgram = periodogram(y)
m = len(pgram)
```

The initial values of the parameters are obtained below.

```python
k = 10 # this is the number of knots
quantile_levels = np.linspace(1/(k+1), k/(k+1), k)
x = np.arange(1, m+1)
x_scaled = (x - np.mean(x))/(np.std(x))
knots_init = np.quantile(x_scaled, quantile_levels)

X = np.column_stack([np.ones(m), x_scaled])
for j in range(k):
    xc = ((x_scaled > knots_init[j]).astype(float)) * (x_scaled - knots_init[j])
    X = np.column_stack([X, xc])
md_init = sm.OLS(np.log(pgram), X).fit()

#print(md_init.summary())
#print(md_init.params)
beta_init = md_init.params
print(knots_init)
print(beta_init)
```

```
[-1.41684902 -1.10199369 -0.78713835 -0.47228301 -0.15742767  0.15742767
  0.47228301  0.78713835  1.10199369  1.41684902]
[-40.11567801 -22.89394746  20.3600293   -0.40359563   1.59487819
  -0.05497328   0.36121425   0.53068634  -0.05943841   0.45359363
  -0.23388732   0.40076595]
```

Here is the PyTorch code.

```python
#y_torch = torch.tensor(pgram/np.std(pgram), dtype = torch.float32).unsqueeze(1)
y_torch = torch.tensor(pgram, dtype = torch.float32).unsqueeze(1)
x_torch = torch.tensor(x_scaled, dtype = torch.float32).unsqueeze(1)
```

```python
md_PiecewiseLinear = PiecewiseLinearModel(knots_init = knots_init, beta_init = beta_init)
optimizer = optim.Adam(md_PiecewiseLinear.parameters(), lr = 0.01)

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

[← Run this code a few times to be sure of convergence.](20-run-this-code-a-few-times-to-be-sure-of-convergence.md) · [Up: contents](index.md) · [Run this code a few times to be sure of convergence. →](22-run-this-code-a-few-times-to-be-sure-of-convergence.md)
