---
title: Prediction-intervals
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Prediction-intervals

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- We can also make a prediction for the location of a new observation that would be collected in a new experiment for a patient with a particular value for their ESR1 expression

- It is important to notice that this experiment still has to be conducted. So we want to predict the non-observed individual expression value for a novel patient.

- For a novel independent observation $Y^*$
$$
  Y^* = g(x) + \epsilon^*
$$
with $\epsilon^*\sim N(0,\sigma^2)$ and $\epsilon^*$ independent of the observations in the sample $Y_1,\ldots, Y_n$.

- We predict a new log-S100A8 for a patient with a known log2-ESR1 expression level x
$$
  \hat{y}(x)=\hat{\beta}_0+\hat{\beta}_1 \times x
$$

- The estimated mean outcome and prediction for a new observation are equal.

- But, their sample distributions are different!

    - Uncertainty on the estimated mean outcome  $\leftarrow$ uncertainty on estimated model parameters $\hat\beta_0$ en $\hat\beta_1$.
    - Uncertainty on new observation $ $\leftarrow$ *uncertainty on estimated mean* and  *additional uncertainty* because the new observation will deviate around the mean!


$$\text{SE}_{\hat{Y}(x)}=\sqrt{\hat\sigma^2+\hat\sigma^2_{\hat{g}(x)}}=\sqrt{MSE\left\{1+\frac{1}{n}+\frac{(x-\bar X)^2}{\sum\limits_{i=1}^n (X_i-\bar X)^2}\right\}}.$$

$$\frac{\hat{Y}(x)-Y}{\text{SE}_{\hat{Y}(x)}}\sim t_{n-2}$$

- Note, that a **prediction-interval** (PI) is an improved version of a reference-interval when the model parameters are unknown: Uncertainty on model parameters +  t-distribution.


```r
p <- predict(lm2,newdata=data.frame(ESR1=grid), interval="prediction")
head(p)
```

```r
preddata<-data.frame(cbind(grid=grid%>%log2,p))
brca %>% ggplot(aes(x=ESR1%>%log2,y=S100A8%>%log2)) +
  geom_point() +
  geom_smooth(method="lm") +
     geom_line(aes(x=grid,y=lwr),preddata,color="blue") +
  geom_line(aes(x=grid,y=upr),preddata,color="blue")
```

```r
preddata<-data.frame(cbind(grid,2^p))
brca %>% ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_line(aes(x=grid,y=fit),newdata) +
  geom_line(aes(x=grid,y=lwr),newdata,color="grey") +
  geom_line(aes(x=grid,y=upr),newdata,color="grey") +
    geom_line(aes(x=grid,y=lwr),preddata,color="blue") +
  geom_line(aes(x=grid,y=upr),preddata,color="blue")
```


### NHANES voorbeeld


- Replace reference interval for cholesterol level from chapter 2 by prediction-interval.

- Reference interval

```r
library(NHANES)
fem <- NHANES %>% filter(Gender=="female"&!is.na(DirectChol))

exp(fem$DirectChol%>%log%>%mean + c(-1,1)* qnorm(0.975) * (fem$DirectChol%>%log%>%sd))
```

- prediction interval

```r
lmChol <- lm(DirectChol %>% log2~1,data=fem)
predInt <- predict(lmChol,interval="prediction",newdata=data.frame(noPred=1))
round(2^predInt,2)
```


Note, that the prediction interval is almost similar to the reference interval for the large sample. Indeed we could estimate the parameters very precise.

We will do the same thing for the small sample size of 10 patients.

- Reference interval

```r
set.seed(1)
fem10<- NHANES %>% filter(Gender=="female"&!is.na(DirectChol)) %>% sample_n(size=10)

2^(fem10$DirectChol%>%log2%>%mean + c(-1,1)* qnorm(0.975) * (fem10$DirectChol%>%log2%>%sd))
```

- Prediction interval

```r
lmChol10 <- lm(DirectChol %>% log2~1,data=fem10)
predInt10 <- predict(lmChol10,interval="prediction",newdata=data.frame(noPred=1))
round(2^predInt10,2)
```

- Note, that the PI now captures uncertainty in parameter estimators (mean and standard error).
And that the interval becomes much wider! This is particularly important here for the upper limit because we back-transformed the data!

- The interval is almost as wide as the one based on the large sample.

- In small samples it is very important to account for this additional uncertainty.

---

[← Invalid assumptions](06-invalid-assumptions.md) · [Up: contents](index.md) · [Sum of squares and Anova-table →](08-sum-of-squares-and-anova-table.md)
