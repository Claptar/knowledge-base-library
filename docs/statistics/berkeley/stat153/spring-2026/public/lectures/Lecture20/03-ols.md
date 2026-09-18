---
title: OLS
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# OLS

Let's first look at fitting the model using OLS. Here we'll use numpy least squares for simplicity, though you can use any OLS solver.

```python
print(xtraind_int.shape)
print(ytrain.shape)
```

```
(161034, 3201)
(161034, 3)
```

```python
# Fit OLS
beta, SSE, rank, s = np.linalg.lstsq(xtraind_int, ytrain, rcond=None)
```

### Cross validation performance

Let's look at performance on held out data by computing predictions from our fitted `beta` values on our new `xtestd` and compare these predictions to the true held out data `ytest`.

```python
# Let's look at performance on predicted versus actual data
ytest_hat = np.dot(xtestd_int, beta)

# Calculate correlation between ytest_hat and ytest for an example electrode
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

### Residuals plot

For completeness, we'll plot the residuals and their autocorrelation function. Note that for this particular type of model, it's often very common that the stimulus will *not* drive the majority of the variance in the data, and that in fact, other ongoing oscillatory processes will dominate the signal that we can't get rid of just through regression with stimulus features. Although this is objectively true, if we are able to use our models to do prediction on new data, we consider this useful, even if we aren't modeling all possible sources of variance.

```python
resid = ytest-ytest_hat
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
plot_acf(resid[:,2]);
```

*(1 figure omitted — see the original notebook.)*

### Plotting the beta coefficients (the STRF)

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

### Problems with OLS

In looking at these weight matrices for each of the three electrodes, we can see that our linear model is performing decently well on held-out data (correlations up to 0.5, which for neural data is very good considering underlying measurement noise and physiological noise). However, the weight matrices themselves are not very interpretable. Ideally, we should be able to read these and interpret large positive values as features in the past that drive a strong neural response at time 0. That's not so obvious here.

One big issue is that our stimulus features are highly correlated! Sounds (and spectrograms) don't represent independent samples, they evolve relatively slowly over time. So one fix here is to use regularization -- in this case, we'll use ridge regression! Autocorrelation in the stimulus produces highly correlated columns in the delay-embedded design matrix, and ridge stabilizes estimation when columns are correlated.

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


wt, corrs, valphas, allRcorrs, valinds, pred, Pstim = cv_ridge(xtraind_int, ytrain, xtestd_int, ytest,
                                                                      alphas, nfolds, chunklen, nchunks,
                                                                      use_corr=use_corr,  single_alpha = single_alpha,
                                                                      use_svd=False)
```

```
INFO:ridge_corr:Selecting held-out test set..
INFO:ridge_corr:Doing Eigenvalue decomposition...
Cmode = False
Number of time points is greater than the number of features
Rstim shape (not cmode):
(128874, 3201)
Covmat shape:
(3201, 3201)
(3201, 3201) (3201, 128874) (128874, 3)
INFO:ridge_corr:Training: alpha=100.000, mean corr=0.29279, max corr=0.35569, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=268.270, mean corr=0.29445, max corr=0.35680, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=719.686, mean corr=0.29756, max corr=0.35885, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=1930.698, mean corr=0.30211, max corr=0.36185, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=5179.475, mean corr=0.30715, max corr=0.36514, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=13894.955, mean corr=0.31126, max corr=0.36732, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=37275.937, mean corr=0.31354, max corr=0.36703, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=100000.000, mean corr=0.31332, max corr=0.36366, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=268269.580, mean corr=0.30987, max corr=0.35686, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=719685.673, mean corr=0.30193, max corr=0.34511, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=1930697.729, mean corr=0.28603, max corr=0.32362, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=5179474.679, mean corr=0.25800, max corr=0.28702, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=13894954.944, mean corr=0.21857, max corr=0.23619, over-under(0.20)=2
INFO:ridge_corr:Training: alpha=37275937.203, mean corr=0.17604, max corr=0.18820, over-under(0.20)=0
INFO:ridge_corr:Training: alpha=100000000.000, mean corr=0.14619, max corr=0.16419, over-under(0.20)=0
INFO:counter:1/3 items complete (19.49 seconds/item, 00:00:38 remaining)
INFO:ridge_corr:Selecting held-out test set..
INFO:ridge_corr:Doing Eigenvalue decomposition...
Cmode = False
Number of time points is greater than the number of features
Rstim shape (not cmode):
(128874, 3201)
Covmat shape:
(3201, 3201)
(3201, 3201) (3201, 128874) (128874, 3)
INFO:ridge_corr:Training: alpha=100.000, mean corr=0.30239, max corr=0.37006, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=268.270, mean corr=0.30412, max corr=0.37146, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=719.686, mean corr=0.30726, max corr=0.37402, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=1930.698, mean corr=0.31170, max corr=0.37765, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=5179.475, mean corr=0.31654, max corr=0.38161, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=13894.955, mean corr=0.32087, max corr=0.38515, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=37275.937, mean corr=0.32443, max corr=0.38816, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=100000.000, mean corr=0.32685, max corr=0.39055, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=268269.580, mean corr=0.32640, max corr=0.39120, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=719685.673, mean corr=0.31960, max corr=0.38626, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=1930697.729, mean corr=0.30126, max corr=0.36817, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=5179474.679, mean corr=0.26836, max corr=0.33084, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=13894954.944, mean corr=0.22180, max corr=0.27328, over-under(0.20)=2
INFO:ridge_corr:Training: alpha=37275937.203, mean corr=0.16681, max corr=0.20258, over-under(0.20)=1
INFO:ridge_corr:Training: alpha=100000000.000, mean corr=0.12503, max corr=0.15051, over-under(0.20)=0
INFO:counter:2/3 items complete (18.87 seconds/item, 00:00:18 remaining)
INFO:ridge_corr:Selecting held-out test set..
INFO:ridge_corr:Doing Eigenvalue decomposition...
Cmode = False
Number of time points is greater than the number of features
Rstim shape (not cmode):
(128874, 3201)
Covmat shape:
(3201, 3201)
(3201, 3201) (3201, 128874) (128874, 3)
INFO:ridge_corr:Training: alpha=100.000, mean corr=0.30072, max corr=0.35952, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=268.270, mean corr=0.30229, max corr=0.36052, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=719.686, mean corr=0.30511, max corr=0.36222, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=1930.698, mean corr=0.30893, max corr=0.36429, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=5179.475, mean corr=0.31264, max corr=0.36598, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=13894.955, mean corr=0.31504, max corr=0.36702, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=37275.937, mean corr=0.31588, max corr=0.36804, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=100000.000, mean corr=0.31509, max corr=0.36930, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=268269.580, mean corr=0.31181, max corr=0.36921, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=719685.673, mean corr=0.30464, max corr=0.36482, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=1930697.729, mean corr=0.29028, max corr=0.35112, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=5179474.679, mean corr=0.26313, max corr=0.32107, over-under(0.20)=3
INFO:ridge_corr:Training: alpha=13894954.944, mean corr=0.22231, max corr=0.27313, over-under(0.20)=2
INFO:ridge_corr:Training: alpha=37275937.203, mean corr=0.17508, max corr=0.21549, over-under(0.20)=1
INFO:ridge_corr:Training: alpha=100000000.000, mean corr=0.14009, max corr=0.17190, over-under(0.20)=0
INFO:counter:3/3 items complete (17.57 seconds/item, 00:00:00 remaining)
INFO:ridge_corr:Finding best alpha for each electrode..
INFO:ridge_corr:Computing weights for each response using entire training set..
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3201)
Covmat shape:
(3201, 3201)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Predicting responses for predictions set..
(3201, 3201) (3201, 161034) (161034, 3)
```

