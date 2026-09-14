---
title: Spectral analysis
source: https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd
source_file: sources/berkeley-stat153/fall-2024/homeworks/homework3/homework3.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Spectral analysis

**Source:** [`homeworks/homework3/homework3.Rmd`](https://github.com/berkeley-stat153/fall-2024/blob/94c943d315ea7361f1f660f42881d219a7e7f009/homeworks/homework3/homework3.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

10. (3 pts)
Let $\omega_j$, $j = 1,\dots,p$ be fixed and arbitrary frequencies and let
$U_{j1}, U_{j2}$, $j = 1,\dots,p$ be uncorrelated random variables with mean
zero, where $U_{j1}, U_{j2}$ have variance $\sigma^2_j$. Define
$$
x_t = \sum_{j=1}^p \Big( U_{j1} \cos(2\pi\omega_j t) + U_{j2} \sin(2\pi\omega_j t) \Big)
$$
for $t = 1,2,3,\dots$. Prove that this process is stationary, and show that its
auto-covariance function is of the form given in lecture (weeks 7-8, "Spectral
analysis and filtering").

11. (2 pts)
Construct a small empirical example to verify the auto-covariance formula you
derived in Q10. That is, generate a process with at least $p=2$ components.
compute its auto-correlation function with `acf()`, and compare to the analytic
formula you derived.

---

[← (as a sanity check) at a particular value of lambda in the middle of the grid](11-as-a-sanity-check-at-a-particular-value-of-lambda-in-the-mid.md) · [Up: contents](index.md)
