---
title: Autocorrelation of random walk with drift
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Autocorrelation of random walk with drift

**Source:** [`public/labs/Lab2_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Now try plotting the autocorrelation for the random walk with drift, generating several examples of the random walk time series. What do you notice? Is it stationary? What changes if you change the scale of the drift (positive, negative, zero, large, small)?

```python
nt = 100
rwd = random_walk_drift(nt, drift=0.01)
plot_acf(rwd, lags=len(rwd)-1);
plt.xlabel('Lags')
plt.ylabel('Autocorrelation')
```

```
Text(0, 0.5, 'Autocorrelation')
```

*(1 figure omitted — see the original notebook.)*

# Real data

We have some examples below from the `astsa` package of real data shown in the Shumway and Stoffer textbook. Try plotting the autocorrelation of these real datasets (or choose others that interest you!). What do you notice about the stationarity of the time series, and about the relationship between the autocorrelation and autocovariance?

First we'll print the list of potential datasets from `astsa` again -- these start with the word `load_`

```python
dir(astsa.datasets)
```

```
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'load_EQ5',
 'load_EXP6',
 'load_Hare',
 'load_Lynx',
 'load_chicken',
 'load_djia',
 'load_fmri1',
 'load_gtemp_land',
 'load_gtemp_ocean',
 'load_jj',
 'load_rec',
 'load_soi',
 'load_speech',
 'load_sunspotz',
 'utils']
```

```python
# Let's try the fMRI data

fmri_data = astsa.load_fmri1()
fmri_data
```

```
time  cort1  cort2  cort3  cort4  thal1  thal2  cere1  cere2
0       1 -0.336 -0.088 -0.579 -0.221 -0.222 -0.046 -0.354 -0.028
1       2 -0.192 -0.359 -0.475 -0.058  0.072 -0.039 -0.346 -0.032
2       3  0.062  0.062  0.063  0.192  0.145 -0.256 -0.337  0.272
3       4  0.128  0.221  0.234 -0.004 -0.104 -0.030  0.149  0.042
4       5  0.358  0.199  0.388  0.255  0.035 -0.081  0.311 -0.080
..    ...    ...    ...    ...    ...    ...    ...    ...    ...
123   124 -0.500 -0.306 -0.279 -0.040 -0.166  0.211 -0.006 -0.191
124   125 -0.443 -0.213 -0.456 -0.103 -0.230  0.156 -0.124 -0.103
125   126 -0.497 -0.526 -0.457  0.376 -0.170  0.126 -0.087 -0.253
126   127 -0.401 -0.081 -0.294 -0.016 -0.186  0.047 -0.081 -0.398
127   128 -0.419 -0.199 -0.394  0.222 -0.044  0.049 -0.031 -0.367

[128 rows x 9 columns]
```

```python
# Let's also load the hare and lynx datasets

hare_data = astsa.load_Hare()
lynx_data = astsa.load_Lynx()

print(hare_data)
print(lynx_data)
```

```
Time  Value
0   1845  19.58
1   1846  19.60
2   1847  19.61
3   1848  11.99
4   1849  28.04
..   ...    ...
86  1931  19.52
87  1932  82.11
88  1933  89.76
89  1934  81.66
90  1935  15.76

[91 rows x 2 columns]
    Time  Value
0   1845  30.09
1   1846  45.15
2   1847  49.15
3   1848  39.52
4   1849  21.23
..   ...    ...
86  1931   8.31
87  1932  16.01
88  1933  24.82
89  1934  29.70
90  1935  35.40

[91 rows x 2 columns]
```

```python
# Now let's look at the autcorrelation function of the fMRI data from a particular region ('thal2')
# We'll also try applying a moving average to our fMRI data, with a window length of 11
region = 'thal2'
win = 11
ma_fmri = moving_average(fmri_data[region], n=win)


plt.figure(figsize=(10,3))
plt.subplot(1,3,1)
plt.plot(fmri_data[region], label='original fMRI data')
plt.plot(ma_fmri, label='smoothed fMRI data')
plt.legend()

plt.subplot(1,3,2)
plot_acf(fmri_data[region], lags=60, ax=plt.gca())
plt.gca().axis('tight')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')

