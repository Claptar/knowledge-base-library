---
title: Loop through the best channels
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Loop through the best channels

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Visualizing the STRF filters

Here we will show the STRF filters we've derived for each channel.  These filters show which spectrotemporal features of the stimulus best predict an increase or decrease in the observed neural activity.

```python

---

[← Plot predictions vs. actual response](25-plot-predictions-vs-actual-response.md) · [Up: contents](index.md) · [Lab10 Part 27 — →](27-lab10-part-27.md)
