---
title: "9. Joint and Conditional Continuous Densities"
course: "MIT 6.041SC"
chapter: 9
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 9. Joint and Conditional Continuous Densities

## What this covers

This chapter extends probability models from a single continuous random variable to pairs of continuous random variables. It develops the joint probability density function, marginalization, independence, and conditional probability density functions, culminating in classical applications including Buffon's needle and sequential stick-breaking. It assumes familiarity with single-variable continuous densities, cumulative distribution functions, and single-variable expectations.

## Joint Probability Density Functions

When modeling two continuous random variables $X$ and $Y$ simultaneously, their joint distribution is described by a joint probability density function (joint PDF), denoted $f_{X,Y}(x, y)$. 

By definition, two random variables $X$ and $Y$ are jointly continuous if there exists a non-negative function $f_{X,Y}(x, y)$ such that for any subset $S$ of the two-dimensional plane:

$$\mathbf{P}((X, Y) \in S) = \iint_S f_{X,Y}(x, y) \, dx \, dy$$

Geometrically, $f_{X,Y}(x, y)$ defines a surface over the $(x, y)$-plane. The probability that the pair $(X, Y)$ falls within the region $S$ is the volume beneath this surface sitting directly above $S$.

Because total probability must equal 1, the joint PDF must integrate over the entire plane to unity:

$$\int_{-\infty}^\infty \int_{-\infty}^\infty f_{X,Y}(x, y) \, dx \, dy = 1$$

and non-negativity requires:

$$f_{X,Y}(x, y) \ge 0, \quad \text{for all } x, y$$

### Intuitive Interpretation: Probability per Unit Area

To interpret $f_{X,Y}(x, y)$ physically, consider the probability of falling inside an infinitesimal rectangle with corners at $(x, y)$ and $(x + \delta, y + \delta)$:

$$\mathbf{P}(x \le X \le x + \delta, \; y \le Y \le y + \delta) = \int_y^{y + \delta} \int_x^{x + \delta} f_{X,Y}(u, v) \, du \, dv$$

If $\delta$ is sufficiently small and $f_{X,Y}$ is continuous, the density is approximately constant across the rectangle. The volume is well-approximated by the height times the base area:

$$\mathbf{P}(x \le X \le x + \delta, \; y \le Y \le y + \delta) \approx f_{X,Y}(x, y) \cdot \delta^2$$

Thus, the joint PDF has dimensions of probability per unit area. Higher values indicate regions in the plane where probability mass is concentrated.

### Expected Values of Functions of Two Variables

For any real-valued function $g(X, Y)$, the expected value $\mathbf{E}[g(X, Y)]$ generalizes the discrete formula by replacing the double sum and joint PMF with a double integral and joint PDF:

$$\mathbf{E}[g(X, Y)] = \int_{-\infty}^\infty \int_{-\infty}^\infty g(x, y) f_{X,Y}(x, y) \, dx \, dy$$

In each tiny cell of area $\delta^2$, the function takes the approximate value $g(x, y)$ with probability roughly $f_{X,Y}(x, y) \, \delta^2$. Summing over all cells yields this integral.

## Marginalization and Independence

Given the joint PDF $f_{X,Y}(x, y)$, we can recover the individual (marginal) density of $X$ by integrating out $Y$.

Consider the probability that $X$ lies in a small interval $[x, x + \delta]$. Geometrically, this corresponds to the vertical strip where $X \in [x, x + \delta]$ and $Y \in (-\infty, \infty)$:

$$\mathbf{P}(x \le X \le x + \delta) = \int_{-\infty}^\infty \left[ \int_x^{x + \delta} f_{X,Y}(u, y) \, du \right] dy \approx \int_{-\infty}^\infty f_{X,Y}(x, y) \cdot \delta \, dy$$

Comparing this with the fundamental single-variable identity $\mathbf{P}(x \le X \le x + \delta) \approx f_X(x) \cdot \delta$, dividing by $\delta$ gives:

$$f_X(x) = \int_{-\infty}^\infty f_{X,Y}(x, y) \, dy$$

Similarly, integrating out $x$ yields the marginal density of $Y$:

$$f_Y(y) = \int_{-\infty}^\infty f_{X,Y}(x, y) \, dx$$

### Independence

Two continuous random variables $X$ and $Y$ are independent if and only if their joint PDF factors into the product of their marginal PDFs for all $x$ and $y$:

$$f_{X,Y}(x, y) = f_X(x) f_Y(y), \quad \text{for all } x, y$$

