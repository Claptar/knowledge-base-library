---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab1.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`public/labs/Lab1.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab1.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

# Lab 1 - Stat 153/248

For this lab, we will give some practical examples for concepts related to time series characteristics discussed in Lectures 1 and 2. This will include the following concepts:

1. Loading data from the `astsa` library (from your Time Series book)
2. Generating white noise
3. Computing moving averages
4. Generating data from an autoregressive process
5. Random walks and random walks + drift

For this lab, you will fill in the aspects of the code marked `...` or with the comment `# FILL IN`

```python
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
!pip install astsa # Only need to do this if you don't have it installed already
import astsa

# Set the random seed, this is so you will generate the same answers
# each time (for example, when generating white noise)
np.random.seed(42)
```

# Data from Time Series Analysis and Its Applications

First, we will use the `astsa` library to load and plot some of the data from Chapter 1. You can use this library yourself if you are interested in looking further at any of the examples.

As we go on, you can think about how to fit models to these data or test assumptions about these data.

```python
# Let's print all the possible datasets we could load from the book
# These are functions named `load_X`

dir(astsa.datasets)
```

---

[Up: contents](index.md) · [Dow Jones Industrial Average Data →](02-dow-jones-industrial-average-data.md)
