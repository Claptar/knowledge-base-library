---
title: "24. Problem Set 8"
course: "Berkeley Stat 243 Fall 2024"
chapter: 24
source: "https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 243 Fall 2024](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/schedule.qmd), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 24. Problem Set 8

## What this covers

This chapter is Problem Set 8 of Berkeley's Stat243, assigned in three offerings (fall 2021,
fall 2024, fall 2025) that share one underlying question: a model's likelihood depends on a
quantity that is only partly seen — a continuous variable reported through its sign (probit
regression) or reported at all only below some threshold (censored regression) — and the
assignment asks you to fit it two independent ways, an EM algorithm built around the missing
piece and a direct numerical maximization of the observed-data likelihood, so that each checks
the other. It assumes the course's own Unit 11 material on the EM algorithm — in particular the
notation, used only implicitly here, that splits the complete data $Y=(X,Z)$ into what is observed,
$X$, and what is missing, $Z$ — together with ordinary linear and logistic regression and the
standard normal density $\phi$ and CDF $\Phi$. Depending on the offering it also assumes
`scipy.optimize` and JAX or PyTorch automatic differentiation (fall 2024, fall 2025), R's `optim()`
and `nlm()` (fall 2021), and, for one fall-2021 problem only, Unit 9's material on importance
sampling.

## A normal variable seen only through a threshold

Two versions of the same idea recur across the three offerings.

**All-or-nothing (probit regression, fall 2024).** The probit model for a binary outcome,
$Y_i\sim\text{Ber}(p_i)$ with $p_i=P(Y_i=1)=\Phi(X_i^\top\beta)$, is rewritten with one latent
variable per observation:
$$
y_i = I(z_i>0), \qquad z_i\sim\mathcal N(X_i^\top\beta,\,1).
$$
Nothing about $z_i$ is ever observed except which side of zero it fell on.

**Partial censoring (censored regression, fall 2025 and fall 2021).** Here most of the data is seen
in full: $Y_i\sim\mathcal N(\beta_0+\beta_1x_i,\sigma^2)$, but any observation with $Y_i$ above a
fixed threshold $\tau$ is reported only as having exceeded it — the value itself is withheld. Of the
$n$ observations, some number $n_c$ end up censored this way, stochastically, depending on how many
draws land above $\tau$. The assignment gives two motivating examples: pollutant concentrations
reported as "below the limit of detection" (censoring in the left tail), and tax records in which
the incomes of the wealthy are reported only as exceeding some round number such as one million
dollars.

In both cases the EM algorithm's expectation step needs the conditional distribution of a normal
variable given that it lies on one side of a cutoff — a **truncated normal** — and specifically only
its first two moments. Quoting the assignment's own formulae (attributed to Johnson and Kotz's
reference volumes on distributions, with the general case also on Wikipedia's truncated-normal
page): for $W\sim\mathcal N(\mu,\sigma^2)$ truncated to $W>\tau$,
$$
E(W\mid W>\tau) = \mu+\sigma\rho(\tau^*), \qquad
V(W\mid W>\tau) = \sigma^2\bigl(1+\tau^*\rho(\tau^*)-\rho(\tau^*)^2\bigr),
$$
$$
\rho(\tau^*) = \frac{\phi(\tau^*)}{1-\Phi(\tau^*)}, \qquad \tau^* = \frac{\tau-\mu}{\sigma}.
$$
These two moments are exactly what the E-step needs to plug in for whichever quantity is hidden —
the latent $z_i$ in the probit case, the unobserved value behind a censored $Y_i$ in the other — and
they are common to every derivation asked for below. Each assignment also flags the same structural
point: once the expectation is taken, the resulting expected complete-data log-likelihood turns out
to be exactly an ordinary linear regression of some derived quantity on the covariates, so the
maximization step reduces to a call to a regression routine rather than a fresh optimization.

## Checking EM against a direct likelihood maximization

Every offering also asks for the same observed-data log-likelihood maximized directly, without
introducing any latent variable — for the censored model this replaces the truncated-normal moments
used in the EM derivation with the tail probability $P(Y_i>\tau)$ for each censored point — using a
general-purpose optimizer: `scipy.optimize.minimize` with BFGS (fall 2024, fall 2025) or R's
`optim()` with BFGS (fall 2021). Since a correct EM derivation and a correct direct maximization are
two routes to the same maximum-likelihood estimate, agreement between them is used as a check on
both the EM derivation and its implementation.

Three practical issues recur around this check. First, BFGS can fail to converge from a poor
starting point, which the assignments ask you to demonstrate directly by searching for starting
values that break it, and then checking whether Nelder-Mead still finds the optimum from the same
place. Second, $\sigma^2$ is constrained to be positive, a constraint an unconstrained optimizer
knows nothing about, so the assignments suggest reparameterizing before optimizing (the fall-2021
version also mentions `optim()`'s `parscale` argument, which rescales the parameters relative to one
another before the optimizer sees them). Third, standard errors need the Hessian of the
log-likelihood at the optimum, and the object `scipy.optimize.minimize` returns as `hess_inv` is
**not** that: it is only the approximation BFGS accumulated along its iterations, not a numerical
derivative evaluated at the optimum itself. The Python offerings therefore ask for the real thing
computed independently — with `numdifftools`, and again by building a Hessian function with JAX or
PyTorch automatic differentiation. Building the objective, its gradient, and its Hessian this way
also lets the assignment ask for the objective and gradient to be just-in-time compiled (`jit`/`@jit`
in JAX, `torch.compile` in PyTorch) so that timing and iteration counts against plain
finite-difference BFGS are worth comparing, not just the resulting estimates.

