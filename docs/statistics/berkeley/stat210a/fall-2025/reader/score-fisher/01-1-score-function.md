---
title: 1 Score Function
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# 1 Score Function

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

## 1 Score Function {.anchored number="1" anchor-id="score-function"}

In this section we introduce the score function and Fisher information, two concepts that are central in asymptotic statistics. We

Assume a family $\cP$ has densities $p_\theta$ with respect to a measure $\mu$, for $\theta \in \Theta \subseteq \RR^d$. Assume additionally that these densities have common support: that $\{x: p_\theta(x) > 0\}$ is the same for all $\theta$ (since we can truncate the sample space to this common support, we could just as well assume $p_\theta(x) > 0$ for all $x$ and $\theta$).

**Definition:** The *Score function* is defined as $S_{\theta}(X) = \nabla \ell(\theta;X)$, a random vector of dimension $d$.

We can think of the score function $S_{\theta_0}(X)$ at a given value $\theta_0$ as a kind of “local” sufficient statistic that we could use to distinguish between $\theta$ values in a small neighorhood of $\theta_0$.

To see why, recall that the log-likelihood $\ell(\theta;X) = \log p_\theta(X)$, thought of as a random function with argument $\theta$, is a minimal sufficient statistic for $X$, up to a vertical shift.

Wait! Didn’t we say a statistic can’t be a function of $\theta$?

Yes, but what we meant by this is, more precisely, is that a statistic can be calculated from the data, by an analyst who doesn’t know what is the *true* value of $\theta$ that governed the sampling distribution of the data $X$.

The trouble is that there is a bit of notational ambiguity when we write $\ell(\theta;X)$. If we want to be a bit more precise, what we mean here is $\ell(\cdot; X)$, which is realized in the space of functions from $\theta$ to $\mathbb{R}$. If the analyst observes $X$ they can plot a graph of this whole likelihood function; that graph is the statistic.

On the other hand, suppose that instead we interpret $\ell(\theta;X)$ as the function *evaluated at* the true value $\theta$, i.e. in more pedantic notation $\left.\ell(\cdot; X)\right|_{\text{true } \theta}$. Then, this would *not* be a statistic because the analyst can’t calculate it without knowing which is the true value.

A third possibility is that we could be evaluating \$()

For any fixed reference point $\theta_0 \in \Theta$, we can subtract $\ell(\theta_0; X)$ to obtain the minimal sufficient statistic $\ell(\theta; X) - \ell(\theta_0; X)$. Then, for a nearby value $\theta = \theta_0 + \eta$, with $\eta$ small, we have

$$
\ell(\theta_0 + \eta; X) - \ell(\theta_0; X) \approx \eta'S_{\theta_0}(X),
$$

 so the statistic $S_{\theta_0}(X)$ would approximately capture all of the information in a “local” model $\{P_{\theta_0+\eta}: \eta \text{ small}\} \subseteq \cP$.

Is the score a statistic?

It depends. Sometimes the reference point $\theta_0$ is generic, or it might be specified by the analyst without knowing whether it is the true value of $\theta$; for example, we could be testing the null hypothesis $H_0:\;\theta = \theta_0$, without knowing whether the null is true. In that case, it is a statistic (and we’ll often call it a “score statistic”).

On the other hand, for many theoretical calculations, including most of the calculations in this section, we will be specifically interested in $S_\theta(X)$ for the *true* value of $\theta$ that is govering the sampling distribution $P_\theta$ of the data. In that case, the score is *not* a statistic.

When we study asymptotic statistics, local models like these will be natural objects of study, because a large data set will commonly allow us to rule out most $\theta$ values and only focus on values in a small neighborhood of the true parameter.

Or, writing it a different way, we have

$$
p_{\theta_0+\eta}(x) = e^{\ell(\theta_0 + \eta; x)} \approx e^{\eta'\nabla \ell(\theta_0;x)}p_{\theta_0}(x).
$$

This evokes some analogies between the score in a generic parametric family and the sufficient statistic in an exponential family. We’ll begin by looking at differential identities.

---

[Up: contents](index.md) · [2 Differential Identities and the Fisher Information →](02-2-differential-identities-and-the-fisher-information.md)
