---
title: 'Application Four: FRED dataset'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFifteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureFifteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Application Four: FRED dataset

The following datset is FRED's "Industrial Production: Total Index" dataset. It is a monthly dataset $I_t$ that is **not** seasonally adjusted.

```python
prod_index = pd.read_csv("IPB50001N-06March2025FRED.csv")
print(prod_index.head(10))
pind = prod_index['IPB50001N']
plt.figure(figsize = (12, 6))
plt.plot(pind)
plt.show()
```

```
observation_date  IPB50001N
0       1919-01-01     4.7841
1       1919-02-01     4.5959
2       1919-03-01     4.4884
3       1919-04-01     4.5691
4       1919-05-01     4.7035
5       1919-06-01     4.9991
6       1919-07-01     5.1604
7       1919-08-01     5.2679
8       1919-09-01     5.2947
9       1919-10-01     5.2679
```

*(1 figure omitted — see the original notebook.)*

The data has an increasing trend so it does not make sense to use the spectrum model directly here. Instead, let us work with the annual growth rates:
\begin{equation*}
   y_t = 100 \left(\log I_t - \log I_{t-12} \right)
\end{equation*}

```python
pind = prod_index['IPB50001N']
pind = pind.to_numpy()
y = 100*(np.log(pind[12:]) - np.log(pind[:-12]))
plt.plot(y)
n = len(y)
print(n) #now n is odd
plt.show()
```

```
1261
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
plt.plot(freqs, np.log(pgram))
plt.title('Log Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
alpha_opt_ridge, freq = spectrum_estimator_ridge(y, 5000)
power_ridge = (2/n)*(np.exp(2*alpha_opt_ridge))
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 100)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

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
# Find peaks
peaks, _ = find_peaks(np.log(power_ridge))
print("Peaks:", peaks)
print(freq[peaks])
print(1/freq[peaks])
```

```
Peaks: [ 27 140 248 266 358 458 484 577]
[0.0222046  0.11181602 0.19746233 0.21173672 0.28469469 0.36399683
 0.38461538 0.45836638]
[45.03571429  8.94326241  5.06425703  4.72284644  3.51253482  2.74727669
  2.6         2.1816609 ]
```

Economists use this as evidence for existence of a business cycle with period around 45 months (which is close to 4 years). See Section 6.4 for the Hamilton book on time series for more on this example.

---

[← Application Three: Quake Vibration Dataset](03-application-three-quake-vibration-dataset.md) · [Up: contents](index.md)
