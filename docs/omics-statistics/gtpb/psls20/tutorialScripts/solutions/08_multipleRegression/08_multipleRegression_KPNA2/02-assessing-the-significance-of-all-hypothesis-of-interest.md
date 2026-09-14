---
title: Assessing the significance of all hypothesis of interest
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/08_multipleRegression/08_multipleRegression_KPNA2.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/solutions/08_multipleRegression/08_multipleRegression_KPNA2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Assessing the significance of all hypothesis of interest

**Source:** [`tutorialScripts/solutions/08_multipleRegression/08_multipleRegression_KPNA2.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/solutions/08_multipleRegression/08_multipleRegression_KPNA2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

We can assess all contrasts of interest using the multcomp package. This will also allow us to correct for multiple testing, since we assess multiple hypotheses to answer the relevant research question.


- $H_0: \log_2{FC}_{g3n0-g1n0}= \beta_{g3}=0$ $\rightarrow$ "grade3 = 0"
- $H_0: \log_2{FC}_{g3n1-g1n1}= \beta_{g3} + \hat\beta_{g3n1}=0$ $\rightarrow$ "grade3+grade3:node1 = 0"
- $H_0: \log_2{FC}_{g1n1-g1n0}= \beta_{n1}$  $\rightarrow$ "node1 = 0"
- $H_0: \log_2{FC}_{g3n1-g1n1}= \beta_{n1} + \hat\beta_{g3n1}=0$ $\rightarrow$ "node1+grade3:node1 = 0"
- $H_0: \log_2{FC}_{g3n1-g1n1} - \log_2{FC}_{g3n0-g1n0} = \hat\beta_{g3n1}=0$, note that the latter hypothesis is also equivalent to $H_0: \log_2{FC}_{g3n1-g3n0} - \log_2{FC}_{g1n1-g1n0} = \hat\beta_{g3n1}=0$ $\rightarrow$ "grade3:node1 = 0"

```r
library(multcomp)
fitGlht<- glht(fit, linfct = c("grade3 = 0","grade3+grade3:node1 = 0","node1 = 0","node1+grade3:node1 = 0","grade3:node1 = 0"))
summary(fitGlht)
confint(fitGlht)
2^confint(fitGlht)$confint
2^-confint(fitGlht)$confint["grade3:node1",]
```

#Conclusion

- There is an extremely significant association between the KPNA2 expression and hystological grade in patients with unaffected as well as in patients with affected lymph nodes (both p<<0.001).
  When lymph nodes are unaffected, the expression is on average `r round(2^confint(fitGlht)$confint["grade3",1],2)` times higher for patients with histological grade 3 than patients with histological grade 1 (95% CI [`r round(2^confint(fitGlht)$confint["grade3",2:3],2)`]).
  For patients with affected lymph nodes the expression is on average `r round(2^confint(fitGlht)$confint["grade3 + grade3:node1",1],2)` times higher for patients with histological grade 3 tumors than patients with histological grade 1 tumors (95% CI [`r round(2^confint(fitGlht)$confint["grade3 + grade3:node1",2:3],2)`]).

- The association between the KPNA2 expression with the lymph node status in grade 1 patients is very significant ($p=$ `r format(summary(fitGlht)$test$pvalues[3],digits=2)`).
The KPNA2 expression in histological grade 1 patients with affected lymph nodes is on average `r round(2^confint(fitGlht)$confint["node1",1],2)` times higher than for grade 1 patients with unaffected lymph nodes (95% CI [`r round(2^confint(fitGlht)$confint["node1",2:3],2)`]).
In grade 3 patients, however, this association is not significant ($p=$ `r format(summary(fitGlht)$test$pvalues[4],digits=2)`, 95% CI [`r round(2^confint(fitGlht)$confint["node1 + grade3:node1",2:3],2)`] ).

- There is also a significant interaction between the hystological grade and the lymph node status. So the association between the KPNA2 expression and the histological grade depends on the lymph node status and vice versa ($p=$ `r format(summary(fitGlht)$test$pvalues[5],digits=2)`). The fold change corresponding to histological grade is on average `r round(1/2^confint(fitGlht)$confint["grade3:node1",1],2)` times lower in patients with affected lymph nodes as compared to patients with unaffected lymph node (95% CI [`r round(1/2^confint(fitGlht)$confint["grade3:node1",3:2],2)`]). (Similarly, the fold change corresponding to the node status is on average `r round(1/2^confint(fitGlht)$confint["grade3:node1",1],2)` times lower in patients with grade 3 tumors as compared to patients with grade 1 tumors, 95% CI [`r round(1/2^confint(fitGlht)$confint["grade3:node1",3:2],2)`])


---

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) {-} →](03-home-https-gtpb-github-io-psls20.md)
