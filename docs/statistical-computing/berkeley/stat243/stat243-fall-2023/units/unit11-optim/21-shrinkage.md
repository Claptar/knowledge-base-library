---
title: Shrinkage
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Shrinkage

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

xs[1,:] = delta * xs[1,:] + (1 - delta) * xs[0,:]
xs[2,:] = delta * xs[2,:] + (1 - delta) * xs[0,:]

plt.plot(xs[1, 0], xs[1, 1], 'ro', marker='o', markersize=4, color='purple')
plt.plot(xs[2, 0], xs[2, 1], 'ro', marker='o', markersize=4, color='purple')

plotseg(0, 1, 'purple')
plotseg(0, 2, 'purple')
plotseg(1, 2, 'purple')

plt.show()
```


We can see the points at which the function was evaluated in the same
quadratic example we saw in previous sections. The left hand panel shows
the steps from a starting point somewhat far from the optimum, with the
first 9 points numbered. In this case, we start with points 1, 2, and 3.
Point 4 is a reflection. At this point, it looks like point 5 is a
contraction but that doesn't exactly follow the algorithm above (since
Point 4 is between Points 2 and 3 so the iteration should end without a
contraction), so perhaps the algorithm as implemented is a bit different
than as described above. In any event, the new set is (2, 3, 4). Then
point 6 and point 7 are reflection and expansion steps and the new set
is (3, 4, 6). Points 8 and 9 are again reflection and expansion steps.
The right hand panel shows the steps from a starting point near
(actually at) the optimum. Points 4 and 5 are reflection and expansion
steps, with the next set being (1, 2, 5). Now step 6 is a reflection but
it is the worst of all the points, so point 7 is a contraction of point
2 giving the next set (1, 5, 7). Point 8 is then a reflection and point
9 is a contraction of point 5.

(Again some code in R.)

```
f <- function(x, plot = TRUE, verbose = FALSE) {
    result <- x[1]^2/1000 + 4*x[1]*x[2]/1000 + 5*x[2]^2/1000
    if(verbose) print(result)
    if(plot && cnt < 10) {
        points(x[1], x[2], pch = as.character(cnt))
        if(cnt < 10) cnt <<- cnt + 1 else cnt <<- 1
        if(interactive())
            invisible(readline(prompt = "Press <Enter> to continue..."))
    } else if(plot) points(x[1], x[2])
    return(result)
}

par(mfrow = c(1,2), mgp = c(1.8,.7,0), mai = c(.5,.45,.1,.5), cex = 0.7)

x1s <- seq(-5, 10, len = 100); x2s = seq(-5, 2, len = 100)
fx <- apply(expand.grid(x1s, x2s), 1, f, FALSE)
cnt <- 1
fields::image.plot(x1s, x2s, matrix(log(fx), 100, 100))
init <- c(7, -4)
optim(init, f, method = "Nelder-Mead", verbose = FALSE)

par(cex = 0.7)
x1s <- seq(-.2, .2, len = 100); x2s = seq(-.12, .12, len = 100)
fx <- apply(expand.grid(x1s, x2s), 1, f, FALSE)
cnt <- 1
fields::image.plot(x1s, x2s, matrix(log(fx), 100, 100))
init <- c(-0, 0)
optim(init, f, method = "Nelder-Mead", verbose = FALSE)
```

![Nelder-Mead](https://raw.githubusercontent.com/berkeley-stat243/stat243-fall-2023/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/nelder-mead.png)

Here's an [online graphical
illustration](http://www.benfrederickson.com/numerical-optimization/) of
Nelder-Mead.

This is the default in `optim()` in R. It is an option
(by specifying `method='Nelder-mead'`) for `scipy.optimize.minimize`
(BFGS or a variant is the default).

## Simulated annealing (SA) (optional)

Simulated annealing is a *stochastic* descent algorithm, unlike the
deterministic algorithms we've already discussed. It has a couple
critical features that set it aside from other approaches. First, uphill
moves are allowed; second, whether a move is accepted is stochastic, and
finally, as the iterations proceed the algorithm becomes less likely to
accept uphill moves.

Assume we are minimizing a negative log likelihood as a function of
$\theta$, $f(\theta)$.

The basic idea of simulated annealing is that one modifies the objective
function, $f$ in this case, to make it less peaked at the beginning,
using a "temperature" variable that changes over time. This helps to
allow moves away from local minima, when combined with the ability to
move uphill. The name comes from an analogy to heating up a solid to its
melting temperature and cooling it slowly - as it cools the atoms go
through rearrangements and slowly freeze into the crystal configuration
that is at the lowest energy level.

Here's the algorithm. We divide up iterations into stages,
$j=1,2,\ldots$ in which the temperature variable, $\tau_{j}$, is
constant. Like MCMC, we require a proposal distribution to propose new
values of $\theta$.

1.  Propose to move from $\theta_{t}$ to $\tilde{\theta}$ from a
    proposal density, $g_{t}(\cdot|\theta_{t})$, such as a normal
    distribution centered at $\theta_{t}$.

2.  Accept $\tilde{\theta}$ as $\theta_{t+1}$ according to the
    probability
    $\min(1,\exp((f(\theta_{t})-f(\tilde{\theta}))/\tau_{j})$ - i.e.,
    accept if a uniform random deviate is less than that probability.
    Otherwise set $\theta_{t+1}=\theta_{t}$. Notice that for larger
    values of $\tau_{j}$ the differences between the function values at
    the two locations are reduced (just like a large standard deviation
    spreads out a distribution). So the exponentiation smooths out the
    objective function when $\tau_{j}$ is large.

3.  Repeat steps 1 and 2 $m_{j}$ times.

4.  Increment the temperature and cooling schedule:
    $\tau_{j}=\alpha(\tau_{j-1})$ and $m_{j}=\beta(m_{j-1})$. Back to
    step 1.

The temperature should slowly decrease to 0 while the number of
iterations, $m_{j}$, should be large. Choosing these 'schedules' is at
the core of implementing SA. Note that we always accept downhill moves
in step 2 but we sometimes accept uphill moves as well.

For each temperature, SA produces an MCMC based on the Metropolis
algorithm. So if $m_{j}$ is long enough, we should sample from the
stationary distribution of the Markov chain,
$\exp(-f(\theta)/\tau_{j}))$. Provided we can move between local minima,
the chain should gravitate toward the global minima because these are
increasingly deep (low values) relative to the local minima as the
temperature drops. Then as the temperature cools, $\theta_{t}$ should
get trapped in an increasingly deep well centered on the global minimum.
There is a danger that we will get trapped in a local minimum and not be
able to get out as the temperature drops, so the temperature schedule is
quite important in trying to avoid this.

A wide variety of schedules have been tried. One approach is to set
$m_{j}=1\forall j$ and
$\alpha(\tau_{j-1})=\frac{\tau_{j-1}}{1+a\tau_{j-1}}$ for a small $a$.
For a given problem it can take a lot of experimentation to choose
$\tau_{0}$ and $m_{0}$ and the values for the scheduling functions. For
the initial temperature, it's a good idea to choose it large enough that
$\exp((f(\theta_{i})-f(\theta_{j}))/\tau_{0})\approx1$ for any pair
$\{\theta_{i},\theta_{j}\}$ in the domain, so that the algorithm can
visit the entire space initially.

Simulated annealing can converge slowly. Multiple random starting points
or stratified starting points can be helpful for finding a global
minimum. However, given the slow convergence, these can also be
computationally burdensome.

---

[← Consider contraction](20-consider-contraction.md) · [Up: contents](index.md) · [6. Basic optimization in Python →](22-6-basic-optimization-in-python.md)
