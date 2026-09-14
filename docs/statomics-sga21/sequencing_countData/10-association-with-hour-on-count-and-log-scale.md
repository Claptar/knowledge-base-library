---
title: association with hour on count and log scale
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd
source_file: sources/statomics-sga21/sequencing_countData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# association with hour on count and log scale

**Source:** [`sequencing_countData.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_countData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

barplot(table(Bikeshare$hr), xlab="Hour of day", ylab="Number of observations")
plot(bikers ~ hr, data=Bikeshare, pch=16, cex=1/2,
        xlab = "Hour of day", ylab = "Bikers")
plot(log1p(bikers) ~ hr, data=Bikeshare, pch=16, cex=1/2,
        xlab = "Hour of day", ylab = "Log (bikers +1)")
```

The data exploration shows that

 - More bikes are being used in better weather.
 - There seems to be a non-linear association between bicycle rentals and humidity, where in both low and high humidity conditions relatively few bikes are used, possibly reflecting very hot and very wet days respectively, while most bikes are being used at moderate humidity.
 - Bicycle rental is associated with the hour of the day, however, in a non-linear way, with clear peaks in usage at typical commute hours (6h-8h and 17h-19h). Here, we will add `hr` as a categorical variable to the model, estimating one parameter for each hour. Note that alternative strategies are possible that may be more efficient, such as incorporating `hr` as a numerical variable and modeling the non-linearity using a lower number of parameters.
 - *Disclaimer*: Note that there are likely interactions between the variables, which here we will not evaluate as our goal is to introduce a Poisson GLM rather than a full analysis of the `Bikeshare` dataset. For example, it seems likely that more people commute by bike in good weather, while fewer people will commute by bike in terrible weather. This would motivate an interaction between the variables `weathersit` and `hr`.

 ---

 - Below, we fit a Poisson GLM using the `glm` function. The number of bikers is used as a response variable, which is modeled as a function of `weathersit`, `hum` and `hr`.
 - Note that there seems to be a non-linear, though fairly simple, association between our response variable and the humidity. We will therefore add a quadratic and cubic term for humidity to the model. In order to avoid multicollinearity between the linear, quadratic and cubic humidity effects, we will first center the humidity variable and store this in a new variable called `humc`. This means that when `humc=0`, this corresponds to the average humidity in the dataset.
 - The argument `family = "poisson"` specifies the Poisson distribution for the response variable and by default the canonical link function, which is the log link, will be used.

```r
Bikeshare$humc <- Bikeshare$hum - mean(Bikeshare$hum)
m <- glm(bikers ~ weathersit + humc + I(humc^2) + I(humc^3) + hr,
         data = Bikeshare,
         family = "poisson")
summary(m)
```

#### Interpretation of estimated model parameters

 - Remember that the Poisson GLM can be defined as
 $$
  \left\{
  \begin{array}{ccc}
  Y_i & \sim & Poi(\mu_i) \\
  \log \mu_i & = & \eta_i \\
  \eta_i & = & \mathbf{X}^T_i \beta \\
  \end{array}
  \right.
  $$

 *Interpretation of the intercept.*

 - We will first interpret the intercept, in terms of the average number of bikes being used. Note that the intercept corresponds to hour 0, at good weather (`weathersit` level 1), and average humidity (`humc`=0). We will denote the intercept as $\beta_0$ and its estimate as $\hat{\beta}_0$. All other coefficients will thus denote a relative change with respect to that reference level.
 - The model definition shows that $\log \mu_i = \mathbf{X}^T_i \mathbf{\beta}$, with $\mu$ the average number of bikes being used. Since we're only working with the intercept here, we may write $\log \mu_i = \beta_0$, and thus $\mu_i = \exp \beta_0$.
 - Plugging in the estimated intercept $\hat{\beta}_0$, we have $\exp \hat{\beta}_0 =$ `r round(exp(coef(m)[1]), 2)`. In other words, in clear weather with few clouds, at average humidity and at hour 0, an average of `r round(exp(coef(m)[1]), 2)` bikes are being used.

 ---

 *Interpretation of `weathersitcloudy/misty`.*

 - We will denote this coefficient as $\beta_1$ and its estimate as $\hat{\beta}_1$.
 - Note that this coefficient defines the difference in linear predictor between `weathersit=2` and `weathersit=1`, all other variables being equal (say, at their reference level). Indeed, define $\eta_{w2}$ and $\eta_{w1}$ to denote the linear predictor at `weathersit=2`, and `weathersit=1`, respectively. Then, $\eta_{w2} - \eta_{w1} = (\beta_0 + \beta_1) - \beta_0 = \beta_1$.
 - This also means that $\beta_1 = \log \mu_{w2} - \log \mu_{w1} = \log \frac{\mu_{w2}}{\mu_{21}}$, and thus $\exp \beta_1 = \frac{\mu_{w2}}{\mu_{21}}$.
 - In our case, $\exp \hat{\beta}_1 =$ `r round(exp(coef(m)[2]), 2)`. In words: All other variables being equal, the average number of bikes being used in cloudy/misty weather is $0.85$ times (or, also, $85\%$ of) the number of bikes being used in good weather.
 - This exercise has shown us that, **due to the $\log$ link function**, the parameters in a Poisson GLM cannot be interpreted in terms of absolute differences in averages of the response variable but instead must be interpreted in terms of **multiplicative differences**!
 - If you're in a meeting and you need a quick way to interpret these parameters, remember that $exp(1) = 2.72 \approx 3$ and thus a difference of $1$ ($-1$) means the average of the response variable is about three times higher (lower).

 ---

 *Interpretation of the humidity effect.*

 - The humidity effect is a bit more involved to interpret. Due to the quadratic and cubic terms, it is not straight forward to interpret the linear term separately (and the same applies to the quadratic or cubic term); we must interpret both the linear, quadratic and cubic term simultaneously.
 - Also due to the higher-order terms, the rate of change in average bikers will not be constant across the range of humidity. We can therefore not interpret the humidity effect using a single number as we've done previously.
 - We can, however, provide some examples for specific humidity values, along with a visualization of its global effect.
  - For example, let's derive the change in average bikes being used at a humidity that is $0.2$ above average, versus average humidity.

    For average humidity $+0.2$ the linear predictor $\eta_{0.2} = \beta_0 + \beta_4 x_{hum} + \beta_5 x_{hum}^2 + \beta_6 x_{hum}^3 = \beta_0 + \beta_4 0.2 + \beta_5 0.2^2 + \beta_6 0.2^3$.

    For average humidity, the linear predictor $\eta_{0} = \beta_0 + \beta_4 x_{hum} + \beta_5 x_{hum}^2 + \beta_6 x_{hum}^3 = \beta_0 + \beta_4 0 + \beta_5 0^2 + \beta_6 0^3 = \beta_0$.

    We thus have $\log \frac{\mu_{0.2}}{\mu_0} = \beta_4 0.2 + \beta_5 0.2^2 + \beta_6 0.2^3$. In our case, $\log \frac{\hat{\mu}_{0.2}}{\hat{\mu}_0} = 0.091751*0.2 - 2.233919 * 0.2^2 - 1.823066 * 0.2^3 = -0.0856$ and thus $\frac{\hat{\mu}_{0.2}}{\hat{\mu}_0} = 0.92$. Therefore, at humidity that is $0.2$ above average, the average number of bikes being used are $0.92$ times the average number of bikes used at average humidity.
 - Just like with linear models, the `predict` function is extremely helpful when trying to visualize and understand a fitted GLM. In GLMs, the `type` argument becomes essential when using the `predict` function. Indeed, by default, estimates are provided on the linear predictor scale: in our case, on the $\log$ scale. If we'd like predictions on the scale of the response variable, we need to set `type="response"`. You can find more information in the help file using `?predict.glm`.
 - The visualization shows that the highest number of bikes are being used at around average humidity, with a decreased usage at higher and lower humidities.

```r
humidityGrid <- seq(min(Bikeshare$humc), max(Bikeshare$humc),
                    length.out = 50)
newDf <- data.frame(weathersit = factor("clear"),
                    hr = factor(8),
                    humc = humidityGrid,
                    "I(humc^2)" = humidityGrid^2,
                    "I(humc^3)" = humidityGrid^3)
yhat <- predict(m,
                newdata = newDf,
                type = "response")

plot(x = humidityGrid,
     y = yhat,
     type = 'l', lwd=2,
     xlab = "Centered humidity",
     ylab = "Average number of bikers")

```

 ---

 *Setting up a contrast.*

 - Suppose we're interested in whether there are more bikers at (A) maximum humidity (centered humidity value of $0.357$), hour 17, in the `light rain/snow` weather category, versus (B) average humidity, hour 8, in the `clear` weather category. This requires us to set up a contrast in terms of a linear combination of the model parameters.
 - **Manually by hand**:
 $$ \log \mu_A = \beta_0 + \beta_2 x_{rainSnow} + \beta_4 x_{hum} + \beta_5 x_{hum}^2 + \beta_6 x_{hum}^3 + \beta_{23} x_{hr17} \\= 3.894 - 0.556 + 0.092 * 0.357 - 2.234 * 0.357^2 - 1.823 * 0.357^3 + 2.140 = 5.143.\\
   \log \mu_B = \beta_0 + \beta_{14} x_{hr8} = 3.894 + 1.830 = 5.724.\\
   \frac{\mu_A}{\mu_B} = \exp(5.143 - 5.724) = 0.559.
   $$
   Thus, at maximum humidity, hour 17, in the `light rain/snow` weather category the average number of bikers is 56% times the average number of bikers in the average humidity, hour 8, in the `clear` weather category.
 - **Manually in `R`**: We can also use matrix multiplication to derive the estimates. We know from our manual calculations above, that the contrast of interest is $(\beta_0 + \beta_2 x_{rainSnow} + \beta_4 x_{hum} + \beta_5 x_{hum}^+ \beta_6 x_{hum}^3 + \beta_{23} x_{hr17}) - (\beta_0 + \beta_{14} x_{hr8})$. We can store this in a contrast matrix, and then multiply it with the coefficients of our model:

```r
L <- matrix(0,
            nrow = length(coef(m)),
            ncol = 1)
rownames(L) <- names(coef(m))
L["weathersitlight rain/snow",1] <- 1
L["humc",1] <- 0.357
L["I(humc^2)", 1] <- 0.357^2
L["I(humc^3)", 1] <- 0.357^3
L["hr17", 1] <- 1
L["hr8",1] <- -1
L

beta <- matrix(coef(m), ncol=1)
exp(t(L) %*% beta) # equals our manual calculation.
```

 - **Using `predict` in `R`**:

```r

---

[← association with humidity on count and log scale](09-association-with-humidity-on-count-and-log-scale.md) · [Up: contents](index.md) · [set up data frames with relevant predictor variables' values. →](11-set-up-data-frames-with-relevant-predictor-variables-values.md)
