---
title: This is cheating!
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# This is cheating!

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We can't do this because of the strong autocorrelations in our dataset. Randomly splitting on time indices will make your predictions falsely more accurate on your test set because your train and test data are coming from the same underlying time series and are autocorrelated with each other.

Instead, we should split based on chunks. For example, train on the first 80% of the time samples and test on the remaining 20%.

```python
y_train = y[:int(0.8*len(y))]
y_test = y[int(0.8*len(y)):]
t_train = t[:int(0.8*len(y))]
t_test = t[int(0.8*len(y)):]

plt.plot(t, y,'.-')
plt.plot(t_train, y_train, '.-')
```

```
[<matplotlib.lines.Line2D at 0x328e04cd0>]
```

*(1 figure omitted — see the original notebook.)*

---

[← Lecture 10 — Part 13 —](13-lecture-10-part-13.md) · [Up: contents](index.md) · [What about choosing the number of parameters? →](15-what-about-choosing-the-number-of-parameters.md)
