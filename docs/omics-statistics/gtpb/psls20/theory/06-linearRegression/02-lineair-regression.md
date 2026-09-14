---
title: Lineair Regression
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd
source_file: sources/gtpb-psls20/theory/06-linearRegression.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Lineair Regression

**Source:** [`theory/06-linearRegression.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/06-linearRegression.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Statistical method to assess association between two variables $(X_i, Y_i)$, measured on each subject $i = 1, ..., n$.

- Gene expression example

    - Response Y : S100A8 expression
    - Predictor X: ESR1 expression

```r
brcaSubset %>%
  ggplot(aes(x=ESR1,y=S100A8)) +
  geom_point() +
  geom_smooth(se=FALSE,col="grey") +
  geom_smooth(method="lm",se=FALSE)
```

## Model

- For fixed $X$, $Y$ does not necessarly has the same value

$$\text{observation = signal + noise}$$

$$Y_i=g(X_i)+\epsilon_i$$
- We define $g(x)$ als the expected outcome for subjects with $X_i=x$

$$E[Y_i|X_i=x]=g(x)$$

Hence, $\epsilon_i$ is on average 0 for subjects with same  $X_i$:
$$E[\epsilon_i|X_i]=0$$

## Lineair regression

- To obtain *accurate* and *interpretable* results one often choose $g(x)$ to be a linear function with unknown parameter.

$$E(Y|X=x)=\beta_0 + \beta_1 x$$

unknown \alert{intercept} $\beta_0$ and
\alert{slope} $\beta_1$.

- Lineair model imposes an *assumption* on the distribution of $X$ and $Y$, which can be invalid.

- *Efficient data-analysis*: because it uses all observations to learn on the expected outcome for $X=x$.


## Use

- *Prediction*: when $Y$ is unknown but $X$ is known we can predict $Y$ using
$$E(Y|X=x)=\beta_0 + \beta_1 x$$

- *Association*: biological relation between variable $X$ and response $Y$
- *Intercept:* $E(Y|X=0)=\beta_0$
\vspace{10pt}
- *Slope*:
\begin{eqnarray*}
E(Y|X=x+\delta)-E(Y|X=x)&=&\beta_0 + \beta_1 (x+\delta) -\beta_0-\beta_1 x\\
&=& \beta_1\delta
\end{eqnarray*}

$\beta_1=$ difference in mean outcome for subjects that differ in one unit of the predictor  $X$.

---

[← Breast cancer dataset](01-breast-cancer-dataset.md) · [Up: contents](index.md) · [Parameter estimation →](03-parameter-estimation.md)
