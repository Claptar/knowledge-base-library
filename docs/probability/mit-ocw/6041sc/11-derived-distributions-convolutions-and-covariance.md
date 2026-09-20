---
title: "11. Derived Distributions, Convolutions, and Covariance"
course: "MIT 6.041SC"
chapter: 11
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 11. Derived Distributions, Convolutions, and Covariance

## What this covers

This chapter addresses how to determine the probability distribution of functions of multiple random variables, specifically through the cumulative distribution function (CDF) technique and the direct monotonic transformation shortcut. It analyzes the distribution of the sum of independent random variables via discrete and continuous convolution, establishes the closure of normal distributions under addition, and introduces covariance and correlation to quantify linear dependencies between variables. It assumes familiarity with single-variable derived distributions, joint probability density functions, and the basics of expected values and variance.

## Derived Distributions via the CDF Method

When finding the probability density function (PDF) of a random variable $Z = g(X, Y)$ defined as a function of two continuous random variables $X$ and $Y$, the general two-step procedure parallels the single-variable case:
1. Determine the cumulative distribution function $F_Z(z) = \mathbf{P}(Z \le z) = \mathbf{P}(g(X, Y) \le z)$ by integrating the joint density $f_{X, Y}(x, y)$ over the region where $g(x, y) \le z$.
2. Differentiate $F_Z(z)$ with respect to $z$ to obtain the density $f_Z(z) = \frac{d}{dz}F_Z(z)$.

### Example: Ratio of Independent Uniform Random Variables

Let $X$ and $Y$ be independent continuous random variables, each uniformly distributed on the interval $[0, 1]$. Their joint PDF is constant on the unit square:
$$f_{X,Y}(x, y) = 1, \quad 0 \le x \le 1, \; 0 \le y \le 1$$
We seek the PDF of $Z = Y / X$.

Since $X, Y \in [0, 1]$, the ratio $Z$ can take any value in $[0, \infty)$. For $z < 0$, $F_Z(z) = 0$. For $z \ge 0$, the CDF is:
$$F_Z(z) = \mathbf{P}\left(\frac{Y}{X} \le z\right) = \mathbf{P}(Y \le zX)$$

This represents the probability that the point $(X, Y)$ falls beneath the straight line $y = zx$ passing through the origin with slope $z$.

<figure>
<svg viewBox="0 0 440 220" role="img" aria-label="Integration regions for the ratio of uniform random variables when the slope is less than one versus greater than one">
  <!-- Left panel: z ≤ 1 -->
  <rect x="40" y="40" width="140" height="140" fill="none" stroke="currentColor" stroke-width="1"/>
  <polygon points="40,180 180,180 180,98" fill="currentColor" fill-opacity="0.15"/>
  <line x1="40" y1="180" x2="180" y2="98" stroke="currentColor" stroke-width="1.5"/>
  <text x="35" y="185" text-anchor="end" font-size="12" fill="currentColor">0</text>
  <text x="180" y="195" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="35" y="45" text-anchor="end" font-size="12" fill="currentColor">1</text>
  <text x="185" y="98" text-anchor="start" font-size="12" fill="currentColor">z</text>
  <text x="110" y="210" text-anchor="middle" font-size="12" fill="currentColor">Case 1: z ≤ 1</text>

  <!-- Right panel: z ≥ 1 -->
  <rect x="250" y="40" width="140" height="140" fill="none" stroke="currentColor" stroke-width="1"/>
  <!-- Unshaded triangle is (250,40) to (308,40) to (250,180) -->
  <!-- Shaded polygon is complement: (250,180) to (308,40) to (390,40) to (390,180) -->
  <polygon points="250,180 308,40 390,40 390,180" fill="currentColor" fill-opacity="0.15"/>
  <line x1="250" y1="180" x2="308" y2="40" stroke="currentColor" stroke-width="1.5"/>
  <text x="245" y="185" text-anchor="end" font-size="12" fill="currentColor">0</text>
  <text x="390" y="195" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <text x="245" y="45" text-anchor="end" font-size="12" fill="currentColor">1</text>
  <text x="308" y="32" text-anchor="middle" font-size="12" fill="currentColor">1/z</text>
  <text x="320" y="210" text-anchor="middle" font-size="12" fill="currentColor">Case 2: z ≥ 1</text>
</svg>
<figcaption>Integration geometry within the unit square for the line $y = zx$ under $z \le 1$ and $z \ge 1$.</figcaption>
</figure>

The geometry bifurcates depending on whether the line exits the unit square through its right boundary ($x = 1$) or its top boundary ($y = 1$):

