---
title: Example AR(2)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture16.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture16.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Example AR(2)

**Source:** [`public/lectures/Lecture16.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture16.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

$$x_t = 0.6 x_{t-1} -0.5x_{t-2} + w_t$$

We will do the following:

1. Write the characteristic polynomial
2. Find its roots. Are they real or complex?
3. Is this process stationary?
4. What kind of behavior do you expect?

```python
# Solve the AR(2) characteristic equation ---
phi_1, phi_2 = 0.6, -0.5

# phi(z) = 1 - 0.6z + 0.5z^2
# from highest to lowest p
coeffs = [-phi_2, phi_1, 1]  # 0.5*z^2 - 0.6*z + 1 = 0
roots = np.roots(coeffs)

print(f"Characteristic polynomial: phi(z) = 1 - {phi_1}z + {phi_2}z^2")
print(f"Roots: {roots}")
print(f"Modulus of roots: {np.abs(roots)}")
print(f"All roots outside unit circle? {np.all(np.abs(roots) > 1)}")
print(f"Roots are complex? {np.any(np.iscomplex(roots))}")
print(f"\nIf are complex, we expect oscillatory behavior")
print(f"If |roots| > 1, the process is stationary")
```

```
Characteristic polynomial: phi(z) = 1 - 0.6z + -0.5z^2
Roots: [-0.6+1.28062485j -0.6-1.28062485j]
Modulus of roots: [1.41421356 1.41421356]
All roots outside unit circle? True
Roots are complex? True

If are complex, we expect oscillatory behavior
If |roots| > 1, the process is stationary
```

```python
# Let's plot the AR(2) model to verify what we predicted
phi_1, phi_2 = 0.6, -0.5
n = 500

x = np.zeros(n)
for t in range(2, n):
    x[t] = phi_1 * x[t-1] + phi_2 * x[t-2] + rng.standard_normal()

fig, axes = plt.subplots(1, 2, figsize=(14, 4))

axes[0].plot(x[:200], lw=0.8)
axes[0].set_title('AR(2): $x_t = $'+ str(phi_1) + '$x_{t-1} ' + str(phi_2) + 'x_{t-2} + w_t$')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('$x_t$')

plot_acf(x, lags=30, ax=axes[1], title='')
axes[1].set_title('ACF — oscillatory decay')
axes[1].set_xlabel('Lag $h$')

plt.tight_layout()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

---

[← Simulating different AR(1) models](02-simulating-different-ar-1-models.md) · [Up: contents](index.md)
