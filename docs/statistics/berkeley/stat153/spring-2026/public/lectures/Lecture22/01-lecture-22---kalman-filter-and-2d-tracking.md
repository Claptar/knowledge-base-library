---
title: Lecture 22 - Kalman Filter and 2D Tracking
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture22.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Lecture 22 - Kalman Filter and 2D Tracking

**Source:** [`public/lectures/Lecture22.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

Here we will look at an example of the Kalman filter for tracking the position and velocity of an object moving on a particular trajectory. Here, we will use a physics-based model, so unlike the example we showed yesterday, we already know how $\Phi$ and $A$.

For example, we know that we can get position directly at time $t$ from $p_t = p_{t-1} + \Delta t v_{t-1}$. Thus, $\Phi$ and $A$ are specified here rather than estimated. In other applications, like the blood markers we talked about last time, we'd have to estimate $\Phi$ from the data.

**Model**

State: $x_t = [p_x, p_y, v_x, v_y]^\top$ (position and velocity)

$$x_t = \Phi x_{t-1} + w_t, \quad w_t \sim \mathcal{N}(0, Q)$$
$$y_t = A x_t + v_t, \quad v_t \sim \mathcal{N}(0, R)$$

with
$$\Phi = \begin{bmatrix} 1 & 0 & \Delta t & 0 \\ 0 & 1 & 0 & \Delta t \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}, \quad A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix}$$

This $\Phi$ matrix can be interpreted as showing that position updates by adding $\Delta t v$ to our position, but velocity is unchanged from one step to the next (as evidenced by 1's in the bottom right diagonal).

We observe noisy position only for $y_t$, while velocity is unobserved (why we have zeros in $A$ for the last two variables). The filter has to infer velocity from the position history.

```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from ipywidgets import interact, FloatSlider, IntSlider, Checkbox, Layout
from IPython.display import display

np.set_printoptions(precision=3, suppress=True)
```

## Ground truth

Let's show what happens when the trajectory is a gentle curve. This matters because the filter's constant-velocity assumption is wrong, and the true velocity is in fact changing over time. This will allow us to show what happens when the model is misspecified.

```python
def gen_truth(N=60):
    """
    Generate a gentle curve
    """
    s = np.linspace(0, 1, N)
    x = -8 + 16 * s
    y = 2 * np.sin(1.3 * np.pi * s) - 1 * s
    return np.stack([x, y], axis=1)

---

[Up: contents](index.md) · [def gentruth(N=60) →](02-def-gentruth-n-60.md)
