---
title: Plotting lag relationships
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Plotting lag relationships

Now we will plot the average cross-correlation function across features to determine how we want to structure our lags for the regression.

```python
lags_s = lags / fs

# Average |CCF| across features, then show per-electrode traces + mean
ccf_abs = np.abs(ccf).mean(axis=1)  # [n_elec, n_lags]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(lags_s, ccf_abs.T, color='gray', alpha=0.3, lw=0.8)
ax.plot(lags_s, ccf_abs.mean(0), color='C0', lw=2, label='mean across elecs')
ax.axvline(0, color='k', ls='--', lw=0.8)
ax.set_xlabel('lag (s)  [positive = spectrogram leads neural]')
ax.set_ylabel('|CCF|, averaged across spec features')
ax.set_title('Stimulus–response cross-correlation envelope')
ax.legend()
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

## Create delay matrices

We now have the prerequisite matrices to perform our regression (`ytrain` and `xtrain`, and cross-validation test set `ytest` and `xtest`). To include time delays, we can set up a stacked matrix of our stimulus at different time delays. This actually has a special name -- it's called a [Toeplitz matrix](http://en.wikipedia.org/wiki/Toeplitz_matrix)). As a toy example, say we have a spectrogram with n time points and 3 frequencies.

$$
\begin{bmatrix}
    x_{1,1} & x_{1,2} & x_{1,3} \\
    x_{2,1} & x_{2,2} & x_{2,3} \\
    x_{3,1} & x_{3,2} & x_{3,3} \\
    \vdots & \vdots & \vdots \\
    x_{n,1} & x_{n,2} & x_{n,3} \\
\end{bmatrix}
$$

Our stacked delay matrix would look something like this:

$$
\begin{bmatrix}
    x_{1,1} & x_{1,2} & x_{1,3} & 0 & 0 & 0 & 0 & 0 & 0 & \ldots & 0 & 0 & 0 \\
    x_{2,1} & x_{2,2} & x_{2,3} & x_{1,1} & x_{1,2} & x_{1,3} & 0 & 0 & 0 & \ldots & 0 & 0 & 0 \\
    x_{3,1} & x_{3,2} & x_{3,3} & x_{2,1} & x_{2,2} & x_{2,3} & x_{1,1} & x_{1,2} & x_{1,3} & \ldots & 0 & 0 & 0 \\
    x_{4,1} & x_{4,2} & x_{4,3} & x_{3,1} & x_{3,2} & x_{3,3} & x_{2,1} & x_{2,2} & x_{2,3} & \ldots & 0 & 0 & 0 \\
    \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\
    x_{n,1} & x_{n,2} & x_{n,3} & x_{n-1,1} & x_{n-1,2} & x_{n-1,3} & x_{n-2,1} & x_{n-2,2} & x_{n-2,3} & \ldots & x_{n-d+1,1} & x_{n-d+1,2} & x_{n-d+1,3} \\
\end{bmatrix}
$$

```python
# Create the delayed matrices

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
# Calculate covariance matrix for training data
dtype = np.single
covmat = np.array(np.dot(xtraind.astype(dtype).T, xtraind.astype(dtype)))
```

```python
# Show covariance matrix
plt.figure(figsize=(5,5))
plt.imshow(covmat[:80,:80], cmap=cm.Reds)
plt.colorbar()
```

```
<matplotlib.colorbar.Colorbar at 0x12db9a350>
```

*(1 figure omitted — see the original notebook.)*

```python
# add an intercept term

xtraind_int = np.hstack((np.ones((xtraind.shape[0],1)), xtraind))
xtestd_int = np.hstack((np.ones((xtestd.shape[0],1)), xtestd))
```

---

[← Stat 153/248 Lecture 20](01-stat-153-248-lecture-20.md) · [Up: contents](index.md) · [OLS →](03-ols.md)
