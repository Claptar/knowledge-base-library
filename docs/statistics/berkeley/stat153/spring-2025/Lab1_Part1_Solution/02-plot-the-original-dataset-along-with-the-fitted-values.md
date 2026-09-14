---
title: Plot the original dataset along with the fitted values
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part1_Solution.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab1_Part1_Solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the original dataset along with the fitted values

**Source:** [`Lab1_Part1_Solution.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab1_Part1_Solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (10, 6))
plt.plot(t, uspop['POPTHM'], label = 'US population', color = 'blue')
plt.plot(t, lin_model.fittedvalues, label = 'Linear Fit', color = 'red')
plt.xlabel("Time (months)")
plt.ylabel("US Population (in thousands)")
plt.title("US Population")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [USA Accidents Dataset →](03-usa-accidents-dataset.md)
