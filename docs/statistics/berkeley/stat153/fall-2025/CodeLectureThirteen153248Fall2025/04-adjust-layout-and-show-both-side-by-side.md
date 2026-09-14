---
title: Adjust layout and show both side by side
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Adjust layout and show both side by side

**Source:** [`CodeLectureThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Summary statistics of the $\tau$ and $\sigma$ samples can be obtained as follows.

```python
df_tau_sigma = pd.DataFrame({
    'tau_samples': tau_samples,
    'sig_samples': sig_samples
})

---

[← Second histogram: sigsamples](03-second-histogram-sigsamples.md) · [Up: contents](index.md) · [Summary statistics →](05-summary-statistics.md)
