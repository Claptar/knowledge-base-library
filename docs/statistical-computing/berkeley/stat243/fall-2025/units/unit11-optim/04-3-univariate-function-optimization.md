---
title: 3. Univariate function optimization
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Univariate function optimization

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

We'll start with some strategies for univariate functions. These can be
useful later on in dealing with multivariate functions.

## Golden section search

This strategy requires only that the function be unimodal.

Assume we have a single minimum, in $[a,b]$. We choose two points in the
interval and evaluate them, $f(x_{1})$ and $f(x_{2})$. If
$f(x_{1})<f(x_{2})$ then the minimum must be in $[a,x_{2}]$, and if the
converse in $[x_{1},b]$. We proceed by choosing a new point in the new,
smaller interval and iterate. At each step we reduce the length of the
interval in which the minimum must lie. The primary question involves
what is an efficient rule to use to choose the new point at each
iteration.

Suppose we start with $x_{1}$ and $x_{2}$ s.t. they divide $[a,b]$ into
three equal segments. Then we use $f(x_{1})$ and $f(x_{2})$ to rule out
either the leftmost or rightmost segment based on whether
$f(x_{1})<f(x_{2})$. If we have divided equally, we cannot place the
next point very efficiently because either $x_{1}$ or $x_{2}$ equally
divides the remaining space, so we are forced to divide the remaining
space into relative lengths of 0.25, 0.25, and 0.5. The next time
around, we may only rule out the shorter segment, which leads to
inefficiency.

The efficient strategy is to maintain the *golden ratio* between the
distances between the points using $\phi=(\sqrt{5}-1)/2\approx.618$ (the
golden ratio), which is determined by solving for $\phi$ in this
equation: $\phi-\phi^{2}=2\phi-1$. We start with $x_{1}=a+(1-\phi)(b-a)$
and $x_{2}=a+\phi(b-a)$. Then suppose $f(x_{1})<f(x_{2})$ so the minimum
must be in $[a,x_{2}]$. Since $x_{1}-a>x_{2}-x_{1}$, we now choose
$x_{3}$ in the interval $[a,x_{1}]$ to produce three subintervals,
$[a,x_{3}],\,[x_{3},x_{1}],\,[x_{1},x_{2}]$. We choose to place $x_{3}$
s.t. it uses the golden ratio in the interval $[a,x_{1}]$, namely
$x_{3}=a+(1-\phi)(x_{2}-a)$. This means that the length of the first
subinterval is $(\phi-\phi^{2})(b-a)$ and the length of the third
subinterval is $(2\phi-1)(b-a)$, but those lengths are equal because we
found $\phi$ to satisfy $\phi-\phi^{2}=2\phi-1$.

The careful choice of $\phi$ allows us to narrow the search interval by
an equal proportion,$1-\phi$, in each iteration. Eventually we have
narrowed the minimum to between $x_{t-1}$ and $x_{t}$, where the
difference $|x_{t}-x_{t-1}|$ is sufficiently small (within some
tolerance - see Section 4 for details), and we report
$(x_{t}+x_{t-1})/2$.

## Bisection method

The bisection method requires the existence of the first derivative but
has the advantage over the golden section search of halving the interval
at each step. We again assume unimodality.

We start with an initial interval $(a_{0},b_{0})$ and proceed to shrink
the interval. Let's choose $a_{0}$ and $b_{0}$, and set $x_{0}$ to be
the mean of these endpoints. Now we update according to the following
algorithm, assuming our current interval is $[a_{t},b_{t}]$.

- If $f^{\prime}(a_{t})f^{\prime}(x_{t})<0$, then $[a_{t+1},b_{t+1}] = [a_{t},x_{t}]$
- If $f^{\prime}(a_{t}) f^{\prime}(x_{t})>0$, then $[a_{t+1},b_{t+1}] = [x_{t},b_{t}]$