* **Case 1 ($0 \le z \le 1$):** The line intersects the line $x = 1$ at $y = z$. The region beneath the line inside the unit square is a right triangle with base $1$ and height $z$. Because the joint density is uniform with value $1$, the probability is the area:
  $$F_Z(z) = \frac{1}{2} \cdot 1 \cdot z = \frac{z}{2}$$

* **Case 2 ($z \ge 1$):** The line intersects the upper boundary $y = 1$ at $x = 1/z$. It is simpler to compute the probability of the complement: the region above the line is a right triangle with height $1$ and base $1/z$. Subtracting this from the total area of $1$:
  $$F_Z(z) = 1 - \frac{1}{2} \cdot 1 \cdot \frac{1}{z} = 1 - \frac{1}{2z}$$

Combining the intervals, the CDF is:
$$F_Z(z) = \begin{cases} 
0, & z < 0 \\
\frac{z}{2}, & 0 \le z \le 1 \\
1 - \frac{1}{2z}, & z > 1 
\end{cases}$$

Differentiating with respect to $z$ yields the PDF:
$$f_Z(z) = \frac{d F_Z(z)}{dz} = \begin{cases} 
\frac{1}{2}, & 0 \le z \le 1 \\
\frac{1}{2z^2}, & z > 1 \\
0, & \text{otherwise}
\end{cases}$$

### Expectation of the Ratio

Computing the expected value $\mathbf{E}[Z]$ illustrates that derived variables can exhibit heavy tails:
$$\mathbf{E}[Z] = \int_0^\infty z f_Z(z) \, dz = \int_0^1 z \left(\frac{1}{2}\right) dz + \int_1^\infty z \left(\frac{1}{2z^2}\right) dz = \left[ \frac{z^2}{4} \right]_0^1 + \frac{1}{2} \int_1^\infty \frac{1}{z} \, dz$$
The second integral evaluates to $\lim_{M \to \infty} [\ln M - \ln 1] = \infty$. Thus, $\mathbf{E}[Z] = \infty$.

A common conceptual error is to compute expectations "on average," guessing $\mathbf{E}[Y/X] = \mathbf{E}[Y] / \mathbf{E}[X]$. For non-linear transformations, expectations do not distribute across functions: $\mathbf{E}[g(X, Y)] \ne g(\mathbf{E}[X], \mathbf{E}[Y])$. Because $X$ and $Y$ are independent, any functions of them are also independent; hence $1/X$ is independent of $Y$, allowing:
$$\mathbf{E}\left[\frac{Y}{X}\right] = \mathbf{E}\left[Y \cdot \frac{1}{X}\right] = \mathbf{E}[Y] \cdot \mathbf{E}\left[\frac{1}{X}\right]$$
Here $\mathbf{E}[Y] = 1/2$, while $\mathbf{E}[1/X] = \int_0^1 \frac{1}{x} dx = \infty$, confirming $\mathbf{E}[Z] = \infty$.

## Direct Formula for Monotonic Functions

When $Y = g(X)$ is a strictly monotonic function (either strictly increasing or strictly decreasing) of a continuous random variable $X$, there is a one-to-one correspondence between $x$ and $y$. We can bypass calculating the CDF by matching probabilities of corresponding differential intervals.

<figure>
<svg viewBox="0 0 360 220" role="img" aria-label="Mapping an interval delta on the x-axis to an interval stretched by the derivative on the y-axis">
  <!-- Axes -->
  <line x1="40" y1="190" x2="340" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="190" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="340" y="205" text-anchor="middle" font-size="12" fill="currentColor">x</text>
  <text x="25" y="30" text-anchor="middle" font-size="12" fill="currentColor">y</text>
  
  <!-- Monotonic curve -->
  <path d="M 60,170 Q 140,150 200,100 T 310,30" fill="none" stroke="currentColor" stroke-width="1.5"/>
  
  <!-- Interval on x-axis -->
  <line x1="160" y1="187" x2="160" y2="193" stroke="currentColor" stroke-width="1.5"/>
  <line x1="190" y1="187" x2="190" y2="193" stroke="currentColor" stroke-width="1.5"/>
  <line x1="160" y1="190" x2="190" y2="190" stroke="currentColor" stroke-width="3"/>
  <text x="175" y="208" text-anchor="middle" font-size="12" fill="currentColor">δ</text>
  
  <!-- Dashed projections to curve and y-axis -->
  <line x1="160" y1="190" x2="160" y2="128" stroke="currentColor" stroke-dasharray="3,3"/>
  <line x1="190" y1="190" x2="190" y2="108" stroke="currentColor" stroke-dasharray="3,3"/>
  
  <line x1="40" y1="128" x2="160" y2="128" stroke="currentColor" stroke-dasharray="3,3"/>
  <line x1="40" y1="108" x2="190" y2="108" stroke="currentColor" stroke-dasharray="3,3"/>
  
  <!-- Interval on y-axis -->
  <line x1="37" y1="128" x2="43" y2="128" stroke="currentColor" stroke-width="1.5"/>
  <line x1="37" y1="108" x2="43" y2="108" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="128" x2="40" y2="108" stroke="currentColor" stroke-width="3"/>
  <text x="25" y="122" text-anchor="end" font-size="11" fill="currentColor">δ |g'|</text>