When $X$ and $Y$ are independent, probabilities of product events factor directly:

$$\mathbf{P}(X \in A, \; Y \in B) = \mathbf{P}(X \in A) \, \mathbf{P}(Y \in B)$$

## Example: Buffon's Needle

Buffon's needle is a classical problem showing how a joint continuous model translates geometric randomness into calculated probabilities.

### Problem Formulation

Consider a floor with horizontal parallel lines separated by a fixed distance $d$. A needle of length $\ell$ is dropped at random onto the floor. We assume $\ell < d$, ensuring the needle can intersect at most one line. What is the probability that the needle intersects one of the lines?

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="Buffon's needle between two parallel lines separated by distance d">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Parallel lines -->
  <line x1="30" y1="30" x2="310" y2="30" stroke="currentColor" stroke-width="2"/>
  <line x1="30" y1="170" x2="310" y2="170" stroke="currentColor" stroke-width="2"/>
  <text x="315" y="34" font-size="12" fill="currentColor">line</text>
  <text x="315" y="174" font-size="12" fill="currentColor">line</text>
  <!-- Distance d indicator -->
  <line x1="45" y1="30" x2="45" y2="170" stroke="currentColor" stroke-dasharray="3,3" stroke-width="1"/>
  <text x="38" y="105" font-size="12" fill="currentColor" text-anchor="end">d</text>
  <!-- Needle -->
  <line x1="120" y1="130" x2="220" y2="70" stroke="currentColor" stroke-width="2.5"/>
  <!-- Center point -->
  <circle cx="170" cy="100" r="3" fill="currentColor"/>
  <!-- Nearest line vertical distance X -->
  <line x1="170" y1="100" x2="170" y2="30" stroke="currentColor" stroke-dasharray="2,2" stroke-width="1.2"/>
  <text x="175" y="65" font-size="12" fill="currentColor">X</text>
  <!-- Angle theta reference -->
  <line x1="170" y1="100" x2="230" y2="100" stroke="currentColor" stroke-dasharray="2,2" stroke-width="1"/>
  <path d="M 195 100 A 25 25 0 0 0 191 87" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="202" y="93" font-size="12" fill="currentColor">$\Theta$</text>
  <!-- Half-needle vertical projection -->
  <line x1="220" y1="100" x2="220" y2="70" stroke="currentColor" stroke-width="1.2"/>
  <text x="225" y="88" font-size="11" fill="currentColor">$\frac{\ell}{2}\sin\Theta$</text>
</svg>
<figcaption>Buffon's needle geometry. The midpoint is at distance $X$ from the nearest line, forming an acute angle $\Theta$ with the horizontal.</figcaption>
</figure>

### The Probabilistic Model

We describe the outcome by two variables:
1. $X$: the vertical distance from the center of the needle to the nearest line. The nearest line cannot be farther than half the total line spacing, so $X \in [0, d/2]$.
2. $\Theta$: the acute angle formed by the needle with the parallel lines, so $\Theta \in [0, \pi/2]$.

Lacking any preferred position or orientation, we model $X$ and $\Theta$ as uniform, independent random variables:
* $X \sim \text{Uniform}[0, d/2] \implies f_X(x) = \frac{1}{d/2} = \frac{2}{d}$, for $x \in [0, d/2]$.
* $\Theta \sim \text{Uniform}[0, \pi/2] \implies f_\Theta(\theta) = \frac{1}{\pi/2} = \frac{2}{\pi}$, for $\theta \in [0, \pi/2]$.

By independence, their joint PDF is the product of their individual PDFs:

$$f_{X,\Theta}(x, \theta) = f_X(x) f_\Theta(\theta) = \frac{4}{\pi d}, \quad 0 \le x \le \frac{d}{2}, \; 0 \le \theta \le \frac{\pi}{2}$$

### Intersection Condition and Calculation

From the midpoint of the needle, each tip extends vertically by a distance of:

$$\frac{\ell}{2} \sin \Theta$$

The needle intersects the nearest line if and only if the vertical distance from the center to that line is less than or equal to this vertical reach:

$$X \le \frac{\ell}{2} \sin \Theta$$

The probability of an intersection is obtained by integrating the joint density over this event:

