---
title: Show whether the data have been z-scored
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Show whether the data have been z-scored

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(ytrain.mean(), ytrain.std())
print(ytest.mean(), ytest.std())
print(xtrain['spec'].mean(), xtrain['spec'].std())
print(xtest['spec'].mean(), xtest['spec'].std())
```

```python

---

[← Here we will read in the contents of the file](06-here-we-will-read-in-the-contents-of-the-file.md) · [Up: contents](index.md) · [Let's look at what we're using for our xtrain matrices →](08-let-s-look-at-what-we-re-using-for-our-xtrain-matrices.md)