## Exercises

### 1. EM for a normal seen only through a threshold

Work whichever variant matches your course offering.

**Probit-regression variant (fall 2024).** Take the complete data for the model above to be
$\{Y,Z\}$.

a. Design an EM algorithm to estimate $\beta$. Use the truncated-normal moments given above; be
   careful to distinguish $\beta$ from its current iterate $\beta^t$ throughout, both when taking
   the expectation and when maximizing; and make sure your calculation uses the fact that, for each
   $i$, $y_i$ already tells you whether $z_i$ is bigger or smaller than $0$. The expected
   log-likelihood should be analytically maximizable, and is worth recognizing as an ordinary
   regression of some new quantities $m_i$ — functions of $\beta^t$ and $y_i$ — on $X$.
b. Propose a way to get reasonable starting values for $\beta$.
c. Write a Python function implementing the algorithm, using the starting values from (b); existing
   regression routines may be used for the update step. Include a stopping criterion.
d. Test the function on data simulated from the model with $n=100$. Choose $\beta_1$ by trial and
   error — simulate for a candidate value and fit an ordinary logistic regression to check the
   resulting signal-to-noise ratio, then adjust — so that $\hat\beta_1/\text{se}(\hat\beta_1)\approx
   2$, with $\beta_2=\beta_3=0$.

**Censored-regression variant (fall 2025, fall 2021).** With $Y_i\sim\mathcal
N(\beta_0+\beta_1x_i,\sigma^2)$ and some observations censored above $\tau$ as described above, take
the complete data to be the fully-observed values together with the actual (unobserved) values
behind the censored ones, and let $\theta=(\beta_0,\beta_1,\sigma^2)$.

a. Design an EM algorithm for $\theta$. Treat the fact that a censored observation exceeded $\tau$
   as part of the observed data $X$, alongside the values that were reported in full. Write the
   complete-data log-likelihood as a sum of a term for the observed values and a term for the
   censored ones, conditioning the latter term on exceeding $\tau$, and use the truncated-normal
   moments above for that conditional expectation. Keep $\theta$ and its current iterate $\theta^t$
   distinct throughout. You should find that the expected log-likelihood is an ordinary regression of
   $\{Y_{\text{obs}}, m^t\}$ on $\{x\}$, where the values $m_i^t$ — functions of $\theta^t$ — stand
   in for the censored observations; the resulting estimator for $\sigma^2$ should have a numerator
   equal to the usual sum of squares for the observed data plus one further term, which is worth
   interpreting statistically. The maximization should again be analytic.
b. Propose reasonable starting values for the three parameters, as functions of the observed data.
c. Implement the algorithm — in Python with `statsmodels` for the regression update (fall 2025), or
   in R with `lm()` (fall 2021), with auxiliary functions as needed and a stopping criterion — and
   test it on data simulated from the course's `ps8.py` or `ps8.R` code, both at a modest censoring
   rate (about 20%) and a high one (about 80%).

### 2. Checking EM against a direct maximum-likelihood fit

**Python/JAX or PyTorch variant (fall 2024, fall 2025).**

a. Write the negative log-likelihood of the observed data as an objective function in JAX or PyTorch
   syntax.
b. Estimate the parameters for your test cases with `scipy.optimize.minimize` (BFGS), and compare
   the number of iterations against your EM implementation — the two approaches should agree on the
   estimates, which is itself a check on your EM derivation and code. (Fall 2024 also asks you to
   compute standard errors here, from the inverse Hessian, using `numdifftools` rather than
   `hess_inv` — see the caution above — watching for loss-of-precision warnings that may mean
   switching JAX or PyTorch to 64-bit floats. Fall 2025 instead asks you to consider
   reparameterizing before fitting, and defers the Hessian comparison to part (d)/(e).)
c. Try a variety of starting values and find some that make BFGS fail to converge. Do the same
   starting values converge under Nelder-Mead?
d. Build a gradient function using automatic differentiation, set up the objective and gradient for
   just-in-time compilation, and refit with BFGS supplying this gradient. Confirm the estimates
   match part (b), and compare iteration count and timing against relying on scipy's numerical
   differentiation.
e. Build a Hessian function the same way (automatic differentiation, JIT-compiled) and use it to get
   the standard errors at the optimum. Compare this Hessian, and the resulting standard errors, to
   whichever alternative your offering used in (b) — `numdifftools` (fall 2024) or the `hess_inv`
   returned by `minimize` (fall 2025), bearing in mind the same caution that `hess_inv` is only the
   approximation accumulated during BFGS, not a numerical derivative at the optimum.

