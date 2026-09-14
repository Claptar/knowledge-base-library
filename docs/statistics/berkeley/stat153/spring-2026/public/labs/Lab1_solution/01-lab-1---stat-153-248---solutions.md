---
title: Lab 1 - Stat 153/248 - Solutions
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1_solution.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lab 1 - Stat 153/248 - Solutions

**Source:** [`public/labs/Lab1_solution.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1_solution.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

For this lab, we will give some practical examples for concepts related to time series characteristics discussed in Lectures 1 and 2. This will include the following concepts:

1. Loading data from the `astsa` library (from your Time Series book)
2. Generating white noise
3. Computing moving averages
4. Generating data from an autoregressive process
5. Random walks and random walks + drift

```python
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
!pip install astsa # Only need to do this if you don't have it installed already
import astsa

---

[Up: contents](index.md) · [Set the random seed, this is so you will generate the same answers →](02-set-the-random-seed-this-is-so-you-will-generate-the-same-an.md)
