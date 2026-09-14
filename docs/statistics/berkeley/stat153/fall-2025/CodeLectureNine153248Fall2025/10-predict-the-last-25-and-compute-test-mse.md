---
title: Predict the last 25 and compute test MSE
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureNine153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Predict the last 25 and compute test MSE

**Source:** [`CodeLectureNine153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureNine153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

y_pred_test = model.predict(X_test)
test_mse = np.mean((y_test - y_pred_test)**2)

#print(model.summary())
print(f"Test MSE (last {n_test} observations): {test_mse:.6g}")
```

```
Test MSE (last 50 observations): 2253.98
```

```python
y_fit_train = model.predict(X_train)
plt.figure(figsize=(10, 6))
plt.plot(y, label='Observed')
plt.plot(np.arange(len(y_fit_train)), y_fit_train, color='black', label='Train fit')
plt.plot(np.arange(n - n_test, n), y_pred_test, color='red', label='Test predictions')
plt.axvspan(n - n_test, n - 1, alpha=0.1, label='Test window')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Discrete Fourier Transform

For a dataset $y_0, \dots, y_{n-1}$, its DFT is $b_0, b_1, \dots, b_{n-1}$ where
\begin{equation*}
   b_j = \sum_{t=0}^{n-1} y_t \exp \left(-\frac{2 \pi i j t}{n} \right).
\end{equation*}
for $j = 0, 1, \dots, n-1$. In other words, $b_j$ is a complex number with real part $\sum_t y_t \cos(2 \pi (j/n) t)$ and imaginary part $-\sum_t y_t \sin(2 \pi (j/n) t)$.

```python
y = np.array([1, -5, 3, 10, -5, 1, 6])
dft_y = np.fft.fft(y)
print(dft_y)
b0 = np.sum(y)
print(b0)
n = len(y)
#Here is the formula for calculating the real and imaginary parts of b2:
f = 3/n
cosvec = np.cos(2 * np.pi * f * np.arange(n))
sinvec = np.sin(2 * np.pi * f * np.arange(n))
b_cos = np.sum(y * cosvec)
b_sin = np.sum(y * sinvec)
print(b_cos, b_sin) #the real part of DFT is b_cos and the imaginary part is -b_sin (note the negative sign for the imaginary part)
```

## Orthogonality of Sinusoids at Fourier Frequencies

```python
n = 79
f = 5/n
t = np.arange(1, n+1)
cos_t = np.cos(2 * np.pi * f * t)
sin_t = np.sin(2 * np.pi * f * t)
plt.figure(figsize = (10, 6))
plt.plot(t, cos_t, '-o', label = 'Cosine')
plt.plot(t, sin_t, '-o', color = 'red', label = 'Sine')
plt.legend()
plt.show()
print(np.sum(cos_t)) #should be zero if f is a Fourier frequency
print(np.sum(sin_t)) #should be zero if f is a Fourier frequency
print(np.sum(cos_t ** 2)) #should equal n/2 if f is a Fourier frequency
print(np.sum(sin_t ** 2)) #should equal n/2 if f is a Fourier frequency
print(np.sum(cos_t * sin_t)) #should be zero if f is a Fourier frequency
```

```
8.43769498715119e-15
-2.809572282159702e-16
39.49999999999999
39.5
-4.388782419329049e-15
```

*(1 figure omitted — see the original notebook.)*

```python
f1 = 4/n
f2 = 5/n
cos_f1 = np.cos(2 * np.pi * f1 * t)
sin_f1 = np.sin(2 * np.pi * f1 * t)
cos_f2 = np.cos(2 * np.pi * f2 * t)
sin_f2 = np.sin(2 * np.pi * f2 * t)
plt.figure(figsize = (10, 6))
y1 = sin_f1
y2 = sin_f2
plt.plot(t, y1, '-o')
plt.plot(t, y2, '-o', color = 'red')
plt.show()
print(sum(y1 * y2)) #should equal zero if f1 and f2 are distinct Fourier frequencies
```

```
2.5743296383495824e-14
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (10, 6))
plt.scatter(y1, y2) #if f1 and f2 are distinct Fourier frequencies, there should be no linear trend in this scatter plot
```

```
<matplotlib.collections.PathCollection at 0x176ec28d0>
```

*(1 figure omitted — see the original notebook.)*

---

[← Fit on train only](09-fit-on-train-only.md) · [Up: contents](index.md)
