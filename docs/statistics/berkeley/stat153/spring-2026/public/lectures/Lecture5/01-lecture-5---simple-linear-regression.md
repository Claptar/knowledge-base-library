---
title: Lecture 5 - Simple linear regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 5 - Simple linear regression

**Source:** [`public/lectures/Lecture5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

```python
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import statsmodels.api as sm # This contains the model fitting libraries for linear regression
from statsmodels.graphics.tsaplots import plot_acf # autocorrelation function

#!pip install astsa
import astsa # You should have pip installed this for Lab 1.. if not, uncomment line above

---

[Up: contents](index.md) · [Set the random seed, this is so you will generate the same answers →](02-set-the-random-seed-this-is-so-you-will-generate-the-same-an.md)
