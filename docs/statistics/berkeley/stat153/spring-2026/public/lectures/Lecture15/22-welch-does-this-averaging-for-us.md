---
title: Welch does this averaging for us
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Welch does this averaging for us

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

f_w, Pxx_w = welch(y_dance, fs=sr, nperseg=chunk_len, noverlap=chunk_len//2)
axes[1].plot(f_w, Pxx_w, color='#e94560', linewidth=1.5)
axes[1].set_title('welch average (overlapping segments)')
axes[1].set_xlabel('Frequency (Hz)')
axes[1].set_ylabel('Power')
axes[1].set_xlim(0, 3000)

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

### Low-Pass and High-Pass Filters

Next let's show what low-pass and high-pass filters do to a signal both in frequency and in time. Here we will use Butterworth filters, which are designed to have frequencies as flat as possible in the pass band (the frequencies you want to keep or "pass"). We will:

1. Listen to the filtered audio
2. See the spectrogram before and after
3. Examine the filter's frequency response

We'll use the slow and dance songs here, but you can try any of them you'd like.

```python

---

[← Welch averages over these to reduce variance.](21-welch-averages-over-these-to-reduce-variance.md) · [Up: contents](index.md) · [Filter design and application →](23-filter-design-and-application.md)
