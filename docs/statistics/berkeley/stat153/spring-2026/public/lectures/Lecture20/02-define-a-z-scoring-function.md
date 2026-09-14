---
title: Define a z-scoring function
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture20.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Define a z-scoring function

**Source:** [`public/lectures/Lecture20.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture20.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

zs = lambda x: (x-x.mean(0))/x.std(0)
```

## Get the data!

Here we will load in the data from our experiment. We have neural data `ytrain` and `ytest`, which are matrices of dimension `[time points x electrodes]`, where each electrode is taken from a session where a patient with epilepsy was listening to a set of movie clips. Here we will look at data from 3 example electrodes from one patient listening to movie clips.

<img src="./images/20_electrodes.png" width=500px alt="image of electrodes in the brain for this dataset"/>

```python
data_file = 'MTdata_TCH28.hf5'

---

[← Stat 153/248 Lecture 20](01-stat-153-248-lecture-20.md) · [Up: contents](index.md) · [Here we will read in the contents of the file →](03-here-we-will-read-in-the-contents-of-the-file.md)
