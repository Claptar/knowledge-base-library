---
title: Download S&P 500 data
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFourteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Download S&P 500 data

**Source:** [`CodeLectureFourteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFourteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

sp500 = yf.download('^GSPC', start='2000-01-01', end='2024-01-01', auto_adjust = True)

sp500_closeprice = sp500['Close'].to_numpy().flatten() #this is the daily closing price of the S&P 500 index

plt.figure(figsize=(12,6))
plt.plot(sp500_closeprice, label="Price")
plt.xlabel("Date")
plt.title("S&P 500 daily closing price")
plt.ylabel("Price (dollar)")
plt.legend()
plt.show()
```

```
[*********************100%***********************]  1 of 1 completed
```

*(1 figure omitted — see the original notebook.)*

Instead of working with the prices directly, we work with percentage daily returns.

```python
log_prices = np.log(sp500_closeprice)
y = 100 * np.diff(log_prices) #these are the percentage daily returns
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.title('SNP Daily Percentage Returns')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The plot above suggests that Model 2 might be useful for this dataset.

```python
alpha_opt_ridge = alpha_est_ridge(y, 40000000)
alpha_opt_lasso = alpha_est_lasso(y, 2000)
plt.figure(figsize = (12, 6))
plt.plot(alpha_opt_ridge, label = 'ridge')
plt.plot(alpha_opt_lasso, color = 'black', label = 'lasso')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting y^2 against tau^2
plt.figure(figsize = (12, 6))
plt.plot(y ** 2, label = 'Data', color = 'lightblue')
plt.plot(np.exp(2*alpha_opt_ridge), color = 'red', label = 'Ridge')
plt.plot(np.exp(2*alpha_opt_lasso), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
#Plotting log y^2 against log tau^2
plt.figure(figsize = (12, 6))
plt.plot(2*np.log(np.abs(y) + 1e-8), color = 'lightblue', label = 'Data') #small value added to np.abs(y) to prevent taking logs of zeros
plt.plot(np.log(np.exp(2*alpha_opt_ridge)), color = 'red', label = 'Ridge')
plt.plot(np.log(np.exp(2*alpha_opt_lasso)), color = 'black', label = 'LASSO')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Model THREE

We shall discuss a third model which is related to the previous two but is much more popular in many sciences and engineering. We shall refer to as the spectrum model. It is simply the variance model applied to the Discrete Fourier Transform (DFT) of the data. Before writing down the model, here is a motivating example.

### EEG Motor Movement Dataset

The following dataset was downloaded from https://physionet.org/content/eegmmidb/1.0.0/. The specific dataset details are here: https://physionet.org/content/eegmmidb/1.0.0/. The dataset consists of over 1500 one and two minute (64 channel) EEG recordings, obtained from 109 volunteers. We will pick data for just one subject (volunteer) and one of the EEG channels, and compare the data for eyes open vs eyes closed. A basic finding of cognitive neuroscience is that the power of occipital alpha-band (~10 Hz) brain waves is increased when peoples' eyes are closed, rather than open (see, for example, the paper titled "Occipital alpha-band brain waves when the eyes are closed are shaped by ongoing visual processes" by Hohaia et al 2022).

The mne python library is necessary for loading the data file.

```python
import mne
```

For each individual subject (here we are using the data for the first subject), there are 64 time series datasets for "open-eyes" and again 64 time series datasets for "closed-eyes". These 64 datasets correspond to the 64 channels which are different electrodes recording brain activity. We pick one of the channels, and compare the "open-eyes" and "closed-eyes" data.

```python
#This is the dataset for the eyes-open setting:
raw_1 = mne.io.read_raw_edf('S001R01.edf', preload = True)
print(raw_1.info)
data_1, times_1 = raw_1[:]

ch_index = 10  # pick a channel
#plt.figure(figsize=(12,6))
plt.plot(times_1, data_1[ch_index, :])
plt.title(f"Channel {ch_index}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.show()
```

```
Extracting EDF parameters from /Users/aditya/Dropbox/Berkeley Teaching/153-248 Fall 2025/S001R01.edf...
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
#Here is the dataset for the eyes closed setting.
raw_2 = mne.io.read_raw_edf('S001R02.edf', preload = True)
print(raw_2.info)
data_2, times_2 = raw_2[:]

#plt.figure(figsize=(12,6))
plt.plot(times_2, data_2[ch_index, :])
plt.title(f"Channel {ch_index}")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.show()
```

```
Extracting EDF parameters from /Users/aditya/Dropbox/Berkeley Teaching/153-248 Fall 2025/S001R02.edf...
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

There is a sampling rate associated with these datasets. This is the number of times per second that the data is obtained.

```python
sampling_rate_1 = raw_1.info['sfreq']
print("Sampling rate:", sampling_rate_1, "Hz")
sampling_rate_2 = raw_2.info['sfreq']
print("Sampling rate:", sampling_rate_2, "Hz")
sampling_rate = sampling_rate_1
```

```
Sampling rate: 160.0 Hz
Sampling rate: 160.0 Hz
```

The length of these time series is 9760 (see below). This corresponds to 160 observations per second, for a total of 61 seconds.

```python
print(times_1)
print(times_2)
n = len(times_1)
print(n, n/sampling_rate)
```

```
[0.000000e+00 6.250000e-03 1.250000e-02 ... 6.098125e+01 6.098750e+01
 6.099375e+01]
[0.000000e+00 6.250000e-03 1.250000e-02 ... 6.098125e+01 6.098750e+01
 6.099375e+01]
9760 61.0
```

Our two datasets are:

```python
y_o = data_1[ch_index, :]
y_c = data_2[ch_index, :]
```

Our main goal is to compare these two datasets and to highlight the main ways in which they are different.

```python
#fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (12, 6))
fig, axes = plt.subplots(nrows = 2, ncols = 1)

axes[0].plot(y_o)
axes[0].set_title('y_o')

axes[1].plot(y_c)
axes[1].set_title('y_c')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.plot(y_o, label = 'Eyes Open', color = 'gray')
plt.plot(y_c, label = 'Eyes Closed', color = 'blue')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is obviously very hard to articulate the differences between the two time series just by looking at their plots. For such datasets, the basic tool is the Periodogram. Recall that the periodogram is given by:
\begin{align*}
   I(j/n) := \frac{|b_j|^2}{n}
\end{align*}
where $b_j$ is given by the Discrete Fourier Transform. We plot the periodogram when $j/n$ lies between 0 and $1/2$.

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
n = len(y_o)
freqs, pgram_o = periodogram(y_o)
freqs, pgram_c = periodogram(y_c)
```

```python
fig, axes = plt.subplots(nrows = 2, ncols = 1)

axes[0].plot(freqs, pgram_o)
axes[0].set_title('Periodogram (eyes open)')

axes[1].plot(freqs, pgram_c)
axes[1].set_title('Periodogram (eyes closed)')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The differences are more apparent from the periodograms. To see them better, we plot the periodograms on the log-scale.

```python
fig, axes = plt.subplots(nrows = 2, ncols = 1)

axes[0].plot(freqs, np.log(pgram_o))
axes[0].set_title('Periodogram (eyes open)')

axes[1].plot(freqs, np.log(pgram_c))
axes[1].set_title('Periodogram (eyes closed)')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Below we plot the log-periodograms in the same plot.

```python

plt.plot(freqs, np.log(pgram_o), label = 'Eyes Open', color = 'blue')
plt.plot(freqs, np.log(pgram_c), label = 'Eyes Closed', color = 'gray')
plt.title('Log Periodograms')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

To visualize the differences better, we need to smooth the log-periodogram somehow. This is where our model 3 is helpful.

### Model 3 (Spectrum Model)

Model 3 is
\begin{equation*}
    \text{Re}(b_j), \text{Im}(b_j) \overset{\text{i.i.d}}{\sim} N(0, \gamma_j^2)
\end{equation*}
for $j = 1, \dots, m$ where $b_j$ is the $j^{th}$ DFT coefficient of the observed data $y_1, \dots, y_n$.

Likelihood in terms of the periodogram is:
\begin{equation*}
   \prod_{j=1}^m \frac{n}{\gamma_j^2} \exp \left(-\frac{n I(j/n)}{2 \gamma_j^2} \right)
\end{equation*}
Negative log-likelihood is
\begin{equation*}
  \sum_{j=1}^m \left(\frac{n I(j/n)}{2 \gamma_j^2} +  2 \log \gamma_j \right)
\end{equation*}
Letting $\alpha_j = \log \gamma_j$, we can rewrite the above as
\begin{equation*}
\sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right)
\end{equation*}
Minimizing this without any regularization on $\{\alpha_j\}$ leads to
\begin{equation*}
    \alpha_j = \log \sqrt{\frac{nI(j/n)}{2}} ~~ \text{ and } ~~ \gamma_j^2 = e^{2\alpha_j} = \frac{nI(j/n)}{2}
\end{equation*}
We will use regularization and estimate $\alpha_j$ (and $\gamma_j$) by minimizing:
\begin{equation*}
   \sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right)  + \lambda \sum_{j=2}^{m-1} \left((\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right)^2
\end{equation*}
or
\begin{equation*}
    \sum_{j=1}^m \left( \frac{nI(j/n)}{2} e^{-2 \alpha_j} + 2 \alpha_j \right) + \lambda \sum_{j=2}^{m-1} \left|(\alpha_{j+1} - \alpha_j) - (\alpha_j - \alpha_{j-1}) \right|.
\end{equation*}
Code for computing these estimators is given below. These functions (alpha_estimator_ridge and alpha_estimator_lasso) use $y$ and $\lambda$ as input. In the first step, one computes the periodogram $I(j/n)$ as the optimization is in terms of the periodogram. We apply these methods to the EEG dataset.

```python
def alpha_estimator_ridge(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)
    alpha = cp.Variable(m)
    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.square(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve(solver = cp.MOSEK)
    return alpha.value, freq

def alpha_estimator_lasso(y, lambda_val):
    freq, I = periodogram(y)
    m = len(freq)
    n = len(y)
    alpha = cp.Variable(m)
    neg_likelihood_term = cp.sum(cp.multiply((n * I / 2), cp.exp(-2 * alpha)) + 2*alpha)
    smoothness_penalty = cp.sum(cp.abs(alpha[2:] - 2 * alpha[1:-1] + alpha[:-2]))
    objective = cp.Minimize(neg_likelihood_term + lambda_val * smoothness_penalty)
    problem = cp.Problem(objective)
    problem.solve(solver = cp.MOSEK)
    return alpha.value, freq
```

We will now apply these estimators to each of the two datasets (eyes open and eyes closed). We compute estimates of $\alpha_j, j = 1, \dots, m$ and also compute the corresponding $2 \gamma_j^2/n$ (where $\gamma_j = \exp(\alpha_j)$). This quantity $2 \gamma_j^2/n$ equals the mean of $I(j/n)$ in our model $I(j/n) \sim \frac{\gamma_j^2}{n} \chi^2_2$.

```python
#Eyes Open
alpha_opt_ridge_o, freq = alpha_estimator_ridge(y_o, 50000000)
pgram_mean_ridge_o = (2/n)*(np.exp(2*alpha_opt_ridge_o))
alpha_opt_lasso_o, freq = alpha_estimator_lasso(y_o, 1000)
pgram_mean_lasso_o = (2/n)*(np.exp(2*alpha_opt_lasso_o))

#Eyes Closed
alpha_opt_ridge_c, freq = alpha_estimator_ridge(y_c, 50000000)
pgram_mean_ridge_c = (2/n)*(np.exp(2*alpha_opt_ridge_c))
alpha_opt_lasso_c, freq = alpha_estimator_lasso(y_c, 1000)
pgram_mean_lasso_c = (2/n)*(np.exp(2*alpha_opt_lasso_c))
```

Below we plot the periodogram and its mean $2 \gamma_j^2/n$ both on log-scale.

```python
fig, axes = plt.subplots(1, 2, sharey=True)

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [----- Left subplot: Eyes Open ----- →](03-------left-subplot-eyes-open.md)
