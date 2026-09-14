---
title: Collinearity
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/36-adjustments/slides.html
source_file: sources/berkeley-stat158/spring-2026/36-adjustments/slides.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Collinearity

**Source:** [`36-adjustments/slides.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/36-adjustments/slides.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

##

Simulated data with two explanatory variables.

    # A tibble: 100 × 3
            y      x1      x2
        <dbl>   <dbl>   <dbl>
     1  3.58  -0.349  -0.708
     2  2.03  -0.756   1.12
     3  8.59  -1.04   -1.07
     4 -7.73   1.21    1.41
     5 -2.51   1.24   -1.90
     6 -7.48   1.74   -0.983
     7  0.319  0.0977 -0.179
     8 17.2   -2.52   -1.93
     9  4.07  -0.789   0.467
    10 -3.49   0.576  -0.0249
    # ℹ 90 more rows

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
pairs(weak_collinearity)
```

<figure>

</figure>

##

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
cor(weak_collinearity)
```

                y         x1         x2
    y   1.0000000 -0.9119516 -0.3798014
    x1 -0.9119516  1.0000000  0.0144365
    x2 -0.3798014  0.0144365  1.0000000

**Collinearity**: describes the presence of linear relationships between the *explanatory* variables.

## Results from Linear Models

<span class="math display">\\$$ \\hat{\\boldsymbol{\\beta}} = (\\mathbf{X}^\\top \\mathbf{X})^{-1} \\mathbf{X}^\\top \\mathbf{y} \\$$</span>

<span class="math display">\\$$ Var(\\hat{\\boldsymbol{\\beta}}) = \\sigma^2 (\\mathbf{X}^\\top \\mathbf{X})^{-1} \\$$</span>

<span class="math display">\\$$ Var(\\hat{\\beta}\_j) = \\frac{\\sigma^2}{(n-1) Var(X\_j)} \\cdot \\frac{1}{1 - R^2\_j} \\$$</span>

where <span class="math inline">\$R^2\_j\$</span> is the <span class="math inline">\$R^2\$</span> from regressing <span class="math inline">\$X\_j\$</span> on other <span class="math inline">\$X\$</span>. The second term is called the **Variance Inflation Factor** (VIF).

## Weak Collinearity

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
m1 <- lm(y ~ x1 + x2, data = weak_collinearity)
summary(m1)$coef
```

                   Estimate Std. Error     t value     Pr(>|t|)
    (Intercept)  0.05407907 0.09898302   0.5463469 5.860820e-01
    x1          -5.04493666 0.10402428 -48.4976860 8.096236e-70
    x2          -1.95018390 0.09941965 -19.6156791 1.569072e-35

This linear model corresponds to a plane in 3D.

##

## Strong Collinearity

    # A tibble: 100 × 3
            y     x1      x2
        <dbl>  <dbl>   <dbl>
     1  5.93  -0.766 -0.806
     2  0.846 -0.200  0.0721
     3  2.33  -0.393 -0.427
     4  8.43  -1.31  -1.24
     5  1.23  -0.204 -0.133
     6 -5.82   0.687  0.767
     7 -2.19   0.350  0.120
     8  3.68  -0.339 -0.255
     9 -1.48   0.297 -0.0168
    10 -5.03   0.722  0.616
    # ℹ 90 more rows

## Strong Collinearity

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
pairs(strong_collinearity)
```

<figure>

</figure>

## Strong collinearity

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
cor(strong_collinearity)
```

                y         x1         x2
    y   1.0000000 -0.9875549 -0.9791803
    x1 -0.9875549  1.0000000  0.9841485
    x2 -0.9791803  0.9841485  1.0000000

High **collinearity** leads to high **VIF**.

##

## Designed Experiment

    # A tibble: 100 × 3
             y    x1    x2
         <dbl> <dbl> <dbl>
     1  20.6      -3    -3
     2  12.0      -1    -3
     3   6.52      0    -3
     4   1.19      1    -3
     5  -9.76      3    -3
     6  18.9      -3    -1
     7   6.23     -1    -1
     8   0.981     0    -1
     9  -3.15      1    -1
    10 -12.3       3    -1
    # ℹ 90 more rows

## Designed Experiment

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
pairs(designed_exp)
```

<figure>

</figure>

## Design Experiment

``` {.sourceCode .numberSource .r .number-lines .code-with-copy}
cor(designed_exp)
```

                y         x1        x2
    y   1.0000000 -0.9256147 -0.369353
    x1 -0.9256147  1.0000000  0.000000
    x2 -0.3693530  0.0000000  1.000000

No collinearity leads to . . .

##

---

[← Regression Adjustments](03-regression-adjustments.md) · [Up: contents](index.md)
