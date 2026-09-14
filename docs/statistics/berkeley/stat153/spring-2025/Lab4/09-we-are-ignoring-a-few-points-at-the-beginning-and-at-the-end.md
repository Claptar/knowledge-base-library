---
title: we are ignoring a few points at the beginning and at the end
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# we are ignoring a few points at the beginning and at the end

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

rssvals = np.array([rss(c) for c in allcvals])
```

```python
plt.plot(allcvals, rssvals)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
c_hat = allcvals[np.argmin(rssvals)]
print(c_hat)
```

```
4981
```

```python

---

[← Here is a simulated dataset having a change point](08-here-is-a-simulated-dataset-having-a-change-point.md) · [Up: contents](index.md) · [Estimates of other parameters →](10-estimates-of-other-parameters.md)
