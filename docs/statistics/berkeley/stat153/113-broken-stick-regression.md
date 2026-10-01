---
title: "113. Broken-Stick Regression"
course: "Berkeley Stat 153"
chapter: 113
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 113. Broken-Stick Regression

## What this covers

This chapter introduces nonlinear regression through a single worked example: the
**change-of-slope** (or "broken-stick") model, in which a regression line is allowed to bend at an
unknown time $c$. It assumes familiarity with ordinary linear regression and the least-squares
estimator $\hat\beta = (X^TX)^{-1}X^Ty$, and asks what happens to that machinery once one of the
model's own inputs — here, the *location* of the break — is itself an unknown parameter.

## Linear versus nonlinear regression

A regression model is **linear** when the mean response is a linear function of the unknown
parameters — this is compatible with nonlinear functions of the predictors, such as $t$, $t^2$,
$\log t$, and so on, since those are just new columns of the design matrix. A model is
**nonlinear** when at least one parameter enters in a way that cannot be absorbed into a fixed
column: it changes *which function of the predictors* is being used, not just the coefficient in
front of it.

## The change-of-slope ("broken-stick") model

The example is

$$y_t = \beta_0 + \beta_1 t + \beta_2\,\mathrm{ReLU}(t-c) + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d.}}{\sim} N(0,\sigma^2), \tag{1}$$

where $\mathrm{ReLU}(t-c) = (t-c)_+$ is the **positive-part** (or **ramp**) function:

$$\mathrm{ReLU}(t-c) = (t-c)_+ = (t-c)\,I\{t>c\} = \max(t-c,\,0),$$

equal to $0$ for $t \le c$ and equal to $t-c$ for $t > c$.

Reading off the slope of (1) on either side of $c$: for $t \le c$ the ramp term vanishes and the
slope is $\beta_1$; for $t > c$ the slope becomes $\beta_1 + \beta_2$. So $\beta_2$ is exactly the
*change* in slope that occurs at $c$. This is why (1) is called the change-of-slope model, and why
it is also known as **broken-stick regression**: the graph of

$$t \mapsto \beta_0 + \beta_1 t + \beta_2\,\mathrm{ReLU}(t-c)$$

is two straight rays joined at $t=c$, resembling a stick bent at that point.

<figure>
<svg viewBox="0 0 320 180" role="img" aria-label="A broken-stick regression line: a straight segment with slope beta_1 for t less than c, joined at the kink to a segment with slope beta_1 plus beta_2 for t greater than c">
  <line x1="20" y1="160" x2="300" y2="160" stroke="currentColor" stroke-width="1"/>
  <text x="300" y="175" text-anchor="end" font-size="12" fill="currentColor">t</text>
  <line x1="40" y1="130" x2="170" y2="70" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="70" x2="280" y2="30" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="160" x2="170" y2="70" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3"/>
  <text x="170" y="172" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="90" y="115" font-size="12" fill="currentColor">slope &#946;&#8321;</text>
  <text x="215" y="42" font-size="12" fill="currentColor">slope &#946;&#8321;+&#946;&#8322;</text>
</svg>
<figcaption>The broken-stick model: a straight line of slope $\beta_1$ up to the break point $c$,
continuing as a straight line of slope $\beta_1+\beta_2$ afterward.</figcaption>
</figure>

The unknown parameters are $c, \beta_0, \beta_1, \beta_2$, and $\sigma$. It is $c$ that makes (1) a
*nonlinear* regression model: it sits inside the ramp function rather than multiplying a fixed
predictor, so the mean response is not a linear function of $c$.

### What linearity looks like once $c$ is known

If $c$ were known, the nonlinearity disappears: $\mathrm{ReLU}(t-c)$ becomes just another column
one can compute for each $t$, and (1) is an ordinary linear regression model,

$$y = X_c\beta + \epsilon, \tag{2}$$

with

$$X_c = \begin{pmatrix} 1 & 1 & \mathrm{ReLU}(1-c) \\ 1 & 2 & \mathrm{ReLU}(2-c) \\ 1 & 3 & \mathrm{ReLU}(3-c) \\ \vdots & \vdots & \vdots \\ 1 & n & \mathrm{ReLU}(n-c) \end{pmatrix}, \qquad \beta := \begin{pmatrix}\beta_0\\\beta_1\\\beta_2\end{pmatrix}, \qquad \epsilon = \begin{pmatrix}\epsilon_1\\\epsilon_2\\\vdots\\\epsilon_n\end{pmatrix}.$$

This is the key move for handling the model: freezing $c$ turns a nonlinear problem into a linear
one, and the difficulty of the nonlinear model is entirely about the one parameter $c$ that stands
outside this reduction.

## Parameter estimation by least squares

As with linear regression, the basic estimation procedure is least squares. The sum of squares to
minimize is

$$S(\beta_0,\beta_1,\beta_2,c) := \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1 t - \beta_2\,\mathrm{ReLU}(t-c)\big)^2, \tag{3}$$

which in matrix notation, using $X_c$ from (2), is

$$S(\beta,c) = \|y - X_c\beta\|^2.$$

Now (3) must be minimized jointly over all four unknowns $\beta_0,\beta_1,\beta_2,c$ — but the
reduction above shows that the four-dimensional problem is not as hard as it looks. **Fix $c$.**
With $c$ held fixed, minimizing $S(\beta,c)$ over $\beta$ alone is exactly the ordinary linear
regression problem for the design matrix $X_c$, whose solution is the usual least-squares formula:

$$\hat\beta(c) := (X_c^TX_c)^{-1}X_c^Ty. \tag{4}$$

So for every candidate value of $c$, (4) hands back the best-fitting slope-and-intercept
coefficients. This is as far as the supplied material goes — it sets up but does not carry out the
remaining step of choosing $c$ itself (for instance by substituting $\hat\beta(c)$ back into (3) and
minimizing what remains over $c$ alone).

## Sources

- Notes: `LectureSix153248Fall2025.md` (STAT 153 & 248, UC Berkeley, Fall 2025, Aditya Guntuboyina,
  Lecture Six, September 16 2025), Section 1 "Nonlinear Regression" and Section 1.1 "Parameter
  Estimation" — the model (1), the ReLU/ramp function, the broken-stick interpretation, the design
  matrix $X_c$ in (2), the least-squares objective (3), and the fixed-$c$ estimator (4).
- The supplied file is a model reconstruction of a PDF with no text layer and is itself incomplete:
  it opens mid-topic ("We started discussing nonlinear regression models near the end of last
  lecture"), so what preceded model (1) in the previous lecture is not available here, and it
  breaks off mid-formula right after equation (4), before the lecture's treatment of how $c$ itself
  is estimated (and before any material on $\sigma$). Nothing beyond what is written above was in
  the source.

---

[← 112. Parameter Estimation in AR(1)](112-parameter-estimation-in-ar-1.md) · [Contents](index.md) · [114. AR Models and Sunspots →](114-ar-models-and-sunspots.md)
