---
title: Regularization parameters (alphas - also sometimes called lambda)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Regularization parameters (alphas - also sometimes called lambda)

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Check alpha values

We can use the function `check_alphas` to see what the best regularization parameter $\alpha$ is for each channel. This will plot each electrode as a curve, with each correlation value vs. alpha. For most "good" electrodes there will be a peak value in the middle of the range of alphas. If your model is consistently showing that the average best $\alpha$ is the smallest or largest value, you should widen your range appropriately and re-run the model.

```python
fig = plt.figure()
plt.semilogx(alphas, allRcorrs.mean(2))  # Log space alphas

---

[← For logging compute times, debug messages](18-for-logging-compute-times-debug-messages.md) · [Up: contents](index.md) · [Plot a line at the maximum alpha. This should be in the middle →](20-plot-a-line-at-the-maximum-alpha-this-should-be-in-the-middl.md)
