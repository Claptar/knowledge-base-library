---
title: 4. Convergence ideas
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Convergence ideas

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

## Convergence metrics

We might choose to assess whether $f^{\prime}(x_{t})$ is near zero,
which should assure that we have reached the critical point. However, in
parts of the domain where $f(x)$ is fairly flat, we may find the
derivative is near zero even though we are far from the optimum.
Instead, we generally monitor $|x_{t+1}-x_{t}|$ (for the moment, assume
$x$ is scalar). We might consider absolute convergence:
$|x_{t+1}-x_{t}|<\epsilon$ or relative convergence,
$\frac{|x_{t+1}-x_{t}|}{|x_{t}|}<\epsilon$. Relative convergence is
appealing because it accounts for the scale of $x$, but it can run into
problems when $x_{t}$ is near zero, in which case one can use
$\frac{|x_{t+1}-x_{t}|}{|x_{t}|+\epsilon}<\epsilon$. We would want to
account for machine precision in thinking about setting $\epsilon$. For
relative convergence a reasonable choice of $\epsilon$ would be to use
the square root of machine epsilon or about $1\times10^{-8}$.

Problems with the optimization may show up in a convergence measure that
fails to decrease or cycles (oscillates). Software generally has a
stopping rule that stops the algorithm after a fixed number of
iterations; these can generally be changed by the user. When an
algorithm stops because of the stopping rule before the convergence
criterion is met, we say the algorithm has failed to converge. Sometimes
we just need to run it longer, but often it indicates a problem with the
function being optimized or with your starting value.

For multivariate optimization, we use a distance metric between
$x_{t+1}$ and $x_{t}$, such as $\|x_{t+1}-x_{t}\|_{p}$ , often with
$p=1$ or $p=2$.

## Starting values

Good starting values are important because they can improve the speed of
optimization, prevent divergence or cycling, and prevent finding local
optima.

Using random or selected multiple starting values can help with multiple
optima (aka multimodality).

Here's a function (the Rastrigin function) with multiple optima that is
commonly used for testing methods that claim to work well for multimodal
problems. This is a hard function to optimize with respect to,
particularly in higher dimensions (one can do it in higher dimensions
than 2 by simply making the $x$ vector longer but having the same
structure). In particular Rastrigin with 30 dimensions is considered to
be very hard.

```python
def rastrigin(x):
    A = 10
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

const = 5.12
nGrid = 100
gr = np.linspace(-const, const, num=nGrid)

---

[← Define the second derivative](07-define-the-second-derivative.md) · [Up: contents](index.md) · [Create a grid of x values →](09-create-a-grid-of-x-values.md)
