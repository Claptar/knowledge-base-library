---
title: Q6. The covariance matrix $X^T X$ and time-lagged ridge regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework4.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Q6. The covariance matrix $X^T X$ and time-lagged ridge regression

In the lecture on time lagged regression and in the lab, you saw an example of performing a regression using spectrogram features at multiple time lags as the inputs to a regression model. The figure below shows $X^T X$ for an 80-band spectrogram at 20 time delays. Columns are ordered frequency-fastest: the first 80 columns correspond to all 80 frequency bins at delay 0, the next 80 columns are all 80 frequency bins at delay 1, and so on.

Q6a. What does the value of `covmat[0,1]` represent (in words, in terms of frequency and delay)? What about `covmat[0,81]`? Next, describe two visible structural features of `covmat`. How would covmat look different if the spectrogram were white noise?

```python
# Run this cell to load and show the stimulus covariance matrix
import h5py
with h5py.File('covmat.hf5', 'r') as hf:
    covmat = hf['covmat'][:]

plt.imshow(covmat);
```

**Answer**: Write your answer to Q6a here.

Q6b. When we fit ridge regression, we penalize this matrix by adding a regularization term to the diagonal, i.e. $X^T X + \lambda I$. Recall that for ridge, the beta estimate is given by $\hat{\beta} = (X^T X + \lambda I)^-1 X^T y$. Looking at `covmat`, why is regularization especially important for this design matrix? Refer to the structural features you identified in Q6a.

**Answer:** Answer to Q6b.

---

[← Q5. Fitting an ARIMA model](03-q5-fitting-an-arima-model.md) · [Up: contents](index.md)
