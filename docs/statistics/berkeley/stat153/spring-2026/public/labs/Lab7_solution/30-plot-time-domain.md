---
title: Plot time domain
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab7_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot time domain

**Source:** [`public/labs/Lab7_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab7_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.plot(t, x, alpha=0.6)
plt.plot(t, signal, 'r', linewidth=2)
plt.title('Original signal + noise')
plt.xlabel('Time')

plt.subplot(2,2,2)
plt.plot(y)
plt.plot(t, signal, 'r', linewidth=2)
plt.title(f'After MA filter (m={m})')
plt.xlabel('Time')

---

[← TODO: Compute the filtered signal using np.convolve with weights 1/m](29-todo-compute-the-filtered-signal-using-np-convolve-with-weig.md) · [Up: contents](index.md) · [Plot frequency domain →](31-plot-frequency-domain.md)
