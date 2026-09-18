---
title: Look at the data as a time series
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Look at the data as a time series

What if we want to see how the number of taps changes over time? We can bin the data (though this can be dangerous... so do look at how binning data affects your results). We'll start here by binning our data in 10 second bins and looking at decay over time bins.

```python
bin_size = 10 # in seconds -- you could also change this to something else!
df_all['time_bin'] = (df_all['t_seconds'] // bin_size).astype(int)
df_all

df_bins = ( df_all.groupby(['subj', 'handedness', 'finger','hand','dominant_hand', 'time_bin'])
            .size()
            .reset_index(name='taps_bin')
          )
df_bins
```

```
subj handedness finger   hand  dominant_hand  time_bin  taps_bin
0       0       left  index   left           True         0        66
1       0       left  index   left           True         1        54
2       0       left  index   left           True         2        52
3       0       left  index   left           True         3        55
4       0       left  index   left           True         4        50
..    ...        ...    ...    ...            ...       ...       ...
598   100      right  index  right           True         1        60
599   100      right  index  right           True         2        57
600   100      right  index  right           True         3        57
601   100      right  index  right           True         4        56
602   100      right  index  right           True         5        55

[603 rows x 7 columns]
```

## Examples of how taps change as a function of time bin

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

← Investigate other model effects · [Up: contents](index.md) · [Fitting models →](07-fitting-models.md)