</svg>
<figcaption>Transformation of a small interval $\delta$ under a strictly monotonic map $g(x)$.</figcaption>
</figure>

Consider a small interval $[x, x + \delta]$ on the $x$-axis. The probability that $X$ falls in this interval is:
$$\mathbf{P}(x \le X \le x + \delta) \approx f_X(x) \cdot \delta$$

Under a strictly increasing mapping $g$, the event $x \le X \le x + \delta$ is identical to $g(x) \le Y \le g(x + \delta)$. By first-order Taylor approximation, the length of the resulting interval on the $y$-axis is:
$$g(x + \delta) - g(x) \approx \delta \left| \frac{dg}{dx}(x) \right|$$

Because these two intervals correspond to identical events, their probabilities must match:
$$f_Y(y) \cdot \delta \left| \frac{dg}{dx}(x) \right| \approx f_X(x) \cdot \delta$$

Canceling $\delta$ and solving for the density of $Y$:
$$f_Y(y) = \frac{f_X(x)}{\left| \frac{dg}{dx}(x) \right|} \Bigg|_{x = g^{-1}(y)}$$

Where the derivative $\frac{dg}{dx}$ is small (i.e., the mapping function $g$ is relatively flat), small intervals of $y$ collect outcomes from larger intervals of $x$, producing high probability densities $f_Y(y)$. Conversely, where $g$ is steep, probability is dispersed over a wide range of $y$, driving $f_Y(y)$ down.

### Example: $Y = X^3$

Let $Y = g(X) = X^3$, which is strictly monotonic for all $x \in \mathbb{R}$. The inverse mapping is $x = y^{1/3}$, and the derivative is $\frac{dg}{dx} = 3x^2$. Applying the transformation formula:
$$f_Y(y) = \frac{f_X(x)}{3x^2} \Bigg|_{x = y^{1/3}} = \frac{f_X(y^{1/3})}{3 y^{2/3}}$$

## Sums of Independent Random Variables: Convolution

Let $W = X + Y$, where $X$ and $Y$ are independent. The process of determining the distribution of $W$ from the individual distributions of $X$ and $Y$ is called **convolution**.

### Discrete Case

For discrete random variables with PMFs $p_X$ and $p_Y$, the event $W = w$ can be partitioned into mutually exclusive outcomes over all possible values of $X$:
$$p_W(w) = \mathbf{P}(X + Y = w) = \sum_x \mathbf{P}(X = x, Y = w - x)$$

Using the independence of $X$ and $Y$, the joint probability factorizes:
$$p_W(w) = \sum_x p_X(x) p_Y(w - x)$$

To calculate $p_W(w)$ graphically:
1. Plot $p_X(x)$ and $p_Y(x)$ along the same axis.
2. Reflect the PMF of $Y$ about the origin to produce $p_Y(-x)$.
3. Shift the reflected PMF to the right by $w$ units to obtain $p_Y(w - x)$.
4. Multiply overlapping points $p_X(x) p_Y(w - x)$ and sum the products.

### Continuous Case

In the continuous case, the summation is replaced by an integral. Conditioning on $X = x$:
$$f_{W|X}(w \mid x) = \frac{d}{dw}\mathbf{P}(X + Y \le w \mid X = x) = \frac{d}{dw}\mathbf{P}(Y \le w - x \mid X = x)$$
By independence, conditioning on $X = x$ leaves $Y$ unaffected:
$$f_{W|X}(w \mid x) = f_Y(w - x)$$

The joint density of $W$ and $X$ is therefore:
$$f_{W, X}(w, x) = f_X(x) f_{W|X}(w \mid x) = f_X(x) f_Y(w - x)$$

Integrating out $x$ gives the marginal PDF of $W$:
$$f_W(w) = \int_{-\infty}^\infty f_X(x) f_Y(w - x) \, dx$$

