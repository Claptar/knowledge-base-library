---
title: Generate a realization.
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit10-linalg.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Generate a realization.

**Source:** [`units/unit10-linalg.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit10-linalg.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

evals = e[0]
evals = 1/evals   # variances
evals[3] = 0      # generalized inverse
rng = np.random.default_rng(seed=1)
y = e[1] @ ((evals ** 0.5) * rng.normal(size = 5))
y.sum()
```

In the second order case, we have two non-identifiabilities: for the sum
and for the linear component of the variation in $y$ (linear in the
indices of $y$).

I could parameterize a statistical model as $\mu+y$ where $y$ has
covariance that is the generalized inverse discussed above. Then I allow
for both a non-zero mean and for smooth variation governed by the
autoregressive structure. In the second-order case, I would need to add
a linear component as well, given the second non-identifiability.

## Matrices arising in regression

In regression, we work with $X^{\top}X$. Some properties of this matrix
are that it is symmetric and non-negative definite (hence our use of
$(X^{\top}X)^{-1}$ in the OLS estimator). When is it not positive
definite?

Fitted values are $X\hat{\beta}=X(X^{\top}X)^{-1}X^{\top}Y=HY$. The
"hat" matrix, $H$, projects $Y$ into the column space of $X$. $H$ is
idempotent: $HH=H$, which makes sense - once you've projected into the
space, any subsequent projection just gives you the same thing back. $H$
is singular. Why? Also, under what special circumstance would it not be
singular?

---

[← 2. Statistical interpretations of matrix invertibility, rank, etc.](04-2-statistical-interpretations-of-matrix-invertibility-rank-e.md) · [Up: contents](index.md) · [3. Computational issues →](06-3-computational-issues.md)
