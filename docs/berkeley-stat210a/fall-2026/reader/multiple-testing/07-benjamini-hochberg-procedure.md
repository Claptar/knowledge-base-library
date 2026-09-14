---
title: Benjamini-Hochberg Procedure
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Benjamini-Hochberg Procedure

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

B-H also proposed a method to control FDR given ordered p-values $p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}$:

$R(X) = \max\{r: p_{(r)} \leq \alpha r/m\}$ (called step-up procedure)

Reject $H_{0(1)},\ldots,H_{0(R)}$

This is much more liberal than Bonferroni procedure:
When $\alpha = 0.05$, B-H rejects at least $r$ p-values if $p_{(r)} \leq 0.05r/m$

### B-H as Empirical Bayes

Equivalent formulation for $R(t) = \#\{p_i \leq t\}$:
Let $\hat{F}(t) = R(t)/m$ = estimate of CDF of p-values

B-H rejects $H_i$ if $p_i \leq T(X) = \max\{t: \hat{F}(t) \geq t/\alpha\}$

When $\hat{F}(t)$ is continuously increasing in $t$ except at jump values where it jumps down:

$\hat{F}(T(X)) = T(X)/\alpha$

[Insert graph showing $\hat{F}(t)$ vs $t/\alpha$]

Only values of $t$ that matter for the algorithm are $t = p_i$ where $\hat{F}(t) = t/\alpha$, i.e., $\alpha i/m = p_{(i)}$

---

[← False Discovery Rate (FDR)](06-false-discovery-rate-fdr.md) · [Up: contents](index.md) · [FDR Control →](08-fdr-control.md)
