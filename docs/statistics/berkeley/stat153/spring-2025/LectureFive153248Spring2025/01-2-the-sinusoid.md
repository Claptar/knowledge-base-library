---
title: 2 The Sinusoid
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFive153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureFive153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureFive153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureFive153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 The Sinusoid

### Lecture Five
Spring 2025, UC Berkeley

Aditya Guntuboyina

February 4, 2025

## 1 Nonlinear Regression

Today, we shall start our discussion on models in which certain parameters appear in nonlinear fashion. The simplest example is the sinusoidal model which we attempt to fit to the sunspots data. Before we start discussing the sinusoidal model, let us review the basic sinusoid functions.

When we say sinusoid, we refer to the following function of time ($t$):
$$s(t) := R \cos(2\pi f t + \phi) \tag{1}$$
$R$ is called the *amplitude*, $f$ is called the *frequency* and $\Phi$ is called the *phase*. The quantity $1/f$ is called the *period* and $2\pi f$ is termed the *angular frequency*. Sometimes, we shall use the notation $\omega = 2\pi f$ for the angular frequency.

Using the formula $\cos(\alpha+\beta) = (\cos \alpha)(\cos \beta)-(\sin \alpha)(\sin \beta)$, we can represent the sinusoid (1) in the following equivalent alternative form:
$$s(t) = A \cos 2\pi f t + B \sin 2\pi f t. \tag{2}$$
The parameters $A, B$ in (2) are related to $R, \phi$ in (1) via $A = R \cos \phi$ and $B = R \sin \phi$. While working with models involving sinusoids, we use the representation (2) because the parameters $A$ and $B$ appear linearly in (2).

### 2.1 Discrete sampling and restricting $f$ to $[0, 1/2]$

Often in time series analysis, we work with equally spaced time points and assume that the time variable $t$ takes the values $1, \dots, n$ (where $n$ is the sample size). It turns out that if we consider the sinusoid (1) and restrict the time $t$ to $1, \dots, n$, then we can always constrain the frequency parameter $f$ to $[0, 1/2]$. This is a consequence of the following result.

**Fact 2.1.** *For every $f \in (-\infty, \infty)$ and $\phi \in (-\infty, \infty)$, there exists $f_0 \in [0, 1/2]$ and $\phi_0 \in (-\infty, \infty)$ such that*
$$s(t) = R \cos(2\pi f t + \phi) = R \cos(2\pi f_0 t + \phi_0) \quad \text{for all } t = 1, \dots, n.$$

*Proof.* Consider the following three cases.

1. If $f < 0$, then we can write $\cos(2\pi f t + \phi) = \cos(2\pi(-f)t - \phi)$. Clearly, $-f \ge 0$.
2. If $f \ge 1$, then we write (below $[f]$ is the largest integer less than or equal to $f$):
$$\cos(2\pi f t + \phi) = \cos(2\pi [f]t + 2\pi(f - [f])t + \phi) = \cos(2\pi(f - [f])t + \phi),$$
because $\cos(\cdot)$ is periodic with period $2\pi$. Clearly $0 \le f - [f] < 1$.
3. If $f \in [1/2, 1)$, then
$$\cos(2\pi f t + \phi) = \cos(2\pi t - 2\pi(1 - f)t + \phi) = \cos(2\pi(1 - f)t - \phi)$$
because $\cos(2\pi t - x) = \cos x$ for all integers $t$. Clearly $0 < 1 - f \le 1/2$.

Thus the sinusoid $R \cos(2\pi f t + \phi)$ equals $R \cos(2\pi f_0 t + \phi_0)$ at all integers $t$ for some $0 \le f_0 \le 1/2$ and a phase $\phi_0$ that is possibly different from $\phi$. $\square$

From now on, when we discuss sinusoids $s(t) = R \cos(2\pi f t + \phi)$ in the context of $t = 1, \dots, n$, we shall assume that the frequency parameter $f$ is restricted to $[0, 1/2]$. Note also the behavior of the sinusoid for the two frequency extremes $f = 0$ and $f = 1/2$. When $f = 0$, the sinusoid $s(t)$ is simply a constant function equal to $R \cos(\phi)$. When $f = 1/2$, we have
$$s(t) = R \cos(\pi t + \phi) = R(\cos \phi)\cos(\pi t) = R(-1)^t \cos \phi.$$
This sinusoid exhibits the maximum possible oscillation going back and forth between $R \cos \phi$ and $-R \cos \phi$.

---

[Up: contents](index.md) · [3 The sinusoidal model →](02-3-the-sinusoidal-model.md)
