---
title: Since n is not very big here, we can work with a dense grid.
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Since n is not very big here, we can work with a dense grid.

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

ngrid = 100000
allfvals = np.linspace(0, 0.5, ngrid)
rssvals = np.array([rss(f) for f in allfvals])
fhat = allfvals[np.argmin(rssvals)]

print(fhat)

plt.plot(allfvals, rssvals)
plt.show()
```

```
0.2035520355203552
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← We can minimize rss(f) over a fine grid of possible f values.](02-we-can-minimize-rss-f-over-a-fine-grid-of-possible-f-values.md) · [Up: contents](index.md) · [Lab4 Part 04 — →](04-lab4-part-04.md)
