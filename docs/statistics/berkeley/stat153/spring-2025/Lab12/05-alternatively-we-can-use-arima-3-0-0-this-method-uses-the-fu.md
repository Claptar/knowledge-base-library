---
title: Alternatively, we can use ARIMA(3, 0, 0). This method uses the full MLE
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab12.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Alternatively, we can use ARIMA(3, 0, 0). This method uses the full MLE

**Source:** [`Lab12.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab12.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

mod1 = ARIMA(np.diff(y), order=(3, 0, 0), trend='c').fit()
print(mod1.summary())

---

[← AutoReg uses OLS (also known as conditional MLE) for parameter estimation.](04-autoreg-uses-ols-also-known-as-conditional-mle-for-parameter.md) · [Up: contents](index.md) · [Both these methods give similar but slightly different answers →](06-both-these-methods-give-similar-but-slightly-different-answe.md)
