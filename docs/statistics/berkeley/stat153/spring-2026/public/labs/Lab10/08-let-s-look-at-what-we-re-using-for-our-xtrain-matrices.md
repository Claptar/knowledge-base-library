---
title: Let's look at what we're using for our xtrain matrices
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's look at what we're using for our xtrain matrices

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

stim_types = ['spec', 'phn']

for stim_type in stim_types:
    ntimes, nfeats = xtest[stim_type].shape
    print(f'{ntimes} time points, {nfeats} {stim_type} features')
    nsec_to_show = 20

    plt.figure(figsize=(10,3))
    plt.imshow(xtest[stim_type].T, aspect='auto', cmap=cm.magma, interpolation='nearest')
    plt.gca().invert_yaxis()
    ticks = np.arange(0, ntimes, fs*10)
    plt.gca().set_xticks(ticks)
    plt.gca().set_xticklabels((ticks / fs).astype(int))
    plt.gca().set_xlim([0,nsec_to_show*fs])
    plt.title(f'xtest - {stim_type}')
    plt.colorbar()

    plt.xlabel('Time (s)')
    plt.ylabel('Feature (bin)')
```

```python

---

[← Show whether the data have been z-scored](07-show-whether-the-data-have-been-z-scored.md) · [Up: contents](index.md) · [Let's show the response data that goes with this test set →](09-let-s-show-the-response-data-that-goes-with-this-test-set.md)
