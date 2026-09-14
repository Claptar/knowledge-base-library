---
title: each time (for example, when generating white noise)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# each time (for example, when generating white noise)

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

np.random.seed(42)
```

```
Requirement already satisfied: astsa in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (0.1)
Requirement already satisfied: pandas in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from astsa) (2.3.3)
Requirement already satisfied: numpy>=1.22.4 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from pandas->astsa) (2.2.6)
Requirement already satisfied: python-dateutil>=2.8.2 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from pandas->astsa) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from pandas->astsa) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from pandas->astsa) (2025.3)
Requirement already satisfied: six>=1.5 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from python-dateutil>=2.8.2->pandas->astsa) (1.17.0)
```

---

[← Set the random seed, this is so you will generate the same answers](02-set-the-random-seed-this-is-so-you-will-generate-the-same-an.md) · [Up: contents](index.md) · [Data from Time Series Analysis and Its Applications →](04-data-from-time-series-analysis-and-its-applications.md)
