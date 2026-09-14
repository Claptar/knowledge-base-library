---
title: Calculate correlation between ytesthat and ytest for an example electrode
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Calculate correlation between ytesthat and ytest for an example electrode

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

elec = 2
r_test = np.corrcoef(ytest_hat[:,elec], ytest[:,elec])[0,1]

ytrain_hat = np.dot(xtraind_int, beta)
plt.figure(figsize=(12,4))
plt.subplot(2,1,1)
plt.imshow(xtestd[:,:nfeats].T, aspect='auto', cmap=cm.magma, interpolation='nearest')
plt.gca().set_xlim([2000,4000])
plt.ylabel('Feature bin')
plt.gca().invert_yaxis()

plt.subplot(2,1,2)
plt.plot(ytest[:,elec], label='ytest')
plt.plot(ytest_hat[:,elec], label='ytest_hat')
plt.xlabel('Time bin')
plt.ylabel('Z')
plt.gca().set_xlim([2000,4000])
plt.title(r_test)
plt.legend()
plt.tight_layout()
```

*(1 figure omitted — see the original notebook.)*

## Residuals plot

For completeness, we'll plot the residuals and their autocorrelation function. Note that for this particular type of model, it's often very common that the stimulus will *not* drive the majority of the variance in the data, and that in fact, other ongoing oscillatory processes will dominate the signal that we can't get rid of just through regression with stimulus features. Although this is objectively true, if we are able to use our models to do prediction on new data, we consider this useful, even if we aren't modeling all possible sources of variance.

```python
resid = ytest-ytest_hat
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(resid[:,2]);
```

*(1 figure omitted — see the original notebook.)*

## Plotting the beta coefficients (the STRF)

Now we'll plot the beta coefficients, showing how reshaping them according to the number of delays and features helps us with interpretability.

```python
print(beta.shape)
plt.plot(beta[:,0])
```

```
(3201, 3)
[<matplotlib.lines.Line2D at 0x16b551090>]
```

*(1 figure omitted — see the original notebook.)*

```python
fig = plt.figure(figsize=(10,3))

for c in np.arange(nelecs):
    ax = fig.add_subplot(1,3,c+1)
    strf = beta[1:,c].reshape(len(delays),-1)
    smax = np.abs(strf).max()
    plt.imshow(strf.T, vmin=-smax, vmax=smax, cmap = cm.RdBu_r, aspect='auto', interpolation='nearest')
    plt.title(f'elec {c}: r={np.corrcoef(ytest_hat[:,c], ytest[:,c])[0,1]:.2f}')
    if c==0:
        plt.xlabel('Time (s)')
        plt.ylabel('Freq.')
    ax.set_ylim(ax.get_ylim()[::-1]) # This just reverses the y axis so low frequency is at the bottom
    ax.xaxis.set_ticks([0,len(delays)])
    ax.xaxis.set_ticklabels([0, -len(delays)/fs])
    plt.gca().invert_xaxis() # Invert the x-axis so Time (s) is on the x rather than Time delay (s)

    ax.yaxis.set_ticks([])

plt.tight_layout();
```

*(1 figure omitted — see the original notebook.)*

## Problems with OLS

In looking at these weight matrices for each of the three electrodes, we can see that our linear model is performing decently well on held-out data (correlations up to 0.5, which for neural data is very good considering underlying measurement noise and physiological noise). However, the weight matrices themselves are not very interpretable. Ideally, we should be able to read these and interpret large positive values as features in the past that drive a strong neural response at time 0. That's not so obvious here.

One big issue is that our stimulus features are highly correlated! Sounds (and spectrograms) don't represent independent samples, they evolve relatively slowly over time. So one fix here is to use regularization -- in this case, we'll use ridge regression! Autocorrelation in the stimulus produces highly correlated columns in the delay-embedded design matrix, and ridge stabilizes estimation when columns are correlated.

```python

---

[← Let's look at performance on predicted versus actual data](16-let-s-look-at-performance-on-predicted-versus-actual-data.md) · [Up: contents](index.md) · [For logging compute times, debug messages →](18-for-logging-compute-times-debug-messages.md)
