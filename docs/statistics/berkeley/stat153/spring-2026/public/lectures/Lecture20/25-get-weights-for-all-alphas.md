---
title: Get weights for all alphas
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Get weights for all alphas

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Calculating performance on the validation set for each alpha

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

## Get model performance for each alpha value

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

## How does the choice of $\alpha$ affect the STRF structure?

Here we will plot the STRF arrays for the 5 best channels for each alpha regularization value. Each row is an electrode, each column is an alpha value. You will see that as the alpha value increases, the STRF weights become broader and smoother. The r-value should peak somewhere in the middle of the range.

Here we will indicate the best weight matrix and alphas with red titles. These are the weights and correlations returned by `bootstrap_ridge`.

```python

---

[← Lecture 20 — Part 24 —](24-lecture-20-part-24.md) · [Up: contents](index.md) · [Show how regularization parameter changes STRFs →](26-show-how-regularization-parameter-changes-strfs.md)
