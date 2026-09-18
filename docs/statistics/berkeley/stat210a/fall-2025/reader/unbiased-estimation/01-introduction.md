---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/unbiased-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/unbiased-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/unbiased-estimation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

1.  [Course Reader](../introduction/index.md)
2.  [Unbiased Estimation](index.md)

## Unbiased Estimation {#unbiased-estimation .title}

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
\DeclareMathOperator*{\maxz}{maximize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
\newcommand{\ep}{\varepsilon}
$$

### 1 Unbiased Estimation {#unbiased-estimation-1 .anchored number="1" anchor-id="unbiased-estimation"}

Recall from [Lecture 2](../estimation/index.md) that we had two primary strategies to choose an estimator:

1.  Summarize the risk function by a scalar (average or supremum)
2.  Restrict attention to a smaller class of estimators

Today we’ll discuss *unbiased estimation*, which is an example of the second strategy. That is, if $g(\theta)$ is our estimand, we will require that $\EE_\theta \delta = g(\theta)$ for all $\theta$

Unbiased estimation is especially convenient in models with a complete sufficient statistic $T(X)$. In that case:

- There is at most one unbiased estimator of the form $\delta(T(X))$, because if $\delta_1, \delta_2(T)$ are both unbiased, then $\delta_1 \eqas \delta_2$
- If an unbiased estimator exists, it **uniformly minimizes** risk for any convex loss function

---

[Up: contents](index.md) · [2 Convex Loss Functions →](02-2-convex-loss-functions.md)