and set $x_{t+1}$ to the mean of $a_{t+1}$ and $b_{t+1}$.
The basic idea is that if the derivative at both $a_{t}$ and $x_{t}$ is
negative, then the minimum must be between $x_{t}$ and $b_{t}$, based on
the intermediate value theorem. If the derivatives at $a_{t}$ and
$x_{t}$ are of different signs, then the minimum must be between $a_{t}$
and $x_{t}$.

Since the bisection method reduces the size of the search space by
one-half at each iteration, one can work out that each decimal place of
precision requires 3-4 iterations. Obviously bisection is more efficient
than the golden section search because we reduce by $0.5>0.382=1-\phi$,
so we've gained information by using the derivative. It requires an
evaluation of the derivative however, while golden section just requires
an evaluation of the original function.

Bisection is an example of a *bracketing* method, in which we trap the
minimum within a nested sequence of intervals of decreasing length.
These tend to be slow, but if the first derivative is continuous, they
are robust and don't require that a second derivative exist.

## Newton-Raphson (Newton's method)

### Overview

We'll talk about Newton-Raphson (N-R) as an optimization method rather
than a root-finding method, but they're just different perspectives on
the same algorithm.

For N-R, we need two continuous derivatives that we can evaluate. The
benefit is speed, relative to bracketing methods. We again assume the
function is unimodal. The minimum must occur at $x^{*}$ s.t.
$f^{\prime}(x^{*})=0$, provided the second derivative is non-negative at
$x^{*}$. So we aim to find a zero (a root) of the first derivative
function. Assuming that we have an initial value $x_{0}$ that is close
to $x^{*}$, we have the Taylor series approximation
$$f^{\prime}(x)\approx f^{\prime}(x_{0})+(x-x_{0})f^{\prime\prime}(x_{0}).$$
Now set $f^{\prime}(x)=0$, since that is the condition we desire (the
condition that holds when we are at $x^{*}$), and solve for $x$ to get
$$x_{1}=x_{0}-\frac{f^{\prime}(x_{0})}{f^{\prime\prime}(x_{0})},$$ and
iterate, giving us updates of the form
$x_{t+1}=x_{t}-\frac{f^{\prime}(x_{t})}{f^{\prime\prime}(x_{t})}$. What
are we doing intuitively? Basically we are taking the tangent to $f(x)$
at $x_{0}$ and extrapolating along that line to where it crosses the
x-axis to find $x_{1}$. We then reevaluate $f(x_{1})$ and continue to
travel along the tangents.

One can prove that if $f^{\prime}(x)$ is twice continuously
differentiable, is convex, and has a root, then N-R converges from any
starting point.

Note that we can also interpret the N-R update as finding the analytic
minimum of the quadratic Taylor series approximation to $f(x)$.

!!! warning "Warning"
Newton's method converges very quickly (as we'll discuss in Section 4),
but if you start too far from the minimum, you can run into serious
problems.

:::

### Secant method variation on N-R

Suppose we don't want to calculate the second derivative required in the
divisor of N-R. We might replace the analytic derivative with a discrete
difference approximation based on the secant line joining
$(x_{t},f^{\prime}(x_{t}))$ and $(x_{t-1},f^{\prime}(x_{t-1}))$, giving
an approximate second derivative:
$$f^{\prime\prime}(x_{t})\approx\frac{f^{\prime}(x_{t})-f^{\prime}(x_{t-1})}{x_{t}-x_{t-1}}.$$
For this variant on N-R, we need two starting points, $x_{0}$ and
$x_{1}$.

An alternative to the secant-based approximation is to use a standard
discrete approximation of the derivative such as
$$f^{\prime\prime}(x_{t})\approx\frac{f^{\prime}(x_{t}+h)-f^{\prime}(x_{t}-h)}{2h}.$$

### How can Newton's method go wrong?

Let's think about what can go wrong - namely when we could have
$f(x_{t+1})>f(x_{t})$? To be concrete (and without loss of generality),
let's assume that $f(x_{t})>0$, in other words that $x^{*}<x_{t}$.

