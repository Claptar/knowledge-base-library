---
title: Look at the raw data and see what is missing
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/labs/Lab11.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Look at the raw data and see what is missing

**Source:** [`public/labs/Lab11.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/labs/Lab11.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

fig, axes = plt.subplots(3, 1, figsize=(10, 6), sharex=True)
labels = ['log(WBC)', 'log(PLT)', 'HCT']
cols = ['WBC', 'PLT', 'HCT']

for ax, col, label in zip(axes, cols, labels):
    mask = df[col].notna()
    ax.plot(df.loc[mask, 'day'], df.loc[mask, col], 'o',
            color='#D85A30', ms=4, alpha=0.7)
    ax.set_ylabel(label)
    # Shade missing regions
    missing = df[col].isna().values
    for i in range(len(missing)):
        if missing[i]:
            ax.axvspan(df['day'].iloc[i] - 0.5, df['day'].iloc[i] + 0.5,
                       color='#888780', alpha=0.06)

axes[-1].set_xlabel('Day post-transplant')
axes[0].set_title('Raw observations (gray = missing)')
plt.tight_layout()
plt.show()
```

## Define the state-space model

We subclass `statsmodels.tsa.statespace.MLEModel` to define our model. We will relate our lecture notation to the variable names defined in `statsmodels`:

| Our notation | statsmodels name | Set in code |
|:---:|:---:|:---|
| $\Phi$ | `transition` | Estimated (9 params) |
| $A_t$ | `design` | Fixed as $I_3$; NaN rows handled automatically |
| $Q$ | `state_cov` | Estimated via Cholesky (6 params) |
| $R$ | `obs_cov` | Estimated via Cholesky (6 params) |
| $I$ | `selection` | Fixed as $I_3$ |

$Q$ and $R$ are parameterized as $L L^\top$ where $L$ is lower triangular. This guarantees positive semi-definiteness regardless of what the optimizer tries.

```python
class BloodSSM(MLEModel):
    """
    x_t = Phi @ x_{t-1} + w_t,   w_t ~ N(0, Q)
    y_t = A_t @ x_t + v_t,        v_t ~ N(0, R)

    A_t = I when observed; statsmodels zeros out rows for NaN
    automatically. Parameters: Phi (9), Q (6 Cholesky), R (6 Cholesky).
    """

    def __init__(self, endog):
        super().__init__(endog, k_states=3, k_posdef=3,
                         initialization='diffuse')
        self['design'] = np.eye(3)
        self['selection'] = np.eye(3)

    @staticmethod
    def _params_to_lower(params, k=3):
        L = np.zeros((k, k))
        L[np.tril_indices(k)] = np.real(params[:k * (k + 1) // 2])
        return L

    @property
    def param_names(self):
        phi = [f'phi.{i+1}{j+1}' for i in range(3) for j in range(3)]
        cQ = [f'chol_Q.{i+1}{j+1}' for i in range(3) for j in range(i + 1)]
        cR = [f'chol_R.{i+1}{j+1}' for i in range(3) for j in range(i + 1)]
        return phi + cQ + cR

    @property
    def start_params(self):
        # Initial Phi: near-identity (persistent markers)
        Phi_init = np.array([[0.9, 0.0, 0.0],
                             [0.0, 0.9, 0.0],
                             [0.0, 0.0, 0.9]])

        # Initial Cholesky factors for Q and R
        chol_Q_init = np.array([[0.1, 0.0, 0.0],
                                [0.0, 0.1, 0.0],
                                [0.0, 0.0, 1.0]])

        chol_R_init = np.array([[0.1, 0.0, 0.0],
                                [0.0, 0.1, 0.0],
                                [0.0, 0.0, 1.0]])

        # Flatten for optimizer (internal detail)
        return np.concatenate([
            Phi_init.ravel(),
            chol_Q_init[np.tril_indices(3)],
            chol_R_init[np.tril_indices(3)],
        ])

    def update(self, params, **kwargs):
        params = super().update(params, **kwargs)
        Phi_full = np.real(params[:9]).reshape(3,3)
        #self['transition'] = np.diag(np.diag(Phi_full)) # uncomment for diagonal only matrix, no interactions
        self['transition'] = np.real(params[:9]).reshape(3, 3)
        L_Q = self._params_to_lower(params[9:15])
        L_R = self._params_to_lower(params[15:21])
        self['state_cov'] = L_Q @ L_Q.T
        self['obs_cov'] = L_R @ L_R.T
```

---

[← Modeling blood markers](04-modeling-blood-markers.md) · [Up: contents](index.md) · [Fit the model →](06-fit-the-model.md)
