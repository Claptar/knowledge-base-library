---
title: "Solutions — Iterated Expectations and Total Variance"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — Iterated Expectations and Total Variance

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 12 Solutions
## October 19, 2010

1.

$$
\rho(aX + b, Y) &= \frac{\text{cov}(aX + b, Y)}{\sqrt{\text{var}(aX + b)(\text{var}(Y))}} \\
&= \frac{\mathbf{E}[(aX + b - \mathbf{E}[aX + b])(Y - \mathbf{E}[Y])]}{\sqrt{a^2 \text{var}(X) \text{var}(Y)}} \\
&= \frac{\mathbf{E}[(aX + b - a\mathbf{E}[X] - b)(Y - \mathbf{E}[Y])]}{a \sqrt{\text{var}(X) \text{var}(Y)}} \\
&= \frac{a\mathbf{E}[(X - \mathbf{E}[X])(Y - \mathbf{E}[Y])]}{a \sqrt{\text{var}(X) \text{var}(Y)}} \\
&= \frac{\text{cov}(X, Y)}{\sqrt{\text{var}(X) \text{var}(Y)}} \\
&= \rho(X, Y)
$$

As an example where this property of the correlation coefficient is relevant, consider the homework and exam scores of students in a class. We expect the homework and exam scores to be positively correlated and thus have a positive correlation coefficient. Note that, in this example, the above property will mean that the correlation coefficient will not change whether the exam is out of 105 points, 10 points, or any other number of points.

2.

(a) When $z \ge 0$:

