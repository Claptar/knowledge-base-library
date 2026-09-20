---
title: "38. Numerical Optimization for Statistics"
course: "Berkeley Stat 243 Fall 2024"
chapter: 38
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 38. Numerical Optimization for Statistics

## What this covers

This chapter answers a practical question: how do you find the minimum (or maximum) of a
function when calculus alone will not hand you a closed-form answer? That situation is the norm
rather than the exception in statistics — finding the MLE for a GLM, fitting a nonlinear
regression model, maximizing a likelihood under constraints, and fitting a machine-learning
model all reduce to a numerical optimization problem. It builds the standard toolkit: bracketing
and Newton-type methods in one dimension, the multivariate methods built on top of them (Newton,
quasi-Newton, gradient and coordinate descent, Nelder-Mead, simulated annealing), how to judge
whether an iterative method is actually converging, and enough of convex analysis and constrained
optimization to recognize when a problem is easy. It assumes multivariable calculus (gradients,
Hessians, Taylor expansions), the linear algebra of Unit 10 (eigendecompositions, positive
definiteness, the SVD and QR decomposition), and enough statistics to recognize a likelihood and
a GLM.

## Setting up the problem

We will not distinguish notationally between univariate and multivariate functions: both are
written $f(x)$, with $x = (x_1,\ldots,x_p)$ in the multivariate case. The gradient is the column
vector of first partial derivatives,
$$f'(x) = \nabla f(x) = \left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_p}\right)^\top,$$
and the Hessian is the matrix of second partial derivatives,
$$f''(x) = \nabla^2 f(x) = H_f(x) = \begin{pmatrix}
\dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1 \partial x_p}\\[4pt]
\dfrac{\partial^2 f}{\partial x_1 \partial x_2} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2 \partial x_p}\\[4pt]
\vdots & \vdots & \ddots & \vdots \\[2pt]
\dfrac{\partial^2 f}{\partial x_1 \partial x_p} & \dfrac{\partial^2 f}{\partial x_2 \partial x_p} & \cdots & \dfrac{\partial^2 f}{\partial x_p^2}
\end{pmatrix}.$$
For an iterative algorithm we write the sequence of trial values as $x_0, x_1, \ldots, x_t,
x_{t+1}$, converging (we hope) to the optimum $x^*$. $x_0$ is the starting point, which usually
has to be chosen with some care. When a likelihood is explicitly in view we write $\theta$ for
the argument being optimized over, $Y$ for the data, and $z$ for covariates, to keep them
visually distinct from a generic $x$.

We will focus on **minimization**, since maximizing $f$ is the same as minimizing $-f$. The goal
is to find the argument $x^*$ that minimizes $f$ over some domain $D$:
$$x^* = \arg\min_{x \in D} f(x).$$
Sometimes $D = \Re^p$, and sometimes $D$ imposes constraints on $x$; the unconstrained case, where
every $x$ for which $f$ is defined is a legal candidate, is the easier one and the one we treat
first. We assume $f$ is continuous throughout — there is little to be done systematically with a
discontinuous objective.

In one dimension, minimization is the same problem as root-finding applied to the derivative:
the minimum of a differentiable function can only occur where the derivative is zero. So for
differentiable $f$ we look for $x^*$ with $f'(x^*) = \nabla f(x^*) = 0$, and to make sure it is a
minimum rather than a maximum or saddle we want $f(y) \ge f(x^*)$ for $y$ near $x^*$, or
equivalently (for twice-differentiable $f$) $f''(x^*) \ge 0$. In more than one dimension the
analogous condition is that the Hessian at $x^*$ is positive semi-definite: moving away from
$x^*$ in *any* direction does not go downhill.

Different strategies suit a discrete, countable domain versus a continuous, dense one; we
concentrate on the continuous case, though the discrete case does arise in statistics (variable
selection, for instance) and is touched on later. Throughout, we assume we can evaluate $f$, and
often that we can get analytic or numerical derivatives of $f$, or derivatives from a package that
does automatic differentiation.

Optimization is, to a first approximation, a solved problem with excellent software. The reason
to go through the basic strategies rather than just calling a library routine is that the
function being optimized changes with every new problem and can be surprisingly easy to trip up —
knowing what can go wrong, and why, is what lets you choose (or debug) an approach when you meet
one. Finding a *global* rather than merely *local* minimum is a persistent extra difficulty. One
topic we will not cover is MCMC — used for approximating integrals and posterior sampling, and
occasionally for optimization itself (Monte Carlo EM, simulated annealing draws on the same
ideas) — since it deserves, and gets, a course of its own.

By the end of this material you should have a working understanding of: line searches
(one-dimensional optimization); multivariate derivative-based optimization, and how line searches
sit inside it; derivative-free methods; the methods actually used by Python's optimization
routines, their strengths and weaknesses, and some tricks for getting more out of them; and enough
of a picture of convex optimization to recognize when you are looking at one.

## Univariate optimization

These one-dimensional strategies matter beyond the univariate case itself: multivariate methods
routinely call a univariate method internally, to choose how far to step once a direction has
been chosen.

### Golden section search

Golden section search requires only that $f$ be **unimodal** on the search interval — no
derivative needed. Suppose the minimum lies in $[a,b]$. The efficient strategy is to maintain a
constant ratio, the *golden ratio* $\phi = (\sqrt5 - 1)/2 \approx 0.618$, between the lengths of
successive sub-intervals; $\phi$ is exactly the root of $\phi - \phi^2 = 2\phi - 1$, and that
identity is what makes the scheme self-similar from one iteration to the next.

Start with $x_1 = a + (1-\phi)(b-a)$ and $x_2 = a + \phi(b-a)$, and evaluate $f(x_1)$ and
$f(x_2)$. Suppose $f(x_1) < f(x_2)$; then the minimum must lie in $[a, x_2]$ (if it were to the
right of $x_2$, $f$ would have to decrease then increase then decrease again on $[a,b]$,
contradicting unimodality). Since $x_1 - a > x_2 - x_1$, we now choose a third point $x_3$ in
$[a,x_1]$, splitting $[a,x_2]$ into three pieces, $[a,x_3],\,[x_3,x_1],\,[x_1,x_2]$, and placing
$x_3$ so that it again respects the golden ratio inside $[a,x_1]$:
$x_3 = a + (1-\phi)(x_2 - a)$. The point of the careful placement is that the first and third
sub-intervals end up with equal length — $(\phi-\phi^2)(b-a)$ and $(2\phi-1)(b-a)$ respectively,
equal precisely because $\phi$ satisfies $\phi - \phi^2 = 2\phi - 1$ — so exactly one new function
evaluation is needed at each step, and the bracket shrinks by the same factor $1-\phi$ every time.

Eventually the bracket narrows to $[x_{t-1}, x_t]$ with $|x_t - x_{t-1}|$ below some tolerance
(see below for how to choose one), and we report $(x_t + x_{t-1})/2$.

### Bisection

Bisection needs the first derivative but, in exchange, halves the bracket at every step rather
than shrinking it by $1-\phi \approx 0.382$. Start with an interval $(a_0,b_0)$ and $x_0$ the
midpoint. Given the current bracket $[a_t,b_t]$ with midpoint $x_t$:

- if $f'(a_t)\,f'(x_t) < 0$, set $[a_{t+1},b_{t+1}] = [a_t, x_t]$;
- if $f'(a_t)\,f'(x_t) > 0$, set $[a_{t+1},b_{t+1}] = [x_t, b_t]$;

and let $x_{t+1}$ be the new midpoint. The logic is the intermediate value theorem applied to
$f'$: if $f'(a_t)$ and $f'(x_t)$ have the same sign, the sign change (and hence the root of $f'$,
hence the minimum) must be in $[x_t, b_t]$; if they differ in sign, it is in $[a_t, x_t]$.

Because the bracket halves every iteration, each extra decimal place of precision costs 3–4
iterations. Bisection is more efficient than golden section because $0.5 > 0.382 = 1-\phi$: using
the derivative buys real information. Its price is needing that derivative at all — golden
section only ever evaluates $f$ itself. Bisection is an example of a *bracketing* method, which
traps the minimum inside a nested, shrinking sequence of intervals; bracketing methods tend to be
slow but, given a continuous first derivative, are robust and need no second derivative.

### Newton's method (Newton-Raphson)

