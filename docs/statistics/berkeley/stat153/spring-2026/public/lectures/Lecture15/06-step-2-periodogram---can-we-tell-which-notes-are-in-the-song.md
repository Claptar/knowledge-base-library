---
title: 'Step 2: Periodogram - can we tell which notes are in the song?'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Step 2: Periodogram - can we tell which notes are in the song?

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, ax = plt.subplots(figsize=(14, 3))
f_psd, Pxx = periodogram(y_solo, fs=sr)
ax.plot(f_psd, Pxx, color='#e94560', linewidth=0.6)
ax.set_title('periodogram(y, fs=sr) — Which frequencies are present?', fontsize=14, fontweight='bold')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('PSD (V²/Hz)')
ax.set_xlim(0, 2000)
plt.tight_layout()
plt.show()

---

[← Step 1: Waveform only - what do we get from this?](05-step-1-waveform-only---what-do-we-get-from-this.md) · [Up: contents](index.md) · [Could you sing the song from this or identify the melody? →](07-could-you-sing-the-song-from-this-or-identify-the-melody.md)
