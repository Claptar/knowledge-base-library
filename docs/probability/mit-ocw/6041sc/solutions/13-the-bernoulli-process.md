---
title: "Solutions — The Bernoulli Process"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — The Bernoulli Process

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 13 Solutions
**October 21, 2010**

1. (a) We begin by writing the definition for $\mathbf{E}[Z \mid X, Y]$
$$ \mathbf{E}[Z \mid X = x, Y = y] = \sum_z z p_{Z \mid X, Y}(z \mid x, y) $$
Since $\mathbf{E}[Z \mid X, Y]$ is a function of the random variables $X$ and $Y$, and is equal to $\mathbf{E}[Z \mid X = x, Y = y]$ whenever $X = x$ and $Y = y$, which happens with probability $p_{X, Y}(x, y)$, using the expected value rule, we have
$$ \begin{aligned} \mathbf{E}[\mathbf{E}[Z \mid X, Y]] &= \sum_x \sum_y \mathbf{E}[Z \mid X = x, Y = y] p_{X, Y}(x, y) \\ &= \sum_x \sum_y \sum_z z p_{Z \mid X, Y}(z \mid x, y) p_{X, Y}(x, y) \\ &= \sum_x \sum_y \sum_z z p_{X, Y, Z}(x, y, z) \\ &= \mathbf{E}[Z] \end{aligned} $$

(b) We start with the definition for $\mathbf{E}[Z \mid X, Y]$ which is a function of the random variables $X$ and $Y$, and is equal to $\mathbf{E}[Z \mid X = x, Y = y]$ whenever $X = x$ and $Y = y$, so
$$ \mathbf{E}[Z \mid X = x, Y = y] = \sum_z z p_{Z \mid X, Y}(z \mid x, y) $$
Proceeding as above, but conditioning on the event $X = x$, we have
$$ \begin{aligned} \mathbf{E}[\mathbf{E}[Z \mid X, Y = y] \mid X = x] &= \sum_y \mathbf{E}[Z \mid X = x, Y = y] p_{Y \mid X}(y \mid x) \\ &= \sum_y \sum_z z p_{Z \mid X, Y}(z \mid x, y) p_{Y \mid X}(y \mid x) \\ &= \sum_y \sum_z z p_{Y, Z \mid X}(y, z \mid x) \\ &= \mathbf{E}[Z \mid X = x] \end{aligned} $$
Since this is true for all possible values of $x$, we have $\mathbf{E}[\mathbf{E}[Z \mid Y, X] \mid X] = \mathbf{E}[Z \mid X]$.

(c) We take expectations of both sides of the formula in part (b) to obtain
$$ \mathbf{E}[\mathbf{E}[Z \mid X]] = \mathbf{E}[\mathbf{E}[\mathbf{E}[Z \mid X, Y] \mid X]]. $$
By the law of iterated expectations, the left-hand side above is $\mathbf{E}[Z]$, which establishes the desired result.

2. Let $Y$ be the length of the piece after we break for the first time. Let $X$ be the length after we break for the second time.

(a) The law of iterated expectations states:
$$ \mathbf{E}[X] = \mathbf{E}[\mathbf{E}[X \mid Y]] $$
We have $\mathbf{E}[X \mid Y] = \frac{Y}{2}$ and $\mathbf{E}[Y] = \frac{\ell}{2}$. So then:
$$ \mathbf{E}[X] = \mathbf{E}[\mathbf{E}[X \mid Y]] = \mathbf{E}[Y/2] = \frac{1}{2} \mathbf{E}[Y] = \frac{1}{2} \frac{\ell}{2} = \frac{\ell}{4} $$

(b) We use the Law of Total Variance to find $\text{var}(X)$:
$$ \text{var}(X) = \mathbf{E}[\text{var}(X \mid Y)] + \text{var}(\mathbf{E}[X \mid Y]). $$
Recall that the variance of a uniform random variable distributed over $[a, b]$ is $(b - a)^2/12$. Since $Y$ is uniformly distributed over $[0, \ell]$, we have
$$ \begin{aligned} \text{var}(Y) &= \frac{\ell^2}{12}, \\ \text{var}(X \mid Y) &= \frac{Y^2}{12}. \end{aligned} $$
We know that $\mathbf{E}[X \mid Y] = Y/2$, and so
$$ \text{var}(\mathbf{E}[X \mid Y]) = \text{var}(Y/2) = \frac{1}{4} \text{var}(Y) = \frac{\ell^2}{48}. $$
Also,
$$ \begin{aligned} \mathbf{E}[\text{var}(X \mid Y)] &= \mathbf{E}\left[\frac{Y^2}{12}\right] \\ &= \int_0^\ell \frac{y^2}{12} f_Y(y) dy \\ &= \frac{1}{12} \cdot \frac{1}{\ell} \int_0^\ell y^2 dy \\ &= \frac{\ell^2}{36}. \end{aligned} $$
Combining these results, we obtain
$$ \text{var}(X) = \mathbf{E}[\text{var}(X \mid Y)] + \text{var}(\mathbf{E}[X \mid Y]) = \frac{\ell^2}{36} + \frac{\ell^2}{48} = \frac{7\ell^2}{144}. $$

3. Let $X_i$ denote the number of widgets in the $i^{\text{th}}$ box. Then $T = \sum_{i=1}^N X_i$.
$$ \begin{aligned} \mathbf{E}[T] &= \mathbf{E}\left[\mathbf{E}\left[\sum_{i=1}^N X_i \Big| N\right]\right] \\ &= \mathbf{E}\left[\sum_{i=1}^N \mathbf{E}[X_i \mid N]\right] \\ &= \mathbf{E}\left[\sum_{i=1}^N \mathbf{E}[X]\right] \\ &= \mathbf{E}[X] \cdot \mathbf{E}[N] = 100. \end{aligned} $$

and,
$$ \begin{aligned} \text{var}(T) &= \mathbf{E}[\text{var}(T \mid N)] + \text{var}(\mathbf{E}[T \mid N]) \\ &= \mathbf{E}\left[\text{var}\left(\sum_{i=1}^N X_i \Big| N\right)\right] + \text{var}\left(\mathbf{E}\left[\sum_{i=1}^N X_i \Big| N\right]\right) \\ &= \mathbf{E}[N \text{var}(X)] + \text{var}(N \mathbf{E}[X]) \\ &= (\text{var}(X)) \mathbf{E}[N] + (\mathbf{E}[X])^2 \text{var}(N) \\ &= 16 \cdot 10 + 100 \cdot 16 = 1760. \end{aligned} $$

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 13](../13-the-bernoulli-process.md)
