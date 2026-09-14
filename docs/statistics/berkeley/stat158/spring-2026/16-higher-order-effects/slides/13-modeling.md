---
title: Modeling
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/16-higher-order-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Modeling

**Source:** [`16-higher-order-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/16-higher-order-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Calculating estimates

A shortcut: use `lm()`.

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
options(contrasts = c("contr.sum", "contr.poly"))
m3 <- lm(strength ~ time * pressure * hard, data = paper)
summary(m3)
```


    Call:
    lm(formula = strength ~ time * pressure * hard, data = paper)

    Residuals:
        Min      1Q  Median      3Q     Max
    -0.8500 -0.3625  0.0000  0.3625  0.8500

    Coefficients:
                            Estimate Std. Error  t value Pr(>|t|)
    (Intercept)           198.055556   0.100769 1965.448  < 2e-16 ***
    time1                  -0.750000   0.100769   -7.443 6.75e-07 ***
    pressure1              -0.472222   0.142508   -3.314 0.003863 **
    pressure2              -0.563889   0.142508   -3.957 0.000924 ***
    hard1                   0.611111   0.142508    4.288 0.000442 ***
    hard2                  -0.097222   0.142508   -0.682 0.503785
    time1:pressure1         0.233333   0.142508    1.637 0.118924
    time1:pressure2        -0.341667   0.142508   -2.398 0.027567 *
    time1:hard1            -0.333333   0.142508   -2.339 0.031066 *
    time1:hard2             0.225000   0.142508    1.579 0.131782
    pressure1:hard1        -0.794444   0.201537   -3.942 0.000956 ***
    pressure2:hard1         0.322222   0.201537    1.599 0.127266
    pressure1:hard2         0.338889   0.201537    1.682 0.109930
    pressure2:hard2         0.005556   0.201537    0.028 0.978312
    time1:pressure1:hard1  -0.250000   0.201537   -1.240 0.230730
    time1:pressure2:hard1  -0.150000   0.201537   -0.744 0.466314
    time1:pressure1:hard2   0.316667   0.201537    1.571 0.133535
    time1:pressure2:hard2  -0.083333   0.201537   -0.413 0.684133
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

    Residual standard error: 0.6046 on 18 degrees of freedom
    Multiple R-squared:  0.9008,    Adjusted R-squared:  0.807
    F-statistic: 9.611 on 17 and 18 DF,  p-value: 7.797e-06

## Main Effects Plot

## Time:Pressure Interaction

## ANOVA Table

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova3 <- aov(strength ~ time * pressure * hard, data = paper)
summary(anova3)
```

                       Df Sum Sq Mean Sq F value   Pr(>F)
    time                1 20.250  20.250  55.395 6.75e-07 ***
    pressure            2 19.374   9.687  26.499 4.33e-06 ***
    hard                2  7.764   3.882  10.619   0.0009 ***
    time:pressure       2  2.195   1.097   3.002   0.0750 .
    time:hard           2  2.082   1.041   2.847   0.0843 .
    pressure:hard       4  6.091   1.523   4.166   0.0146 *
    time:pressure:hard  4  1.973   0.493   1.350   0.2903
    Residuals          18  6.580   0.366
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
summary(anova3)[[1]]$`F value`
```

    [1] 55.395137 26.499240 10.619301  3.002280  2.847264  4.165653  1.349544
    [8]        NA

## Randomization-based Inference

Recall for 2 factor w interactions:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
shuffle_two_factor <- function(y, a, b) {
  Y <- sample(y) # source of randomness

  battery_sim <- data.frame(lifetime = Y,
                            temp = a,
                            material = b)

  battery_anova <- aov(lifetime ~ temp * material, data = battery_sim)
  anova_table <- summary(battery_anova)
  f_stats <- anova_table[[1]]$`F value`
  f_stats
}
```

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(500, shuffle_two_factor(y = battery$lifetime,
                                                a = battery$temp,
                                                b = battery$material))
f_temp_null <- null_stats[1, ]
f_material_null <- null_stats[2, ]
f_interaction_null <- null_stats[3, ]
```

---

[← Time and Pressure and Hardness](12-time-and-pressure-and-hardness.md) · [Up: contents](index.md)
