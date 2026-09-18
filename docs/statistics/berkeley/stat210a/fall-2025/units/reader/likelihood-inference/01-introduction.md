---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/likelihood-inference.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/likelihood-inference.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/likelihood-inference.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## Likelihood-Based Inference: Wald, Score, and Generalized Likelihood Ratio Tests {#likelihood-based-inference-wald-score-and-generalized-likelihood-ratio-tests .title}

Published

November 16, 2023

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

### 1 Likelihood-Based Inference {.anchored number="1" anchor-id="likelihood-based-inference"}

#### 1.1 Setting {.anchored number="1.1" anchor-id="setting"}

$X_1, \ldots, X_n \stackrel{\text{iid}}{\sim} p_\theta(x)$, $p_\theta \in \cP$, smooth in $\theta$

Assume: - $\mathbb{E}_\theta[\nabla \ell_\theta(X)] = 0$ - $\text{Var}_\theta[\nabla \ell_\theta(X)] = \mathbb{E}_\theta[-\nabla^2 \ell_\theta(X)] = J(\theta) > 0$ - MLE $\hat{\theta}$ Consistent

Then if $\theta = \theta_0$: - $\nabla \ell_n(\theta_0; X) \sim N(0, nJ(\theta_0))$ - $-\nabla^2 \ell_n(\theta_0; X) \xrightarrow{p} nJ(\theta_0)$

Used $\theta = \hat{\theta} + J^{-1}(\theta_0) \nabla \ell_n(\theta_0; X)/n + o_p(n^{-1/2})$ to get $\sqrt{n}(\hat{\theta} - \theta_0) \sim N(0, J^{-1}(\theta_0))$

Can use this for inference on $\theta_0$

---

[Up: contents](index.md) · [2 Wald-Type Confidence Regions →](02-2-wald-type-confidence-regions.md)
