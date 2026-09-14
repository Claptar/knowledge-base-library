---
title: Additive multiple linair model
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd
source_file: sources/gtpb-psls20/theory/08-MultipleRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Additive multiple linair model

**Source:** [`theory/08-MultipleRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/08-MultipleRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Separate simple linair models, like

$$E(Y|X_v)=\alpha+\beta_v X_v$$

- Association between lpsa en 1 variabele e.g lcavol.
- More accurate predictions by simultaneously accounting for multiple predictors
- Estimate for parameter $\beta_v$ does not only capture the effect of tumor volume.
- $\beta_v$ average difference for log-psa for patients that differ in 1 unit of the log tumor volume.
- Even if lcavol is not associated with lpsa then patients with a higher tumor volume can have a higher lpsa because their semen vesicles are affected (svi status 1).
$\rightarrow$ confounding.
- Compare patients with same svi status
- Is posible in multiple linear model

---

## Statistical model

- $p-1$ predictors $X_1,...,X_{p-1}$ and outcome $Y$ for $n$ subjecten.

\begin{equation}
Y_i =\beta_0 + \beta_1 X_{i1} + ... +\beta_{p-1} X_{ip-1} + \epsilon_i
\end{equation}

- $\beta_0,\beta_1,...,\beta_{p-1}$ unknown parameters
- $\epsilon_i$ residuals that cannot be explained by predictors
- Estimation by *least squares method*

---

Model allows to

1. predict the expected outcome for subjects given their values $x_1,...,x_{p-1}$ for the predictor variables.
$E[Y\vert X_1=x_1, \ldots X_{p-1}=x_{p-1}]=\hat{\beta}_0+\hat{\beta}_1x_1+...+\hat{\beta}_{p-1}x_{p-1}$.
2. Does the average outcome differ between two groups of patients that differ by $\delta$ units in predictor $X_j$ but have the same value for the remaining variables $\{X_k,k=1,...,p,k\ne j\}$.
$$
\begin{array}{l}
E(Y|X_1=x_1,...,X_j=x_j+\delta,...,X_{p-1}=x_{p-1}) \\
\quad\quad - E(Y|X_1=x_1,...,X_j=x_j,...,X_{p-1}=x_{p-1}) \\\\
\quad =\beta_0 + \beta_1 x_1 + ... + \beta_j(x_j+\delta)+...+\beta_{p-1} x_{p-1}\\
\quad\quad- \beta_0 - \beta_1 x_1 - ... - \beta_jx_j-...-\beta_{p-1} x_{p-1} \\\\
\quad= \beta_j\delta
\end{array}
$$

Interpretation $\beta_j$:

- difference in mean outcome between subjects that differ in one unit of $X_j$, but have the same value for the remaining predictors in the model.

or

- Effect of predictor j corrected for the remaining predictors.  e.g. effect of cancer volume correct for prostate weight and the svi status.

---

### Prostate example

```r
lmV <- lm(lpsa~lcavol,prostate)
summary(lmV)
```

---

```r
lmVWS <- lm(lpsa~lcavol + lweight + svi ,prostate)
summary(lmVWS)
```

---

```r
library(plot3D)
grid.lines = 10
x<-prostate$lcavol
y<-prostate$lweight
z<-prostate$lpsa
fit<-lm(z~x+y+svi,data=prostate)
x.pred <- seq(min(x), max(x), length.out = grid.lines)
y.pred <- seq(min(y), max(y), length.out = grid.lines)

---

[← Intro](01-intro.md) · [Up: contents](index.md) · [fitted points for droplines to surface →](03-fitted-points-for-droplines-to-surface.md)
