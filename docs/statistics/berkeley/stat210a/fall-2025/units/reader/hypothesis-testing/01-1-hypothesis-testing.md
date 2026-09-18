---
title: 1 Hypothesis Testing
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hypothesis-testing.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/hypothesis-testing.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`units/reader/hypothesis-testing.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/hypothesis-testing.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Hypothesis Testing

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

## 1 Hypothesis Testing {.anchored number="1" anchor-id="hypothesis-testing"}

Assume we have a larger model $\cP = \{P_\theta: \theta \in \Theta\}$ (which, as usual, may be “nonparametric” if $\theta$ is an infinite-dimensional object like a density), and two competing hypotheses about where $\theta$ lies:

- Null hypothesis: $H_0: \theta \in \Theta_0$

- Alternative hypothesis: $H_1: \theta \in \Theta_1$

These hypotheses should be *disjoint*, meaning $\Theta_0 \cap \Theta_1 = \emptyset$, and *exhaustive*, meaning $\Theta_0 \cup \Theta_1 = \Theta$. Sometimes $\Theta_0$ is specified and $\Theta_1$ is left unspecified; in that case you can assume $\Theta_1 = \Theta \setminus \Theta_0$.

A few examples to have in mind:

**Example 1 (Gaussian summary statistic, a.k.a. $Z$-test):** We observe $Z \sim N(\theta,1)$ (which is commonly a summary statistic $Z(X)$ from a large data set) and we want to draw an inference about $\theta$. Two common hypothesis testing settings are the *one-sided* hypotheses $H_0:\; \theta \leq \theta_0$ vs $H_1:\; \theta > \theta_0$ and the *two-sided* hypotheses $H_0:\; \theta = \theta_0$ vs $H_1:\; \theta \neq \theta_0$.

**Example 2 (Two-sample nonparametric testing):** We observe two samples, $X_1,\ldots,X_n \simiid P$ and $Y_1,\ldots,Y_m \simiid Q$, independently of each other. Without making any further assumptions about $P$ and $Q$, we want to test the *nonparametric* hypotheses $H_0:\; P = Q$ vs $H_1:\; P \neq Q$.

A hypothesis is called *simple* if it fully specifies the data distribution, and *composite* otherwise. In the examples above, the point null hypothesis $H_0:\; \theta = \theta_0$ is a simple hypothesis, and the other five are composite.

We’d like to use the data $X\sim P_\theta$ to determine which of $H_0$ or $H_1$ is true, but if a statistician has been called in then this is usually not possible through pure deductive reasoning. For example, if the distributions $P_\theta$ all have the same support, then any data set $X$ we see is logically consistent with any value of $\theta$ in the parameter space.

As usual, we have two options to get around this problem: we can beg the question (the Bayesian approach) or change the subject (the frequentist approach). The Bayesian answer to this problem is clean and simple: just calculate the posterior probabilities $\Lambda(\Theta_0 \mid X) = \PP(\theta \in \Theta_0 \mid X)$ and $\Lambda(\Theta_1 \mid X) = \PP(\theta \in \Theta_1 \mid X)$.

But there are a variety of settings where this is regarded as unappealing: scientists, drug companies, and others often work very hard to design carefully controlled experiments where the only stochastic assumptions made are ones that very few people would disagree with, and we’d like to be able to analyze the data from those experiments without having to layer on any further assumptions.

The frequentist approach to this conundrum is to replace *inductive reasoning* with *inductive behavior*: we will come up with a decision rule to decide between the two hypotheses based on the data. Formally, we can say we will either

1.  Reject $H_0$ (conclude that $H_0$ is implausible and $H_1$ must be true), or

2.  Accept $H_0$ (go on believing $H_0$).

There is a basic asymmetry here in that $H_0$ is privileged as the default choice to be disconfirmed, or else corroborated. An analogy is often drawn to a criminal trial where the defendant is innocent until proven guilty.

In reality, of course, our credence in the null (or alternative) hypothesis should be continuous in the evidence that we observe; it would be ridiculous to flip from 100% belief in the null to 100% belief in the alternative just at the point where a normal random variable crosses some threshold. But there are real-world situations in which a dichotomous decision must be made. For example, should the FDA approve a drug, or not? Or, do we need to control for some variable in our experimental setup, or not? Still, it is helpful to retain some critical distance from the conceit that we are ever really dichotomously “rejecting” or “accepting” either hypothesis in an epistemic sense.

In many settings where hypothesis testing is applied, including the examples of two-sided $Z$-testing and two-sample nonparametric testing above, there will always be points in the alternative hypothesis that explain the data even better than the null hypothesis does. As a result, even if we accept the conceit of making a dichotomous decision about what to “conclude,” it is implausible that we would ever “accept” $H_0$ in the sense of regarding $H_1$ as disconfirmed, even in an approximate sense. As a result, it is usually preferable to say that we “fail to reject $H_0$” rather than saying we accept it. Though we will continue to use “accept” as a technical term in what follows, “fail to reject” has less risk of inadvertently misleading non-statisticians.

---

[Up: contents](index.md) · [2 The critical function →](02-2-the-critical-function.md)
