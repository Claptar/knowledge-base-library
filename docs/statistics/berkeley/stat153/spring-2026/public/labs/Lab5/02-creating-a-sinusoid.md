---
title: Creating a sinusoid
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Creating a sinusoid

**Source:** [`public/labs/Lab5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab5.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

We will first make a sinusoid as we discussed this week in class. This is defined as

$y = \beta_0 + R \cos (2 \pi ft+\phi) + \epsilon$

Where $\epsilon \overset{iid}\sim N(0, \sigma^2)$. We will also specify a sampling rate `fs`, a `duration` of our signal in seconds, and the initial parameters $(\beta_0, f, R, \phi, \sigma)$.

Recall that:

* $\beta_0$ is the intercept that shifts the sinusoid from mean 0.
* $f$ is the frequency of the oscillation (how many peaks in one second)
* $R$ is the amplitude
* $\phi$ is the phase shift
* $\sigma$ is the variance of our white noise signal

```python
fs = 500 # sampling rate
duration = 2
t = np.arange(0,duration,step=1/fs)
B0 = 2
phi = 0
f = 3.2
R =  2.5
var_eps = 0.2 # Variance of white noise

---

[← Stat153/248 - Lab 5](01-stat153-248---lab-5.md) · [Up: contents](index.md) · [Our true sinusoid →](03-our-true-sinusoid.md)
