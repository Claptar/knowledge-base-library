---
title: These are functions named loadX
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# These are functions named loadX

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

dir(astsa.datasets)
```

```
['__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'load_EQ5',
 'load_EXP6',
 'load_Hare',
 'load_Lynx',
 'load_chicken',
 'load_djia',
 'load_fmri1',
 'load_gtemp_land',
 'load_gtemp_ocean',
 'load_jj',
 'load_rec',
 'load_soi',
 'load_speech',
 'load_sunspotz',
 'utils']
```

## Dow Jones Industrial Average Data

```python
import matplotlib.dates as mdates
locator = mdates.AutoDateLocator(minticks=7, maxticks=10)

djia_data = astsa.load_djia()

---

[← Let's print all the possible datasets we could load from the book](05-let-s-print-all-the-possible-datasets-we-could-load-from-the.md) · [Up: contents](index.md) · [Calculate the return →](07-calculate-the-return.md)
