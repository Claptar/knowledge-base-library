---
title: '── Row 2: Daniell smoother ──'
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# ── Row 2: Daniell smoother ──

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

daniell_Ls = [1, 2, 15]
for col, L in enumerate(daniell_Ls):
    smoothed = daniell_smooth(power_n, L)
    axes[0, col].semilogy(freqs_n, smoothed, lw=1.2, color='C1',
                          label=f'Daniell (2L+1 = {2*L+1})')
    axes[0, col].semilogy(freqs_n, power_n, lw=0.3, color='C0')
    for freq in f:
        axes[1, col].axvline(freq, ls='--', color='red', alpha=0.4, lw=1)
    axes[0, col].set_xlim(0, 50)
    axes[0, col].set_ylim(1e-2, 1e4)
    axes[0, col].legend(fontsize=9, loc='upper right')
    if col == 0:
        axes[1, col].set_ylabel('Daniell smoother\n\nPower (log)')

---

[← Column labels](13-column-labels.md) · [Up: contents](index.md) · [── Row 3: Welch ── →](15-row-3-welch.md)
