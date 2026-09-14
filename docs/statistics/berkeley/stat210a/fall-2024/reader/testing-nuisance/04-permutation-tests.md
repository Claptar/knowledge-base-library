---
title: Permutation Tests
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-nuisance.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-nuisance.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Permutation Tests

**Source:** [`reader/testing-nuisance.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-nuisance.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Even if we don't get a UMPU test at the end, conditioning on null suff. stat. still helps

Example: $X_1, \ldots, X_n \sim \text{iid } P$, $Y_1, \ldots, Y_m \sim \text{iid } Q$
$H_0: P=Q$ vs $H_1: P \neq Q$

Under $H_0$: $P=Q$, $X_1, \ldots, X_n, Y_1, \ldots, Y_m \sim P$

Let $Z = (Z_1, \ldots, Z_{n+m}) = (X_1, \ldots, X_n, Y_1, \ldots, Y_m)$

Under $H_0$, $U = Z$ is complete sufficient

Let $S_{n+m}$ = Permutations on $n+m$ elements

$(X, Y) = (U_{\pi(1)}, \ldots, U_{\pi(n+m)})$ for $\pi \in S_{n+m}$

Thus for test stat $T$, if $P=Q$:

$$\mathbb{P}(T \geq t | U) = \frac{1}{(n+m)!}\sum_{\pi \in S_{n+m}} 1\{T(Z_{\pi(1)}, \ldots, Z_{\pi(n+m)}) \geq t\}$$

Monte Carlo test: In practice, we sample $\pi_1, \ldots, \pi_B \sim

---

[← Proof Sketch](03-proof-sketch.md) · [Up: contents](index.md)
