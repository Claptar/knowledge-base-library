---
title: Logistic regression
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd
source_file: sources/gtpb-psls20/theory/10-categoricalDataAnalysis.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Logistic regression

**Source:** [`theory/10-categoricalDataAnalysis.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/10-categoricalDataAnalysis.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Framework to model binary data (e.g cancer vs no cancer): *logistic regression model*.
- Model binary data with continuous and/or dummy variables.

- The model assumes that observations for subject $i=1,\ldots,n$ are independent and follow a Bernoulli distribution.
- The logarithm of the odds is modelled using a linear model, also referred to as linear predictor:
\begin{equation}
\left\{
\begin{array}{ccl}
Y_i&\sim&B(\pi_i)\\\\
\log \frac{\pi_i}{1-\pi_i}&=&\beta_0 + \beta_1X_{i1} + \ldots + \beta_p X_{ip}
\end{array}\right.
\end{equation}

---

## Categorical predictor

- breast cancer example: is BRCA 1  variant associated with breast cancer.

- As in the Anova context, a factor in logistic regression is coded using dummy variables.
- 1 dummy variable less than the number of groups.

- For BRCA 1 we need two dummy variables and obtain the following linear predictor:

\begin{eqnarray*}
  \log \frac{\pi_i}{1-\pi_i} &=& \beta_0+\beta_1 x_{i1} +\beta_2 x_{i2}
\end{eqnarray*}

- with :
$$x_{i1} = \left\{ \begin{array}{ll}
1 & \text{ if subject $i$ is heterozygous, Pro/Leu variant} \\
0 & \text{if subject $i$ is homozygous, (Pro/Pro or Leu/Leu variant)} \end{array}\right. .$$
$$x_{i2} = \left\{ \begin{array}{ll}
1 & \text{ if subject $i$ is homozygous is the Leucine mutation: Leu/Leu } \\
0 & \text{ of subject $i$ is not homozygous in the Leu/Leu variant} \end{array}\right. .$$

- Homozygosity in the  wild type allele Pro/Pro is the  **reference group**.

---

We fit the model in R.

- Note that we use the function `as.factor` to convert the cancer variable to a factor variable. - We further use the function `relevel` to specify the control treatment as the reference group.
```r
brca$cancer<-brca$cancer %>% as.factor %>% relevel("control")
brca$variant<-brca$variant %>% as.factor %>% relevel("pro/pro")
brcaLogit <- glm(cancer~variant,data=brca,family=binomial)
summary(brcaLogit)
```

The intercept is the log-odds on cancer in the reference class (Pro/Pro) and the slope terms are  log odds ratios between treatment and reference class:
\begin{eqnarray*}
\log \text{ODDS}_\text{Pro/Pro}&=&\beta_0\\\\
\log \text{ODDS}_\text{Pro/Leu}&=&\beta_0+\beta_1\\\\
\log \text{ODDS}_\text{Leu/Leu}&=&\beta_0+\beta_2\\\\
\log  \frac{\text{ODDS}_\text{Pro/Leu}}{\text{ODDS}_\text{Pro/Pro}}&=&\log \text{ODDS}_\text{Pro/Leu}-\log ODDS_{Pro/Pro}\\
&=&\beta_0+\beta_1-\beta_0=\beta_1\\\\
\log  \frac{\text{ODDS}_\text{Leu/Leu}}{\text{ODDS}_\text{Pro/Pro}}&=&\beta_2
\end{eqnarray*}

- The analysis allows us to interpret the result immediately in oddses and odds ratios!

---

```r
anova(brcaLogit,test="Chisq")
```

The $\chi^2$-test on the logsitic regression model also indicates that there is no significant association between cancer status and the genetic variant of the BRCA gene ($p=$ `r format(anova(brcaLogit,test="Chisq")[2,"Pr(>Chi)"],digits=3)`).
De p-value is almost equivalent to the one of the  $\chi^2$-test (see previous section).

---

- Significant association?

    - Post-hoc tests to evaluate which of the odds ratios are different from 1.
    - For BRCA1 example we did not reject the omnibus hypothesis so no post-hoc analysis
    - For your reference we include the post hoc analysis so that you would have the code.

---

```r
suppressPackageStartupMessages({library(multcomp)})
posthoc <- glht(brcaLogit,linfct=mcp(variant = "Tukey"))
posthocTests <- summary(posthoc)
posthocTests
```

---

```r
posthocCI <- confint(posthoc)
posthocCI
```
- With the `confint` function CI are obtained on the log-odds ratios corrected for multiple testing.

---

- CI's can be backtransformed to odds ratios:

```r
OR <- exp(posthocCI$confint)
OR
```

- De odds ratios that we obtain is exactly equal to the one we calculated based on the contingency table:
- e.g  $\text{OR}_\text{Leu/Leu-Pro/Pro}=89\times 266/(56\times 342)=$ `r format((89/56)/(342/266),digits=4)`.

- Note, that statistical inference for logistic regression relies on asymptotic theory.

---

## Continuous Predictor

- Toxicolocal effect of carbon disulfite (CS$_2$) on beetles.
- Research hypothesis is there an effect of the  CS$_2$ concentration on the mortality of beetles?

##Design##
- 32 independent experiments
- Each time 1 beatle is exposed to one of 8 CS$_2$ concentrations (mg/l).
- The outcome: mortality ($y=1$) or survival ($y=0$).

```r
beetles<-read_csv("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/beetles.csv")
head(beetles)
table(beetles$dose,beetles$status)
```

---

We build a model for the log odds in function of the dose $x_i$:
$$\log \frac{\pi_i}{1-\pi_i}=\beta_0+\beta_1 \times x_i.$$

```r
beatleModel<-glm(status~dose,data=beetles,family=binomial)
summary(beatleModel)
```

----

- Intercept has an interpretation of a log odds on mortality when no $\text{CS}_2$ gas is applied.
- Very small odds on mortality ($\pi/(1-\pi)=\exp(-53.2)$) so the probability is almost 0.
- Note that this is a very large extrapolation: minimum dose in dataset is `r min(beetles$dose)` mg/l.


- Estimated odds ratio for the effect of dose on the mortality probability is $\exp(0.3013)=1.35$.
- So a beatle exposed to a CS$_2$ concentration that is 1 mg/l larger than another beatle, will on average have an odds ratio on mortality of $1.35$.

---

- We conclude that this effect is very significant ($p=$ `r round(summary(beatleModel)$coef[2,4],3)`).
- Increasing the CS$_2$ dose increases the mortality.


```r
beetlesTab<-table(beetles) %>% data.frame

data.frame(grid=seq(min(beetles$dose),max(beetles$dose),.1)) %>%
  mutate(piHat=predict(beatleModel,
	      newdata=data.frame(dose=grid),
	      type="response")) %>%
  ggplot(aes(grid,piHat))+
  geom_line() +
  xlab("dose") +
  ylab("probability (dead)") +
  geom_text(aes(x=dose%>%as.character%>%as.double,y=status%>%as.character%>%as.double,label=Freq),beetlesTab%>%filter(status==0)) +
geom_text(aes(x=dose%>%as.character%>%as.double,y=status%>%as.character%>%as.double,label=Freq),beetlesTab%>%filter(status==1))
```


---

---

[← Unpaired observations](04-unpaired-observations.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) →](06-home-https-gtpb-github-io-psls20.md)
