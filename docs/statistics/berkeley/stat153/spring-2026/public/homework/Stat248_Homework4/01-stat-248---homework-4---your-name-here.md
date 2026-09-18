---
title: Stat 248 - Homework 4 - YOUR NAME HERE
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework4.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework4.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework4.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Stat 248 - Homework 4 - YOUR NAME HERE

### Student ID: {-}

### Collaborated with: {-}

Due April 23 at 11:59pm. Grading will be completed within 14 days of the late deadline (remember you have 120 late hours you can use across the semester).

*Instructions:* Please complete the homework by filling out this Jupyter notebook and exporting the final file as a PDF or .html file. (Go to File menu -> Save and Export Notebook as -> choose PDF or html, save, and upload this file as your submission.

**Note: For this homework, if you are in the graduate section of the course you also have an assignment due soon for the final project, so you have the option of completing at least 5 out of 6 questions to receive full credit.**

You should ideally write out your solutions as markdown / LaTeX within this notebook. If you do decide to include any handwritten notes, these must be incorporated into one PDF (including all your code, solutions, etc) and each problem must be clearly labeled with the question number. Everything must be submitted as one single PDF. Points will be deducted if questions are not clearly labeled and formatting guidelines are not followed.

Remember, if you collaborated with anyone, you should list their names on this document, but your answers must be your own (unique, not a copy of/identical to a friend's). This homework will be graded for completion, so while you may use external tools to help you in completing it, it is recommended that you try to figure out the solutions and understand them yourself.

```python
# Some imports that might be useful to you
import numpy as np
!pip install h5py
!pip install astsa
import h5py
import astsa # Necessary for loading data for some Qs (may need to do !pip install astsa)
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.arima.model import ARIMA
```

## Q1. MA model properties

For an MA(1), $x_t =w_t + \theta w_{t−1}$, show that $\rho_x(1)| \leq 1/2$ for any number $\theta$. For which values of $\theta$ does $\rho_x(1)$ attain its maximum and minimum?

**Answer:** Fill in here

---

[Up: contents](index.md) · [Q2. ARMA model parameterization →](02-q2-arma-model-parameterization.md)
