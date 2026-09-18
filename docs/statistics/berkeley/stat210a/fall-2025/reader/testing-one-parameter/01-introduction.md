---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-one-parameter.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/testing-one-parameter.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-one-parameter.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

1.  [Course Reader](../introduction/index.md)
2.  [Testing with One Real Parameter](index.md)

## Testing with One Real Parameter {#testing-with-one-real-parameter .title}

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

### 1 Testing with one real parameter {#testing-with-one-real-parameter-1 .anchored number="1" anchor-id="testing-with-one-real-parameter"}

This lecture concerns the general problem of testing with one real parameter. We observe $X \sim P_\theta$ for $\theta \in \Theta \subseteq \RR$, and we might want to test a *one-sided alternative* like $H_0:\; \theta \leq \theta_0$ vs the one-sided alternative $H_1:\; \theta > \theta_0$, or a *point null* hypothesis like $H_0:\; \theta = \theta_0$ against a *two-sided alternative* $H_1:\; \theta \neq \theta_0$. Or, we could test an *interval null* $H_0:\; |\theta - \theta_0| \leq \delta$ vs the two-sided alternative $H_1:\; |\theta-\theta_0|>\delta$, for $\delta \geq 0$ (which reduces to the point null if $\delta = 0$).

---

[Up: contents](index.md) · [2 One-sided testing →](02-2-one-sided-testing.md)
