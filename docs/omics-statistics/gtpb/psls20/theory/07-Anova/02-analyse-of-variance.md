---
title: Analyse of Variance
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd
source_file: sources/gtpb-psls20/theory/07-Anova.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Analyse of Variance

**Source:** [`theory/07-Anova.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Correct solution for testing problem: ANalysis Of VAriance (ANOVA)

- We develop the method for 3 groups (prostacyclin example)
- Model data with linear model by using dummy variables.
- 1 dummy variable less than the number of groups. Here we need 2 dummy variables.
- Generalizing to g groups $g>3$ is trivial (extra dummy variables)

### Model

\begin{eqnarray}
  Y_i &=& g(x_{i1},x_{i2}) + \epsilon_i\\
  Y_i &=& \beta_0+\beta_1 x_{i1} +\beta_2 x_{i2} +\epsilon_i
\end{eqnarray}

- $Y_i$ de outcome for observation $i$ ($i=1,\ldots, n$)
\vspace{7pt}
- $\epsilon_i\text{i.i.d.} N(0,\sigma^2)$
\vspace{7pt}
- and dummy variables
$$x_{i1} = \left\{ \begin{array}{ll}
1 & \text{ if observation $i$ belongs to middle dose group (M)} \\
0 & \text{ if observation $i$ belongs to other dose group} \end{array}\right.$$
$$x_{i2} = \left\{ \begin{array}{ll}
1 & \text{ if observation $i$ belongs to high dose group (H)} \\
0 & \text{if observation $i$ belongs to other dose group} \end{array}\right. .$$
\vspace{7pt}
 - Low dose group (L) with $x_{i1}=x_{i2}=0$ is  *reference group*

Regression-model can be rewritten as a model for each group :
\vspace{-20pt}
\begin{eqnarray*}
 Y_{i\vert \text{dose=L}} &=& \beta_0+\epsilon_i \\
 Y_{i\vert \text{dose=M}} &=& \beta_0+\beta_1+ \epsilon_i  \\
 Y_{i\vert \text{dose=H}} &=& \beta_0+\beta_2 + \epsilon_i
\end{eqnarray*}
with $\epsilon_i \sim N(0,\sigma^2)$
\vspace{10pt}

Interpretation of model parameters:
\vspace{-20pt}
 \begin{eqnarray*}
   \beta_0 &=&  \text{E}\left[Y_i \mid \text{treatment with low dose group L}\right] \\
   \beta_1 &=&  (\beta_0+\beta_1)-\beta_0 = \text{E}\left[Y_i \mid \text{treatment M}\right] - \text{E}\left[Y_i \mid \text{treatment L}\right] \\
   \beta_2 &=&  (\beta_0+\beta_2)-\beta_0 = \text{E}\left[Y_i \mid \text{treatment H}\right]-\text{E}\left[Y_i \mid \text{treatment L}\right].
 \end{eqnarray*}

 1.  $\beta_0$ is the mean outcome for group L
 \vspace{7pt}
 2.  $\beta_1$ is effect (difference in mean  concentration) of group M vs group L
 \vspace{7pt}
 3.  $\beta_2$ is effect of group H vs group L


We reformulate the model by using $\mu$-notations:
 \vspace{-7pt}
 \begin{eqnarray*}
  Y_{i\vert \text{dose=L}} &=& \beta_0+\epsilon_i = \mu_1+\epsilon_i \\
  Y_{i\vert \text{dose=M}} &=& \beta_0+\beta_1+ \epsilon_i = \mu_2+\epsilon_i \\
  Y_{i\vert \text{dose=H}} &=& \beta_0+\beta_2 + \epsilon_i = \mu_3+\epsilon_i .
 \end{eqnarray*}
 with $\epsilon_i \sim N(0,\sigma^2)$ and
 $$  \mu_j = \text{E}\left[Y_i \mid \text{treatment group } j\right].$$

 Original null hypothese
 $$H_0:\mu_1=\mu_2=\mu_3$$
 can be formulated as
 $$H_0: \beta_1=\beta_2=0.$$

Model allows us to use all methods from linear regression.

- Parameter estimators for means, variances and  standard errors
\vspace{10pt}
- Inference: Confidence intervals, hypothesis tests
\vspace{10pt}
  - Test $H_0: \beta_1=\beta_2=0$ with $F$-test.

## Prostacyclin example

```r
model1 <- lm(prostac~dose,data=prostacyclin)
summary(model1)
```

---

[← Prostacyclin Example](01-prostacyclin-example.md) · [Up: contents](index.md) · [Sum of squares and Anova →](03-sum-of-squares-and-anova.md)
