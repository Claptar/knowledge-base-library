---
title: their left index finger for the first part of the task
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# their left index finger for the first part of the task

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

df_all
```

```
Unnamed: 0  tap_index  t_seconds  dt_seconds  subj finger   hand  \
0               0          1      0.000       0.000     0  index   left
1               1          2      0.149       0.149     0  index   left
2               2          3      0.316       0.167     0  index   left
3               3          4      0.483       0.167     0  index   left
4               4          5      0.634       0.151     0  index   left
...           ...        ...        ...         ...   ...    ...    ...
34108       34108        343     58.878       0.188   100  index  right
34109       34109        344     59.058       0.180   100  index  right
34110       34110        345     59.229       0.171   100  index  right
34111       34111        346     59.411       0.182   100  index  right
34112       34112        347     59.591       0.180   100  index  right

      handedness  dominant_hand  time_bin
0           left           True         0
1           left           True         0
2           left           True         0
3           left           True         0
4           left           True         0
...          ...            ...       ...
34108      right           True         5
34109      right           True         5
34110      right           True         5
34111      right           True         5
34112      right           True         5

[34113 rows x 10 columns]
```

```python

---

[← For example, the first several rows are from subj 0, who is left handed and used](05-for-example-the-first-several-rows-are-from-subj-0-who-is-le.md) · [Up: contents](index.md) · [dfbins is the binned data when we use 10 second bins -- this is very →](07-dfbins-is-the-binned-data-when-we-use-10-second-bins----this.md)
