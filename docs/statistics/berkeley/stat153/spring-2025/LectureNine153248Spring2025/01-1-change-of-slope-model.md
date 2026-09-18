---
title: 1 Change of Slope Model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureNine153248Spring2025.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`LectureNine153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureNine153248Spring2025.pdf) — berkeley-stat153 · spring-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 1 Change of Slope Model

### Lecture Nine
Spring 2025, UC Berkeley

Aditya Guntuboyina

February 18, 2025

While our focus, in the last few lectures, has been on sinusoidal models, the methodology can be applied in the same way to some other nonlinear regression models. As an illustrative example, we study the change of slope model today. Other examples can be found in Homework Two. The change of slope model is given by:
$$y_t = \beta_0 + \beta_1 t + \beta_2 \text{ReLU}(t - c) + \epsilon_t \tag{1}$$
with $\epsilon_t \overset{\text{i.i.d}}{\sim} N(0, \sigma^2)$. Here $\text{ReLU}(t - c) = (t - c)_+$ equals $0$ if $t \le c$ and equals $t - c$ if $t \ge c$. We can also write
$$\text{ReLU}(t - c) = (t - c)_+ = (t - c)I\{t > c\} = \max(t - c, 0).$$
$(\cdot)_+$ is also called the positive part function, or, the ramp function.

The model (1) says that for times $t \le c$, the slope of the regression line is $\beta_1$, while for $t > c$, the slope changes to $(\beta_1 + \beta_2)$. An alternative name for this model is "Broken-stick regression". This is because the function
$$t \mapsto \beta_0 + \beta_1 t + \beta_2 \text{ReLU}(t - c)$$
resembles a broken stick.

The unknown parameters for this model are $c, \beta_0, \beta_1, \beta_2$ as well as $\sigma$. The unknown parameter $c$ makes (1) a nonlinear regression model. If $c$ were known, then (1) would be a linear regression model:
$$y = X_c \beta + \epsilon \tag{2}$$
with
$$X_c = \begin{pmatrix}
1 & 1 & \text{ReLU}(1 - c) \\
1 & 2 & \text{ReLU}(2 - c) \\
1 & 3 & \text{ReLU}(3 - c) \\
\cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot \\
1 & n & \text{ReLU}(n - c)
\end{pmatrix}$$

## 2 Estimation of $c, \beta_0, \beta_1, \beta_2, \sigma$

Parameter estimation can be done via Maximum Likelihood Estimation. Just as in the case of the sinusoidal model, a crucial role is played by the residual sum of squares in the linear regression model (2):
$$RSS(c) = \min_{\beta_0, \beta_1, \beta_2} \sum_{t=1}^n (y_t - \beta_0 - \beta_1 t - \beta_2 \text{ReLU}(t - c))^2.$$
The MLE of $c$ is given by the minimizer of $RSS(c)$ over $c$. On the computer, we calculate this by enumerating all the possible values of $c$ (these are just $1, 2, \dots, n$) and then using a function such as `np.argmin`.

After the MLE $\hat{c}$ of $c$ is obtained, $\beta_0, \beta_1, \beta_2$ are estimated as in linear regression (e.g., using `sm.OLS`). Specifically,
$$\hat{\beta} = (\hat{\beta}_0, \hat{\beta}_1, \hat{\beta}_2)^T = (X_{\hat{c}}^T X_{\hat{c}})^{-1} X_{\hat{c}}^T y. \tag{3}$$
Then $\sigma$ is estimated as in linear regression:
$$\hat{\sigma} = \sqrt{\frac{RSS(\hat{c})}{n - 3}}.$$

---

[Up: contents](index.md) · [3 Uncertainty Quantification for $c, \beta0, \beta1, \beta2, \sigma$ →](02-3-uncertainty-quantification-for.md)
