---
title: Simple Question 2 {#simple-question-2}
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex
source_file: sources/berkeley-stat153/fall-2026/LectureThree153248Fall2026.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Simple Question 2 {#simple-question-2}

**Source:** [`LectureThree153248Fall2026.tex`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Suppose $a$ and $b$ are two numbers such that $a + b = 7$. Suppose $b$ is small in magnitude. What then can be said about $a$?

Here is a way of arriving at a reasonable solution to this problem using probability theory. Assume that $a$ and $b$ are independent with $$\begin{align}
\label{md2}
  a \sim \operatorname{Unif}(-C,C) ~~ \text{ and } ~~
  b \sim N(0,\sigma^2)
\end{align}$$ where $C$ is very large, and $\sigma$ is a fixed quantity that characterizes smallness of $b$. Depending on what we understand by smallness of $b$, we can set a value of $\sigma$ (e.g., $\sigma =
0.5$).

Using the *modeling* assumption <a href="#md2" data-reference-type="eqref" data-reference="md2">[md2]</a> and the available *data* that $a + b = 7$, our uncertainty in $a$ will be captured by the probability distribution: $$\begin{align*}
  a \mid a + b = 7.
\end{align*}$$ Here is a simple way of calculating this conditional distribution. Let $y = a + b$ so that we need to calculate the conditional density of $a
\mid y = 7$. The conditional distribution of $y \mid a$ is given by $N(a, \sigma^2)$ because $y = a + b$, and $b$ is distributed as $N(0,
\sigma^2)$ independently of $a$. Therefore by Bayes rule: $$\begin{align*}
  f_{a \mid y = 7}(a) &\propto f_{y \mid a}(7) f_{a}(a) \\
  &= \frac{1}{\sigma \sqrt{2 \pi}} \exp \left(-\frac{(7 - a)^2}{2
    \sigma^2} \right) \times \frac{I\{-C < a < C\}}{2C} \\
  &\propto \exp \left(-\frac{(7 - a)^2}{2
    \sigma^2} \right) I\{-C < a < C\}.
\end{align*}$$ This is the normal distribution $N(7, \sigma^2)$ truncated to the interval $(-C, C)$. Because we shall take $C$ to be very large, the restriction to $(-C, C)$ has almost no effect and therefore, $$\begin{align*}
  a\mid a+b=7 &\approx N(7,\sigma^2).
\end{align*}$$ Thus under our probabilistic assumptions and the given information, our uncertainty about $a$ is captured by the normal distribution centered at 7 and variance $\sigma^2$. The amount of uncertainty is controlled by $\sigma^2$.

---

[← Simple Question 1 {#simple-question-1}](02-simple-question-1-simple-question-1.md) · [Up: contents](index.md) · [Simple Question 3 {#simple-question-3} →](04-simple-question-3-simple-question-3.md)
