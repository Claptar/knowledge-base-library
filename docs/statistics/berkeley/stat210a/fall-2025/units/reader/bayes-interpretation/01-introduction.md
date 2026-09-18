---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/bayes-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/bayes-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/bayes-interpretation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## Interpretations of Probability and Sources of Priors {#interpretations-of-probability-and-sources-of-priors .title}

Published

September 26, 2023

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

### 1 Interpretations of Probability {.anchored number="1" anchor-id="interpretations-of-probability"}

Why do we model anything as random? What does probability mean in the real world?

#### 1.1 1. Long-run Frequency Over Repeated Trials {.anchored number="1.1" anchor-id="long-run-frequency-over-repeated-trials"}

- Examples:
  - Repeatedly flipping a coin
  - Shooting electrons at a double slit

Note: “You can never step into the same river twice.”

#### 1.2 2. Systematic Random Sampling from a Population {.anchored number="1.2" anchor-id="systematic-random-sampling-from-a-population"}

- Examples:
  - Survey of 500 random voters
  - Random assignment to treatment/control in controlled experiments

#### 1.3 3. Subjective Uncertainty About an Outcome {.anchored number="1.3" anchor-id="subjective-uncertainty-about-an-outcome"}

- Examples:
  - Chance that President Biden is re-elected
  - Higgs boson having a given mass
  - P = NP

Notes: - Could be broad intersubjective agreement - These are often conflated with \#1 - What if survey sampling is pseudo-random? - Probably relying on shared ignorance

---

[Up: contents](index.md) · [2 Where Does the Prior Come From? →](02-2-where-does-the-prior-come-from.md)
