---
title: Sort from lowest RSS to highest RSS (best to worst)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sort from lowest RSS to highest RSS (best to worst)

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ranked_idx = np.argsort(rss_per_freq)
ranked_freqs = f_grid[ranked_idx]

print(ranked_freqs[:10])
```

```
[ 2.50501002  2.00400802 12.5250501   5.51102204  3.00601202  3.50701403
  1.50300601  4.00801603  5.01002004 93.68737475]
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← What about choosing the number of parameters?](15-what-about-choosing-the-number-of-parameters.md) · [Up: contents](index.md) · [Now CV over how many top frequencies to include →](17-now-cv-over-how-many-top-frequencies-to-include.md)
