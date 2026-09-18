---
title: 8 FDR Control
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/multiple-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/multiple-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/multiple-testing.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 8 FDR Control

Elegant but fragile proof due to Storey, Taylor, Siegmund (2002)

Assume $#\{i: H_{0i} \text{ true}\} = m_0$ indep. $p_i \sim U[0,1]$ under $H_{0i}$

Let $V(t) = #\{i \in H_{0c}: p_i \leq t\}$

$\text{FDR} = \mathbb{E}[\text{FDP}] = \mathbb{E}\left[\frac{V(T)}{R(T)} \cdot 1\{R(T) > 0\}\right]$

Then FDR $= \mathbb{E}[\text{FDP}] = \mathbb{E}[\mathbb{E}[\text{FDP} | T]] \leq \mathbb{E}[m_0T/(mT)] = \alpha m_0/m \leq \alpha$

Note: $Q(t) = V(t)/(mt)$ is a martingale when $t$ runs backwards from $t=1$ to $t=0$

$\mathbb{E}[V(s) | V(t)] = V(t) \cdot s/t$

$\mathbb{E}[1\{p_i \leq s\} | 1\{p_i \leq t\}, V(t)] = s/t \cdot 1\{p_i \leq t\}$

And $T$ is a stopping time w.r.t. the filtration $\mathcal{F}_t$ of $\{V(t), R(t)\}$ (again, filtration with $t=1 \to t=0$)

Why? For $s<t$, $R(s) = #\{i: p_i \leq s\}$

$\mathbb{E}[1\{p_i \leq s\} | \mathcal{F}_t] = s/t \cdot 1\{p_i \leq t\}$

$\hat{F}(s) = R(s)/m$

$$
Insert graph showing $\hat{F}(t)$ vs $t/\alpha$ and $Q(t)$
$$

$\text{FDR} = \alpha \mathbb{E}[V(T)/(mT)] = \alpha \mathbb{E}[Q(T)] = \alpha \mathbb{E}[Q(1)] = \alpha m_0/m$

## 8.1 Remarks {.anchored number="8.1" anchor-id="remarks"}

- Proof only works if p-values indep., null ones exactly uniform
- More robust proof shows FDR controlled when null p-values conservative
- Can be extended to positive dependence
- FDR controlled under general dependence if we use corrected level $\alpha m / (m+1-i)$
- $\sum_{i=1}^m 1/i \approx \log m + 0.577$

---

[← 5 Deduced Inference](02-5-deduced-inference.md) · [Up: contents](index.md)
