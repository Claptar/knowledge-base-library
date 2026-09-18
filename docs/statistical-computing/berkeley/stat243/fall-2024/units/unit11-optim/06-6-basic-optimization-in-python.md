---
title: 6. Basic optimization in Python
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) — berkeley-stat243 · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 6. Basic optimization in Python

### Core optimization functions

Scipy provides various useful optimization functions via `scipy.optimize`, including many of the algorithms discussed in this unit.

- `minimize_scalar` implements golden section search (`golden`) and interpolation combined with golden section search (`brent`, akin to `optimize` in R).
- `minimize` implements various methods for multivariate optimization including Nelder-Mead and BFGS. You can choose which
    method you prefer and can try multiple methods. You can supply a
    gradient function for use with the Newton-related
    methods but it can also calculate numerical derivatives on the fly.
- One can provide a variety of nonlinear, linear, and simple bounds constraints as well, though certain types of constraints can only be used with certain algorithms.

Here's a very basic example of using `minimize` with the Mauna Loa CO2 example we saw earlier when hand-coding Newton-Raphson. Here we'll include the unknown variance as an additional parameter so we have a full likelihood. And as mentioned previously, we could profile out $\beta_0$ and $\beta_1$ and $\sigma^2$, but we won't do that here so as to illustrate multivariate Newton-Raphson.

```python
#| eval: False

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.optimize import minimize

data = pd.read_csv(os.path.join('..','data', 'co2_annmean_mlo.csv'),
    header = 0, names = ['year','co2','unc'])

## Center years for better numerical behavior
data.year = data.year - np.mean(data.year)

beta2_init = 50
implicit_covar = np.exp(data.year/beta2_init)

X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params

def nll(params, data):
    # params[3] is log of sigma^2 to address constraint
    n = len(data.year)
    fitted = params[0] + params[1] * np.exp(data.year / params[2])
    return (n/2)*params[3] + 0.5 * np.sum((data.co2 - fitted)**2) / np.exp(params[3])

sigma2_init = np.mean((data.co2-model.fittedvalues)**2)

inits = (beta0_init, beta1_init, beta2_init, np.log(sigma2_init))

# Optimization using Nelder-Mead
start_time = time.time()
fit1 = minimize(nll, inits, args=(data), method='Nelder-Mead', options={'disp': True})
end_time = time.time()
print("Nelder-Mead Optimization:")
print(fit1)
print("Execution Time:", end_time - start_time, "seconds")

# Optimization using BFGS
start_time = time.time()
fit2 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})
end_time = time.time()
print("\nBFGS Optimization:")
print(fit2)
print("Execution Time:", end_time - start_time, "seconds")

## IMPORTANT: `hess_inv` is just the final estimate from BFGS not
## a direct numerical estimate of the Hessian at the optimum.
## If you need the Hessian, calculate it directly, e.g, using `numdifftools`.

# BFGS with specific relative tolerance on 'x', given precision loss message.
## See `https://docs.scipy.org/doc/scipy/reference/optimize.minimize-bfgs.html`.

fit2_alt = minimize(nll, inits, args=(data), method='BFGS',
    options={'disp': True, 'xrtol': 1e-6})


# Different starting value (recall non-positive definite Hessian)


beta2_init = 100
implicit_covar = np.exp(data.year/beta2_init)
X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params
sigma2_init = np.mean((data.co2-model.fittedvalues)**2)
inits = (beta0_init, beta1_init, beta2_init, np.log(sigma2_init))
fit3 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})

beta2_init = 10
implicit_covar = np.exp(data.year/beta2_init)
X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params
sigma2_init = np.mean((data.co2-model.fittedvalues)**2)
inits = (beta0_init, beta1_init, beta2_init, np.log(sigma2_init))
fit4 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})

# Arbitrarily bad starting values
inits = (10, 0, 10000, 0.1)
fit5 = minimize(nll, inits, args=(data), method='Nelder-Mead', options={'disp': True})
fit6 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})
```

```python
#| include: False
#| code-fold: True
#| eval: False

## Real example with US precip data -- not included in 2023 for sake of time.
## In the demo code (not shown here; see the source qmd file), we'll work our way through a real example of optimizing a likelihood for some climate data on extreme precipitation.

import numpy as np
import matplotlib.pyplot as plt

