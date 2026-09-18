---
title: Permutation Tests
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture17-nuisanceparams.pdf
source_file: sources/berkeley-stat210a/fall-2025/handwritten/lecture17-nuisanceparams.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture17-nuisanceparams.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/handwritten/lecture17-nuisanceparams.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Permutation Tests

Even if we don't get a UMPU test at the end, conditioning on null suff. stat. still helps.

**Ex.** $X_1, \dots, X_n \overset{\text{iid}}{\sim} P \qquad Y_1, \dots, Y_m \overset{\text{iid}}{\sim} Q \qquad H_0: P = Q \quad H_1: P \neq Q$

Under $H_0$, $P = Q$, $X_1, \dots, X_n, Y_1, \dots, Y_m \overset{\text{iid}}{\sim} P$

Let $(Z_1, \dots, Z_{n+m}) = (X_1, \dots, X_n, Y_1, \dots, Y_m)$

Under $H_0$, $U(Z) = (Z_{(1)}, \dots, Z_{(n+m)})$ compl. suff.

Let $S_{n+m} = \{ \text{Permutations on } n+m \text{ elements} \}$

$$(X, Y) \mid U \overset{H_0}{\sim} \text{Unif}\left( \{ \pi U : \pi \in S_{n+m} \} \right)$$

Thus, for any test stat $T$, if $P = Q$,

$$\mathbb{P}_{P, Q}(T(Z) \geq t \mid U) = \frac{1}{(n+m)!} \sum_{\pi \in S_{n+m}} \mathbf{1}\{ T(\pi Z) \geq t \}$$

**Monte Carlo test:** In practice, we sample

$$\pi_1, \dots, \pi_B \overset{\text{iid}}{\sim} S_{n+m}, \qquad \text{e.g. } B = 1000$$

Then $Z, \pi_1 Z, \dots, \pi_B Z \overset{\text{iid}}{\sim} \text{Unif}(S_{n+m} U)$ under $H_0$

MC $p$-value:

$$p = \frac{1}{1+B} \left( 1 + \sum_{b=1}^B \mathbf{1}\{ T(Z) \leq T(\pi_b Z) \} \right)$$

$$\overset{H_0}{\sim} \text{Unif}\left( \left\{ \frac{1}{1+B}, \dots, \frac{B-1}{1+B}, 1 \right\} \right) \quad (\text{if no ties})$$

$$(p \geq \text{Unif}(\cdot) \quad \text{if there are ties})$$

---

## One-sample t-test ($n=2$)

**Ex** $X_1, X_2 \overset{\text{iid}}{\sim} N(\mu, \sigma^2) \qquad \sigma^2 > 0 \text{ unknown}$

$$H_0: \mu = 0 \quad \text{vs.} \quad H_1: \mu \neq 0$$

$$\begin{aligned}
p_{\mu, \sigma^2}(x) &= \frac{1}{2\pi \sigma^2} e^{-\frac{1}{2\sigma^2} \sum_{i=1}^2 (X_i - \mu)^2} \\
&= e^{\overbrace{\frac{\mu}{\sigma^2}}^{\theta} \overbrace{\sum X_i}^{T = \bar{X}} - \overbrace{\frac{1}{2\sigma^2}}^{\lambda} \overbrace{\sum X_i^2}^{u = \|X\|^2} - \frac{\mu^2}{\sigma^2}} \cdot \frac{1}{2\pi \sigma^2}
\end{aligned}$$

Optimal test rejects when $T = X_1 + X_2$ is extreme given $T = \|X\|^2$

If $\mu = 0$, $P$ is rotationally symmetric

$$\Rightarrow X \text{ rotationally symmetric}, \quad \frac{X}{\|X\|} \perp\!\!\!\perp \|X\|^2$$

$$\iff X / \|X\|^2 = u \overset{H_0}{\sim} \text{Unif}(\sqrt{u} \cdot S^1)$$

where $S^1 = \text{unit circle}$

---

## Geometric Picture

