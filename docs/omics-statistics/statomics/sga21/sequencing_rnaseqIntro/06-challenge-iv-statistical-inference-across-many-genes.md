---
title: 'Challenge IV: Statistical inference across many genes'
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Challenge IV: Statistical inference across many genes

## Contrasts on the treatment effects

We will first derive all contrasts that are also investigated in the original manuscript, using our extended model where we are allowing for an interaction effect between treatment and time.

The mean model is
$$ \log(\mu_{gi}) = \beta_{g0} + \beta_{g1} x_{DPN} + \beta_{g2} x_{OHT} + \beta_{g3} x_{48h} + \beta_{g4} x_{pat2} + \beta_{g5} x_{pat3} + \beta_{g6} x_{pat4} + \\ \beta_{g7} x_{DPN:48h} + \beta_{g8} x_{OHT:48h}. $$

The intercept corresponds to the log average gene expression in the control group at 24h for patient 1.

**DPN 24h vs control 24h.**
The respective means are
$$\log \mu_{g,DPN,24h} = \beta_{g0} + \beta_{g1},$$
$$\log \mu_{g,con,24h} = \beta_{g0}.$$
And their difference is
$$ \delta_g = \beta_{g1}. $$

**DPN 48h vs control 48h.**
The respective means are
$$\log \mu_{g,DPN,48h} = \beta_{g0} + \beta_{g1} + \beta_{g3} + \beta_{g7},$$
$$\log \mu_{g,con,48h} = \beta_{g0} + \beta_{g3}.$$
And their difference is
$$ \delta_g = \beta_{g1} + \beta_{g7}. $$

**OHT 24h vs control 24h.**
The respective means are
$$\log \mu_{g,OHT,24h} = \beta_{g0} + \beta_{g2} ,$$
$$\log \mu_{g,con,24h} = \beta_{g0}.$$
And their difference is
$$ \delta_g = \beta_{g2}. $$

**OHT 48h vs control 48h.**
The respective means are
$$\log \mu_{g,OHT,48h} = \beta_{g0} + \beta_{g2} + \beta_{g3} + \beta_{g8},$$
$$\log \mu_{g,con,48h} = \beta_{g0} + \beta_{g3}.$$
And their difference is
$$ \delta_g = \beta_{g2} + \beta_{g8}. $$

However, we can also assess the interaction effects: is the time effect different between DPN and OHT treatment versus the control? And how about the DPN vs OHT treatments?

**DPN vs control interaction.**
The time effect for each condition is
$$ \delta_{DPN} = \log \mu_{g,DPN,48h} - \log \mu_{g,DPN,24h} = \beta_{g3} + \beta_{g7},$$
$$ \delta_{con} = \log \mu_{g,con,48h} - \log \mu_{g,con,24h} = \beta_{g3}. $$
So the interaction effect is
$$\delta_{DPN-con} = \beta_{g7}.$$

**OHT vs control interaction.**
The time effect for each condition is
$$ \delta_{OHT} = \log \mu_{g,OHT,48h} - \log \mu_{g,OHT,24h} = \beta_{g3} + \beta_{g8},$$
$$ \delta_{con} = \log \mu_{g,con,48h} - \log \mu_{g,con,24h} = \beta_{g3}. $$
So the interaction effect is
$$\delta_{DPN-con} = \beta_{g8}.$$

**OHT vs DPN interaction.**
The time effect for each condition is
$$ \delta_{OHT} = \log \mu_{g,OHT,48h} - \log \mu_{g,OHT,24h} = \beta_{g3} + \beta_{g8},$$
$$ \delta_{DPN} = \log \mu_{g,DPN,48h} - \log \mu_{g,DPN,24h} = \beta_{g3} + \beta_{g7},$$
So the interaction effect is
$$\delta_{OHT-DPN} = \beta_{g8} - \beta_{g7}.$$

Let's implement all of these in a contrast matrix.

```r
L <- matrix(0, nrow = ncol(fit$coefficients), ncol = 7)
rownames(L) <- colnames(fit$coefficients)
colnames(L) <- c("DPNvsCON24", "DPNvsCON48",
                 "OHTvsCON24", "OHTvsCON48",
                 "DPNvsCONInt", "OHTvsCONInt",
                 "OHTvsDPNInt")
# DPN vs control at 24h
L[2,"DPNvsCON24"] <- 1
# DPN vs control at 48h
L[c(2,8),"DPNvsCON48"] <- 1
# OHT vs control at 24h
L[3,"OHTvsCON24"] <- 1
# OHT vs control at 48h
L[c(3,9),"OHTvsCON48"] <- 1
# DPN control interaction
L[8,"DPNvsCONInt"] <- 1
# OHT control interaction
L[9,"OHTvsCONInt"] <- 1
# OHT DPN interaction
L[c(9,8),"OHTvsDPNInt"] <- c(1, -1)

L
```

