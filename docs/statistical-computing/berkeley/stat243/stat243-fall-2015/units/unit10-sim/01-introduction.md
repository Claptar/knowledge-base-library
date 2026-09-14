---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit10-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit10-sim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`units/unit10-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit10-sim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Unit 10: Simulation

October 31, 2015

References:

- Gentle: Computational Statistics

- Monahan: Numerical Methods of Statistics

Many (most?) statistical papers include a simulation (i.e., Monte Carlo) study. The basic idea is that closed-form analysis of the properties of a statistical method/model is often hard to do. Even if possible, it usually involves approximations or simplifications. A canonical situation is that we have an asymptotic result and we want to know what happens in finite samples, but often we do not even have the asymptotic result. Instead, we can estimate mathematical expressions using random numbers. So we design a simulation study to evaluate the method/model or compare multiple methods. The result is that the statistician carries out an experiment, generally varying different factors to see what has an effect on the outcome of interest.

The basic strategy generally involves simulating data and then using the method(s) on the simulated data, summarizing the results to assess/compare the method(s).

Most simulation studies aim to approximate an integral, generally an expected value (mean, bias, variance, MSE, probability, etc.). In low dimensions, methods such as Gaussian quadrature are best for estimating an integral but these methods don’t scale well (we’ll discuss this in Unit 12 on integration/differentiation), so in higher dimensions we often use Monte Carlo techniques.

---

[Up: contents](index.md) · [1 Monte Carlo considerations →](02-1-monte-carlo-considerations.md)
