---
title: 7 Combinatorial optimization over discrete spaces
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit11-optim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7 Combinatorial optimization over discrete spaces

**Source:** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit11-optim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Many statistical optimization problems involve continuous domains, but sometimes there are problems in which the domain is discrete. Variable selection is an example of this.

_Simulated annealing_ can be used for optimizing in a discrete space. Another approach uses _genetic algorithms_ , in which one sets up the dimensions as loci grouped on a chromosome and has mutation and crossover steps in which two potential solutions reproduce. An example would be in high-dimensional variable selection.

_Stochastic search variable selection_ is a popular Bayesian technique for variable selection that involves MCMC.

---

[← 6 Basic optimization in R](14-6-basic-optimization-in-r.md) · [Up: contents](index.md) · [8 Convexity →](16-8-convexity.md)
