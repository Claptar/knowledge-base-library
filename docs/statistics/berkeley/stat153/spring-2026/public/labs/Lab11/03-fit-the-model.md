---
title: Fit the model
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Fit the model

```python
endog = df[['WBC', 'PLT', 'HCT']].values.astype(float)

mod = BloodSSM(endog)
res = mod.fit(disp=False, maxiter=2000, method='powell', cov_type='robust')
print(res.summary())
```

Notice here that you may get errors related to the covariance matrix being singular or near-singular. The Ljung-Box test tests whether our one-step-ahead prediction errors are serially correlated - if these p-values are less than 0.05, then we do have correlations left in our model that we're missing out on. Here it seems like that's not the case, so that's good news.

On the other hand, there are a number of other assumptions that we aren't meeting. The standard errors here are all close to zero, which means the confidence intervals are likely not trustworthy. Although there are other diagnostics here that are maybe concerning, this is often the case with real biological data. One thing we could try is to force the dynamics to be simpler (i.e. only allow for diagonal terms in $\Phi$), and see if this helps.

## Extract and interpret estimated matrices

In this scenario, we are estimating $\Phi$, $Q$, $R$, so we will print those here and talk about how to interpret them.

```python
# Helper to extract Q or R from Cholesky parameters
def extract_chol_matrix(params, start_idx):
    L = np.zeros((3, 3))
    idx = start_idx
    for i in range(3):
        for j in range(i + 1):
            L[i, j] = np.real(params[idx]); idx += 1
    return L @ L.T, idx

params = res.params
Phi_hat = np.real(params[0:9]).reshape(3, 3)
Q_hat, next_idx = extract_chol_matrix(params, 9)
R_hat, _ = extract_chol_matrix(params, next_idx)

marker_names = ['WBC', 'PLT', 'HCT']

print("Estimated Phi:")
print(pd.DataFrame(Phi_hat, index=marker_names, columns=marker_names).round(3))
print(f"\nEstimated Q:")
print(pd.DataFrame(Q_hat, index=marker_names, columns=marker_names).round(4))
print(f"\nEstimated R:")
print(pd.DataFrame(R_hat, index=marker_names, columns=marker_names).round(4))
```

### Interpreting $\hat{\Phi}$

Each row of $\Phi$ is a regression: today's marker value as a function of yesterday's three markers.

**Diagonal entries (persistence):**
- $\phi_{11} \approx 0.95$: log(WBC) is highly persistent — today's value is close to yesterday's
- $\phi_{22} \approx 0.91$: log(PLT) is slightly less persistent
- $\phi_{33} \approx 0.89$: HCT is the least persistent of the three

All diagonal entries are close to 1 but strictly less, consistent with mean-reverting biological processes. A value of exactly 1 would imply a random walk (no mean reversion).

**Off-diagonal entries (cross-coupling):**
- $\phi_{21} \approx 0.07$: yesterday's WBC slightly predicts today's PLT (consistent with WBC recovery preceding platelet recovery during engraftment)
- $\phi_{31} \approx -0.79$ and $\phi_{32} \approx 1.21$: HCT is strongly coupled to both WBC and PLT — its dynamics are driven more by the other markers than by its own history

## Plot the Kalman filter and smoother estimates

The Kalman smoother gives us $x_t^n = E[x_t \mid y_{1:n}]$, which is the best estimate of each marker at every time point using the entire dataset. This fills in the missing values optimally. We can also compare this to the Kalman filter, which uses only the forward step and cannot integrate data from the future.

