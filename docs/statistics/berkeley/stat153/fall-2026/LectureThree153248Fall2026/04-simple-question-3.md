---
title: Simple Question 3
source: https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex
source_file: sources/berkeley-stat153/fall-2026/LectureThree153248Fall2026.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Simple Question 3

**Source:** [`LectureThree153248Fall2026.tex`](https://github.com/berkeley-stat153/fall-2026/blob/1df2e362c312415dc83d910dc9e724e1646fafab/LectureThree153248Fall2026.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Now suppose we have three numbers $a, b_1, b_2$. Assume that both $b_1$ and $b_2$ are small in magnitude. Also suppose that $$\begin{align*}
  a+b_1 = 7 ~~ \text{ and } ~~ a+b_2 &= 10.
\end{align*}$$ What can then be said about $a$?

Note now that there are three unknown numbers and two pieces of information. So this problem is also logically unanswerable without further assumptions. We shall make probabilistic assumptions on the unknown $a, b_1, b_2$. Specifically, we assume that $$\begin{align}
\label{md3}
  a \sim \operatorname{Unif}(-C,C),  ~~~ \text{ and } ~~~  b_1,b_2\mid\sigma
  \overset{\mathrm{iid}}{\sim}N(0,\sigma^2) ~~~ \text{ and } ~~~
  \log\sigma \sim \operatorname{Unif}(-C,C)
\end{align}$$ where, as before, $C$ is a very large constant. The idea behind this modeling assumption is:

1.  We don’t want to assume anything specific about $a$

2.  Because $b_1, b_2$ are given to be small in magnitude, we assume a normal distribution centered at 0 for them with their magnitude controlled by a parameter $\sigma$. This also assumes they have the same scale.

3.  The common scale $\sigma$ of $b_1, b_2$ is also unknown. We don’t want to assume anything specific about this scale so we use the uniform $(-C, C)$ prior on $\log \sigma$. Because $\sigma$ is always positive, $\log \sigma$ makes sense and it takes values that can be both positive and negative, and this makes the $\text{Unif}(-C, C)$ prior reasonable for $\log \sigma$.

The assumption $\log \sigma \sim \text{unif}(-C, C)$ leads to the following density for $\sigma$ (by the change of variables formula): The last assumption says that we do not know the order of magnitude of $\sigma$. By a change of variables, it gives the density $$\begin{align*}
  f_\sigma(\sigma)
  = f_{\log\sigma}(\log\sigma)
  \left|\frac{d}{d\sigma}\log\sigma\right| = f_{\log \sigma}(\log
  \sigma) \frac{1}{\sigma} = \frac{I\{-C < \log \sigma < C\}}{2 C
  \sigma}.
\end{align*}$$ With these assumptions, we need to calculate the conditional distribution of: $$\begin{align*}
  a \mid a+ b_1 = 7, a + b_2 = 10.
\end{align*}$$ This determines our uncertainty about $a$ given the information $a +
b_1 = 7$ and $a + b_2 = 10$. To compute the above conditional, let us use the notation: $$\begin{align*}
  y_1 = a + b_1 ~~~ \text{ and } ~~~ y_2 = a + b_2,
\end{align*}$$ so that we need to calculate the density of: $$\begin{align}
\label{req_cond}
  a \mid y_1 = 7, y_2 = 10.
\end{align}$$ One complication in calculating this density is the variable $\sigma$ which is present in the modeling assumption but is not present in this conditional density. A simple way of dealing with this is to first compute the joint conditional density $$\begin{align}
\label{req_cond_sig}
  a, \sigma \mid y_1 = 7, y_2 = 10
\end{align}$$ and then to integrate over $\sigma$ to obtain the required conditional density <a href="#req_cond" data-reference-type="eqref" data-reference="req_cond">[req_cond]</a>. To calculate <a href="#req_cond_sig" data-reference-type="eqref" data-reference="req_cond_sig">[req_cond_sig]</a>, we use the Bayes rule in the following way: (note that $y_1, y_2 \mid a,
\sigma \sim N(a, \sigma^2)$) $$\begin{align*}
  f_{a, \sigma \mid y_1, y_2}(a, \sigma) &\propto
                                                         f_{y_1, y_2
                                                         \mid a,
                                                         \sigma}(y_1,  y_2)
                                                         f_{a,
                                                         \sigma}(a,
                                                         \sigma) \\
  &= \left\{\prod_{j=1}^2
  \frac{1}{\sqrt{2\pi}\sigma}
  \exp\left(-\frac{(y_j-a)^2}{2\sigma^2}\right)\right\} f_a(a)
    f_{\sigma}(\sigma) \\
  &= \left\{\prod_{j=1}^2
  \frac{1}{\sqrt{2\pi}\sigma}
  \exp\left(-\frac{(y_j-a)^2}{2\sigma^2}\right)\right\} \frac{I\{-C <
    a < C\}}{2 C} \frac{I\{-C < \log \sigma < C\}}{2 C \sigma} \\
  &\propto \sigma^{-3} \exp \left(-\frac{(y_1 - a)^2 + (y_2 - a)^2}{2
    \sigma^2} \right) I\{-C < a < C\} I\{e^{-C} < \sigma < e^C\}
\end{align*}$$ where, in the last step above, we ignored the terms involving $\sqrt{2\pi}$ and $C$ in the proportional constant. As $C$ is very large, we shall also ignore the first indicator function above because it will be 1 for all reasonable values of $a$, and replace the second indicator function by $I\{\sigma > 0\}$ because it will be 1 for all reasonable values of $\sigma > 0$. This gives $$\begin{align*}
  f_{a, \sigma \mid y_1, y_2}(a, \sigma) \propto \sigma^{-3} \exp \left(-\frac{(y_1 - a)^2 + (y_2 - a)^2}{2
    \sigma^2} \right) I\{\sigma > 0\}.
\end{align*}$$ This conditional density reflects our knowledge of both $a$ and $\sigma$ given the information on $y_1$ and $y_2$. Since the question only cares about $a$ (and not $\sigma$), we can obtain <a href="#req_cond" data-reference-type="eqref" data-reference="req_cond">[req_cond]</a> by integrating the above with respect to $\sigma$. This gives: $$\begin{align*}
  f_{a \mid y_1, y_2}(a) &= \int f_{a, \sigma \mid y_1, y_2}(a, \sigma)
                           d\sigma \propto \int_0^{\infty} \sigma^{-3} \exp \left(-\frac{(y_1 - a)^2 + (y_2 - a)^2}{2
                           \sigma^2} \right) d \sigma.
\end{align*}$$ Let $$\begin{align*}
  S(a) &= (y_1-a)^2+(y_2-a)^2,
\end{align*}$$ and we can call $S(a)$ the sum of squares function. Then $$\begin{align*}
  f_{a \mid y_1, y_2}(a) \propto \int_0^{\infty} \sigma^{-3} \exp \left(-\frac{S(a)}{2
                           \sigma^2} \right) d \sigma.
\end{align*}$$ We use the change of variable: $$\begin{align}
\label{cov}
  \sigma = t \sqrt{S(a)} ~~~ \text{ so that } ~~~ d \sigma =
  \sqrt{S(a)}~dt.
\end{align}$$ Then $$\begin{align*}
  f_{a \mid y_1, y_2}(a) &\propto \int_0^{\infty} \sigma^{-3} \exp \left(-\frac{S(a)}{2
                           \sigma^2} \right) d \sigma \\
  &= \int_0^{\infty} t^{-3} S(a)^{-3/2} \exp \left(-\frac{1}{2 t^2}
    \right) \sqrt{S(a)} dt \\
  &= \frac{1}{S(a)} \int_0^{\infty} t^{-3} \exp \left(-\frac{1}{2t^2}
    \right) dt \\
  &\propto \frac{1}{S(a)},
\end{align*}$$ where, in the last step, we ignored the integral term because it is a constant (i.e., does not depend on $a$). We therefore proved $$\begin{align*}
  f_{a\mid y_1,y_2}(a) \propto \frac{1}{(y_1-a)^2+(y_2-a)^2}.
\end{align*}$$ It turns out that this is a Cauchy density. To see this, first complete the square and rewrite $S(a)$ as: $$\begin{align*}
  (y_1-a)^2+(y_2-a)^2
  =2\left(a-\frac{y_1+y_2}{2}\right)^2
    +\frac{(y_1-y_2)^2}{2} =2\left\{
    \left(a-\frac{y_1+y_2}{2}\right)^2
    +\left(\frac{|y_1-y_2|}{2}\right)^2
    \right\}
\end{align*}$$ so that $$\begin{align}
\label{tcau_1}
  f_{a \mid y_1, y_2}(a) \propto \frac{1}{    \left(a-\frac{y_1+y_2}{2}\right)^2
    +\left(\frac{|y_1-y_2|}{2}\right)^2}.
\end{align}$$ The density of a Cauchy random variable with location $\mu$ and scale $\tau$ is $$\begin{align}
 \label{tcau_2}
 \text{Density of Cauchy}(\mu, \tau) = \frac{1}{\pi\tau} \frac{1}{1+\left((x-\mu)/\tau\right)^2}
  \propto \frac{1}{\tau^2+(x-\mu)^2}.
\end{align}$$ Comparing <a href="#tcau_1" data-reference-type="eqref" data-reference="tcau_1">[tcau_1]</a> and <a href="#tcau_2" data-reference-type="eqref" data-reference="tcau_2">[tcau_2]</a>, we get $$\begin{align*}
  a\mid y_1,y_2
  \sim \operatorname{Cauchy}\left(
  \frac{y_1+y_2}{2},\frac{|y_1-y_2|}{2}\right).
\end{align*}$$ For $y_1=7$ and $y_2=10$, this becomes $$\begin{align*}
  a\mid y_1=7,y_2=10
  &\sim \operatorname{Cauchy}(8.5,1.5).
\end{align*}$$ It is quite remarkable that we obtain a Cauchy density to capture the uncertainty about $a$ given the observations. This is basically a consequence of the modeling assumptions <a href="#md3" data-reference-type="eqref" data-reference="md3">[md3]</a>.

---

[← Simple Question 2](03-simple-question-2.md) · [Up: contents](index.md) · [Question 4: Several Measurements of One Quantity →](05-question-4-several-measurements-of-one-quantity.md)
