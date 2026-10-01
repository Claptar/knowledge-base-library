---
title: 4 Preliminaries
source: https://doi.org/10.1101/2020.09.25.312868/
source_file: sources/papers/gorin-pachter-2020-intrinsic-extrinsic/gorin-pachter-2020-intrinsic-extrinsic.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2020-intrinsic-extrinsic.pdf` from [papers/gorin-pachter-2020-intrinsic-extrinsic](https://doi.org/10.1101/2020.09.25.312868/) — papers · gorin-pachter-2020-intrinsic-extrinsic, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Preliminaries

## 4.1 Intrinsic noise model

### 4.1.1 Probability mass function

The full joint distribution for the burst model requires numerical integration and Fourier
transformation [7]. To our knowledge, no analytical solution exists, although approximations in
terms of hypergeometric functions are available [26].

The nascent marginal is distributed per $NegBin\left(\frac{k_i}{\beta}, \frac{b}{1+b}\right)$. The
mature marginal is NB-distributed in the limit of low $\beta$ and Poisson-distributed in the limit
of high $\beta$. Although the distribution in the intermediate region is qualitatively similar to
NB, it does not appear to be *exactly* representable as NB. Furthermore, even the determination of
the closest NB approximation according to some divergence metric is an open problem, although
method of moments approximations may be satisfactory for some purposes.

### 4.1.2 Moments

Per the results from Singh and Bokes [20]:

$$\mu_N = \frac{k_i b}{\beta}$$

$$\mu_M = \frac{k_i b}{\gamma}$$

$$\sigma_N^2 = \mu_N(1+b) = \frac{k_i b}{\beta}(1+b)$$

$$\sigma_M^2 = \mu_M\left(1 + \frac{b\beta}{\beta+\gamma}\right) = \frac{k_i b}{\gamma}\left(1 + \frac{b\beta}{\beta+\gamma}\right)$$

$$Cov(N,M) = \frac{\mu_N b\beta}{\beta+\gamma} = \frac{k_i b}{\beta}\frac{b\beta}{\beta+\gamma} = \frac{k_i b^2}{\beta+\gamma},$$

yielding the following Pearson correlation coefficient:

$$\rho := \frac{Cov(N,M)}{\sigma_N \sigma_M}$$

$$= \frac{\frac{k_i b^2}{\beta+\gamma}}{\sqrt{\frac{k_i b}{\beta}(1+b)\frac{k_i b}{\gamma}\left(1+\frac{b\beta}{\beta+\gamma}\right)}}$$

$$= b\sqrt{\frac{f(1-f)}{(1+b)(1+bf)}},$$

where $f$ controls the relationship between the splicing and degradation timescales.

## 4.2 Extrinsic noise model

### 4.2.1 Probability mass function

The full time-dependent copy-number probability distribution under constitutive production is
well-known and represents one of the most valuable and general results in chemical master equation
(CME) analysis [27]. In the relevant steady-state regime, the solution $\tilde{P}(n,m)$ giving the
probability of a state with a given number of nascent and mature molecules is the product of
independent Poisson distributions. Given a production rate $K$, splicing rate $\beta$, and
degradation rate $\gamma$,

$$\tilde{P}(n,m;K/\beta,K/\gamma) = \left(\frac{(K/\beta)^n e^{-K/\beta}}{n!}\right)\left(\frac{(K/\gamma)^m e^{-K/\gamma}}{m!}\right)$$

Therefore, marginalizing over the gamma-distributed production rate $K$:

$$P(n,m;\alpha,\eta) = \int_0^\infty P(n,m;x) f(x;\alpha,\eta)\,dx$$

$$= \int_0^\infty \left(\frac{(x/\beta)^n e^{-x/\beta}}{n!}\right)\left(\frac{(x/\gamma)^m e^{-x/\gamma}}{m!}\right)\frac{\eta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\eta x}\,dx$$

$$= \frac{\eta^\alpha}{\Gamma(\alpha)n!m!\beta^n\gamma^m}\int_0^\infty x^{n+m+\alpha-1}e^{-x\left(\eta+\frac{1}{\beta}+\frac{1}{\gamma}\right)}\,dx$$

$$= \frac{\Gamma(\alpha+n+m)}{\Gamma(\alpha)n!m!}\left(\frac{\eta}{\eta+\frac{1}{\beta}+\frac{1}{\gamma}}\right)^\alpha \left(\frac{1}{\beta\left(\eta+\frac{1}{\beta}+\frac{1}{\gamma}\right)}\right)^n \left(\frac{1}{\gamma\left(\eta+\frac{1}{\beta}+\frac{1}{\gamma}\right)}\right)^m$$

$$= \frac{\Gamma(\alpha+n+m)}{\Gamma(\alpha)n!m!}\left(\frac{1}{C}\right)^\alpha \left(\frac{\eta\beta^{-1}}{C}\right)^n \left(\frac{\eta\gamma^{-1}}{C}\right)^m,$$

where $C := 1 + \frac{1}{\eta}\left(\frac{1}{\beta}+\frac{1}{\gamma}\right)$. This is the
multivariate negative binomial (MVNB) distribution [28]. For the sake of completeness, we show that
the marginal distributions take the expected negative binomial form:

$$P(n;\alpha,\eta) = \int_0^\infty P(n;x) f(x;\alpha,\eta)\,dx$$

$$= \int_0^\infty \left(\frac{(x/\beta)^n e^{-x/\beta}}{n!}\right)\frac{\eta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\eta x}\,dx$$

$$= \frac{\eta^\alpha}{\Gamma(\alpha)n!\beta^n}\int_0^\infty x^{n-\alpha-1}e^{-x\left(\eta+\frac{1}{\beta}\right)}\,dx$$

$$= \frac{\Gamma(\alpha+n)}{\Gamma(\alpha)n!}\left(\frac{\eta}{\eta+\frac{1}{\beta}}\right)^\alpha \left(\frac{1}{\beta\left(\eta+\frac{1}{\beta}\right)}\right)^n$$

$$= \frac{\Gamma(\alpha+n)}{\Gamma(\alpha)n!}\left(\frac{1}{C_N}\right)^\alpha \left(\frac{\eta\beta^{-1}}{C_N}\right)^n;$$

$$P(m;\alpha,\eta) = \int_0^\infty P(m;x) f(x;\alpha,\eta)\,dx$$

$$= \int_0^\infty \left(\frac{(x/\gamma)^m e^{-x/\gamma}}{m!}\right)\frac{\eta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\eta x}\,dx$$

$$= \frac{\eta^\alpha}{\Gamma(\alpha)m!\gamma^m}\int_0^\infty x^{m-\alpha-1}e^{-x\left(\eta+\frac{1}{\gamma}\right)}\,dx$$

$$= \frac{\Gamma(\alpha+n)}{\Gamma(\alpha)m!}\left(\frac{\eta}{\eta+\frac{1}{\gamma}}\right)^\alpha \left(\frac{1}{\gamma\left(\eta+\frac{1}{\gamma}\right)}\right)^m$$

$$= \frac{\Gamma(\alpha+m)}{\Gamma(\alpha)m!}\left(\frac{1}{C_M}\right)^\alpha \left(\frac{\eta\gamma^{-1}}{C_M}\right)^m$$

where $C_N := 1 + \frac{1}{\eta\beta}$ and $C_M := 1 + \frac{1}{\eta\gamma}$. The two marginals' NB
parameters are $r = \alpha$, $p_N = \frac{1}{\eta\beta+1}$, and $p_M = \frac{1}{\eta\gamma+1}$.

We note that the Poissonian framework due to Jahnke and Huisinga [27] yields the solutions for
arbitrary graphs representing sources, sinks, and reaction channels. This is sufficient, for
example, to construct a directed acyclic graph representing alternative splicing of a
constitutively expressed gene. Adding extrinsic noise to these graphs is trivial and immediately
follows from the definitions of the corresponding Poisson rate constants.

### 4.2.2 Moments

The moments and variances of the marginals follow immediately from standard identities for the
NB distribution:

$$\mu = \frac{rp}{(1-p)}$$

$$\mu_N = \frac{\alpha \frac{1}{\eta\beta+1}}{\frac{\eta\beta}{\eta\beta+1}} = \frac{\alpha}{\eta\beta}$$

$$\mu_M = \frac{\alpha \frac{1}{\eta\gamma+1}}{\frac{\eta\gamma}{\eta\gamma+1}} = \frac{\alpha}{\eta\gamma}$$

$$\sigma^2 = \frac{\mu}{1-p}$$

$$\sigma_N^2 = \frac{\mu_N}{1-p_N} = \frac{\alpha}{\eta\beta}\frac{\eta\beta+1}{\eta\beta} = \frac{\alpha(\eta\beta+1)}{(\eta\beta)^2}$$

$$\sigma_M^2 = \frac{\mu_M}{1-p_M} = \frac{\alpha}{\eta\gamma}\frac{\eta\gamma+1}{\eta\gamma} = \frac{\alpha(\eta\gamma+1)}{(\eta\gamma)^2}$$

The moment-generating function (MGF) of the MVNB distribution is
$\phi(x,y) = \left(C - \frac{e^x}{\eta\beta} - \frac{e^y}{\eta\gamma}\right)^{-\alpha}$ [28].
Differentiating the expression with respect to $x$ and $y$ yields
$\frac{\alpha(\alpha+1)}{\eta^2\beta\gamma}\left(C-\frac{e^x}{\eta\beta}-\frac{e^y}{\eta\gamma}\right)^{-\alpha-2}$.
Evaluating at $x=y=1$ yields the cross moment $\mathbb{E}[NM] = \frac{\alpha^2+\alpha}{\eta^2\beta\gamma}$.
Therefore, the covariance is
$Cov(N,M) = \mathbb{E}[NM] - \mu_N\mu_M = \frac{\alpha^2+\alpha}{\eta^2\beta\gamma} - \frac{\alpha^2}{\eta^2\beta\gamma} = \frac{\alpha}{\eta^2\beta\gamma}$.
This result yields the following Pearson correlation coefficient:

$$\rho := \frac{Cov(N,M)}{\sigma_N\sigma_M}$$

$$= \frac{\frac{\alpha}{\eta^2\beta\gamma}}{\sqrt{\frac{\alpha(\eta\beta+1)}{(\eta\beta)^2}\frac{\alpha(\eta\gamma+1)}{(\eta\gamma)^2}}}$$

$$= \frac{1}{\sqrt{(\eta\gamma+1)(\eta\beta+1)}}$$

---

[← 3 Notation](03-3-notation.md) · [Up: contents](index.md) · [5 Discriminating between intrinsic and extrinsic noise models →](05-5-discriminating-between-intrinsic-and-extrinsic-noise-model.md)
