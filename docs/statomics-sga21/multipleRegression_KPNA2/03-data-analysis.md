---
title: Data analysis
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd
source_file: sources/statomics-sga21/multipleRegression_KPNA2.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Data analysis

**Source:** [`multipleRegression_KPNA2.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Import KPNA2 data in R
```r
kpna2 <- read.table("https://raw.githubusercontent.com/statOmics/SGA21/master/data/kpna2.txt",header=TRUE)
kpna2
```

## Transform the variable grade and node to a factor
```r
kpna2$grade <- as.factor(kpna2$grade)
kpna2$node <- as.factor(kpna2$node)
```

## Data exploration
Histologic grade and lymph node status can be associated with the kpna2 gene expression. Moreover, it is also possible that the differential expression associated with histological grade is different in patients that have unaffected lymph nodes and patients for which the lymph nodes had to be removed.

```r
kpna2 %>%
  ggplot(aes(x=node:grade,y=gene,fill=node:grade)) +
  geom_boxplot(outlier.shape = NA) +
  geom_jitter()
```

The plot suggests

- An effect of the histological grade
- An effect of node status
- The differential expression associated to grade seems to differ according to the lymph node status (interaction)
- Mean variance relation?

## Model

Histologic grade and lymph node status can be associated with the kpna2 gene expression. Moreover, it is also possible that the differential expression associated with histological grade is different in patients that have unaffected lymph nodes and patients for which the lymph nodes had to be removed. Hence, we will have to model the gene expression by using main effects for grade, node and a grade x node interaction.

```r
#Model with main effects for histological grade and node and grade x node interaction
fit <- lm(gene~grade*node,data=kpna2)
plot(fit)
```

The variance seems to increase with the mean.
The QQ-plot of the residuals shows deviations from normality or some outliers.

We will first log transform the data.


```r
fit <- lm(gene %>% log2~grade*node,data=kpna2)
plot(fit)
```

- The variance is now more or less equal for every treatment x node combination.
- The QQ-plot of the residuals shows no deviations from normality.


```r
library(car)
Anova(fit,type="III")
```

The output shows that there is a very significant interaction ($p=$ `r format(Anova(fit,type="III")["grade:node",4],digits=2)`). Hence, the association of the histological grade on the gene expression differs according to the lymph node status and vice versa.


The researchers are therefore interested in studying and reporting on the following hypotheses:

- Is the KPNA2 expression on average different between grade 3 and grade 1 tumors from patients with unaffected lymph nodes (by testing $H_0: \log_2{FC}_{g3n0-g1n0}=0\text{ vs }H1: \log_2{FC}_{g3n0-g1n0}\neq 0$)
- Is the KPNA2 expression on average different between grade 3 and grade 1 tumors from patients with affected lymph nodes (by testing $H_0: \log_2{FC}_{g3n1-g1n1}=0\text{ vs }H1: \log_2{FC}_{g3n1-g1n1}\neq 0$)

- Is the KPNA2 expression on average different in grade 1 tumors of patients with affected and patients with unaffected lymph nodes (by testing $H_0: \log_2{FC}_{g1n1-g1n0}=0\text{ vs }H1: \log_2{FC}_{g1n1-g1n0}\neq 0$)

- Is the KPNA2 expression on average different in grade 3 tumors of patients with affected and patients with unaffected lymph nodes (by testing $H_0: \log_2{FC}_{g3n1-g3n0}=0\text{ vs }H1: \log_2{FC}_{g3n1-g3n0}\neq 0$)

- Is the fold change of the KPNA2 gene between grade 3 and grade 1 different according to the lymph node status and vice versa (tested already by assessing the interaction: $H_0: \log_2{FC}_{g3n0-g1n0}=\log_2{FC}_{g3n1-g1n1} \text{ vs }H1:\log_2{FC}_{g3n0-g1n0}\neq\log_2{FC}_{g3n1-g1n1}$).

---

[← Background](02-background.md) · [Up: contents](index.md) · [Interpretation of model parameters and statistical tests →](04-interpretation-of-model-parameters-and-statistical-tests.md)
