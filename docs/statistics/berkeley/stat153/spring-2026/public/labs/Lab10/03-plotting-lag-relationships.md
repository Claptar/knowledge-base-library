---
title: Plotting lag relationships
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

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

### Create delay matrices

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

### Look at delayed stimulus matrix

Here I'll plot only a subset of the delayed matrix so you can see its structure. Again, this is transposed so that time is on the x axis. Red lines are shown so you can appreciate the small shifts of the matrices as a function of delay.

```python
fig, axes = plt.subplots(figsize=(10,3))
plt.imshow(xtraind[0:4000,:].T, cmap = cm.magma, aspect='auto', interpolation='nearest')
plt.gca().xaxis.grid(color='w')
plt.xlabel('Time bin')
plt.ylabel('Feature x delay')
```

### Problems with OLS

In class we looked at the OLS solution and saw that the beta weights were very speckly and difficult to interpret. Here we will instead use ridge regression, which helps deal with our correlated predictors.

```python
# For logging compute times, debug messages
import logging
logging.basicConfig(level=logging.DEBUG)

# Regularization parameters (alphas - also sometimes called lambda)
alphas = np.logspace(2,8,15) # Gives you 15 values between 10^2 and 10^8
nalphas = len(alphas)

use_corr = True # Use correlation between predicted and validation set as metric for goodness of fit
single_alpha = False # If False, use best alpha for each electrode. Usually this is what you should do.
nfolds = 3 # How many folds of cross-validation we want to do to find the ridge parameter (this is a pretty low number)
chunklen = int(len(delays)*4) # We will randomize the data in chunks - we should not randomly choose
                              # time points as that will remove correlation structure that we need to keep
nchunks = np.floor(0.2*xtraind.shape[0]/chunklen).astype('int')

nchans = ytrain.shape[1] # Number of electrodes/sensors

# outputs are:
#     beta:      the beta values,
#     corrs:     correlations on held out data,
#     valphas:   the best alphas for each electrode
#     allRcorrs: correlations for each alpha value across folds
#     valinds:   indices for cross validation
#     pred:      predictions
beta, corrs, valphas, allRcorrs, valinds, pred, _ = cv_ridge(xtraind, ytrain, xtestd, ytest,
                                                               alphas, nfolds, chunklen, nchunks,
                                                               use_corr=use_corr,  single_alpha = single_alpha,
                                                               use_svd=False)
```

### Check alpha values

We will now check the best regularization parameter $\alpha$ for each channel. This will plot each electrode as a curve, with each correlation value vs. alpha. For most "good" electrodes there will be a peak value in the middle of the range of alphas. If your model is consistently showing that the average best $\alpha$ is the smallest or largest value, you should widen your range appropriately and re-run the model.

```python
fig = plt.figure()
plt.semilogx(alphas, allRcorrs.mean(2))  # Log space alphas
# Plot a line at the maximum alpha. This should be in the middle
plt.axvline(alphas[allRcorrs.mean(2).mean(1).argmax()])
plt.xlabel('Alpha')
plt.ylabel('Correlation')
plt.show()
```

### Show predictions

Now we will show the predicted versus actual activity for all electrodes. If these are well-modeled by the STRF, you should see that the predicted and actual activity look fairly similar. If a larger regularization value alpha was chosen, the predicted activity will tend to look smoother.

```python
# How much time to show?
ntimes = int(30*fs) # Show 30 seconds of time
ntimes_start = int(5*fs)  # Start 5 seconds in since there is a lot of silence at the beginning
times = np.arange(ntimes_start, ntimes_start+ntimes)/fs

# Plot predictions vs. actual response
print("Prediction matrix shape: ", pred.shape)
print("Response matrix shape: ", ytest.shape)

fig = plt.figure(figsize=(10,5))
plt.subplot(nelecs+1,1,1)
plt.imshow(xtestd[ntimes_start:ntimes_start+ntimes,:nfeats].T, aspect='auto', cmap=cm.magma, interpolation='nearest')
xticks = np.arange(0, len(times), step=500)
plt.gca().set_xticks(xticks)
plt.gca().set_xticklabels([int(times[x]) for x in xticks])
plt.gca().invert_yaxis()

# Loop through the best channels
for i in np.arange(nelecs):
    # Get the predicted neural response
    prediction = pred[ntimes_start:ntimes_start+ntimes, i]
    prediction = prediction/prediction.max() # Rescale to max

    actual_resp = ytest[ntimes_start:ntimes_start+ntimes,i]
    actual_resp = actual_resp/actual_resp.max(0) # Rescale to max

    plt.subplot(nelecs+1,1,i+2)
    plt.plot(times, actual_resp, color='k', label='actual')
    plt.plot(times, prediction.T, color='r',label='pred')

    plt.title(f'Channel {i}, r={corrs[i]:.2f}')
    plt.gca().set_xlim([ntimes_start/fs,(ntimes_start+ntimes)/fs])
    plt.legend(loc='upper right')
plt.tight_layout()
```

### Visualizing the STRF filters

Here we will show the STRF filters we've derived for each channel.  These filters show which spectrotemporal features of the stimulus best predict an increase or decrease in the observed neural activity.

