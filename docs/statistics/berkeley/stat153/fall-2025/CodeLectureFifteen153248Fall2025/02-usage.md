---
title: Usage
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFifteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Usage

**Source:** [`CodeLectureFifteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

df_soi = load_soi_data("soi_monthly.txt")
print(df_soi)
```

```
SOI
Date
1876-01-01  11.3
1876-02-01  11.0
1876-03-01   0.2
1876-04-01   9.4
1876-05-01   6.8
...          ...
2024-10-01   4.2
2024-11-01   6.5
2024-12-01  10.8
2025-01-01   3.7
2025-02-01   3.0

[1790 rows x 1 columns]
```

```python
y = df_soi['SOI']
n = len(y)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

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

```python
alpha_opt_ridge, freq = spectrum_estimator_ridge(y, 50000)
power_ridge = (2/n)*(np.exp(2*alpha_opt_ridge))
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 100)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(freq, pgram, linefmt = 'lightblue', basefmt = '')
markerline.set_marker("None")
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, power_ridge, color = 'red', label = 'Ridge')
plt.plot(freq, power_lasso, color = 'black', label = "LASSO")
plt.legend()
plt.show()
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

```python
from scipy.signal import find_peaks

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Find peaks →](03-find-peaks.md)
