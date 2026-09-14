---
title: 'Step 1: Waveform only - what do we get from this?'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Step 1: Waveform only - what do we get from this?

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, ax = plt.subplots(figsize=(14, 3))
time_axis = np.arange(len(y_solo)) / sr
ax.plot(time_axis, y_solo, color='#0f3460', linewidth=0.3)
ax.set_title('Waveform', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_xlim(0,time_axis[-1])
plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← Change these paths if you have other sounds you want to use](04-change-these-paths-if-you-have-other-sounds-you-want-to-use.md) · [Up: contents](index.md) · [Step 2: Periodogram - can we tell which notes are in the song? →](06-step-2-periodogram---can-we-tell-which-notes-are-in-the-song.md)
