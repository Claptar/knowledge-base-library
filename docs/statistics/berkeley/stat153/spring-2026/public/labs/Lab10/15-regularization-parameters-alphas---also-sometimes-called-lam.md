---
title: Regularization parameters (alphas - also sometimes called lambda)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Regularization parameters (alphas - also sometimes called lambda)

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

alphas = np.logspace(2,8,15) # Gives you 15 values between 10^2 and 10^8
nalphas = len(alphas)

use_corr = True # Use correlation between predicted and validation set as metric for goodness of fit
single_alpha = False # If False, use best alpha for each electrode. Usually this is what you should do.
nfolds = 3 # How many folds of cross-validation we want to do to find the ridge parameter (this is a pretty low number)
chunklen = int(len(delays)*4) # We will randomize the data in chunks - we should not randomly choose
                              # time points as that will remove correlation structure that we need to keep
nchunks = np.floor(0.2*xtraind.shape[0]/chunklen).astype('int')

nchans = ytrain.shape[1] # Number of electrodes/sensors

---

[← For logging compute times, debug messages](14-for-logging-compute-times-debug-messages.md) · [Up: contents](index.md) · [outputs are →](16-outputs-are.md)
