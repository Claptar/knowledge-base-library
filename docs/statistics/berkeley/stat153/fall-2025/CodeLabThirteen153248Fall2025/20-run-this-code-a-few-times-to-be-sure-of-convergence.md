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
Epoch 0, Loss: 1876.1447
Epoch 1000, Loss: 384.1796
Epoch 2000, Loss: 382.5848
Epoch 3000, Loss: 380.2390
Epoch 4000, Loss: 378.5027
Epoch 5000, Loss: 376.6567
Epoch 6000, Loss: 374.1023
Epoch 7000, Loss: 373.7757
Epoch 8000, Loss: 373.1777
Epoch 9000, Loss: 372.4913
Epoch 10000, Loss: 372.2776
Epoch 11000, Loss: 372.0750
Epoch 12000, Loss: 372.0114
Epoch 13000, Loss: 372.4420
Epoch 14000, Loss: 371.9330
Epoch 15000, Loss: 371.8340
Epoch 16000, Loss: 371.8694
Epoch 17000, Loss: 371.8499
Epoch 18000, Loss: 372.0723
Epoch 19000, Loss: 371.8283
```

The estimate of $\alpha_t$ is obtained as follows.

```python
alpha_est = md_PiecewiseLinear(x_torch).detach().numpy()
```

```python
plt.figure(figsize = (12, 6))
plt.plot(alpha_est, label = 'PyTorch Estimate')
plt.plot(alpha_true, color = 'red', label = 'true')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The estimate is pretty good.

### Spectrum Model

We have a time series $y_t$ with periodogram $I(j/n)$. The spectrum model is given by:
\begin{equation*}
   I(j/n) \overset{\text{ind}}{\sim} f(j/n) \eta_j
\end{equation*}
for $j = 1, \dots, m$ where $m$ is the largest integer strictly smaller than $n/2$. Here $\eta_j \overset{\text{i.i.d}}{\sim} Exp(1)$. The parameters in this model are $f(j/n), j = 1, \dots, m$ (it is called the power of frequency $j/n$).

The likelihood is given by:
\begin{align*}
   \prod_{j=1}^m \frac{1}{f(j/n)} \exp \left(-\frac{I(j/n)}{f(j/n)} \right).
\end{align*}
So the negative log-likelihood is:
\begin{align*}
   \sum_{j = 1}^{m} \left(\frac{I(j/n)}{f(j/n)} + \log f(j/n)\right).
\end{align*}
We reparametrize this by $\log f(j/n) = \alpha_j$ so the minimization problem becomes:
\begin{align*}
   \sum_{j = 1}^{m} \left(I(j/n) \exp(-\alpha_j) + \alpha_j\right).
\end{align*}
Unconstrained minimization is easily seen to lead to $\alpha_j = \log I(j/n)$, so it makes sense to make further constraining assumptions on $\alpha_j$. We use the assumption:
\begin{align*}
   \alpha_j = \beta_0 + \beta_1 j + \beta_2 (j - c_1)_+ + \dots + \beta_{k+1} (j - c_k)_+.
\end{align*}

### Example One: Sunspots Data

Let us apply the method to the sunspots dataset.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)

plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we compute the periodogram of the data.

```python
def periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    return fourier_freqs, pgram_y
```

```python
n = len(y)
freqs, pgram = periodogram(y)
m = len(pgram)
```

Below we plot the periodogram and its logarithm.

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, pgram, label = 'Periodogram')
plt.title('Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram), label = 'Log Periodogram')
plt.title('Logarithm of Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Our first step is to get preliminary estimates of $c_1, \dots, c_k$ and $\beta_0, \dots, \beta_{k+1}$. We rescale $j = 1, \dots, n$ to $x_1, \dots, x_m$. Then we take $c_1, \dots, c_k$ to be the quantiles of $x_j$ at $1/(k+1), \dots, k/(k+1)$. For $\beta_0, \dots, \beta_{k+2}$, we run a linear regression of $\log I(j/n)$ on $1, x_j, (x_j - c_1)_+, \dots, (x_j - c_k)_+$ with these initial $c_1, \dots, c_k$ and then take the corresponding coefficients.

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
[-1.40841158 -1.09543123 -0.78245088 -0.46947053 -0.15649018  0.15649018
  0.46947053  0.78245088  1.09543123  1.40841158]
[ -9.0879961  -10.99249551  23.75611862 -26.47556894  16.98756723
  -9.10663734   3.89842712   2.67957451  -3.61744261   3.02132995
   0.94878987  -1.06944189]
```

Below we create the torch objects for use in the PyTorch code.

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

[← of mdPiecewiseLinear during training, using a learning rate of 0.01.](19-of-mdpiecewiselinear-during-training-using-a-learning-rate-o.md) · [Up: contents](index.md) · [Run this code a few times to be sure of convergence. →](21-run-this-code-a-few-times-to-be-sure-of-convergence.md)
