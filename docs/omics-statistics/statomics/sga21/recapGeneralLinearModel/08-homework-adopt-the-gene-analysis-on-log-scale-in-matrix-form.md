---
title: 'Homework: Adopt the gene analysis on log scale in matrix form!'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd
source_file: sources/statomics-sga21/recapGeneralLinearModel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Homework: Adopt the gene analysis on log scale in matrix form!

**Source:** [`recapGeneralLinearModel.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

1. Study the solution of the exercise to understand the analysis in R


2. Calculate
- model parameters and contrasts of interest
- standard errors, standard errors on contrasts
- t-test statistics on the model parameters and contrasts of interest

3. Compare your results with the output of the lm(.) function


---

## Inspiration

Tip: details on the implementation can be found in the book of Faraway (chapter 2). https://people.bath.ac.uk/jjf23/book/

- Design matrix

```r
X <- model.matrix(~grade*node,data=gene)
```

- Transpose of a matrix: use function t(.)

```r
t(X)
```

- Matrix product %\*% operator

```r
t(X)%*%X
```

- Degrees of freedom of a model?

$$ df =  n-p$$

```r
summary(lm1)
dfRes <- (nrow(X)-ncol(X))
dfRes
```

- Variance estimator: MSE

$$
\hat \sigma^2 = \frac{\sum\limits_{i=1}^n\epsilon_i^2}{n-p}
$$


- Invert matrix: use function solve(.)

- Diagonal elements of a matrix: use function diag(.)

```r
t(X)%*%X
diag(t(X)%*%X)
```

---

[← fitted points for droplines to surface](07-fitted-points-for-droplines-to-surface.md) · [Up: contents](index.md)
