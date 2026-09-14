---
title: Slutsky's Theorem
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/asymptotics.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/asymptotics.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Slutsky's Theorem

**Source:** [`reader/asymptotics.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/asymptotics.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Theorem (Slutsky): Assume $X_n \xrightarrow{d} X$, $Y_n \xrightarrow{p} c$. Then:

1. $X_n + Y_n \xrightarrow{d} X + c$
2. $X_n Y_n \xrightarrow{d} cX$
3. $X_n / Y_n \xrightarrow{d} X/c$ if $c \neq 0$

Proof: Show $(X_n, Y_n) \xrightarrow{d} (X, c)$, apply continuous mapping.

Wouldn't normally be true that $X_n \xrightarrow{d} X$, $Y_n \xrightarrow{d} Y$ implies $X_n + Y_n \xrightarrow{d} X + Y$ without specifying joint dist.

---

[← Continuous Mapping Theorem](04-continuous-mapping-theorem.md) · [Up: contents](index.md) · [Delta Method →](06-delta-method.md)
