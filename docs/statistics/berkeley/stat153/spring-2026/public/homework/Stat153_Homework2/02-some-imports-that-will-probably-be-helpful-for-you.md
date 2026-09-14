---
title: Some imports that will probably be helpful for you
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Some imports that will probably be helpful for you

**Source:** [`public/homework/Stat153_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework2.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

## Q2. Choosing covariates for multiple linear regression

In class (Lectures 7 + 8), we fit a multiple linear regression model to predict data from students in the class performing a finger tapping exercise where you clicked as fast as possible using your left hand or right hand, doing the task separately for index finger and pinky finger. We collected data on which hand the person used to complete the task (left/right), which finger (index/pinky), what hand each person uses to write with / their dominant hand (left/right), and some other demographic factors. For one model, we predicted the total number of taps (`ntaps`) as a function of hand dominance, index vs. pinky finger, whether the person was a gamer or not, how much sleep they got, and how many years they participated in sports. For this particular example, we always had each person use the same hand for the finger tapping.

**Q2a. What would happen if we fit our regression using handedness, hand, and finger as covariates in this scenario? Can we uniquely attribute variance to these predictors? Explain using the solutions for OLS. (3 points)**

**Q2b. In Lab 4, we showed that adding predictors increases $R^2$. This can contribute to overfitting, which we also discuss in Lecture 10 and 11. Prove that $R^2$ never decreases when you add a predictor, and explain why adjusted $R^2$ can. (2 points)**

## Q3. Sinusoidal regression

**Q3a. Fit a sinusoidal regression $y = R \cos (2\pi f t +\phi) + \epsilon$ to the sunspots dataset from ASTSA assuming one major oscillation frequency $f$. Do a grid search over possible values of $f$, explaining how you chose this range, then evaluate what is the best $f$ and fit the regression via OLS. Report the $\beta$ parameters, then re-derive $R$ and $\phi$. Comment on the units for these measurements and verify that they make sense for the problem. Also plot your predicted sunspot data on top of the true data and label. (7 points)**

```python
sunspots = astsa.load_sunspotz()
t = sunspots['Time']
y = sunspots['Value']

plt.plot(t,y)
plt.xlabel('Time (year)')
plt.ylabel('Sunspots')

---

[← Stat 153 - Homework 2 - YOUR NAME HERE](01-stat-153---homework-2---your-name-here.md) · [Up: contents](index.md) · [INSERT CODE HERE →](03-insert-code-here.md)