Newton-Raphson (N-R) is usually taught as a root-finder, but as an optimization method it is the
same algorithm pointed at $f'$: we want a zero of the derivative. It needs two continuous
derivatives, in exchange for being much faster than a bracketing method. Given a current guess
$x_0$ near $x^*$, Taylor-expand the derivative,
$$f'(x) \approx f'(x_0) + (x - x_0) f''(x_0),$$
set the left side to zero (the condition that holds at $x^*$), and solve for $x$:
$$x_1 = x_0 - \frac{f'(x_0)}{f''(x_0)},$$
giving the general update
$$x_{t+1} = x_t - \frac{f'(x_t)}{f''(x_t)}.$$
Geometrically, this is following the tangent line to $f'$ at $x_t$ down to where it crosses zero,
then re-evaluating and repeating — equivalently, it is the minimum of the quadratic Taylor
approximation to $f$ itself at $x_t$. If $f'$ is twice continuously differentiable, convex, and
has a root, N-R converges from *any* starting point; without convexity, as we see below, the
starting point matters a great deal.

**Warning.** Newton's method converges very fast once it is close, but starting too far from the
minimum can cause serious problems — see the failure modes below.

#### The secant variation

If you would rather not compute $f''$, replace it with a discrete approximation from the secant
line joining $(x_t, f'(x_t))$ and $(x_{t-1}, f'(x_{t-1}))$:
$$f''(x_t) \approx \frac{f'(x_t) - f'(x_{t-1})}{x_t - x_{t-1}},$$
which needs two starting points $x_0, x_1$ rather than one. An alternative is an ordinary
symmetric finite-difference approximation, $f''(x_t) \approx \big(f'(x_t+h) - f'(x_t-h)\big)/2h$.

#### How Newton's method can go wrong

Ask when we could have $f(x_{t+1}) > f(x_t)$ — a step that makes things worse. Concretely, take
$x^* < x_t$ (WLOG, by symmetry) so $f'(x_t) > 0$.

1. In the worst case $f''(x_t) = 0$: the method fails outright, since $x_{t+1}$ would be
   $-\infty$.
2. If $f''(x_t)$ is small and positive — the derivative is nearly flat — dividing by it can send
   $x_{t+1}$ much *further* from $x^*$ than $x_t$ was, even though the step is at least in the
   right direction.
3. If $f''(x_t) < 0$, the update goes *uphill*: it is chasing a local maximum rather than a
   minimum, since Newton's method finds critical points, not minima specifically. This can
   happen whenever $f$ is not convex and the current iterate sits in a concave region.

Any of these can make the sequence diverge outright. Two small numerical experiments illustrate
this, using $f'(x) = \operatorname{expit}(x) - 0.5$ with $f''(x) = \operatorname{expit}(x)(1 -
\operatorname{expit}(x))$ (so $f$ itself is a smoothed step, and $x^*=0$):

```python
def f_deriv1(x, theta=1):
    return np.exp(x*theta) / (1 + np.exp(x*theta)) - 0.5

def f_deriv2(x, theta=1):
    return np.exp(x*theta) / (1 + np.exp(x*theta))**2

def newton_step(x):
    return x - f_deriv1(x) / f_deriv2(x)
```
Starting at $x_0 = 1$ converges quickly; $x_0 = 2$ still converges, more slowly; $x_0 = 2.5$
diverges — the second derivative there is small enough that each step overshoots by more than the
last, and the iterates blow up to numerical overflow within a handful of steps. A second example,
minimizing $f(x)=\cos(x)$ near its minimum at $x^*=\pi$, shows the uphill failure mode directly:
starting at $x_0 = 5.5$ (where $f''(x_0) < 0$) sends the iterates *uphill* toward the local
maximum at $0$; starting at $x_0=4.3$ nearly diverges before turning around; starting at
$x_0 = 3.8$ converges cleanly. In all three cases the only thing that changed was the starting
value.

#### Safeguarding Newton's method

A robust general strategy is to run a fast method, safeguarded by a slower but reliable one.
For N-R, that safeguard is usually bisection: check whether the proposed N-R step falls outside
the bracket already established by previous steps and gradient signs, and if it does, fall back
to a bisection step instead. A second strategy is *backtracking*: if a proposed step increases
$f$, retreat along the step direction until it decreases — the crudest version repeatedly halves
the step, and a better one fits a polynomial to the known values $f(x_t)$, $f(x_{t+1})$,
$f'(x_t)$, $f''(x_t)$ and steps to the minimum of that polynomial. A full line search at every
step is usually not worth its cost, particularly in the multivariate case, where the next
iteration is about to head off in a different direction anyway.

## Judging convergence

### Convergence metrics

The obvious criterion — is $f'(x_t)$ near zero? — is unreliable wherever $f$ happens to be flat,
since the derivative can be small there even far from the optimum. Instead we generally monitor
the size of the step itself, $|x_{t+1} - x_t|$. **Absolute convergence** checks
$|x_{t+1}-x_t| < \epsilon$; **relative convergence** checks
$|x_{t+1}-x_t|/|x_t| < \epsilon$, which is appealing because it accounts for the scale of $x$, but
breaks down as $x_t \to 0$ — the usual fix is
$|x_{t+1}-x_t| / (|x_t| + \epsilon) < \epsilon$. The choice of $\epsilon$ should respect machine
precision; for relative convergence, the square root of machine epsilon (about $10^{-8}$) is a
reasonable default. In the multivariate case the same idea applies to a norm,
$\|x_{t+1}-x_t\|_p$, usually $p=1$ or $p=2$.

A convergence measure that fails to decrease, or that cycles, is a sign of trouble. Software
generally stops after a fixed (user-adjustable) number of iterations regardless; when it stops
that way rather than by meeting the convergence criterion, the algorithm has *failed to converge*
— sometimes it just needs longer, but often that is a symptom of a poorly-behaved objective or a
bad starting value.

### Starting values and multimodality

Good starting values matter for three separate reasons: they speed convergence, they can prevent
divergence or cycling outright, and they help avoid landing at the wrong local optimum. Trying
several starting values — random or deliberately spread out — is the standard defense against
multimodality. A stress-test commonly used for this is the **Rastrigin function**,
$$f(x) = An + \sum_{i=1}^n \big(x_i^2 - A\cos(2\pi x_i)\big), \qquad A = 10,$$
which has a huge number of local minima arranged in a regular grid around the single global
minimum at the origin; it is notoriously hard to optimize even in fairly low dimension, and
30-dimensional Rastrigin is a standard hard benchmark.

### Order of convergence

Let $\epsilon_t = |x_t - x^*|$. If, for some $\beta > 0$ and $c \ne 0$,
$$\lim_{t\to\infty} \frac{|\epsilon_{t+1}|}{|\epsilon_t|^\beta} = c$$
exists, the method is said to have **order of convergence** $\beta$, meaning
$|\epsilon_{t+1}| \approx c\,|\epsilon_t|^\beta$: it measures how the error at step $t+1$ scales
with the error at step $t$. Bisection does not strictly satisfy this definition but behaves as
though it has **linear convergence** ($\beta=1$): the error shrinks by a roughly constant factor
each step.

Newton's method has **quadratic convergence** ($\beta = 2$), which is fast. To see why, assume
$f'$ is twice continuously differentiable and Taylor-expand the gradient at $x^*$ around the
current iterate $x_t$:
$$f'(x^*) = f'(x_t) + (x^*-x_t) f''(x_t) + \tfrac12 (x^*-x_t)^2 f'''(\xi_t) = 0$$
for some $\xi_t$ between $x^*$ and $x_t$. Substituting the N-R update
$x_{t+1} = x_t - f'(x_t)/f''(x_t)$ and simplifying gives
$$\frac{|\epsilon_{t+1}|}{|\epsilon_t|^2} = \frac{|x^*-x_{t+1}|}{(x^*-x_t)^2}
= \left|\frac12 \frac{f'''(\xi_t)}{f''(x_t)}\right|.$$
If the right side has a limit as $x_t \to x^*$,
$$c = \left|\frac12\, \frac{f'''(x^*)}{f''(x^*)}\right|,$$
then $\beta = 2$. If $c$ happened to equal $1$, having $k$ correct digits at step $t$ would give
$2k$ at step $t+1$ — which is the sense in which quadratic convergence is fast. In practice $c$
moderates the rate: we would like a large second derivative and a small third derivative, and the
expression is also a warning that things go badly if $f''(x_t) = 0$ anywhere along the way — think
about what that means for the next step geometrically. The behavior of the derivatives near
$x^*$ determines the **domain of attraction**: the region from which N-R converges rather than
diverges. (For reference, Givens and Hoeting show that the secant variant of N-R — using the
finite-difference approximation to $f''$ instead of the exact value — has order of convergence
$\beta \approx 1.62$, between linear and quadratic.)

## Optimization in several dimensions

Moving from one dimension to many makes things harder in three specific ways: there are many
possible directions to move in at each step, not just two; the linear algebra (large vectors and
matrices) becomes a real computational cost; and multimodality becomes both more likely and
harder to detect. We start with a trick — profiling — that reduces the dimension of the problem
before optimizing at all, then work through methods that use the Hessian, methods that use only
the gradient, and methods that use neither.

### Profiling

If the parameters split into two groups $\theta_1, \theta_2$ and we can maximize analytically
over $\theta_2$ for fixed $\theta_1$, that gives $\hat\theta_2(\theta_1)$; substituting it back
into the objective gives the **profile** likelihood, a function of $\theta_1$ alone, over which
numerical optimization is now simpler.

Example: for regression with correlated errors, $Y \sim \mathcal N(X\beta, \sigma^2 \Sigma(\rho))$
with correlation matrix $\Sigma(\rho)$ depending on a scalar $\rho$, the maximum over $\beta$ for
fixed $\rho$ is the GLS estimator
$\hat\beta(\rho) = (X^\top \Sigma(\rho)^{-1} X)^{-1} X^\top \Sigma(\rho)^{-1} Y$ (in general such
a maximizer would depend on all the other parameters, but here conveniently only on $\rho$).
Substituting gives an intermediate profile likelihood in $\sigma^2$ and $\rho$; maximizing that
over $\sigma^2$ in turn gives
$\hat\sigma^2(\rho) = (Y - X\hat\beta(\rho))^\top \Sigma(\rho)^{-1} (Y-X\hat\beta(\rho))/n$.
Substituting *that* leaves a likelihood in $\rho$ alone — a one-dimensional numerical problem in
place of the original multi-parameter one.

### Newton-Raphson in several dimensions

The multivariate update replaces the scalar second derivative with the Hessian:
$$x_{t+1} = x_t - H_f(x_t)^{-1} \nabla f(x_t).$$
Three things need watching, more urgently than in one dimension: good starting values, the
positive definiteness of $H_f$ (if it fails, one option is to nudge the Cholesky factor of $H_f$
by adding to the diagonal until it is positive definite), and correctness of the derivatives
themselves.

**Worked example.** Fit the nonlinear model $Y_i = \beta_0 + \beta_1 \exp(t_i/\beta_2) + \epsilon_i$
to the Mauna Loa annual CO$_2$ record (with $t_i$ the year, centered for numerical behavior).
Starting values come from linearizing: pick a trial $\beta_2$, compute the "covariate"
$\exp(t_i/\beta_2)$, and fit $\beta_0, \beta_1$ by OLS. With $\beta_2$ set to the rough order of
magnitude of the (centered) year values, the fit is visibly poor; increasing $\beta_2$ to $100$
improves it. Automatic differentiation (JAX, here; PyTorch or TensorFlow would also do) gives the
gradient and Hessian of the sum of squared residuals directly from the model code:

```python
def loss(params):
    fitted = params[0] + params[1]*jnp.exp(jnp.array(data.year)/params[2])
    return jnp.sum((fitted - jnp.array(data.co2))**2.0)

deriv1, deriv2 = jax.grad(loss), jax.hessian(loss)
```
At the $\beta_2 = 100$ starting values the Hessian turns out *not* to be positive definite — a
real warning sign, not just an inconvenience. Trying $\beta_2 = 50$ instead gives a positive
definite Hessian, and running the update
$x_{t+1} = x_t - H_f(x_t)^{-1}\nabla f(x_t)$ from there converges to a good-looking fit. The
moral is not "it worked" but that *sensitivity to the starting value, and to whether the Hessian
is positive definite along the way, is the normal state of affairs* for Newton's method in more
than one dimension — visual (or other) sanity-checking of the final fit remains essential.

Automatic differentiation deserves a word on its own: it is the systematic application of the
chain rule by the computer, building up the derivative of a whole computation from the known
derivatives of its elementary operations (multiplication, exponentiation, etc.). It is exactly
the same idea used to train deep networks by gradient descent. From the user's side it typically
just means writing the calculation with an AD-aware array library.

### Fisher scoring and IRLS

The **Fisher information** is the expected outer product of the score,
$I(\theta) = E_f\big(\nabla f(y)\nabla f(y)^\top\big)$; under standard regularity conditions
(satisfied by exponential families) the expected Hessian of the log-likelihood is minus the
Fisher information, $E_f H_f(y) = -I(\theta)$, and plugging in the data instead of taking the
expectation gives the *observed* Fisher information. Ordinary N-R therefore implicitly uses the
observed Fisher information as its curvature matrix. Replacing it with (minus) the *expected*
Fisher information, where that expectation can be computed, gives the **Fisher scoring** (FS)
algorithm:
$$(\text{N-R}):\ \theta_{t+1} = \theta_t - H_f(\theta_t)^{-1}\nabla f(\theta_t), \qquad
(\text{FS}):\ \theta_{t+1} = \theta_t + I(\theta_t)^{-1}\nabla f(\theta_t).$$
FS and N-R share the same (quadratic) order of convergence; which is cheaper depends on the
problem, and Givens and Hoeting note FS tends to do better early in the iteration while N-R does
better as refinement near the optimum. The **Gauss-Newton** algorithm for nonlinear least squares
is the analogous move of substituting the Fisher information for the Hessian; it is what `nls()`
in R uses.

When either the observed or expected Fisher information is nearly singular, that is a small
eigenvalue in the precision matrix — equivalently a large eigenvalue in the covariance, meaning
some linear combination of the parameters is poorly determined and the likelihood is nearly flat
in that direction. That is exactly the situation in which N-R-type convergence slows down, so
statistical uncertainty and numerical ill-conditioning are two faces of the same thing; near
collinear regressors are one common cause.

For **generalized linear models** in the canonical parameterization (log link for Poisson, logit
for binomial, so the natural parameter is the linear predictor $\eta = X\beta$), the gradient of
the log-likelihood works out to $\nabla l(\beta) = (Y - E(Y))^\top X$ and the Hessian to
$H_l(\beta) = -X^\top W X$, with $W$ diagonal and $W_{ii} = \operatorname{Var}(Y_i)$ (the
*working weights*) — both $E(Y)$ and $W$ depend on the current $\beta$, and get updated at every
iteration. The N-R update
$$\beta_{t+1} = \beta_t + (X^\top W_t X)^{-1} X^\top (Y - E(Y)_t)$$
can be re-expressed as an ordinary weighted least squares update,
$$\beta_{t+1} = (X^\top W_t X)^{-1} X^\top W_t \tilde Y_t, \qquad
\tilde Y_t = X\beta_t + W_t^{-1}(Y - E(Y)_t),$$
where the *working observations* $\tilde Y_t$ are the current fitted values plus residuals
rescaled (by the inverse variance) onto the scale of the linear predictor. This is exactly
**iteratively reweighted least squares (IRLS / IWLS)**, the standard estimation method for GLMs —
it is Newton-Raphson in disguise. Because the canonical-link Hessian does not depend on the data,
observed and expected Fisher information coincide here, so N-R and FS are also the same
algorithm in this case. IRLS is itself a special case of Gauss-Newton for nonlinear least squares.

### Descent and Newton-like methods

More generally, a **Newton-like** update has the form
$$x_{t+1} = x_t - \alpha_t M_t^{-1} f'(x_t),$$
where $M_t$ approximates the Hessian in some cheaper or more robust way, and $\alpha_t$ scales the
step. This opens up three separate knobs: cheaper approximations to $M_t$, safeguards against
stepping in the wrong (uphill) direction, and control over how far to step.

**Descent methods** choose a direction $p_t$ and move $x_{t+1} = x_t + \alpha_t p_t$, choosing
$\alpha_t$ (e.g. by a line search such as golden section or bisection on
$f(x_t + \alpha_t p_t)$) — though running that line search to full convergence is usually
wasteful, since another step is coming regardless. **Steepest descent** takes $M_t = I$: the
negative gradient is the direction of steepest local decrease, so
$$x_{t+1} = x_t - \alpha_t f'(x_t),$$
with $\alpha_t$ small enough (via a line search) to guarantee a decrease. Its well-known failure
mode is **zig-zagging** on elongated (ill-conditioned) contours: since each step moves exactly
perpendicular to the local contour, a narrow elliptical valley forces many short steps that
bounce from one side of the valley to the other rather than heading straight down it.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Steepest descent zig-zagging across an elongated elliptical valley toward the minimum">
  <g transform="rotate(-24 170 110)">
    <ellipse cx="170" cy="110" rx="140" ry="48" fill="none" stroke="currentColor" stroke-width="1" opacity="0.55"/>
    <ellipse cx="170" cy="110" rx="104" ry="34" fill="none" stroke="currentColor" stroke-width="1" opacity="0.65"/>
    <ellipse cx="170" cy="110" rx="68" ry="21" fill="none" stroke="currentColor" stroke-width="1" opacity="0.8"/>
    <ellipse cx="170" cy="110" rx="32" ry="9" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1"/>
  </g>
  <polyline points="40,32 232,190 68,176 206,120 122,140 170,110"
    fill="none" stroke="#d2691e" stroke-width="2" marker-end="url(#arrow)"/>
  <circle cx="40" cy="32" r="3" fill="#d2691e"/>
  <circle cx="170" cy="110" r="3" fill="#d2691e"/>
  <text x="30" y="24" font-size="12" fill="currentColor">x0</text>
  <text x="176" y="104" font-size="12" fill="currentColor">x*</text>
  <defs>
    <marker id="arrow" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
      <polygon points="0,0 8,4 0,8" fill="#d2691e"/>
    </marker>
  </defs>
</svg>
<figcaption>Each steepest-descent step is perpendicular to the local contour of an elongated
quadratic, so successive steps zig-zag across the narrow valley instead of heading straight for
the minimum $x^*$ — the number of steps needed grows with how elongated (ill-conditioned) the
contours are.</figcaption>
</figure>

If the contours were circular instead, steepest descent would head straight for the minimum in
one step; Newton's method effectively *undoes* the elliptical deformation using the Hessian,
which is the sense in which it "takes account of the rate of change in the gradient" and
steepest descent does not. Formally, a Taylor expansion of $f(x_{t+1}) - f(x_t)$ shows that any
descent update with **positive definite** $M_t$ decreases $f$ provided the step is not too large
— though this alone is not a convergence guarantee; one also needs the steps to descend
sufficiently fast and to avoid crawling along a level set. (The **conjugate gradient** algorithm
for large linear systems is, from this point of view, a particularly careful choice of direction
and step size.)

#### Quasi-Newton methods (BFGS)

When the exact Hessian is expensive, a natural alternative is to *learn* an approximation to it
as the iteration proceeds, using only gradient information already computed. The **secant
condition** requires the new curvature estimate $M_{t+1}$ to be consistent with the most recent
step:
$$M_{t+1}(x_{t+1}-x_t) = \nabla f(x_{t+1}) - \nabla f(x_t),$$
motivated by the secant line approximating the gradient along the direction just traveled. This
does not pin $M_{t+1}$ down uniquely, so extra conditions are imposed — symmetry and positive
definiteness in particular. Writing $s_t = x_{t+1}-x_t$ and $y_t = \nabla f(x_{t+1}) - \nabla
f(x_t)$, the unique symmetric **rank-one** update satisfying the secant condition is
$$M_{t+1} = M_t + \frac{(y_t - M_t s_t)(y_t - M_t s_t)^\top}{(y_t - M_t s_t)^\top s_t}$$
(positive definiteness is not automatic here, but can be arranged). The standard choice in
practice is a **rank-two** update,
$$M_{t+1} = M_t - \frac{M_t s_t (M_t s_t)^\top}{s_t^\top M_t s_t} + \frac{y_t y_t^\top}{s_t^\top y_t},$$
the **Broyden–Fletcher–Goldfarb–Shanno (BFGS)** update, which is generally positive definite and
is one of the methods behind R's `optim()`. (There is also an efficient way to update the
Cholesky factor of $M_t$ directly, which is preferable to updating $M_t^{-1}$.)

Quasi-Newton convergence is slower than N-R's quadratic rate — the curvature is only
approximate — but faster than linear, and works much better when the components of $x$ are on
comparable scales. A good starting value for $M_0$, where feasible, is the expected information
at a sensible starting point. One caveat: don't reuse the final $M_t$ as a covariance estimate —
it is only an approximation to the Hessian and can be poor; if you need the information matrix,
compute the Hessian directly at $x^*$.

#### Stochastic gradient descent

**Stochastic gradient descent (SGD)**, the workhorse of deep learning, drops the second
derivative entirely, moving along the gradient with a step size $\alpha_t$:
$$x_{t+1} = x_t - \alpha_t f'(x_t) \quad\longrightarrow\quad x_{t+1} = x_t - \alpha_t g(x_t),$$
replacing the exact gradient with anything $g(x_t)$ whose *expectation* equals it,
$E(g(x_t)) = f'(x_t)$: on average the step still heads downhill. This is useful precisely when
$f(x) = \sum_{i=1}^n f_i(x)$ for large $n$, so an exact gradient costs $O(n)$ per step. SGD instead
computes the gradient contribution from a single randomly-chosen observation, or a random
mini-batch — the latter tends to work better computationally, since it uses vectorized
arithmetic. Data should be shuffled before starting: cycling through observations in a
meaningfully-ordered sequence biases the gradient estimate and slows convergence. It is also
standard to divide the objective (and hence gradient) by $n$, which does not change the optimum
or direction but keeps the gradient's scale independent of batch size and makes its expectation
the *true* gradient rather than an $n$-scaled version of it.

Choosing the step size (**learning rate**) $\alpha_t$ trades off speed against simply bouncing
around the optimum without settling; the usual prescription is to shrink $\alpha_t$ over time,
for instance $\alpha_t = 1/t$, or a step schedule that multiplies $\alpha$ by some
$\gamma\in(0.8,0.9)$ every $T$ iterations, or that halves $\alpha$ every $T$ iterations (then
quarters it, and so on). SGD can be shown formally to converge for convex objectives.

### Coordinate descent (Gauss-Seidel)

**Gauss-Seidel**, also called back-fitting or cyclic coordinate descent, updates one coordinate at
a time rather than choosing a full-dimensional direction: treat the $j$th component of $f'(x)$ as
a univariate function of $x_j$ alone (holding the rest fixed) and solve it for a root, cycle
through $j = 1,\ldots,p$, and repeat. The appeal is that univariate root-finding is easy, often
more numerically stable than the multivariate version, and fast per step. (Back-fitting used to
be the standard way to fit additive models $E(Y) = f_1(z_1) + \cdots + f_p(z_p)$.) Because it can
only move axis-by-axis, coordinate descent zig-zags on elongated contours for essentially the same
reason steepest descent does — each step is confined to a single coordinate direction rather than
the true downhill direction.

**Worked example: the lasso.** The lasso minimizes
$\|Y - X\beta\|_2^2 + \lambda \sum_j |\beta_j|$. Coordinate descent is the standard way to solve
it, either cycling through coordinates or greedily choosing whichever gives the largest decrease,
using **directional derivatives** since the $L_1$ penalty is not differentiable at zero (though it
does have one-sided directional derivatives). The directional derivative of the objective in
$\beta_j$ is $-2\sum_i x_{ij}(Y_i - X_i^\top\beta) \pm \lambda$ (add $\lambda$ moving in the
direction $\beta_j \ge 0$, subtract it moving toward $\beta_j < 0$); if $\beta_{j,t}=0$, a step in
*either* direction contributes $+\lambda$ from the penalty. Having chosen a coordinate, set its
directional derivative to zero and solve for the new $\beta_j$. (`glmnet` in R implements this
family of penalized fits efficiently; related work by Mittal et al. does the analogous thing for
survival models with very large $p$, exploiting sparsity in $X$ rather than using Newton-Raphson,
which is infeasible at that scale.) A useful practical trick is **warm starts**: solve for a large
$\lambda$ (where all coefficients are zero), decrease $\lambda$ gradually, and start each new fit
from the previous solution — this traces out the whole "solution path" quickly, and is how
$\lambda$ is usually then chosen by cross-validation. (LARS computes the entire path at once by a
related strategy.) The lasso can equivalently be posed as constrained minimization,
$\|Y-X\beta\|_2^2$ subject to $\sum_j|\beta_j| \le c$ — a case of quadratic programming, discussed
below.

### Nelder-Mead

Nelder-Mead avoids derivatives (or approximations to them) entirely, which makes it robust but
slower than Newton-like methods. It tracks a **simplex** of $p+1$ points in $p$ dimensions (a
triangle in 2D, a tetrahedron in 3D), and at each iteration reflects, expands, contracts, or
shrinks that simplex based on the ranking of $f$ at its vertices. It needs four tuning constants:
a reflection factor $\alpha>0$, an expansion factor $\gamma>1$, a contraction factor
$0<\beta<1$, and a shrinkage factor $0<\delta<1$.

1. Order the vertices $x_1,\ldots,x_{p+1}$ so $f(x_1)\le\cdots\le f(x_{p+1})$, and let $\bar x$
   be the centroid of the $p$ *best* points (all but $x_{p+1}$).
2. **Reflect** the worst point through $\bar x$: $x_r = (1+\alpha)\bar x - \alpha x_{p+1}$.
3. If $f(x_r)$ falls between the best and worst of the other points, accept it in place of
   $x_{p+1}$ and stop — a good direction has been found.
4. **Expand** if $f(x_r)$ beats *every* other point (the optimum may lie further out):
   $x_e = \gamma x_r + (1-\gamma)\bar x$. Use $x_e$ if it beats $x_r$, else use $x_r$; stop
   either way.
5. Otherwise $f(x_r)$ is worse than all the other points. Let $x_h$ be whichever of $x_r,
   x_{p+1}$ is worse.
   - **Contract** $x_h$ toward $\bar x$: $x_c = \beta x_h + (1-\beta)\bar x$. If this improves on
     $f(x_h)$, replace $x_{p+1}$ with $x_c$.
   - Otherwise **shrink** the whole simplex toward the best point:
     $x_i \leftarrow \delta x_i + (1-\delta)x_1$ for $i=2,\ldots,p+1$.

All of reflection, expansion, and contraction move along the same line — through $x_{p+1}$ and
the centroid $\bar x$ — which is what makes the picture below a faithful summary of a single
iteration:

<figure>
<svg viewBox="0 0 380 240" role="img" aria-label="One Nelder-Mead iteration: reflecting, expanding, and contracting a triangle along the line through its worst vertex and the centroid of the rest">
  <polygon points="230,50 200,140 310,130" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.5"/>
  <line x1="10" y1="12" x2="325" y2="138" stroke="currentColor" stroke-width="1" stroke-dasharray="3,3" opacity="0.6"/>
  <circle cx="230" cy="50" r="3" fill="currentColor"/>
  <circle cx="200" cy="140" r="3" fill="currentColor"/>
  <circle cx="310" cy="130" r="3" fill="currentColor"/>
  <circle cx="215" cy="95" r="3" fill="currentColor"/>
  <circle cx="120" cy="60" r="3.5" fill="#d2691e"/>
  <circle cx="25" cy="25" r="3.5" fill="#d2691e"/>
  <circle cx="262" cy="112" r="3.5" fill="#d2691e"/>
  <text x="234" y="44" font-size="12" fill="currentColor">x1 (best)</text>
  <text x="150" y="150" font-size="12" fill="currentColor">x2</text>
  <text x="314" y="122" font-size="12" fill="currentColor">x3 (worst)</text>
  <text x="187" y="88" font-size="11" fill="currentColor">centroid</text>
  <text x="70" y="52" font-size="12" fill="#d2691e">xr (reflect)</text>
  <text x="-12" y="18" font-size="12" fill="#d2691e">xe (expand)</text>
  <text x="264" y="104" font-size="12" fill="#d2691e">xc (contract)</text>
</svg>
<figcaption>A single Nelder-Mead step: the worst vertex $x_3$ is reflected through the centroid of
the remaining vertices to $x_r$; if that looks especially promising the simplex expands further
to $x_e$, and if it looks worse the simplex contracts back toward the centroid to $x_c$ instead.
All three candidate points lie on the line through $x_3$ and the centroid.</figcaption>
</figure>

Convergence is judged by the spread of function values across the simplex, the total movement of
its vertices between iterations, or its size. Nelder-Mead is the default for `optim()` in R and
is available in `scipy.optimize.minimize` (though BFGS or a variant is the default there).

### Simulated annealing

Simulated annealing (SA) is a *stochastic* descent method — unlike everything above — with three
distinguishing features: uphill moves are allowed, whether a move is accepted is random, and the
algorithm becomes progressively less willing to accept uphill moves as it runs. The name is an
analogy to annealing a solid: heat it near its melting point, then cool slowly so the atoms have
time to settle into the lowest-energy (crystalline) configuration rather than freezing into a
defective one.

Iterations are grouped into stages $j=1,2,\ldots$ with a constant "temperature" $\tau_j$ within
each stage. As in MCMC, a proposal distribution $g_t(\cdot\mid\theta_t)$ generates candidate
moves:

1. Propose $\tilde\theta$ from $g_t(\cdot\mid\theta_t)$ (e.g. Normal centered at $\theta_t$).
2. Accept $\tilde\theta$ as $\theta_{t+1}$ with probability
   $\min\big(1, \exp((f(\theta_t)-f(\tilde\theta))/\tau_j)\big)$; otherwise stay at $\theta_t$.
   Downhill moves ($f(\tilde\theta) < f(\theta_t)$) are always accepted; uphill moves are
   accepted with a probability that shrinks as $\tau_j$ shrinks — a large $\tau_j$ smooths out
   the objective (much as a large variance flattens a density), so early on the algorithm can
   explore freely.
3. Repeat steps 1–2 $m_j$ times.
4. Update $\tau_j = \alpha(\tau_{j-1})$ and $m_j = \beta(m_{j-1})$, both according to some
   pre-chosen *cooling schedule*, and return to step 1.

At fixed temperature, SA is a Metropolis MCMC chain with stationary distribution
$\propto \exp(-f(\theta)/\tau_j)$; if $m_j$ is long enough to mix, the chain gravitates toward the
global minimum as it becomes an increasingly deep well relative to local minima while $\tau_j$
falls. The risk is getting trapped in a local minimum once the temperature has dropped too far
to escape it, which is why the cooling schedule matters so much — one workable choice is
$m_j \equiv 1$ and $\alpha(\tau_{j-1}) = \tau_{j-1}/(1+a\tau_{j-1})$ for small $a$, with the
initial $\tau_0$ chosen large enough that
$\exp((f(\theta_i)-f(\theta_j))/\tau_0) \approx 1$ for essentially any pair of points, so the
chain can visit the whole space at the start. SA can converge very slowly, and while multiple or
stratified starting points help find the global minimum, they compound that cost.

## Doing this in Python

`scipy.optimize` implements most of the above. `minimize_scalar` provides golden section
(`golden`) and a hybrid of interpolation with golden section (`brent`, comparable to R's
`optimize`). `minimize` covers the multivariate methods — Nelder-Mead, BFGS, and others — accepts
an optional gradient function (falling back to numerical derivatives if none is supplied), and
accepts a range of bound, linear, and nonlinear constraints (though which constraint types are
available depends on the chosen method). The CO$_2$ example above, refit with `minimize`, adds
$\sigma^2$ as a free parameter (optimized on the log scale, to enforce positivity) and compares
Nelder-Mead against BFGS from several starting points — including one deliberately bad set of
starting values, to see both methods struggle.

Automatic differentiation, as noted above, is the practical way to supply gradients (and
Hessians) to these routines without hand-deriving them: write the objective in JAX or PyTorch and
pass the resulting derivative functions straight to the optimizer.

A handful of practical considerations recur regardless of which routine is used:

- **Starting values** matter for the same three reasons as before (speed, avoiding divergence,
  avoiding bad local optima) — it is worth the time to find a good one, or several.
- **Scaling** matters: aim for a problem where a unit step in any parameter produces a roughly
  comparable change in the objective, ideally close to a unit change near the optimum. If $x_j$
  is naturally $p$ orders of magnitude smaller than the other components, reparameterize as
  $\tilde x_j = x_j \cdot 10^p$ (or work on the log scale, $\tilde x_j = \log x_j$, for
  naturally-positive parameters), and convert back at the end. If the objective itself takes
  very large or small values near the solution, rescale it too — this also avoids false
  "convergence" that is really just a gradient that looks small only because the function's
  scale is small. Working with a log-likelihood, mainly to control over/underflow, usually helps
  here as a side effect even when overflow was never actually a risk.
- **Always sanity-check the answer** — in particular, make sure the optimizer has not simply
  wandered to an extreme value on the boundary of the parameter space.
- Venables and Ripley's advice is worth keeping: it is usually worth supplying analytic *first*
  derivatives, but rarely worth the trouble of supplying analytic *second* derivatives — let the
  optimizer approximate those.
- For likelihood optimization specifically, asymptotic theory is a hidden ally: with a large
  enough sample the log-likelihood is approximately quadratic near the MLE (this is exactly the
  content of asymptotic normality), which is a very friendly surface to optimize over. For
  variance components and other non-negative parameters, optimizing on the log scale sidesteps
  the constraint altogether.

Note that `hess_inv` returned by SciPy's BFGS is the running *approximation* to the Hessian from
the quasi-Newton updates, not a direct numerical Hessian at the optimum — if you actually need
the Hessian (e.g. for standard errors), compute it separately, for instance with `numdifftools`
or by automatic differentiation.

## Combinatorial optimization over discrete spaces

Most of the methods above assume a continuous domain, but some statistical problems — variable
selection prominent among them — have a genuinely discrete one. Simulated annealing, described
above, adapts directly to a discrete space. **Genetic algorithms** are another approach: encode
candidate solutions as "chromosomes" (the dimensions of the space become loci on the
chromosome), and evolve a population of candidates through mutation and crossover steps, as in
high-dimensional variable selection. **Stochastic search variable selection** is a popular
Bayesian approach to the same problem, implemented via MCMC.

## Convexity

Many optimization problems are, or can be transformed into, convex ones, and it is worth being
able to recognize when that is true because convex optimization is qualitatively easier: there
are no local optima to worry about, since *any* stationary point (any point with zero gradient)
is automatically a global minimum.

A set $S \subseteq \Re^p$ is **convex** if the line segment between any two points of $S$ lies
entirely in $S$; equivalently, every convex combination $\sum_i \alpha_i x_i$ (non-negative
weights summing to $1$) of points of $S$ is itself in $S$. A function $f$ defined on a convex set
is **convex** if
$$f\Big(\sum_{i=1}^m \alpha_i x_i\Big) \le \sum_{i=1}^m \alpha_i f(x_i)$$
for every convex combination of points $x_i \in S$; it is *strictly* convex if the inequality is
strict. Two equivalent, more operational characterizations:

- **First-order condition.** $f$ is convex iff $f(x) \ge f(y) + \nabla f(y)^\top (x-y)$ for all
  $x,y$ in the domain — the first-order Taylor approximation at *any* point lies entirely below
  (or touching) the graph of $f$.
- **Second-order condition.** For a univariate, twice-differentiable $f$, convexity is equivalent
  to $f''(x) \ge 0$ everywhere (a nondecreasing derivative); a function with $f'' \le 0$
  everywhere is *concave*, and $-f$ is then convex. In several dimensions, the analogous
  statement is that $f$ is convex if its Hessian is positive semi-definite everywhere.

There is a substantial toolkit (see Boyd and Vandenberghe) of operations that create or preserve
convexity, which is how one recognizes convexity in a problem that does not present it directly.
One useful fact: every norm is convex, directly from the triangle inequality,
$\|\sum_i \alpha_i x_i\| \le \sum_i \alpha_i \|x_i\|$.

### The MM algorithm

**MM** stands for majorize-minorize; it is less a specific algorithm than a template for building
a problem-specific one. To minimize $f(x)$, construct at the current iterate $x_t$ a **majorizing
function** $g_t$: one that touches $f$ at $x_t$ ($f(x_t) = g_t(x_t)$) and lies above it everywhere
else ($f(x) \le g_t(x)$ for all $x$). Minimize $g_t$ (or just move downhill on it, e.g. with a
Newton step) to get $x_{t+1}$, build a new majorizer $g_{t+1}$, and repeat. Because $g_t$ lies
above $f$ and agrees with it at $x_t$, decreasing $g_t$ is guaranteed to decrease $f$ too — the
algorithm cannot fail to go downhill, and (a real virtue) it never over- or under-shoots
numerically, at the price of often converging slowly. The genuine difficulty is finding a good
majorizer; that is a skill in working with inequalities more than a formula (Lange's book has
extensive discussion).

**Worked example: median regression.** Minimize
$f(\theta) = \sum_i |y_i - z_i^\top \theta| = \sum_i |r_i(\theta)|$. This is convex, since affine
functions are convex, a convex function of an affine function is convex, and sums preserve
convexity. Write $f(\theta) = \sum_i \sqrt{r_i(\theta)^2}$, and use the fact that
$h(x)=\sqrt x$ is concave, so $h(x) \le h(y) + h'(y)(x-y)$ for any $y$ (with equality at $x=y$).
Applying this at $y = r_i(\theta_t)^2$, current value:
$$f(\theta) \le \sum_i \sqrt{r_i(\theta_t)^2} + \frac{r_i(\theta)^2 - r_i(\theta_t)^2}
{2\sqrt{r_i(\theta_t)^2}} = g_t(\theta).$$
Since $\theta_t$ is fixed within this iteration, minimizing $g_t(\theta)$ over $\theta$ reduces
(dropping constants not involving $\theta$) to a **weighted least squares** problem with weights
$w_i = 1/\sqrt{(y_i - z_i^\top\theta_t)^2}$ — intuitively sensible, since it upweights
observations with small current residuals, compensating for the fact that we are using a
squared-error surrogate to approximate an absolute-error objective. The update is
$$\theta_{t+1} = (Z^\top W(\theta_t) Z)^{-1} Z^\top W(\theta_t) Y,$$
with $W(\theta_t)$ diagonal with entries $w_i$. Watch for instability if some residuals are very
small: they get very heavily upweighted.

### The EM algorithm as a special case of MM

The **EM algorithm** — maximization, in this case, so we are using the minorize half of MM — is
most naturally motivated by missing data. Write the complete data as $Y=(X,Z)$ with $Z$ missing;
often $Z$ is a set of *latent variables* introduced purely to make the problem tractable (the
canonical case is component membership in a mixture model), in which case direct maximization of
the observed-data likelihood is also an option and sometimes works better than EM.

The observed-data log-likelihood, $L(\theta\mid x) = f(x;\theta) = \int f(x,z;\theta)\,dz$, is
often intractable because of that integral. EM sidesteps it. Define, for current value
$\theta^t$,
$$Q(\theta;\theta^t) = E\big(\log L(\theta\mid Y) \mid x; \theta^t\big),$$
the expectation taken over $Z$ under its conditional distribution $f(z\mid x;\theta^t)$. The
algorithm:

1. **E step.** Compute $Q(\theta;\theta^t)$ — ideally in closed form. It is a function of both
   $\theta$ (the argument being optimized) and $\theta^t$ (the current value, fixed for this
   step).
2. **M step.** Maximize $Q(\theta;\theta^t)$ over $\theta$ to get $\theta^{t+1}$.
3. Repeat to convergence.

When the M step has no closed form, fall back on the numerical methods above; when the E step has
no closed form, the standard fix is **Monte Carlo EM (MCEM)**: draw $z_j \sim f(z\mid
x,\theta^t)$ (by a short MCMC run if direct sampling is not possible) and approximate $Q$ by a
Monte Carlo average of $\log f(x,z_j;\theta)$. EM (and especially MCEM) is often slow even when
everything is tractable.

EM's monotonicity — it never decreases the likelihood — follows from Jensen's inequality
(equivalently, the information inequality on Kullback-Leibler divergence). In MM language, $Q$
(up to a fixed additive term) is exactly a **minorizing function** for $\log L(\theta)$: tangent
to it at $\theta^t$ and lying below it everywhere, so maximizing $Q$ is guaranteed to raise
$\log L$ at least as much.

**Worked example: mixture models.** Take $f(x;\theta) = \sum_{k=1}^K \pi_k f_k(x;\mu_k,\sigma_k)$,
a $K$-component mixture (normal components, say), with $\theta = \{\pi_k,\mu_k,\sigma_k\}$. The
likelihood is a product over observations of a *sum* over components, which is unpleasant to
maximize directly, and such likelihoods are well known to be multimodal (label-switching among
the components). Take the group membership $z_i \in \{1,\ldots,K\}$ of each observation as the
missing data — "breaking the mixture": if memberships were known, each component's parameters
could be estimated separately by the ordinary sample mean and variance of its members. EM
delivers a *soft* (probabilistic) version of that. The complete-data log-likelihood is
$$\log L(\theta\mid x,z) = \sum_i \sum_k I(z_i=k)\big(\log f_k(x_i;\mu_k,\sigma_k) + \log\pi_k\big),$$
so
$$Q(\theta;\theta^t) = \sum_i\sum_k E\big(I(z_i=k)\mid x_i;\theta^t\big)
\big(\log f_k(x_i;\mu_k,\sigma_k)+\log\pi_k\big),$$
where the conditional expectation is exactly the posterior membership probability, by Bayes'
theorem:
$$p_{ik}^t = \frac{\pi_k^t f_k(x_i;\mu_k^t,\sigma_k^t)}{\sum_j \pi_j^t f_j(x_i;\mu_j^t,\sigma_j^t)}.$$
$Q$ separates into a term in the $\pi_k$'s and a term in the component parameters, so the two can
be maximized independently: for normal components, this gives the weighted (by $p_{ik}^t$) sample
mean and variance for each component, and the average of the $p_{ik}^t$ for each $\pi_k$.

## Optimization under constraints

Constrained optimization is harder than unconstrained, and inequality constraints are harder
still than equality constraints. Sometimes a constraint can be eliminated entirely by
reparameterizing — the log scale for a non-negative parameter (a variance component, say), or a
logit transform for a parameter confined to $(0,1)$ (or, after shifting and scaling, any bounded
interval). When that is not possible, constrained optimization goes by various names
("programming") depending on the type of objective and constraint.

### Convex, linear, and quadratic programming

**Convex programming** minimizes $f(x)$ subject to $h_j(x)\le 0$ for $j=1,\ldots,m$ and
$a_i^\top x = b_i$ for $i=1,\ldots,q$, where $f$ and all the $h_j$ are convex. This form is more
general than it looks: an equality constraint $g(x)=b$ can be written as the pair
$g(x)\le b, -g(x) \le -b$; a lower-bound constraint $h_j(x) \ge b_j$ becomes
$-h_j(x) + b_j \le 0$; and an upper bound $h_j(x) \le b_j$ shifts to $h_j(x)-b_j \le 0$ without
disturbing convexity. A point satisfying all the constraints is called **feasible**.

Good algorithms exist for convex programs with hundreds or thousands of variables and
constraints — the hard part is usually *recognizing* (or engineering, via a change of variables)
that a given problem is one; once that is done, existing solvers take over. **Linear programming**,
**quadratic programming**, **second-order cone programming**, and **semidefinite programming**
are convex programming's special cases, each progressively more expensive computationally.

**Linear programming** minimizes $f(x) = c^\top x$ subject to $m$ inequality constraints
$a_i^\top x \le b_i$ (equivalently $Ax \preceq b$). Each equation $a_i^\top x = b_i$ defines a
hyperplane, so each inequality defines a half-space; minimizing a linear objective over the
intersection of half-spaces must push the solution to a corner (vertex) of the resulting solid —
there is nowhere else for a linear function's minimum to hide. The **simplex method** starts at a
feasible vertex and walks along edges that improve the objective; **interior-point methods**
(below) offer an alternative route.

### Equality constraints

**Linear equality constraints**, $Ax=b$, can be eliminated entirely rather than handled directly.
The **null space** of $A$ is $\{\delta : A\delta = 0\}$. Given any one feasible point $x_c$ (e.g.
$x_c = A^+ b$, via the pseudo-inverse), every other feasible point is $x = x_c + B z$ for
$z\in\Re^{p-q}$, where $B$'s columns span the null space of $A$. Defining $h(z) = f(x_c+Bz)$
turns the problem into an *unconstrained* one in the smaller space of $z$, with
$\nabla h(z) = B^\top \nabla f(x_c+Bz)$ and $H_h(z) = B^\top H_f(x_c+Bz)\, B$ — any unconstrained
method now applies. ($B$ can be built either from the columns of $V$ in the SVD of $A$
corresponding to zero singular values, or from the columns of $Q_2$ in a QR decomposition of
$A^\top$, corresponding to the zero rows of $R$.)

**Nonlinear equality constraints**, $g_i(x)=b_i$ for $i=1,\ldots,q$, are handled instead with a
**Lagrange multiplier**: form
$$L(x,\lambda) = f(x) + \lambda^\top (g(x)-b),$$
and setting the derivative of $L$ with respect to *both* $x$ and $\lambda$ to zero gives a
critical point of $f$ that also respects the constraint.

**Worked example: quadratic programming with affine equality constraints.** Minimize
$f(x) = \tfrac12 x^\top Q x + m^\top x + c$ subject to $Ax=b$, with $Q$ positive semi-definite
(this is a simplification of quadratic programming in general, which allows affine *inequality*
constraints $Ax - b \preceq 0$). The Lagrangian is
$L(x,\lambda) = \tfrac12 x^\top Q x + m^\top x + c + \lambda^\top(Ax-b)$; differentiating gives
$$\frac{\partial L}{\partial x} = m + Qx + A^\top \lambda = 0, \qquad
\frac{\partial L}{\partial \lambda} = Ax - b = 0,$$
a linear system for $(x,\lambda)$ together:
$$\begin{pmatrix} x \\ \lambda \end{pmatrix} =
\begin{pmatrix} Q & A^\top \\ A & 0 \end{pmatrix}^{-1}
\begin{pmatrix} -m \\ b \end{pmatrix},$$
which, using standard block-matrix inverse formulas, resolves to
$x^* = -Q^{-1}m + Q^{-1}A^\top (AQ^{-1}A^\top)^{-1}(AQ^{-1}m + b)$ — computable with the
techniques for structured linear systems from Unit 10.

### The Lagrangian dual

Sometimes reformulating a constrained problem eases the optimization rather than solving it
directly; we look at the **Lagrangian dual**. Let $f(x)$ be the objective, with constraints
$g_i(x)=0$ ($i=1,\ldots,q$) and $h_j(x)\le 0$ ($j=1,\ldots,m$), and Lagrangian
$$L(x,\lambda,\mu) = f(x) + \sum_i \lambda_i g_i(x) + \sum_j \mu_j h_j(x).$$
The original problem is equivalent to
$\inf_x \sup_{\lambda,\mu:\, \mu_j \ge 0} L(x,\lambda,\mu)$: the inner supremum sends $L$ to
$+\infty$ whenever a constraint is violated, so the infimum is only ever taken over feasible $x$.
Swapping the order of infimum and supremum can only decrease the value —
$$\sup_{\lambda,\mu:\,\mu_j\ge0} \inf_x L(x,\lambda,\mu) \le \inf_x \sup_{\lambda,\mu:\,\mu_j\ge0} L(x,\lambda,\mu)$$
— because $\inf_x L(x,\lambda,\mu) \le f(x^*)$ for the true minimizer $x^*$. This defines the
**Lagrange dual function** $d(\lambda,\mu) = \inf_x L(x,\lambda,\mu)$ and the **dual problem**,
finding the best lower bound $\sup_{\lambda,\mu:\,\mu_j\ge0} d(\lambda,\mu)$.

The dual problem is *always* a convex optimization problem — $d$ is concave, being a pointwise
infimum of a family of affine functions of $(\lambda,\mu)$ — even when the primal is not. If the
primal and dual optimal values coincide there is said to be **no duality gap**; for convex
programs, this holds under mild extra conditions ("constraint qualifications"), which are met by
essentially any standard-form convex program. When $x$ can be eliminated from $L$ in closed
form, maximizing $d(\lambda,\mu)$ over the multipliers is often an easier constrained problem, and
one further fact (Boyd, p. 242) closes the loop: $\mu_i^* = 0$ unless the $i$th inequality
constraint is *active* at $x^*$, and $x^*$ itself minimizes $L(x,\lambda^*,\mu^*)$ — so once the
optimal multipliers are known, recovering $x^*$ is an unconstrained (and, if $L$ is strictly
convex there, uniquely solvable) problem.

**Example.** Minimize $x^\top x$ subject to $Ax=b$. The Lagrangian is
$L(x,\lambda) = x^\top x + \lambda^\top(Ax-b)$, quadratic in $x$, so the infimum over $x$ comes
from $\nabla_x L = 2x + A^\top\lambda = 0$, i.e. $x = -\tfrac12 A^\top \lambda$; substituting back
gives the dual function
$$d(\lambda) = -\tfrac14 \lambda^\top AA^\top \lambda - b^\top \lambda,$$
a concave quadratic — so the original constrained problem reduces to this unconstrained one.
Another classic instance is the support vector machine classifier: with $n$ pairs
$(x_i,y_i)$, $x_i \in \Re^p$, the primal problem optimizes in $\Re^p$ while the dual optimizes in
$\Re^n$ — worth reaching for when $n \ll p$.

### KKT conditions

**Karush-Kuhn-Tucker (KKT)** theory generalizes the Lagrange multiplier approach to give
sufficient conditions for a constrained minimum, mixing equality and inequality constraints. With
$f$, the $g_i$, and the $h_j$ continuously differentiable near $x^*$, and $L$ as above: for
nonconvex problems, *if* $x^*$ and $(\lambda^*,\mu^*)$ are primal and dual optimal with no
duality gap, then
$$h_j(x^*) \le 0, \quad g_i(x^*) = 0, \quad \mu_j^* \ge 0, \quad \mu_j^* h_j(x^*) = 0, \quad
\nabla f(x^*) + \sum_i \lambda_i^* \nabla g_i(x^*) + \sum_j \mu_j^* \nabla h_j(x^*) = 0.$$
For *convex* problems the implication reverses too: KKT conditions holding is enough to certify
$x^*,(\lambda^*,\mu^*)$ as optimal with no duality gap. Many algorithms for convex optimization
are, from this angle, just ways of solving the KKT system.

There is a second-order refinement, assuming $L$ twice differentiable. A **tangent direction**
$w$ with respect to $g$ at a feasible $x^*$ satisfies $\nabla g_i(x^*)^\top w = 0$: moving in
direction $w$ stays (to first order) on the constraint surface. An **active** inequality
constraint is one with $h_j(x^*)=0$ exactly (as opposed to strictly satisfied,
$h_j(x^*)<0$) — the only inequality constraints that matter locally are the ones currently
"touched". If the Lagrangian's gradient vanishes at $x^*$ and $w^\top H_L(x^*,\lambda,\mu)\,w > 0$
for every tangent direction $w$ of the active constraints (equality and active inequality alike),
then $x^*$ is a local minimum: intuitively, positive definiteness of the Hessian is only needed
in the directions that actually stay feasible — a direction that leaves the feasible region is
not a threat, however the quadratic form behaves there.

### Interior-point methods

**Interior-point** methods, of which the **barrier method** is one instance, solve a convex
program by repeatedly calling Newton's method on a sequence of related *equality-constrained*
problems — turning the harder inequality-constrained problem into a sequence of easier ones.
Start from the convex-programming form above, and move the inequality constraints into the
objective as an indicator penalty,
$$f(x) + \sum_{j=1}^m I_-(h_j(x)), \qquad I_-(u) = \begin{cases} 0 & u \le 0 \\ \infty & u > 0,\end{cases}$$
which enforces feasibility exactly but is not differentiable, so Newton's method cannot be used
on it directly. Approximate the indicator with a smooth **log barrier**:
$$\tilde f(x) = f(x) - \frac1{t^*}\sum_{j=1}^m \log(-h_j(x)),$$
convex and differentiable, and increasingly close to the true objective as $t^*\to\infty$ — the
barrier term blows up as $x$ approaches the boundary of the feasible set, so starting feasible
and running Newton's method on $\tilde f$ (subject only to the remaining linear equality
constraints $Ax=b$) keeps every iterate feasible. As the iterations proceed, $t^*$ is
increased, letting the solution approach the boundary if that is where the true minimum lies.

Newton's method with linear equality constraints works by (1) starting at a feasible
$x_0$ (so $Ax_0=b$) and (2) restricting every step to a *feasible direction*,
$A(x_{t+1}-x_t)=0$. Enforcing that requires solving a linear system with the same block structure
as the quadratic-programming example above:
$$\begin{pmatrix} x_{t+1}-x_t \\ \lambda \end{pmatrix} =
\begin{pmatrix} H_{\tilde f}(x_t) & A^\top \\ A & 0 \end{pmatrix}^{-1}
\begin{pmatrix} -\nabla \tilde f(x_t) \\ 0 \end{pmatrix},$$
which should not be surprising, since Newton's method is always, at bottom, substituting a
quadratic approximation for the true objective.

### Software

For general convex optimization in Python, see `cvxopt` — it has solvers for a range of specific
convex-optimization problem types (`help(cvxopt.solvers)`), plus a general-purpose one,
`cvxopt.solvers.cp`; specifying the objective and constraints for it is fairly involved. Other
options worth knowing about: MATLAB's `fmincon()` and its linear/quadratic programming tools, the
CVX system, and the CVXR package in R (whose developers include Stephen Boyd).

## Summary

The methods above trade off in a fairly consistent way. According to Lange, MM and EM are
numerically stable and simple to implement but can converge very slowly; Newton's method
converges very fast but comes with the fragility discussed above (bad starting values, loss of
positive definiteness, possible divergence); quasi-Newton methods sit in between on both counts.
Convex optimization tools tend to be reached for specifically when there are constraints to
satisfy.

One caution about constrained optimization in particular: it hands you a point estimate, but
quantifying the *uncertainty* of that estimate is genuinely harder than in the unconstrained
case. A workable strategy is to discard the inactive inequality constraints (they are not
binding at the optimum) and reparameterize away the active equality constraints, reducing to an
unconstrained problem in a lower-dimensional space — the Hessian there can then be used in the
usual way to estimate the information matrix.

## Sources

This chapter merges the "Unit 11: Optimization" notes as taught in Berkeley STAT 243, in the
fall-2024 and fall-2025 offerings — the two are essentially identical, and fall-2025 (which
carries a small notational fix to the EM section, $Q(\theta;\theta^t)$ rather than
$Q(\theta\mid\theta^t)$) was used as the primary text throughout:

- `01-1-notation.md` — notation for the gradient, Hessian, and iterate sequence.
- `02-2-overview.md` — the minimization setup, first/second-order conditions, scope, and unit
  goals.
- `03-3-univariate-function-optimization.md` — golden section search, bisection, Newton-Raphson,
  the secant variant, and Newton's failure modes (a small number of transcription artifacts in
  the lossless conversion — dropped inequality signs in two places — were checked and corrected
  against the source `.qmd`).
- `04-4-convergence-ideas.md` — convergence metrics, starting values, the Rastrigin function, and
  the order-of-convergence derivation for Newton's method.
- `05-5-multivariate-optimization.md` — profiling, multivariate Newton-Raphson (the Mauna Loa
  CO$_2$ example), Fisher scoring, IRLS, descent and quasi-Newton (BFGS) methods, stochastic
  gradient descent, coordinate descent and the lasso, Nelder-Mead, and simulated annealing.
- `06-6-basic-optimization-in-python.md` — `scipy.optimize`, automatic differentiation, practical
  tuning advice, and combinatorial optimization over discrete spaces (originally numbered
  "Section 7" within the same file).
- `07-8-convexity.md` — convex sets and functions, the MM algorithm (median regression example),
  and EM as a special case of MM (mixture-model example).
- `08-9-optimization-under-constraints.md` — convex/linear/quadratic programming, equality
  constraints, the Lagrangian dual, KKT conditions, interior-point/barrier methods, and the
  chapter summary (originally numbered "Section 10" within the same file). One dropped matrix
  entry in the interior-point linear system, and a stray LaTeX `\label`, were corrected against
  the source `.qmd`.

Both offerings are licensed CC BY 4.0 by the instructor (Christopher Paciorek). A third supplied
source, `stat243-fall-2021/units/unit11-optim.md`, is a partial, model-reconstructed transcription
of an image-only PDF (fidelity: reconstructed, licence CC0-1.0) covering only the tail end of the
constraints material; since that same material is present in full, lossless form in the
2024/2025 notes, the 2021 fragment was not drawn on directly.

Referenced but not supplied, and not reproduced here beyond the pointer: Gentle's *Computational
Statistics*, Lange's *Optimization*, Monahan's *Numerical Methods of Statistics*, Givens and
Hoeting's *Computational Statistics*, Boyd and Vandenberghe's *Convex Optimization* (and the
associated Stanford EE364a course materials), a set of 2020 lecture videos in the course's media
gallery (on convergence, profiling, multivariate Newton-Raphson, descent methods, SGD, coordinate
descent, Nelder-Mead, optimization in practice, and constrained optimization), Jung et al. (2014,
*JASA* 109:1355) on MM for SNP biomarker detection, the `glmnet` *Journal of Statistical Software*
paper, Mittal et al. on penalized survival regression at large $p$, and an online interactive
illustration of Nelder-Mead at benfrederickson.com.

---

[← 37. Numerical Linear Algebra](37-numerical-linear-algebra.md) · [Contents](index.md) · [39. Good Practices for Graphics →](39-good-practices-for-graphics.md)