Geometrically, computing $f_W(w)$ corresponds to integrating the joint density $f_{X,Y}(x, y) = f_X(x)f_Y(y)$ along the diagonal line $x + y = w$.

## Sums of Independent Normal Random Variables

Let $X \sim \mathcal{N}(\mu_x, \sigma_x^2)$ and $Y \sim \mathcal{N}(\mu_y, \sigma_y^2)$ be independent normal random variables. Their joint PDF is:
$$f_{X,Y}(x, y) = \frac{1}{2\pi \sigma_x \sigma_y} \exp\left\{ - \frac{(x - \mu_x)^2}{2\sigma_x^2} - \frac{(y - \mu_y)^2}{2\sigma_y^2} \right\}$$

The contours of equal probability density are defined by:
$$\frac{(x - \mu_x)^2}{2\sigma_x^2} + \frac{(y - \mu_y)^2}{2\sigma_y^2} = c$$
which describe concentric ellipses centered at $(\mu_x, \mu_y)$. If $\sigma_x = \sigma_y$, these contours are concentric circles.

To find the distribution of $W = X + Y$ for independent zero-mean normals ($X \sim \mathcal{N}(0, \sigma_x^2)$, $Y \sim \mathcal{N}(0, \sigma_y^2)$), evaluate the continuous convolution integral:
$$f_W(w) = \frac{1}{2\pi \sigma_x \sigma_y} \int_{-\infty}^\infty \exp\left\{ -\frac{x^2}{2\sigma_x^2} \right\} \exp\left\{ -\frac{(w - x)^2}{2\sigma_y^2} \right\} dx$$

Expanding the quadratic terms in the exponent and completing the square with respect to $x$ yields an integrand proportional to a Gaussian density in $x$. Factoring out terms that depend only on $w$, the integral over $x$ integrates to a constant, leaving:
$$f_W(w) = c \exp\left\{ -\gamma w^2 \right\}$$
where $\gamma = \frac{1}{2(\sigma_x^2 + \sigma_y^2)}$. This functional form is another normal distribution. 

By linearity of expectation and variance of independent variables:
$$\mathbf{E}[W] = \mathbf{E}[X] + \mathbf{E}[Y] = \mu_x + \mu_y$$
$$\operatorname{var}(W) = \operatorname{var}(X) + \operatorname{var}(Y) = \sigma_x^2 + \sigma_y^2$$

Thus, the sum of independent normal random variables is always normal:
$$W \sim \mathcal{N}\left(\mu_x + \mu_y, \, \sigma_x^2 + \sigma_y^2\right)$$

## Covariance

When random variables are not independent, their joint variation is characterized by their **covariance**.

### Definition

The covariance of two random variables $X$ and $Y$ measures the degree to which deviations of $X$ from its mean are associated with deviations of $Y$ from its mean:
$$\operatorname{cov}(X, Y) = \mathbf{E}\left[ (X - \mathbf{E}[X])(Y - \mathbf{E}[Y]) \right]$$

Expanding the expectation yields the standard computational shortcut:
$$\operatorname{cov}(X, Y) = \mathbf{E}[XY - X\mathbf{E}[Y] - \mathbf{E}[X]Y + \mathbf{E}[X]\mathbf{E}[Y]] = \mathbf{E}[XY] - \mathbf{E}[X]\mathbf{E}[Y]$$

For zero-mean random variables, $\operatorname{cov}(X, Y) = \mathbf{E}[XY]$.

### Properties

1. **Self-covariance is variance:**
   $$\operatorname{cov}(X, X) = \mathbf{E}\left[(X - \mathbf{E}[X])^2\right] = \operatorname{var}(X)$$
2. **Symmetry:**
   $$\operatorname{cov}(X, Y) = \operatorname{cov}(Y, X)$$
3. **Independence implies zero covariance:**
   If $X$ and $Y$ are independent, $\mathbf{E}[XY] = \mathbf{E}[X]\mathbf{E}[Y]$, so:
   $$\operatorname{cov}(X, Y) = 0$$
   The converse is **not** true in general: a zero covariance indicates an absence of linear association, but higher-order nonlinear dependencies may exist.

### Variance of a Sum of Dependent Variables

