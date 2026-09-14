---
title: Let's implement the DPNvsCON48 contrast
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Let's implement the DPNvsCON48 contrast

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

L2 <- matrix(0, nrow = ncol(fit2$coefficients), ncol = 1)
rownames(L2) <- colnames(fit2$coefficients)
L2[c("treatTimeDPN48h", "treatTimeControl48h"),1] <- c(1, -1)
lrt2 <- glmLRT(fit2, contrast=L2[,1])
hist(lrt2$table$PValue)


plot(x=lrt2$table$PValue, y=lrtList[[2]]$table$PValue,
     xlab="No intercept model p-value",
     ylab="Intercept model p-value")
```

---

[← Alternative parameterizations](35-alternative-parameterizations.md) · [Up: contents](index.md) · [Additional Challenge (Opportunity?): The importance of reproducible analysis →](37-additional-challenge-opportunity-the-importance-of-reproduci.md)
