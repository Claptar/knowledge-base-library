---
title: Google form data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Google form data

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We also collected data from our google form on sports, gaming, and sleep. Let's look at that here:

```python
google_form
```

```
Unnamed: 0  ntaps handedness finger   hand gamer  sleep_hrs  sport  \
0            0    338      Right  Pinky   Left    No       7.00      0
1            1    398      Right  Index  Right    No       6.00      8
2            2    364      Right  Index  Right    No       5.00      0
3            3    409      Right  Pinky  Right   Yes       4.00      7
4            4    304      Right  Index   Left    No       5.83      2
..         ...    ...        ...    ...    ...   ...        ...    ...
60          60    360      Right  Index  Right    No       6.00      5
61          61    271       Left  Pinky  Right    No       6.00      4
62          62    425      Right  Index  Right    No       8.00      4
63          63    328      Right  Index   Left    No       8.50      7
64          64    424      Right  Pinky  Right    No       8.00      4

    dominant_hand
0           False
1            True
2            True
3            True
4           False
..            ...
60           True
61          False
62           True
63          False
64           True

[65 rows x 9 columns]
```

---

[← Plots to look at balance within our data](23-plots-to-look-at-balance-within-our-data.md) · [Up: contents](index.md) · [Investigate other model effects →](25-investigate-other-model-effects.md)