And, finally, we can assess each hypothesis using the `glmLRT` function implemented in `edgeR`. We can assess each hypothesis separately by looping over the contrasts.

```r
lrtList <- list() #list of results
for(cc in 1:ncol(L)) lrtList[[cc]] <- glmLRT(fit, contrast = L[,cc])

# p-value histograms
pvalList <- lapply(lrtList, function(x) x$table$PValue)
pvalMat <- do.call(cbind,  pvalList)
colnames(pvalMat) <- colnames(L)
par(mfrow=c(3,3))
sapply(1:ncol(pvalMat), function(ii) hist(pvalMat[,ii],
                                          main = colnames(pvalMat)[ii],
                                          xlab = "p-value"))
```

### Multiple testing

```r
# number of DE genes
padjMat <- apply(pvalMat, 2, p.adjust, method="fdr")
colSums(padjMat <= 0.05 )
```

We are finding low numbers of DE genes between treatments at a 5\% FDR level. This was already reflected in the the MDS plots.

### Visualization

Let's visualize some results for the DPN vs control at 48h contrast.

```r
library(scales) # for scales::alpha()
deGenes <- p.adjust(lrtList[[2]]$table$PValue, "fdr") <= 0.05

## volcano plot
plot(x = lrtList[[2]]$table$logFC,
     y = -log10(lrtList[[2]]$table$PValue),
     xlab = "log Fold-change",
     ylab = "-log10 P-value",
     pch = 16, col = alpha(deGenes+1, .4),
     cex=2/3, bty='l')
legend("topright", c("DE", "not DE"),
       col = 2:1, pch=16, bty='n')

## MD-plot
plot(x = lrtList[[2]]$table$logCPM,
     y = lrtList[[2]]$table$logFC,
     xlab = "Average log CPM",
     ylab = "Log fold-change",
     pch = 16, col = alpha(deGenes+1, .4),
     cex=2/3, bty='l')
legend("topright", c("DE", "not DE"),
       col = 2:1, pch=16, bty='n')
abline(h=0, col="orange", lwd=2, lty=2)

```

 ---

```r
# extract all DE genes
deGenes <- rownames(lrtList[[2]]$table)[p.adjust(lrtList[[2]]$table$PValue, "fdr") <= 0.05]
deGenes
# order according to absolute fold-change
orderedDEGenes <- deGenes[order(abs(lrtList[[2]]$table[deGenes, "logFC"]), decreasing = TRUE)]

par(mfrow=c(3,3))
for(kk in 1:9){
  boxplot(log1p(assays(se)$counts[orderedDEGenes[kk],]) ~ interaction(treatment, time))
  boxplot(fit$fitted.values[orderedDEGenes[kk],] ~ interaction(treatment, time))
}
```

## Contrast on the time effect

Based on the MDS plot, we can expect comparatively more DE genes for the time effect. For didactic purposes, here we assess an **average time effect across the three treatments**. The analysis shows how flexible one can be when using contrasts.

Mean of time 24h:
$$\log \mu_{g,24h} = \frac{1}{3} \left\{ \underbrace{(\beta_{g0})}_\text{Control, 24h} + \underbrace{(\beta_{g0} + \beta_{g1})}_\text{DPN, 24h} + \underbrace{(\beta_{g0} + \beta_{g2})}_\text{OHT, 24h} \right\}$$

Mean of time 48h:
$$\log \mu_{g,48h} = \frac{1}{3} \left\{ \underbrace{(\beta_{g0} + \beta_{g3})}_\text{Control, 48h} + \underbrace{(\beta_{g0} + \beta_{g1} + \beta_{g3} + \beta_{g7})}_\text{DPN, 48h} + \underbrace{(\beta_{g0} + \beta_{g2}+ \beta_{g3} + \beta_{g8})}_\text{OHT, 48h} \right\}$$

Difference:
$$ \log \left( \frac{\mu_{g,48h}}{\mu_{g,24h}} \right) = \beta_{g3} + \frac{1}{3}(\beta_{g7} + \beta_{g8}) $$

```r
Ltime <- matrix(0, nrow = ncol(fit$coefficients), ncol = 1)
rownames(Ltime) <- colnames(fit$coefficients)
Ltime[c("time48h", "treatmentDPN:time48h", "treatmentOHT:time48h"),1] <- c(1, 1/3, 1/3)

lrtTime <- glmLRT(fit, contrast=Ltime)
hist(lrtTime$table$PValue) # very different p-value distribution

sum(p.adjust(lrtTime$table$PValue, "fdr") <= 0.05) # many DE genes
```

---

[← Challenge III: Parameter estimation (under limited information setting)](05-challenge-iii-parameter-estimation-under-limited-information.md) · [Up: contents](index.md) · [Alternative parameterizations →](07-alternative-parameterizations.md)
