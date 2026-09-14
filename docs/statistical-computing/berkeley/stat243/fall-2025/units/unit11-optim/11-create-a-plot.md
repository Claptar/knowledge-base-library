---
title: Create a plot
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Create a plot

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

---

[← Calculate the Rastrigin function for each point in the grid](10-calculate-the-rastrigin-function-for-each-point-in-the-grid.md) · [Up: contents](index.md) · [Define the original function →](12-define-the-original-function.md)
