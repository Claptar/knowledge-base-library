---
title: Different starting value (recall non-positive definite Hessian)
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Different starting value (recall non-positive definite Hessian)

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

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

[← BFGS with specific relative tolerance on 'x', given precision loss message.](25-bfgs-with-specific-relative-tolerance-on-x-given-precision-l.md) · [Up: contents](index.md) · [Arbitrarily bad starting values →](27-arbitrarily-bad-starting-values.md)
