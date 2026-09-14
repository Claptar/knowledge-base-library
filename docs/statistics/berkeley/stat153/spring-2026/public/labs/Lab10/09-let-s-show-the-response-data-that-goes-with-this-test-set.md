---
title: Let's show the response data that goes with this test set
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's show the response data that goes with this test set

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ntimes,nelecs = ytest.shape
print(f'{ntimes} time points, {nelecs} electrodes')

plt.figure(figsize=(10,3))
for ch in np.arange(nelecs):
    plt.subplot(nelecs,1,ch+1)
    plt.plot(ytest[:,ch]+ch)
    ticks = np.arange(0, ntimes, fs*10)
    plt.gca().set_xticks(ticks)
    plt.gca().set_xlim([0,nsec_to_show*fs])
    #plt.colorbar(label='z-score')
    if ch == nelecs-1:
        plt.xlabel('Time (s)')
        plt.ylabel('Z')
        plt.gca().set_xticklabels((ticks / fs).astype(int))
    else:
        plt.gca().set_xticklabels([])
```

---

[← Let's look at what we're using for our xtrain matrices](08-let-s-look-at-what-we-re-using-for-our-xtrain-matrices.md) · [Up: contents](index.md) · [How do we choose the lags? →](10-how-do-we-choose-the-lags.md)
