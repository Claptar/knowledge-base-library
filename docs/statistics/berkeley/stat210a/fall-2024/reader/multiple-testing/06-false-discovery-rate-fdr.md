---
title: False Discovery Rate (FDR)
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/multiple-testing.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/multiple-testing.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# False Discovery Rate (FDR)

**Source:** [`reader/multiple-testing.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/multiple-testing.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Problem: With 10K independent test statistics, all at level $\alpha = 0.001$, we expect 10 rejections just by chance. What if we get 50? Probably only ~20 of them are false rejections.

Can we accept 10 false rejections as long as most rejections are valid?

Benjamini-Hochberg (1995) proposed a more liberal error control criterion called FDR:

$R(X) = |R(X)|$ = rejections ("discoveries")
$V(X) = |R(X) \cap H_{0c}|$ = false discoveries

The FDP is:
$\text{FDP} = \begin{cases} V(X)/R(X) & \text{if } R(X) > 0 \\ 0 & \text{if } R(X) = 0 \end{cases}$

The FDR is $\mathbb{E}[\text{FDP}]$

---

[← Deduced Inference](05-deduced-inference.md) · [Up: contents](index.md) · [Benjamini-Hochberg Procedure →](07-benjamini-hochberg-procedure.md)
