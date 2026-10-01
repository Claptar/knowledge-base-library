---
title: 5 Discriminating between intrinsic and extrinsic noise models
source: https://doi.org/10.1101/2020.09.25.312868/
source_file: sources/papers/gorin-pachter-2020-intrinsic-extrinsic/gorin-pachter-2020-intrinsic-extrinsic.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2020-intrinsic-extrinsic.pdf` from [papers/gorin-pachter-2020-intrinsic-extrinsic](https://doi.org/10.1101/2020.09.25.312868/) — papers · gorin-pachter-2020-intrinsic-extrinsic, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 5 Discriminating between intrinsic and extrinsic noise models

Using the above computations, we can show that steady-state information about the nascent and
mature distributions is sufficient to distinguish between the two models. We start from an *a
priori* non-identifiable negative binomial nascent mRNA distribution, and demonstrate disagreement
between statistics predicted for the mature mRNA. For the purposes of illustration, we assume
data-based constraints upon $\mu_M$ and upon $\sigma_M^2$, motivated by the existence of
experimental methods for determining these quantities [1, 29]. However, we restrict our analysis to
analytical distributions to avoid the details of any particular observation or statistical
inference method.

The intrinsic and extrinsic noise models are respectively parametrized by $\{b, k_i, \beta,
\gamma\}$ and $\{\alpha, \eta, \beta, \gamma\}$. However, at steady state, the time variable is not
independently identifiable. Therefore, the absolute scaling of the rate variables
$\{k_i, \eta, \beta, \gamma\}$ is not feasible to determine. This non-identifiability is self-evident
from the functional forms of the distributions, e.g. the moment dependence on $\frac{k_i}{\beta}$
and $\frac{k_i}{\gamma}$ in the intrinsic noise model and on $\eta\beta$ and $\eta\gamma$ in the
extrinsic noise model. Therefore, we set $\beta$ to 1 with no loss of generality.

Further, the nascent marginal is governed by the two-parameter NB distribution. In the context of
model fitting, this implies that two of the parameters of the joint distribution are fully
determined by the nascent distribution, and only one degree of freedom remains to be determined by
the mature mRNA data.

Crucially, given a negative binomial distribution of nascent mRNA, with mean $\mu_N$ and variance
$\sigma_N^2$, the intrinsic and extrinsic noise models are not distinguishable. Using the intrinsic
noise model uniquely identifies $b = \frac{\sigma_N^2}{\mu_N} - 1$ and $k_i = \mu_N$. Conversely,
using the extrinsic noise model uniquely identifies $\eta = \left(\frac{\sigma_N^2}{\mu_N}-1\right)^{-1}$
and $\alpha = \mu_N\eta$.

## 5.1 Case of constrained $\gamma$ or $\mu_M$

Constraining $\gamma$ is equivalent to fixing the mature mRNA means:

$$\mu_{M,i} = \frac{k_i b}{\gamma} = \frac{\mu_N}{\gamma}$$

$$\mu_{M,e} = \frac{\alpha}{\eta\gamma} = \frac{\mu_N}{\gamma}$$

$$\frac{\mu_{M,i}}{\mu_{M,e}} = 1$$

However, the higher moments disagree. Defining the statistic $q := \frac{\sigma_N^2}{\mu_N} - 1 > 0$
and recalling that $f = \frac{1}{1+\gamma}$ for $\beta=1$:

$$\sigma_{M,i}^2 = \mu_M\left(1+\frac{b}{1+\gamma}\right) = \mu_N\left(1+\frac{q}{1+\gamma}\right) = \frac{\mu_N}{\gamma}\left(1+\gamma+q\right)\left(\frac{1}{1+\gamma}\right)$$

$$\sigma_{M,e}^2 = \mu_M \frac{\eta\gamma+1}{\eta\gamma} = \frac{\mu_N}{\gamma}\frac{q^{-1}\gamma+1}{q^{-1}\gamma}$$

$$\frac{\sigma_{M,i}^2}{\sigma_{M,e}^2} = \frac{1+\gamma+q}{1+\gamma}\frac{q^{-1}\gamma}{q^{-1}\gamma+1} = \frac{(1+\gamma)q^{-1}\gamma+\gamma}{(1+\gamma)q^{-1}\gamma+\gamma+1} < 1$$

$$\rho_i^2 = b^2\frac{f(1-f)}{(1+b)(1+bf)} = q^2\frac{f(1-f)}{(1+q)(1+qf)}$$

$$\rho_e^2 = \frac{1}{(\eta\gamma+1)(\eta\beta+1)} = \frac{1}{(q^{-1}\gamma+1)(q^{-1}+1)}$$

$$\frac{\rho_i^2}{\rho_e^2} = q^2\frac{f(1-f)(q^{-1}\gamma+1)(q^{-1}+1)}{(1+q)(1+qf)} = \frac{f(1-f)(\gamma+q)(1+q)}{(1+q)(1+qf)} = \frac{\gamma}{(1+\gamma)^2}\frac{\gamma+q}{1+\frac{q}{1+\gamma}}$$

$$= \frac{\gamma(\gamma+q)}{(1+\gamma)(1+\gamma+q)} < \frac{(1+\gamma)(1+\gamma+q)}{(1+\gamma)(1+\gamma+q)} = 1$$

Therefore, the extrinsic noise model is overdispersed with respect to the intrinsic noise model,
but its nascent and mature copy numbers are more highly correlated.

## 5.2 Case of constrained $\sigma_M^2$

Using these expressions, it is straightforward to extend the analysis to the scenario of fixing
$\sigma_M^2$:

$$\sigma_{M,i}^2 = \frac{\mu_N}{\gamma_i}\left(1+\frac{q}{1+\gamma_i}\right)$$

$$\sigma_{M,e}^2 = \frac{\mu_N}{\gamma_e}\left(1+\frac{1}{q^{-1}\gamma_e}\right) = \frac{\mu_N}{\gamma_e}\left(1+\frac{q}{\gamma_e}\right)$$

The physical solutions for $\gamma_i$ and $\gamma_e$ are given by positive roots of quadratic
equations. For the intrinsic noise model:

$$\sigma_{M,i}^2 = \frac{\mu_N}{\gamma_i}\left(1+\frac{q}{1+\gamma_i}\right)$$

$$\gamma_i(1+\gamma_i)\sigma_{M,i}^2 = \mu_N(1+\gamma_i) + \mu_N q$$

$$\sigma_{M,i}^2 \gamma_i^2 + (\sigma_{M,i}^2 - \mu_N)\gamma_i - \mu_N(q+1) = 0$$

$$\gamma_i = \frac{1}{2\sigma_{M,i}^2}\left[(\mu_N-\sigma_{M,i}^2) \pm \sqrt{(\mu_N-\sigma_{M,i}^2)^2 + 4\sigma_{M,i}^2\mu_N(q+1)}\right]$$

Since $4\sigma_{M,i}^2\mu_N(q+1) > 0$, the physical solution ($\gamma_i > 0$) is given by:

$$\gamma_i = \frac{1}{2\sigma_{M,i}^2}\left[(\mu_N-\sigma_{M,i}^2) + \sqrt{(\mu_N-\sigma_{M,i}^2)^2 + 4\sigma_{M,i}^2\mu_N(q+1)}\right]$$

Further, for the extrinsic noise model:

$$\sigma_{M,e}^2 = \frac{\mu_N}{\gamma_e}\left(1+\frac{q}{\gamma_e}\right)$$

$$\gamma_e^2\sigma_{M,e}^2 - \mu_N\gamma_e - \mu_N q = 0$$

$$\gamma_e = \frac{1}{2\sigma_{M,e}^2}\left[\mu_N \pm \sqrt{\mu_N^2 + 4\sigma_{M,e}^2\mu_N q}\right]$$

Again, since $4\sigma_{M,e}^2\mu_N q > 0$, the physical solution ($\gamma_e > 0$) is given by:

$$\gamma_e = \frac{1}{2\sigma_{M,e}^2}\left[\mu_N + \sqrt{\mu_N^2 + 4\sigma_{M,e}^2\mu_N q}\right]$$

Imposing equal variances:

$$\sigma_{M,e}^2 = \sigma_{M,i}^2 = \sigma_M^2 \implies$$

$$\gamma_i = \frac{1}{2\sigma_M^2}\left[(\mu_N-\sigma_M^2) + \sqrt{(\mu_N-\sigma_M^2)^2 + 4\sigma_M^2\mu_N(q+1)}\right]$$

$$\gamma_e = \frac{1}{2\sigma_M^2}\left[\mu_N + \sqrt{\mu_N^2 + 4\sigma_M^2\mu_N q}\right]$$

Consider $\chi := \frac{\sigma_M^2}{\mu_N}$. This definition yields:

$$\gamma_i = \frac{1}{2\chi}\left(1-\chi+\sqrt{(1-\chi)^2+4\chi(q+1)}\right)$$

$$\gamma_e = \frac{1}{2\chi}\left(1+\sqrt{1+4\chi q}\right)$$

$$\frac{\gamma_i}{\gamma_e} = \frac{1-\chi+\sqrt{(1-\chi)^2+4\chi(q+1)}}{1+\sqrt{1+4\chi q}}$$

$$= \frac{1-\chi+\sqrt{1+\chi^2-2\chi+4\chi+4\chi q}}{1+\sqrt{1+4\chi q}}$$

$$= \frac{1-\chi+\sqrt{(1+\chi)^2+4\chi q}}{1+\sqrt{1+4\chi q}}$$

We may investigate the case where this quantity is equal to 1:

$$1+\sqrt{1+4\chi q} = 1-\chi+\sqrt{(1+\chi)^2+4\chi q}$$

$$\sqrt{1+4\chi q} = \sqrt{(1+\chi)^2+4\chi q} - \chi$$

No values of $q, \chi > 0$ yield this equality. This is straightforward because even the more
general equation $\sqrt{1+C} = \sqrt{(1+x)^2+C} - x$ is nowhere satisfied for $x, C > 0$. Therefore,
the $\frac{\gamma_i}{\gamma_e}$ is never 1. From the quadratic equation solution, we know that
$\gamma_e$ and $\gamma_i$ are both constrained to be positive; therefore, $\frac{\gamma_i}{\gamma_e} >
0$. Using the test case $\chi = q = 1$, we yield $\frac{\gamma_i}{\gamma_e} = \frac{\sqrt{4+4}}{1+\sqrt{1+4}} \approx 0.87 < 1$.
Since $\gamma_e$ is nonzero and $\gamma_i(\chi,q)$ is continuous with respect to both variables,
$\frac{\gamma_i}{\gamma_e}(\chi,q)$ is continuous. Finally, we conclude that
$\frac{\gamma_i}{\gamma_e}(\chi,q)$ is always constrained to $(0,1)$ and $\gamma_e > \gamma_i$
whenever $\sigma_M^2$ is fixed. This matches the intuition of the provided by the finding that
$\sigma_{M,e}^2 > \sigma_{M,i}^2$ whenever $\gamma$ is fixed: to compensate for increased dispersion
in the extrinsic noise model, the degradation rate must be increased. It trivially follows that
$\mu_{M,i} > \mu_{M,e}$.

---

[← 4 Preliminaries](04-4-preliminaries.md) · [Up: contents](index.md) · [6 Experimental opportunities and limitations →](06-6-experimental-opportunities-and-limitations.md)
