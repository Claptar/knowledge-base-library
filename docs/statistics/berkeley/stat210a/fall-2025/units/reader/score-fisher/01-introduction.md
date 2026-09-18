---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/score-fisher.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## Score Function and Fisher Information {#score-function-and-fisher-information .title}

$$
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cP}{\mathcal{P}}
\newcommand{\cX}{\mathcal{X}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\td}{\,\textrm{d}}
\newcommand{\simiid}{\stackrel{\textrm{i.i.d.}}{\sim}}
\newcommand{\simind}{\stackrel{\textrm{ind.}}{\sim}}
\newcommand{\eqas}{\stackrel{\textrm{a.s.}}{=}}
\newcommand{\eqPas}{\stackrel{\cP\textrm{-a.s.}}{=}}
\newcommand{\eqmuas}{\stackrel{\mu\textrm{-a.s.}}{=}}
\newcommand{\eqD}{\stackrel{D}{=}}
\newcommand{\indep}{\perp\!\!\!\!\perp}
\DeclareMathOperator*{\minz}{minimize\;}
\DeclareMathOperator*{\maxz}{minimize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
$$

Under construction

Think through “tangent family” part… is it really helping, or can it be combined with curved exponential family example?

Add back in figures from handwritten notes.

### 1 Outline {.anchored number="1" anchor-id="outline"}

1.  Score function
2.  Fisher information
3.  Cramér-Rao Lower Bound
4.  Examples

### 2 Motivation: Tangent Family {.anchored number="2" anchor-id="motivation-tangent-family"}

Consider a family of densities:

$$
p(x; \theta) = e^{\theta'T(x) - A(\theta)}h(x)
$$

where $\theta \in \RR^d$ and $A(\theta) = \log \int e^{\theta'T(x)}h(x)dx$.

For this family:

- $T(X)$ is complete sufficient
- $T(X)$ is minimal
- $\PP_\theta(T(X) = t) = e^{\theta't - A(\theta)}$
- $\EE_\theta[T(X)] = A'(\theta)$

Let $\theta_0 \in \RR^d$ be fixed. Define the **tangent family**

$$
q(x; t) = e^{t'\nabla l_{\theta_0}(x) - k(t)}p_{\theta_0}(x)
$$

where $k(t) = \log \int e^{t'\nabla l_{\theta_0}(x)}p_{\theta_0}(x)dx$.

Then $\nabla l_{\theta_0}(X)$ is complete sufficient for the tangent family at $\theta_0$.

This is called the Score function.

### 3 Score Function {.anchored number="3" anchor-id="score-function"}

Assume a family $\cP$ has densities $p_\theta$ with respect to a measure $\mu$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that these densities have common support: that $\{x: p_\theta(x) > 0\}$ is the same for all $\theta$.

Recall the log-likelihood is $l(\theta;X) = \log p_\theta(X)$ (thought of as a random function of $\theta$)

**Definition:** The *Score function* is $\nabla l_\theta(X)$.

It plays a key role in many areas of statistics, especially in asymptotics. We can think of it as a “local complete sufficient statistic.” For $\eta \approx 0$, and $\theta_0 \in \Theta^\circ$, we have

$$
p_{\theta_0+\eta}(x) = e^{\ell(\theta_0 + \eta; x)} \approx e^{\eta'\nabla \ell(\theta_0;x)}p_{\theta_0}(x).
$$

---

[Up: contents](index.md) · [4 Differential Identities and the Fisher Information →](02-4-differential-identities-and-the-fisher-information.md)
