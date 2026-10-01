---
title: 3 Notation
source: https://doi.org/10.1101/2020.09.25.312868/
source_file: sources/papers/gorin-pachter-2020-intrinsic-extrinsic/gorin-pachter-2020-intrinsic-extrinsic.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2020-intrinsic-extrinsic.pdf` from [papers/gorin-pachter-2020-intrinsic-extrinsic](https://doi.org/10.1101/2020.09.25.312868/) — papers · gorin-pachter-2020-intrinsic-extrinsic, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 3 Notation

## 3.1 Model parametrization

Model-independent quantities and statistics are defined in Table 1. The two models' parameters
are defined in Tables 2 and 3. Finally, $x_z$, where $x$ is a statistic computed from data moments
(e.g., $\mu_M$, $\sigma_M^2$, $\rho$, $\gamma$) and $z \in \{i, e\}$ refers to the predicted value of
that statistic based on either the *i*ntrinsic or *e*xtrinsic noise model. For example, $\mu_{M,i}$
refers to the predicted mean mature mRNA copy number under the intrinsic noise model, while
$\rho_e$ refers to the predicted nascent–mature correlation under the extrinsic noise model.

A probability mass function (PMF) associated with a discrete-valued random variable $X$ is
equivalently denoted by $P(\cdot;\cdot)$ or $P(X=k;\cdot)$. A probability density function (PDF)
associated with a continuous-valued random variable is denoted by $f(\cdot;\cdot)$.

## 3.2 Probability distributions

The geometric distribution is defined as follows: if $X \sim Geom(p)$,
$P(X=k;p) = (1-p)^k p$, where $p \in (0,1]$ and $k \in \mathbb{N}_0$. The geometric distribution is
well-known to arise in the short-burst limit of the two-state transcription model [25].

The negative binomial distribution is defined as follows: if $X \sim NegBin(r,p)$,
$P(X=k;r,p) = \frac{\Gamma(r+k)}{k!\Gamma(r)}(1-p)^r p^k$, where $p \in [0,1]$ and $r > 0$. We note
that MATLAB and the NumPy library take the opposite convention, with a $\bar{p}$ parameter defined
as $1-p$.

The gamma distribution is defined as follows: if $X \sim Gamma(\alpha,\eta)$,
$f(x;\alpha,\eta) = \frac{\eta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\eta x}$. This is the
shape/rate parametrization. We note that MATLAB and the NumPy library take the opposite
shape/scale parametrization with parameter $\theta = \eta^{-1}$. Furthermore, the rate $\eta$ is
usually given the variable name "$\beta$"; however, we use the current convention to preclude
confusion with the splicing rate parameter.

**Table 1: Observation variables**

| Parameter | Definition |
| --- | --- |
| $n$ | Number of nascent mRNA |
| $m$ | Number of mature mRNA |
| $N$ | Random variable denoting number of nascent mRNA; $N \in \mathbb{N}_0$ |
| $M$ | Random variable denoting number of mature mRNA; $M \in \mathbb{N}_0$ |
| $\gamma$ | Degradation rate |
| $\mu_z, \mathbb{E}[Z]$ | Expectation of species $Z \in \{N, M\}$ |
| $\mu$ | Expectation of an arbitrary distribution |
| $\sigma_z^2$ | Variance of species $Z \in \{N, M\}$ |
| $\sigma^2$ | Variance of an arbitrary distribution $Z \in \{N, M\}$ |
| $Cov(N,M)$ | Covariance nascent and mature copy numbers |
| $\rho$ | Pearson correlation coefficient |
| $q$ | Computed statistic $\frac{\sigma_N^2}{\mu_N} - 1$ |
| $P(n,m;\cdot)$ | Joint PMF of nascent and mature mRNA, shorthand for $P(N=n, M=m;\cdot)$ |
| $P(\cdot;\cdot)$ | PMF of an arbitrary parametrized discrete random variable |
| $f(\cdot;\cdot)$ | PDF of an arbitrary parametrized continuous random variable |

**Table 2: Intrinsic noise model parameters**

| Parameter | Definition |
| --- | --- |
| $k_i$ | Burst frequency |
| $B$ | Geometric random variable denoting burst size |
| $b$ | Mean of $B$ |
| $\beta$ | Splicing rate |
| $\gamma$ | Degradation rate |
| $f$ | $\frac{\beta}{\beta+\gamma}$, non-dimensional splicing rate |

**Table 3: Extrinsic noise model parameters**

| Parameter | Definition |
| --- | --- |
| $K$ | Gamma-distributed random variable denoting transcription rate |
| $\alpha$ | Shape of gamma distribution |
| $\eta$ | Rate of gamma distribution |
| $\beta$ | Splicing rate |
| $\gamma$ | Degradation rate |
| $f$ | $\frac{\beta}{\beta+\gamma}$, non-dimensional splicing rate |

---

[← 2 Two models for gene expression](02-2-two-models-for-gene-expression.md) · [Up: contents](index.md) · [4 Preliminaries →](04-4-preliminaries.md)
