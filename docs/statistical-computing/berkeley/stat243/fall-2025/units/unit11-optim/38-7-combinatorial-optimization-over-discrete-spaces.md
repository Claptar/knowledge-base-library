---
title: 7. Combinatorial optimization over discrete spaces
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 7. Combinatorial optimization over discrete spaces

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

[← Plot the objective function](37-plot-the-objective-function.md) · [Up: contents](index.md) · [8. Convexity →](39-8-convexity.md)
