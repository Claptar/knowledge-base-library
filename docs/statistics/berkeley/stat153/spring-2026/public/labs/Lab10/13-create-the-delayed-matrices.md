---
title: Create the delayed matrices
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Create the delayed matrices

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

## FILL IN
delay_min = ... # Could have this be a negative number (in class we had this =0)
delay_max = ...  # positive number for sound leading the neural response (in class we had =0.4)

delays = np.arange(np.floor(delay_min*fs), np.ceil(delay_max*fs), dtype=int)
print(delays)

print('Creating delayed training set matrix')
xtraind = make_delayed(xtrain[stim_type], delays)

print('Creating delayed test set matrix')
xtestd = make_delayed(xtest[stim_type], delays)

print(f'Training set is {xtrain[stim_type].shape[0]} time points by {xtraind.shape[1]} features')
print(f'Test set is {xtest[stim_type].shape[0]} time points by {xtestd.shape[1]} features')

print(f'{xtraind.shape[1]} features should be # original features {xtrain[stim_type].shape[1]} x # delays {len(delays)}')
print(xtraind.shape[1] == xtrain[stim_type].shape[1]*len(delays))
```

## Look at delayed stimulus matrix

Here I'll plot only a subset of the delayed matrix so you can see its structure. Again, this is transposed so that time is on the x axis. Red lines are shown so you can appreciate the small shifts of the matrices as a function of delay.

```python
fig, axes = plt.subplots(figsize=(10,3))
plt.imshow(xtraind[0:4000,:].T, cmap = cm.magma, aspect='auto', interpolation='nearest')
plt.gca().xaxis.grid(color='w')
plt.xlabel('Time bin')
plt.ylabel('Feature x delay')
```

## Problems with OLS

In class we looked at the OLS solution and saw that the beta weights were very speckly and difficult to interpret. Here we will instead use ridge regression, which helps deal with our correlated predictors.

```python

---

[← Average |CCF| across features, then show per-electrode traces + mean](12-average-ccf-across-features-then-show-per-electrode-traces-m.md) · [Up: contents](index.md) · [For logging compute times, debug messages →](14-for-logging-compute-times-debug-messages.md)
