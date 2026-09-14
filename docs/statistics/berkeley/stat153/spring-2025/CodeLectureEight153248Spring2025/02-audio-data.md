---
title: Audio Data
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEight153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureEight153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Audio Data

**Source:** [`CodeLectureEight153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureEight153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
y,sr=librosa.load("Hear Piano Note - Middle C.mp3")
n = len(y)
print(n)
print(sr) #sr represents the sampling ratio (this is the number of datapoints for 1 second of audio)
print(n/sr)
```

```
301272
22050
13.66312925170068
```

```python
plt.plot(y)
plt.xlabel('Time')
plt.title('Audio Data')
plt.ylabel('Sound waverform')
```

```
Text(0, 0.5, 'Sound waverform')
```

*(1 figure omitted — see the original notebook.)*

The full plot of the data is not very revealing as the data size is very long. But if we restrict to a smaller portion of the dataset, we can visualize the cyclical behavior more easily.

```python
y_smallpart = y[50000:(50000 + 500)]
plt.plot(y_smallpart)
plt.xlabel('Time')
plt.title('A small segment of the full audio data')
plt.ylabel('Sound waveform')
```

```
Text(0, 0.5, 'Sound waveform')
```

*(1 figure omitted — see the original notebook.)*

Let us fit the single sinusoidal model: $y_t = \beta_0 + \beta_1 \cos(2 \pi f t) + \beta_2 \sin(2 \pi f t) + \epsilon_t$ to this dataset to figure out the best fitting $f$ parameter. Here, in order to compute
\begin{equation*}
    RSS(f) := \argmin_{\beta_0, \beta_1, \beta_2} \sum_{i=1}^n (y_t - \beta_0 - \beta_1 \cos(2 \pi f t) - \beta_2 \sin(2 \pi f t))^2,
\end{equation*}
we have to rely on the periodogram. This method will calculate $RSS(f)$ at the Fourier frequencies very quickly using the connection between $RSS(f)$, the periodogram and the DFT.
\begin{equation*}
   RSS(j/n) = \sum_t (y_t - \bar{y})^2 - 2 I(j/n) ~~ \text{ and } ~~ I(j/n) = \frac{|b_j|^2}{n} ~~ \text{ with }~~ b_j = \sum_t y_t \exp(- 2 \pi i j t/n)
\end{equation*}

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
plt.plot(freqs, pgram)
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.title('Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
def rss_periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, 1/2, 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    var_y = np.sum((y - np.mean(y)) ** 2)
    rssvals = var_y - 2*pgram_y
    return fourier_freqs, rssvals
```

```python
freqs, rssvals = rss_periodogram(y)
plt.plot(freqs, rssvals)
plt.xlabel('Frequency')
plt.ylabel('Residual Sum of Squares')
plt.title('RSS Plot')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Now we estimate the frequency parameter f in the single sinusoidal model:
fhat = freqs[np.argmax(pgram)]
print(fhat)
#To get the frequency in Hertz (which is the number of cycles in one sec)
print(fhat * sr)
#This is quite close to the Middle C frequency (261.625565 Hertz) on the piano
```

```
0.011799968135107147
260.1892973791126
```

For Bayesian uncertainty quantification, we use the posterior:
\begin{equation*}
   I\{0 \leq f \leq 1/2\} |X_f^T X_f|^{-1/2} \left(\frac{1}{RSS(f)} \right)^{(n-p)/2}
\end{equation*}
where $p = 3$ and $|X_f^T X_f|$ denotes the determinant of $X_f^T X_f$. When $f$ is a Fourier frequency (between 0 and 1/2), we have seen that
\begin{equation*}
   X_f^T X_f = \begin{pmatrix} n & 0 & 0 \\ 0 & n/2 & 0 \\ 0 & 0 & n/2 \end{pmatrix}
\end{equation*}
which means that $X_f^T X_f$ does not depend on $f$ (as long as $f$ is a Fourier frequency strictly between 0 and 0.5). For such frequencies, we can drop the $|X_f^T X_f|^{-1/2}$ term from the posterior and we are left with the following simpler formula for the posterior:
\begin{equation*}
   I\{0 < f < 0.5 \text{ is a Fourier frequency}\} \left(\frac{1}{RSS(f)} \right)^{(n-p)/2}
\end{equation*}

```python
#Uncertainty quantification for f:
def logpost_periodogram(y):
    fft_y = np.fft.fft(y)
    n = len(y)
    fourier_freqs = np.arange(1/n, (1/2) + (1/n), 1/n)
    m = len(fourier_freqs)
    pgram_y = (np.abs(fft_y[1:m+1]) ** 2)/n
    var_y = np.sum((y - np.mean(y)) ** 2)
    rssvals = var_y - 2*pgram_y
    p = 3
    logpostvals = ((p-n)/2) * np.log(rssvals)
    return fourier_freqs, logpostvals
```

```python
freqs, logpostvals = logpost_periodogram(y)
plt.plot(freqs, logpostvals)
plt.xlabel('Frequency')
plt.ylabel('Logarithm of Unnormalized Posterior')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Next we exponentiate the log posterior values to compute the posterior.

```python
postvals_unnormalized = np.exp(logpostvals - np.max(logpostvals))
postvals = postvals_unnormalized/(np.sum(postvals_unnormalized))
plt.plot(freqs, postvals)
plt.xlabel('Frequency')
plt.ylabel('Probability')
plt.title('Posterior distribution of frequency')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Credible intervals for $f$ can be obtained as follows.

```python
def PostProbAroundMax(m):
    est_ind = np.argmax(postvals)
    ans = np.sum(postvals[(est_ind-m):(est_ind+m)])
    return(ans)
m = 0
while PostProbAroundMax(m) <= 0.95:
    m = m+1
est_ind = np.argmax(postvals)
f_est = freqs[est_ind]
#95% credible interval for f:
ci_f_low = freqs[est_ind - m]
ci_f_high = freqs[est_ind + m]
print(np.array([f_est, ci_f_low, ci_f_high]))
#Uncertainty estimate in Hertz:
f_est_hz = f_est * sr
ci_f_low_hz = ci_f_low * sr
ci_f_high_hz = ci_f_high * sr
print(np.array([f_est_hz, ci_f_low_hz, ci_f_high_hz]))
```

```
[0.01179997 0.01179665 0.01180329]
[260.18929738 260.1161077  260.26248705]
```

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Sunspots Dataset →](03-sunspots-dataset.md)
