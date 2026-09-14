---
title: Find peaks
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFifteen153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureFifteen153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Find peaks

**Source:** [`CodeLectureFifteen153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureFifteen153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

### Application Four: EEG Motor Movement Dataset

The following dataset was downloaded from https://physionet.org/content/eegmmidb/1.0.0/. The specific dataset details are here: https://physionet.org/content/eegmmidb/1.0.0/. The dataset consists of over 1500 one and two minute (64 channel) EEG recordings, obtained from 109 volunteers. We will pick data for just one subject (volunteer) and one of the EEG channels, and compare the data for eyes open vs eyes closed. A basic finding of cognitive neuroscience is that the power of occipital alpha-band (~10 Hz) brain waves is increased when peoples' eyes are closed, rather than open (see, for example, the paper titled "Occipital alpha-band brain waves when the eyes are closed are shaped by ongoing visual processes" by Hohaia et al 2022).

The mne python library is necessary for loading the data file.

```python
import mne
```

For each individual subject (here we are using the data for the first subject), there are 64 time series datasets for "open-eyes" and again 64 time series datasets for "closed-eyes". These 64 datasets correspond to the 64 channels which are different electrodes recording brain activity. We pick one of the channels, and compare the "open-eyes" and "closed-eyes" data.

```python
raw_1 = mne.io.read_raw_edf('S001R01.edf', preload = True)
print(raw_1.info)
data_1, times_1 = raw_1[:]

ch_index = 10  # pick a channel
plt.figure(figsize=(12,6))
plt.plot(times_1, data_1[ch_index, :])
plt.title(f"Channel {ch_index}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.show()
```

```
Extracting EDF parameters from /Users/aditya/Dropbox/Berkeley Teaching/153-248 Spring 2025/S001R01.edf...
EDF file detected
Setting channel info structure...
Creating raw.info structure...
Reading 0 ... 9759  =      0.000 ...    60.994 secs...
<Info | 8 non-empty values
 bads: []
 ch_names: Fc5., Fc3., Fc1., Fcz., Fc2., Fc4., Fc6., C5.., C3.., C1.., ...
 chs: 64 EEG
 custom_ref_applied: False
 highpass: 0.0 Hz
 lowpass: 80.0 Hz
 meas_date: 2009-08-12 16:15:00 UTC
 nchan: 64
 projs: []
 sfreq: 160.0 Hz
 subject_info: <subject_info | his_id: X, sex: 0, last_name: X>
>
```

*(1 figure omitted — see the original notebook.)*

```python
raw_2 = mne.io.read_raw_edf('S001R02.edf', preload = True)
print(raw_2.info)
data_2, times_2 = raw_2[:]

plt.figure(figsize=(12,6))
plt.plot(times_2, data_2[ch_index, :])
plt.title(f"Channel {ch_index}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.show()
```

```
Extracting EDF parameters from /Users/aditya/Dropbox/Berkeley Teaching/153-248 Spring 2025/S001R02.edf...
EDF file detected
Setting channel info structure...
Creating raw.info structure...
Reading 0 ... 9759  =      0.000 ...    60.994 secs...
<Info | 8 non-empty values
 bads: []
 ch_names: Fc5., Fc3., Fc1., Fcz., Fc2., Fc4., Fc6., C5.., C3.., C1.., ...
 chs: 64 EEG
 custom_ref_applied: False
 highpass: 0.0 Hz
 lowpass: 80.0 Hz
 meas_date: 2009-08-12 16:15:00 UTC
 nchan: 64
 projs: []
 sfreq: 160.0 Hz
 subject_info: <subject_info | his_id: X, sex: 0, last_name: X>
>
```

*(1 figure omitted — see the original notebook.)*

```python
#Let us check if the time series are equally spaced
print(np.diff(times_1))
print(np.diff(times_2))
#Let us check if the lengths of the two time series ('open eyes' and 'closed eyes') are the same
print(len(times_1))
print(len(times_2))
```

```
[0.00625 0.00625 0.00625 ... 0.00625 0.00625 0.00625]
[0.00625 0.00625 0.00625 ... 0.00625 0.00625 0.00625]
9760
9760
```

```python
y_o = data_1[ch_index, :]
y_c = data_2[ch_index, :]
```

```python
fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))

axes[0].plot(y_o)
axes[0].set_title('y_o')

axes[1].plot(y_c)
axes[1].set_title('y_c')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
n = len(y_o)
freqs, pgram_o = periodogram(y_o)
alpha_opt_ridge_o, freq = spectrum_estimator_ridge(y_o, 1000000)
pgram_mean_ridge_o = (2/n)*(np.exp(2*alpha_opt_ridge_o))
alpha_opt_lasso_o, freq = spectrum_estimator_lasso(y_o, 1000)
pgram_mean_lasso_o = (2/n)*(np.exp(2*alpha_opt_lasso_o))
```

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram_o), color = 'lightblue', label = 'Periodogram')
#plt.plot(freqs, np.log(pgram_cl), color = 'None', label = 'Periodogram')
plt.title('Log Periodogram (Eyes Open)')
plt.plot(freqs, np.log(pgram_mean_ridge_o), color = 'red', label = 'Ridge')
plt.plot(freqs, np.log(pgram_mean_lasso_o), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
n = len(y_c)
freqs, pgram_c = periodogram(y_c)
alpha_opt_ridge_c, freq = spectrum_estimator_ridge(y_c, 1000000)
pgram_mean_ridge_c = (2/n)*(np.exp(2*alpha_opt_ridge_c))
alpha_opt_lasso_c, freq = spectrum_estimator_lasso(y_c, 1000)
pgram_mean_lasso_c = (2/n)*(np.exp(2*alpha_opt_lasso_c))
```

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram_c), color = 'lightblue', label = 'Periodogram')
#plt.plot(freqs, np.log(pgram_cl), color = 'None', label = 'Periodogram')
plt.title('Log Periodogram (Eyes Closed)')
plt.plot(freqs, np.log(pgram_mean_ridge_c), color = 'red', label = 'Ridge')
plt.plot(freqs, np.log(pgram_mean_lasso_c), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram_mean_lasso_o), color = 'black', label = 'Open')
plt.plot(freqs, np.log(pgram_mean_lasso_c), color = 'red', label = 'Closed')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
sampling_rate = raw_1.info['sfreq']
print("Sampling rate:", sampling_rate, "Hz")
```

```
Sampling rate: 160.0 Hz
```

```python
from scipy.signal import find_peaks

---

[← Usage](02-usage.md) · [Up: contents](index.md) · [Find peaks →](04-find-peaks.md)
