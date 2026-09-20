---
title: "12. Iterated Expectations and Total Variance"
course: "MIT 6.041SC"
chapter: 12
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 12. Iterated Expectations and Total Variance

## What this covers

This chapter covers conditional expectations and conditional variances viewed as random variables in their own right, rather than as single numbers. It introduces the law of iterated expectations and the law of total variance, and applies them to analyze sums of a random number of independent random variables. It assumes familiarity with basic conditioning, discrete and continuous expectations, and the standard formulas for variance and independence.

## Conditional Expectation as a Random Variable

For two discrete random variables $X$ and $Y$, the conditional expectation of $X$ given that $Y = y$ is defined by
$$E[X \mid Y = y] = \sum_x x \, p_{X \mid Y}(x \mid y)$$
In the continuous case, the sum is replaced by an integral involving the conditional probability density function $f_{X \mid Y}(x \mid y)$.

In either setting, once a specific numerical value $y$ is supplied, $E[X \mid Y = y]$ is simply a fixed number. For example, consider a stick of length $\ell$. Suppose we break the stick at a point $Y$ chosen uniformly at random along its length:
$$Y \sim \text{Uniform}(0, \ell)$$
Having broken the stick at $Y$, we take the remaining left piece (of length $Y$) and break it again at a location $X$ chosen uniformly at random between $0$ and $Y$. If we are told that $Y$ took a specific numerical value $y$, then $X$ is distributed uniformly on $[0, y]$. Its conditional expectation is the midpoint:
$$E[X \mid Y = y] = \frac{y}{2}$$
This is an equality between two real numbers.

However, before the experiment is run, we do not know what numerical value $Y$ will take. The value of $E[X \mid Y = y]$ depends directly on the realization of $Y$. We can therefore view the conditional expectation as an abstract object prior to the experiment: a random variable whose numerical value is determined by the outcome of $Y$. 

We denote this random variable by $E[X \mid Y]$. Formally, $E[X \mid Y]$ is a function of the random variable $Y$, say $g(Y)$, where the function $g$ is defined by:
$$g(y) = E[X \mid Y = y]$$
Whenever $Y$ takes the value $y$, the random variable $E[X \mid Y]$ takes the numerical value $g(y)$. In the stick-breaking example, this relation is expressed directly as an equality of random variables:
$$E[X \mid Y] = \frac{Y}{2}$$

## The Law of Iterated Expectations

Because $E[X \mid Y]$ is a random variable, it possesses an expectation of its own. To compute $E\bigl[E[X \mid Y]\bigr]$, we apply the expected value rule to the function $g(Y)$:
$$E\bigl[E[X \mid Y]\bigr] = E[g(Y)] = \sum_y g(y) \, p_Y(y) = \sum_y E[X \mid Y = y] \, p_Y(y)$$
This summation is precisely the total expectation theorem: to obtain the overall expectation of $X$, we weight the conditional expectations across each possible scenario $Y = y$ by the probability of that scenario. Hence:
$$E\bigl[E[X \mid Y]\bigr] = E[X]$$
This identity is the **law of iterated expectations**. It states that the average of the conditional expectation is the unconditional expectation.

Returning to the stick-breaking process, we find the overall expected length of the remaining piece $X$ without computing joint densities or multi-dimensional integrals:
$$E[X] = E\bigl[E[X \mid Y]\bigr] = E\left[\frac{Y}{2}\right] = \frac{1}{2} E[Y] = \frac{1}{2} \cdot \frac{\ell}{2} = \frac{\ell}{4}$$

## Conditional Variance and the Law of Total Variance

Just as the conditional distribution of $X$ given $Y = y$ has a mean, it also has a variance. For a fixed numerical value $y$, the conditional variance is defined as the expected squared deviation from the conditional mean, computed entirely within the conditional universe:
$$\text{var}(X \mid Y = y) = E\left[ (X - E[X \mid Y = y])^2 \;\middle|\; Y = y \right]$$
Like the conditional expectation, once $y$ is specified, $\text{var}(X \mid Y = y)$ is a fixed number. 

