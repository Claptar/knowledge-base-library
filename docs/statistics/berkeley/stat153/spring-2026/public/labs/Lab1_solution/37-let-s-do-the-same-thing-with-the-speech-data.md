---
title: Let's do the same thing with the speech data
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Let's do the same thing with the speech data

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

speech_data = astsa.load_speech()
speech_data
```

```
Time  Value
0        1   1814
1        2   1556
2        3   1442
3        4   1416
4        5   1352
...    ...    ...
1015  1016   2119
1016  1017   2044
1017  1018   1945
1018  1019   1886
1019  1020   1879

[1020 rows x 2 columns]
```

```python
plt.plot(speech_data['Value'])

---

[← Does this change how you might interpret the data?](36-does-this-change-how-you-might-interpret-the-data.md) · [Up: contents](index.md) · [Plot the smoothed speech data →](38-plot-the-smoothed-speech-data.md)
