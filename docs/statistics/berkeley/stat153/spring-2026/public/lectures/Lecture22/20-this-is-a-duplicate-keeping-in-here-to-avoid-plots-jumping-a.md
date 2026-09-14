---
title: This is a duplicate, keeping in here to avoid plots jumping around! (mpl bug)
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture22.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# This is a duplicate, keeping in here to avoid plots jumping around! (mpl bug)

**Source:** [`public/lectures/Lecture22.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture22.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import FloatSlider, IntSlider, Checkbox, Layout, Output, VBox, HBox, interactive_output
from IPython.display import display

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
                   xytext=(8, 8), textcoords='offset points', fontsize=9)
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

    ax[0].set_xlabel('x'); ax[0].set_ylabel('y')
    ax[0].legend(frameon=False, fontsize=9, loc='lower left')
    ax[0].set_title(f'Position   σ_Q={sigma_Q:.3f}, σ_R={sigma_R:.2f}')

    tr_f = np.trace(Pf[:, :2, :2], axis1=1, axis2=2)
    tr_s = np.trace(Ps[:, :2, :2], axis1=1, axis2=2)
    if show_filter:
        ax[1].plot(tr_f, '-', color='#378ADD', lw=1.8, label='Filter')
    if show_smoother:
        ax[1].plot(tr_s, '--', color='#1D9E75', lw=1.8, label='Smoother')
    ax[1].set_xlabel('t'); ax[1].set_ylabel(r'$\mathrm{tr}(P^{pos}_t)$')
    ax[1].legend(frameon=False, fontsize=9)
    ax[1].set_title('Position uncertainty')

    plt.tight_layout()
    plt.show()


style = {'description_width': '160px'}
layout = Layout(width='500px')

sq_w = FloatSlider(value=0.05, min=0.001, max=0.5, step=0.001,
                   description='Process noise σ_Q', readout_format='.3f',
                   style=style, layout=layout)
sr_w = FloatSlider(value=0.8, min=0.05, max=3.0, step=0.01,
                   description='Measurement noise σ_R', readout_format='.2f',
                   style=style, layout=layout)
seed_w = IntSlider(value=1, min=1, max=20, step=1, description='seed')
m_w = Checkbox(value=True, description='Measurements')
f_w = Checkbox(value=True, description='Filter')
s_w = Checkbox(value=False, description='Smoother')
e_w = Checkbox(value=True, description='Ellipses')

out = interactive_output(demo, {
    'sigma_Q': sq_w, 'sigma_R': sr_w, 'seed': seed_w,
    'show_measurements': m_w, 'show_filter': f_w,
    'show_smoother': s_w, 'show_ellipses': e_w,
})

display(VBox([sq_w, sr_w, seed_w, m_w, f_w, s_w, e_w, out]))
```

---

[← This seems to help make the figure not jump around](19-this-seems-to-help-make-the-figure-not-jump-around.md) · [Up: contents](index.md)