Before the experiment is carried out, the realization of $Y$ is unknown. We therefore define the **conditional variance** $\text{var}(X \mid Y)$ as a random variable that takes the numerical value $\text{var}(X \mid Y = y)$ whenever $Y$ takes the value $y$. It is a function of $Y$.

One might wonder whether taking the expectation of this conditional variance yields the unconditional variance $\text{var}(X)$. It does not. The true relationship requires an additional term accounting for the spread of the conditional means themselves.

### The Law of Total Variance
$$\text{var}(X) = E[\text{var}(X \mid Y)] + \text{var}(E[X \mid Y])$$

### Proof
Recall the standard variance formula for any random variable $W$:
$$\text{var}(W) = E[W^2] - (E[W])^2$$

Because this is a general property of variance, it holds within any conditional universe given $Y$:
$$\text{var}(X \mid Y) = E[X^2 \mid Y] - (E[X \mid Y])^2 \tag{a}$$

Now, take the expectation of both sides of equation (a) with respect to $Y$. Applying the law of iterated expectations to the first term on the right-hand side, $E\bigl[E[X^2 \mid Y]\bigr] = E[X^2]$, we get:
$$E[\text{var}(X \mid Y)] = E[X^2] - E\left[(E[X \mid Y])^2\right] \tag{b}$$

Next, consider the second term of the total variance formula: the variance of the random variable $E[X \mid Y]$. Applying the standard variance formula directly to $W = E[X \mid Y]$ gives:
$$\text{var}(E[X \mid Y]) = E\left[(E[X \mid Y])^2\right] - \left(E\bigl[E[X \mid Y]\bigr]\right)^2$$
By the law of iterated expectations, $E\bigl[E[X \mid Y]\bigr] = E[X]$, so:
$$\text{var}(E[X \mid Y]) = E\left[(E[X \mid Y])^2\right] - (E[X])^2 \tag{c}$$

Adding equations (b) and (c), the terms $E\left[(E[X \mid Y])^2\right]$ cancel:
$$E[\text{var}(X \mid Y)] + \text{var}(E[X \mid Y]) = E[X^2] - (E[X])^2 = \text{var}(X)$$
which completes the derivation.

## Decomposing Variance: Within-Group and Between-Group Variation

The two components of the total variance law have a clear physical interpretation:
$$\text{var}(X) = \underbrace{E[\text{var}(X \mid Y)]}_{\text{average variability within groups}} + \underbrace{\text{var}(E[X \mid Y])}_{\text{variability between groups}}$$

Consider a class divided into two quiz sections:
* Section $1$ ($y = 1$): contains $10$ students; section mean is $90$; section variance is $10$.
* Section $2$ ($y = 2$): contains $20$ students; section mean is $60$; section variance is $20$.

A student is chosen uniformly at random from the $30$ total students. Let $X$ be the quiz score of the selected student, and let $Y$ be the student's section number.

Because each student is chosen with equal probability, the probability of selecting someone from section $1$ is $10/30 = 1/3$, and from section $2$ is $20/30 = 2/3$.

### Iterated Expectations on the Sections
The conditional expectations for each section are:
$$E[X \mid Y = 1] = 90, \quad E[X \mid Y = 2] = 60$$
As a random variable, $E[X \mid Y]$ has the distribution:
$$E[X \mid Y] = \begin{cases} 90, & \text{with probability } 1/3 \\ 60, & \text{with probability } 2/3 \end{cases}$$
The expectation of this random variable yields the overall average score:
$$E[E[X \mid Y]] = \frac{1}{3}(90) + \frac{2}{3}(60) = 30 + 40 = 70 = E[X]$$

The variance of this conditional expectation captures how widely the section averages fluctuate around the overall class mean of $70$:
$$\text{var}(E[X \mid Y]) = \frac{1}{3}(90 - 70)^2 + \frac{2}{3}(60 - 70)^2 = \frac{1}{3}(400) + \frac{2}{3}(100) = \frac{600}{3} = 200$$

