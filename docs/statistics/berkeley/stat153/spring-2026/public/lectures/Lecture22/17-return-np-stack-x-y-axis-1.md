---
title: return np.stack([x,y], axis=1)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture22.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# return np.stack([x,y], axis=1)

**Source:** [`public/lectures/Lecture22.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

def gen_measurements(truth, sigma_R, seed):
    """
    Make noisy measurements from our ground truth with some measurement
    error with covariance sigma_R
    """
    rng = np.random.default_rng(seed)
    return truth + sigma_R * rng.standard_normal(truth.shape)
```

## Kalman filter

Now we will build the state-space matrices and create functions for both the Kalman Filter and the Kalman Smoother.

```python
def build_matrices(sigma_Q, sigma_R, dt=1.0):
    """Build state-space matrices for a 2D constant-velocity tracking model.

    State vector: x = [p_x, p_y, v_x, v_y]
    Observation:  y = [p_x, p_y] + measurement noise

    Dynamics:     x_t = Phi @ x_{t-1} + w_t,  w_t ~ N(0, Q)
    Observation:  y_t = A @ x_t       + v_t,  v_t ~ N(0, R)

    Q uses the continuous white-noise-acceleration discretization
    (Bar-Shalom et al., Estimation with Applications to Tracking and
    Navigation), which couples position and velocity noise through
    integrated acceleration. A diagonal Q is structurally incorrect for
    this model.

    Parameters
    ----------
    sigma_Q : float
        Process noise scale. Interpretable as the standard deviation of
        unmodeled acceleration, with units of [position / time^2] * sqrt(time).
        Controls how much the filter distrusts its constant-velocity
        dynamics assumption.
    sigma_R : float
        Measurement noise standard deviation, in units of position. Assumed
        equal and independent across x and y components.
    dt : float, default 1.0
        Time step between observations.

    Returns
    -------
    Phi : (4, 4) ndarray
        State transition matrix.
    Q : (4, 4) ndarray
        Process noise covariance.
    A : (2, 4) ndarray
        Observation matrix (picks off position).
    R : (2, 2) ndarray
        Measurement noise covariance.
    """
    Phi = np.array([[1, 0, dt, 0],
                    [0, 1, 0, dt],
                    [0, 0, 1,  0],
                    [0, 0, 0,  1]], dtype=float)
    q = sigma_Q ** 2
    Q = q * np.array([[dt**3/3, 0,       dt**2/2, 0      ],
                      [0,       dt**3/3, 0,       dt**2/2],
                      [dt**2/2, 0,       dt,      0      ],
                      [0,       dt**2/2, 0,       dt     ]])
    A = np.array([[1, 0, 0, 0],
                  [0, 1, 0, 0]], dtype=float)
    R = sigma_R ** 2 * np.eye(2)
    return Phi, Q, A, R


def kalman_filter(meas, sigma_Q, sigma_R):
    """Run the Kalman filter forward pass on a sequence of 2D position measurements.

    At each time t, performs:
        Predict:  x_t^{t-1} = Phi @ x_{t-1}^{t-1}
                  P_t^{t-1} = Phi @ P_{t-1}^{t-1} @ Phi.T + Q
        Update:   K_t = P_t^{t-1} @ A.T @ (A @ P_t^{t-1} @ A.T + R)^{-1}
                  x_t^t = x_t^{t-1} + K_t @ (y_t - A @ x_t^{t-1})
                  P_t^t = (I - K_t @ A) @ P_t^{t-1}

    Initialization uses the first measurement as the position estimate with
    zero initial velocity. This is a practical shortcut; a mathematically
    cleaner alternative is a diffuse prior (P_0 very large), which produces
    nearly identical results after the first few steps.

    Parameters
    ----------
    meas : (N, 2) ndarray
        Noisy 2D position observations.
    sigma_Q : float
        Process noise scale (see build_matrices).
    sigma_R : float
        Measurement noise standard deviation (see build_matrices).

    Returns
    -------
    xf : (N, 4) ndarray
        Filtered state means x_t^t = E[x_t | y_{1:t}].
    Pf : (N, 4, 4) ndarray
        Filtered state covariances P_t^t.
    xp : (N, 4) ndarray
        One-step-ahead predicted state means x_t^{t-1} = E[x_t | y_{1:t-1}].
        At t=0 this equals the initial state (no prediction step).
    Pp : (N, 4, 4) ndarray
        One-step-ahead predicted state covariances P_t^{t-1}. Required
        inputs for the RTS smoother.
    """
    Phi, Q, A, R = build_matrices(sigma_Q, sigma_R)
    N = len(meas)
    # Initial state: first measurement for position, zero velocity
    x = np.array([meas[0, 0], meas[0, 1], 0.0, 0.0])
    P = np.diag([1.0, 1.0, 10.0, 10.0])
    xf = np.zeros((N, 4));  Pf = np.zeros((N, 4, 4))
    xp = np.zeros((N, 4));  Pp = np.zeros((N, 4, 4))
    for t in range(N):
        if t > 0:
            # Predict
            x = Phi @ x
            P = Phi @ P @ Phi.T + Q
        xp[t] = x;  Pp[t] = P
        # Update
        innov = meas[t] - A @ x                # innovation
        S = A @ P @ A.T + R                    # innovation covariance
        K = P @ A.T @ np.linalg.inv(S)         # Kalman gain
        x = x + K @ innov
        P = (np.eye(4) - K @ A) @ P
        xf[t] = x;  Pf[t] = P
    return xf, Pf, xp, Pp


def rts_smoother(xf, Pf, xp, Pp, sigma_Q):
    """Run the Rauch-Tung-Striebel smoother backward pass.

    Computes x_t^N = E[x_t | y_{1:N}] and P_t^N using the full observation
    record. Initialized at t=N-1 with the filtered estimate (where filter
    and smoother coincide), then iterates backward using:

        J_t = P_t^t @ Phi.T @ (P_{t+1}^t)^{-1}
        x_t^N = x_t^t + J_t @ (x_{t+1}^N - x_{t+1}^t)
        P_t^N = P_t^t + J_t @ (P_{t+1}^N - P_{t+1}^t) @ J_t.T

    The smoother's error covariance P_t^N is guaranteed to satisfy
    tr(P_t^N) <= tr(P_t^t) for all t, since smoothing conditions on strictly
    more information.

    Parameters
    ----------
    xf : (N, 4) ndarray
        Filtered state means from kalman_filter.
    Pf : (N, 4, 4) ndarray
        Filtered state covariances from kalman_filter.
    xp : (N, 4) ndarray
        One-step-ahead predicted means from kalman_filter.
    Pp : (N, 4, 4) ndarray
        One-step-ahead predicted covariances from kalman_filter.
    sigma_Q : float
        Process noise scale. Must match the value used in the forward pass.
        Phi does not actually depend on sigma_Q in this constant-velocity
        model; the argument is kept for interface consistency.

    Returns
    -------
    xs : (N, 4) ndarray
        Smoothed state means x_t^N = E[x_t | y_{1:N}].
    Ps : (N, 4, 4) ndarray
        Smoothed state covariances P_t^N.
    """
    Phi, _, _, _ = build_matrices(sigma_Q, 1.0)  # R doesn't matter here
    N = len(xf)
    xs = xf.copy();  Ps = Pf.copy()
    for t in range(N - 2, -1, -1):
        J = Pf[t] @ Phi.T @ np.linalg.inv(Pp[t+1])
        xs[t] = xf[t] + J @ (xs[t+1] - xp[t+1])
        Ps[t] = Pf[t] + J @ (Ps[t+1] - Pp[t+1]) @ J.T
    return xs, Ps
```

## Sanity check

Run once with default parameters and plot.

```python
truth = gen_truth()
meas = gen_measurements(truth, sigma_R=0.8, seed=1)
xf, Pf, xp, Pp = kalman_filter(meas, sigma_Q=0.05, sigma_R=0.8)
xs, Ps = rts_smoother(xf, Pf, xp, Pp, sigma_Q=0.05)

fig, ax = plt.subplots(1, 2, figsize=(11, 4))
ax[0].plot(truth[:, 0], truth[:, 1], 'k-', lw=1.5, label='Truth')
ax[0].plot(meas[:, 0], meas[:, 1], '.', color='#D85A30', ms=5, alpha=0.75, label='Measurements')
ax[0].plot(xf[:, 0], xf[:, 1], '-', color='#378ADD', lw=1.8, label='Filter')
ax[0].plot(xs[:, 0], xs[:, 1], '--', color='#1D9E75', lw=1.8, label='Smoother')
ax[0].set_xlabel('x'); ax[0].set_ylabel('y'); ax[0].legend(frameon=False, fontsize=9)
ax[0].set_title('Position')

tr_f = np.trace(Pf[:, :2, :2], axis1=1, axis2=2)
tr_s = np.trace(Ps[:, :2, :2], axis1=1, axis2=2)
ax[1].plot(tr_f, '-', color='#378ADD', lw=1.8, label='Filter')
ax[1].plot(tr_s, '--', color='#1D9E75', lw=1.8, label='Smoother')
ax[1].set_xlabel('t'); ax[1].set_ylabel(r'$\mathrm{tr}(P^{pos}_t)$'); ax[1].legend(frameon=False, fontsize=9)
ax[1].set_title('Position uncertainty')
plt.tight_layout(); plt.show()
```

## Interactive version

Use the sliders to explore. Suggested experiments:

1. **Default values** ($\sigma_Q = 0.05$, $\sigma_R = 0.80$). What do you predict the filter will do?
2. **Large $\sigma_R$** (~2.5): measurements become nearly useless. Does the filter still track? What will the estimate look like?
3. **Tiny $\sigma_Q$** (~0.005): filter is told to trust its dynamics model. What goes wrong, and why?
4. **Enable the smoother.** Where does it help most — beginning, middle, end?

The covariance ellipses are 95% confidence regions from the 2×2 position block of $P$.

```python
def cov_ellipse(ax, mean, cov, color, alpha=0.12):
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    vals, vecs = vals[order], vecs[:, order]
    theta = np.degrees(np.arctan2(vecs[1, 0], vecs[0, 0]))
    # chi^2 with 2 dof, 95%: 5.991
    w, h = 2 * np.sqrt(5.991 * vals)
    e = Ellipse(mean, w, h, angle=theta, facecolor=color, alpha=alpha,
                edgecolor=color, lw=0.8)
    ax.add_patch(e)

def demo(sigma_Q=0.05, sigma_R=0.8, seed=1,
         show_measurements=True, show_filter=True,
         show_smoother=False, show_ellipses=True):
    truth = gen_truth()
    meas = gen_measurements(truth, sigma_R, seed)
    xf, Pf, xp, Pp = kalman_filter(meas, sigma_Q, sigma_R)
    xs, Ps = rts_smoother(xf, Pf, xp, Pp, sigma_Q)

    fig, ax = plt.subplots(1, 2, figsize=(12, 4.5),
                           gridspec_kw={'width_ratios': [2, 1]})

    # Position plot
    ax[0].plot(truth[:, 0], truth[:, 1], 'k-', lw=1.5, label='Truth')
    ax[0].annotate('t=0', xy=(truth[0, 0], truth[0, 1]),
                   xytext=(8, 8), textcoords='offset points',
                   fontsize=9, color='black')
    if show_measurements:
        ax[0].plot(meas[:, 0], meas[:, 1], '.', color='#D85A30',
                   ms=5, alpha=0.75, label='Measurements')
    if show_filter:
        ax[0].plot(xf[:, 0], xf[:, 1], '-', color='#378ADD',
                   lw=1.8, label='Filter')
    if show_smoother:
        ax[0].plot(xs[:, 0], xs[:, 1], '--', color='#1D9E75',
                   lw=1.8, label='Smoother')
    if show_ellipses:
        stride = 6
        for t in range(0, len(truth), stride):
            if show_filter:
                cov_ellipse(ax[0], xf[t, :2], Pf[t, :2, :2], '#378ADD')
            if show_smoother:
                cov_ellipse(ax[0], xs[t, :2], Ps[t, :2, :2], '#1D9E75')

    #ax[0].set_xlim(-10, 10); ax[0].set_ylim(-4, 4)
    ax[0].set_xlabel('x'); ax[0].set_ylabel('y')
    ax[0].legend(frameon=False, fontsize=9, loc='lower left')
    ax[0].set_title(f'Position   σ_Q={sigma_Q:.3f}, σ_R={sigma_R:.2f}')

    # Trace plot
    # This gives you the uncertainty for 2D collapsed into
    # a single scalar
    tr_f = np.trace(Pf[:, :2, :2], axis1=1, axis2=2)
    tr_s = np.trace(Ps[:, :2, :2], axis1=1, axis2=2)
    if show_filter:
        ax[1].plot(tr_f, '-', color='#378ADD', lw=1.8, label='Filter')
    if show_smoother:
        ax[1].plot(tr_s, '--', color='#1D9E75', lw=1.8, label='Smoother')
    ax[1].set_xlabel('t'); ax[1].set_ylabel(r'$\mathrm{tr}(P^{pos}_t)$')
    ax[1].legend(frameon=False, fontsize=9)
    ax[1].set_title('Position uncertainty')

    plt.tight_layout(); plt.show()

style = {'description_width': '160px'}
layout = Layout(width='500px')
interact(demo,
         sigma_Q=FloatSlider(value=0.05, min=0.001, max=0.5, step=0.001,
                                description='Process noise σ_Q', readout_format='.3f',
                                style=style, layout=layout),
         sigma_R=FloatSlider(value=0.8, min=0.05, max=3.0, step=0.01,
                                description='Measurement noise σ_R', readout_format='.2f',
                                style=style, layout=layout),
         seed=IntSlider(value=1, min=1, max=20, step=1, description='seed'),
         show_measurements=Checkbox(value=True, description='Measurements'),
         show_filter=Checkbox(value=True, description='Filter'),
         show_smoother=Checkbox(value=False, description='Smoother'),
         show_ellipses=Checkbox(value=True, description='Ellipses'));
```

```python

---

[← y = 3x + 0.3](16-y-3x-0-3.md) · [Up: contents](index.md) · [Filler text →](18-filler-text.md)
