---
title: Does this change how you might interpret the data?
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Does this change how you might interpret the data?

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

n = 30
plt.plot(djia_data['Close'])
plt.plot(moving_average(djia_data['Close'], n=n))
```

```
[<matplotlib.lines.Line2D at 0x148c85e40>]
```

*(1 figure omitted — see the original notebook.)*

```python

---

[← when you apply the average over a month, a year, etc?](35-when-you-apply-the-average-over-a-month-a-year-etc.md) · [Up: contents](index.md) · [Let's do the same thing with the speech data →](37-let-s-do-the-same-thing-with-the-speech-data.md)