$$
F_Z(z) = \mathbf{P}(X - Y \le z) &= \mathbf{P}(X \le Y + z) \\
&= \int_0^\infty \int_0^{y+z} f_{X,Y}(x, y') dx dy \\
&= \int_0^\infty \lambda e^{-\lambda y} \int_0^{y+z} \lambda e^{-\lambda x} dx dy \\
&= \lambda y \left(1 - e^{-\lambda(y+z)}\right) dy \\
&= 1 + \left. \frac{e^{-\lambda z}}{2} e^{-2\lambda y} \right|_{y=0}^{y=\infty} \\
&= 1 - \frac{1}{2} e^{-\lambda z} \quad z \ge 0
$$

When $z < 0$:

$$
\mathbf{P}(X \le Y + z) &= \int_0^\infty \int_0^{y+z} f_{X,Y}(x, y) dx dy \\
&= \int_0^\infty \lambda e^{-\lambda x} \int_{x-z}^\infty \lambda e^{-\lambda y} dy dx \\
&= \int_0^\infty \lambda e^{-\lambda x} e^{-\lambda(x-z)} dx \\
&= e^{\lambda z} \int_0^\infty \lambda e^{-2\lambda x} dx \\
&= \frac{1}{2} e^{\lambda z} \quad z \le 0
$$

$$
F_Z(z) = \begin{cases}
1 - \frac{1}{2} e^{-\lambda z} & z \ge 0 \\
\frac{1}{2} e^{\lambda z} & z < 0
$$

$$
f_Z(z) = \frac{d}{dz} F_Z(z) = \begin{cases}
\frac{\lambda}{2} e^{-\lambda z} & z \ge 0 \\
\frac{\lambda}{2} e^{\lambda z} & z < 0
$$

Hence,

$$
f_Z(z) = \frac{\lambda}{2} e^{\lambda |z|}
$$

(b) Solving using the total probability theorem, we have:

$$
f_Z(z) &= \int_{-\infty}^\infty f_X(x) f_{Z|X}(z|x) dx \\
&= \int_{-\infty}^\infty f_X(x) f_{Y|X}(x - z|x) dx \\
&= \int_{-\infty}^\infty f_X(x) f_Y(x - z) dx
$$

First when $z < 0$, we have:

$$
\int_{-\infty}^\infty f_X(x) f_Y(x - z) dx &= \int_0^\infty \lambda e^{-\lambda x} \lambda e^{-\lambda(x-z)} dx \\
&= \lambda e^{\lambda z} \int_0^\infty \lambda e^{-2\lambda x} dx \\
&= \frac{\lambda}{2} e^{\lambda z}
$$

Then, when $z \ge 0$ we have:

$$
\int_{-\infty}^\infty f_X(x) f_Y(x - z) dx &= \int_z^\infty \lambda e^{-\lambda x} \lambda e^{-\lambda(x-z)} dx \\
&= \lambda e^{\lambda z} \int_z^\infty \lambda e^{-2\lambda x} dx \\
&= \frac{\lambda}{2} e^{\lambda z} e^{-2\lambda z} \\
&= \frac{\lambda}{2} e^{-\lambda z}
$$

$$
f_Z(z) = \frac{\lambda}{2} e^{-\lambda |z|} \quad \forall z
$$

3. (a) We have $X = R\cos(\Theta)$ and $Y = R\sin(\Theta)$. Recall that in polar coordinates, the differential area is $dA = dx dy = r dr d\theta$. So

$$
F_R(r) = \mathbf{P}(R \le r) &= \int_0^r \int_0^{2\pi} f_X(r' \cos\theta) f_Y(r' \sin\theta) d\theta \, r' dr' \\
&= \int_0^r \int_0^{2\pi} \frac{1}{2\pi} e^{-(r')^2/2} d\theta \, r' dr' \\
&= \int_0^r r' e^{-(r')^2/2} dr' \int_0^{2\pi} \frac{d\theta}{2\pi} \\
&= \int_0^{r^2/2} e^{-u} du \quad (u = (r')^2/2)
$$

$$
F_R(r) = \begin{cases}
1 - e^{-r^2/2} & r \ge 0 \\
0 & r < 0
$$

$$
f_R(r) = \frac{d}{dr} F_R(r) &= (-1/2)(2r)(-e^{-r^2/2}) \\
&= r e^{-r^2/2}, \quad r \ge 0
$$

(b)

$$
F_\Theta(\theta) = \mathbf{P}(\Theta \le \theta) &= \int_0^\theta \int_0^\infty f_X(r\cos\theta') f_Y(r\sin\theta') r dr \, d\theta' \\
&= \int_0^\theta \int_0^\infty \frac{1}{2\pi} e^{-r^2/2} r dr \, d\theta' \\
&= \int_0^\infty r e^{-r^2/2} dr \int_0^\theta \frac{d\theta'}{2\pi} \\
&= \frac{\theta}{2\pi} \int_0^\infty e^{-u} du \quad (u = r^2/2) \\
&= \frac{\theta}{2\pi} \left[ -e^{-u} \right]_0^\infty = \frac{\theta}{2\pi} \quad 0 \le \theta \le 2\pi
$$

$$
F_\Theta(\theta) = \begin{cases}
0 & \theta < 0 \\
\frac{\theta}{2\pi} & 0 \le \theta \le 2\pi \\
1 & \theta \ge 2\pi
$$

$$
f_\Theta(\theta) = \frac{d}{d\theta} F_\Theta(\theta) = \frac{1}{2\pi} \quad 0 \le \theta \le 2\pi
$$

(c)

$$
F_{R,\Theta}(r, \theta) = \mathbf{P}(R \le r, \Theta \le \theta) &= \int_0^\theta \int_0^r \frac{1}{2\pi} r' e^{-(r')^2/2} dr' d\theta' \\
&= \int_0^\theta \int_0^{r^2/2} \frac{1}{2\pi} e^{-u} du \, d\theta' \quad (u = (r')^2/2) \\
&= \int_0^\theta \frac{1}{2\pi} \left(1 - e^{-r^2/2}\right) d\theta' \\
&= \frac{\theta}{2\pi} \left(1 - e^{-r^2/2}\right) \quad r \ge 0, \quad \theta > 2\pi
$$

