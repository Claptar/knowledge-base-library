---
title: Permutation Tests
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture17-F24.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-F24.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture17-F24.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Permutation Tests

Even if we don't get a UMPU test at the end, conditioning on null suff. stat. still helps.

**Ex.** $X_1, \dots, X_n \overset{\text{iid}}{\sim} P \quad Y_1, \dots, Y_m \overset{\text{iid}}{\sim} Q \qquad H_0 : P = Q \quad H_1 : P \ne Q$

Under $H_0$, $P = Q$, $X_1, \dots, X_n, Y_1, \dots, Y_m \overset{\text{iid}}{\sim} P$

Let $(Z_1, \dots, Z_{n+m}) = (X_1, \dots, X_n, Y_1, \dots, Y_m)$

Under $H_0$, $U(Z) = (Z_{(1)}, \dots, Z_{(n+m)})$ compl. suff.

Let $S_{n+m} = \{ \text{Permutations on } n+m \text{ elements} \}$

$$(X, Y) \mid U \overset{H_0}{\sim} \text{Unif}\left(\{ \pi U : \pi \in S_{n+m} \}\right)$$

Thus, for any test stat $T$, if $P = Q$,
$$\mathbb{P}_{P, Q}(T(Z) \ge t \mid U) = \frac{1}{(n+m)!} \sum_{\pi \in S_{n+m}} \mathbf{1}\{ T(\pi Z) \ge t \}$$

**Monte Carlo test:** In practice, we sample
$$\pi_1, \dots, \pi_B \overset{\text{iid}}{\sim} S_{n+m}, \qquad \text{e.g. } B = 1000$$

Then $Z, \pi_1 Z, \dots, \pi_B Z \overset{\text{iid}}{\sim} \text{Unif}(S_{n+m} U)$ under $H_0$

MC $p$-value
$$p = \frac{1}{1 + B} \sum_{b=1}^B \mathbf{1}\{ T(Z) \le T(\pi_b Z) \}$$
$$\overset{H_0}{\sim} \text{Unif}\left(\left\{ \frac{1}{1+B}, \dots, \frac{B-1}{1+B}, 1 \right\}\right) \quad (\text{if no ties})$$
$$(p \ge \text{Unif}(\cdot) \quad \text{if there are ties})$$

---

[← Proof](03-proof.md) · [Up: contents](index.md)
