---
title: Heart Rate Variability
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab9.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab9.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab9.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Heart Rate Variability

In this notebook we'll work through a third dataset on Heart Rate Variability to add to what we discussed in class (see Lecture18.ipynb notebook).

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import warnings
warnings.filterwarnings('ignore')

# statsmodels imports
import statsmodels.api as sm
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

import warnings
from statsmodels.tools.sm_exceptions import ConvergenceWarning
warnings.filterwarnings('ignore', category=ConvergenceWarning)

plt.rcParams.update({
    'figure.figsize': (12, 4),
    'axes.spines.top': False,
    'axes.spines.right': False,
    'font.size': 16,
})
```

Heart rate variability (HRV) — the beat-to-beat fluctuation in your heart's rhythm — is a widely studied biosignal. The RR interval series (time between consecutive heartbeats) reflects a mix of:

- **Autonomic feedback loops** (sympathetic/parasympathetic regulation, which could be modeled like an AR component)
- **Respiratory and other short-lived perturbations** (breathing, posture changes, which could cause MA-like shocks)

This mix makes HRV a natural ARMA process. Let's see it in action.

We'll use data from the **MIT-BIH Normal Sinus Rhythm Database** on PhysioNet. We can get this from the package [WFDB (Waveform Database)](https://www.physionet.org/content/wfdb/10.7.0/)

```python
# Heart Rate Variability - RR intervals
!pip install wfdb

import wfdb
# MIT-BIH Normal Sinus Rhythm Database, record 16265
record = wfdb.rdrecord('16265', pn_dir='nsrdb/', channels=[0],
                       sampfrom=0, sampto=128*600)  # ~10 min at 128 Hz
ecg = record.p_signal[:, 0]

# First we will plot the original ECG waveform. We will use this to measure
# the heart rate variability by finding peaks in the signal (the R wave - which
# is the first upward deflection in the ECG time series.)
timepts = np.linspace(0,600,128*600)
plt.plot(timepts[1:1000], ecg[1:1000])
plt.xlabel('Time (s)')
```

Next we will detect R-peaks in this ECG waveform and find their intervals.

```python
# Detect R-peaks
from scipy.signal import find_peaks

peaks, _ = find_peaks(ecg, distance=int(0.5*128), height=0.5)
rr_intervals = np.diff(peaks) / 128.0 * 1000  # in ms
hrv_data = rr_intervals
data_source = "PhysioNet MIT-BIH Normal Sinus Rhythm DB (record 16265)"

print(f"Data source: {data_source}")
print(f"Number of RR intervals: {len(hrv_data)}")
print(f"Mean RR: {np.mean(hrv_data):.1f} ms ({60000/np.mean(hrv_data):.0f} bpm)")
print(f"SDNN: {np.std(hrv_data):.1f} ms")

fig, axes = plt.subplots(2, 1, figsize=(14, 6))

axes[0].plot(hrv_data, linewidth=0.6)
axes[0].set(xlabel='Beat number', ylabel='RR interval (ms)',
            title='RR Interval Time Series (Heart Rate Variability)')

# Also show a zoomed window
window = slice(700, 900)
axes[1].plot(np.arange(700, 900), hrv_data[window], 'o-', markersize=3, linewidth=0.8)
axes[1].set(xlabel='Beat number', ylabel='RR interval (ms)',
            title='Zoomed: beats 700-900')

plt.tight_layout()
plt.show()
```

### Predict (discussion)

Let's think about the structure of this time series. Discuss with a partner:

1. **Look at the zoomed plot.** Do you see features that look like slow drifts (AR) *and* sudden jumps (MA)?
2. **Predict the ACF shape.** Will it look like sunspots (oscillatory decay)? Gas prices (monotone decay)? Something else?
3. **Predict the PACF.** Will it cut off cleanly?

```python
# Demean for stationarity
y_hrv = hrv_data - np.mean(hrv_data)

fig, axes = plt.subplots(1, 2, figsize=(14, 4))

plot_acf(y_hrv, lags=40, ax=axes[0], title='ACF — HRV (RR intervals)')
plot_pacf(y_hrv, lags=40, ax=axes[1], title='PACF — HRV (RR intervals)', method='ywm')

plt.tight_layout()
plt.show()
```

### More predictions

Now having seen the ACF and the PACF, what is your best guess for the model? AR(p)? MA(q)? ARMA(p,q)? What orders?

## Results

The ACF decays but not as cleanly as pure AR would predict. The PACF doesn't cut off cleanly either, so this doesn't seem to be a pure AR *or* MA process.

This is what you might expect from ARMA. When you see gradual ACF decay *and* a messy PACF that doesn't cut off cleanly after a certain number of lags, the data likely has both autoregressive feedback and moving-average shock structure.

Let's try each of the models as before.

## AR vs MA vs ARMA

Here we will compare several AR, MA, and ARMA models of various orders. We will use the very naive split that we showed in class, where we will just try to predict the last `t` samples.

```python
t = 10 # Let's try and predict the last t samples

# Split our data into training and test data
y_train = y_hrv[:-t]
y_test = y_hrv[-t:]

print(f"Train: {len(y_train)} obs, Test: {len(y_test)} obs")

models_to_test = {
    'AR(1)':     (1, 0, 0),
    'AR(2)':     (2, 0, 0),
    'AR(3)':     (3, 0, 0),
    'AR(4)':     (4, 0, 0),
    'MA(1)':     (0, 0, 1),
    'MA(2)':     (0, 0, 2),
    'MA(4)':     (0, 0, 4),
    'ARMA(1,1)': (1, 0, 1),
    'ARMA(2,1)': (2, 0, 1),
    'ARMA(3,1)': (3, 0, 1),
}

results = {}
for name, order in models_to_test.items():
    model = ARIMA(y_train, order=order).fit()
    forecasts = model.forecast(steps=len(y_test))
    errors = y_test - forecasts
    results[name] = {
        'rmse': np.sqrt(np.mean(errors**2)),
        'mae': np.mean(np.abs(errors)),
        'forecasts': forecasts,
        'errors': errors,
    }
    print(f"{name:<12} RMSE={results[name]['rmse']:.5f}")
```

## Question:

* What do you notice about these models?
* Which is the best in terms of RMSE?
* Does this depend on your train/test split? Try different values of t and see what you find

```python
fig, axes = plt.subplots(len(results), 1, figsize=(14, 2 * len(results)), sharex=True)

split_point = len(y_train)

for ax, (name, res) in zip(axes, results.items()):
    # Training data
    ax.plot(np.arange(len(y_train)), y_train, 'k-', linewidth=0.4, alpha=0.5, label='Train')
    # Test actual
    ax.plot(np.arange(split_point, split_point + len(y_test)), y_test, 'k-', linewidth=0.8, label='Actual')
    # Forecast
    ax.plot(np.arange(split_point, split_point + len(y_test)), res['forecasts'], 'r--', linewidth=1.2, label=f'{name} forecast')
    # Split line
    ax.axvline(split_point, color='orange', linewidth=1.5, linestyle=':', label='Train/Test split')
    ax.set(ylabel='RR interval', title=f'{name}  |  RMSE={res["rmse"]:.5f}')
    ax.legend(loc='upper left')
    ax.set_xlim(600,1000)

axes[-1].set(xlabel='Time index')
plt.tight_layout()
plt.show()
```

---

[Up: contents](index.md) · [Model parameter counts →](02-model-parameter-counts.md)
