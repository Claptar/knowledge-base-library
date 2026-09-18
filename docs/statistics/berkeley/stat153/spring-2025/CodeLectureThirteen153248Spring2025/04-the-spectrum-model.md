---
title: The Spectrum Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThirteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureThirteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The Spectrum Model

To obtain the spectrum model, we shall first remove the $\epsilon_t$ and write:
\begin{equation*}
   y_t = \beta_0 + \sum_{j = 1}^{m} \left( \beta_{1j} \cos(2 \pi (j/n) t) + \beta_{2j} \sin (2 \pi (j/n) t) \right)
\end{equation*}
where $m := (n-1)/2$. We further assume that
\begin{equation*}
    \beta_{1j}, \beta_{2j} \overset{\text{i.i.d}}{\sim} N(0, \tau_j^2)
\end{equation*}
The variances $\tau_1^2, \dots, \tau_m^2$ denote the unknown parameters in the model (collectively, they are known as the spectrum of the model).

The variance parameter $\tau_j^2$ represents how much contribution the corresponding frequency $j/n$ has in the overall variance structure of $y_t$. If $\tau_j^2$ is large for a specific $j$, the corresponding frequency $j/n$ has a strong contribution to the data. If $\tau_j^2$ is small, the contribution of that frequency is small.

The total variance of $y_t$ is given by:
\begin{equation*}
   \text{var}(y_t) = \sum_{j=1}^m \tau_j^2.
\end{equation*}
This reflects how the variance of the signal is distributed across different frequency components.

The sequence $\{\tau_j^2\}$ provides a **spectral representation** of the time series, in the sense that it describes the distribution of variance across frequencies.

Below we take some fixed spectrum i.e., we fix $\tau_j^2, j = 1, \dots, m$ and simulate data from the spectrum model. The goal is to get a sense of the kind of data we would get for different spectra.

## Example One

The first example corresponds to the case where $\tau_j^2$ takes a constant value when $j/n$ lies between $1/13$ and $1/9$ and then zero for other values of $j/n$. Frequencies between $1/13$ and $1/9$ contributed equally to this data while no other frequency has any contribution. Let us see how the data looks.

```python
X = np.column_stack([np.ones(n)])
x = np.arange(1, n+1)
m = (n-1)//2
for j in range(m):
    f = j/n
    xcos = np.cos(2 * np.pi * f * x)
    xsin = np.sin(2 * np.pi * f * x)
    X = np.column_stack([X, xcos, xsin])

tau_t = np.zeros(m)
lf = n // 13
uf = n // 9
y = sunspots.iloc[:,1].values
tau_t[lf:uf] = np.sqrt(np.var(y)/(uf - lf))

b_coeff = np.zeros(n)
b_coeff[0] = np.mean(y) #we are using the mean of the sunspots dataset for b0
for j in range(m):
    tauval = tau_t[j]
    aj = rng.normal(loc = 0, scale = tauval, size = 1)
    bj = rng.normal(loc = 0, scale = tauval, size = 1)
    b_coeff[(2*j)+1] = aj.item()
    b_coeff[(2*j)+2] = bj.item()
simvals = np.dot(X, b_coeff)
plt.figure(figsize = (10, 6))
plt.plot(simvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The data looks quite smooth (without any seemingly random fluctuation). Let us look at the peaks and the gaps between them.

```python
# Find peaks
peaks, _ = find_peaks(simvals)
gaps = np.diff(peaks)
print("Peaks:", peaks)
print("Gaps between peaks:", gaps)
```

```
Peaks: [  3  13  24  34  43  51  59  69  79  90 100 105 115 124 134 144 154 164
 174 184 195 208 219 230 243 251 262 272 283 292 302 312 319]
Gaps between peaks: [10 11 10  9  8  8 10 10 11 10  5 10  9 10 10 10 10 10 10 11 13 11 11 13
  8 11 10 11  9 10 10  7]
```

The gaps between the peaks varies in a way that is somewhat reminiscent of the sunspots dataset.

We can try to fit a single sinusoid model to this dataset to see which frequency estimate it gives.

```python
y = simvals
ngrid = 10000
fvals = np.linspace(0, 0.5, ngrid)
rssvals = np.array([rss(f) for f in fvals])
plt.plot(fvals, rssvals)
fhat = fvals[np.argmin(rssvals)]
print(1/fhat)
```

```
9.619047619047619
```

*(1 figure omitted — see the original notebook.)*

## Example Two

In the second example, we take $\tau_j^2$ to equal some constant value when the $j/n$ lies between $1/13$ and $1/9$, and some other constant value when $j/n$ lies between $1/25$ and $1/22$. We will take it to be zero for all other frequencies.

```python
tau_t = np.zeros(m)
lf = n // 13
uf = n // 9
tau_t[lf:uf] = np.sqrt(1/(uf - lf))
lf2 = n//25
uf2 = n//22
tau_t[lf2:uf2] = np.sqrt(1/(uf2 - lf2))
y = sunspots.iloc[:,1].values
tau_t = np.sqrt(np.var(y)) * (tau_t/np.sqrt(np.sum(tau_t ** 2)))