$$\begin{aligned}
\mathbf{P}\left(X \le \frac{\ell}{2} \sin \Theta\right) &= \int_0^{\pi/2} \int_0^{(\ell/2)\sin\theta} f_{X,\Theta}(x, \theta) \, dx \, d\theta \\
&= \frac{4}{\pi d} \int_0^{\pi/2} \left[ \int_0^{(\ell/2)\sin\theta} dx \right] d\theta \\
&= \frac{4}{\pi d} \int_0^{\pi/2} \frac{\ell}{2} \sin \theta \, d\theta \\
&= \frac{2\ell}{\pi d} \left[ -\cos \theta \right]_0^{\pi/2} \\
&= \frac{2\ell}{\pi d} (0 - (-1)) = \frac{2\ell}{\pi d}
\end{aligned}$$

This result provides an experimental mechanism for estimating $\pi$: by choosing known lengths $\ell$ and $d$ (such as $d = 2\ell$, where the intersection probability becomes $1/\pi$), dropping needles repeatedly, and recording the empirical proportion of intersections, one can infer $\pi$. More generally, this illustrates the Monte Carlo method: evaluating complex or multi-dimensional integrals by estimating probabilities through simulated random samples.

## Conditional PDFs

When conditioning on an event involving continuous random variables, subtleties arise because the probability of an exact value $\{Y = y\}$ is zero.

### Definition and Meaning

To motivate conditioning on $Y = y$, consider the conditional probability that $X$ lies in a small interval $[x, x + \delta]$ given that $Y$ lies within an infinitesimal band $[y, y + \epsilon]$:

$$\mathbf{P}(x \le X \le x + \delta \mid y \le Y \le y + \epsilon) = \frac{\mathbf{P}(x \le X \le x + \delta, \; y \le Y \le y + \epsilon)}{\mathbf{P}(y \le Y \le y + \epsilon)} \approx \frac{f_{X,Y}(x, y) \cdot \delta \epsilon}{f_Y(y) \cdot \epsilon} = \frac{f_{X,Y}(x, y)}{f_Y(y)} \cdot \delta$$

Letting $\epsilon \to 0$, we define the conditional probability density function of $X$ given $Y = y$ as:

$$f_{X|Y}(x \mid y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}, \quad \text{for } y \text{ such that } f_Y(y) > 0$$

Under this definition:

$$\mathbf{P}(x \le X \le x + \delta \mid Y \approx y) \approx f_{X|Y}(x \mid y) \cdot \delta$$

This matches the form of the discrete conditional PMF $p_{X|Y}(x \mid y) = p_{X,Y}(x, y)/p_Y(y)$. If $X$ and $Y$ are independent, $f_{X,Y}(x, y) = f_X(x) f_Y(y)$, which immediately gives:

$$f_{X|Y}(x \mid y) = \frac{f_X(x) f_Y(y)}{f_Y(y)} = f_X(x)$$

Conditioning on $Y = y$ provides no information about $X$.

### Geometric Interpretation: Slicing and Normalizing

Fixing $Y = y$ in the joint density $f_{X,Y}(x, y)$ takes a cross-sectional "slice" of the joint surface along the line $Y = y$. 

The shape of $f_{X|Y}(x \mid y)$ as a function of $x$ is identical to this cross-sectional slice. However, a slice of a joint PDF is not directly a PDF because its integral with respect to $x$ is the marginal density $f_Y(y)$, which is generally not equal to 1:

$$\int_{-\infty}^\infty f_{X,Y}(x, y) \, dx = f_Y(y)$$

Dividing by $f_Y(y)$ renormalizes the slice so that the area under the conditional curve equals 1:

$$\int_{-\infty}^\infty f_{X|Y}(x \mid y) \, dx = \int_{-\infty}^\infty \frac{f_{X,Y}(x, y)}{f_Y(y)} \, dx = \frac{1}{f_Y(y)} \int_{-\infty}^\infty f_{X,Y}(x, y) \, dx = \frac{f_Y(y)}{f_Y(y)} = 1$$

## Example: Sequential Stick-Breaking

A stick of length $\ell$ is broken at a point $X$ distributed uniformly along its length. The remaining piece, which has length $X$, is then broken at a second point $Y$ distributed uniformly on $[0, X]$.

### Setting Up the Densities

The initial break $X$ is uniform on $[0, \ell]$:

$$f_X(x) = \frac{1}{\ell}, \quad 0 \le x \le \ell$$

Given that the first break occurs at $X = x$, the second break $Y$ is uniform on $[0, x]$:

$$f_{Y|X}(y \mid x) = \frac{1}{x}, \quad 0 \le y \le x$$

