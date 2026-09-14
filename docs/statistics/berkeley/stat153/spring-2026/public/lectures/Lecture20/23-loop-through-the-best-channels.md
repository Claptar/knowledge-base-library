---
title: Loop through the best channels
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Loop through the best channels

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Visualizing the STRF filters

Here we will show the STRF filters we've derived for each channel.  These filters show which spectrotemporal features of the stimulus best predict an increase or decrease in the observed neural activity.

```python

---

[← Plot predictions vs. actual response](22-plot-predictions-vs-actual-response.md) · [Up: contents](index.md) · [Lecture 20 — Part 24 — →](24-lecture-20-part-24.md)