```python
from ipywidgets import Checkbox, Layout, interactive_output, VBox, HBox
from IPython.display import display

def contiguous_regions(mask):
    """Find contiguous True regions in a boolean array."""
    regions = []
    start = None
    for i, val in enumerate(mask):
        if val and start is None:
            start = i
        elif not val and start is not None:
            regions.append((start, i - 1))
            start = None
    if start is not None:
        regions.append((start, len(mask) - 1))
    return regions

# Extract filtered states and standard errors
filtered_state = res.filter_results.filtered_state.T
filtered_cov = res.filter_results.filtered_state_cov
filtered_se = np.sqrt(
    np.array([filtered_cov[i, i, :] for i in range(3)]).T
)

# Extract smoothed states and standard errors
smoothed_state = res.smoother_results.smoothed_state.T
smoothed_cov = res.smoother_results.smoothed_state_cov
smoothed_se = np.sqrt(
    np.array([smoothed_cov[i, i, :] for i in range(3)]).T
)

# Forecast to day 100
fc = res.get_forecast(steps=9)
fc_mean = fc.predicted_mean
fc_ci = fc.conf_int()

# Plot function
labels = ['log(WBC)', 'log(PLT)', 'HCT']
colors_smooth = ['#378ADD', '#1D9E75', '#534AB7']
colors_filter = ['#85B7EB', '#5DCAA5', '#AFA9EC']
days = df['day'].values
fc_days = np.arange(days[-1] + 1, days[-1] + 10)

def plot_blood(show_observed=True, show_filtered=True,
               show_smoothed=True, show_forecast=True,
               show_ci=True):
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    for i, (ax, label) in enumerate(zip(axes, labels)):
        obs = endog[:, i]
        observed_mask = ~np.isnan(obs)
        missing_mask = np.isnan(obs)

        # Shade missing regions
        for start, end in contiguous_regions(missing_mask):
            ax.axvspan(days[start] - 0.5,
                       days[min(end, len(days) - 1)] + 0.5,
                       color='#888780', alpha=0.06)

        if show_observed:
            ax.plot(days[observed_mask], obs[observed_mask], 'o',
                    color='#D85A30', ms=4, alpha=0.7,
                    label='Observed', zorder=3)

        if show_filtered:
            ax.plot(days, filtered_state[:, i], '-',
                    color=colors_filter[i], lw=1.2,
                    label='Filtered', alpha=0.8)
            if show_ci:
                ax.fill_between(days,
                    filtered_state[:, i] - 1.96 * filtered_se[:, i],
                    filtered_state[:, i] + 1.96 * filtered_se[:, i],
                    color=colors_filter[i], alpha=0.08)

        if show_smoothed:
            ax.plot(days, smoothed_state[:, i], '-',
                    color=colors_smooth[i], lw=1.5, label='Smoothed')
            if show_ci:
                ax.fill_between(days,
                    smoothed_state[:, i] - 1.96 * smoothed_se[:, i],
                    smoothed_state[:, i] + 1.96 * smoothed_se[:, i],
                    color=colors_smooth[i], alpha=0.12)

        if show_forecast:
            ax.plot(fc_days, fc_mean[:, i], '--',
                    color=colors_smooth[i], lw=1.2, label='Forecast')
            if show_ci:
                ax.fill_between(fc_days, fc_ci[:, i], fc_ci[:, i + 3],
                                color=colors_smooth[i], alpha=0.08)

        ax.set_ylabel(label)
        ax.legend(frameon=False, fontsize=9, loc='upper left')

    axes[-1].set_xlabel('Day post-transplant')
    axes[0].set_title('Blood markers: Kalman filter and smoother')
    plt.tight_layout()
    plt.show()


# Widgets
obs_w = Checkbox(value=True, description='Observed')
filt_w = Checkbox(value=True, description='Filtered')
smooth_w = Checkbox(value=True, description='Smoothed')
fc_w = Checkbox(value=True, description='Forecast')
ci_w = Checkbox(value=True, description='95% CI bands')

out = interactive_output(plot_blood, {
    'show_observed': obs_w,
    'show_filtered': filt_w,
    'show_smoothed': smooth_w,
    'show_forecast': fc_w,
    'show_ci': ci_w,
})

display(VBox([HBox([obs_w, filt_w, smooth_w, fc_w, ci_w]), out]))
```

### What do we see in these plots?

1. **Confidence intervals widen in missing-data regions** (gray bands) because no update step occurs. We can only use the dynamics, and $P_t$ grows via the $+Q$ term at each predict step. When the next observation arrives, $P_t$ snaps back down.

2. **WBC and PLT** are smoothly estimated with tight CIs even when there is missing data. Their small $Q$ entries mean the model treats them as slowly varying.

3. **HCT** has much wider CIs, consistent with its large $Q_{33}$ and $R_{33}$. Biologically, hematocrit is more variable and harder to measure precisely.

4. **Forecasts** (dashed lines past day 91) converge toward the long-run mean with widening CIs. The platelet forecast at day 100 is a clinically relevant quantity that is correlated with long term survival. In particular, research has shown a good prognosis for a total platelet count > 50 (log platelet count > 3.91) ([Bolwell et al. 2004](https://www.nature.com/articles/1704330).)

---

[← Modeling blood markers](02-modeling-blood-markers.md) · [Up: contents](index.md) · [Platelet forecast at day 100 →](04-platelet-forecast-at-day-100.md)