Using the multiplication rule $f_{X,Y}(x, y) = f_X(x) f_{Y|X}(y \mid x)$, the joint PDF is:

$$f_{X,Y}(x, y) = \frac{1}{\ell x}, \quad 0 \le y \le x \le \ell$$

and $f_{X,Y}(x, y) = 0$ everywhere else.

<figure>
<svg viewBox="0 0 280 230" role="img" aria-label="Support region for the stick breaking example: a triangle defined by 0 ≤ y ≤ x ≤ l">
  <!-- Axes -->
  <line x1="40" y1="180" x2="240" y2="180" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="180" x2="40" y2="20" stroke="currentColor" stroke-width="1.5"/>
  <text x="245" y="184" font-size="12" fill="currentColor">x</text>
  <text x="36" y="15" font-size="12" fill="currentColor">y</text>
  <!-- Region 0 ≤ y ≤ x ≤ l -->
  <polygon points="40,180 200,180 200,20" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <!-- Boundary lines -->
  <line x1="40" y1="180" x2="200" y2="20" stroke="currentColor" stroke-dasharray="3,3" stroke-width="1"/>
  <text x="130" y="80" font-size="12" fill="currentColor">y = x</text>
  <line x1="200" y1="180" x2="200" y2="20" stroke="currentColor" stroke-width="1"/>
  <text x="200" y="195" font-size="12" fill="currentColor" text-anchor="middle">$\ell$</text>
  <text x="30" y="25" font-size="12" fill="currentColor" text-anchor="end">$\ell$</text>
  <!-- Integration strip for marginal f_Y(y) -->
  <line x1="100" y1="120" x2="200" y2="120" stroke="currentColor" stroke-width="2"/>
  <circle cx="100" cy="120" r="2.5" fill="currentColor"/>
  <text x="105" y="112" font-size="11" fill="currentColor">integrate $x$ from $y$ to $\ell$</text>
  <text x="30" y="124" font-size="12" fill="currentColor" text-anchor="end">y</text>
</svg>
<figcaption>The triangular region of positive joint density $0 \le y \le x \le \ell$. To compute the marginal density $f_Y(y)$, integrate $x$ horizontally from the boundary line $x = y$ to $x = \ell$.</figcaption>
</figure>

### Conditional Expectation

The conditional expectation of $Y$ given $X = x$ is calculated directly from the conditional density:

$$\mathbf{E}[Y \mid X = x] = \int_{-\infty}^\infty y f_{Y|X}(y \mid x) \, dy = \int_0^x y \left( \frac{1}{x} \right) dy = \left[ \frac{y^2}{2x} \right]_0^x = \frac{x}{2}$$

Because $Y$ is uniformly distributed on $[0, x]$, its expected value is the midpoint of the interval.

### Finding the Marginal Density $f_Y(y)$

To find the marginal density $f_Y(y)$ of the length of the remaining piece, integrate out $x$. For a fixed $y \in [0, \ell]$, the joint density is non-zero only where $x \ge y$ and $x \le \ell$:

$$\begin{aligned}
f_Y(y) &= \int_{-\infty}^\infty f_{X,Y}(x, y) \, dx \\
&= \int_y^\ell \frac{1}{\ell x} \, dx \\
&= \frac{1}{\ell} \Big[ \ln x \Big]_y^\ell \\
&= \frac{1}{\ell} (\ln \ell - \ln y) \\
&= \frac{1}{\ell} \ln\left(\frac{\ell}{y}\right), \quad 0 < y \le \ell
\end{aligned}$$

As $y \to 0$, $f_Y(y) \to \infty$; the density diverges logarithmically, though the area under the curve remains finite and integrates to 1.

### Calculating $\mathbf{E}[Y]$

We evaluate the expected value of $Y$ directly from its marginal PDF:

$$\mathbf{E}[Y] = \int_0^\ell y f_Y(y) \, dy = \int_0^\ell y \cdot \frac{1}{\ell} \ln\left(\frac{\ell}{y}\right) dy$$

Using integration by parts, set $u = \ln(\ell/y)$ and $dv = y \, dy$, so $du = -1/y \, dy$ and $v = y^2/2$:

