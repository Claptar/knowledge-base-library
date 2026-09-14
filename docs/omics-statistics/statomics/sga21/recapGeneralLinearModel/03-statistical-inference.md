---
title: Statistical Inference
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd
source_file: sources/statomics-sga21/recapGeneralLinearModel.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Statistical Inference

**Source:** [`recapGeneralLinearModel.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/recapGeneralLinearModel.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

- Researchers want to assess the association of histological grade on KPNA2 gene expression
- Inference?

---

![](https://raw.githubusercontent.com/statOmics/SGA21/master/figures/statGenomicsGent201718-7.jpeg)


---


- Researchers want to assess the association of histological grade on KPNA2 gene expression
- Inference?
- testing + CI $ \rightarrow $ Assumptions

---

- In general we start from **alternative hypothese** $H_A$: we want to show an association
- Gene expression of grade 1 and grade 3 patients is on average different

- But, we will assess it by falsifying the opposite:

- The average KPNA2 gene expression of  grade 1 and grade 3 patients is equal

---

- How likely is it to observe an equal or more extreme association than the one observed in the sample when the null hypothesis is true?

- When we make assumptions about the distribution of our test statistic we can quantify this probability: **p-value**.
- If the p-value is below a significance threshold $\alpha$ we reject the null hypothesis

*We control the probability on a false positive result at the $\alpha$-level (type I error)*

- The p-value will only be calculated correctly if the underlying assumptions hold!

```r
library(gridExtra)
p1
p2
```

```r
t.test(gene~grade,data=gene)

effectSize <- effectSize %>%
  mutate(t.stat=delta/seDelta) %>%
  mutate(p.value= pt(-abs(t.stat),21.352)*2)

effectSize
```

- Intensities are often not normally distributed and have a mean variance relation
- Commonly log2-transformed
- Differences on log scale:

$$
\log_2(B) - \log_2(A) = \log_2 \frac{B}{A} = \log_2 FC_{\frac{B}{A}}
$$


![](https://raw.githubusercontent.com/statOmics/SGA21/master/figures/statGenomicsGent201718-8.jpeg)

---

## Log transformation

```r
gene <- gene %>%
  mutate(lgene = log2(gene))

p1 <- gene %>%
  ggplot(aes(x=grade,y=lgene)) +
  geom_boxplot(outlier.shape=NA) +
  geom_jitter()

p2 <- gene %>%
  ggplot(aes(sample=lgene)) +
  geom_qq() +
  geom_qq_line() +
  facet_wrap(~grade)

p1
p2

logtest <- t.test(lgene~grade,data=gene,var.equal=TRUE)
logtest

log2FC <- logtest$estimate[2]-logtest$estimate[1]
log2FC
names(log2FC) <- "g3-g1"
2^log2FC
```

## Conclusion

There is a extremely significant association of the histological grade on the gene expression in tumor tissue.  On average, the gene expression for the grade 3 patients is `r round(2^log2FC,2)` times higher than the gene expression in grade 1 patients (95\% CI  [`r paste(round(2^-logtest$conf.int[2:1],2),collapse=", ")`], $p<<0.001$).


![](https://raw.githubusercontent.com/statOmics/SGA21/master/figures/statGenomicsGent201718-10.jpeg)

---


![](https://raw.githubusercontent.com/statOmics/SGA21/master/figures/statGenomicsGent201718-11.jpeg)

---

The patients also differ in the their lymph node status. Hence, we have a two factorial design: grade x lymph node status!!!

Solution??

![](https://raw.githubusercontent.com/statOmics/SGA21/master/figures/statGenomicsGent201718-12.jpeg)

---

---

[← Data Exploration](02-data-exploration.md) · [Up: contents](index.md) · [General Linear Model →](04-general-linear-model.md)
