---
title: Create the delayed matrices
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Create the delayed matrices

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

delay_min = 0 # Could have this be a negative number
delay_max = 0.4  # positive number for sound leading the neural response
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

```
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
Creating delayed training set matrix
Creating delayed test set matrix
Training set is 161034 time points by 3200 features
Test set is 13563 time points by 3200 features
3200 features should be # original features 80 x # delays 40
True
```

## Look at delayed stimulus matrix

Here I'll plot only a subset of the delayed matrix so you can see its structure. Again, this is transposed so that time is on the x axis. Red lines are shown so you can appreciate the small shifts of the matrices as a function of delay.

```python
fig, axes = plt.subplots(figsize=(10,6))
plt.imshow(xtraind[0:4000,:].T, cmap = cm.magma, aspect='auto', interpolation='nearest')
plt.gca().xaxis.grid(color='w')
plt.xlabel('Time bin')
plt.ylabel('Feature x delay')
```

```
Text(0, 0.5, 'Feature x delay')
```

*(1 figure omitted — see the original notebook.)*

## Covariance matrix

In most STRF analyses, we must normalize by autocorrelations in the stimulus (frequencies that always appear together, or temporal correlations that occur as a result of smoothly varying signals).  We do this by calculating the covariance of the delayed stimulus.  This will tell us which frequencies/features covary with one another in our stimulus, and how they covary across time.

```python

---

[← Average |CCF| across features, then show per-electrode traces + mean](09-average-ccf-across-features-then-show-per-electrode-traces-m.md) · [Up: contents](index.md) · [Calculate covariance matrix for training data →](11-calculate-covariance-matrix-for-training-data.md)
