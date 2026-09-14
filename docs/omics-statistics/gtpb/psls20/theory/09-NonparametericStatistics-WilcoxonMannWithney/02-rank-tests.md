---
title: Rank Tests
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd
source_file: sources/gtpb-psls20/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Rank Tests

**Source:** [`theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-WilcoxonMannWithney.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Important group of non-parametric test
  - Non-parametric,
  - Exact $p$-values using a permutation null distribution.
  - No need for separate permutation distribution for each new dataset.
  - Permutation null distribution of rank tests only depends on sample size
  - Robust to outliers

---

#Ranks

Rank tests start from rank-transformed data.

- Let $Y_1, \ldots, Y_n$.
- In the absence of *ties*
  $$R_i=R(Y_i) = \#\{Y_j: Y_j\leq Y_i; j=1,\ldots, n\}$$
- Smallest observation has rank 1, second smallest rank 2, ... , largest observation gets rank $n$

```r
chol$cholest
rank(chol$cholest)
```

---

## ties

Sometimes *ties* occur: two observations with identical values

```r
withTies=c(403,507,507,610,651,651,651,830,900)
rank(withTies)
```

- Ties: 507 occurs twice, 651 occurs 3 times
- If ties occur *midranks* are used.

- **midrank** of observation $Y_i$ becomes
  \begin{eqnarray*}
   R_i &=& \frac{ \#\{Y_j: Y_j\leq Y_i\} + ( \#\{Y_j: Y_j < Y_i\} +1)}{2}.
   \end{eqnarray*}

---

## Ranks of pooled sample

- Let $Y_{ij}$, $i=1,\ldots, n_j$ be observations from two treatment groups $j=1,2$.
- They can also be represented by $Z_1,\ldots, Z_n$ ($n=n_1+n_2$), the outcomes of the pooled sample

```r
t(chol)
z=chol$cholest
z
rank(z)
```
---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Wilcoxon-Mann-Whitney Test →](03-wilcoxon-mann-whitney-test.md)
