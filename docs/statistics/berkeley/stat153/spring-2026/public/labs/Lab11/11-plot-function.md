---
title: Plot function
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot function

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

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

---

[← Forecast to day 100](10-forecast-to-day-100.md) · [Up: contents](index.md) · [Widgets →](12-widgets.md)