### Total Variance across the Sections
The conditional variances within each section are:
$$\text{var}(X \mid Y = 1) = 10, \quad \text{var}(X \mid Y = 2) = 20$$
As a random variable, $\text{var}(X \mid Y)$ takes values:
$$\text{var}(X \mid Y) = \begin{cases} 10, & \text{with probability } 1/3 \\ 20, & \text{with probability } 2/3 \end{cases}$$
Its expected value is the average within-section variance:
$$E[\text{var}(X \mid Y)] = \frac{1}{3}(10) + \frac{2}{3}(20) = \frac{50}{3}$$

Combining both components via the law of total variance gives:
$$\text{var}(X) = E[\text{var}(X \mid Y)] + \text{var}(E[X \mid Y]) = \frac{50}{3} + 200 = 216\frac{2}{3}$$
The total variance $216\frac{2}{3}$ reflects both the spread of individual student scores around their respective section averages ($50/3$) and the substantial gap between the two section averages ($200$).

<figure>
<svg viewBox="0 0 420 180" role="img" aria-label="Points representing quiz scores clustered within two sections, illustrating within-section and between-section spread.">
  <line x1="40" y1="50" x2="380" y2="50" stroke="currentColor" stroke-width="1.5"/>
  <line x1="40" y1="130" x2="380" y2="130" stroke="currentColor" stroke-width="1.5"/>
  <!-- Section 1 (mean 90, spread small) -->
  <line x1="320" y1="40" x2="320" y2="60" stroke="currentColor" stroke-width="2"/>
  <rect x="290" y="42" width="60" height="16" fill="currentColor" fill-opacity="0.15"/>
  <circle cx="305" cy="50" r="3" fill="currentColor"/>
  <circle cx="320" cy="50" r="3" fill="currentColor"/>
  <circle cx="335" cy="50" r="3" fill="currentColor"/>
  <text x="320" y="32" text-anchor="middle" font-size="12" fill="currentColor">E[X|Y=1] = 90</text>
  <text x="45" y="45" font-size="12" fill="currentColor">Section 1</text>
  <!-- Section 2 (mean 60, spread moderate) -->
  <line x1="170" y1="120" x2="170" y2="140" stroke="currentColor" stroke-width="2"/>
  <rect x="130" y="122" width="80" height="16" fill="currentColor" fill-opacity="0.15"/>
  <circle cx="145" cy="130" r="3" fill="currentColor"/>
  <circle cx="170" cy="130" r="3" fill="currentColor"/>
  <circle cx="195" cy="130" r="3" fill="currentColor"/>
  <text x="170" y="112" text-anchor="middle" font-size="12" fill="currentColor">E[X|Y=2] = 60</text>
  <text x="45" y="125" font-size="12" fill="currentColor">Section 2</text>
  <!-- Overall class mean -->
  <line x1="220" y1="20" x2="220" y2="160" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="220" y="172" text-anchor="middle" font-size="12" fill="currentColor">E[X] = 70</text>
</svg>
<figcaption>Total variance is the sum of within-group spread (shaded intervals around each group mean) and between-group spread (the distance between section means and the overall mean).</figcaption>
</figure>

## Worked Example: Piecewise Uniform PDF

The law of total variance can also simplify variance calculations for continuous random variables by using a "divide and conquer" strategy. Suppose $X$ has a piecewise constant probability density function:
$$f_X(x) = \begin{cases} 1/3, & 0 \le x \le 1 \\ 2/3, & 1 < x \le 2 \\ 0, & \text{otherwise} \end{cases}$$

Rather than evaluating $\int x^2 f_X(x) \, dx$ directly, define an auxiliary indicator random variable:
$$Y = \begin{cases} 1, & \text{if } 0 \le X \le 1 \\ 2, & \text{if } 1 < X \le 2 \end{cases}$$
The marginal PMF of $Y$ is:
$$P(Y = 1) = \int_0^1 \frac{1}{3} \, dx = \frac{1}{3}, \quad P(Y = 2) = \int_1^2 \frac{2}{3} \, dx = \frac{2}{3}$$

Conditional on each interval, $X$ is uniformly distributed:
* Given $Y = 1$: $X \sim \text{Uniform}(0, 1)$, so $E[X \mid Y = 1] = 1/2$.
* Given $Y = 2$: $X \sim \text{Uniform}(1, 2)$, so $E[X \mid Y = 2] = 3/2$.

