---
title: 4 METHODOLOGICAL EXTENSIONS
source: https://doi.org/10.1101/2022.10.17.512599/
source_file: sources/papers/gorin-2022-transient-delay-cme/gorin-2022-transient-delay-cme.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-2022-transient-delay-cme.pdf` from [papers/gorin-2022-transient-delay-cme](https://doi.org/10.1101/2022.10.17.512599/) — papers · gorin-2022-transient-delay-cme, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 METHODOLOGICAL EXTENSIONS

In the current section, we draw useful connections to theory we previously reported in (Gorin and Pachter, 2021), contextualize the work with respect to standard tools of DCME analysis, and discuss potential extensions.

## 4.1 Generating function identifiability

Consider a system with $n$ species, described by a generating function $G(\mathbf{u})$. Some of these species may not be mutually identifiable. Suppose there are $n$ identifiable species, where each species $i \in \{1, ..., n\}$ may be assigned to each category $\iota$ with probability $p_{i,\iota}$ for each molecule. If this assignment process is independent, the process induces a collection of $n$ generating functions $\mathbf{G}^s(\mathbf{u})$, such that each component is the PGF of a categorical distribution (i.e., a multinomial distribution with a single trial):

$$G_i^s(\mathbf{u}) = \sum_{\iota=0}^n (u_\iota + 1)p_{i,\iota}, \tag{31}$$

where $p_{i,0}$ is defined as $1 - \sum_\iota p_{i,\iota}$, the probability of assigning species $i$ to none of the observable species, and losing it. Evidently,

$$G_i^s(\mathbf{u}) - 1 = \sum_{\iota=0}^n u_\iota p_{i,\iota}. \tag{32}$$

From standard properties of generating functions, the distribution resulting from "filtering" $G$ through $\mathbf{G}^s$ is a function composition:

$$G(\mathbf{u}) = G(\mathbf{G}^s(\mathbf{u}) - \mathbf{1}), \tag{33}$$

where $\mathbf{1}$ denotes the length-$n$ vector of ones.

## 4.2 Erlang-distributed delays

Consider the case of a system with bursty transcription, Markovian degradation, and Erlang-distributed waiting time for splicing, with shape $q$ and mean waiting time $\tau$. First, set up a system with $q+1$ species:

$$\varnothing \xrightarrow{\alpha} B \times \mathcal{T}_1 \xrightarrow{q/\tau} ... \mathcal{T}_q \xrightarrow{q/\tau} \mathcal{T}_{q+1} \xrightarrow{\gamma} \varnothing \tag{34}$$

The characteristic corresponding to $\mathcal{T}_{q+1}$ is simply $u_{q+1}e^{-\gamma s}$. By somewhat tedious computation, amounting to repeatedly solving ordinary differential equations of the form $\frac{dU_i}{dt} = \frac{q}{\tau}(U_{i+1} - U_i)$, we find that the characteristic corresponding to $\mathcal{T}_1$ takes the following form:

$$U_1 = u_{q+1}e^{-\gamma s} \times \left(\frac{\lambda}{\lambda - \gamma}\right)^q + e^{-\lambda s}\sum_{i=0}^{q-1}\frac{(u_{i+1}+\lambda s)^q}{i!} - u_{q+1}e^{-\lambda s}\frac{(\lambda)^q}{(\lambda-\gamma)^q}\sum_{i=0}^{q-1}\frac{s^i(\lambda-\gamma)^i}{i!}, \tag{35}$$

where $\lambda$ is defined as $q/\tau$.

To aggregate $\mathcal{T}_1, ..., \mathcal{T}_q$ into a single species $X_1$, and represent $\mathcal{T}_{q+1}$ as the downstream species $X_2$, we evaluate the arguments at $u_1 = ... = u_q = u_1$ and $u_{q+1} = u_2$. This yields:

$$U_1 = u_2 e^{-\gamma s} \times \left(\frac{\lambda}{\lambda-\gamma}\right)^q + u_1 e^{-\lambda s}\frac{\Gamma(q,\lambda s)}{\Gamma(q)} - u_2 e^{-\gamma s}\frac{\lambda^q}{(\lambda-\gamma)^q}\frac{\Gamma(q,(\lambda-\gamma)s)}{\Gamma(q)}. \tag{36}$$

To evaluate the PGF, we plug $U_1$ into the burst distribution MGF and integrate.

## 4.3 Linear chain trick

The same approach can be used to arrive at the solution for deterministically delayed systems, commonly known as the "linear chain trick." Taking the limit as $q \to \infty$ and exploiting the properties of special functions:

$$\lim_{q\to\infty} U_1 = u_2 e^{-\gamma s}e^{\gamma\tau} + u_1\mathbb{I}(s<\tau) - \lim_{q\to\infty} u_2 e^{-\gamma s}e^{\gamma\tau}\frac{\Gamma(q,(q/\tau - \gamma)s)}{\Gamma(q)}$$
$$= u_2 e^{-\gamma(s-\tau)} + u_1\mathbb{I}(s<\tau) - u_2 e^{-\gamma(s-\tau)}\mathbb{I}(s<\tau)$$
$$= u_1\mathbb{I}(s<\tau) + u_2 e^{-\gamma(s-\tau)}\mathbb{I}(s>\tau). \tag{37}$$

To obtain the PGF, we plug $\lim_{q\to\infty} U_1$ into the burst distribution MGF and integrate, eliding the functional analysis justification for interchanging the limit and the integral. This reproduces the results in Section 3.2.3, albeit with considerably more effort.

## 4.4 General waiting time distributions

The same approach may be used to evaluate systems with more generic waiting time distributions. For example, the characteristic appropriate for a molecule that remains in the system for time $\tau$, then exhibits Markovian efflux is immediately implied by the results of the previous section:

$$U = u\left[\mathbb{I}(s<\tau) + e^{-\gamma(s-\tau)}\mathbb{I}(s>\tau)\right], \tag{38}$$

obtained by evaluating the previous characteristic $U_1$ at $u_1 = u_2 = u$. This holds for any combination of Markovian and deterministic delays.

Throughout the current section, we have considered delays only in downstream molecular processing. However, studies have indicated that non-Markovian refractory periods can occur in promoter state transitions (Harper et al., 2011). If the refractory period can be effectively described by a series of Markovian processes (e.g., if the waiting time is Erlang), such systems can be solved by defining "internal" inactive states and adding their $P_j$, obtained through Equation 16, in the spirit of (Herbach, 2019). Stinchcombe et al. treated the case of arbitrary switching time distributions (Stinchcombe et al., 2012); however, this approach requires a degree of ingenuity and is fairly challenging to formalize in the language of generating functions.

The case of more general waiting times was explored in considerable detail by Zhang and Zhou (Zhang and Zhou, 2019), albeit with somewhat more emphasis on theoretical foundations and implications for noise buffering than here. Essentially, arbitrary waiting time distributions may be encoded by properly exploiting their statistical structure; for example, it is immediately evident that the characteristic in Equation 38 is simply the survival function (complementary cumulative distribution function) of each molecule, evaluated at its birth. In the same vein, the $U_2^D$ terms in Equations 25 and 28 are the survival functions of the degenerate and exponential distributions, whereas the $u_2$ term of the characteristic in Equation 24 is the survival function of the two-parameter hypoexponential distribution.

It appears that more general waiting time distributions can be incorporated in the characteristic framework by appropriately manipulating their survival functions. We forgo detailed discussion of this extension, as it is less suitable to automation and tends to lead to intractable integrals. Further, Markovian and deterministic delays are relatively easy to motivate from first principles by appealing to memorylessness or perfect molecular memory, respectively (either maximum or zero entropy in the language of statistical physics (Pressé et al., 2013)). On the other hand, "intermediate" non-Markovian cases require a specific hypothesis to instantiate a functional form for the waiting time distribution.

The simulation algorithm outlined in Section 3.1.1 generalizes to arbitrary waiting time distributions, and may be used to investigate the impact of different assumptions even when analytical solutions are unavailable. Further, the tools outlined here can be used to explore some pathological cases, such as the loss of stationarity due to particularly ill-behaved waiting time distributions. For example, if the RNA production process is constitutive with unity transcription rate and the waiting time distribution is standard half-Cauchy, the characteristic and log-PGF take the following form:

$$U = u\left[1 - \frac{2}{\pi}\tan^{-1}s\right]$$
$$\phi = \frac{u}{\pi}\left[\pi t - 2t\tan^{-1}(t) + \ln(1+t^2)\right], \tag{39}$$

where $\phi$ is immediately recognizable as the log-PGF of a Poisson distribution, albeit one that does not possess a limit as $t \to \infty$. This implies that the $M/G/\infty$ queue with half-Cauchy service times has no stationary distribution. In contrast, if the waiting time distribution is standard Pareto, with support on $[1,\infty)$, we find:

$$U = us^{-\alpha}$$
$$\phi = \frac{u}{\alpha-1}\left(1 - t^{1-\alpha}\right)$$
$$\text{or } \phi = u\ln t \text{ when } \alpha = 1. \tag{40}$$

This distribution possesses a Poisson steady state with mean $(\alpha-1)^{-1}$ whenever $\alpha > 1$. This implies that the $M/G/\infty$ queue with Pareto service times has a stationary distribution, but only if the service time distribution is endowed with a mean. Approaches such as this may be of use in identifying classes of non-Markovian processes admissible under particular axioms about biology, e.g., the existence of all Laplace transforms for the waiting time distributions (Zhang and Zhou, 2019).

---

[← 3 RESULTS](04-3-results.md) · [Up: contents](index.md) · [5 DISCUSSION →](06-5-discussion.md)
