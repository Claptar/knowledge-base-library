---
title: Using seaborn to explore our dataset
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab4_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Using seaborn to explore our dataset

**Source:** [`public/labs/Lab4_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab4_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

[Seaborn](https://seaborn.pydata.org/) is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

We'll use it to explore some of the features of our data

```python
!pip install seaborn # Comment out if already installed
import seaborn as sns
```

```
Requirement already satisfied: seaborn in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (0.13.2)
Requirement already satisfied: numpy!=1.24.0,>=1.20 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from seaborn) (2.2.6)
Requirement already satisfied: pandas>=1.2 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from seaborn) (2.3.3)
Requirement already satisfied: matplotlib!=3.6.1,>=3.4 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from seaborn) (3.10.8)
Requirement already satisfied: contourpy>=1.0.1 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.3.2)
Requirement already satisfied: cycler>=0.10 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (4.61.1)
Requirement already satisfied: kiwisolver>=1.3.1 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.4.9)
Requirement already satisfied: packaging>=20.0 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (25.0)
Requirement already satisfied: pillow>=8 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (12.1.0)
Requirement already satisfied: pyparsing>=3 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (3.3.1)
Requirement already satisfied: python-dateutil>=2.7 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from pandas>=1.2->seaborn) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from pandas>=1.2->seaborn) (2025.3)
Requirement already satisfied: six>=1.5 in /Users/liberty/anaconda3/envs/stat153_sp26/lib/python3.10/site-packages (from python-dateutil>=2.7->matplotlib!=3.6.1,>=3.4->seaborn) (1.17.0)
```

```python
sns.lineplot(x='tap_index', y='t_seconds', hue='finger', data=df_all)
```

```
<Axes: xlabel='tap_index', ylabel='t_seconds'>
```

*(1 figure omitted — see the original notebook.)*

```python
sns.violinplot(data=df_all, x='dominant_hand', y='dt_seconds', hue='finger')
```

```
<Axes: xlabel='dominant_hand', ylabel='dt_seconds'>
```

*(1 figure omitted — see the original notebook.)*

```python
summary_df
```

```
Unnamed: 0  subj   hand finger handedness  dominant_hand  ntaps
0             0     0   left  index       left           True    330
1             1     1  right  pinky      right           True    371
2             2     2   left  pinky      right          False    296
3             3     3   left  index      right          False    308
4             4     4  right  index       left          False    301
..          ...   ...    ...    ...        ...            ...    ...
96           96    96   left  pinky      right          False    314
97           97    97   left  index       left           True    355
98           98    98   left  index      right          False    305
99           99    99  right  index      right           True    387
100         100   100  right  index      right           True    347

[101 rows x 7 columns]
```

---

[← later](17-later.md) · [Up: contents](index.md) · [Fitting regression models →](19-fitting-regression-models.md)
