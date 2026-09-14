---
title: Define objective (negative log-likelihood) function
source: https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd
source_file: sources/berkeley-stat243/fall-2024/units/unit11-optim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Define objective (negative log-likelihood) function

**Source:** [`units/unit11-optim.qmd`](https://github.com/berkeley-stat243/fall-2024/blob/9c62305d05fca31df0d9c6a3b68b350ad8722fee/units/unit11-optim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

def pp_negloglik(par, y, thresh, npy):
    mu, sc, sh = par
    uInd = y > thresh

    # Invalid parameter values or data/parameter combos:
    if sc <= 0:
        return 1e6
    if (1 + ((sh * (thresh - mu)) / sc) < 0):
        return 1e6

    y = (y - mu) / sc
    y = 1 + sh * y

    if np.min(y[uInd]) <= 0:
        return 1e6
    else:
        ytmp = y.copy()
        ytmp[~uInd] = 1 # 'zeroes' out those below the threshold after applying the log in next line

        l = np.sum(uInd * np.log(sc)) + np.sum(uInd * np.log(ytmp) * (1 / sh + 1)) + \
                   (len(y) / npy) * np.mean((1 + (sh * (thresh - mu)) / sc) ** (-1 / sh))

    return l

---

[← Create a histogram of the data](28-create-a-histogram-of-the-data.md) · [Up: contents](index.md) · [Initial parameter values →](30-initial-parameter-values.md)
