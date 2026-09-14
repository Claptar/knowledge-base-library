---
title: Kruskal-Wallis Rank Test
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-KruskalWallis.Rmd
source_file: sources/gtpb-psls20/theory/09-NonparametericStatistics-KruskalWallis.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Kruskal-Wallis Rank Test

**Source:** [`theory/09-NonparametericStatistics-KruskalWallis.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/09-NonparametericStatistics-KruskalWallis.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- The Kruskal-Wallis Rank Test (KW-test) is a  non-parameteric alternative  for ANOVA F-test.

-  Classical $F$-teststatistic can be written as
  $$
    F = \frac{\text{SST}/(g-1)}{\text{SSE}/(n-g)} = \frac{\text{SST}/(g-1)}{(\text{SSTot}-\text{SST})/(n-g)} ,
  $$
-  with $g$ the number of groups.

- SSTot depends only on  outcomes $\mathbf{y}$ and will not vary in permutation test.

- SST can be used as statistic
 $$\text{SST}=\sum_{j=1}^t n_j(\bar{Y}_j-\bar{Y})^2$$


-  The KW test statistic is based on SST on rank-transformed outcomes^[we assume that no *ties* are available],
  $$
     \text{SST} = \sum_{j=1}^g n_j \left(\bar{R}_j - \bar{R}\right)^2 = \sum_{j=1}^t n_j \left(\bar{R}_j - \frac{n+1}{2}\right)^2 ,
  $$
-  with $\bar{R}_j$ the mean of the ranks in group $j$, and $\bar{R}$ the mean of all ranks,
  $$
    \bar{R} = \frac{1}{n}(1+2+\cdots + n) = \frac{1}{n}\frac{1}{2}n(n+1) = \frac{n+1}{2}.
  $$
-  The KW teststatistic is given by
  $$
    KW = \frac{12}{n(n+1)}  \sum_{j=1}^g n_j \left(\bar{R}_j - \frac{n+1}{2}\right)^2.
  $$
-  The factor $\frac{12}{n(n+1)}$ is used so that $KW$ has a simple asymptotic null distribution. In particular under $H_0$, given thart $\min(n_1,\ldots, n_g)\rightarrow \infty$,
  $$
    KW  \rightarrow \chi^2_{t-1}.
  $$

-  The exact KW-test can be executed by calculating the permutation null distribution (that only depends on $n_1, \ldots, n_g$) to test
  $$H_0: f_1=\ldots=f_g \text{ vs } H_1: \text{ at least two means are different}.$$

- In order to allow $H_1$ to be formulated in terms of means, the assumption of locations shift should be valid.
- For DMH example this is not the case.
- If location-shift is invalid, we have to formulate $H_1$ in terms of probabilistic indices:
  $$H_0: f_1=\ldots=f_g \text{ vs } H_1: \exists\ j,k \in \{1,\ldots,g\} : \text{P}\left[Y_j\geq Y_k\right]\neq 0.5$$


## DNA Damage Example

```r
kruskal.test(length~dose,data=dna)
```

- On the $5\%$ level of significance we can reject the null hypothesis.

- R-functie `kruskal.test` only returns the asymptotic approximation for $p$-values.

- With only 6 observaties per groep, this is not a good approximation of the $p$-value

-  With the `coin` R package we can calculate the exacte $p$-value

```r
library(coin)
kwPerm <- kruskal_test(length~dose,data=dna,
		    distribution=approximate(B=100000))
kwPerm
```

- We conclude that the difference in the distribution of the DNA damages due to the DMH dose is extremely significantly different.

- Posthoc analysis with WMW tests.

```r
pairwise.wilcox.test(dna$length,dna$dose)
```

- All DMH behandelingen are significantly different from the control.
- The DMH are not significantly different from one another.
- U1 does not occur in the `pairwise.wilcox.test` output. Point estimate on probability on higher DNA-damage?

```r
pairWilcox <- pairwise.wilcox.test(dna$length,dna$dose)
```

```r
nGroup <- table(dna$dose)
probInd <- combn(levels(dna$dose),2,function(x)
		 {
		 test <- wilcox.test(length~dose,subset(dna,dose%in%x))
		 return(test$statistic/prod(nGroup[x]))
		 }
		 )
names(probInd) <- combn(levels(dna$dose),2,paste,collapse="vs")
probInd
```

Because there are doubts on the location-shift model we draw our conclusions in terms of the probabilistic index.

### Conclusion

- There is an extremely significant difference in in the distribution of the DNA-damage measurements due to the treatment with DMH  ($p<0.001$ KW-test).
- DNA-damage is more likely upon DMH treatment than in the control treatment (all p=0.013, WMW-testen).
- The probability on higher DNA-damage upon exposure to DMH is 100% (Calculation of a CI on the probabilistic index is beyond the scope of the course)
- There are no significant differences in the distributions of the comit-lengths among the treatment with the different DMH concentrations ($p=$ `r paste(format(range(pairWilcox$p.value[,-1],na.rm=TRUE),digit=2),collapse="-")`).
- DMH shows already genotoxic effects at low dose.
- (Alle paarswise tests are gecorrected for multiple testing using Holm's methode).


---

---

[← DMH Voorbeeld](02-dmh-voorbeeld.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) →](04-home-https-gtpb-github-io-psls20.md)