The overall expectation is:
$$E[X] = E\bigl[E[X \mid Y]\bigr] = \frac{1}{3}\left(\frac{1}{2}\right) + \frac{2}{3}\left(\frac{3}{2}\right) = \frac{1}{6} + \frac{6}{6} = \frac{7}{6}$$

The variance of a continuous uniform random variable on an interval of unit length is $1/12$. Therefore:
$$\text{var}(X \mid Y = 1) = \frac{1}{12}, \quad \text{var}(X \mid Y = 2) = \frac{1}{12}$$
Because $\text{var}(X \mid Y)$ takes the constant value $1/12$ in all scenarios, its expectation is simply:
$$E[\text{var}(X \mid Y)] = \frac{1}{12}$$

Now compute the variance of the conditional mean:
$$\text{var}(E[X \mid Y]) = \frac{1}{3}\left(\frac{1}{2} - \frac{7}{6}\right)^2 + \frac{2}{3}\left(\frac{3}{2} - \frac{7}{6}\right)^2$$
Since $\frac{1}{2} - \frac{7}{6} = -\frac{4}{6} = -\frac{2}{3}$ and $\frac{3}{2} - \frac{7}{6} = \frac{2}{6} = \frac{1}{3}$:
$$\text{var}(E[X \mid Y]) = \frac{1}{3}\left(-\frac{2}{3}\right)^2 + \frac{2}{3}\left(\frac{1}{3}\right)^2 = \frac{1}{3}\left(\frac{4}{9}\right) + \frac{2}{3}\left(\frac{1}{9}\right) = \frac{6}{27} = \frac{2}{9}$$

By the law of total variance:
$$\text{var}(X) = E[\text{var}(X \mid Y)] + \text{var}(E[X \mid Y]) = \frac{1}{12} + \frac{2}{9} = \frac{3}{36} + \frac{8}{36} = \frac{11}{36}$$

## Sum of a Random Number of Independent Random Variables

Consider a shopper visiting a random number of stores $N$, where $N$ is a nonnegative integer-valued random variable. Let $X_i$ be the amount of money spent in store $i$. We assume:
1. The $X_i$ are independent and identically distributed (i.i.d.) with common mean $E[X]$ and variance $\text{var}(X)$.
2. The sequence $\{X_1, X_2, \dots\}$ is independent of the number of stores $N$.

Let $Y$ be the total money spent across all visited stores:
$$Y = \sum_{i=1}^N X_i$$
Here, both the individual terms $X_i$ and the number of terms $N$ are random.

### Mean of the Random Sum
Condition on the event that $N$ takes a fixed value $n$:
$$E[Y \mid N = n] = E\left[\sum_{i=1}^n X_i \;\middle|\; N = n\right]$$
Because $N$ is independent of the $X_i$, conditioning on $N = n$ does not alter their distributions:
$$E\left[\sum_{i=1}^n X_i \;\middle|\; N = n\right] = E\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n E[X_i] = n E[X]$$

Translating this numerical statement into a statement about random variables:
$$E[Y \mid N] = N E[X]$$
Applying the law of iterated expectations:
$$E[Y] = E\bigl[E[Y \mid N]\bigr] = E\bigl[N E[X]\bigr]$$
Since $E[X]$ is a fixed constant, it factors out of the expectation:
$$E[Y] = E[N] E[X]$$

The expected total expenditure is simply the expected number of stores multiplied by the expected spending per store.

### Variance of the Random Sum
To find $\text{var}(Y)$, apply the law of total variance conditioning on $N$:
$$\text{var}(Y) = E[\text{var}(Y \mid N)] + \text{var}(E[Y \mid N])$$

We evaluate each term separately:

1. **Second term ($\text{var}(E[Y \mid N])$):**
   Using $E[Y \mid N] = N E[X]$, where $E[X]$ is a constant, scaling rules for variance give:
   $$\text{var}(E[Y \mid N]) = \text{var}(N E[X]) = (E[X])^2 \text{var}(N)$$
   This term represents the variability in total expenditure caused by fluctuations in the number of stores visited.

