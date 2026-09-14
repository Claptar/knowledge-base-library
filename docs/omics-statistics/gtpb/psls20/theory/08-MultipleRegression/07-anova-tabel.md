---
title: ANOVA Tabel
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd
source_file: sources/gtpb-psls20/theory/08-MultipleRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# ANOVA Tabel

**Source:** [`theory/08-MultipleRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

The total SSTot is again

$$
  \text{SSTot} = \sum_{i=1}^n (Y_i - \bar{Y})^2.
$$

The residual sum of squares remains similar
$$
  \text{SSE} = \sum_{i=1}^n (Y_i-\hat{Y}_i)^2.
$$

Again the total sum of squares can be decomposed in ,
$$
  \text{SSTot} = \text{SSR} + \text{SSE} ,
$$
with
$$
  \text{SSR} = \sum_{i=1}^n (\hat{Y}_i-\bar{Y})^2.
$$

---

We have following degrees of freedom and mean sum of squares:

- SSTot has $n-1$ degrees of freedom and $\text{SSTot}/(n-1)$ is an estimator for the total variance in $Y$ (marginal distribution of $Y$).
- SSE has $n-p$ degrees of freedom and $\text{MSE}=\text{SSE}/(n-p)$ is an schatter for the residual variance of $Y$ given the predictores (i.e. an estimator for the residual variance $\sigma^2$ of the error term $\epsilon$).
- SSR has $p-1$ degrees of freedom   and $\text{MSR}=\text{SSR}/(p-1)$ is the mean sum of squares of the regression.

The determination coefficients remains as before,  i.e.
$$
  R^2 = 1-\frac{\text{SSE}}{\text{SSTot}} = \frac{\text{SSR}}{\text{SSTot}}
$$
and is the fraction of the total variability that can be explained by the regression model.

Teststatistic $F=\text{MSR}/\text{MSE}$ is under $H_0:\beta_1=\ldots=\beta_{p-1}=0$ distributed by an F distribution: $F_{p-1;n-p}$.

---

```r
summary(lmVWS)
```

---

## Additional sums of squares


Consider 2 models for the predictors $x_1$ en $x_2$:
$$
  Y_i = \beta_0+\beta_1 x_{i1} + \epsilon_i,
$$
with $\epsilon_i\text{ iid } N(0,\sigma_1^{2})$, and
$$
Y_i = \beta_0+\beta_1 x_{i1}+\beta_2 x_{i2} + \epsilon_i,
$$
with $\epsilon_i\text{ iid } N(0,\sigma_2^{2})$.

for the first (gereduceerde) model we have decomposition
$$
  \text{SSTot} = \text{SSR}_1 + \text{SSE}_1
$$
en for the second non-reduced model we have
$$
  \text{SSTot} = \text{SSR}_2 + \text{SSE}_2
$$
(SSTot is of course the same because it only depends on the response and not of the models).

---

**Definition of additional sum of squares**
The *additional sum of squares* of predictor $x_2$ as compared to the model with only $x_1$ as predictor is given by
$$
  \text{SSR}_{2\mid 1} = \text{SSE}_1-\text{SSE}_2=\text{SSR}_2-\text{SSR}_1.
$$

Note that,  $\text{SSE}_1-\text{SSE}_2=\text{SSR}_2-\text{SSR}_1$ is triviaal is because of the decomposition of the total sum of squares.

The additional sum of squares $\text{SSR}_{2\mid 1}$ can simply be interpreted as the additional variability that can be explained by adding predictor $x_2$ to the model with predictor $x_1$.

With this sum of squares we can further decompose the total sum of squares
$$
  \text{SSTot} = \text{SSR}_1+ \text{SSR}_{2\mid 1} + \text{SSE}.
$$
which follows directly from the definition $\text{SSR}_{2\mid 1}$.

---

Extension: ($s<p-1$)
$$
Y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_{s} x_{is} + \epsilon_i
$$
with $\epsilon_i\text{ iid }N(0,\sigma_1^{2})$, and ($s< q\leq p-1$)
$$
Y_i = \beta_0 + \beta_1 x_{i1} + \cdots + \beta_{s} x_{is} + \beta_{s+1} x_{is+1} + \cdots \beta_{q}x_{iq}+ \epsilon_i
$$
with $\epsilon_i\text{ iid } N(0,\sigma_2^{2})$.


The **additional sum of squares** of predictor $x_{s+1}, \ldots, x_q$ compared to a model with only predictors  $x_1,\ldots, x_{s}$ is given by

$$
  \text{SSR}_{s+1, \ldots, q\mid 1,\ldots, s} = \text{SSE}_1-\text{SSE}_2=\text{SSR}_2-\text{SSR}_1.
$$

---

### Type I Sums of Squares
Suppose that $p-1$ predictors are considered, and suppose the following sequence of models ($s=2,\ldots, p-1$)
$$
Y_i = \beta_0 + \sum_{j=1}^{s} \beta_j x_{ij} + \epsilon_i
$$
wuth $\epsilon_i\text{ iid } N(0,\sigma^{2})$.

- The corresponding sum of squares are denoted as $\text{SSR}_{s}$ and $\text{SSE}_{s}$.
- The sequence of models gives rise to the following sums of squares: $\text{SSR}_{s\mid 1,\ldots, s-1}$.
- The latter sum of squares is referred to as type I sums of squares. Note that they depend on the order in which the models were added to the model.

---

We can show for model Model with $s=p-1$ that
$$
 \text{SSTot} = \text{SSR}_1 + \text{SSR}_{2\mid 1} + \text{SSR}_{3\mid 1,2} + \cdots + \text{SSR}_{p-1\mid 1,\ldots, p-2} + \text{SSE},
$$
with $\text{SSE}$ the residual sum of squares of the model with all $p-1$ predictors
$$
  \text{SSR}_1 + \text{SSR}_{2\mid 1} + \text{SSR}_{3\mid 1,2} + \cdots + \text{SSR}_{p-1\mid 1,\ldots, p-2} = \text{SSR}
$$
with $\text{SSR}$ the sum of squares of all  $p-1$ predictors.

- The interpretation of each term depends on the order of the sequence of the regression models.

---

- Each type I SSR involves 1 predictor and has 1 degree of freedom (note that multiple dummies for a factor are typically removed together).
- For each type I SSR term the mean sum of squares is defined by  $\text{MSR}_{j\mid 1,\ldots, j-1}=\text{SSR}_{j\mid 1,\ldots, j-1}/1$.
- And teststatistic $F=\text{MSR}_{j\mid 1,\ldots, j-1}/\text{MSE}$ follows a $F_{1;n-(j+1)}$ distribution under  $H_0:\beta_j=0$ with $s=j$.
- These sums of squares are the default sum of squares in the anova function of R.

---

### Type III Sums of squares

 Type III sum of squares for predictor $x_j$ are given by the additional sum of squares
$$
  \text{SSR}_{j \mid 1,\ldots, j-1,j+1,\ldots, p-1} = \text{SSE}_1-\text{SSE}_2
$$

- $\text{SSE}_2$ the sum of squares of the residuals of the model with all $p-1$ predictors.
- $\text{SSE}_1$ sum of squares of the residuals with all $p-1$ predictors, except for predictor $x_j$.

The type III sum of squares $\text{SSR}_{j \mid 1,\ldots, j-1,j+1,\ldots, p-1}$ quantify the contribution in the total variance of the outcome explained by $x_j$ that cannot be explained by the remaining $p-2$ predictors.

---

The type III sum of squares has 1 degree of freedom because it involves 1 $\beta$-parameter.

For each type III SSR term the mean sum of squares is defined by $\text{MSR}_{j \mid 1,\ldots, j-1,j+1,\ldots, p-1}=\text{SSR}_{j \mid 1,\ldots, j-1,j+1,\ldots, p-1}/1$.

Teststatistiek $F=\text{MSR}_{j \mid 1,\ldots, j-1,j+1,\ldots, p-1}/\text{MSE}$ is $F_{1;n-p}$ distributed under $H_0:\beta_j=0$.

We can obtain these sums of squares using the `Anova` function from the `car` package.
---

```r
library(car)
Anova(lmVWS,type=3)
```

The p-values are identical to those of two-sided t-tests

Note, however, that all dummies for factors with multiple levels will be taken out of the model at once. So then the type III sum of squares will have as many degrees of freedom as the number of dummies and an omnibus test is performed for the effect of the factor.

---

#Diagnostics
## Multicollineariteit

```r
summary(lmVWS)
```

---

```r
summary(lmVWS_IntVW)
```

---

- Estimates are different from those in the additive model and the standard errors are much higher!

- This is caused by the multicollinearity problem.

- If 2 predictors are strongly correlated than they share a lot of information.

- It is therefore difficult to estimate the individual contribution of each predictor on the outcome.

- Least squares estimators become instable.

- Standard errors become inflated.

- As long as we only do predictions on the basis of the regression model without extrapolating beyond the range of the predictors observed in the sample multicolinearity is not problematic.

- But for inference it is problematic.

---

```r
cor(cbind(prostate$lcavol,prostate$lweight,prostate$lcavol*prostate$lweight))
```

- High correlation between log-tumor volume and interaction.
- It is a known problem for higher order terms (interactions and quadratic terms)

---

- Detect multicollineariteit based on the correlation matrix or scatterplot matrix is suboptimal.
- In models with 3 or more predictors, say X1, X2, X3 we can have high multicollinearity while alle pairswise correlations between the predictors are low.
- We also have multicollinearity if there is a high correlation between X1 and a linair combination of X2 and X3.

---

### Variance inflation factor (VIF)

For parameter $j$ in de regression model
$$\textrm{VIF}_j=\left(1-R_j^2\right)^{-1}$$

- In this expression $R_j^2$ is the multiple determination coefficient of the linear regression of predictor j on the remaining predictors in the model.
- VIF is 1 if predictor j is not linear associated with the remaining predictors in the model.
- VIF is larger than 1 in all andere cases.
- VIF is the factor with which the observed variance inflates as compared to a model for which all predictoren would be independend.
- VIF > 10 $\rightarrow$ strong multicollinearity.

---

### Body fat example

```r
bodyfat <- read_delim("https://raw.githubusercontent.com/GTPB/PSLS20/master/data/bodyfat.txt",delim=" ")
bodyfat %>% ggpairs()
```

---

```r
lmFat <- lm(Body_fat~Triceps+Thigh+Midarm ,data=bodyfat)
summary(lmFat)
```

---

```r
vif(lmFat)
```

---

```r
lmMidarm <- lm(Midarm ~ Triceps+Thigh,data=bodyfat)
summary(lmMidarm)
```

---


We evaluate the VIF in the prostate cancer example for the additive model and the model with interactie.

```r
vif(lmVWS)
vif(lmVWS_IntVW)
```

- Inflation in interaction terms often caused because main effect get another interpretation.

---

## Influencial Observaties


```r
set.seed(112358)
nobs<-20
sdy<-1
x<-seq(0,1,length=nobs)
y<-10+5*x+rnorm(nobs,sd=sdy)
x1<-c(x,0.5)
y1 <- c(y,10+5*1.5+rnorm(1,sd=sdy))
x2 <- c(x,1.5)
y2 <- c(y,y1[21])
x3 <- c(x,1.5)
y3 <- c(y,11)
plot(x,y,xlim=range(c(x1,x2,x3)),ylim=range(c(y1,y2,y3)))
points(c(x1[21],x2[21],x3[21]),c(y1[21],y2[21],y3[21]),pch=as.character(1:3),col=2:4)
abline(lm(y~x),lwd=2)
abline(lm(y1~x1),col=2,lty=2,lwd=2)
abline(lm(y2~x2),col=3,lty=3,lwd=2)
abline(lm(y3~x3),col=4,lty=4,lwd=2)
legend("topleft",col=1:4,lty=1:4,legend=paste("lm",c("",as.character(1:3))),text.col=1:4)
```

---

- It is not desirable that a single observation largely influences the result of a linear regression analysis

- Diagnostics allow us to detect extreme observations.
- *Studentized residuals* to spot outliers
- *Leverage* to spot observations with extreem covariate pattern

---

### Cook's distance

- A statistics to assess the influence the effect of a single observation on the regression analysis
- Cook's distance for observation i is diagnostic measure for this particular observation on all all predictions or on *all* estimated parameters.
$$D_i=\frac{\sum_{j=1}^n(\hat{Y}_j-\hat{Y}_{j(i)})^2}{p\textrm{MSE}}$$

- Observation $i$ has a large influence on the regression parameters and predictions if the  Cook's distance $D_i$ is large.
- Extreme Cook's distance if it is larger than the 50% quantile of an $F_{p+1,n-(p+1)}$-distribution.

---


```r
par(mfrow=c(2,2))
plot(lmVWS,which=5)
plot(lmVWS_IntVW,which=5)
plot(cooks.distance(lmVWS),type="h",ylim=c(0,1),main="Additive model")
abline(h=qf(0.5,length(lmVWS$coef),nrow(prostate)-length(lmVWS$coef)),lty=2)
plot(cooks.distance(lmVWS_IntVW),type="h",ylim=c(0,1), main="Model with lcavol:lweight interaction")
abline(h=qf(0.5,length(lmVWS_IntVW$coef),nrow(prostate)-length(lmVWS_IntVW$coef)),lty=2)
```

---

- Once we established that an observation is influential we can use *DFBETAS* to find the parameters for which the estimates are largely affected by the observation
-  DFBETAS of observatie i is a diagnostic measure for *each model parameter separately*.
$$\textrm{DFBETAS}_{j(i)}=\frac{\hat{\beta}_{j}-\hat{\beta}_{j(i)}}{\textrm{SD}(\hat{\beta}_{j})}$$
-  DFBETAS is extreme when it is larger than 1 in small to moderate datasets or exceeds $2/\sqrt{n}$ in large datasets.

---


```r
par(mfrow=c(2,2))
dfbetasPlots(lmVWS)
```

---

```r
par(mfrow=c(2,2))
dfbetasPlots(lmVWS_IntVW)
```

---

```r
boxplot(exp(prostate$lweight),ylab="Prostate Weight (g)")
```


---

---

[← fitted points for droplines to surface](06-fitted-points-for-droplines-to-surface.md) · [Up: contents](index.md) · [[Home](https://gtpb.github.io/PSLS20/) →](08-home-https-gtpb-github-io-psls20.md)
