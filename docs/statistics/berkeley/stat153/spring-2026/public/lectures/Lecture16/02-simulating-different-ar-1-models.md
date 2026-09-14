---
title: Simulating different AR(1) models
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture16.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture16.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Simulating different AR(1) models

**Source:** [`public/lectures/Lecture16.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture16.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Let's simulate AR(1) processes with different values of $\phi$ and see what happens. If we increase $\phi$ from 0.5 to 0.95, what do you expect to change about the series?

```python
phi_values = [0.0, 0.5, 0.7, 0.99]
n = 500
w = rng.standard_normal(n)  # same shocks for all — isolate effect of phi

fig, axes = plt.subplots(len(phi_values), 1, figsize=(10, 6), sharex=True)

for ax, phi in zip(axes, phi_values):
    x = np.zeros(n)
    for t in range(1, n):
        x[t] = phi * x[t-1] + w[t]
    ax.plot(x, lw=0.7)
    ax.set_title(f'AR(1), $\\phi = {phi}$', loc='left')
    ax.set_ylabel('$X_t$')

axes[-1].set_xlabel('Time')
plt.tight_layout()
plt.savefig('images/16_AR1_phi.png')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

# Properties of the AR(1) model

Here we will look at how the ACF decays exponentially for a sample AR(1) process, and compare that to the theoretical ACF.

```python
phi = -0.6
n = 1000

# Simulate
x = np.zeros(n)
for t in range(1, n):
    x[t] = phi * x[t-1] + rng.standard_normal()

fig, ax = plt.subplots(figsize=(10, 4))
plot_acf(x, lags=30, ax=ax, title='', alpha=0.05)

# Overlay theoretical ACF
lags = np.arange(0, 31)
theoretical_acf = phi ** lags
ax.plot(lags, theoretical_acf, 'r--', lw=2, label=f'Theoretical: $\\phi^{{|h|}}$ with $\\phi={phi}$')
ax.set_title(f'ACF of AR(1) with $\\phi = {phi}$, n = {n}')
ax.set_xlabel('Lag $h$')
ax.set_ylabel('$\\rho(h)$')
ax.legend()
plt.tight_layout()
plt.savefig('images/16_acf.png')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Example AR(2) →](03-example-ar-2.md)
