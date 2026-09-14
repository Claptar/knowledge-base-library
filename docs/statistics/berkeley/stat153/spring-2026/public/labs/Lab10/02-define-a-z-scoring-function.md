---
title: Define a z-scoring function
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab10.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Define a z-scoring function

**Source:** [`public/labs/Lab10.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab10.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

zs = lambda x: (x-x.mean(0))/x.std(0)
```

## Get the data!

Here we will load in the data from our experiment. We have neural data `ytrain` and `ytest`, which are matrices of dimension `[time points x electrodes]`, where each electrode is taken from a session where a patient with epilepsy was listening to a set of movie clips. Here we will look at data from 3 example electrodes from one patient listening to movie clips.

```python

---

[← Lab 10](01-lab-10.md) · [Up: contents](index.md) · [Lab10 Part 03 — →](03-lab10-part-03.md)
