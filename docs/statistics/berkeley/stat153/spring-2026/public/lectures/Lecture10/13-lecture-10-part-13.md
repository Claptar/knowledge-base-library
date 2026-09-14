---
title: Lecture 10 — Part 13 —
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 10 — Part 13 —

**Source:** [`public/lectures/Lecture10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

y_train = y[mask]
y_test = y[~mask]
t_train = t[mask]
t_test = t[~mask]

plt.plot(t, y,'.-')
plt.plot(t_train, y_train, '.-')
plt.plot(t_test, y_test, '.-')
#plt.gca().set_xlim([0, 0.2])
```

```
[<matplotlib.lines.Line2D at 0x328eeac80>]
```

*(1 figure omitted — see the original notebook.)*

---

[← Cross-validation on time series data](12-cross-validation-on-time-series-data.md) · [Up: contents](index.md) · [This is cheating! →](14-this-is-cheating.md)
