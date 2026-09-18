---
title: Alternative parameterizations
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Alternative parameterizations

While our design matrix here was parameterized as `~ treatment*time + patient` alternative, equivalent parameterizations are also possible.
Below, we demonstrate another parameterization that could work, too, and can be more intuitive. In this parameterization, we estimate a mean for each experimental condition, without an intercept, which can be convenient to think about how to set up contrasts.

```r
treatTime <- as.factor(paste0(treatment, time))
table(treatTime)

design2 <- model.matrix(~ 0 + treatTime + patient)

dge2 <- calcNormFactors(se)
dge2 <- estimateDisp(dge2, design2)
plotBCV(dge2)
fit2 <- glmFit(dge2, design2)
head(fit2$coefficients)

## for example: the estimate for the DPN24h vs control 24h is still the same,
## but requires a different combination of parameters
plot(fit$coefficients[,"treatmentDPN"],
     fit2$coefficients[,"treatTimeDPN24h"] - fit2$coefficients[,"treatTimeControl24h"],
     xlab="Intercept model estimate", ylab="No intercept model estimate")

# Let's implement the DPNvsCON48 contrast
L2 <- matrix(0, nrow = ncol(fit2$coefficients), ncol = 1)
rownames(L2) <- colnames(fit2$coefficients)
L2[c("treatTimeDPN48h", "treatTimeControl48h"),1] <- c(1, -1)
lrt2 <- glmLRT(fit2, contrast=L2[,1])
hist(lrt2$table$PValue)


plot(x=lrt2$table$PValue, y=lrtList[[2]]$table$PValue,
     xlab="No intercept model p-value",
     ylab="Intercept model p-value")
```

## Additional Challenge (Opportunity?): The importance of reproducible analysis

Finally, it is crucial to make your analysis reproducible using tools such as RMarkdown and GitHub. Please sit back and watch this [amazing lecture from Professor Keith Baggerly on "The Importance of Reproducible Research in High-Throughput Biology](https://www.youtube.com/watch?v=8QJfNS7XXwA).

---

[← Challenge IV: Statistical inference across many genes](06-challenge-iv-statistical-inference-across-many-genes.md) · [Up: contents](index.md)
