---
title: FDR Control
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# FDR Control

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Elegant but fragile proof due to Storey, Taylor, Siegmund (2002)

Assume $\#\{i: H_{0i} \text{ true}\} = m_0$ indep. $p_i \sim U[0,1]$ under $H_{0i}$

Let $V(t) = \#\{i \in H_{0c}: p_i \leq t\}$

$\text{FDR} = \mathbb{E}[\text{FDP}] = \mathbb{E}\left[\frac{V(T)}{R(T)} \cdot 1\{R(T) > 0\}\right]$

Then FDR $= \mathbb{E}[\text{FDP}] = \mathbb{E}[\mathbb{E}[\text{FDP} | T]] \leq \mathbb{E}[m_0T/(mT)] = \alpha m_0/m \leq \alpha$

Note: $Q(t) = V(t)/(mt)$ is a martingale when $t$ runs backwards from $t=1$ to $t=0$

$\mathbb{E}[V(s) | V(t)] = V(t) \cdot s/t$

$\mathbb{E}[1\{p_i \leq s\} | 1\{p_i \leq t\}, V(t)] = s/t \cdot 1\{p_i \leq t\}$

And $T$ is a stopping time w.r.t. the filtration $\mathcal{F}_t$ of $\{V(t), R(t)\}$ (again, filtration with $t=1 \to t=0$)

Why? For $s<t$, $R(s) = \#\{i: p_i \leq s\}$

$\mathbb{E}[1\{p_i \leq s\} | \mathcal{F}_t] = s/t \cdot 1\{p_i \leq t\}$

$\hat{F}(s) = R(s)/m$

[Insert graph showing $\hat{F}(t)$ vs $t/\alpha$ and $Q(t)$]

$\text{FDR} = \alpha \mathbb{E}[V(T)/(mT)] = \alpha \mathbb{E}[Q(T)] = \alpha \mathbb{E}[Q(1)] = \alpha m_0/m$

### Remarks

- Proof only works if p-values indep., null ones exactly uniform
- More robust proof shows FDR controlled when null p-values conservative
- Can be extended to positive dependence
- FDR controlled under general dependence if we use corrected level $\alpha m / (m+1-i)$
- $\sum_{i=1}^m 1/i \approx \log m + 0.577$

---

[← Benjamini-Hochberg Procedure](07-benjamini-hochberg-procedure.md) · [Up: contents](index.md)