$$
F_{R,\Theta}(r, \theta) = \begin{cases}
\frac{\theta}{2\pi} \left(1 - e^{-r^2/2}\right) & r \ge 0, \quad 0 \le \theta \le 2\pi \\
1 - e^{-r^2/2} & r \ge 0, \quad \theta > 2\pi \\
0 & \text{otherwise}
$$

$$
f_{R,\Theta}(r, \theta) = \frac{\partial}{\partial r} \frac{\partial}{\partial \theta} F_{R,\Theta}(r, \theta) = \frac{1}{2\pi} r e^{-r^2/2} \quad r \ge 0, \quad 0 \le \theta \le 2\pi
$$

Note: The PDF of $R^2$ is exponentially distributed with parameter $\lambda = 1/2$. This is a very convenient way to generate normal random variables from independent uniform and exponential random variables. We can generate an arbitrary random variable $X$ with CDF $F_X$ by first generating a uniform random variable and then passing the samples from the uniform distribution through the function $F_X^{-1}$. But since we don't have a closed-form expression for the CDF of a normal random variable, this method doesn't work. However, we do have a closed-form expression for the exponential distribution. Therefore, we can generate an exponential distribution with parameter $1/2$ and we can generate a uniform distribution in $[0, 2\pi]$, and with these two distributions we can generate standard normal distributions.

4. Problem 4.20, page 250 in text. See text for the proof.

An alternative proof is given below:

Consider the problem of picking a parameter $\alpha$ to minimize the expected squared difference between two random variables $X$ and $Y$. Consider

$$
J(\alpha) = \mathbf{E}\left[(X - \alpha Y)^2\right]
$$

with $Y \ne 0$. We start with a variational calculation to find $\alpha$ that minimizes $J(\alpha)$. The value of $\alpha$ which minimizes $J(\alpha)$ is found by setting the first derivative of $J(\alpha)$ to zero (since, for $Y \ne 0$, $\frac{d^2}{d\alpha^2} J(\alpha) = 2\mathbf{E}[Y^2] > 0$).

$$\frac{dJ}{d\alpha} = 0$$

$$
\frac{d}{d\alpha} J(\alpha) = \frac{d}{d\alpha} \left(\mathbf{E}[X^2] - 2\alpha \mathbf{E}[XY] + \alpha^2 \mathbf{E}[Y^2]\right) = 0
$$

$$
\rightarrow \alpha = \frac{\mathbf{E}[XY]}{\mathbf{E}[Y^2]} \text{ minimizes } J(\alpha).
$$

Then

$$
J\left(\frac{\mathbf{E}[XY]}{\mathbf{E}[Y^2]}\right) &= \mathbf{E}\left[\left(X - \frac{\mathbf{E}[XY]}{\mathbf{E}[Y^2]} Y\right)^2\right] \ge 0 \\
&= \mathbf{E}[X^2] - 2\frac{(\mathbf{E}[XY])^2}{\mathbf{E}[Y^2]} + \frac{(\mathbf{E}[XY])^2 \mathbf{E}[Y^2]}{(\mathbf{E}[Y^2])^2} \\
&= \mathbf{E}[X^2] - \frac{(\mathbf{E}[XY])^2}{\mathbf{E}[Y^2]} \ge 0
$$

Rearranging this expression gives the Schwarz inequality for expected values:

$$
\mathbf{E}[X^2]\mathbf{E}[Y^2] \ge (\mathbf{E}[XY])^2
$$

Note that in the above derivation, we assumed $Y \ne 0$ so that $\mathbf{E}[Y^2] > 0$. If we assume $Y = 0$ then the Schwarz inequality will hold with equality since then $\mathbf{E}[XY] = 0$ and $\mathbf{E}[Y^2] = 0$.

---

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

## Department of Electrical Engineering & Computer Science
## 6.041SC Probabilistic Systems Analysis and Applied Probability
## Lecture 12 Bonus Video Solution

