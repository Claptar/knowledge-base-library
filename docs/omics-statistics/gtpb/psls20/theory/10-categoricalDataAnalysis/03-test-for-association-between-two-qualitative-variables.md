---
title: Test for association between two qualitative variables
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd
source_file: sources/gtpb-psls20/theory/10-categoricalDataAnalysis.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Test for association between two qualitative variables

**Source:** [`theory/10-categoricalDataAnalysis.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

## Paired observations

- 2 measurements on same individual
- e.g. before and after exposure to a chemical substance
- observe a categorical outcome before and after.
- *gepaarde binary responses*
- Statistical analysis has to account for paired design.

---

### Example:  Females choose gentle, but not healthy or macho males in Campbell dwarf hamsters (Rogovin et al. 2017)

```r
library(plotrix)
par(mar=c(0,0,0,0),mai=c(0,0,0,0))
plot(0,0,axes=FALSE,xlab="",ylab="",col=0,xlim=c(0,3),ylim=c(0,3))
rect(0,0,3,3)
lines(c(1,1),c(0,3))
lines(c(2,2),c(0,3))
lines(c(1,1),c(1,2),lwd=2)
lines(c(1,1),c(1,2),lwd=4)
lines(c(2,2),c(1,2),lwd=4)
rect(1.45,1,1.55,1.3)
draw.circle(1.5,1.36,0.05)
lines(c(1.5,1.5),c(1,.85))
text(1.5,1.15,"\\VE",vfont=c("sans serif","bold"),cex=1.3)
rect(0.5,1.05,0.8,1.15)
draw.circle(0.86,1.1,0.05)
lines(c(0.5,0.35),c(1.1,1.1))
lines(c(0.8,0),c(1.1,1.5),lty=2)
text(0.65,1.1,"\\MA",vfont=c("sans serif","bold"),cex=1.3)
rect(2.5,1.95,2.2,1.85)
draw.circle(2.14,1.9,0.05)
lines(c(2.5,2.65),c(1.9,1.9))
lines(c(2.2,3),c(1.9,1.5),lty=2)
text(2.35,1.9,"\\MA",vfont=c("sans serif","bold"),cex=1.3)
```

---

- The gate is opened upon 3 minutes
- aggressive vs non-agressive male
- Each female undergoes the test twice:

    - once upon stay in hostile environment (high population density, shortage of feed, a lot of competition)
    - and once upon stay in gentle evironment.


```r
hamster <- matrix(c(3,17,1,13),ncol=2,byrow=TRUE)
rownames(hamster) <- c("hostile_agressive", "hostile_non-agressive")
colnames(hamster) <- c("friendly_agressive","friendly_non-agressive")
hamsterTot=matrix(0,nrow=3,ncol=3)
hamsterTot[1:2,1:2]=hamster
hamsterTot[3,1:2]=colSums(hamster)
hamsterTot[,3]=rowSums(hamsterTot[,1:2])
hamsterLetters=matrix(c(" (e)"," (f)",""," (g)"," (h)","","","",""),ncol=3,byrow=TRUE)
hamsterTot=matrix(paste0(hamsterTot,hamsterLetters),byrow=FALSE,ncol=3)
colnames(hamsterTot)<-c(colnames(hamster),"total")
rownames(hamsterTot)<-c(rownames(hamster),"total")
knitr::kable(hamsterTot,booktabs = TRUE)
```

---
### Absolute risk difference (ARD)
- $\pi_1=P[\text{agressive male } \vert \text{hostile}]$
- $\hat \pi_1=(e+f)/n$, with $n=e+f+g+h$.

- $\pi_0=P[\text{agressive male } \vert \text{ friendly}]$
- $\hat \pi_0=(e+g)/n$
\begin{equation*}
\widehat{\text{ARD}}=\hat\pi_1-\hat\pi_0=\frac{e+f}{n}-\frac{e+g}{n}=\frac{f-g}{n}
\end{equation*}
- Only affected by discordant pairs $f$ en $g$

---

- Standard error on ARD
\begin{equation*}
\text{SE}_{\widehat{\text{ARD}}}=\frac{1}{n}\sqrt{f+g-\frac{(f-g)^2}{n}}
\end{equation*}

- If we have large number of observations we can use the CLT to establish an $(1-\alpha)100\%$ CI on the ARD
$$\left[\widehat{\text{ARD}}-z_{\alpha/2}\text{SE}_{\widehat{\text{ARD}}},\widehat{\text{ARD}}-z_{\alpha/2}\text{SE}_{\widehat{\text{ARD}}}\right]$$
or
$$\left[\frac{f-g}{n}-\frac{z_{\alpha/2}}{n}\sqrt{f+g-\frac{(f-g)^2}{n}},\frac{f-g}{n}+\frac{z_{\alpha/2}}{n}\sqrt{f+g-\frac{(f-g)^2}{n}}\right] $$

---

```r
hamster <- matrix(c(3,17,1,13),ncol=2,byrow=TRUE)
rownames(hamster) <- c("hostile-agressive", "hostile-non-agressive")
colnames(hamster) <- c("friendly-agressive","friendly-non-agressive")

f=hamster[1,2]; g=hamster[2,1] ;n=sum(hamster)
riskdiff=(f-g)/n
riskdiff
se=sqrt(f+g-(f-g)^2/n)/n
se
ci<-riskdiff+c(-1,1)*qnorm(0.975)*se
ci
```

---

\begin{equation*}
\widehat{\text{ARD}}=\frac{17-1}{34}=0.471
\end{equation*}
The absolute risk difference on choosing for an agressive male is 47.1% larger upon staying in a hostile environment that when residing in a gentle environment.
- The standard error
\begin{equation*}
\text{SE}_{\widehat{\text{ARD}}}=\frac{1}{34}\sqrt{17+1-\frac{(17-1)^2}{34}}=0.0952
\end{equation*}
- A 95\% confidence interval on this absolute risk difference is
\begin{equation*}
\left[0.471-1.96\times 0.0952,0.471+1.96\times 0.0952\right]=[0.284,0.658]
\end{equation*}

---

## McNemar test
```r
knitr::kable(hamsterTot,booktabs = TRUE)
```

- Assess if risk on choice for agressive male differs between residing in hostile and friendly environment.
- Only discordant pairs give information.
- $f>g$ indication against $H_0$: choice of partner not associated with environment.
- Evaluate probability that in a random discordant pair, a female chooses an agressive male upon a stay in a hostile environment.
- We estimate the probability as
  $$\frac{f}{f+g}$$

---

  \begin{eqnarray*}
  \text{E}\left[f/(f+g)\right]&\stackrel{H_0}{=}& 0.5\\
  f & \stackrel{H_0}{\sim}& \text{Binom}(n=f+g,\pi=0.5)\\
  \text{SE}_{\frac{f}{f+g}} & \stackrel{H_0}{=}& \sqrt{(f+g)\times 0.5\times 0.5}=\frac{\sqrt{f+g}}{2}
\end{eqnarray*}

---

- Asymptotically a one-sample z-test (based on the Normal distribution)

\begin{equation*}
z=\frac{f-(f+g)/2}{\sqrt{f+g}/2}=\frac{f-g}{\sqrt{f+g}}
\end{equation*}

- Normal approximation is good if $$f \times g/(f+g) \geq 5$$

The **Mc Nemar test** is the analogon of the paired t-test for binary qualitative variables.

---

In R we can conduct the analysis using the  `mcnemar.test` function
```r
mcnemar.test(hamster)
```


- We reject the null hypothesis at the 5% significance level
- We conclude that the choice of partner is extremely significantly associated with the environment.

---

- Normale approximation is not optimal and we can perform an exact test using the binomiale test

```r
binom.test(x=f,n=f+g,p=0.5)
```

---

### Conclusion

- We conclude that the partner choice is extremely signficantly associated with the environment ($p<0.001$).
- The probability on choosing an agressive male is on average `r format(riskdiff*100,digits=3)`% higher when a female hamster resides in a hostile environment than when she resides in a friendly environment (95% CI [`r paste(format(ci*100,digits=3),collapse=",")`]%).

---

---

[← Test for a proportion](02-test-for-a-proportion.md) · [Up: contents](index.md) · [Unpaired observations →](04-unpaired-observations.md)
