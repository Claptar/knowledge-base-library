---
title: Assessing the significance of all hypothesis of interest
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd
source_file: sources/statomics-sga21/multipleRegression_KPNA2.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Assessing the significance of all hypothesis of interest

**Source:** [`multipleRegression_KPNA2.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

We can assess all contrasts of interest using the multcomp package. This will also allow us to correct for multiple testing, since we assess multiple hypotheses to answer the relevant research question.


- $H_0: \log_2{FC}_{g3n0-g1n0}= \beta_{g3}=0$ $\rightarrow$ "grade3 = 0"
- $H_0: \log_2{FC}_{g3n1-g1n1}= \beta_{g3} + \hat\beta_{g3n1}=0$ $\rightarrow$ "grade3+grade3:node1 = 0"
- $H_0: \log_2{FC}_{g1n1-g1n0}= \beta_{n1}$  $\rightarrow$ "node1 = 0"
- $H_0: \log_2{FC}_{g3n1-g3n0}= \beta_{n1} + \hat\beta_{g3n1}=0$ $\rightarrow$ "node1+grade3:node1 = 0"
- $H_0: \log_2{FC}_{g3n1-g1n1} - \log_2{FC}_{g3n0-g1n0} = \hat\beta_{g3n1}=0$, note that the latter hypothesis is also equivalent to $H_0: \log_2{FC}_{g3n1-g3n0} - \log_2{FC}_{g1n1-g1n0} = \hat\beta_{g3n1}=0$ $\rightarrow$ "grade3:node1 = 0"

```r
library(multcomp)
fitGlht<- glht(fit, linfct = c("grade3 = 0","grade3+grade3:node1 = 0","node1 = 0","node1+grade3:node1 = 0","grade3:node1 = 0"))
summary(fitGlht)
confint(fitGlht)
2^confint(fitGlht)$confint
2^-confint(fitGlht)$confint["grade3:node1",]
```

---

[← Interpretation of model parameters and statistical tests](04-interpretation-of-model-parameters-and-statistical-tests.md) · [Up: contents](index.md) · [Conclusion →](06-conclusion.md)