```
                X₂ ^
                   |             / X₁ = X₂ line
                   |            /
                   |           /
                   |      ..-*""*-.   largest values of T = X₁ + X₂
                   |    .'  /   *  '.                    = 1₂' X
                   |   /   /     *   \
                   |  /   /       *   \ X
                   | ;   /         *   ;
                   | :  /           *  : Conditioning set: ||X|| · S¹
                1₂ |;  /             * ;   X | ||X||² ~ Unif(||X|| · S¹)
                 \ |: /              * :
       -----------+-+----------------+------>
                 /| :                 :       X₁
                / | ;                 ;
               /  |  \               /  two-sided p(X)
              /   |   \             /             = 4 · ∢(1₂, X)
             *    |    '.         .'
            *     |      '-.....-'
           *      |       /
      Smallest    |      /
      values of   |     /
      T = 1₂' X   |    /
```

---

## t-statistic

Above test rejects for:

* conditionally extreme $1_2' X$ given $\|X\|^2$
* ($\text{equiv.}$) marginally extreme $R = \frac{1_2' X}{\sqrt{2} \cdot \|X\|} = \cos \sphericalangle(1_2, X)$

  (since $R \perp\!\!\!\perp \|X\|^2$)

* ($\text{equiv.}$) marginally extreme $T = \frac{R}{\sqrt{1-R^2}} \overset{H_0}{\sim} t_1$

  $= \cot \sphericalangle(1_2, X)$

---

## Geometric Picture

$$T = \frac{R}{\sqrt{1-R^2}} = \frac{\|\text{Proj}_{1_2} X\|}{\|\text{Proj}_{1_2}^\perp X\|} \cdot \text{sgn}(\bar{X})$$

```
                   X₂ ^
                      |             / X₁ = X₂ line
                      |            /
                      |           /
                      |      .---*---.
                      |    .'   /     '.
                      |   /    /   -->  \  ||X|| · √(1 - R²) = ||Proj_{1_n}^⊥ X||
                      |  /    /   /      \ X
                      | ;    /   /        ;
                      | :   /   /         :
                   1₂ |;   /   /          ;
                    \ |:  /  / ∢(1, X)    :
          -----------+-+-/---------------+------>
                     /| :                 :       X₁
                    / | ;                 ;
                   /  |  \               /
                  /   |   \             /
                 /    |    '.         .'
                /     |      '-------'
               /      |       /
                      |      /
```
(Vector along line: $\|X\| \cdot R = \|\text{Proj}_{1_n} X\|$)

**Next major theme**: ratios of projections

---

## One-sample t-test

**Ex** $X_1, \dots, X_n \overset{\text{iid}}{\sim} N(\mu, \sigma^2) \qquad \mu, \sigma^2 \text{ unknown}$

$$H_0: \mu = \mu_0 \quad \text{vs} \quad H_1: \mu \neq \mu_0$$

Same logic: Reject for extreme $\bar{X}$ given $\|X\|^2$

$$\iff \text{Reject for extreme } R = \frac{1_n' X}{\sqrt{n} \cdot \|X\|} = \frac{\sqrt{n} \, \bar{X}}{\|X\|}$$

$$\iff \text{Reject for extreme}$$

$$\begin{aligned}
T &= \sqrt{n-1} \cdot \frac{R}{\sqrt{1-R^2}} \\
&= \sqrt{n-1} \cdot \frac{\sqrt{n} \, \bar{X}}{\sqrt{\|X\|^2 - n\bar{X}^2}} = \frac{\sqrt{n} \, \bar{X}}{\sqrt{S^2}}
\end{aligned}$$

for sample variance

$$\begin{aligned}
S^2 &= \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2 \\
&= \frac{1}{n-1} \|X - \bar{X} 1_n\|^2 \quad \leftarrow \|\text{Proj}_{1_n}^\perp X\|^2 \\
&= \frac{1}{n-1} \left( \|X\|^2 - n\bar{X}^2 \right) \\
&\sim \frac{\sigma^2}{n-1} \chi_{n-1}^2
\end{aligned}$$

**Next major theme**: ratios of projections

---

[← Step 3](04-step-3.md) · [Up: contents](index.md)
