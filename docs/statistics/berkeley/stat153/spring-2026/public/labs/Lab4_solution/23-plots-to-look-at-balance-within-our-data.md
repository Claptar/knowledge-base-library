---
title: Plots to look at balance within our data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plots to look at balance within our data

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Are we sampling evenly across handedness? Around 10-12% of the world's population is left-handed, so we should expect that to be roughly the case for the data we get here. Let's see if that pans out.

```python
sns.countplot(x='handedness', data=summary_df)
```

```
<Axes: xlabel='handedness', ylabel='count'>
```

*(1 figure omitted — see the original notebook.)*

We do indeed have an imbalance in the data, with many more right-handed people than left-handed people. If we ran a regression just looking at whether using your right hand helps, it would show that there is a strong positive effect, but this is drive by the fact that we are mostly running this on right-handed people! So remember to think about how to interpret your coefficients in the context of your actual data.

Let's also just plot which hand the person used to do the task, and whether it was their dominant hand:

```python
sns.countplot(x='hand', data=summary_df, hue='dominant_hand')
```

```
<Axes: xlabel='hand', ylabel='count'>
```

*(1 figure omitted — see the original notebook.)*

---

[← FILL IN](22-fill-in.md) · [Up: contents](index.md) · [Google form data →](24-google-form-data.md)
