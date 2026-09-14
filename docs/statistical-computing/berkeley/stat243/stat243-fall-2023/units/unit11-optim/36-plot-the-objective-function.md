---
title: Plot the objective function
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Plot the objective function

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

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

plt.show()
```

## Various considerations in using the Python functions

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

**Always** consider your answer and make sure it makes sense, in particular
that you haven't 'converged' to an extreme value on the boundary of the
space.

Venables and Ripley suggest that it is often worth supplying analytic
first derivatives rather than having a routine calculate numerical
derivatives but not worth supplying analytic second derivatives.
One possibility is using software such as Mathematica to do symbolic (i.e., analytic) differentiation and
then writing code to implement the math of the result.
Another is using software that can give derivatives using automatic differentiation
such as `PyTorch`, `jax` and `tensorflow`. We saw an example of using Jax
earlier in the unit.

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

---

[← Data on a different scale](35-data-on-a-different-scale.md) · [Up: contents](index.md) · [7. Combinatorial optimization over discrete spaces →](37-7-combinatorial-optimization-over-discrete-spaces.md)