### Check alpha values

We can use the function `check_alphas` to see what the best regularization parameter $\alpha$ is for each channel. This will plot each electrode as a curve, with each correlation value vs. alpha. For most "good" electrodes there will be a peak value in the middle of the range of alphas. If your model is consistently showing that the average best $\alpha$ is the smallest or largest value, you should widen your range appropriately and re-run the model.

```python
fig = plt.figure()
plt.semilogx(alphas, allRcorrs.mean(2))  # Log space alphas
# Plot a line at the maximum alpha. This should be in the middle
plt.axvline(alphas[allRcorrs.mean(2).mean(1).argmax()])
plt.xlabel('Alpha')
plt.ylabel('Correlation')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

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

```
Prediction matrix shape:  (13563, 3)
Response matrix shape:  (13563, 3)
```

*(1 figure omitted — see the original notebook.)*

### Visualizing the STRF filters

Here we will show the STRF filters we've derived for each channel.  These filters show which spectrotemporal features of the stimulus best predict an increase or decrease in the observed neural activity.

```python
# Plot all of the STRFs, using a separate regularization parameter for each (whichever gives the best performance)

fig = plt.figure(figsize=(10,3))
print(wt.shape)

for c in np.arange(nelecs):
    ax = fig.add_subplot(1,nelecs,c+1)
    strf = wt[1:,c].reshape(len(delays),-1)
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

```
(3201, 3)
```

*(1 figure omitted — see the original notebook.)*

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

```
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
Fitting model for alpha=100
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=268
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=720
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=1.93e+03
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
(3200, 3200) (3200, 161034) (161034, 3)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
Fitting model for alpha=5.18e+03
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=1.39e+04
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=3.73e+04
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=1e+05
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=2.68e+05
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=7.2e+05
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=1.93e+06
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=5.18e+06
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=1.39e+07
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=3.73e+07
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
INFO:ridge_corr:Doing Eigenvalue decomposition on the full stimulus matrix...
(3200, 3200) (3200, 161034) (161034, 3)
Fitting model for alpha=1e+08
Cmode = False
Number of time points is greater than the number of features
stim shape (not cmode):
(161034, 3200)
Covmat shape:
(3200, 3200)
INFO:ridge_corr:Computing weights
(3200, 3200) (3200, 161034) (161034, 3)
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

```
Calculating predicted response to validation set
(3200, 3, 15)
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

```
Calculating correlations on validation set
Done calculating correlations
Correlation matrix shape:  (15, 3)
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

*(1 figure omitted — see the original notebook.)*

## Putting it together

Here you've now seen a real-world example of a time-lagged regression that incorporates all of the following topics we've discussed so far in class:

1. Spectral analysis (using the spectrogram of the sound as a covariate in regression)
2. Multiple linear regression with time lags
3. Cross-validation
4. Dealing with auto-correlated predictors
5. OLS vs. ridge

---

[← Plotting lag relationships](02-plotting-lag-relationships.md) · [Up: contents](index.md)
