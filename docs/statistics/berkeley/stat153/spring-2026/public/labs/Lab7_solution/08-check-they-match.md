---
title: Check they match
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Check they match

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure()
plt.plot(d_manual)
plt.plot(d_numpy)

plt.figure()
plt.plot(fft_numpy)
print("Max difference between manual and numpy DFT:", np.max(np.abs(d_manual - d_numpy)))
```

```
Max difference between manual and numpy DFT: 1.5169458873047464e-13
/Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages/matplotlib/cbook.py:1719: ComplexWarning: Casting complex values to real discards the imaginary part
  return math.isfinite(val)
/Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages/matplotlib/cbook.py:1355: ComplexWarning: Casting complex values to real discards the imaginary part
  return np.asarray(x, float)
```

*(2 figures omitted — see the original notebook.)*

### From DFT to periodogram

The scaled periodogram is $P(j/n) = \frac{4}{n}|d(j/n)|^2$. Let's compute it from the DFT and compare to `scipy.signal.periodogram`.

```python

---

[← Lab7 solution Part 07 —](07-lab7-solution-part-07.md) · [Up: contents](index.md) · [Compute the scaled periodogram from our DFT →](09-compute-the-scaled-periodogram-from-our-dft.md)
