---
title: Analysis
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
source_file: sources/gtpb-psls20/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Analysis

**Source:** [`tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/tutorialScripts/excercises/08_multipleRegression/Multiple_regression_FEV_2.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
lm_sa <- lm(log(fev)~smoking+age+gender, data=fev)

summary(lm_sa)
plot(lm_sa)
```


```r
table(fev$gender,fev$smoking)
```

```r
```


```r
full_formula <- log(fev)~ age + height_cm + smoking + gender + smoking:age + smoking:height_cm + smoking:gender + age:height_cm + age:gender + height_cm:gender

lm_full <- lm(full_formula, data=fev)

summary(lm_full)
```

```r
lm_red <- lm(log(fev)~ age + height_cm + smoking + gender, data=fev)

summary(lm_red)
```


```r
lm_2 <- lm(log(fev)~ age + height_cm + gender + smoking + age:height_cm + age:gender + height_cm:gender, data=fev)

anova(lm_full, lm_2)
```

```r
summary(lm_2)
```

```r
car::vif(lm_2)
```


```r
summary(lm_red)
```


```r
summary(lm_2)
```


```r
lm_3 <- lm(log(fev)~ age + height_cm + gender + age:height_cm + age:gender + height_cm:gender, data=fev)

anova(lm_full, lm_3)
```

```r
vif(lm_3)
```


```r
plot(lm_full)
```

```r
summary(lm_full)
```

```r
lm_2 <- lm(log(fev)~ age + height_cm + smoking + gender + smoking:age, data=fev)

plot(lm_2)

summary(lm_2)
```

```r
install.packages("margins")
library(margins)
```


```r
lm_3 <- lm(log(fev)~ age + height_cm + smoking + gender + smoking:age, data=fev_11_15)
summary(margins(lm_3))
#summary(lm_3)
```


## Multiple regression analysis with forward model selection

Now, we will perform a multiple regression analysis on the data,
accounting for all the required variables that may influence the
relationship between smoking and FEV.

** Note: to meet the required assumptions for linear regression, **
** we will need to log-tranform the FEV response variable. **

Having spurious terms in the model (main effects and interaction terms)
may make the model worse. If an effect or interaction has no added
value, it might be better not to have it in the model.

We can select the best/required terms by performing a forward selection.
Here, we will start with an _empty_ model, i.e. a model without
explanatory variables. Each step, we will add the most useful
variable to the model

```r
full_formula <- log(fev)~ age + height_cm + smoking + gender + smoking:age + smoking:height_cm + smoking:gender

subfev <- fev[,c(-3)] ## retain the potential explanatory variables and the  response variable, remove height (inches)

m1 <- lm(log(fev)~1, subfev) # empty model
add1(m1, scope=full_formula, data=subfev, test="F")
```

The variable _height-cm_ has the most significant contribution
to the model (based on p-value and AIC. As such, we will include
it in our improved model:

```r
m2 <- update(m1,~.+height_cm)
add1(m2, scope=full_formula, data=subfev, test="F")
```

After doing this, _age_ has the most significant contribution
to the model. As such, we will include it in our improved model:

```r
m3 <- update(m2,~.+age)
add1(m3, scope=full_formula, data=subpoison, test="F")
```

After including height_cm and age in the model,
the _smoking_ status (again) appears significant.
Include it in the model:

```r
m4 <- update(m3,~.+smoking)
add1(m4, scope=full_formula,data=subfev, test="F")
```

After including the smoking term, none of the remaining
model parameters (including both interactions) appear
significant (5%). As such, we won't include any other
parameters in the model. As such, based on the forward
selection, we assume the following model:

$$y_i=\beta_0+\beta_a x_{ia} + \beta_h x_{ih} + \beta_{s1} x_{is1} + \epsilon_i,$$

This model has a main effect for smoking (s), age (a) and height (h).

## Check the assumptions

For checking the assumptions of the final model,
we will first fit it:

```r
lm_full <- lm(log(fev) ~ age + height_cm + smoking, data=fev)
plot(lm_full)
```

List assumptions:

1. The observations are independent of each other
2. Linearity between the response and predictor variable
3. The residues of the model must be normally distributed
4. Homoscedasticity of the data

1. The first assumption is **met**: children that are more
alike in terms of age, height and smoking status will probably
have more similar FEV values, but this is accounted for by
the model.

2. The linearity assumption is **met** (see plot 1).

3. The normality assumption is **met** (see plot 2).

4. The homosccedasticity assumption is **met** (see plot 3).

## Conclusion

```r
library(car)
Anova(lm_full, type=3)
```

```r
coefficients(lm_full)
confint(lm_full)
```


- Age main effect: The log FEV for children is, on
average, `r format(abs(lm_full$coefficients["age"]),digits=3)` liters
higher for every unit increase in age (year), after correcting
for height and smoking effects (95% CI [0.01725221; 0.03166769]).
This increase is extremely significant (p=6.001e-11) on the 5%
significance level.

- Heigth main effect: The log FEV for children is, on
average, `r format(abs(lm_full$coefficients["height_cm"]),digits=3)`
liters higher for every unit increase in height (cm), after correcting
for age and smoking effects (95% CI [0.01561981; 0.01827859]).
This increase is extremely significant (p < 2.2e-16) on the 5%
significance level.

- Smoking main effect: The log FEV for children is, on
average, `r format(abs(lm_full$coefficients["smoking"]),digits=3)`
liters lower for smokers than for non-smokers, after correcting
for age and height effects (95% CI [-0.09651575; -0.01381958]).
This decrease is highly significant (p =0.009007) on the 5%
significance level.

---

[← Data tidying](04-data-tidying.md) · [Up: contents](index.md)
