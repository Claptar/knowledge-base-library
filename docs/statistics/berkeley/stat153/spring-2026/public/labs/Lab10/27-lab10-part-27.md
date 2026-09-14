---
title: Lab10 Part 27 —
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab10 Part 27 —

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## How does the selection of regularization parameter $\alpha$ affect the observed coefficients?

It is important to choose a range of $\alpha$ values and determine which yield the best predictions on held out data, since the regularization parameter itself can affect the structure of your STRF.

One of the things we did above was just to choose the best regularization parameter for each electrode separately. However, this choice does affect what the STRF filters look like, so here we will do an exercise where we fit all possible alphas and show the weights. This is just for educational purposes and is not typically needed in an analysis.

```python
from ridge.ridge import eigridge

---

[← Loop through the best channels](26-loop-through-the-best-channels.md) · [Up: contents](index.md) · [Get weights for all alphas →](28-get-weights-for-all-alphas.md)
