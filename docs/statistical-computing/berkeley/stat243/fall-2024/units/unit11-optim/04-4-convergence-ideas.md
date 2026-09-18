---
title: 4. Convergence ideas
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 4. Convergence ideas

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

# Create a grid of x values
x1, x2 = np.meshgrid(gr, gr)
xs = np.column_stack((x1.ravel(), x2.ravel()))

# Calculate the Rastrigin function for each point in the grid
y = np.apply_along_axis(rastrigin, 1, xs)

# Create a plot
plt.figure(figsize=(8, 6))
plt.imshow(y.reshape((nGrid, nGrid)), extent=[-const, const, -const, const], origin='lower', cmap='viridis')
plt.colorbar()
plt.title('Rastrigin Function')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
```

## Convergence rates

Let $\epsilon_{t}=|x_{t}-x^{*}|$. If the limit

$$\lim_{t\to\infty}\frac{|\epsilon_{t+1}|}{|\epsilon_{t}|^{\beta}}=c$$
exists for $\beta>0$ and $c\ne0$, then a method is said to have order of
convergence $\beta$. This basically measures how big the error at the
$t+1$th iteration is relative to that at the $t$th iteration, with the
approximation that $|\epsilon_{t+1}|\approx c|\epsilon_{t}|^{\beta}$.

Bisection doesn't formally satisfy the criterion needed to make use of
this definition, but roughly speaking it has linear convergence
($\beta=1$), so the magnitude of the error decreases by a factor of $c$
at each step. Next we'll see that N-R has quadratic convergence
($\beta=2$), which is fast.

To analyze convergence of N-R, we'll assume that $f^{\prime}(x)$ is twice continuously differentiable and consider a Taylor expansion of the
gradient at the minimum, $x^{*}$, around the current value, $x_{t}$:
$$f^{\prime}(x^{*})=f^{\prime}(x_{t})+(x^{*}-x_{t})f^{\prime\prime}(x_{t})+\frac{1}{2}(x^{*}-x_{t})^{2}f^{\prime\prime\prime}(\xi_{t})=0,$$
for some $\xi_{t}\in[x^{*},x_{t}]$. Making use of the N-R update
equation:
$x_{t+1}=x_{t}-\frac{f^{\prime}(x_{t})}{f^{\prime\prime}(x_{t})}$ to
substitute , and some algebra, we have
$$\frac{|\epsilon_{t+1}|}{|\epsilon_t|^{\beta}} = \frac{|x^{*}-x_{t+1}|}{(x^{*}-x_{t})^{2}}=\left| \frac{1}{2}\frac{f^{\prime\prime\prime}(\xi_{t})}{f^{\prime\prime}(x_{t})} \right|.$$
If the limit of the ratio on the right hand side exists (note the assumption of twice continuous differentiability) and is equal to
$c$:
$$c=\lim_{x_{t}\to x^{*}}\left|\frac{1}{2}\frac{f^{\prime\prime\prime}(\xi_{t})}{f^{\prime\prime}(x_{t})}\right|=\left|\frac{1}{2}\frac{f^{\prime\prime\prime}(x^{*})}{f^{\prime\prime}(x^{*})}\right|$$
then we see that $\beta=2$.

If $c$ were one, then we see that if we have $k$ digits of accuracy at
$t$, we'd have $2k$ digits at $t+1$ (e.g., $|\epsilon_{t}|=0.01$ results
in $|\epsilon_{t+1}|=0.0001$), which justifies the characterization of
quadratic convergence being fast. In practice $c$ will moderate the rate
of convergence. The smaller $c$ the better, so we'd like to have the
second derivative be large and the third derivative be small. The
expression also indicates we'll have a problem if
$f^{\prime\prime}(x_{t})=0$ at any point (think about what this
corresponds to graphically - what is our next step when
$f^{\prime\prime}(x_{t})=0$?). The characteristics of the derivatives
determine the domain of attraction (the region in which we'll converge
rather than diverge) of the minimum.

Givens and Hoeting show that using the secant-based approximation to the
second derivative in N-R has order of convergence, $\beta\approx1.62$.

Here's an example of convergence comparing bisection and N-R. First, Newton-Raphson:

```python
np.set_printoptions(precision=10)

# Define the original function
def f(x):
    return np.cos(x)

# Define the gradient
def f_deriv1(x):
    return -np.sin(x)

# Define the second derivative
def f_deriv2(x):
    return -np.cos(x)

xstar = np.pi  # known minimum

## Newton-Raphson (N-R) method
x0 = 2
n_it = 10
xvals = np.zeros(n_it)
xvals[0] = x0
for t in range(1, n_it):
    xvals[t] = xvals[t - 1] - f_deriv1(xvals[t - 1]) / f_deriv2(xvals[t - 1])

print(xvals)
```

Next, here is bisection:

```python
## Bisection method
def bisec_step(interval, f_deriv1):
    interval = interval.copy()
    xt = np.mean(interval)
    if f_deriv1(interval[0]) * f_deriv1(xt) <= 0:
        interval[1] = xt
    else:
        interval[0] = xt
    return interval

n_it = 30
a0 = 2
b0 = (3 * np.pi / 2) - (xstar - a0)
interval = np.zeros((n_it, 2))
interval[0,:] = [a0, b0]

for t in range(1, n_it):
    interval[t,:] = bisec_step(interval[t-1,:], f_deriv1)

print(np.mean(interval, axis=1))
```

---

[← 3. Univariate function optimization](03-3-univariate-function-optimization.md) · [Up: contents](index.md) · [5. Multivariate optimization →](05-5-multivariate-optimization.md)
