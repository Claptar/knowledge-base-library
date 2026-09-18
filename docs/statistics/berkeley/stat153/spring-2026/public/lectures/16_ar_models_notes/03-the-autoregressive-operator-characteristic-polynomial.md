---
title: The autoregressive operator/characteristic polynomial
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md
source_file: sources/berkeley-stat153/spring-2026/public/lectures/16_ar_models_notes.md
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/16_ar_models_notes.md`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/16_ar_models_notes.md) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.md`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# The autoregressive operator/characteristic polynomial

We then define the *autoregressive operator* as:

$$\phi(B) = (1 - \phi_1 B - \phi_2 B^2 - \dots - \phi_p B^p)$$

so we have $\phi(B)x_t=w_t$

This is also sometimes called the *characteristic polynomial* because we can use it to find the roots of the polynomial, which will then tell us some more interpretable information about stationarity and oscillatory frequency. Let's first consider the AR(1) model. There we have:

$$\phi(B) = (1 - \phi_1 B)$$

The root is at $B = 1/\phi$.

**Important:** For stationarity, we require all roots to lie outside the unit circle, that is, $|1/\phi| > 1 \iff |\phi| < 1$.

Now let's try this with an AR(2) model:

$$x_t = \phi_1 x_{t-1} + \phi_2 x_{t-2} + w_t$$

the characteristic polynomial is:

$$\phi(B) = (1 - \phi_1 B - \phi_2 B^2)$$

Now when we solve for the roots of this polynomial, we could potentially get:

1. Two real roots (overdamped behavior) - this means the process will decay smoothly back to the mean without oscillating
2. Complex conjugate roots - this will lead to oscillatory decay

### Example AR(2) model

Let's try an example:

$$x_t = 0.6 x_{t-1} -0.5x_{t-2} + w_t$$

We will do the following:

1. Write the characteristic polynomial
2. Find its roots. Are they real or complex?
3. Is this process stationary?
4. What kind of behavior do you expect?

**Characteristic polynomial:**

$$\phi(B) = (1 - 0.6 B + 0.5 B^2)$$

We then solve for its roots using the quadratic formula. For this particular AR(2) model, we get complex roots:

$0=\frac{0.6 \pm \sqrt{(-0.6)^2 - 4(0.5)(1)}}{2(0.5)}$

The roots are $0.6 \pm 1.28i$, which are complex. The modulus tells us whether the process is stationary:

$|z| = \sqrt{a^2+b^2} = \sqrt{0.6^2 + 1.28^2} = 1.41$

Because this is greater than 1, we determine that yes, the process is indeed stationary. The modulus also has another intuitive meaning - a modulus closer to 1 means less damping and a more persistent oscillation, whereas a modulus closer to 0 means more damping (the signal dies out fast).

## Next time - ARMA
Next time, we will discuss AR(p) models and the extension to ARMA models, which include a moving average comopnent that allows us to also model recent shocks in our autoregressive process.

---

[← AR(1) process](02-ar-1-process.md) · [Up: contents](index.md)
