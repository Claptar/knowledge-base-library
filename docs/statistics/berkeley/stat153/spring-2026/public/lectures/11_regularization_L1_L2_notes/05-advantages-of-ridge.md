---
title: Advantages of ridge
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/11_regularization_L1_L2_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Advantages of ridge

**Source:** [`public/lectures/11_regularization_L1_L2_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/11_regularization_L1_L2_notes.md) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.md` (lossless)

* Works well when best subset selection is computationally infeasible
* Closed-form solution - fit only a single model (aside from CV repetitions)
* Helpful in situations where there are many parameters and few time points, and where predictors are correlated so we don't necessarily want to get rid of them
* *bias-variance* trade-off: In the case of large $p$ compared to $n$ (either they are close or $p>n$), the OLS solution will be highly variable or won't have a unique solution. As $\lambda$ increases, the flexibility of the ridge regression fit decreases, so we have decreased variance but increased bias.

---

[← Ridge regression solution](04-ridge-regression-solution.md) · [Up: contents](index.md) · [Another flavor - lasso regularization →](06-another-flavor---lasso-regularization.md)
