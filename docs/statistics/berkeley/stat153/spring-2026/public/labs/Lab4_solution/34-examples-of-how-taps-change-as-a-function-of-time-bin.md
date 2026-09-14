---
title: Examples of how taps change as a function of time bin
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Examples of how taps change as a function of time bin

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Again let's do some exploration of the dataset, splitting by different categories.

```python
sns.lineplot(x='time_bin', y='taps_bin', data=df_bins)
```

```
<Axes: xlabel='time_bin', ylabel='taps_bin'>
```

*(1 figure omitted — see the original notebook.)*

```python
sns.lineplot(x='time_bin', y='taps_bin', hue='hand', data=df_bins)
```

```
<Axes: xlabel='time_bin', ylabel='taps_bin'>
```

*(1 figure omitted — see the original notebook.)*

```python
sns.lineplot(x='time_bin', y='taps_bin', hue='finger', data=df_bins)
```

```
<Axes: xlabel='time_bin', ylabel='taps_bin'>
```

*(1 figure omitted — see the original notebook.)*

---

[← Look at the data as a time series](33-look-at-the-data-as-a-time-series.md) · [Up: contents](index.md) · [Fitting models →](35-fitting-models.md)
