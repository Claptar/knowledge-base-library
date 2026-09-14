---
title: Conclusion
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd
source_file: sources/statomics-sga21/multipleRegression_KPNA2.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Conclusion

**Source:** [`multipleRegression_KPNA2.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/multipleRegression_KPNA2.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

- There is an extremely significant association between the KPNA2 expression and hystological grade in patients with unaffected as well as in patients with affected lymph nodes (both p<<0.001).
  When lymph nodes are unaffected, the expression is on average `r round(2^confint(fitGlht)$confint["grade3",1],2)` times higher for patients with histological grade 3 than patients with histological grade 1 (95% CI [`r round(2^confint(fitGlht)$confint["grade3",2:3],2)`]).
  For patients with affected lymph nodes the expression is on average `r round(2^confint(fitGlht)$confint["grade3 + grade3:node1",1],2)` times higher for patients with histological grade 3 tumors than patients with histological grade 1 tumors (95% CI [`r round(2^confint(fitGlht)$confint["grade3 + grade3:node1",2:3],2)`]).

- The association between the KPNA2 expression with the lymph node status in grade 1 patients is very significant ($p=$ `r format(summary(fitGlht)$test$pvalues[3],digits=2)`).
The KPNA2 expression in histological grade 1 patients with affected lymph nodes is on average `r round(2^confint(fitGlht)$confint["node1",1],2)` times higher than for grade 1 patients with unaffected lymph nodes (95% CI [`r round(2^confint(fitGlht)$confint["node1",2:3],2)`]).
In grade 3 patients, however, this association is not significant ($p=$ `r format(summary(fitGlht)$test$pvalues[4],digits=2)`, 95% CI [`r round(2^confint(fitGlht)$confint["node1 + grade3:node1",2:3],2)`] ).

- There is also a significant interaction between the hystological grade and the lymph node status. So the association between the KPNA2 expression and the histological grade depends on the lymph node status and vice versa ($p=$ `r format(summary(fitGlht)$test$pvalues[5],digits=2)`). The fold change corresponding to histological grade is on average `r round(1/2^confint(fitGlht)$confint["grade3:node1",1],2)` times lower in patients with affected lymph nodes as compared to patients with unaffected lymph node (95% CI [`r round(1/2^confint(fitGlht)$confint["grade3:node1",3:2],2)`]). (Similarly, the fold change corresponding to the node status is on average `r round(1/2^confint(fitGlht)$confint["grade3:node1",1],2)` times lower in patients with grade 3 tumors as compared to patients with grade 1 tumors, 95% CI [`r round(1/2^confint(fitGlht)$confint["grade3:node1",3:2],2)`])

---

[← Assessing the significance of all hypothesis of interest](05-assessing-the-significance-of-all-hypothesis-of-interest.md) · [Up: contents](index.md)