plt.subplot(1,3,3)
plot_acf(ma_fmri[~np.isnan(ma_fmri)], lags=60, ax=plt.gca(), color='orange', vlines_kwargs={'color': 'orange'}, );
plt.gca().axis('tight')
plt.title('Autocorrelation for smoothed data')
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
```

```
Text(0, 0.5, 'Autocorrelation')
```

*(1 figure omitted — see the original notebook.)*

What happens to the autocorrelation of these data after smoothing? Try it for other brain areas - any of the column names for the fmri_data dataset should work (see cell above when we printed it).

```python
# Now try this for the hare and lynx dataset. We will look at the cross-correlation of these datasets later.

plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.plot(hare_data['Value'])
plt.xlabel('Time point')
plt.ylabel('Value')
plt.ylabel('Hare pelts')
plt.title('Hare data')

plt.subplot(2,2,2)
plot_acf(hare_data['Value'], lags=len(hare_data['Value'])-1, ax=plt.gca());
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('ACF - Hare')

plt.subplot(2,2,3)
plt.plot(lynx_data['Value'])
plt.xlabel('Time point')
plt.ylabel('Lynx pelts')
plt.title('Lynx data')

plt.subplot(2,2,4)
plot_acf(lynx_data['Value'], lags=len(hare_data['Value'])-1, ax=plt.gca());
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('ACF - Lynx');

plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

# A Practical use of autocorrelation

Finally, let's try this for the speech dataset. Here, the autocorrelation function can be used to calculate the pitch of the person's voice, if we express the time lags in seconds rather than in samples. Here, we know that the sampling rate of the speech data was 10000 Hz (given in your book).

We can look for peaks in the autocorrelation function, and large peaks outsize of `lag=0` correspond to the pitch period and multiples of the pitch period (its harmonics).

```python
speech_data = astsa.load_speech()
sampling_rate = 10000 # This is the sampling rate of the speech data in samples per sec (Hz), according to SS
t = (speech_data['Time']-1)/sampling_rate # Subtract 1 so time series starts from 0 seconds

speech_acf = acf(speech_data['Value'], nlags=250)
plot_acf(speech_data['Value'], lags=250);
plt.gca().set_xticks(np.arange(251,step=50), labels=[t[a] for a in np.arange(251,step=50)]);
plt.xlabel('Time (s)')

# It looks like there is a large peak around t=0.01 seconds (and tellingly, another
# around t=0.02 seconds, which is a multiple. t=0.01 seconds is the pitch period,
# but typically we convert this to a frequency by dividing 1 second by this amount:
print(f'The pitch is approximately {1/0.01} Hz')

# We could use a function like `scipy.signal.findpeaks` to do this more accurately,
# but for now that is beyond the scope of the lab (you can try to implement yourself!)
```

```
The pitch is approximately 100.0 Hz
```

*(1 figure omitted — see the original notebook.)*

# Cross-covariance and cross-correlation

Many times, we don't just want to describe the relationship between time points in the same series, we want to describe the relationship between multiple time series. For example, how does the time course of reported cases of a disease relate to time course of reported deaths? How do the numbers of lynx and hare pelts relate to each other in our prior example?

In this case, we can use cross-correlation (or look at cross-covariance) of the two time series.

```python
#plot_ccf(lynx_data['Value'], hare_data['Value'], lags=len(lynx_data['Value'])-1, negative_lags=True)

x = lynx_data['Value'].values
y = hare_data['Value'].values

max_lag = 30   # Let's choose some value here explicitly

# Positive lags: lynx data leads hare data
ccf_xy = ccf(x, y, adjusted=False)[:max_lag+1]

# Negative lags: hare data leads lynx data
ccf_yx = ccf(y, x, adjusted=False)[:max_lag+1]

# Build symmetric lag axis
lags = np.arange(-max_lag, max_lag+1)

# Combine (exclude duplicate lag 0)
ccf_full = np.r_[ccf_yx[1:][::-1], ccf_xy]

plt.stem(lags, ccf_full)
plt.axvline(0, color='r')
plt.xlabel('Lag')
plt.ylabel('CCF')
plt.title('positive: lynx leads hare, negative: hare leads lynx');
plt.grid()
```

*(1 figure omitted — see the original notebook.)*

# Interpreting cross correlation

One point of caution is that with these real data examples presented here, they are not usually weakly stationary, so interpreting the cross-correlation analysis can be problematic. In the future, we will use other tools such as prewhitening, and detrending to help before we run the cross-correlation analysis. See Example 1.29 and 1.30 in your book (SS pages 34-35) to read more about this.

---

[← Autocorrelation of moving average](02-autocorrelation-of-moving-average.md) · [Up: contents](index.md)