data_file = os.path.join('..', 'data', 'precipData.txt')
y_hundredths = np.genfromtxt(data_file, missing_values = 'NA')  # precip in hundredths of inches
y_hundredths = y_hundredths[~np.isnan(y_hundredths)]
y = y_hundredths / 100  # precip now in inches

npy=31+28+31 # number of days in winter season
cutoff = 1 / 25.4  # Convert 1 mm to inches
thresh = np.percentile(y[y > cutoff], 98,)

# Create a histogram of the data
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(y, bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Precipitation (inches)')
plt.ylabel('Frequency')
plt.title('Histogram of All Data')

plt.subplot(1, 2, 2)
plt.hist(y[y > thresh], bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Precipitation (inches)')
plt.ylabel('Frequency')
plt.title(f'Histogram of Wet Days (Precip > {np.round(thresh,2)} inches)')
plt.tight_layout()
plt.show(block=False)

# Define objective (negative log-likelihood) function

def pp_negloglik(par, y, thresh, npy):
    mu, sc, sh = par
    uInd = y > thresh

    # Invalid parameter values or data/parameter combos:
    if sc <= 0:
        return 1e6
    if (1 + ((sh * (thresh - mu)) / sc) < 0):
        return 1e6

    y = (y - mu) / sc
    y = 1 + sh * y

    if np.min(y[uInd]) <= 0:
        return 1e6
    else:
        ytmp = y.copy()
        ytmp[~uInd] = 1 # 'zeroes' out those below the threshold after applying the log in next line

        l = np.sum(uInd * np.log(sc)) + np.sum(uInd * np.log(ytmp) * (1 / sh + 1)) + \
                   (len(y) / npy) * np.mean((1 + (sh * (thresh - mu)) / sc) ** (-1 / sh))

    return l


# Initial parameter values
y_exc = y[y > thresh]
in2 = np.sqrt(6 * np.var(y_exc)) / np.pi
in1 = np.mean(y_exc) - 0.57722 * in2
init0 = [in1, in2, 0.1]

# Optimization using Nelder-Mead
start_time = time.time()
fit1 = minimize(pp_negloglik, init0, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
end_time = time.time()
print("Nelder-Mead Optimization:")
print(fit1)
print("Execution Time:", end_time - start_time, "seconds")

# Optimization using BFGS
start_time = time.time()
fit2 = minimize(pp_negloglik, init0, args=(y, thresh, npy), method='BFGS', options={'disp': True})
end_time = time.time()
print("\nBFGS Optimization:")
print(fit2)
print("Execution Time:", end_time - start_time, "seconds")

mle = fit2.x
# Need code to get Hessian at optimum; `hess_inv` is NOT that.

# Different starting values
init1 = [np.mean(y[y > thresh]), np.std(y[y > thresh]), -0.1]
fit1a = minimize(pp_negloglik, init1, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
fit2a = minimize(pp_negloglik, init1, args=(y, thresh, npy), method='BFGS', options={'disp': True})

# Bad starting value for BFGS
init2 = [thresh, 0.01, .5]
fit1b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='Nelder-Mead', options={'disp': True})
fit2b = minimize(pp_negloglik, init2, args=(y, thresh, npy), method='BFGS', options={'disp': True})

# Data on a different scale
y_exc2 = y[y > thresh] * 1000
y2 = y * 1000
thresh2 = thresh * 1000

init3 = [np.mean(y_exc2), np.std(y_exc2), 0.1]
fit3 = minimize(pp_negloglik, init3, args=(y2, thresh2, npy), method='Nelder-Mead', options={'disp': True})
fit4 = minimize(pp_negloglik, init3, args=(y2, thresh2, npy), method='BFGS', options={'disp': True})

# Plot the objective function
n_grid = 30
loc_vals = np.linspace(0, 5, n_grid)
scale_vals = np.linspace(0.1, 3, n_grid)
shape_vals = np.linspace(-0.3, 0.3, 16)

loc_grid, scale_grid, shape_grid = np.meshgrid(loc_vals, scale_vals, shape_vals, indexing='ij')
par_grid = np.column_stack((loc_grid.ravel(), scale_grid.ravel(), shape_grid.ravel()))
obj = np.apply_along_axis(pp_negloglik, 1, par_grid, y=y, thresh=thresh, npy=npy)

fig, axes = plt.subplots(4, 4, figsize=(14, 10))
for i, shape_value in enumerate(shape_vals):
    ax = axes[i // 4, i % 4]
    obj_matrix = np.array(obj[par_grid[:,2] == shape_value]).reshape(n_grid, n_grid).T
    im = ax.imshow(obj_matrix, extent=(0, 5, 0.1, 3), cmap='viridis', vmin=40, vmax=80, aspect='auto', origin='lower')
    ax.set_title(f"shape = {shape_value:.2f}")

fig.colorbar(im, ax=axes, label="Objective Function Value")
plt.tight_layout()

plt.show(block=False)
```

### Automatic differentiation (AD)

Optimizers that use derivative information often allow you to pass in
a gradient function and possibly a Hessian function.

Automatic differentiation is basically the implementation of the chain rule
on a computer, building up derivative information for a potentially complicated
calculation from the known derivatives of basic functions (such as multiplication,
exponentiation, etc.). This involves some careful software engineering that
generates the code that will calculate the derivative via the chain rule. Given that it's
*just* the chain rule, it gets surprisingly complicated.

However, from a user perspective, it's often simple to use if you are able
to write your calculation using JAX or PyTorch or another AD-enabled package.

So if you have an optimizer that takes gradient/Hessian functions, you can probably
pass in JAX or PyTorch versions of those functions.

And of course if you're implementing something yourself, you may want
to consider making use of AD rather than using numerical differentiation.
We saw an example of this in Section 5.

### Various considerations in using the Python functions

As we've seen, initial values are important both for avoiding divergence
(e.g., in N-R), for increasing speed of convergence, and for helping to
avoid local optima. So it is well worth the time to try to figure out a
good starting value or multiple starting values for a given problem.

Scaling can be important. One useful step is to make sure the problem is
well-scaled, namely that a unit step in any parameter has a comparable
change in the objective function, preferably approximately a unit change
at the optimum. Basically if
$x_{j}$ is varying at $p$ orders of magnitude smaller than the other
$x$s, we want to reparameterize to $\tilde{x}_{j}=x_{j}\cdot10^{p}$ and then
convert back to the original scale after finding the answer. Or we may
want to work on the log scale for some variables, reparameterizing as
$\tilde{x}_{j}=\log(x_{j})$.

If the function itself gives very large or small values near the
solution, you may want to rescale the entire function to avoid
calculations with very large or small numbers. This can avoid problems
such as having apparent convergence because a gradient is near zero,
simply because the scale of the function is small. When we use
the log of a likelihood (primarily to avoid over/underflow), that
often helps in this regard as well even if the function would not
over/underflow.

!!! important "Important"
**Always** consider your answer and make sure it makes sense, in particular
that you haven't 'converged' to an extreme value on the boundary of the
space.
:::

Venables and Ripley suggest that it is often worth supplying analytic
first derivatives rather than having a routine calculate numerical
derivatives but not worth supplying analytic second derivatives.

In general for software development it's obviously worth putting more
time into figuring out the best optimization approach and supplying
derivatives. For a one-off analysis, you can try a few different
approaches and assess sensitivity.

The nice thing about likelihood optimization is that the asymptotic
theory tells us that with large samples, the likelihood is approximately
quadratic (i.e., the asymptotic normality of MLEs), which makes for a
nice surface over which to do optimization. When optimizing with respect
to variance components and other parameters that are non-negative, one
approach to dealing with the constraints is to optimize with respect to
the log of the parameter.

## 7. Combinatorial optimization over discrete spaces

Many statistical optimization problems involve continuous domains, but
sometimes there are problems in which the domain is discrete. Variable
selection is an example of this.

*Simulated annealing* can be used for optimizing in a discrete space.
Another approach uses *genetic algorithms*, in which one sets up the
dimensions as loci grouped on a chromosome and has mutation and
crossover steps in which two potential solutions reproduce. An example
would be in high-dimensional variable selection.

*Stochastic search variable selection* is a popular Bayesian technique
for variable selection that involves MCMC.

---

[← 5. Multivariate optimization](05-5-multivariate-optimization.md) · [Up: contents](index.md) · [8. Convexity →](07-8-convexity.md)
