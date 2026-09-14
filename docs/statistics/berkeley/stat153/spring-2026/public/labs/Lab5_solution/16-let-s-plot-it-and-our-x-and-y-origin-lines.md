---
title: Let's plot it and our x and y origin lines
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's plot it and our x and y origin lines

**Source:** [`public/labs/Lab5_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.plot(t, y)
plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.xlabel('Time')
plt.ylabel('value')
```

```
Text(0, 0.5, 'value')
```

*(1 figure omitted — see the original notebook.)*

```python
nf = 1000  # Test this number of frequencies
f_grid = np.linspace(0,fs/2,nf)

---

[← Our true sinusoid](15-our-true-sinusoid.md) · [Up: contents](index.md) · [or →](17-or.md)
