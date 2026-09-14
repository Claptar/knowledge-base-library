---
title: Show how regularization parameter changes STRFs
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Show how regularization parameter changes STRFs

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[← Get weights for all alphas](25-get-weights-for-all-alphas.md) · [Up: contents](index.md) · [Putting it together →](27-putting-it-together.md)
