---
title: Real data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab2.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Real data

We have some examples below from the `astsa` package of real data shown in the Shumway and Stoffer textbook. Try plotting the autocorrelation of these real datasets (or choose others that interest you!). What do you notice about the stationarity of the time series, and about the relationship between the autocorrelation and autocovariance?

First we'll print the list of potential datasets from `astsa` again -- these start with the word `load_`

```python
dir(astsa.datasets)
```

```python
# Let's try the fMRI data

fmri_data = astsa.load_fmri1()
fmri_data
```

```python
# Let's also load the hare and lynx datasets

hare_data = astsa.load_Hare()
lynx_data = astsa.load_Lynx()

print(hare_data)
print(lynx_data)
```

```python
# Now let's look at the autcorrelation function of the fMRI data from a particular region ('thal2')
# We'll also try applying a moving average to our fMRI data, with a window length of 11
region = 'thal2'
win = 11

# Apply the moving average function to the fMRI data:
ma_fmri = # FILL IN


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

---

[← Autocovariance and Autocorrelation](03-autocovariance-and-autocorrelation.md) · [Up: contents](index.md) · [A practical use of autocorrelation →](05-a-practical-use-of-autocorrelation.md)