2. **First term ($E[\text{var}(Y \mid N)])$:**
   For a fixed number of stores $n$, $Y$ is the sum of $n$ independent random variables, each with variance $\text{var}(X)$. Hence:
   $$\text{var}(Y \mid N = n) = \text{var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{var}(X_i) = n \text{var}(X)$$
   In terms of random variables:
   $$\text{var}(Y \mid N) = N \text{var}(X)$$
   Taking expectations on both sides (noting that $\text{var}(X)$ is a constant):
   $$E[\text{var}(Y \mid N)] = E[N \text{var}(X)] = E[N] \text{var}(X)$$
   This term represents the expected contribution of spending fluctuations within individual stores.

Combining both pieces yields:
$$\text{var}(Y) = E[N] \text{var}(X) + (E[X])^2 \text{var}(N)$$

## Exercises

1. Show that for any two random variables $X$ and $Y$ and any constants $a > 0$ and $b$, the correlation coefficient satisfies $\rho(aX + b, Y) = \rho(X, Y)$.

2. Romeo and Juliet have a date at a scheduled time. Independently, each will arrive late by an amount of time distributed exponentially with parameter $\lambda$. Let $X$ and $Y$ denote the lateness of Romeo and Juliet, respectively.
   (a) Find the probability density function (PDF) of $Z = X - Y$ by first calculating the cumulative distribution function (CDF) and differentiating.
   (b) Find the PDF of $Z$ using the total probability theorem / conditioning.

3. Let $X$ and $Y$ be independent standard normal random variables. Represent the pair $(X, Y)$ in polar coordinates $(R, \Theta)$, with $R \ge 0$ and $\Theta \in [0, 2\pi)$, such that
   $$X = R \cos\Theta, \quad Y = R \sin\Theta$$
   Show that $R$ and $\Theta$ are independent by determining:
   (a) The marginal PDF $f_R(r)$.
   (b) The marginal PDF $f_\Theta(\theta)$.
   (c) The joint PDF $f_{R,\Theta}(r, \theta)$.

4. **Cauchy-Schwarz Inequality.** Prove that for any two random variables $X$ and $Y$,
   $$\left(E[XY]\right)^2 \le E[X^2] \, E[Y^2]$$

5. A biased coin is tossed $n$ times. The probability of obtaining heads on any given toss is $q$, which is the realization of a continuous random variable $Q$ with mean $\mu$ and positive variance $\sigma^2$. Let $X_i = 1$ if the $i$th toss results in heads, and $X_i = 0$ otherwise. Given $Q = q$, the variables $X_1, \dots, X_n$ are conditionally independent. Let $X = \sum_{i=1}^n X_i$ be the total number of heads.
   (a) Use the law of iterated expectations to determine $E[X_i]$ and $E[X]$.
   (b) Compute $\text{cov}(X_i, X_j)$ for $i \ne j$. Determine whether $X_1, \dots, X_n$ are independent.
   (c) Use the law of total variance to compute $\text{var}(X)$, and verify the result using the pairwise covariance from part (b).

## Sources

* `SLIDES: LECTURE 12`: Definitions of conditional expectation and conditional variance as random variables; statement and proof of the law of iterated expectations; statement and proof of the law of total variance; the two-section quiz score example; piecewise uniform example outline; sum of a random number of independent random variables formulas.
* `TRANSCRIPT: 12 captions`: Detailed derivations, intuitive explanations of between-group versus within-group variance, stick-breaking example details, and full algebraic calculations for the piecewise uniform and bookstore examples.
* `SLIDES: 12 slides Lec 12 —bonvid`: Problem statement for coin tosses with a random parameter $Q$ (Exercise 5).
* `PROBLEMS: 12 slides`: Recitation 12 problems (Exercises 1 through 4).

Solutions: [chapter 12](solutions/12-iterated-expectations-and-total-variance.md)


---

[← 11. Derived Distributions, Convolutions, and Covariance](11-derived-distributions-convolutions-and-covariance.md) · [Contents](index.md) · [13. The Bernoulli Process →](13-the-bernoulli-process.md)
