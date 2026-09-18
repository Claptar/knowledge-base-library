---
title: Where does $\Lambda$ come from?
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf
source_file: sources/berkeley-stat210a/fall-2024/handwritten/lecture10-bayesinterp.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`handwritten/lecture10-bayesinterp.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/handwritten/lecture10-bayesinterp.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Where does $\Lambda$ come from?

1) Interpretations of Probability
2) Where does prior come from?
3) Examples

---

## Interpretations of Probability

Why do we model anything as random?
What does "probability" mean in the real world?

1) **Long-run frequency over repeated trials**
   **Ex.** repeatedly flipping a coin
   shooting electrons at a double slit
   "you can never step into the same river twice"

2) **Systematic random sampling from a population**
   **Ex.** survey of 500 random voters
   random assignment to treatment/control
   Randomness comes from experimenter's actions

3) **Subjective uncertainty about an outcome**
   chance that...
   - President Biden is re-elected
   - Higgs boson has a given mass
   - $P = NP$
   - $100^{\text{th}}$ digit of $\pi$ is 5
   Could be broad intersubjective agreement

These are often intertwined:
**Ex.** What if survey sampling is pseudo-random?
Probably relying on shared ignorance

---

(Bayesian rejoinder: Where does $\mathcal{P}$ come from?)

Four main sources for prior on $\Theta$

### Source #1: Subjective beliefs

**Pro**: Brings all relevant info. to bear
Straightforward interp. of posterior

**Con**: Posterior is therefore subjective
Embarrassing to write "I think" in abstract
Hard if $\Theta$ high-dim or $\mathcal{P}$ nonparametric

**Ex**: Flip coin 20 times, get 7 heads
$0.5$ probably a better estimate than $0.35$
My subjective prior on coins:

```
    λ(θ)
     |
     |         |
     |         |
     |         |
     |         |
     |         |
     +---------+---------+
     0        0.5        1     θ
```

---

### Source #2: "Objective" or "vague" prior

Using default prior removes subjectivity
(But then what does the posterior mean?)

**Flat prior** $\lambda(\theta) \propto_\theta 1$ on $\Theta$
"Indifference" (in $\theta$ parameterization)
Often improper ($\Lambda(\Theta) = \infty$) but usually ok

**Ex**: $\theta \sim$ flat prior on $\mathbb{R}$
$X \mid \theta \sim N(\theta, \sigma^2)$

$$
\begin{aligned}
\lambda(\theta \mid x) &\propto_\theta p_\theta(x) \\
&= \frac{1}{\sqrt{2\pi}} e^{-(x-\theta)^2 / 2\sigma^2} \\
&\propto_\theta N(x, \sigma^2)
\end{aligned}
$$

$$
\begin{aligned}
\Lambda([\theta, \theta + \varepsilon)) &\approx \varepsilon \lambda(\theta) \propto \varepsilon \sqrt{J(\theta)} \\
&\approx \sqrt{D_{kl}(P_\theta \parallel P_{\theta+\varepsilon})}
\end{aligned}
$$

**Jeffreys prior** $\lambda(\theta) \propto_\theta |J(\theta)|^{1/2}$
Higher density where $P_\theta$ "changing faster"
Invariant to parameterization

**Ex**. $X \mid \theta \sim \text{Binom}(n, \theta)$

$$
\lambda(\theta) \propto_\theta J(\theta)^{1/2} = \left(\frac{n}{\theta(1-\theta)}\right)^{1/2} \propto_\theta \text{Beta}\left(\frac{1}{2}, \frac{1}{2}\right)
$$

$\lambda(\theta) \to \infty$ as $\theta \to 0$ or $1$:
$$
D_{\text{KL}}(0.001 \parallel 0.01) \underset{(35\times)}{\gg} D_{\text{KL}}(0.49 \parallel 0.5)
$$
$$
7n \cdot 10^{-3} \qquad\qquad 2n \cdot 10^{-4}
$$

```
   λ(θ) | \             /
        |  \___________/
        +----------------+
        0                1     θ
```

---

## Intersubjective Agreement

Data may effectively rule out most $\Theta$ values
$\rightsquigarrow$ Makes posterior uncontroversial

**Ex**. $X \sim \text{Binom}(10^4, \theta)$, observe $X = 3000$

$$
\text{SD}_\theta(X/n) = \sqrt{\frac{\theta(1-\theta)}{n}} \le 0.005
$$

$\Rightarrow \text{Lik}(\theta; X) \approx 0$ outside $C = [0.29, 0.31]$

All "reasonable" priors may be $\approx$ flat on $C$

$$
\begin{aligned}
\Rightarrow \lambda(\theta \mid X) &\tilde{\propto}_\theta \text{Lik}(\theta; X) \\
&\tilde{\propto}_\theta \exp\left\{ -\frac{J(0.3)}{2} (\theta - 0.3)^2 \right\} \\
&\propto_\theta N(0.3, J(0.3)^{-1})
\end{aligned}
$$

Data "swamps" everyone's prior

---

---

[Up: contents](index.md) · [Gaussian sequence model →](02-gaussian-sequence-model.md)
