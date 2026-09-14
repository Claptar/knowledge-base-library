---
title: P-values
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd
source_file: sources/statomics-sga21/technicalDetailsProteomics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# P-values

**Source:** [`technicalDetailsProteomics.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Simulation under H_0.

- Mean log2 protein intensity for atrium equals mean log2 protein intensity for ventriculum in the left heart region.
- sd equals the sd for the protein.


1. Extract $\hat \sigma$ and $\beta$'s
```r
sd <- sapply(
  rowData(pe[["proteinRobust"]])$msqrobModels,
  getSigma) %>%
  na.exclude

coefs <-
sapply(rowData(pe[["proteinRobust"]])$msqrobModels,
    function(x) getCoef(x)[1:nCoefs]
  ) %>%
  t %>%
  na.exclude
```

2. Set $\beta_\text{tissue}$ equal to 0. No FC between atrium and ventriculum left.

```r
coefs0 <- coefs
coefs0[,3] <- 0
```

3. Simulate protein expressions for each protein from a Normal distribution under $H_0$ for left heart region (no FC between atrium and ventriculum left) and sd the sd for the protein.
```r
set.seed(104)
f0 <- sapply(1:p,
  function(i, betas, sd, design)
  rnorm(n, mean = design %*% betas[i,], sd = sd[i]),
  betas = coefs0,
  sd = sd,
  design = X
  ) %>%
  t
colnames(f0) <- colnames(pe[[1]])
```

4. Setup QFeatures object and perform MSqRob analysis

```r
sims <- readQFeatures(f0 %>% as.data.frame, ecol = 1:n, name = "sim0")
colData(sims) <- colData(pe)
sims <- msqrob(object = sims, i = "sim0", formula = ~ location*tissue + patient)
sims <- hypothesisTest(object = sims, i = "sim0", contrast = L)
```

### Evaluate  pvalues  under H_0

```r
volcano <- ggplot(rowData(sims[["sim0"]])$tissueV,
                 aes(x = logFC, y = -log10(pval), color = pval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) + theme_minimal()
volcano
```

Number of false positives without multiple testing?

```r
rowData(sims[["sim0"]])$tissueV %>%
  filter(pval <0.05) %>%
  nrow
mean(rowData(sims[["sim0"]])$tissueV$pval < 0.05)
hist(rowData(sims[["sim0"]])$tissueV$pval,main = "simulation H0")
```


- The p-values are uniform!
- All p-values under the null are equally likely.
- Statistical hypthesis testing leads to a uniform test strategy under $H_0$
- If use p-value cutoff at 0.05 we expect to return 5% of the non-DE proteins  as differentially expressed: many false positives can be expected!


## Pvalue distribution in real experiment

```r
hist(rowData(pe[["proteinRobust"]])$tissueV$pval, main = "realData")
```

- A mixture of null proteins (non-DE): uniform, and, DE proteins: enrichment of p-values at low p-values

---

[← Empirical Bayes/Moderated $t$-test.](04-empirical-bayes-moderated--test.md) · [Up: contents](index.md) · [Correction for multiple testing →](06-correction-for-multiple-testing.md)
