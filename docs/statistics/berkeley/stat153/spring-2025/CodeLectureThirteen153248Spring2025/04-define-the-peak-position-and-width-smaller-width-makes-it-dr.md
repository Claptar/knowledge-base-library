---
title: Define the peak position and width (smaller width makes it drop quickly)
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThirteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Define the peak position and width (smaller width makes it drop quickly)

**Source:** [`CodeLectureThirteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Estimating the spectrum by smoothing the periodogram

In the next lecture, we shall see how to estimate the spectrum from observed data. The main idea is to smooth the periodogram. This is illustrated below (details will be given in the next lecture).

```python
y = sunspots.iloc[:,1].values
def periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    return fourier_freqs, pgram_y
```

Below we compute the periodogram, and plot its logarithm.

```python
freqs, pgram = periodogram(y)
plt.plot(freqs, np.log(pgram))
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The following function computes the estimate of $\log \tau_j$ (below $\log \tau_j$ is denoted by $\alpha_j$).

```python
def spectrum_estimator(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)  # Length of original time series
    alpha = cp.Variable(m)
    likelihood_term = cp.sum(cp.multiply((2 * I / n), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve()
    return alpha.value, freq  # Return estimated log spectral density and frequencies
```

```python
alpha_opt, freq = spectrum_estimator(y, 1000)
#Below we plot the log(periodogram) and the fitted spectrum estimator on the same plot
#This illustrates how the spectrum estimate can be viewed as a smoothing of the periodogram
plt.plot(freqs, np.log(pgram))
plt.plot(freqs, np.log(n/4) + 2*alpha_opt)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Below we plot the peridogram and its smoothed version (on the original scale without the logarithms)
plt.plot(freqs, pgram)
plt.plot(freqs, (n/4)*np.exp(2*alpha_opt))
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below is the plot of the estimated spectrum.

```python
#Estimated spectrum
tau_opt = np.exp(alpha_opt)
plt.plot(tau_opt)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we simulate data from this spectrum.

```python
b_coeff = np.zeros(n)
b_coeff[0] = np.mean(y)
for j in range(m):
    tauval = tau_opt[j]
    aj = rng.normal(loc = 0, scale = tauval, size = 1)
    bj = rng.normal(loc = 0, scale = tauval, size = 1)
    b_coeff[(2*j)+1] = aj
    b_coeff[(2*j)+2] = bj
simvals = np.dot(X, b_coeff)
plt.figure(figsize = (10, 6))
plt.plot(simvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The following are the peaks and the gaps between them for the above simulated dataset.

```python
peaks, _ = find_peaks(simvals)
gaps = np.diff(peaks)
print("Peaks:", peaks)
print("Gaps between peaks:", gaps)
```

```
Peaks: [  6  11  15  19  28  30  37  40  49  54  60  63  68  72  74  80  83  86
  90  93  97 100 104 107 109 115 125 134 141 146 150 153 158 162 172 176
 180 184 189 194 197 201 205 216 222 224 229 233 240 242 245 248 253 261
 266 273 281 283 285 289 291 298 306 313 318]
Gaps between peaks: [ 5  4  4  9  2  7  3  9  5  6  3  5  4  2  6  3  3  4  3  4  3  4  3  2
  6 10  9  7  5  4  3  5  4 10  4  4  4  5  5  3  4  4 11  6  2  5  4  7
  2  3  3  5  8  5  7  8  2  2  4  2  7  8  7  5]
```

The following are the peaks and the gaps between them for the actual sunspots dataset.

```python
peaks, _ = find_peaks(y)
gaps = np.diff(peaks)
print("Peaks:", peaks)
print("Gaps between peaks:", gaps)
```

```
Peaks: [  5  17  27  38  50  52  61  69  78  87 102 104 116 130 137 148 160 164
 170 177 183 193 198 205 207 217 228 237 247 257 268 272 279 289 291 300
 314]
Gaps between peaks: [12 10 11 12  2  9  8  9  9 15  2 12 14  7 11 12  4  6  7  6 10  5  7  2
 10 11  9 10 10 11  4  7 10  2  9 14]
```

We simulate a bunch of these datasets and compare them to the original sunspots data.

```python
fig, axes = plt.subplots(3, 3, figsize = (12, 4))
axes = axes.flatten()
for i in range(6):
    b_coeff = np.zeros(n)
    b_coeff[0] = np.mean(y)
    for j in range(m):
        tauval = tau_opt[j]
        aj = rng.normal(loc = 0, scale = tauval, size = 1)
        bj = rng.normal(loc = 0, scale = tauval, size = 1)
        b_coeff[(2*j)+1] = aj
        b_coeff[(2*j)+2] = bj
        simvals = np.dot(X, b_coeff)
    axes[i].plot(simvals)
axes[6].plot(y)
for i, idx in enumerate(range(7, 9)):
    b_coeff = np.zeros(n)
    b_coeff[0] = np.mean(y)
    for j in range(m):
        tauval = tau_opt[j]
        aj = rng.normal(loc = 0, scale = tauval, size = 1)
        bj = rng.normal(loc = 0, scale = tauval, size = 1)
        b_coeff[(2*j)+1] = aj
        b_coeff[(2*j)+2] = bj
        simvals = np.dot(X, b_coeff)
    axes[idx].plot(simvals)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The simulated datasets still look different from the actual sunspots dataset. But they are not as wiggly as before and seem to have well-defined peaks with gaps between peaks varying as in the actual sunspots dataset.

---

[← Find peaks](03-find-peaks.md) · [Up: contents](index.md)