b_coeff = np.zeros(n)
b_coeff[0] = np.mean(y)
print(b_coeff[0])
for j in range(m):
    tauval = tau_t[j]
    aj = rng.normal(loc = 0, scale = tauval, size = 1)
    bj = rng.normal(loc = 0, scale = tauval, size = 1)
    b_coeff[(2*j)+1] = aj
    b_coeff[(2*j)+2] = bj
simvals = np.dot(X, b_coeff)
plt.figure(figsize = (10, 6))
plt.plot(simvals)
plt.show()
```

```
78.76
```

*(1 figure omitted — see the original notebook.)*

This dataset visually seems more similar to the sunspots data compared to the previous datasets with lots of random fluctuations.

```python
peaks, _ = find_peaks(simvals)
gaps = np.diff(peaks)
print("Peaks:", peaks)
print("Gaps between peaks:", gaps)
```

```
Peaks: [  9  20  27  37  47  56  67  77  94 103 118 127 139 148 157 169 178 195
 203 222 230 249 258 269 276 287 298 315]
Gaps between peaks: [11  7 10 10  9 11 10 17  9 15  9 12  9  9 12  9 17  8 19  8 19  9 11  7
 11 11 17]
```

Again the gaps between the peaks varies over the course of the dataset (which happens in the actual sunspots dataset as well).

## Example Three

In the third example, we take the spectrum to be given by a decreasing or increasing sequence of $\tau_j^2$.

```python
freqs = (np.arange(1, m+1))/n
th = -0.8
tau_t = np.sqrt((1 + (th ** 2) + 2*th*np.cos(2 * np.pi * freqs)))
#when th>0, these tau_t values are decreasing.
#when th<0, these tau_t values are increasing
y = sunspots.iloc[:,1].values
tau_t = np.sqrt(np.var(y)) * (tau_t/np.sqrt(np.sum(tau_t ** 2)))
plt.plot(tau_t)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
b_coeff = np.zeros(n)
b_coeff[0] = np.mean(y)
print(b_coeff[0])
for j in range(m):
    tauval = tau_t[j]
    aj = rng.normal(loc = 0, scale = tauval, size = 1)
    bj = rng.normal(loc = 0, scale = tauval, size = 1)
    b_coeff[(2*j)+1] = aj
    b_coeff[(2*j)+2] = bj
simvals = np.dot(X, b_coeff)
plt.figure(figsize = (10, 6))
plt.plot(simvals)
plt.show()
```

```
78.76
```

*(1 figure omitted — see the original notebook.)*

Change the $\tau_t$ values from increasing to decreasing, and then examine how the plot of the data changes.

## Example Four

Here we take $\tau_j^2$ to be peaked for $j/n$ which is close to 11.

```python
#the following tau_j^2 is peaked around j/n = 1/11 and then drops quickly as j/n moves away from 1/11
j_vals = np.arange(m)
# Define the peak position and width (smaller width makes it drop quickly)
peak_pos = n // 11
width = n // 50  # Adjust width for quicker drop-off
tau_t = 100*np.exp(-((j_vals - peak_pos) ** 2) / (2 * width ** 2))
tau_t = np.sqrt(np.var(y)) * (tau_t / np.sqrt(np.sum(tau_t ** 2)))
plt.plot(tau_t)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
b_coeff = np.zeros(n)
b_coeff[0] = np.mean(y)
print(b_coeff[0])
for j in range(m):
    tauval = tau_t[j]
    aj = rng.normal(loc = 0, scale = tauval, size = 1)
    bj = rng.normal(loc = 0, scale = tauval, size = 1)
    b_coeff[(2*j)+1] = aj
    b_coeff[(2*j)+2] = bj
simvals = np.dot(X, b_coeff)
plt.figure(figsize = (10, 6))
plt.plot(simvals)
plt.show()
```

```
78.76
```

*(1 figure omitted — see the original notebook.)*

```python
peaks, _ = find_peaks(simvals)
gaps = np.diff(peaks)
print("Peaks:", peaks)
print("Gaps between peaks:", gaps)
```

```
Peaks: [  9  20  27  37  47  56  67  77  94 103 118 127 139 148 157 169 178 195
 203 222 230 249 258 269 276 287 298 315]
Gaps between peaks: [11  7 10 10  9 11 10 17  9 15  9 12  9  9 12  9 17  8 19  8 19  9 11  7
 11 11 17]
```

---

[← Ridge and LASSO regression with sinusoids](03-ridge-and-lasso-regression-with-sinusoids.md) · [Up: contents](index.md) · Estimating the spectrum by smoothing the periodogram →
