---
title: Building a Model
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/15-main-effects/slides.html
source_file: sources/berkeley-stat158/spring-2026/15-main-effects/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Building a Model

**Source:** [`15-main-effects/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/15-main-effects/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

## Models for Two Factors

1.  Main Effects Only (Additive Model)
2.  Main Effects + Interactions

## 1. Additive Model

<span class="math display">\\$$ Y\_{i} = \\mu + \\alpha\_{j(i)} + \\beta\_{k(i)} + \\epsilon\_{i} \\$$</span>

Zero-sum constraints:

<span class="math display">\\$$ \\sum\_{j=1}^J \\alpha\_j = 0 \\quad \\quad \\quad \\sum\_{k=1}^K \\beta\_k = 0 \\$$</span>

## 1. Additive Model (simulated data)

<span class="math inline">\$\\quad\$</span>

## 1. Additive Model

Estimates:

<span class="math display">\\$$ \\begin{aligned} {\\hat{\\mu}} &= \\hat{\\bar{Y}} \\\\ {\\hat{\\alpha}}\_j &= \\hat{\\bar{Y}}\_{j} - \\hat{\\bar{Y}} \\\\ \\hat{\\beta}\_k &= \\hat{\\bar{Y}}\_{k} - \\hat{\\bar{Y}} \\end{aligned} \\$$</span>

> Why use these estimates?

## 1. Additive Model (simulated data)

<span class="math inline">\$Y\_i = \\hat{\\bar{Y}}\$</span>

## 1. Additive Model (simulated data)

<span class="math inline">\$Y\_i = \\hat{\\bar{Y}} + \\hat{\\alpha}\_j\$</span>

## 1. Additive Model (simulated data)

<span class="math inline">\$Y\_i = \\hat{\\bar{Y}} + \\hat{\\alpha}\_j + \\hat{\\beta}\_k\$</span>

## 1. ANOVA for Additive Model (simulated data)

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova1 <- aov(lifetime ~ temp + material, data = battery)
summary(anova1)
```

                Df Sum Sq Mean Sq F value   Pr(>F)
    temp         2  39119   19559  21.776 1.24e-06 ***
    material     2  10684    5342   5.947  0.00651 **
    Residuals   31  27845     898
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

## Battery Lifetimes (Real Data)

<figure>

</figure>

## Interaction Plot 1

## Interaction Plot 2

## Interaction Plots

- Each plot displays the group averages as a function of one factor.
- If there are no interactions, the lines should be *parallel*.

## 2. Two-way ANOVA with Interactions

<span class="math display">\\$$ y\_{ijk} = \\mu + \\alpha\_i + \\beta\_j + \\gamma\_{ij} + \\epsilon\_{ijk} \\$$</span>

## 2. Two-way ANOVA with Interactions

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova2 <- aov(lifetime ~ temp + material + temp:material, data = battery)
summary(anova2)
```

                  Df Sum Sq Mean Sq F value   Pr(>F)
    temp           2  39119   19559  28.968 1.91e-07 ***
    material       2  10684    5342   7.911  0.00198 **
    temp:material  4   9614    2403   3.560  0.01861 *
    Residuals     27  18231     675
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

## Randomization F tests

Algorithm to generate null distribution

1.  Shuffle the response
2.  Calculate F-statistics
3.  Rise and repeat

Then compare null distribution to observed statistics.

## Observed statistics

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
battery_anova <- aov(lifetime ~ temp * material, data = battery)
anova_table <- summary(battery_anova)
f_temp_obs <- anova_table[[1]]$`F value`[1]
f_material_obs <- anova_table[[1]]$`F value`[2]
f_interaction_obs <- anova_table[[1]]$`F value`[3]
f_temp_obs
```

    [1] 28.96769

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
f_material_obs
```

    [1] 7.911372

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
f_interaction_obs
```

    [1] 3.559535

## Simulated data frame

First shuffle:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
battery_sim1 <- battery
battery_sim1$lifetime <- sample(battery_sim1$lifetime)
battery_sim1
```

       id material temp lifetime
    1   1        1   15      122
    2   2        1   15      136
    3   3        1   70       25
    4   4        1   70      150
    5   5        1  125      155
    6   6        1  125       20
    7   7        1   15      130
    8   8        1   15      150
    9   9        1   70      139
    10 10        1   70       58
    11 11        1  125       70
    12 12        1  125       75
    13 13        2   15       34
    14 14        2   15       60
    15 15        2   70       45
    16 16        2   70      106
    17 17        2  125      160
    18 18        2  125      104
    19 19        2   15       82
    20 20        2   15       96
    21 21        2   70      168
    22 22        2   70      110
    23 23        2  125      126
    24 24        2  125       58
    25 25        3   15      188
    26 26        3   15      120
    27 27        3   70       82
    28 28        3   70      115
    29 29        3  125      174
    30 30        3  125       80
    31 31        3   15       70
    32 32        3   15       74
    33 33        3   70      159
    34 34        3   70      138
    35 35        3  125      180
    36 36        3  125       40

## Simulated data frame

Second shuffle:

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
battery_sim2 <- battery
battery_sim2$lifetime <- sample(battery_sim2$lifetime)
battery_sim2
```

       id material temp lifetime
    1   1        1   15       60
    2   2        1   15       74
    3   3        1   70       70
    4   4        1   70       75
    5   5        1  125      120
    6   6        1  125      115
    7   7        1   15       58
    8   8        1   15      180
    9   9        1   70      136
    10 10        1   70       82
    11 11        1  125      159
    12 12        1  125       20
    13 13        2   15      174
    14 14        2   15      110
    15 15        2   70      122
    16 16        2   70      104
    17 17        2  125      106
    18 18        2  125      160
    19 19        2   15       58
    20 20        2   15       96
    21 21        2   70       82
    22 22        2   70       80
    23 23        2  125       40
    24 24        2  125       34
    25 25        3   15      139
    26 26        3   15       25
    27 27        3   70      130
    28 28        3   70      155
    29 29        3  125      126
    30 30        3  125       45
    31 31        3   15       70
    32 32        3   15      150
    33 33        3   70      138
    34 34        3   70      150
    35 35        3  125      168
    36 36        3  125      188

## As a function

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

## Run Simulation 5 times

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(5, shuffle_two_factor(y = battery$lifetime,
                                              a = battery$temp,
                                              b = battery$material))
null_stats
```

             [,1]      [,2]      [,3]      [,4]      [,5]
    [1,] 1.057870 2.2623417 0.1545131 0.2875059 0.3891141
    [2,] 1.447381 0.6046787 0.2802976 1.2278416 2.6550284
    [3,] 1.107107 0.1233809 0.1720598 0.2389194 0.2353213
    [4,]       NA        NA        NA        NA        NA

## Run Simulation 500 times

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
null_stats <- replicate(500, shuffle_two_factor(y = battery$lifetime,
                                                a = battery$temp,
                                                b = battery$material))
f_temp_null <- null_stats[1, ]
f_material_null <- null_stats[2, ]
f_interaction_null <- null_stats[3, ]
```

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
data.frame(stats = f_temp_null) |>
  ggplot(aes(x = stats)) +
  geom_histogram() +
  theme_bw() +
  geom_vline(xintercept = f_temp_obs, color = "tomato") +
  labs(title = "Null for Temperature Factor")
```

<figure>

</figure>

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
data.frame(stats = f_material_null) |>
  ggplot(aes(x = stats)) +
  geom_histogram() +
  theme_bw() +
  geom_vline(xintercept = f_material_obs, color = "tomato") +
  labs(title = "Null for Material Factor")
```

<figure>

</figure>

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
data.frame(stats = f_interaction_null) |>
  ggplot(aes(x = stats)) +
  geom_histogram() +
  theme_bw() +
  geom_vline(xintercept = f_interaction_obs, color = "tomato") +
  labs(title = "Null for Interaction")
```

<figure>

</figure>

## Interaction p-values compared

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
data.frame(stats = f_interaction_null) |>
  summarize(pval = mean(f_interaction_null > f_interaction_obs))
```

       pval
    1 0.014

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
anova_table
```

                  Df Sum Sq Mean Sq F value   Pr(>F)
    temp           2  39119   19559  28.968 1.91e-07 ***
    material       2  10684    5342   7.911  0.00198 **
    temp:material  4   9614    2403   3.560  0.01861 *
    Residuals     27  18231     675
    ---
    Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

---

[← Main Effects and Interactions {#main-effects-and-interactions .title}](01-main-effects-and-interactions-main-effects-and-interactions.md) · [Up: contents](index.md)
