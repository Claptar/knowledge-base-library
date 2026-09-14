---
title: Unpaired observations
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd
source_file: sources/gtpb-psls20/theory/10-categoricalDataAnalysis.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Unpaired observations

**Source:** [`theory/10-categoricalDataAnalysis.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

## Genetic association study

- Are genetic polymorphisms in the BRCA1 gene associated with breast cancer?
- Retrospective case-control study with 800 breast cancer cases en 572 controls

```r
brca<-read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/brca.csv")
head(brca)
summary(brca)
```

---

```r
brcaHlp <- data.frame(Genotype=c("Pro/Pro","Pro/Leu","Leu/Leu","Totaal"),Control=c("266 (a)","250 (b)","56 (c)","572 (a+b+c)"),Cases=c("342 (d)","369 (e)","89 (f)","800 (d+e+f)"),Total=c("608 (a+d)","619 (b+e)","145 (c+f)","1372 (n)"))
knitr::kable(brcaHlp,
  booktabs = TRUE
)
```

- In case-control study one chooses a fixed number of cases and controls and registers which exposures they had in the past.
- Retrospective study
- Impossible to assess risks and risk-differences on breast cancer because the proportion of cases and controls does not reflect that in the population!

---

```r
brcaHlp=data.frame(Genotype=c("Pro/Pro","Pro/Leu","Leu/Leu","Totaal"),Controls=c("266 (a)","250 (b)","56 (c)","572 (a+b+c)"),Cases=c("342 (d)","369 (e)","89 (f)","800 (d+e+f)"),Total=c("608 (a+d)","619 (b+e)","145 (c+f)","1372 (n)"))
knitr::kable(brcaHlp,
  booktabs = TRUE
)
```

- Is possible to assess probability on allel Leu/Leu
    - cases: $\pi_1=f/(d+e+f)=89/800=11.1\%$
    - controls:$\pi_0=c/(a+b+c)=56/572=9.8\%$
- Relative risk on exposure for cases versus controls is $11.1/9.8=1.14$.
- The probability on the Leu/Leu genotype is 14% higher for women with breast cancer than for women without borstkanker.
- It suggests an association, but it does not let us conclude how much higher the risk is on breast cancer for women with the Leu/Leu genotype as compared to the other women.
- Other statistic?

---

\begin{equation*}
Odds=\frac{p}{1-p}
\end{equation*}
with $p$ the probability on the event.

Transformation of risk with following properties:

  - odds has value between 1 and $\infty$.

  - odds only equals 1 for probability $p=1/2$.

  - de odds increases if probability increases.

- popular in gambling: how much more likely is it to win than to loose

---

```r
brcaHlp=data.frame(Genotype=c("Pro/Pro","Pro/Leu","Leu/Leu","Totaal"),Controls=c("266 (a)","250 (b)","56 (c)","572 (a+b+c)"),Cases=c("342 (d)","369 (e)","89 (f)","800 (d+e+f)"),Total=c("608 (a+d)","619 (b+e)","145 (c+f)","1372 (n)"))
knitr::kable(brcaHlp,
  booktabs = TRUE
)
```

Odds on allel Leu/Leu

- Cases: $\mbox{odds}_1=\frac{ f/(d+e+f)}{(d+e)/(d+e+f)}=f/(d+e)=89/711=0.125$. The double Leu/Leu variant is 8 times less likely than other allele combinations in the breast cancer cases
- Controls: $\mbox{odds}_2=c/(a+b)=56/516=0.109$.

- Association between exposure and outcome:
$$
OR_{Leu/Leu}=\frac{\mbox{odds}_T}{\mbox{odds}_C}= \frac{f/(d+e)}{c/(a+b)}=\frac{f/(d+e)}{c/(a+b)}=1.15
$$

---


```r
brcaHlp=data.frame(Genotype=c("Pro/Pro","Pro/Leu","Leu/Leu","Totaal"),Controls=c("266 (a)","250 (b)","56 (c)","572 (a+b+c)"),Cases=c("342 (d)","369 (e)","89 (f)","800 (d+e+f)"),Total=c("608 (a+d)","619 (b+e)","145 (c+f)","1372 (n)"))
knitr::kable(brcaHlp,
  booktabs = TRUE
)
```

- If the study would have been a random sample of the population (number of cases and controls not fixed by design) then we would be able to calculate the odds ratio on breast cancer for people with and without the double Leu/leu variant.
\begin{equation*}
OR_{case}=\frac{ \frac{ f}{c}}{ \frac{(d+e)}{(a+b)}} = \frac{f(a+b)}{c(d+e)}=OR_{Leu/Leu}=1.15,
\end{equation*}
- OR is a symmetric statistic!
- OR on borstcancer can be estimated!
- The odds on borstcancer is 15% higher for women with this specific allele combination.

---

- Is the difference large enough to generalize the effect in the sample towards the population?

- We will first rewrite the data in a 2x2 table

```r
brcaTab2 <- table(brca$variant2,brca$cancer)
brcaTab2 <- brcaTab2[2:1,]
brcaHlp2 <- data.frame(Genotype=c("other","Leu/Leu","Total"),Controls=c("516 (a)","56 (b)","572 (a+b)"),Cases=c("711 (c)","89 (d)","800 (c+d)"),Totaal=c("1227 (a+c)","145 (b+d)","1372 (n)"))
knitr::kable(brcaHlp2,
  booktabs = TRUE
)
```

---

## Pearson Chi-square test for independent samples

- Test association between categorical exposure(e.g. variant, X) en categorical response (e.g. disease, Y).
$$H_0: \text{There is no association between } X \text{ and } Y \text{ vs } H_1: X \text{ and } Y \text{ are associated}$$

- Consider row totals $n_\text{other}=a+c$, $n_\text{leu,leu}=b+d$ and
- column totals $n_\text{contr}=a+b$ en $n_\text{case}=c+d$.
- They give information on *marginal distribution* of the exposure (variant, X) and outcome (disease, Y),
but not on the association between these variables.
- Under $H_0$ $X$ and $Y$ are independent and one expects  that $(b+d)/n$
of the $a+b$ controls have a Leu/Leu variant, or that $(a+b)(b+d)/n$ of them has a Leu/Leu variant
- We can calculate this expected number $E_{ij}$ under the null hypothesis for *each cell* of the $2
\times 2$ table.

---

- $E_{11}$ = Expected number under $H_0$ in  (1,1)-cell = `r sum(brcaTab2[1,])` $\times$ `r sum(brcaTab2[,1])`/`r sum(brcaTab2)` = `r format(sum(brcaTab2[1,])*sum(brcaTab2[,1])/sum(brcaTab2),digits=4)` ;

- $E_{12}$ = Expected number under $H_0$ in  (1,2)-cell = `r sum(brcaTab2[1,])` $\times$ `r sum(brcaTab2[,2])`/`r sum(brcaTab2)` = `r format(sum(brcaTab2[1,])*sum(brcaTab2[,2])/sum(brcaTab2),digits=4)` ;

- $E_{21}$ = Expected number under $H_0$ in  (2,1)-cell = `r sum(brcaTab2[2,])` $\times$ `r sum(brcaTab2[,1])`/`r sum(brcaTab2)` = `r format(sum(brcaTab2[2,])*sum(brcaTab2[,1])/sum(brcaTab2),digits=4)` ;

- $E_{22}$ = Expected number under $H_0$ in  (2,2)-cell = `r sum(brcaTab2[2,])` $\times$ `r sum(brcaTab2[,2])`/`r sum(brcaTab2)` = `r format(sum(brcaTab2[2,])*sum(brcaTab2[,2])/sum(brcaTab2),digits=4)` ;

Test-statistic:
\begin{eqnarray*}
X^2 &=& \frac{\left (|O_{11} - E_{11}| - .5 \right)^2 }{ E_{11}} + \frac{
\left ( |O_{12} - E_{12}| - .5 \right)^2 }{E_{12} }+ \\
&&\quad\quad
\frac{ \left ( |O_{21}
- E_{21}| - .5 \right)^2 }{E_{21}}+ \frac{ \left ( |O_{22} - E_{22}| - .5
\right)^2 }{E_{22} }\\
 X^2 &\stackrel{H_0}{\longrightarrow}& \chi^2(df=1)
\end{eqnarray*}

---

```r
grid <- seq(0,10,.1)
plot(grid,dchisq(grid,1),type="l",lwd=2)
dfs <- c(1,2,5)
for (i in 2:3)
	lines(grid,dchisq(grid,dfs[i]),col=i,lwd=2)
legend("topright",lty=1,lwd=2,col=1:3,legend=sapply(dfs, function(d) as.expression(substitute(chi[df==val]^2,list(val=d)))))
```

---

- A large value of the test statistic gives an indication that the null hypothesis is false.
- The test will reject $H_0$ at the $\alpha 100\%$
significance level as soon as the observed test-statistic is larger than the $100\%(1-\alpha)$-quantile, $\chi^2_{1,
\alpha}$, of the $\chi^2_1$-distribution.
- Otherwise we do not reject $H_0$.
- The p-value of a 2-sided test is the probability to observe a larger test-statistic in a random sample under the null than what we observed in our sample.
$$p=P_0[\chi^2_1 \geq x^2]$$.

---

```r
expected <- matrix(0,nrow=2,ncol=2)
for (i in 1:2)
	for (j in 1:2)
		expected[i,j] <-
			sum(brcaTab2[i,])*sum(brcaTab2[,j])/sum(brcaTab2)
expected
x2 <- sum((abs(brcaTab2-expected) - .5)^2/expected)
1-pchisq(x2,1)
```

---

- Because $O_{ij}$ are discrete values, the $X^2$ can only take discrete values and the continuouss $\chi^2_1$-distribution is only an approximation of the real distribution.
- To improve the approximation one substracts 0.5 from the value in each cell:
*continuity-correction*
- We refer to this test as *Pearson Chi-squared test with Yates correction*.
- When the correction is not used (i.e. when the values of `0.5' in the estimator $X^2$ are replaced) we use the *Pearson Chi-squared test*.

---

In R you can switch the correction on or off by setting the argument `correct` on TRUE or FALSE, respectively:

```r
chisq.test(brcaTab2)
chisq.test(brcaTab2,correct=FALSE)
```

---

- Even with the $\chi^2_1$ correction the approximation is only valid if non of the cells has an expected count below 5 under $H_0$.
- When the $\chi^2$-approximation is invalid we will use *Fisher's exact test*.
-  Null hypothesis is also that $X$ and $Y$ are independent, and, the alternative hypothesis that $X$ and $Y$ are dependent.

```r
fisher.test(brcaTab2)
```

---


## Extension to categorical variables with multiple levels

- The $\chi^2$-test can also be used if one of the categorical variables $X$ and $Y$ has more than 2 levels

- Again: the null hypothesis $H_0$: $X$ and $Y$ are independent (not associated), against the alternative $H_A: X$ and $Y$
are associated.

- Let the variable in the rows have $r$ different possible outcomes and the one in the columns $c$ possible outcomes, then we obtain an $r \times c$ table.

- Again we will compare the observed values in  cell $(i,j)$, referred to as $O_{ij}$, with the expected number under $H_0$, $E_{ij}$
 - Again $E_{ij}$ is the product of the $i^\text{th}$ row-total and the $j^\text{th}$ column total devided by the overall total.

\begin{equation*}
X^2 = \sum_{ij} \frac{\left (O_{ij} - E_{ij}\right)^2 }{ E_{ij}}
\end{equation*}

---

- We can show that the statistic follows a $\chi^2$ distribution with $(r-1) \times
(c-1)$ degrees of freedom under $H_0$.
- No continuity correction
- **Pearson $\chi^2$ test** is analogon of one-way ANOVA for qualitative variables.

---


```r
brcaTab <- table(brca$variant,brca$cancer)
chisq.test(brcaTab)
```

- To assess if the variant of the BRCA1 gene is associated with breast cancer we conducted a  Pearson $\chi^2$test for the $3 \times 2$ table.
- The statistic is now `r format(chisq.test(brcaTab)$statistic,digits=4)` and follows a $\chi^2$ distribution with `r chisq.test(brcaTab)$parameter` degrees of freedom under $H_0$. The probability to obtain a $\chi^2$-test statistic in a random sample under $H_0$ that is more extreme than `r format(chisq.test(brcaTab)$statistic,digits=4)`, is `r format(chisq.test(brcaTab)$p.value*100,digits=2)`%.
- On the 5% level of significance we conclude that the variant of the BRCA-gene is not associated with breast cancer.

---

---

[← Test for association between two qualitative variables](03-test-for-association-between-two-qualitative-variables.md) · [Up: contents](index.md) · [Logistic regression →](05-logistic-regression.md)
