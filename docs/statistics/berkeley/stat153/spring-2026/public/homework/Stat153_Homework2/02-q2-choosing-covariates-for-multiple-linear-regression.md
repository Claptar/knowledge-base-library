---
title: Q2. Choosing covariates for multiple linear regression
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework2.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/homework/Stat153_Homework2.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/homework/Stat153_Homework2.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/homework/Stat153_Homework2.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Q2. Choosing covariates for multiple linear regression

In class (Lectures 7 + 8), we fit a multiple linear regression model to predict data from students in the class performing a finger tapping exercise where you clicked as fast as possible using your left hand or right hand, doing the task separately for index finger and pinky finger. We collected data on which hand the person used to complete the task (left/right), which finger (index/pinky), what hand each person uses to write with / their dominant hand (left/right), and some other demographic factors. For one model, we predicted the total number of taps (`ntaps`) as a function of hand dominance, index vs. pinky finger, whether the person was a gamer or not, how much sleep they got, and how many years they participated in sports. For this particular example, we always had each person use the same hand for the finger tapping.

**Q2a. What would happen if we fit our regression using handedness, hand, and finger as covariates in this scenario? Can we uniquely attribute variance to these predictors? Explain using the solutions for OLS. (3 points)**

**Q2b. In Lab 4, we showed that adding predictors increases $R^2$. This can contribute to overfitting, which we also discuss in Lecture 10 and 11. Prove that $R^2$ never decreases when you add a predictor, and explain why adjusted $R^2$ can. (2 points)**

---

[← Collaborated with](01-collaborated-with.md) · [Up: contents](index.md) · [Q3. Sinusoidal regression →](03-q3-sinusoidal-regression.md)
