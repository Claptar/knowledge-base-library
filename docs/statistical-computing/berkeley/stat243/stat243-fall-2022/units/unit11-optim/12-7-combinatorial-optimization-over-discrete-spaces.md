---
title: 7. Combinatorial optimization over discrete spaces
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit11-optim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7. Combinatorial optimization over discrete spaces

**Source:** [`units/unit11-optim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit11-optim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Many statistical optimization problems involve continuous domains, but
sometimes there are problems in which the domain is discrete. Variable
selection is an example of this.

*Simulated annealing* can be used for optimizing in a discrete space.
Another approach uses *genetic algorithms*, in which one sets up the
dimensions as loci grouped on a chromosome and has mutation and
crossover steps in which two potential solutions reproduce. An example
would be in high-dimensional variable selection.

*Stochastic search variable selection* is a popular Bayesian technique
for variable selection that involves MCMC.

---

[← 6. Basic optimization in R](11-6-basic-optimization-in-r.md) · [Up: contents](index.md) · [8. Convexity →](13-8-convexity.md)
