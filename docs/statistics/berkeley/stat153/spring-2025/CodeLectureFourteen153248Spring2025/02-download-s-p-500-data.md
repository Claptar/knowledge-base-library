---
title: Download S&P 500 data
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFourteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureFourteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Download S&P 500 data

**Source:** [`CodeLectureFourteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFourteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

sp500 = yf.download('^GSPC', start='2000-01-01', end='2024-01-01')

sp500_closeprice = sp500['Close'].to_numpy().flatten() #this is the daily closing price of the S&P 500 index

plt.figure(figsize=(12,6))
plt.plot(sp500_closeprice, label="Price")
plt.xlabel("Date")
plt.title("S&P 500 daily closing price")
plt.ylabel("Price (dollar)")
plt.legend()
plt.show()
```

```
[*********************100%***********************]  1 of 1 completed
```

*(1 figure omitted — see the original notebook.)*

Instead of working with the prices directly, we work with percentage daily returns.

```python
log_prices = np.log(sp500_closeprice)
y = 100 * np.diff(log_prices) #these are the percentage daily returns
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.title('SNP Daily Percentage Returns')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The plot above suggests that Model 2 might be useful for this dataset.

```python
alpha_opt_ridge = alpha_est_ridge(y, 40000000)
alpha_opt_lasso = alpha_est_lasso(y, 2000)
plt.figure(figsize = (12, 6))
plt.plot(alpha_opt_ridge, label = 'ridge')
plt.plot(alpha_opt_lasso, color = 'black', label = 'lasso')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting y^2 against tau^2
plt.figure(figsize = (12, 6))
plt.plot(y ** 2, label = 'Data', color = 'lightblue')
plt.plot(np.exp(2*alpha_opt_ridge), color = 'red', label = 'Ridge')
plt.plot(np.exp(2*alpha_opt_lasso), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting log y^2 against log tau^2
plt.figure(figsize = (12, 6))
plt.plot(2*np.log(np.abs(y) + 1e-8), color = 'lightblue', label = 'Data') #small value added to np.abs(y) to prevent taking logs of zeros
plt.plot(np.log(np.exp(2*alpha_opt_ridge)), color = 'red', label = 'Ridge')
plt.plot(np.log(np.exp(2*alpha_opt_lasso)), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Model THREE

Model 3 is
\begin{equation*}
    \text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2)
\end{equation*}
for $j = 1, \dots, m$ where $b_j$ is the $j^{th}$ DFT coefficient of the observed data $y_1, \dots, y_n$.

Likelihood in terms of the periodogram is:
\begin{equation*}
   \prod_{j=1}^m \frac{n}{\gamma_j^2} \exp \left(-\frac{n I(j/n)}{2 \gamma_j^2} \right)
\end{equation*}
Negative log-likelihood is
\begin{equation*}
  \sum_{j=1}^m \left(\frac{n I(j/n)}{2 \gamma_j^2} +  2 \log \gamma_j \right)
\end{equation*}
Letting $\alpha_j = \log \gamma_j$, we can rewrite the above as
\begin{equation*}
\sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right)
\end{equation*}
Minimizing this without any regularization on $\{\alpha_j\}$ leads to
\begin{equation*}
    \alpha_j = \log \sqrt{\frac{nI(j/n)}{2}} ~~ \text{ and } ~~ \gamma_j^2 = e^{2\alpha_j} = \frac{nI(j/n)}{2}
\end{equation*}
We will use regularization and estimate $\alpha_j$ (and $\gamma_j$) by minimizing:
\begin{equation*}
   \sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right)  + \lambda \sum_{j=2}^{m-1} \left((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right)^2
\end{equation*}
or
\begin{equation*}
    \sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right) + \lambda \sum_{j=2}^{m-1} \left|(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right|.
\end{equation*}
Code for computing these estimators is given below. These functions (spectrum_estimator_ridge and spectrum_estimator_lasso) use $y$ and $\lambda$ as input. In the first step, one computes the periodogram $I(j/n)$ as the optimization is in terms of the periodogram. We apply these methods to the sunspots dataset.

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (10, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

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
freqs, pgram = periodogram(y)
plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(freqs, pgram)
markerline.set_marker("None")
plt.title('Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(freqs, np.log(pgram))
markerline.set_marker("None")
plt.title('Logarithm of the Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
def spectrum_estimator_ridge(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)
    alpha = cp.Variable(m)
    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return alpha.value, freq

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
    return alpha.value, freq
```

After computing the estimators using the above code, we can the periodogram and its logarithm along with suitable estimates. The mean of $I(j/n)$ according to the model is
\begin{equation*}
  \mathbb{E} I(j/n) = \frac{2 \gamma_j^2}{n} = \frac{2}{n} e^{2 \alpha_j}
\end{equation*}

```python
alpha_opt_ridge, freq = spectrum_estimator_ridge(y, 100)
pgram_mean_ridge = (2/n)*(np.exp(2*alpha_opt_ridge))
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 10)
pgram_mean_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(freq, pgram, linefmt = 'lightblue', basefmt = '')
markerline.set_marker("None")
plt.title('Periodogram')
plt.plot(freq, pgram_mean_ridge, color = 'red', label = 'Ridge')
plt.plot(freq, pgram_mean_lasso, color = 'black', label = "LASSO")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(freq, np.log(pgram), linefmt = 'lightblue', basefmt = '')
markerline.set_marker("None")
plt.title('Periodogram')
plt.plot(freq, np.log(pgram_mean_ridge), color = 'red', label = 'Ridge')
plt.plot(freq, np.log(pgram_mean_lasso), color = 'black', label = "LASSO")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Three High-Dimensional Models for Time Series](01-three-high-dimensional-models-for-time-series.md) · [Up: contents](index.md)