**Problem 27.\*** We toss $n$ times a biased coin whose probability of heads, denoted by $q$, is the value of a random variable $Q$ with given mean $\mu$ and positive variance $\sigma^2$. Let $X_i$ be a Bernoulli random variable that models the outcome of the $i$th toss (i.e., $X_i = 1$ if the $i$th toss is a head). We assume that $X_1, \dots, X_n$ are conditionally independent, given $Q = q$. Let $X$ be the number of heads obtained in the $n$ tosses.

(a) Use the law of iterated expectations to find $\mathbf{E}[X_i]$ and $\mathbf{E}[X]$.

(b) Find $\text{cov}(X_i, X_j)$. Are $X_1, \dots, X_n$ independent?

(c) Use the law of total variance to find $\text{var}(X)$. Verify your answer using the covariance result of part (b).

**Solution.** (a) We have, from the law of iterated expectations and the fact $\mathbf{E}[X_i \mid Q] = Q$,

$$\mathbf{E}[X_i] = \mathbf{E}[\mathbf{E}[X_i \mid Q]] = \mathbf{E}[Q] = \mu.$$

Since $X = X_1 + \dots + X_n$, it follows that

$$\mathbf{E}[X] = \mathbf{E}[X_1] + \dots + \mathbf{E}[X_n] = n\mu.$$

(b) We have, for $i \neq j$, using the conditional independence assumption,

$$\mathbf{E}[X_i X_j \mid Q] = \mathbf{E}[X_i \mid Q]\mathbf{E}[X_j \mid Q] = Q^2,$$

and

$$\mathbf{E}[X_i X_j] = \mathbf{E}[\mathbf{E}[X_i X_j \mid Q]] = \mathbf{E}[Q^2].$$

Thus,

$$\text{cov}(X_i, X_j) = \mathbf{E}[X_i X_j] - \mathbf{E}[X_i]\mathbf{E}[X_j] = \mathbf{E}[Q^2] - \mu^2 = \sigma^2.$$

Since $\text{cov}(X_i, X_j) > 0$, $X_1, \dots, X_n$ are not independent.

Also, for $i = j$, using the observation that $X_i^2 = X_i$,

$$\begin{aligned}
\text{var}(X_i) &= \mathbf{E}[X_i^2] - (\mathbf{E}[X_i])^2 \\
&= \mathbf{E}[X_i] - (\mathbf{E}[X_i])^2 \\
&= \mu - \mu^2.
\end{aligned}$$

(c) Using the law of total variance, and the conditional independence of $X_1, \dots, X_n$, we have

$$\begin{aligned}
\text{var}(X) &= \mathbf{E}[\text{var}(X \mid Q)] + \text{var}(\mathbf{E}[X \mid Q]) \\
&= \mathbf{E}[\text{var}(X_1 + \dots + X_n \mid Q)] + \text{var}(\mathbf{E}[X_1 + \dots + X_n \mid Q]) \\
&= \mathbf{E}[nQ(1 - Q)] + \text{var}(nQ) \\
&= n\mathbf{E}[Q - Q^2] + n^2\text{var}(Q) \\
&= n(\mu - \mu^2 - \sigma^2) + n^2\sigma^2 \\
&= n(\mu - \mu^2) + n(n - 1)\sigma^2.
\end{aligned}$$

To verify the result using the covariance formulas of part (b), we write

$$\begin{aligned}
\text{var}(X) &= \text{var}(X_1 + \dots + X_n) \\
&= \sum_{i=1}^n \text{var}(X_i) + \sum_{\{(i,j) \mid i \neq j\}} \text{cov}(X_i, X_j) \\
&= n\text{var}(X_1) + n(n - 1)\text{cov}(X_1, X_2) \\
&= n(\mu - \mu^2) + n(n - 1)\sigma^2.
\end{aligned}$$

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 12](../12-iterated-expectations-and-total-variance.md)
