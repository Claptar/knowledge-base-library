---
title: Lab4 Part 04 —
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab4 Part 04 —

**Source:** [`Lab4.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab4.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fft_y = np.fft.fft(y)
m = n // 2 - 1
fourier_freqs = np.arange(1/n, (1/2) + (1/n), 1/n)
m = len(fourier_freqs)
pgram_y = (np.abs(fft_y[1:(m + 1)]) ** 2)/n

plt.plot(fourier_freqs, pgram_y)
plt.xlabel("Frequencies")
plt.title("Periodogram")
plt.show()

fhat_fft = fourier_freqs[np.argmax(pgram_y)]
print(fhat_fft)
```

```
0.2025
```

*(1 figure omitted — see the original notebook.)*

Except in rare cases where the true frequency is already a Fourier frequency, the MLE of $f$ computed on a fine grid will be closer to the truth compared to the MLE computed on the grid of Fourier frequencies. But the MLE computed on Fourier frequencies is much more computationally cheap.

After computing the MLE of $f$, we can do linear regression (where $f$ is fixed the MLE) to compute the MLEs of the coefficient parameters and $\sigma$.

```python
x = np.arange(1, n + 1)
xcos = np.cos(2 * np.pi * fhat * x)
xsin = np.sin(2 * np.pi * fhat * x)
Xfhat = np.column_stack([np.ones(n), xcos, xsin])

md = sm.OLS(y, Xfhat).fit()
print(md.params)

---

[← Since n is not very big here, we can work with a dense grid.](03-since-n-is-not-very-big-here-we-can-work-with-a-dense-grid.md) · [Up: contents](index.md) · [Lab4 Part 05 — →](05-lab4-part-05.md)
