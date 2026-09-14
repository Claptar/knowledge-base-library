---
title: General Linear Model
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd
source_file: sources/statomics-sga21/recapGeneralLinearModel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# General Linear Model

**Source:** [`recapGeneralLinearModel.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

How can we integrate multiple factors and continuous covariates in linear model.

$$
y_i= \beta_0 + \beta_1 x_{i,1} + \beta_2 x_{i,2} + \beta_{12}x_{i,1}x_{i,2}+\epsilon_i,
$$
with

- $x_{i,1}$ a dummy variable for histological grade: $x_{i,1}=\begin{cases}
0& \text{grade 1}\\
1& \text{grade 3}
\end{cases}$
- $x_{i,2}$ a dummy variable for : $x_{i,2}=\begin{cases}
0& \text{lymph nodes were not removed}\\
1& \text{lymph nodes were removed}
\end{cases}$
- $\epsilon_i$?

---

## Implementation in R

```r
lm1 <- lm(gene~grade*node,data=gene)
summary(lm1)
```

---

## Assumptions

```r
plot(lm1)
```

---

## Breast cancer example

-  Paper: https://doi.org/10.1093/jnci/djj052
- Histologic grade in breast cancer provides clinically important prognostic information. Two factors have to be concidered: Histologic grade (grade 1 and grade 3) and lymph node status (0 vs 1). The researchers assessed gene expression of the KPNA2 gene a protein-coding gene associated with breast cancer and are mainly interested in the association of histological grade. Note, that the gene variable consists of background corrected normalized intensities obtained with a microarray platform. Upon log-transformation, they are known to be a good proxy for the $\log$ transformed concentration of gene expression product of the KPNA2 gene.
- Research questions and translate them towards model parameters (contrasts)?
- Make an R markdown file to answer the research questions


```r
library(ExploreModelMatrix)
explMx <- VisualizeDesign(gene,designFormula = ~grade*node)
explMx$plotlist
```

You can also explore the model matrix interactively:

```r
ExploreModelMatrix(gene,designFormula = ~grade*node)
```
---

---

[← Statistical Inference](03-statistical-inference.md) · [Up: contents](index.md) · [Linear regression in matrix form →](05-linear-regression-in-matrix-form.md)