**R/`optim()` variant (fall 2021).** Using `optim()` with the BFGS method — considering
reparameterization, and possibly the `parscale` argument — estimate the parameters and their
standard errors for your simulated test cases, and compare the iteration counts of EM and BFGS as a
check on each other.

### 3. Importance sampling and tail weight (fall 2021)

Consider estimating $\phi=E(X)$ and $\phi=E(X^2)$ under a density $f$ by importance sampling from a
different density $g$, using a Pareto density $p(x)=\beta\alpha^\beta/x^{\beta+1}$ for
$\alpha<x<\infty$, $\alpha,\beta>0$, whose mean is $\beta\alpha/(\beta-1)$ for $\beta>1$ (and does
not exist otherwise) and whose variance is $\beta\alpha^2/\bigl[(\beta-1)^2(\beta-2)\bigr]$ for
$\beta>2$ (and does not exist otherwise).

a. Does the tail of the Pareto decay more quickly or more slowly than that of an exponential
   distribution?
b. Let $f$ be an exponential density with rate $1$, shifted right by $2$ so that $f(x)=0$ for $x<2$,
   and pretend you cannot sample from $f$ directly. Using importance sampling with $g$ a Pareto
   distribution with $\alpha=2,\ \beta=3$, and $m=10{,}000$ draws, estimate $E(X)$ and $E(X^2)$ and
   compare against the known values for the shifted exponential. Recalling that
   $\text{Var}(\hat\phi)\propto\text{Var}\bigl(h(X)f(X)/g(X)\bigr)$, plot histograms of both
   $h(x)f(x)/g(x)$ and the raw weights $f(x)/g(x)$ to judge whether $\text{Var}(\hat\phi)$ is large,
   and note whether any extreme weights would dominate $\hat\phi$.
c. Now swap roles: let $f$ be the Pareto distribution above (pretending you cannot sample from it)
   and $g$ the shifted exponential, and answer the same questions, comparing against the known
   Pareto moments.

### 4. Mapping a genuinely multimodal objective: the helical valley (fall 2021)

Using the "helical valley" function defined in the course's `ps8.R` file, plot slices of it — fixing
one input and plotting the function as a surface in the other two, for instance with `image()`,
`contour()`, or `persp()` (or their `ggplot2` equivalents) — to get a feel for its shape. Then use
`optim()` and `nlm()` (or `optimx()`) to find its minimum from a range of different starting points,
and use what you find to assess whether the function has more than one local minimum.

### 5. Extra credit: a small neural network for nonlinear regression (fall 2025)

Fit a basic one- or two-layer neural network — most easily built in PyTorch — to a nonlinear
regression/prediction problem with a single predictor. Explore how sensitive the fit is to starting
values, choice of optimizer, and learning rate, and look for signs of overfitting, bearing in mind
that deep networks are often surprisingly robust to overfitting despite their large number of
parameters.

## Sources

- `docs/statistical-computing/berkeley/stat243/fall-2024/ps/ps8.md` — converted losslessly from
  `ps/ps8.qmd`, berkeley-stat243 fall-2024, CC BY 4.0. Problem 1: the probit-regression EM
  algorithm. Problem 2: the direct-maximization and JAX/PyTorch automatic-differentiation exercise.
- `docs/statistical-computing/berkeley/stat243/fall-2025/ps/ps8.md` — converted losslessly from
  `ps/ps8.qmd`, berkeley-stat243 fall-2025, CC BY 4.0. Problem 1: the censored-regression EM
  algorithm (Python/`statsmodels`). Problem 2: the direct-maximization and automatic-differentiation
  exercise. Problem 3: the extra-credit neural-network exercise.
- `docs/statistical-computing/berkeley/stat243/stat243-fall-2021/ps/ps8.md` — reconstructed by a
  model from a PDF with no text layer (berkeley-stat243 stat243-fall-2021, CC0-1.0); its own source
  note flags the prose as paraphrase and every equation as unverified, so exact wording drawn from
  it should be treated as a pointer to the original PDF rather than settled fact. Problem 1: the
  importance-sampling exercise. Problem 2: the helical-valley optimization exercise. Problem 3: the
  censored-regression EM algorithm (R) and its direct-BFGS check.
- Referred to but not contained in any of the three files: the course's Unit 11 lecture notes on the
  EM algorithm, including the $X$/$Y$/$Z$ observed/complete/missing-data notation the hints assume;
  Unit 9's material on importance sampling (fall 2021 only); Problem Set 1, for the formatting and
  attribution requirements each version points back to; the simulation scripts `ps8.py` (fall 2025)
  and `ps8.R` (fall 2021, which also defines the helical-valley function); the R bootcamp materials
  on `image()`, `contour()`, and `persp()` (fall 2021); Johnson and Kotz's reference volumes on
  distributions and Wikipedia's page on the truncated normal distribution, both cited for the
  truncated-normal moments; and the documentation for `numdifftools`, JAX, PyTorch, and R's `optimx`
  package.

---

[← 23. Problem Set 7](23-problem-set-7.md) · [Contents](index.md) · [25. Comparing R and Python Semantics →](25-comparing-r-and-python-semantics.md)