```python
# Plot all of the STRFs, using a separate regularization parameter for each (whichever gives the best performance)

fig = plt.figure(figsize=(10,3))
print(beta.shape)

for c in np.arange(nelecs):
    ax = fig.add_subplot(1,nelecs,c+1)
    strf = beta[:,c].reshape(len(delays),-1)
    smax = np.abs(strf).max()
    plt.imshow(strf.T, vmin=-smax, vmax=smax, cmap = cm.RdBu_r, aspect='auto', interpolation='nearest')
    plt.title(f'elec {c}: r={corrs[c]:.2f}')
    if c==0:
        plt.xlabel('Time (s)')
        plt.ylabel('Freq.')
    ax.set_ylim(ax.get_ylim()[::-1]) # This just reverses the y axis so low frequency is at the bottom
    ax.xaxis.set_ticks([0,len(delays)])
    ax.xaxis.set_ticklabels([0, -len(delays)/fs])
    plt.gca().invert_xaxis() # Invert the x-axis so Time (s) is on the x rather than Time delay (s)

    ax.yaxis.set_ticks([])
    #title('alpha=%3.3g'%(alphas[best_alphas_indiv[c]]))
    #colorbar()

plt.tight_layout();
```

### How does the selection of regularization parameter $\alpha$ affect the observed coefficients?

It is important to choose a range of $\alpha$ values and determine which yield the best predictions on held out data, since the regularization parameter itself can affect the structure of your STRF.

One of the things we did above was just to choose the best regularization parameter for each electrode separately. However, this choice does affect what the STRF filters look like, so here we will do an exercise where we fit all possible alphas and show the weights. This is just for educational purposes and is not typically needed in an analysis.

```python
from ridge.ridge import eigridge

# Get weights for all alphas
all_alpha_wts = []
for alpha in alphas:
    print("Fitting model for alpha=%.3g"%(alpha))
    tmp_wt = eigridge(xtraind, ytrain, alpha)
    all_alpha_wts.append(tmp_wt)

awt=np.array(all_alpha_wts)
```

### Calculating performance on the validation set for each alpha

Next, we need to calculate the predicted response to our validation set for our assessment of model performance.  Normally we would only do this for the best alpha found in the previous step, but here we will calculate all STRFs for all channels and all alphas so we can compare the correlations later.

The predictions are normally returned by `cv_ridge`, but here we can also calculate them directly by getting the dot product between the delayed stimulus matrix and the STRF weights. This is exactly calculating $\hat{Y} = X \beta$.

```python
print("Calculating predicted response to validation set")
wt_array = np.dstack(awt)
print(wt_array.shape)
vPred_alpha = [ [ np.dot(xtestd, wt_array[:,ch,alph]) for ch in np.arange(nchans)] for alph in np.arange(nalphas)]
vPred_alpha = np.array(vPred_alpha)
```

### Get model performance for each alpha value

Since we didn't get them for free, we will now also manually calculate the correlations between each prediction and the actual held out data `vResp`.

```python
print("Calculating correlations on validation set")
vcorr  = [ [ np.corrcoef(vPred_alpha[alph][ch], ytest[:,ch])[0,1] for ch in np.arange(nchans)] for alph in np.arange(nalphas)]
vcorr = np.array(vcorr)
print("Done calculating correlations")
print("Correlation matrix shape: ", vcorr.shape)
```

### How does the choice of $\alpha$ affect the STRF structure?

Here we will plot the STRF arrays for the 5 best channels for each alpha regularization value. Each row is an electrode, each column is an alpha value. You will see that as the alpha value increases, the STRF weights become broader and smoother. The r-value should peak somewhere in the middle of the range.

Here we will indicate the best weight matrix and alphas with red titles. These are the weights and correlations returned by `bootstrap_ridge`.

```python
# Show how regularization parameter changes STRFs
fig = plt.figure(figsize=(20,10))
fig.clf()
axes = [fig.add_subplot(nelecs,len(alphas),ii+1) for ii in range((len(alphas))*nelecs)]
p = 0
for ch in np.arange(nelecs): # loop through all electrodes
    for a in np.arange(len(alphas)): # loop through the alpha regularization parameter
        strf = wt_array[:,ch,a].reshape(len(delays),-1)
        smax = np.abs(strf).max()
        axes[p].imshow(strf.T,vmin=-smax, vmax=smax, cmap = cm.RdBu_r, aspect='auto', interpolation='nearest')
        axes[p].xaxis.set_ticks([])
        axes[p].yaxis.set_ticks([])
        axes[p].set_ylim(axes[p].get_ylim()[::-1]) # This just reverses the y axis so low frequency is at the bottom
        axes[p].set_xlim(axes[p].get_xlim()[::-1]) # Invert the x-axis so Time (s) is on the x rather than Time delay (s)
        axes[p].set_title(f'a={alphas[a]:.2f}\nr={vcorr[a,ch]:.3f}')
        if a == vcorr[:,ch].argmax():
            axes[p].set_title(f'a={alphas[a]:.2f}\nr={vcorr[a,ch]:.3f}', color='r')
        p+=1

plt.tight_layout()
#fig.subplots_adjust(hspace=.5, wspace=.8)
```

## Putting it together

Here you've now seen a real-world example of a time-lagged regression that incorporates all of the following topics we've discussed so far in class:

1. Spectral analysis (using the spectrogram of the sound as a covariate in regression)
2. Multiple linear regression with time lags
3. Cross-validation
4. Dealing with auto-correlated predictors
5. OLS vs. ridge

## For you to try

* Try using different lags (shorter? longer? positive and negative? negative only?)
* Try using 'phn' instead of 'spec' in the training - how does the model performance compare (when assessed as correlation)?

---

[← How do we choose the lags?](02-how-do-we-choose-the-lags.md) · [Up: contents](index.md)