For a sum of $n$ random variables $\sum_{i=1}^n X_i$:
$$\operatorname{var}\left(\sum_{i=1}^n X_i\right) = \mathbf{E}\left[ \left( \sum_{i=1}^n (X_i - \mathbf{E}[X_i]) \right)^2 \right]$$
Expanding the square of the sum into diagonal and off-diagonal cross terms:
$$\operatorname{var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \operatorname{var}(X_i) + \sum_{i \ne j} \operatorname{cov}(X_i, X_j)$$
By symmetry, $\operatorname{cov}(X_i, X_j) = \operatorname{cov}(X_j, X_i)$, so this can also be written as:
$$\operatorname{var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \operatorname{var}(X_i) + 2 \sum_{1 \le i < j \le n} \operatorname{cov}(X_i, X_j)$$

## Correlation Coefficient

A deficiency of covariance is that its value depends directly on the physical units in which $X$ and $Y$ are measured. Multiplying $X$ by a constant scales the covariance by that constant.

The **correlation coefficient** $\rho(X, Y)$ normalizes the covariance by dividing by the product of individual standard deviations, producing a dimensionless measure of linear dependence:
$$\rho = \mathbf{E}\left[ \left(\frac{X - \mathbf{E}[X]}{\sigma_X}\right) \left(\frac{Y - \mathbf{E}[Y]}{\sigma_Y}\right) \right] = \frac{\operatorname{cov}(X, Y)}{\sigma_X \sigma_Y}$$

### Key Properties

* **Bounded Range:** 
  $$-1 \le \rho \le 1$$
* **Extreme Values and Linearity:** 
  $|\rho| = 1$ if and only if $X - \mathbf{E}[X]$ and $Y - \mathbf{E}[Y]$ are perfect linear functions of one another:
  $$Y - \mathbf{E}[Y] = c (X - \mathbf{E}[X])$$
  where $\rho = 1$ if $c > 0$, and $\rho = -1$ if $c < 0$.
* **Uncorrelated Variables:** 
  If $X$ and $Y$ are independent, $\rho = 0$. However, $\rho = 0$ does not imply independence.

## Exercises

### Exercise 1
Let $X$ be a discrete random variable that takes the values $1$ with probability $p$ and $-1$ with probability $1 - p$. Let $Y$ be a continuous random variable independent of $X$ with the Laplacian (two-sided exponential) distribution
$$f_Y(y) = \frac{1}{2}\lambda e^{-\lambda|y|},$$
and let $Z = X + Y$. Find $\mathbf{P}(X = 1 \mid Z = z)$. Check that the expression obtained makes sense for $p \to 0^+$, $p \to 1^-$, $\lambda \to 0^+$, and $\lambda \to \infty$.

### Exercise 2
Let $Q$ be a continuous random variable with PDF
$$f_Q(q) = \begin{cases} 6q(1 - q), & \text{if } 0 \le q \le 1, \\ 0, & \text{otherwise.} \end{cases}$$
This $Q$ represents the probability of success of a Bernoulli random variable $X$, i.e.,
$$\mathbf{P}(X = 1 \mid Q = q) = q.$$
Find $f_{Q \mid X}(q \mid x)$ for $x \in \{0, 1\}$ and all $q$.

### Exercise 3
Let $X$ have the standard normal distribution with mean $0$ and variance $1$:
$$f_X(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$
Let $Y = g(X)$, where
$$g(t) = \begin{cases} -t, & \text{for } t \le 0 \\ \sqrt{t}, & \text{for } t > 0 \end{cases}$$
Find the probability density function of $Y$.

## Sources

* **Derived Distributions via CDF:** Slide "Example: $f_{X,Y}(y, x) = 1$", Transcript [01:05]–[12:14].
* **Strictly Monotonic Derived Distributions:** Slide "A general formula", Transcript [13:17]–[23:20].
* **Discrete and Continuous Convolution:** Slides "The distribution of $X + Y$" and "The continuous case", Transcript [24:29]–[33:11].
* **Sum of Independent Normal Variables:** Slides "Two independent normal r.v.s" and "The sum of independent normal r.v.'s", Transcript [33:11]–[40:55].
* **Covariance and Correlation Coefficient:** Slides "Covariance" and "Correlation coefficient", Transcript [41:00]–[50:47].
* **Exercises:** Recitation 11 problems 1, 2, and 3 (Fall 2010). Note: the variance formula on the lecture slide contained a typographical index notation corrected during lecture delivery at [46:24].

Solutions: [chapter 11](solutions/11-derived-distributions-convolutions-and-covariance.md)


---

[← 10. Derived Distributions and Bayesian Inference](10-derived-distributions-and-bayesian-inference.md) · [Contents](index.md) · [12. Iterated Expectations and Total Variance →](12-iterated-expectations-and-total-variance.md)
