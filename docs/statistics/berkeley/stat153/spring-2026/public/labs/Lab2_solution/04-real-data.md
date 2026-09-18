---
title: Real data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab2_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

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

---

[← Autocovariance and Autocorrelation](03-autocovariance-and-autocorrelation.md) · [Up: contents](index.md) · [A Practical use of autocorrelation →](05-a-practical-use-of-autocorrelation.md)