1.  As usual, we can develop some intuition by starting with the worst
    case that $f^{\prime\prime}(x_{t})$ is 0, in which case the method
    would fail as $x_{t+1}$ would be $-\infty$.
2.  Now suppose that $f^{\prime\prime}(x_{t})$ is a small positive
    number. Basically, if $f^{\prime}(x_{t})$ is relatively flat, we can
    get that $|x_{t+1}-x^{*}|>|x_{t}-x^{*}|$ because we divide by a
    small value for the second derivative, causing $x_{t+1}$ to be far
    from $x_{t}$ (though it does at least go in the correct direction).
    We'll see an example on the board and the demo code (see below).
3.  Newton's method can also go uphill (going in the wrong direction,
    away from $x^{*}$) when the second derivative is negative, with the
    method searching for a maximum, since we would have $x_{t+1}>x_{t}$.
    Another way to think of this is that Newton's method does not
    automatically minimize the function, rather it finds local optima.

In all these cases Newton's method could diverge, failing to converge on
the optimum.

#### Divergence

First let's see an example of divergence. The first and second plots
show two cases of convergence, while the third plot panel shows divergence.
In the third plot, the initial second derivative value is small enough
that $x_{2}$ is further from $x^{*}$ than $x_{1}$ and then $x_{3}$ is
yet further away. In all cases the sequence of $x$ values is indicated
by the red letters.

```python
#| fig-height: 3

import numpy as np
import matplotlib.pyplot as plt

def f_deriv1(x, theta=1):
    ## First derivative - we want the root of this.
    return np.exp(x * theta) / (1 + np.exp(x * theta)) - 0.5

def f_deriv2(x, theta=1):
    ## Second derivative - used to scale the optimization steps.
    return np.exp(x * theta) / ((1 + np.exp(x * theta)) ** 2)

def make_plot(xs, xvals, f_deriv1, f_deriv2, subplot, title):
    plt.plot(xs, f_deriv1(xs), '-', label="f'(x)", color = 'grey')
    plt.plot(xs, f_deriv2(xs), '--', label="f''(x)", color = 'grey')
    for i in range(len(xvals)):
        plt.text(xvals[i], 0, i, fontsize=14, color = 'red')
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.title(title)
    plt.legend(loc='upper left')


xs = np.linspace(-15, 15, 300)

n = 10
xvals = np.zeros(n)

## Good starting point
x0 = 1

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - f_deriv1(xvals[t-1]) / f_deriv2(xvals[t-1])

make_plot(xs, xvals, f_deriv1, f_deriv2, 1, "converges quickly")
plt.show(block=False)

print(np.round(xvals,3))

## Ok starting point
x0 = 2

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - f_deriv1(xvals[t-1]) / f_deriv2(xvals[t-1])

make_plot(xs, xvals, f_deriv1, f_deriv2, 2, "converges")
plt.show(block=False)

print(np.round(xvals,3))

## Bad starting point

x0 = 2.5

xvals[0] = x0
for t in range(1,10):
    xvals[t] = xvals[t-1] - f_deriv1(xvals[t-1]) / f_deriv2(xvals[t-1])

make_plot(xs, xvals[np.abs(xvals) < 15], f_deriv1, f_deriv2, 3, "diverges")
plt.show(block=False)
## whoops!

print(np.round(xvals,3))
```

In the last case the divergence quickly leads to numerical overflow and then NaNs (resulting from trying to use infinity in calculations).

#### Multiple optima: converging to the wrong optimum

In the first row of the next figure, let's see an example of climbing
uphill and finding a local maximum rather than minimum. The other rows
show convergence. In all cases the minimum is at $x^{*}\approx3.14$

```python
#| fig-height: 7

---

[← 2. Overview](03-2-overview.md) · [Up: contents](index.md) · [Define the original function →](05-define-the-original-function.md)
