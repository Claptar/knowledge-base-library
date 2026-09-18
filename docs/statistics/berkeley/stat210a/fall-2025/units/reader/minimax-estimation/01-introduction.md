---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/minimax-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## Minimax Estimation {#minimax-estimation .title}

Published

October 5, 2023

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

### 1 Minimax Risk Estimator {.anchored number="1" anchor-id="minimax-risk-estimator"}

#### 1.1 Definition of Minimax Risk {.anchored number="1.1" anchor-id="definition-of-minimax-risk"}

The last idea for choosing an estimator: worst-case risk.

Minimize $\sup_\theta R(\theta, \delta)$

The minimum achievable sup risk is called the minimax risk of the estimation problem:

$$
r = \inf_\delta \sup_\theta R(\theta, \delta)
$$

An estimator $\delta$ is called minimax if it achieves the minimax risk, i.e.,

$$
\sup_\theta R(\theta, \delta) = r
$$

#### 1.2 Game Theory Interpretation {.anchored number="1.2" anchor-id="game-theory-interpretation"}

1.  Analyst chooses estimator $\delta$
2.  Nature chooses parameter $\theta$ to maximize risk

Note: Nature chooses $\theta$ adversarially, not $X$.

Compare to Bayes where Nature chooses prior from a known distribution (Nature plays a specific mixed strategy).

We will look for Nature’s Nash equilibrium strategy.

---

[Up: contents](index.md) · [2 Least Favorable Priors →](02-2-least-favorable-priors.md)
