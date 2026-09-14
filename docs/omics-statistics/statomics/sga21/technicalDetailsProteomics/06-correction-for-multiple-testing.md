---
title: Correction for multiple testing
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd
source_file: sources/statomics-sga21/technicalDetailsProteomics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Correction for multiple testing

**Source:** [`technicalDetailsProteomics.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/technicalDetailsProteomics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

- We can adjust the p-values for multiple testing.

## Family wise error rate correction:

- A list of returned proteins is considered to be in error as soon as it contains at most one false positive protein.

- $\text{FWER} = P(FP \leq 1)$

- FWER: probability of making at least one false positive decision or
probability to declare at least one protein differentially abundant which is truly non differentially abundant

### Bonferroni method

- Simple method
- $m$ tests are performed at the level $\alpha/m$
- FWER$\leq\sum\limits_{p=1}^{m}P(reject H_{0p}\vert H_{0p}\text{ is true})=m \alpha/m=\alpha$
- Provides strong control
- Bonferroni is very conservative
- Works for dependent tests
- Adjusted p-value: $\tilde{p}_p=\min(m\ p_p,1)$

---

#### Bonferroni in practise

Via R functions

```r
padj <- p.adjust(
  rowData(pe[["proteinRobust"]])$tissueV$pval,
  method = "bonferroni")
```

Own Implementation: adjust and make sure that p-value is smaller than 1.

```r
m <- sum(!is.na(rowData(pe[["proteinRobust"]])$tissueV$pval))
padjSelf <-  rowData(pe[["proteinRobust"]])$tissueV$pval * m
padjSelf[padjSelf > 1] <- 1

range(padj - padjSelf, na.rm = TRUE)
```
#### Illustration in simulation under $H_0$ and heart case study

```r
volcano <- ggplot(rowData(sims[["sim0"]])$tissueV,
                 aes(x = logFC, y = -log10(pval), color = p.adjust(pval,"bonferroni") < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
 theme_minimal() +
 ggtitle("simulated heart data under H0")
volcano
```

- No false positives are returned for simulation under H_0. List is correct according to FWER.

```r
volcano <- ggplot(rowData(pe[["proteinRobust"]])$tissueV,
                 aes(x = logFC, y = -log10(pval), color = p.adjust(pval,"bonferroni") < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
 theme_minimal() +
 ggtitle("real heart data")
volcano
```

- Very few proteins are returned for real data. Very conservative!

### FWER: step down method of Holm

- Compare smallest p-value with $\alpha/m$
- If you can reject the smallest p-value at $\alpha/m$ level
  - asses second smallest p-value at the $\alpha/(m-1)$
- If you can reject the second smallest p-value at $\alpha/(m-1)$ level
    - asses third smallest p-value at the $\alpha/(m-2)$
- ...
- If you can reject the k-1 smallest p-value at $\alpha/(m-k+2)$ level
  - asses k smallest p-value at the $\alpha/(m-k+1)$ level
- continu as long as you can reject.

The Holm is a step down method (from more to less significant) that corrects in each step for the number of null hypothesis that you still can falsely reject.

---

Adjusted p-values:

- Order p-values with $(k)$ the $k^{th}$ smallest p-value
- $\tilde{p}_{(k)}=\min(p_{(k)}(m-k+1),1)$

Suppose 2 tests: $p_{(1)}=0.001$, $p_{(2)}=0.0015$
$\rightarrow$ $\tilde{p}_{(1)}=0.002$, $\tilde{p}_{(2)}=0.0015$

- Problem: Monotonicity is not the same as for original p-values!
- Enforce monotonicity:
$\tilde{p}_{(k)}=\max\limits_{h=1,\ldots,k}\min(p_{(h)}(m-h+1),1)$

---

#### Holm example

With R functions:

```r
padj <- p.adjust(
  rowData(pe[["proteinRobust"]])$tissueV$pval,
  method = "holm")
```

Own implementation

1. Order p-values
```r
padjSelf <-  rowData(pe[["proteinRobust"]])$tissueV$pval
ord <- order(padjSelf)
pOrd <- padjSelf[ord]
m <- sum(!is.na(padjSelf))
```

2. Adjust ordered p-values and ensure that value is not larger than 1
```r
pOrd[1:m] <- pOrd[1:m]*(m - (1:m) + 1)
pOrd[pOrd>1] <- 1
```

3. Monotonicity
```r
pmax <- pOrd[1]
for (i in 2:m)
{
  if (pOrd[i] > pmax)
    pmax <- pOrd[i] else
    pOrd[i] <- pmax
}
```

4. Put adjusted p-values in original order
```r
padjSelf[ord] <- pOrd
range(padj - padjSelf, na.rm = TRUE)
```

#### Illustration in simulation under $H_0$ and heart case study

```r
volcano <- ggplot(rowData(sims[["sim0"]])$tissueV,
                 aes(x = logFC, y = -log10(pval), color = p.adjust(pval,"holm") < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
 theme_minimal() +
 ggtitle("simulated heart data under H0")
volcano
```

- No false positives are returned for simulation under H_0. List is correct according to FWER.

```r
volcano <- ggplot(rowData(pe[["proteinRobust"]])$tissueV,
                 aes(x = logFC, y = -log10(pval), color = p.adjust(pval,"holm") < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
 theme_minimal() +
 ggtitle("real heart data")
volcano
```

- Very few proteins are returned for real data. Still very conservative!


## False discovery rate

- Adjusted P-values with the Benjamini Hochberg correction correspond to the estimated FDR of the set that is returned when the significance level is set at this threshold.
\begin{eqnarray}
FDR(p_0) &=& \text{E}\left[\frac{FP}{(FP + TP)}\right]\\
&\approx&\frac{p_0 \times m}{\#p_p \leq p_0}\\
\end{eqnarray}

So adjusted p-value for protein j equals
$$\tilde p_j = \frac{p_{0,j} \times m}{\#p_p \leq p_{0,j}}$$

However, the FDR always has to be between 0 and 1 so:

$$\tilde p_j = \min\left[\frac{p_{0,j} \times m}{\#p_p \leq p_{0,j}},1\right]$$

and the adjusted p-values should remain in the same order as the original p-values.

$$\tilde p_j =  \min\limits_{\forall k: p_k > p_j} \min\left[\frac{p_{0,k} \times m}{\#p_p \leq p_{0,k}},1\right]$$

1. Order pvalues
```r
pvals <- rowData(pe[["proteinRobust"]])$tissueV$pval
naInd <- is.na(pvals)
pHlp <- pvals[!naInd]
ord <- pHlp %>% order
pHlp <- pHlp[ord]
```

2. Adjust ordered p-values
```r
pHlp <- pHlp*length(pHlp)/(1:length(pHlp))
```

3. Ensure adjust p-values are smaller are equal than 1
```r
pHlp[pHlp>1] <- 1
```

4. Monotonicity constraint
```r
pmin <- pHlp[length(pHlp)]
for (j in (length(pHlp)-1):1)
{
  if (pHlp[j] < pmin)
    pmin <- pHlp[j] else
    pHlp[j] <- pmin
}
```

5. Put p-values back in original order

```r
pHlp[ord] <- pHlp
pAdj <- pvals
pAdj[!naInd] <- pHlp

head(pAdj)
head(rowData(pe[["proteinRobust"]])$tissueV)
range(rowData(pe[["proteinRobust"]])$tissueV$adjPval - pAdj,na.rm=TRUE)
```

#### Illustration in simulation under $H_0$ and heart case study

```r
volcano <- ggplot(rowData(sims[["sim0"]])$tissueV,
                 aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
 theme_minimal() +
 ggtitle("simulated heart data under H0")
volcano
```

- No false positives are returned for simulation under H_0. List is correct according to FWER.
- It can be shown that the FDR-method controls the FWER when $H_0$ is true for all features.


```r
volcano <- ggplot(rowData(pe[["proteinRobust"]])$tissueV,
                 aes(x = logFC, y = -log10(pval), color = adjPval < 0.05)) +
 geom_point(cex = 2.5) +
 scale_color_manual(values = alpha(c("black", "red"), 0.5)) +
 theme_minimal() +
 ggtitle("real heart data")
volcano
```

The FDR method allows us to return much longer DA protein lists at the expense of a few false positives.
The FDR controls the fraction of false positives in the list that you return on average on the significance level that is adopted.
So if you use $\alpha=0.05$ we expect on average 5% of false positives in the list that we return.

---

[← P-values](05-p-values.md) · [Up: contents](index.md)
