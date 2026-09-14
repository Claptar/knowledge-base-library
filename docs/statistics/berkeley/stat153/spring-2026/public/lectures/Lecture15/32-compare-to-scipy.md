---
title: Compare to scipy
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Compare to scipy

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, axes = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
nps = 2048

f1, t1, S1 = spectrogram(y_rep, fs=sr, nperseg=nps, noverlap=nps//2)
axes[0].pcolormesh(t1, f1, 10*np.log10(S1+1e-10), cmap='magma', shading='gouraud')
axes[0].set_title('scipy.signal.spectrogram', fontsize=12, fontweight='bold')
axes[0].set_ylabel('Frequency (Hz)')
axes[0].set_xlabel('Time (s)')
axes[0].set_ylim(0, 1500)

f2, t2, S2 = my_spectrogram(y_rep, fs=sr, nperseg=nps, noverlap=nps//2)
axes[1].pcolormesh(t2, f2, 10*np.log10(S2+1e-10), cmap='magma', shading='gouraud')
axes[1].set_title('my_spectrogram (np.fft by hand)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Time (s)')
axes[1].set_ylim(0, 1500)

plt.suptitle('No magic — spectrogram = sliding periodogram',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Build a spectrogram from scratch](31-build-a-spectrogram-from-scratch.md) · [Up: contents](index.md)
