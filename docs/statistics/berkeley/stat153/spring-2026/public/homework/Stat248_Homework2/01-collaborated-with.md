---
title: Collaborated with
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat248_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat248_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat248_Homework2.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Collaborated with

## Student ID: {-}

## Collaborated with: {-}

Due March 3 at 11:59pm. Grading will be completed within 14 days of the late deadline (remember you have 120 late hours you can use across the semester).

*Instructions:* Please complete the homework by filling out this Jupyter notebook and exporting the final file as a PDF or .html file. (Go to File menu -> Save and Export Notebook as -> choose PDF or html, save, and upload this file as your submission.

You should ideally write out your solutions as markdown / LaTeX within this notebook. If you do decide to include any handwritten notes, these must be incorporated into one PDF (including all your code, solutions, etc) and each problem must be clearly labeled with the question number. Everything must be submitted as one single PDF. Points will be deducted if questions are not clearly labeled and formatting guidelines are not followed.

Remember, if you collaborated with anyone, you should list their names on this document, but your answers must be your own (unique, not a copy of/identical to a friend's). This homework will be graded for completion, so while you may use external tools to help you in completing it, it is recommended that you try to figure out the solutions and understand them yourself.

```python
# Some imports that will probably be helpful for you

import numpy as np
from matplotlib import pyplot as plt
#!pip install astsa # Uncomment if you don't have this
import astsa
import statsmodels.api as sm
```

## Q1. Multiple linear regression equations

In class, we showed that the solution for multiple linear regression of responses $y$ and feature vectors $x_i \in \mathbb{R}^p$, $i=1,\dots, n$ could be written in two ways:

$$\hat{\beta} = \left( \displaystyle\sum_{i=1}^n x_i x_i^T \right)^{-1} \displaystyle\sum_{i=1}^n x_i y_i$$

or in matrix notation as:

$$\hat{\beta} = (X^\intercal X)^{-1}X^\intercal y$$

Where $X$ is a matrix of size $(n\times p)$, with $i^{\text{th}}$ row $x_i$, and $y$ is a response vector with $i^{\text{th}}$ component $y_i$. Prove that these two expressions are equivalent (3 points).

---

[Up: contents](index.md) · [Q2. Choosing covariates for multiple linear regression →](02-q2-choosing-covariates-for-multiple-linear-regression.md)
