---
title: Different starting value (recall non-positive definite Hessian)
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/stat243-fall-2023/units/unit11-optim.qmd
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Different starting value (recall non-positive definite Hessian)

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/units/unit11-optim.qmd) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.qmd` (lossless)

beta2_init = 100
implicit_covar = np.exp(data.year/beta2_init)
X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params
sigma2_init = np.mean((data.co2-model.fittedvalues)**2)
inits = (beta0_init, beta1_init, beta2_init, np.log(sigma2_init))
fit3 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})

beta2_init = 10
implicit_covar = np.exp(data.year/beta2_init)
X = sm.add_constant(implicit_covar)
model = sm.OLS(data.co2, X).fit()
beta0_init, beta1_init = model.params
sigma2_init = np.mean((data.co2-model.fittedvalues)**2)
inits = (beta0_init, beta1_init, beta2_init, np.log(sigma2_init))
fit4 = minimize(nll, inits, args=(data), method='BFGS', options={'disp': True})

---

[← Optimization using BFGS](24-optimization-using-bfgs.md) · [Up: contents](index.md) · [Arbitrarily bad starting values →](26-arbitrarily-bad-starting-values.md)
