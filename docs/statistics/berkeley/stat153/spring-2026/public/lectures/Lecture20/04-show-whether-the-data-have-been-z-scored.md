---
title: Show whether the data have been z-scored
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Show whether the data have been z-scored

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

print(ytrain.mean(), ytrain.std())
print(ytest.mean(), ytest.std())
print(xtrain['spec'].mean(), xtrain['spec'].std())
print(xtest['spec'].mean(), xtest['spec'].std())
```

```
(161034, 3) (13563, 3)
1.8826142342050505e-18 0.9999999999999961
1.1176174172048075e-17 1.0000000000000016
2.188539047263371e-15 1.0
-1.2874952646199382e-15 0.9999999999999996
```

```python

---

[← Here we will read in the contents of the file](03-here-we-will-read-in-the-contents-of-the-file.md) · [Up: contents](index.md) · [Let's look at what we're using for our xtrain matrices →](05-let-s-look-at-what-we-re-using-for-our-xtrain-matrices.md)