$$\begin{aligned}
\mathbf{E}[Y] &= \frac{1}{\ell} \left( \left[ \frac{y^2}{2} \ln\left(\frac{\ell}{y}\right) \right]_0^\ell - \int_0^\ell \frac{y^2}{2} \left(-\frac{1}{y}\right) dy \right) \\
&= \frac{1}{\ell} \left( 0 + \frac{1}{2} \int_0^\ell y \, dy \right) \\
&= \frac{1}{\ell} \cdot \frac{1}{2} \left[ \frac{y^2}{2} \right]_0^\ell = \frac{1}{\ell} \cdot \frac{\ell^2}{4} = \frac{\ell}{4}
\end{aligned}$$

This aligns with intuition: on average, the first break bisects the original stick ($\mathbf{E}[X] = \ell/2$), and the second break bisects the remaining piece on average ($\mathbf{E}[Y \mid X = x] = x/2$), giving an overall expected length of $\ell/4$.

---

## Exercises

### Exercise 1
Random variable $X$ is uniformly distributed between $-1.0$ and $1.0$. Let $X_1, X_2, \dots$ be independent and identically distributed random variables with the same distribution as $X$. Determine which, if any, of the following sequences (all with $i = 1, 2, \dots$) are convergent in probability. Fully justify your answers, including limits if they exist.
1. $U_i = \frac{X_1 + X_2 + \dots + X_i}{i}$
2. $W_i = \max(X_1, \dots, X_i)$
3. $V_i = X_1 \cdot X_2 \cdot \dots \cdot X_i$

### Exercise 2
Demonstrate that the Chebyshev inequality is tight: for every $\mu$, $\sigma > 0$, and $c \ge \sigma$, construct a random variable $X$ with mean $\mu$ and standard deviation $\sigma$ such that:
$$\mathbf{P}(|X - \mu| \ge c) = \frac{\sigma^2}{c^2}$$
*(Hint: Use a discrete random variable that takes on 3 distinct values with nonzero probability.)*

### Exercise 3
Show the one-sided Chebyshev inequality:
$$\mathbf{P}(X - \mu \ge a) \le \frac{\sigma^2}{\sigma^2 + a^2}$$
where $\mu$ and $\sigma^2$ are the mean and variance of $X$, respectively, and $a > 0$. *(Hint: Consider $\mathbf{P}(X - \mu + c \ge a + c)$ for $c \ge 0$, and optimize over $c$.)*

### Exercise 4
Let $X$ and $Y$ have a joint PDF that is uniform over the triangle with vertices $(0, 0)$, $(0, 1)$, and $(1, 0)$.
1. Find the joint PDF $f_{X,Y}(x, y)$.
2. Find the marginal PDF $f_Y(y)$.
3. Find the conditional PDF $f_{X|Y}(x \mid y)$.
4. Compute $\mathbf{E}[X \mid Y = y]$, and use the total expectation theorem to express $\mathbf{E}[X]$ in terms of $\mathbf{E}[Y]$.
5. Use symmetry to determine the value of $\mathbf{E}[X]$.

### Exercise 5
We break a stick of unit length into three pieces by choosing two break points independently and uniformly along the stick. What is the probability that the three resulting segments can form a triangle?

### Exercise 6
Let $X$ be an exponential random variable with parameter $\lambda > 0$.
1. Calculate the probability that $X$ falls inside one of the intervals $[n, n + 1]$ for odd integers $n$.
2. Let $T$ be an exponential random variable with parameter $\lambda$ representing light bulb lifetime. Given $A = \{T > t\}$, find the conditional CDF of the remaining lifetime $X = T - t$.

---

## Sources

* **Lecture slides (Lecture 9):** Concept comparison table (PMF/PDF), joint PDF definition, infinitesimal square interpretation, marginalization integrals, continuous independence definition, Buffon's needle model and derivation, conditional PDF formula, and stick-breaking example formulation.
* **Lecture transcript (Lecture 9):** Geometric intuition of probability mass as volume under a surface, infinitesimal strip argument for marginalization, physical setup and historical context of Buffon's needle, the link to Monte Carlo integration, slice-and-normalize intuition for conditional densities, and sequential stick-breaking derivations.
* **Recitation 9 / Homework 9 problem sets:** Exercises on uniform triangular distributions, stick-breaking into three pieces, exponential distribution properties, Chebyshev bounds, and convergence in probability.

Solutions: [chapter 9](solutions/09-joint-and-conditional-continuous-densities.md)


---

[← 8. Continuous Random Variables and the Normal Distribution](08-continuous-random-variables-and-the-normal-distribution.md) · [Contents](index.md) · [10. Derived Distributions and Bayesian Inference →](10-derived-distributions-and-bayesian-inference.md)
