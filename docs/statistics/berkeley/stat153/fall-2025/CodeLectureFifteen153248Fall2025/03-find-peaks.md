---
title: Find peaks
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFifteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLectureFifteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

peaks, _ = find_peaks(np.log(power_ridge))
print("Peaks:", peaks)
print(1/freq[peaks])
```

```
Peaks: [ 33 186 257 318 423 560 631 710 782 857]
[52.64705882  9.57219251  6.9379845   5.61128527  4.22169811  3.19073084
  2.83227848  2.51758087  2.28607918  2.08624709]
```

The peak therefore corresponds to the period of about 52.64 months, which is about 4.5 years.

### Application Three: Quake Vibration Dataset

This dataset is from the Mathworks (MATLAB) tutorial "Practical Introduction to Frequency-Domain Analysis" (see [this link](https://www.mathworks.com/help/signal/ug/practical-introduction-to-frequency-domain-analysis.html)). From this matlab tutorial: *Active Mass Driver (AMD) control systems are used to reduce vibration in a building under an earthquake. An active mass driver is placed on the top floor of the building and, based on displacement and acceleration measurements of the building floors, a control system sends signals to the driver so that the mass moves to attenuate ground disturbances. Acceleration measurements were recorded on the first floor of a three story test structure under earthquake conditions. Measurements were taken without the active mass driver control system (open loop condition), and with the active control system (closed loop condition).*

```python
from scipy.io import loadmat
mat_dict = loadmat('quakevibration.mat')
print(mat_dict.keys())
```

```
dict_keys(['__header__', '__version__', '__globals__', 'gfloor1OL', 'gfloor1CL'])
```

```python
gfloor1OL_array = mat_dict['gfloor1OL']
gfloor1CL_array = mat_dict['gfloor1CL']
print(gfloor1OL_array.shape)
print(gfloor1CL_array.shape)
```

```
(10000, 1)
(10000, 1)
```

```python
y_ol = gfloor1OL_array.ravel()
y_cl = gfloor1CL_array.ravel()
```

```python
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))

axes[0].plot(y_ol)
axes[0].set_title('y_ol')

axes[1].plot(y_cl)
axes[1].set_title('y_cl')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
n = len(y_ol)
freqs, pgram_ol = periodogram(y_ol)
alpha_opt_ridge_ol, freq = spectrum_estimator_ridge(y_ol, 100000)
pgram_mean_ridge_ol = (2/n)*(np.exp(2*alpha_opt_ridge_ol))
alpha_opt_lasso_ol, freq = spectrum_estimator_lasso(y_ol, 1000)
pgram_mean_lasso_ol = (2/n)*(np.exp(2*alpha_opt_lasso_ol))
```

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, (pgram_ol), color = 'lightblue', label = 'Periodogram')
#plt.plot(freqs, np.log(pgram_ol), color = 'None', label = 'Periodogram')
plt.title('Periodogram (OL)')
plt.plot(freqs, (pgram_mean_ridge_ol), color = 'red', label = 'Ridge')
plt.plot(freqs, (pgram_mean_lasso_ol), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram_ol), color = 'lightblue', label = 'Periodogram')
#plt.plot(freqs, np.log(pgram_ol), color = 'None', label = 'Periodogram')
plt.title('Periodogram (OL)')
plt.plot(freqs, np.log(pgram_mean_ridge_ol), color = 'red', label = 'Ridge')
plt.plot(freqs, np.log(pgram_mean_lasso_ol), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
n = len(y_cl)
freqs, pgram_cl = periodogram(y_cl)
alpha_opt_ridge_cl, freq = spectrum_estimator_ridge(y_cl, 100000)
pgram_mean_ridge_cl = (2/n)*(np.exp(2*alpha_opt_ridge_cl))
alpha_opt_lasso_cl, freq = spectrum_estimator_lasso(y_cl, 1000)
pgram_mean_lasso_cl = (2/n)*(np.exp(2*alpha_opt_lasso_cl))
```

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, (pgram_cl), color = 'lightblue', label = 'Periodogram')
#plt.plot(freqs, np.log(pgram_cl), color = 'None', label = 'Periodogram')
plt.title('Periodogram (CL)')
plt.plot(freqs, (pgram_mean_ridge_cl), color = 'red', label = 'Ridge')
plt.plot(freqs, (pgram_mean_lasso_cl), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram_cl), color = 'lightblue', label = 'Periodogram')
#plt.plot(freqs, np.log(pgram_cl), color = 'None', label = 'Periodogram')
plt.title('Periodogram (CL)')
plt.plot(freqs, np.log(pgram_mean_ridge_cl), color = 'red', label = 'Ridge')
plt.plot(freqs, np.log(pgram_mean_lasso_cl), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram_mean_lasso_ol), color = 'black', label = 'OL')
plt.plot(freqs, np.log(pgram_mean_lasso_cl), color = 'red', label = 'CL')
plt.legend()
plt.title('Log Power Spectral Density')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

There are three loops on the open loop spectrum and two on the closed loop spectrum. The control system reduces the overall power of the vibrations and gets rid of one harmonic component. In other words, the control system not only reduces the vibration but also brings it closer to a sinusoid.

The main point is that the differences between the two time series is much better summarized using their power spectra, compared to the raw data.

### Application Four: FRED dataset

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

---

[← Usage](02-usage.md) · [Up: contents](index.md) · [Find peaks →](04-find-peaks.md)
