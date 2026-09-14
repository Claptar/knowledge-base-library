---
title: RMSE vs. complexity
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture19.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# RMSE vs. complexity

**Source:** [`public/lectures/Lecture19.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture19.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

colors = {0: 'C0', 1: 'C3', 2: 'C2'}

for d_val in sorted(df['d'].unique()):
    sub = df[df['d'] == d_val]
    plt.scatter(sub['n_params'], sub['rmse'],
               c=colors[d_val], s=80,
               label=f'd = {d_val}', edgecolor='k', linewidth=0.5)
    for _, row in sub.iterrows():
        plt.gca().annotate(row['spec'], (row['n_params'], row['rmse']),
                    xytext=(5, 5), textcoords='offset points')

plt.xlabel('# ARMA parameters (p + q)')
plt.gca().set_xticks(np.arange(1,5))
plt.ylabel(f'RMSE')
plt.title('Forecast accuracy vs. model complexity')
plt.legend(title='Differencing', loc='upper right')
plt.grid(alpha=0.3)

---

[← ---- 4. Fit, forecast, score ----](19------4-fit-forecast-score.md) · [Up: contents](index.md) · [Forecast →](21-forecast.md)
