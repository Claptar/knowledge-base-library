---
title: Find peaks
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureThirteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLectureThirteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureThirteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

### Example Two

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

### Example Three

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

### Example Four

Here we take $\tau_j^2$ to be peaked for $j/n$ which is close to 11.

```python
#the following tau_j^2 is peaked around j/n = 1/11 and then drops quickly as j/n moves away from 1/11
j_vals = np.arange(m)

---

[← Find peaks](02-find-peaks.md) · [Up: contents](index.md) · [Define the peak position and width (smaller width makes it drop quickly) →](04-define-the-peak-position-and-width-smaller-width-makes-it-dr.md)
