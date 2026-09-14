---
title: Integrals
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/measure-theory-basics.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/measure-theory-basics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Integrals

**Source:** [`reader/measure-theory-basics.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/measure-theory-basics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

One very nice thing about measures is that they let us define integrals of (nice enough) real-valued functions on $\cX$ with respect to the measure $\mu$, meaning the integral is "weighted" in a way that assigns total weight $\mu(A)$ to each set $A$. We will use the notation $\int f(x)\,\td\mu(x)$, or just $\int f \td\mu$.

To construct this integral, we begin by defining it for indicator functions, and then extend to more general functions by linearity and limits, in a few steps:

First, for an indicator function $1_A(x) = 1\{x \in A\}$ of a set $A \in \cF$, it is straightforward to define the integral as $\int 1_A \td\mu = \mu(A)$ (note if $A \notin \cF$ this does not work, but we are only defining the integral for a class of "nice" functions determined by our $\sigma$-field)

Next, consider a *simple function* $f(x) = \sum_{i=1}^\infty c_i 1_{A_i}(x)$, with all $c_i \geq 0$ and $A_i \in \cF$. Because the integral should be linear, we should have

$$
\int f\td\mu = \sum_{i=1}^\infty c_i \int 1_{A_i}\td\mu = \sum_{i=1}^\infty c_i \mu(A_i)
$$

Third, we can extend to all sufficiently nice non-negative functions by approximating them from below with a series of simple functions:

$$
\int f\td\mu = \lim_{i=1}^\infty \int f_i\td\mu.
$$

This idea is illustrated in the picture below:

![Approximating a non-negative function from below by a series of simple (piecewise constant) functions. The red function is an indicator, the blue function is a simple function, and the dashed orange function is a simple function that approximates the orange curve.](https://raw.githubusercontent.com/berkeley-stat210a/fall-2024/812543bde50398a54db3044bf8ba7120189a4dfa/reader/images/Screenshot%202023-08-23%20at%2011.16.18%20PM.png)

Finally, we can write any real-valued function as the sum of its positive and negative parts, $f(x) = f^+(x) - f^-(x)$, where $f^+(x) = \max\{f(x), 0\}$ and $f^-(x) = \max\{-f(x), 0\}$. Then both $f^+$ and $f^-$ have non-negative (possibly infinite) integrals. Then we simply take

$$
\int f\td\mu = \int f^+\td\mu - \int f^-\td\mu \in [-\infty, \infty],
$$

calling the difference undefined if the integrals of both $f^+$ and $f^-$ are infinite.

As a result, we have $\int f\td\mu$ for any function $f$ whose positive and negative parts can both be approximated from below by simple functions. Note that we have left out some important details in this presentation (for example we have not characterized which functions $f$ are nice enough to be approximated well by simple functions) but these details are unimportant for this class. The important thing to know is that to any measure $\mu$ there corresponds a well-defined integral $\int \cdot \td\mu$, which behaves as we would expect it to.

We can now return to our previous examples of measures and ask what the corresponding integrals are:

**Example 1, continued (Counting measure):** An integral with respect to $\#$ just adds up all the values of $f(x)$:

$$
\int f\td\# = \sum_{x\in \cX} f(x)
$$

**Example 2, continued (Lebesgue measure):** An integral with respect to the Lebesgue measure is called a *Lebesgue integral*, which is essentially just the usual integral you are used to from calculus class:

$$
\int f\td\lambda = \int\cdots \int f(x) \td x_1 \cdots \td x_n.
$$

The Lebesgue integral extends the Riemann integral to a more general class of functions, in the sense that if the Riemann integral of $f$ is defined then the Lebesgue integral is also well defined and the two integrals coincide. But the Lebesgue integral is also well-defined for functions like $f(x) = 1\{x \in \mathbb{Q}\}$, for which the Riemann integral is not well-defined (**Exercise:** what is the Lebesgue integral of $1\{x \in \mathbb{Q}\}$?)

**Example 3, continued (Gaussian measure):** Note that $P_Z(A)$ is defined as the (Lebesgue) integral of $1_A(x)\phi(x)$. By extension, the integral of $f$ with respect to $P_Z$ is the Lebesgue integral of $f(x) \phi(x)$, which is nothing more than the expectation of $f(Z)$:

$$
\int f\td P_Z = \int_{-\infty}^\infty f(x) \phi(x) \td x = \EE[f(Z)].
$$

---

[← Measures](02-measures.md) · [Up: contents](index.md) · [Densities →](04-densities.md)
