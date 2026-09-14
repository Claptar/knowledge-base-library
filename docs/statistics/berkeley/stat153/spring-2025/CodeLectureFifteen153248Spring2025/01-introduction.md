---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFifteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureFifteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`CodeLectureFifteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFifteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

---
title: Spectral Analysis
---

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import cvxpy as cp
import mosek
```

The library "mosek" above is a commercial solver for convex optimization. I will use "solver = MOSEK" in the convex optimization schemes below for computing the spectral estimators. Mosek is more reliable than the other solvers that cvxpy uses. To use MOSEK, you first have to install it in your python environment (e.g., using "pip install mosek" or "conda install -c conda-forge mosek"), then you need to request a personal mosek academic license (at this address: https://www.mosek.com/products/academic-licenses/ by using your email address). The license will be emailed to you. You need to download the license file and place it in the correct directory (this information is given in the license email). After this, the mosek solver should work in cvxpy.

## Spectrum Model

We are working with the model: $\text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2)$ for $j = 1, \dots, m$ (here $m = (n-1)/2$), where $b_0, \dots, b_{n-1}$ denote the DFT of the observed data $y_t$. The parameters underlying this model are $\gamma_1^2, \dots, \gamma_m^2$. The model can be written in terms of the periodogram $I(j/n)$ as
\begin{equation*}
   I(j/n) = \frac{|b_j|^2}{n} \overset{\text{ind}}{\sim} \frac{\gamma_j^2}{n} \chi^2_2
\end{equation*}
The mean of the periodogram is called the power spectrum and is given by
\begin{equation*}
   f(j/n) = \frac{2 \gamma_j^2}{n} ~~~ \text{ for } j = 1, \dots, m.
\end{equation*}
If we treat $f(j/n)$ as a function on $[0, 1/2]$ (say by joining successive values by lines), we obtain the power spectral density function.

### Application One: Sunspots Dataset

```python
sunspots = pd.read_csv('SN_y_tot_V2.0.csv', header = None, sep = ';')
y = sunspots.iloc[:,1].values
n = len(y)
plt.figure(figsize = (12, 6))
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
plt.plot(freqs, pgram)
plt.title('Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
freqs, pgram = periodogram(y)
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram))
plt.title('Log Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To estimate $\gamma_j, j = 1, \dots, m$, we use the following estimators (below $\alpha_j = \log \gamma_j$)
\begin{equation*}
   \sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right)  + \lambda \sum_{j=2}^{m-1} \left((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right)^2
\end{equation*}
or
\begin{equation*}
    \sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right) + \lambda \sum_{j=2}^{m-1} \left|(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right|.
\end{equation*}

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
    problem.solve(solver = cp.MOSEK)
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
    problem.solve(solver = cp.MOSEK)
    return alpha.value, freq
```

The power spectrum is given by
\begin{equation*}
   f(j/n) = \mathbb{E} I(j/n) = \frac{2 \gamma_j^2}{n} = \frac{2}{n} e^{2 \alpha_j}
\end{equation*}

```python
alpha_opt_ridge, freq = spectrum_estimator_ridge(y, 100)
power_ridge = (2/n)*(np.exp(2*alpha_opt_ridge))
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 10)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
#markerline, stemline, baseline = plt.stem(freq, pgram, linefmt = 'lightblue', basefmt = '')
#markerline.set_marker("None")
plt.plot(freq, pgram)
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, power_ridge, color = 'red', label = 'Ridge')
plt.plot(freq, power_lasso, color = 'black', label = "LASSO")
plt.legend()
plt.show()

#Mosek sometimes gives some format conversion warnings which you can ignore
```

```
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.11/site-packages/mosek/__init__.py:18617: UserWarning: Argument sub in putvarboundlist: Incorrect array format causing data to be copied
  warnings.warn("Argument sub in putvarboundlist: Incorrect array format causing data to be copied");
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.11/site-packages/mosek/__init__.py:18925: UserWarning: Argument subj in putclist: Incorrect array format causing data to be copied
  warnings.warn("Argument subj in putclist: Incorrect array format causing data to be copied");
/Users/aditya/mambaforge/envs/stat153spring2025/lib/python3.11/site-packages/mosek/__init__.py:18349: UserWarning: Argument sub in putconboundlist: Incorrect array format causing data to be copied
  warnings.warn("Argument sub in putconboundlist: Incorrect array format causing data to be copied");
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
#markerline, stemline, baseline = plt.stem(freq, np.log(pgram), linefmt = 'lightblue', basefmt = '')
#markerline.set_marker("None")
plt.plot(freq, np.log(pgram), color = 'lightblue')
plt.title('Log Periodogram and Log Power Spectrum')
plt.plot(freq, np.log(power_ridge), color = 'red', label = 'Ridge')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "LASSO")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There is a whole band of frequencies which contribute towards the mode in the power spectrum.

### Application Two: Southern Oscillation Index Dataset

This dataset can be downloaded from http://www.bom.gov.au/climate/enso/soi/. El Niño (see wiki entry) is a climate pattern that describes the unusual warming of surface waters in the eastern tropical Pacific Ocean. It is believed to occur irregularly at two to seven year intervals. Closely related to the fluctuations in oceanic temperatures are large-scale changes in atmospheric pressure. El Nino events are associated with sustained negative Southern Oscillation Index (SOI) values. The SOI is computed from fluctuations in the surface air pressure difference between Tahiti and Darwin. See the paper "The definition of El Nino" by Trenberth 1997 for more details.

Wikipedia article for El Niño Southern Oscillation has this sentence: "El Niño and Li Niña last a year or so and typically occur every two to seven years with varying intensity, with neutral periods of lower intensity interspersed."

```python
def load_soi_data(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip blank lines if any

            date_str, soi_str = line.split(',')
            date_code = int(date_str)   # e.g. 187601
            year = date_code // 100     # e.g. 1876
            month = date_code % 100     # e.g. 1
            soi_val = float(soi_str)

            data.append([year, month, soi_val])

    # Create a DataFrame from parsed rows
    df = pd.DataFrame(data, columns=['Year', 'Month', 'SOI'])

    # Convert Year, Month to a datetime; assume day=1 for each month
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))

    # Make Date the index
    df.set_index('Date', inplace=True)

    # Sort by date just in case (and drop the now-redundant Year/Month columns)
    df.sort_index(inplace=True)

    return df[['SOI']]

---

[Up: contents](index.md) · [Usage →](02-usage.md)
