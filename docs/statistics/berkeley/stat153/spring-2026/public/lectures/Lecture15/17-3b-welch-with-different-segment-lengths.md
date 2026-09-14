---
title: 3b. Welch with different segment lengths
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# 3b. Welch with different segment lengths

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

for nperseg in [4096, 2048, 1024]:
    f_w, Pxx_w = welch(y_dance, fs=sr, nperseg=nperseg, noverlap=nperseg//2)
    n_segs = (len(y_dance) - nperseg) // (nperseg//2) + 1
    axes[1].plot(f_w, Pxx_w, linewidth=1.2, label=f'welch(nperseg={nperseg}, ~{n_segs} segments)')

axes[1].set_title('welch(y, fs=sr, nperseg=...)')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Power')
axes[1].legend(fontsize=9, loc='upper right')

plt.tight_layout()
plt.show()

print('Dance track:')
display(Audio(y_dance, rate=sr))
```

```
Dance track:
<IPython.lib.display.Audio object>
```

*(1 figure omitted — see the original notebook.)*

Now let's overlay some raw periodograms from different chunks of the music data. Do you think the individual periodograms will look the same or different?

```python

---

[← 3a. Raw periodogram](16-3a-raw-periodogram.md) · [Up: contents](index.md) · [--- Overlay raw periodograms from different chunks --- →](18-----overlay-raw-periodograms-from-different-chunks.md)
