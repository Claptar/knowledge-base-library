---
title: 'Question 4: Several Measurements of One Quantity'
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex
source_file: sources/berkeley-stat153/fall-2026/LectureThree153248Fall2026.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Question 4: Several Measurements of One Quantity

**Source:** [`LectureThree153248Fall2026.tex`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Suppose a scientist makes $n=6$ measurements of an unknown physical quantity $\theta$ and obtains $$\begin{align*}
  y_1=26.6, ~~ y_2=38.5, ~~ y_3 = 34.4, ~~ y_4 = 34.0, ~~ y_5 = 31.0,
  ~~
  y_6
  =
  23.6.
\end{align*}$$ Based on these observations, what can be inferred about $\theta$?

We consider each observation $y_i$ as comprised of $\theta$ and an ’error’ or ’noise’ term $\epsilon_i$: $$\begin{align*}
  y_i = \theta + \epsilon_i \qquad\text{for $i = 1, \dots, n$}.
\end{align*}$$ This means that we are trying to write the $n$ observations $y_1,
\dots, y_n$ in terms of $n+1$ unknowns $\theta$ and $\epsilon_1,
\dots, \epsilon_n$. On these $n+1$ unknowns, we make the following modeling assumptions: $$\begin{align*}
  \theta \sim \operatorname{Unif}(-C,C) ~~ \text{ and } ~~
  \epsilon_1,\ldots,\epsilon_n\mid\sigma
  \overset{\mathrm{iid}}{\sim}N(0,\sigma^2) ~~ \text{ and } ~~
  \log\sigma \sim \operatorname{Unif}(-C,C).
\end{align*}$$ This assumption is the same as that used in the previous section, the only difference is that $n$ is now 6 as opposed to 2, and also we are using different notation ($\theta$ in place of $a$, and $\epsilon_1,
\dots, \epsilon_n$ in place of $b_1, b_2$).

Our goal is to find the conditional density of $\theta$ given $y_1,
\dots, y_n$. As in question 3, we first find the joint conditional density of $(\theta, \sigma)$ given $y_1, \dots, y_n$, and then we integrate out $\sigma$ to calculate $\theta \mid y_1, \dots, y_n$. By Bayes rule, $$\begin{align*}
  f_{\theta, \sigma \mid y_1, \dots, y_n}(\theta, \sigma) &\propto
                                                         f_{y_1,
                                                            \dots, y_n
                                                         \mid \theta,
                                                         \sigma}(y_1,
                                                            \dots,  y_n)
                                                         f_{\theta,
                                                         \sigma}(\theta,
                                                         \sigma) \\
  &= \left\{\prod_{j=1}^n
  \frac{1}{\sqrt{2\pi}\sigma}
  \exp\left(-\frac{(y_j-\theta)^2}{2\sigma^2}\right)\right\} f_{\theta}(\theta)
    f_{\sigma}(\sigma) \\
  &= \left\{\prod_{j=1}^n
  \frac{1}{\sqrt{2\pi}\sigma}
  \exp\left(-\frac{(y_j-\theta)^2}{2\sigma^2}\right)\right\} \frac{I\{-C <
    \theta < C\}}{2 C} \frac{I\{-C < \log \sigma < C\}}{2 C \sigma} \\
  &\propto \sigma^{-n-1} \exp \left(-\frac{(y_1 - \theta)^2 + \dots +
    (y_n - \theta)^2}{2
    \sigma^2} \right) I\{-C < \theta < C\} I\{e^{-C} < \sigma <
    e^C\}.
\end{align*}$$ Ignoring the indicators, we get $$\begin{align*}
  f_{\theta, \sigma \mid y_1, \dots, y_n}(\theta, \sigma) \propto
  \sigma^{-n-1} \exp \left(-\frac{(y_1 - \theta)^2 + \dots + (y_n -
  \theta)^2}{2  \sigma^2} \right) I\{\sigma > 0\}.
\end{align*}$$ Integrating the above with respect to $\sigma$, we get $$\begin{align*}
  f_{\theta \mid y_1, \dots, y_n}(\theta) &= \int f_{\theta, \sigma \mid
                                            y_1, \dots, y_n}(\theta, \sigma)
                           d\sigma \propto \int_0^{\infty}
                                            \sigma^{-n-1} \exp
                                            \left(-\frac{(y_1 - \theta)^2 +
                                            \dots +
                                            (y_n - \theta)^2}{2
                           \sigma^2} \right) d \sigma.
\end{align*}$$ Let $$\begin{align*}
  S(\theta) &= (y_1-\theta)^2+ \dots +(y_n-\theta)^2
\end{align*}$$ be the sum of squares function. Then $$\begin{align*}
  f_{\theta \mid y_1, \dots, y_n}(\theta) \propto \int_0^{\infty}
  \sigma^{-n-1} \exp \left(-\frac{S(\theta)}{2
                           \sigma^2} \right) d \sigma.
\end{align*}$$ Using the same change of variable as in <a href="#cov" data-reference-type="eqref" data-reference="cov">[cov]</a>, we deduce $$\begin{align}
\label{tt_1}
  f_{\theta \mid y_1, \dots, y_n}(\theta) \propto \left(
  \frac{1}{S(\theta)} \right)^{n/2}.
\end{align}$$ We will see next week that this is a $t$-density with $n-1$ degrees of freedom. Note that the value of $\theta$ that minimizes $S(\theta)$ is the sample mean: $$\begin{align*}
  \bar{y} = \frac{y_1 + \dots + y_n}{n}.
\end{align*}$$ Because $1/S(\theta)$ appears in <a href="#tt_1" data-reference-type="eqref" data-reference="tt_1">[tt_1]</a>, it means that the conditional density of $\theta$ given $y_1, \dots, y_n$ is maximized at the sample mean.

---

[← Simple Question 3](04-simple-question-3.md) · [Up: contents](index.md) · [Linear Regression with Time as a Covariate →](06-linear-regression-with-time-as-a-covariate.md)
