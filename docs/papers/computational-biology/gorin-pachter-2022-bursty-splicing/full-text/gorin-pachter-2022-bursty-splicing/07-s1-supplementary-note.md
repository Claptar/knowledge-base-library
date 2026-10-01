---
title: S1 Supplementary Note
source: https://doi.org/10.1101/2021.03.24.436847/
source_file: sources/papers/gorin-pachter-2022-bursty-splicing/gorin-pachter-2022-bursty-splicing.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2022-bursty-splicing.pdf` from [papers/gorin-pachter-2022-bursty-splicing](https://doi.org/10.1101/2021.03.24.436847/) — papers · gorin-pachter-2022-bursty-splicing, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# S1 Supplementary Note

## S1.1 Delay chemical master equations

In the current supplement, we detour from the Markovian framework to consider *delay* systems,
which have deterministic, rather than stochastic, state transitions. Certain degenerate cases – for
example, the problem of incremental, linear movement with identical transition rates – directly
bear upon the class of delay chemical master equations (DCMEs). As an example, we can model
the simple linear chain of reactions with constitutive production

$$\varnothing \xrightarrow{k} \mathcal{T}_1 \xrightarrow{\beta/n} \ldots \xrightarrow{\beta/n} \mathcal{T}_n \xrightarrow{\beta/n} \varnothing,$$

the total delay between production of $\mathcal{T}_1$ and degradation of $\mathcal{T}_n$ is Erlang-distributed, with shape
$n$ and rate $\beta$. As $n\to\infty$, the Erlang distribution reduces to a point mass at $\beta^{-1} := \tau$. This implies
that we can treat an *aggregated* species $\mathcal{T}$, produced at rate $k$ and degraded after a deterministic
delay $\tau$:

$$\varnothing \xrightarrow{k} \mathcal{T} \xRightarrow{\tau} \varnothing$$

This is precisely the "linear chain trick" introduced by MacDonald in 1978 [48]. The study of
delayed dynamical systems, such as delay differential equations, dates back to the eighteenth century [49], with cornerstone biological models by Lotka and Volterra [48, 49]. Recent work has
focused on developing exact solutions [47, 50, 51] and simulation methods [52, 53]. In particular,
studies by Lafuerza and Toral [54, 55] report full analytical solutions for constitutive systems with
isomerization, while a contemporary study by Jia and Kulkarni [56] reports lower moments for a
system with bursty mRNA production and catalysis.

Unfortunately, applying these methods to bursty systems is challenging, and all but the simplest
problems are intractable. As an illustration, we consider the constitutive two-stage system described by by Lafuerza and Toral [54], and discuss the challenges of extending it to include bursty
production. If we assume that no stochastic degradation reactions occur, the reaction equations
and generating function relations take the following form:

$$\varnothing \xrightarrow{k} \mathcal{T}_1 \xrightarrow{\beta} \mathcal{T}_2 \xRightarrow{\tau} \varnothing$$

$$\frac{\partial G}{\partial t} = k(F(x_1)-1)G + \beta(x_2-x_1)\frac{\partial G}{\partial x_1} + \beta(1-x_2)\sum_{m_1=0}^\infty G^*(x_1,x_2,\tau)m_1P(m_1,t-\tau),$$

where $G^*$ is a conditional generating function for an auxiliary *non-degrading* system, initialized at
$m_1-1$ molecules of the parent transcript $\mathcal{T}_1$. This auxiliary system has no degradation reactions,
and allows us to incorporate the non-Markovian effects of delays. Assuming constitutive production,
and using the shifted variables $u_i$ for convenience, we find:

$$\frac{\partial G}{\partial t} = ku_1G + \beta(u_2-u_1)\frac{\partial G}{\partial u_1} - \beta u_2\sum_{m_1=0}^\infty G^*(u_1,u_2,\tau)m_1P(m_1,t-\tau)$$

The final term is *not* proportional to $G$, so no convenient exponential *ansatz* is available. However,
the sum affords an alternative representation, which exploits the separability of the initial condition
and the dynamics on $[0,\tau]$:

$$G^*(u_1,u_2,\tau) = [1+U_1(\tau)]^{m_1-1}e^{\phi^*(\tau)}$$

$$\sum_{m_1=0}^\infty G^*(u_1,u_2,\tau)m_1P(m_1,t-\tau) = e^{\phi^*(\tau)}\sum_{m_1=0}^\infty [1+U_1(\tau)]^{m_1-1}m_1P(m_1,t-\tau),$$

where $\phi^*$ is the factorial-cumulant generating function of the auxiliary system, started at zero
molecules. This sum may be treated as the first derivative of the stationary $\mathcal{T}_1$ PGF, evaluated at
$1+U_1$, where $U_1$ is a function computed by solving the non-degrading system with the method of
characteristics.

We start by computing the auxiliary $U_1$ by using the method of characteristics and enforcing
$U_2(0)=u_2$ and $U_1(0)=u_1$.

$$\varnothing \xrightarrow{k} \mathcal{T}_1 \xrightarrow{\beta} \mathcal{T}_2$$

$$\frac{\partial U_2}{\partial s} = 0 \implies U_2 = u_2$$

$$\frac{\partial U_1}{\partial s} = \beta(U_2-U_1) \implies U_1 = u_2 + (u_1-u_2)e^{-\beta s}$$

Now, we compute the generating function of the subsystem:

$$\phi^*(t) = k\int_0^t U_1(s)ds = k\int_0^\tau \left[u_2+(u_1-u_2)e^{-\beta s}\right]ds$$

$$= ku_2\tau + \frac{k}{\beta}(u_1-u_2)\left[1-e^{-\beta\tau}\right]$$

We compute the derivative of the $\mathcal{T}_1$ Poisson PGF:

$$H(x_1) = e^{k(x_1-1)/\beta}$$

$$H(u_1) = e^{ku_1/\beta}$$

$$H'(U_1) = \frac{k}{\beta}e^{kU_1/\beta}$$

This construction is slightly simpler than in the original: we do not use the full time-dependent
Poisson distribution, but presuppose that the system starts with $\mathcal{T}_1$ in equilibrium. Since it approaches this distribution exponentially fast regardless of initial conditions, the error is minimal,
and the simplification eliminates the time dependence in the degradation term.

Plugging in and evaluating the non-Markovian term:

$$e^{\phi^*(\tau)}H'(U_1(\tau)) = \frac{k}{\beta}\exp(ku_2\tau+ku_1/\beta)$$

Finally, considering the full generating function expression:

$$\frac{\partial G}{\partial t} = ku_1G + \beta(u_2-u_1)\frac{\partial G}{\partial u_1} - ku_2e^{u_1\frac{k}{\beta}+u_2k\tau}$$

Lafuerza and Toral report a solution [54], though computed through an *ansatz* rather than directly
– this PDE is not quite as simple as that of the Markovian system. We restrict ourselves to the
stationary solution, which can be solved with a rather mechanical application of the integrating
factor method, or by noticing that the uncorrelated Poisson PMF solves the equation:

$$G = e^{u_1\frac{k}{\beta}+u_2k\tau}$$

$$\frac{\partial G}{\partial u_1} = \frac{k}{\beta}G$$

$$\frac{\partial G}{\partial t} = ku_1G + \beta(u_2-u_1)\frac{k}{\beta}G - ku_2G = 0$$

Of course, this result can be derived just as well without writing down anything at all – by using the
standard results for constitutive production [14], and the fact that sums of Poisson random variables
are Poisson. However, the rigorous approach can be used to treat more general systems. In particular,
we attempt to solve the delayed analog of the two-stage bursty system [10]:

$$\varnothing \xrightarrow{k} B\times \mathcal{T}_1 \xrightarrow{\beta} \mathcal{T}_2 \xRightarrow{\tau} \varnothing$$

$$\frac{\partial G}{\partial t} = k\left[\frac{1}{1-bu_1}-1\right]G + \beta(u_2-u_1)\frac{\partial G}{\partial u_1} - \beta u_2 e^{\phi^*(\tau)}H'(U_1(\tau)),$$

where the auxiliary system is now bursty.

First, we compute the factors of the non-Markovian term. The PGF derivative is found by evaluating the $\mathcal{T}_1$ marginal:

$$k\int_0^T \left[\frac{1}{1-bu_1e^{-\beta s}}-1\right]ds = \frac{k}{\beta}\ln\left(\frac{bu_1e^{-\beta T}-1}{bu_1-1}\right),$$

which coincides with the relevant result for the gamma Ornstein–Uhlenbeck SDE [21]. However,
this form is needlessly challenging to work with, and it is more straightforward to assume $T\gg 0$,
or the system starts in the equilibrium distribution of $\mathcal{T}_1$. Again, due to exponential convergence,
the error is minimal. Differentiating with respect to $x_1 = u_1+1$:

$$H'(x_1) = \frac{d}{dx_1}\left(\frac{1}{1-b(x_1-1)}\right)^{k/\beta} = \frac{kb}{\beta}\left(\frac{1}{1-b(x_1-1)}\right)^{k/\beta+1}$$

$$H'(u_1) = \frac{\mu_1H(u_1)}{1-bu_1},$$

where we define $\mu_1 := kb/\beta$ for simplicity. This yields a straightforward expression for the summation:

$$\sum_{m_1=0}^\infty [1+U_1]^{m_1-1}m_1P(m_1,t-\tau) = \frac{\mu H(U_1)}{1-bU_1}$$

We reuse $U_1$ and $U_2$ from the derivation of the constitutive system, as the downstream components
of the auxiliary systems match:

$$\varnothing \xrightarrow{k} B\times \mathcal{T}_1 \xrightarrow{\beta} \mathcal{T}_2$$

$$\phi^*(\tau) = k\int_0^\tau (M(U_1)-1)ds = k\int_0^\tau \left[\frac{1}{1-bU_1}-1\right]ds$$

$$= k\int_0^\tau \left[\frac{1}{1-bu_2-b(u_1-u_2)e^{-\beta s}}-1\right]ds$$

$$\theta := \frac{b(u_1-u_2)}{1-bu_2}$$

$$\phi^* = k\int_0^\tau \left[\frac{(1-bu_2)^{-1}}{1-\theta e^{-\beta s}}-1\right]ds$$

$$= k\tau\left(\frac{bu_2}{1-bu_2}\right) + \frac{k}{\beta(1-bu_2)}\ln\left(\frac{\theta e^{-\beta\tau}-1}{\theta-1}\right)$$

$$= k\tau\left(\frac{bu_2}{1-bu_2}\right) + \frac{k}{\beta(1-bu_2)}\ln\left(\frac{bU_1(\tau)-1}{bu_1-1}\right)$$

which follows from the derivation of the PGF of the nascent marginal.

Now, considering the full generating function relation:

$$\frac{\partial G}{\partial t} = k\left[\frac{1}{1-bu_1}\right]G + \beta(u_2-u_1)\frac{\partial G}{\partial u_1}$$

$$-\beta u_2 e^{-k\tau}\exp\left(\frac{k\tau}{1-bu_2}\right)\left(\frac{bU_1(\tau)-1}{bu_1-1}\right)^{k\beta^{-1}(1-bu_2)^{-1}}\times \frac{kb}{\beta}\left(\frac{1}{1-bU_1(\tau)}\right)^{k/\beta+1}$$

This PDE is not easily tractable by standard analytical or numerical methods. The form of the
equation is rather complicated and not amenable to analysis by characteristics. In principle, a
numerical PDE or ODE solver can be used: we may fix $u_2$ and solve for $G(u_1,u_2)$ over a mesh of
$u_1$. By repeating this for many values of $u_2$, we can compute the Fourier transform of the joint
distribution. However, this requires solvers that can integrate over the complex plane, as well
as initial conditions $G(0,u_2)$ for each $u_2$. These are the very values we seek, so even numerical
approaches require some ingenuity.

In short, the stochastically delayed systems reduce to deterministically delayed systems in some
well-studied regimes. However, in spite of the formal connection between the CME and the DCME,
the former is far simpler to analyze: the DCME is non-Markovian, and generally resistant to exact
analysis. Although much recent progress has been made, regulated transcriptional systems do not
yet have full probabilistic solutions.

---

[← References](06-references.md) · [Up: contents](index.md)
