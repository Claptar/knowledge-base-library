---
title: Interpretation of model parameters and statistical tests
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd
source_file: sources/statomics-sga21/multipleRegression_KPNA2.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Interpretation of model parameters and statistical tests

**Source:** [`multipleRegression_KPNA2.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
ExploreModelMatrix::VisualizeDesign(kpna2,~grade*node)$plotlist
```


```r
summary(fit)
#Calculate confidence intervals for parameters of model
CIfit <- confint(fit)
#log_2 FC between g3n0-g1n0, g1n1-g1n0
#and log_2 difference in FC g3n1-g1n1 and FC g3n0-g1n0
CIfit
#Transform parameters and the CI back to the original scale
2^fit$coef
2^CIfit
2^-fit$coef["grade3:node1"]
2^-CIfit["grade3:node1",]
```

We model the log$_2$-transformed intensities with the following model:
$$
y=\beta_0+\beta_{g3}x_{g3}+\beta_{n1}x_{n1}+\beta_{g3n1}x_{g3}x_{n1},
$$

with $\beta_0$ the intercept, $\beta_{g3}$ the main effect for grade, $x_{g3}$ a dummy variable for grade which is 0 for the control treatment in the absence of grade and 1 for the treatment with grade, $\beta_{n1}$ the main effect for node, $x_{n1}$ a dummy variable that is 0 for the measurements of patients with unaffected lymph nodes and 1 for patients for which the lymph nodes were removed and $\beta_{g3n1}$ the interaction effect between grade and node.
To ease the interpretation of the parameters, $\log_2$ transformed geometric mean intensities are given for each treatment group as well as corresponding contrasts between treatments, which have an interpretation in terms of $\log_2$ transformed fold changes (FC).

- $\log_2\hat{\mu}_{g1n0}=\hat\beta_0$, $\log_2 \hat{\mu}_{g3n0}=\hat\beta_0+\hat\beta_{g3}$ --> $\log_2 \widehat{FC}_{g3n0-g1n0}=\hat\beta_{g3}$

- $\log_2 \hat{\mu}_{g1n1}=\hat\beta_0+\hat\beta_{n1}$, $\log_2 \hat {\mu}_{g3n1}=\hat\beta_0+\hat\beta_{g3}+\hat\beta_{n1}+\hat\beta_{g3n1}$ --> $\log_2 \widehat{FC}_{g3n1-g1n1}=\hat \beta_{g3} +\hat\beta_{g3n1}$

- Similarly, $\log_2 \widehat{FC}_{g1n1-g1n0}=\hat\beta_{n1}$, $\log_2 \widehat{FC}_{g3n1-g3n0}=\hat\beta_{n1}+\hat\beta_{g3n1}$

- $\log_2\frac{\widehat{FC}_{g3n1-g1n1}}{\widehat{FC}_{g3n0-g1n0}}=\log_2\frac{\widehat{FC}_{g3n1-g3n0}}{\widehat{FC}_{g1n1-g1n0}}=\hat\beta_{g3n1}$

with $\log_2\hat{\mu}_{g1n0}$, $\log_2\hat{\mu}_{g3n0}$, $\log_2\hat {\mu}_{g1n1}$ and $\log_2\hat{\mu}_{g3n1}$ the estimated mean $\log_2$ transformed intensity for patients with grade 1 and node 0 status, grade 3 and node 0 status, grade 1 and node 1 status and grade 3 and node 1 status, respectively. With $\log_2 \widehat{FC}_{b-a}$ we indicate $\log_2$ transformed fold change estimates between treatment b and treatment a, i.e. $\log_2 \widehat{FC}_{b-a}=\log_2 \hat{\mu}_{b}-\log_2 \hat{\mu}_a=\log_2 \frac{\hat{\mu}_{b}}{\hat{\mu}_{a}}$.

The model immediately provides statistical tests for assessing the significance of fold changes between grade 3 and grade 1 for patients with unaffected lymph nodes (n=0) $\log_2 {FC}_{g3n0-g1n0}$,  fold changes between the grade 1-node 1 patients and grade 1- node 0 patients $\log_2 {FC}_{g1n1-g3n0}$ and for differences in fold change related to histological grade for node 1 patients and node 0 patients. $\log_2\frac{{FC}_{g3n1-g1n1}}{{FC}_{g3n0-g1n0}}$, the interaction term.

Interpretation of the model parameters in the model output:

- The geometric mean intensity for grade 1 patients with unaffected lymph nodes equals $\exp(\hat \beta_0)$=
`r round(2^fit$coef["(Intercept)"],2)`.
	- When lymph nodes are unaffected, the expression is on average `r round(2^fit$coef["grade3"],2)` times higher for patients with histological grade 3 than patients with histological grade 1.
	- The gene expression in histological grade 1 patients with affected lymph nodes is on average `r round(2^fit$coef["node1"],2)` times higher than for grade 1 patients with unaffected lymph nodes.
- The fold change corresponding to histological grade is on average `r round(1/2^fit$coef["grade3:node1"],2)` times lower in patients with affected lymph nodes as compared to patients with unaffected lymph node.


For the remaining hypothesis of interest we will have to define contrasts: linear combinations of the model parameters and evaluate the contrasts with the multcomp package.

The F-test showed an extremely significant association of the node status, hystological grade and/or the interaction between the node status and the grade (p<<0.001).

---

[← Data analysis](03-data-analysis.md) · [Up: contents](index.md) · [Assessing the significance of all hypothesis of interest →](05-assessing-the-significance-of-all-hypothesis-of-interest.md)
