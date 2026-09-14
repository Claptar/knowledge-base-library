---
title: Add frequency labels
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture14.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Add frequency labels

**Source:** [`public/lectures/Lecture14.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture14.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

for ax in axes:
    for freq in f:
        ax.text(freq + 0.5, ax.get_ylim()[1] * 0.3, f'{freq} Hz',
                fontsize=8, color='red')

plt.tight_layout()
```

### Smoothing

Now let's use the noisy data (which is a more realistic case) and the smoothing methods to see what we recover.

```python
fig, axes = plt.subplots(2, 3, figsize=(15, 11))

---

[← Theoretical power for each component](11-theoretical-power-for-each-component.md) · [Up: contents](index.md) · [Column labels →](13-column-labels.md)
