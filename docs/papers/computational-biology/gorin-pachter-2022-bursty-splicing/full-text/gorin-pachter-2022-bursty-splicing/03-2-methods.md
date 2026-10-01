---
title: 2 Methods
source: https://doi.org/10.1101/2021.03.24.436847/
source_file: sources/papers/gorin-pachter-2022-bursty-splicing/gorin-pachter-2022-bursty-splicing.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-pachter-2022-bursty-splicing.pdf` from [papers/gorin-pachter-2022-bursty-splicing](https://doi.org/10.1101/2021.03.24.436847/) — papers · gorin-pachter-2022-bursty-splicing, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 Methods

## 2.1 Path graph splicing

**Figure 1:** Graph representation of the generic path graph model. The source transcript $\mathcal{T}_1$ is synthesized at the gene locus in random geometrically distributed bursts (according to a distribution $B$ with burst frequency $k$). Each molecule proceeds to isomerize in a chain of splicing reactions governed by successive rates $\beta_1, \beta_2, \ldots, \beta_{n-1}$, until reaching the form $\mathcal{T}_n$, which is ultimately degraded at rate $\gamma$.

(Graph: $\varnothing \xrightarrow{k} B \times \mathcal{T}_1 \xrightarrow{\beta_1} \mathcal{T}_2 \xrightarrow{\beta_2} \cdots \xrightarrow{\beta_{n-2}} \mathcal{T}_{n-1} \xrightarrow{\beta_{n-1}} \mathcal{T}_n \xrightarrow{\gamma}$)

Consider the system consisting of a bursting gene coupled to a $n$-step birth-death process, characterized
by the path graph in Figure 1 where $B \sim \mathrm{Geom}(b)$, and all reactions occur after exponentiallydistributed waiting times. The bursts occur with rate $k$, the conversion of adjacent transcripts $\mathcal{T}_i$
to $\mathcal{T}_{i+1}$ occurs with rate $\beta_i$, and the degradation of $\mathcal{T}_n$ occurs with rate $\gamma := \beta_n$. We assume the
rates of conversion and degradation are all distinct. The amount of species $\mathcal{T}_i$ can be described by
the non-negative discrete random variable $m_i$. We assume no molecules are present at $t=0$.

### 2.1.1 Discrete formulation and algorithm

We would like to compute the probability mass function (PMF) of the count distribution, denoted by
$P(m_1,\ldots,m_n,t)$; this corresponds to the probability of observing $m_1$ molecules of $\mathcal{T}_1$, $m_2$ molecules
of $\mathcal{T}_2$, etc., at time $t$. Following a previous derivation [10], this problem can be reframed in terms of
a partial differential equation involving the probability generating function (PGF) $G(x_1,\ldots,x_n,t)$:

$$G := \sum_{m_1,\ldots,m_n} x_1^{m_1}\ldots x_n^{m_n} P(m_1,\ldots,m_n,t)$$

$$\frac{\partial G}{\partial t} = k(F(x_1)-1)G + \sum_{i=1}^{n-1}\beta_i(x_{i+1}-x_i)\frac{\partial G}{\partial x_i} + \gamma(1-x_n)\frac{\partial G}{\partial x_n},$$

where $F$ is the PGF of the burst distribution. Applying the transformations $u_i := x_i - 1$ and
$\phi := \ln G$ yields the equation:

$$\frac{\partial \phi}{\partial t} = k(M(u_1)-1) + \sum_{i=1}^{n-1}\beta_i(u_{i+1}-u_i)\frac{\partial \phi}{\partial u_i} - \gamma u_n \frac{\partial \phi}{\partial u_n},$$

where $M(u) := F(1+u)$. This equation can be solved using the method of characteristics, with
formal solution $\phi = \int_0^t [M(U_1(s))-1]ds$. The characteristics $U_i$, $i1$ (i.e., molecular species with several potential products), the associated ODE has a functional
form identical to that of a path graph. Therefore, the solutions are analogous.

As an illustration, consider the simplest tree graph, shown in Figure 2a, where the splicing reactions
occur at rates $\alpha_1$ and $\alpha_2$ and degradation reactions occur at rates $\beta_1$ and $\beta_2$. Physically, this graph
can be interpreted as a single source mRNA being directly and stochastically converted to one of
two terminal isoforms by removal of intron 1 or intron 2. Clearly, $U_i = u_i e^{-\beta_i s}$ for $i \in \{1,2\}$.

The ODE governing the source species is $\frac{dU_0}{ds} = \alpha_1(U_1-U_0) + \alpha_2(U_2-U_0) = \alpha_1 U_1 + \alpha_2 U_2 -
(\alpha_1+\alpha_2)U_0$. The solution is $U_0 = \frac{\alpha_1}{\alpha_1+\alpha_2-\beta_1}u_1 e^{-\beta_1 s} + \frac{\alpha_2}{\alpha_1+\alpha_2-\beta_2}u_2 e^{-\beta_2 s} + K e^{-(\alpha_1+\alpha_2)s}$, with $K =
u_0 - \frac{\alpha_1}{\alpha_1+\alpha_2-\beta_1}u_1 - \frac{\alpha_2}{\alpha_1+\alpha_2-\beta_2}u_2$. Finally, the expression for $U_0$ can be directly plugged into the desired
burst distribution generating function.

### 2.2.2 Example: two-intron splicing with non-deterministic order

Consider the same tree graph as in the example above, and suppose $\mathcal{T}_1$ and $\mathcal{T}_2$ are converted
to product $\mathcal{T}_{12}$ at rates $\beta_1$ and $\beta_2$, as shown in Figure 2b. Afterward, $\mathcal{T}_{12}$ is degraded at rate
$\gamma$. Physically, this graph can be interpreted as a single source mRNA being converted to one of
two intermediate isoforms by the removal of one of two introns, then to a single terminal isoform
by the removal of the other intron. Clearly, $U_{12} = u_{12}e^{-\gamma s}$. Setting $f_i := \frac{\beta_i}{\beta_i-\gamma}$, we find $U_i =
(u_i - f_i u_{12})e^{-\beta_i s} + f_i u_{12}e^{-\gamma s}$. Finally, the dynamics of the source molecule $\mathcal{T}_0$ are governed by the
following ODE:

$$\frac{dU_0}{ds} = \alpha_1(u_1-f_1u_{12})e^{-\beta_1 s} + \alpha_2(u_2-f_2u_{12})e^{-\beta_2 s} + (\alpha_1 f_1+\alpha_2 f_2)u_{12}e^{-\gamma s} - (\alpha_1+\alpha_2)U_0$$

Yet again, the functional form affords a straightforward analytical solution:

$$U_0 = Ke^{-cs} + \frac{C_1}{c-\beta_1}e^{-\beta_1 s} + \frac{C_2}{c-\beta_2}e^{-\beta_2 s} + \frac{C_3}{c-\gamma}e^{-\gamma s},$$

where $c := \alpha_1+\alpha_2$, $C_1 := \alpha_1(u_1-f_1u_{12})$, $C_2 := \alpha_2(u_2-f_2u_{12})$, and $C_3 := \alpha_1 f_1+\alpha_2 f_2$. From the
initial condition $U_0(s=0) = u_0$, we yield $K = u_0 - \frac{C_1}{c-\beta_1} - \frac{C_2}{c-\beta_2} - \frac{C_3}{c-\gamma}$. The details of the ODE
solution are described in Section 5 and the computation procedure is demonstrated in Figure 3.

### 2.2.3 Algorithm

It is facile to extend this procedure to an arbitrary directed acyclic graph with a unique root. The
reaction system is fully characterized by two arrays, the stoichiometric matrix $S$ and the
rate vector $r$ used in the stochastic simulation algorithm [13]. Thus, for example, the path graph

**Figure 3:** Illustration of the solution algorithm. The differential equation structure requires the
backward propagation of downstream species' solutions, weighted by ratios of rates.

1. Initialize product coefficient: $A_{12} = u_{12}$
2. Compute intermediate weights: $A_i \leftarrow u_i - \frac{\beta_i}{\beta_i-\gamma}u_{12}$, $i \in \{1,2\}$
3. Update weights and compute $U_0$: $A_{12} \leftarrow A_{12}\sum_{i\in\{1,2\}}\frac{\alpha_i}{\alpha_1+\alpha_2-\gamma}\frac{\beta_i}{\beta_i-\gamma}$; $A_0 \leftarrow u_0 - \sum_{i\in\{1,2\}}\frac{\alpha_i}{\alpha_1+\alpha_2-\beta_i}A_i - A_{12}$

can be represented by the full rate vector $[k,\beta_1,\ldots,\beta_{n-1},\gamma]$ and the following stoichiometric matrix:

$$\begin{bmatrix}
B & 0 & 0 & \ldots & 0 & 0 \\
-1 & 1 & 0 & \ldots & 0 & 0 \\
0 & -1 & 1 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & -1 & 1 \\
0 & 0 & 0 & \ldots & 0 & -1
\end{bmatrix}$$

A well-defined system has $n$ species and $q+1$ reactions. We assume unbounded accumulation
does not occur and the graph is connected, so each species has influx and efflux reaction pathways,
implying $q \ge n$. Further, we suppose that each species is associated with at most one degradation
reaction; if several channels are available, they can be added by the superposition property of
a Poisson process. Finally, we assume that all isomerization and degradation rates are distinct.
Since the underlying graph is acyclic, there exists at least one terminal species with a single efflux
reaction. Thus, consider a single production reaction with rate $k$ coupled to a set of isomerization
reactions with rates $c_{ji}$ and degradation reactions with rates $c_{j0}$.

The downstream dynamics are determined by $U_1$, an exponential sum with $n$ terms. In this generic
case, *lumped* rate exponents $r_i$ must be computed as the net efflux rate from each molecule. A
simple implementation of the routine is outlined below:

```
r_i ← Σ_j c_ij  ∀ i                                               ▷ Compute all exponents
A_ij ← 0  ∀ i,j ∈ [1,n]                                           ▷ Initialize coefficient array
R_D ← {k | Σ_i S_ki = -1}                                         ▷ Identify reaction channels that correspond to degradation
D ← {i | S_ki = -1 for k ∈ R_D}                                   ▷ Identify degraded species
T ← {j ∈ D | ∄(S_kj = -1 ∩ S_ki = 1)}                              ▷ Identify terminal species
R_T ← {k | S_ki = -1 for i ∈ T}                                   ▷ Identify terminal reactions
A_ii ← u_i  ∀ i ∈ T                                                ▷ Assign terminal degradation coefficients
C ← {∅}                                                           ▷ Initialize set of computed species

while |C| < n do                                                  ▷ Iterate over all species that have not yet been computed
    for j ∉ C do
        R_I = {k | (S_kj = -1 ∩ S_ki = 1)}                        ▷ Identify isomerization reactions originating at j
        P = {i | (S_ki = 1 for k ∈ R_I)}                          ▷ Identify corresponding isomerization products
        if P ⊂ C then                                             ▷ If all products have been computed
            for i ∈ P do                                          ▷ For each isomerization product
                A_jk ← A_jk + A_ik × c_ji/(r_j - r_i)              ▷ Propagate results from downstream solutions
            end for
            A_jj ← u_j − Σ_k A_jk                                 ▷ Apply initial condition, compute coefficient for e^{-r_j s}
            C ← C ∪ j                                              ▷ Adjust set of computed species
        end if
    end for
end while
```

The terminal exponential sum is given by $U_1 = \sum_{i=1}^n A_{1i}e^{-r_i s}$. As before, the full time-dependent
solution for any burst distribution with a well-defined moment-generating function is computable by
quadrature. The case of the geometric burst distribution yet again corresponds to $\phi(t;u_1,\ldots,u_n) =
k\int_0^t \frac{bU_1(s)}{1-bU_1(s)}ds$.

## 2.3 Continuous formulation

We have defined a series of discrete joint distributions induced by a graph governing splicing
and degradation. However, we can equivalently recast the problem in terms of the stochastic
differential equations (SDEs) governing the distributions' Poisson intensities $\Lambda_i$. Specifically, the
following identity can be used to relate a set of stochastic processes $\Lambda_1,\ldots,\Lambda_n$ with joint distribution
$F_{\Lambda_1,\ldots,\Lambda_n}$ to the solution of the CME [9, 14–16]:

$$P(m_1,\ldots,m_n,t) = \int \prod_{i=1}^n \frac{e^{-\Lambda_i}\Lambda_i^{m_i}}{m_i!} dF_{\Lambda_1,\ldots,\Lambda_n}$$

As an illustration, we can consider the intensity of an $n$-step isomerization process driven by a
finite-activity compound Poisson Lévy subordinator $L_t$:

$$d\Lambda_1 = -\beta_1\Lambda_1 dt + dL_t$$
$$d\Lambda_2 = -\beta_2\Lambda_2 dt + \beta_1\Lambda_1 dt$$
$$\ldots$$
$$d\Lambda_n = -\gamma\Lambda_n dt + \beta_{n-1}\Lambda_n dt,$$

This formulation has an intimate connection with the theory of moving average processes, which
can be immediately seen by applying variation of parameters to the Poisson representation:

$$\Lambda_i^p = Ce^{-\beta_i t}$$
$$\Lambda_i = C_t e^{-\beta_i t}$$
$$d\Lambda_i = -\beta_i C_t e^{-\beta_i t}dt + e^{-\beta_i t}dC_t$$
$$= -\beta_i C_t e^{-\beta_i t}dt + \beta_i \Lambda_{i-1}dt$$
$$C_t = \int_0^t \beta_i \Lambda_{i-1}(s)e^{\beta_i s}ds$$
$$\Lambda_i(t) = e^{-\beta_i t}C_t = \int_0^t \beta_i\Lambda_{i-1}(s)e^{-\beta_i(t-s)}ds$$

By convention, $\beta_n := \gamma$ and $\Lambda_0 ds := dL_s$, the underlying driving subordinator.

Thus, each $\Lambda_i$ is the exponentially-weighted moving average of $\Lambda_{i-1}$; $\Lambda_1$ is the moving average of
the Poisson shot noise introduced by the compound Poisson subordinator. Although ample literature
exists on the topic of moving average processes [17], it generally considers the problem of inference
and prediction from discrete-time observations. Furthermore, discussions in the context of the
chemical systems only tend to consider the first-order moving average of shot noise [9].

This formulation implies that any $n$-step isomerization process is identical to an $(n-i)$-step isomerization process driven by an order $i$ iterated moving average process. This identity affords
the route for the analytical computation of hybrid continuous-discrete system solutions merely by
marginalizing the first $i$ species.

The Poisson representation enables the simultaneous discussion of the properties of $F_{m_1,\ldots,m_n}$,
the stationary distribution of the continuous-time Markov chain, and $F_{\Lambda_1,\ldots,\Lambda_n}$, the stationary
distribution of the underlying series of stochastic differential equations. In fact, from standard
properties of Poisson mixtures [18], the PGF $G(x_1,\ldots,x_n)$ of the former evaluated at $u_i = x_i-1$
yields the moment-generating function (MGF) of the latter.

This connection also allows the evaluation of the solution for a broad class of compound Poisson
driving processes. Specifically, $M(u) = \frac{1}{1-bu}$ is the MGF associated with exponentially distributed
jumps. In the discrete domain, this translates to the geometric burst distribution. However, the
downstream dynamics, represented by $U_1(s)$, are independent of the burst distribution. Therefore,
the procedure affords computable solutions for any finite-activity pure-jump Lévy driving process.
Extensions to generic directed acyclic graphs are entirely analogous. These solutions, identical
to the CME case, can be used to exactly solve arbitrary DAGs representing *continuous*-valued
molecular concentrations. This representation is conventional for high-abundance species [19].

This formulation occasionally enables the confirmation of CME results using standard properties
of SDEs. For example, when $L_t$ is a compound Poisson subordinator with exponential jumps,
$\Lambda_1$ is the gamma Ornstein–Uhlenbeck process [20–23]. Inspired by a highly general result for
constitutive transcription [14], which states that Poisson distributions always remain Poisson for a
birth-death process, we may reasonably ask whether equivalent results are available for bursty
processes. This intuition turns out incorrect, and straightforward to disconfirm using SDE results.
The distribution of the gamma Ornstein–Uhlenbeck process is not gamma for any finite $t \in (0,\infty)$
– although it does approach a gamma law exponentially fast [21]; therefore, the corresponding
Poisson mixture is *not* simply a time-varying negative binomial.

## 2.4 Distribution properties

Using the algorithms above, we can compute the generating functions corresponding to the stochastic
processes of interest. However, it is not yet clear that these generating functions are everywhere
well-defined. For example, certain physiologically plausible noise models do not have all
moments [24]; their generating functions fail to converge in certain regimes. By analyzing the
functional form of the downstream process and assuming geometric-distributed bursts, we demonstrate
this class of processes is guaranteed to yield convergent generating functions and finite
moments.

### 2.4.1 Positivity of the exponential sum

First, we demonstrate that the downstream processes yield a strictly positive functional form of
time dependence. Noting that the marginal of species $i$ yields the functional form $U_1(u_i;s) =
u_i\sum_{j=1}^n a_j e^{-r_j s} := u_i\psi_i(s)$, this condition translates to $\psi_i(s) > 0$ for all $s>0$.

Consider $F(x) = x$, corresponding to constitutive production of the source species (i.e. a Poisson
birth process), with no molecules present at $t=0$. Focusing on the marginal of species $i$, this
assumption yields $\phi(u_i;s) = k\int_0^t U_1(u_i;s)ds = k\int_0^t u_n\psi_n(s)ds$. Evaluating $e^\phi$ at $x_i=0$, i.e. $u_i =
-1$, marginalizes over all $j\neq i$ and yields the probability of observing zero counts of species
$i$: $G(u_i;t) = P(m_i=0,t) = P_0(t) = \exp(-k\int_0^t \psi_i(s)ds)$. The corresponding time derivative is
$\frac{dP_0}{dt} = -k\psi_n(t)\exp(-k\int_0^t \psi_i(s)ds)$. Simultaneously, we know that $P_0(t) = e^{-\lambda_i(t)}$, the solution for species
$i$ [14]. Clearly, $\frac{dP_0}{dt} = -P_0(t)\frac{d\lambda_i(t)}{dt}$. The reaction
rate $\frac{d\lambda_i(t)}{dt} > 0$ at $t=0$ under given initial conditions. Furthermore, $\frac{d\lambda_i(t)}{dt}$ is strictly positive.
This follows from the reaction rate equations. By the continuous formulation, $\lambda_i$ is a weighted
moving average of some set of processes $\{\lambda_k\}$. $\lambda_1$ is a strictly increasing function governed by
$\frac{k}{r_1}(1-e^{-r_1 s})$. The property of being strictly increasing is retained under moving average and
rescaling. Therefore, each successive moving average must be strictly increasing.

Finally, $P_0 \in (0,1) > 0$, because the solution for $m_i$ is given by a Poisson distribution, which has
support on all of $\mathbb{N}_0$. Therefore, $\frac{dP_0}{dt}$ is strictly negative. As the exponential term and $k$ are positive,
this implies $\psi_i(s)$ is strictly positive for all $s>0$.

### 2.4.2 Existence of generating functions and moments

Next, we show that $G(u_i;t)$, the generating function of the $i$th marginal, is finite for the geometric
burst system. This follows from the construction of the original PGF: the marginal PGF is
guaranteed to be finite if $1-bu_i\psi_i$ is never zero. But for the relevant domain $\Re(u_n) \le 0$, on
the shifted complex unit circle, $\Re(1-bu_i\psi_i) \ge 1$, except at the degenerate initial case. The existence
of the marginal moments of $m_i$ is implied by the existence of the generating function. The existence
of all cross moments follows from the Cauchy-Schwarz inequality. Per standard properties, this
existence property holds for both $m_i$ and $\Lambda_i$.

The tails of the stationary discrete marginals decay no slower than the geometric distribution. This
follows immediately from the lower bound on $\Re(1-bu_i\psi_i)$, which in turn gives an upper bound on
$x_i$ [10]. Equivalently, this follows from the existence of all moments [24]. An analytical radius of
convergence has been given previously for $n=2$ [10], but numerical optimization is necessary to
establish rates of tail decay for $n>2$.

### 2.4.3 Statistical properties

**All marginals are infinitely divisible.** This follows from the functional form of the PGF: the
random variable corresponding to any marginal distribution can be written as a sum of $q$ random
variables with burst frequency $k/q$.

**Only the first marginal is self-decomposable.** This follows from the condition that a random
variable has a self-decomposable (sd) law if and only if it offers a representation of the form
$Y = \int_0^\infty e^{-t}dX_t$, with Lévy $X_t$ [25]. However, only $\Lambda_0$ is Lévy. All downstream intensity processes
have nontrivial, almost-everywhere $C^\infty$ trajectories, which implies they cannot be represented by
a Lévy triplet: the only permitted continuous Lévy processes are linear combinations of the (nondifferentiable) Brownian motion $W_t$ and the trivial process $t$. Therefore, $\Lambda_i$ is sd for $i=1$ and
non-sd for all $i>1$.

**All stationary marginals are unimodal.** Multimodality in the distribution of the moving average
over time is contingent on time-inhomogeneity in the trajectory process. However, the
underlying driving process is defined to be time-homogeneous, with uniformly distributed jump
times; therefore, each downstream process has a unimodal distribution over time. By ergodicity,
this distribution is equivalent to the ensemble distribution. Therefore, all marginals of downstream
species are unimodal.

### 2.4.4 Moments

The moments of the marginals can be computed directly from the derivatives of the marginal MGF
$e^{\phi(u_i)}$ at $u_i=0$:

$$\frac{de^\phi}{du_i} = e^\phi\frac{d\phi}{du_i} = e^\phi\frac{d}{du_i}k\int_0^\infty \frac{bu_i\psi_i(s)}{1-bu_i\psi_i(s)}ds$$

$$= kb\int_0^\infty \psi_i(s)ds = kb\int_0^\infty \sum_{i=1}^n a_i e^{-r_i s}ds = kb\sum_{i=1}^n \frac{a_i}{r_i}.$$

For the path graph system, the CME immediately yields $\mu_i = \frac{kb}{r_i}$. Considering the previously discussed
constitutive solution $\phi^0(u_i) = ku_i\int_0^\infty \psi_i(s)ds$, we yield the identity $\int_0^\infty \psi_i(s)ds = \sum_{i=1}^n \frac{a_i}{r_i}$,
which is equal to $\frac{1}{r_i}$ for the path graph system. Per the standard properties of mixed Poisson
distributions [2], the value of $\mu_i$ is identical for the underlying continuous process and the derived
discrete process.

The stationary second moments can be found analogously:

$$\frac{d^2e^\phi}{du_i^2} = e^\phi\frac{d^2\phi}{du_i^2} + e^\phi\left(\frac{d\phi}{du_i}\right)^2$$

$$= 2kb^2\int_0^\infty \psi_i^2(s)ds + \left(\frac{kb}{r_i}\right)^2$$

$$\psi_n^2(s) = \sum_{j,k=1}^n a_j a_k e^{-(r_j+r_k)s} = \sum_{j=1}^n a_j^2 e^{-2r_j s} + \sum_{j,k=1,\ j\neq k}^n a_j a_k e^{-(r_j+r_k)s}$$

$$\frac{d^2e^\phi}{du_i^2} = 2kb^2\sum_{j,k=1}^n \frac{a_j a_k}{r_j+r_k} + \mu_i^2 = \mathbb{E}[\Lambda_i^2]$$

$$\mathbb{V}[\Lambda_i] = 2kb^2\sum_{j,k=1}^n \frac{a_j a_k}{r_j+r_k},$$

which is straightforward to compute, but does not appear to have an easily amenable analytical
form beyond the first few cases. Naturally, the standard properties of Poisson mixtures [26] allow
conversion to the discrete domain, with $\mathbb{V}[m_i] = \mathbb{V}[\Lambda_i]+\mu_i$.

The covariances can be computed directly from the derivatives of the MGF $e^{\phi(u_l,u_i)}$, i.e., the
marginalized MGF for $u_q=0$ for all $q\neq l,i$. The particular functional form of $\phi(u_l,u_i)$ is given by
$k\int_0^\infty \frac{bU_1(u_l,u_i;s)}{1-bU_1(u_l,u_i;s)}ds$. By construction, $U_1(u_l,u_i;s) = u_l\psi_l(s)+u_i\psi_i(s)$, where each $\psi$ is the exponential
sum corresponding to the marginal of the species in question. This yields:

$$\frac{d^2e^\phi}{du_l du_i} = \frac{d}{du_l}e^\phi k\int_0^\infty \frac{b\psi_i ds}{(1-bu_l\psi_l-bu_i\psi_i)^2}$$

$$= e^\phi k^2\int_0^\infty \frac{b\psi_l ds}{(1-bu_l\psi_l-bu_i\psi_i)^2}\int_0^\infty \frac{b\psi_i ds}{(1-bu_l\psi_l-bu_i\psi_i)^2}$$

$$+ 2e^\phi k\int_0^\infty \frac{b^2\psi_l\psi_i ds}{(1-bu_l\psi_l-bu_i\psi_i)^3}$$

$$\mathbb{E}[\Lambda_l\Lambda_i] = k^2b^2\int_0^\infty \psi_l ds\int_0^\infty \psi_i ds + 2kb^2\int_0^\infty \psi_l\psi_i ds$$

$$= \mu_l\mu_i + 2kb^2\int_0^\infty \psi_l\psi_i ds = \mathrm{Cov}(\Lambda_l,\Lambda_i) + \mu_l\mu_i,$$

which implies that

$$\mathrm{Cov}(\Lambda_l,\Lambda_i) = 2kb^2\int_0^\infty \psi_l\psi_i ds.$$

As above,

$$\psi_l(s)\psi_i(s) = \sum_{j,k=1}^n a_j c_k e^{-(r_j+r_k)s}$$

$$\int_0^\infty \psi_l(s)\psi_i(s)ds = \sum_{j,k=1}^n \frac{a_j c_k}{r_j+r_k}$$

$$\mathrm{Cov}(\Lambda_l,\Lambda_i) = 2kb^2\sum_{j,k=1}^n \frac{a_j c_k}{r_j+r_k} = 2kb^2\sum_{j,k=1}^n \frac{a_j c_k}{r_j+r_k},$$

where $a_j$ are the weights associated with $\psi_l$ and $c_k$ are the weights associated with $\psi_i$. This form
of the summation is very general; for example, in case of the path graph system with $l>i$, it
can be equivalently represented as $2kb^2\sum_{j=1}^l \sum_{k=1}^i \frac{a_j c_k}{r_j+r_k}$. From standard identities, the covariance
of a mixed bivariate Poisson distribution with no intrinsic covariance forcing is identical to the
covariance of the mixing distribution [26]. Therefore, this result holds for both the CME and the
underlying SDE.

The Pearson correlation coefficient follows immediately from the result above:

$$\rho = \frac{\sum_{j,k=1}^n \frac{a_j c_k}{r_j+r_k}}{\sqrt{\sum_{j,k=1}^n \frac{a_j a_k}{r_j+r_k}\times \sum_{j,k=1}^n \frac{c_j c_k}{r_j+r_k}}}$$

Since mixing decreases variance but not covariance, the correlation coefficient of the discrete system
will always be lower than that of its continuous or hybrid analog.

## 2.5 Simulation

To compare the analytical solutions with simulation, we generated a random directed acyclic graph,
shown in Figure 4. The numbers of species (7) and isomerization reactions (11) were chosen
arbitrarily. We enforced the existence of a single unique source node (a) and the weakly connected
property to ensure only a single source mRNA would be present and all isoforms would be reachable
from it, but did not impose any other conditions. The number of degraded species (3) was chosen
arbitrarily; we assigned degradation reactions to the two sink species (c, e) and randomly chose a
degraded intermediate (b) from a uniform distribution over the molecular species.

All reaction rates were drawn from a log-uniform distribution on $[10^{-0.5},10^{0.5}]$; we chose to sample
them from a single order of magnitude to avoid the trivial degenerate cases that occur in cases
of very slow or very fast export [10]. This process produced the parameter values $k=0.44$,
$\beta = [0.48, 2.12, 1.31, 2.21, 1.16, 2.41, 0.4, 1.19, 0.37, 1.19, 0.53]$, and $\gamma = [0.94, 2.38, 0.72]$, with the
indices corresponding to those in Figure 4. Finally, we chose the geometric burst model with
$b=10$.

We applied the algorithm to compute the exponents and coefficients, and computed the stationary
distributions of all species. The simulated distributions match the quantitative results for the
marginals, as shown in Figure 5. Furthermore, the 49 entries of the covariance matrix are likewise
effectively predicted by the procedure for moment calculation.

**Figure 4:** Graph representation of the randomly generated transcription, splicing, and degradation
model. A single source isoform $\mathcal{T}_a$ is converted to a variety of downstream isoforms $\mathcal{T}_b,\ldots,\mathcal{T}_g$, which
isomerize according to a directed acyclic graph. (Source node connects via $k$, $B\times$, to $\mathcal{T}_a$, which degrades at $\gamma_1$ and connects via $\beta_2,\beta_3$ to $\mathcal{T}_c$ and $\mathcal{T}_f$; $\mathcal{T}_b$ connects via $\beta_1$ to $\mathcal{T}_d$ and via $\beta_7$ to $\mathcal{T}_f$; $\mathcal{T}_f$ connects via $\beta_8,\beta_9,\beta_5$ to $\mathcal{T}_c, \mathcal{T}_b, \mathcal{T}_e$; $\mathcal{T}_d$ connects via $\beta_6$ to $\mathcal{T}_e$ and via $\beta_{10}$ to $\mathcal{T}_g$; $\mathcal{T}_c$ degrades at $\gamma_2$; $\mathcal{T}_a$ connects via $\beta_4$ to $\mathcal{T}_g$; $\mathcal{T}_g$ connects via $\beta_{11}$ to $\mathcal{T}_e$; $\mathcal{T}_e$ degrades at $\gamma_3$.)

**Figure 5:** Simulation of the randomly generated graph model. Histograms: empirical results (10,000
simulations). Black dots: theoretical and empirical covariance. Red lines: theory. [Species a–g marginal histograms, and a theoretical-vs-empirical covariance scatter plot.]

## 2.6 Multi-gene systems

Although the CME solution is a general framework, the relevance to modern transcriptomic experimental
data is tempered somewhat by the simplicity of the model. The model can describe
the splicing cascade of a single gene, but does not naturally extend to multi-gene networks. Yet
we know that genes often belong to co-expression modules that are identifiable by similarity metrics [3, 27]. Therefore, we are faced with the challenge of integrating multiple genes in a physically
meaningful way.

Instead of building intractable "top-down" models that encode complex networks, we may build
"bottom-up" models that extend analytical solutions. For example, we can consider sets of *synchronized* genes that experience bursting events at the same time. This model represents the bursty
limit of multiple genes with transcription rates governed by a single telegraph process, up to scaling;
a conceptually similar model has previously been used to describe correlations between multiple
copies of one gene [28]. This model retains the appeal of physical interpretability – for example,
gene modules may be regulated by the same molecule – but does not excessively complicate the
mathematics, and offers an incremental step toward more detailed descriptions.

### 2.6.1 Two-gene bursty model, no splicing

We begin by considering the instructive model of two genes influenced by the same regulator, with
no downstream splicing. The burst processes are synchronized, but the burst sizes are not, and
may indeed come from different distributions.

$$\varnothing \xrightarrow{k} B_1\times \mathcal{T}_1 + B_2\times\mathcal{T}_2$$
$$\mathcal{T}_1 \xrightarrow{\beta_1} \varnothing$$
$$\mathcal{T}_2 \xrightarrow{\beta_2} \varnothing$$

The following CME holds:

$$\frac{dP(m_1,m_2,t)}{dt} = k\left(\sum_{i=0}^{m_1}\sum_{j=0}^{m_2}p_i q_j P(m_1-i,m_2-j) - P(m_1,m_2,t)\right)$$
$$-\beta\left((m_1+1)P(m_1+1,m_2,t)-m_1P(m_1,m_2,t)\right)$$
$$-\gamma\left((m_2+1)P(m_1,m_2+1,t)-m_2P(m_1,m_2,t)\right),$$

where $p_i$ and $q_j$ give the PMF weights of the burst size distributions that govern $B_1$ and $B_2$. We
define the joint PGF

$$G(x_1,x_2,t) := \sum_{m_1=0}^\infty \sum_{m_2=0}^\infty P(m_1,m_2,t)x_1^{m_1}x_2^{m_2},$$

and recognize that the degradation terms have the familiar functional forms $-\beta_1(x_2-1)\frac{\partial G}{\partial x_1}$ and
$-\beta_2(x_2-1)\frac{\partial G}{\partial x_2}$. Therefore, considering the burst term:

$$\sum_{m_1=0}^\infty \sum_{m_2=0}^\infty x_1^{m_1}x_2^{m_2}\sum_{i=0}^{m_1}\sum_{j=0}^{m_2}p_i q_j P(m_1-i,m_2-j,t)$$

$$= \sum_{m_1=0}^\infty \sum_{m_2=0}^\infty \sum_{i=0}^{m_1}\sum_{j=0}^{m_2}x_1^{m_1}x_2^{m_2}p_i q_j P(m_1-i,m_2-j,t)$$

$$= \sum_{m_1=0}^\infty \sum_{m_2=0}^\infty \sum_{i=0}^{n}\sum_{j=0}^{m}(x_1^i p_i)(x_2^j q_j)x_1^{m_1-i}y^{m_2-j}P(m_1-i,m_2-j,t)$$

$$= \sum_{m_1=0}^\infty \sum_{i=0}^{n}(x_1^i p_i)x_1^{m_1-i}\sum_{m_2=0}^\infty \sum_{j=0}^{m_2}(x_2^j q_j)x_2^{m_2-j}P(m_1-i,m_2-j,t)$$

$$= \sum_{m_1=0}^\infty \sum_{i=0}^{m_1}(x_1^i p_i)x_1^{m_1-i}F_2(x_2)G'(x_2;m_1-i)$$

$$= F_1(x_1)F_2(x_2)G(x_1,x_2),$$

where $G'$ is the conditional PGF assuming $m_1-i$ molecules of $\mathcal{T}_1$ and $F_i$ are the burst distribution
PGFs; the final steps exploit the interpretation of the double sums as Cauchy products. This result
implies:

$$\frac{\partial G}{\partial t} = k(F_1(x_1)F_2(x_2)-1)G - \beta_1(x_1-1)\frac{\partial G}{\partial x_1} - \beta_2(y_2-1)\frac{\partial G}{\partial y_2};$$

defining $G=e^\phi$, $u_i = x_i-1$, and $M_i(u_i) = F_i(1+u_i)$:

$$\frac{\partial\phi}{\partial t} = k(M_1(u_1)M_2(u_2)-1) - \sum_{i=1}^2 \beta_i u_i\frac{\partial\phi}{\partial u_i}.$$

The PDE can be solved using the method of characteristics, yielding $U_i = u_i e^{-\beta_1 s}$:

$$\phi = k\int_0^t [M_1(U_1)M_2(U_2)-1]ds = k\int_0^t \left[\frac{1}{1-b_1U_1}\frac{1}{1-b_2U_2}-1\right]ds$$

$$= k\int_0^t \left[\frac{1}{1-b_1u_1e^{-\beta_1 s}}\frac{1}{1-b_2u_2e^{-\beta_2 s}}-1\right]ds,$$

assuming, as before, that $B_i \sim \mathrm{Geom}(b_i)$.

### 2.6.2 $n$-gene bursty model with splicing

From the derivation above, four interesting properties stand out. Firstly, the functional form of $U_i$
depends only on the details of the downstream processes; as shown, it can be easily computed for
any DAG. Secondly, the derivation holds with no loss of generality for *any* number of genes, so long
as the burst distributions are uncoupled, by repeated application of the Cauchy product formula.

Thirdly, even if they *are* coupled, the derivation still holds, but with intermediate conditional
PGFs $F_i$, ultimately yielding a joint PGF $F$ that factorizes in the independent case. Finally, even
though we have considered the case of disjoint DAGs, the results still hold if the gene products
can ultimately converge. This becomes self-evident by identifying $\mathcal{T}_1$ with $\mathcal{T}_2$ and setting $u_1=u_2$,
$b_1=b_2$, and $\beta_1=\beta_2$: the synchronized loci are merely multiple copies of the same gene, and
produce bursts sampled from a *negative binomial* distribution. Therefore, in the most general case
of arbitrary burst distributions and downstream splicing cascades, the factorial-cumulant generating
function takes the following form:

$$\phi = k\int_0^t [M(U_1,\ldots,U_N)-1]ds,$$

where $U_1,\ldots,U_N$ are now the "$U_1$" functions, not necessarily distinct, corresponding to the species
produced by each bursty locus, and $M$ is the joint MGF of the burst distributions. The single-gene
results are recovered by marginalization.

### 2.6.3 Examples of multi-gene systems

**Uncorrelated gene loci** By the Cauchy-Schwarz inequality, all moments and cross-moments
exist. The correlations are straightforward to compute. For example, we can consider the stationary covariance of gene products from two co-expressed genes, with disjoint downstream splicing
processes. We marginalize over all other transcripts and consider the functional forms $U_l = u_l\psi_l$
and $U_i = u_i\psi_i$, supposing that the respective average burst sizes are $b_l$ and $b_i$.

$$\frac{d^2e^\phi}{du_l du_i} = \frac{d}{du_l}e^\phi k\int_0^\infty \frac{1}{(1-b_lu_l\psi_l)}\frac{b_i\psi_i ds}{(1-b_iu_i\psi_i)^2}$$

$$= e^\phi k^2\int_0^\infty \frac{1}{1-b_uu_l\psi_l}\frac{b_i\psi_i ds}{(1-b_iu_i\psi_i)^2}\int_0^\infty \frac{b_l\psi_l ds}{(1-b_lu_l\psi_l)}\frac{1}{1-b_iu_i\psi_i}$$

$$+e^\phi k\int_0^\infty \frac{b_l\psi_l}{(1-b_lu_l\psi_l)^2}\frac{b_i\psi_i ds}{(1-b_iu_i\psi_i)^2}$$

$$\mathbb{E}[\Lambda_l\Lambda_i] = k^2 b_i b_l\int_0^\infty \psi_l ds\int_0^\infty \psi_i ds + kb_ib_l\int_0^\infty \psi_l\psi_i ds$$

$$= \mu_l\mu_i + kb_ib_l\int_0^\infty \psi_l\psi_i ds = \mathrm{Cov}(\Lambda_l,\Lambda_i) + \mu_l\mu_i,$$

which implies that

$$\mathrm{Cov}(\Lambda_l,\Lambda_i) = kb_ib_l\int_0^\infty \psi_l\psi_i ds = kb_ib_l\sum_{j,k=1}^n \frac{a_jc_k}{r_j+r_k},$$

where $a_j$ are the weights associated with $\psi_l$ and $c_k$ are the weights associated with $\psi_i$, much as
before. The covariance of the discrete process is identical. We reiterate that this expression *only*
applies when the splicing graphs downstream of the gene loci are disjoint. The converse case
requires slightly more unwieldy notation to account for, e.g., species $l$ accessible from $N$ source
transcripts being associated with distinct coefficients $a_l^{(1)},a_l^{(2)},\ldots,a_l^{(N)}$, and does not appear to have a simple
analytical expression totally agnostic of the number of loci and accessibility; nevertheless, it is easily
tractable by appropriately defining the function sets $\{U_l^{(j)}\}$ and $\{U_i^{(j)}\}$ and using the procedure
above.

With this solution in hand, we can revisit the two-gene problem with no splicing:

$$\mathrm{Cov}(\Lambda_1,\Lambda_2) = \frac{kb_1b_2}{\beta_1+\beta_2}. \tag{1}$$

We are interested in standard summaries, such as the Pearson correlation coefficient:

$$\rho = \frac{\mathrm{Cov}(\Lambda_1,\Lambda_2)}{\sigma_1\sigma_2} = \frac{kb_1b_2}{\beta_1+\beta_2}\times \sqrt{\frac{\beta_1\beta_2}{k^2b_1(1+b_1)b_2(1+b_2)}}$$

$$= \frac{\sqrt{\beta_1\beta_2}}{\beta_1+\beta_2}\times \sqrt{\frac{1}{(1+1/b_1)(1+1/b_2)}}$$

$$= \frac{\sqrt{\beta_1/\beta_2}}{1+\beta_1/\beta_2}\times \sqrt{\frac{1}{(1+1/b_1)(1+1/b_2)}},$$

where we use the fact that the absolute timescale is immaterial. The first term achieves a global
maximum of $1/2$ at $\beta_1=\beta_2$. The second is strictly smaller than 1, but asymptotically approaches
1 as $b_1,b_2$ jointly approach infinity. All downstream processes are stochastic and desynchronize
molecular observables. Therefore, $1/2$ is the supremum of gene-gene correlations in this class of
models.

**Fully correlated gene loci** Conversely, we can consider the two-gene problem assuming that
the burst distributions are identical and fully correlated. Physically, this model may correspond to
coupling of *initiation* processes, e.g. this may occur when two genes are controlled by a single
promoter. This burst distribution has the following joint PGF:

$$F(x_1,x_2) = \sum_{i,j}x_1^i x_2^j p_{i,j}$$

$$= \sum_{i,j}x_1^i x_2^j p_i\delta(i-j) = \sum_{i=0}^\infty (x_1x_2)^i\left(\frac{b}{b+1}\right)^i \frac{1}{b+1}$$

$$= \frac{1}{1+b-bx_1x_2}$$

$$M(u_1,u_2) = F(1+u_1,1+u_2) = \frac{1}{1+b-b(1+u_1)(1+u_2)};$$

upon inserting the characteristics, we yield

$$\phi = k\int_0^\infty \left[\frac{1}{1+b-b(1+u_1e^{-\beta_1 s})(1+u_2e^{-\beta_2 s})}-1\right]ds$$

$$\frac{d^2e^\phi}{du_1du_2} = \frac{d}{du_1}e^\phi k\int_0^\infty \frac{b(1+u_1e^{-\beta_1 s})e^{-\beta_2 s}ds}{(1+b-b(1+u_1e^{-\beta_1 s})(1+u_2e^{-\beta_2 s}))^2}$$

$$= e^\phi k^2\int_0^\infty \frac{b(1+u_1e^{-\beta_1 s})e^{-\beta_2 s}ds}{(1+b-b(1+u_1e^{-\beta_1 s})(1+u_2e^{-\beta_2 s}))^2}$$

$$\times \int_0^\infty \frac{b(1+u_2e^{-\beta_2 s})e^{-\beta_1 s}ds}{(1+b-b(1+u_1e^{-\beta_1 s})(1+u_2e^{-\beta_2 s}))^2}$$

$$-e^\phi k\int_0^\infty \frac{be^{-(\beta_1+\beta_2)s}ds}{(1+b-b(1+u_1e^{-\beta_1 s})(1+u_2e^{-\beta_2 s}))^2}$$

$$+e^\phi k\int_0^\infty \frac{2be^{-(\beta_1+\beta_2)s}(1+b)ds}{(1+b-b(1+u_1e^{-\beta_1 s})(1+u_2e^{-\beta_2 s}))^3}$$

Plugging in $u_1=u_2=0$,

$$\mathbb{E}[\Lambda_1\Lambda_2] = k^2b^2\int_0^\infty e^{-\beta_1 s}ds\int_0^\infty e^{-\beta_2 s}ds$$

$$-kb\int_0^\infty e^{-(\beta_1+\beta_2)s}ds + 2kb(1+b)\int_0^\infty e^{-(\beta_1+\beta_2)s}ds$$

$$= k^2b^2\frac{1}{\beta_1}\frac{1}{\beta_2} - kb\frac{1}{\beta_1+\beta_2} + 2kb(1+b)\frac{1}{\beta_1+\beta_2}$$

$$= \mu_1\mu_2 + \frac{kb(2b+1)}{\beta_1+\beta_2},$$

which yields the result

$$\mathrm{Cov}(\Lambda_1,\Lambda_2) = \frac{kb(2b+1)}{\beta_1+\beta_2}.$$

Therefore, the correlation is

$$\rho = \frac{\mathrm{Cov}(\Lambda_1,\Lambda_2)}{\sigma_1\sigma_2} = \frac{kb(2b+1)}{\beta_1+\beta_2}\times\sqrt{\frac{\beta_1\beta_2}{k^2b^2(1+b)^2}}$$

$$= \frac{2b+1}{\beta_1+\beta_2}\times \frac{\sqrt{\beta_1\beta_2}}{1+b} = \frac{\sqrt{\beta_1\beta_2}}{\beta_1+\beta_2}\times\frac{2b+1}{b+1} = \frac{\sqrt{\beta_1\beta_2}}{\beta_1+\beta_2}\times\left(\frac{b+1}{b+1}+\frac{b}{b+1}\right)$$

$$= \frac{\sqrt{\beta_1/\beta_2}}{1+\beta_1/\beta_2}\times\left(1+\frac{b}{b+1}\right).$$

As in the case of uncoupled gene sizes reported in Equation 1, the first term is at most $1/2$. The
second term asymptotically approaches 2 as $b\to\infty$. Therefore, there are no intrinsic model
constraints on Pearson correlation coefficients of two gene products; constraints arise as the *effect*
of the burst size correlation structure.

**Anti-correlated gene loci** With these results in mind, we can consider the problem of describing
genes with high *negative* correlations. As an illustration, we can consider two genes driven by a
single telegraph process: gene 1 is on whenever gene 2 is off and vice versa; therefore, their respective
products $\mathcal{T}_1$ and $\mathcal{T}_2$ must have a negative correlation. However, only one of these genes has a welldefined bursty limit that is infinitesimally short on periods; the other will essentially be on all the
time and transcribe constitutively, containing no mutual information about the burst timing.

Nevertheless, putting aside the problem of positing a specific limiting mechanism, we can ask
whether *any* joint burst distribution can produce negative correlations in molecule counts, *despite*
perfect synchronization between burst events. Considering the cross moment of mRNA produced
at two synchronized loci:

$$\phi = k\int_0^\infty [M(U_1(u_1),U_2(u_2))-1]ds$$

$$\frac{d^2e^\phi}{du_1du_2} = \frac{d}{du_1}e^\phi k\int_0^\infty \frac{dM}{du_2}ds$$

$$= e^\phi k\int_0^\infty \frac{d^2M}{du_1u_2}ds + e^\phi k^2\int_0^\infty \frac{dM}{du_1}ds\int_0^\infty \frac{dM}{du_2}ds$$

$$\mathbb{E}[\Lambda_1\Lambda_2] = k\int_0^\infty \frac{d^2M}{du_1u_2}ds + k^2\int_0^\infty \frac{dM}{du_1}ds\int_0^\infty \frac{dM}{du_2}ds,$$

with the partial derivatives evaluated at $u_1=u_2=0$. The second term matches $\mu_1\mu_2$, and is
strictly positive. The first term is the integral of an exponentially discounted burst cross moment:

$$\frac{d^2M}{du_1u_2} = \frac{d}{du_2}\left(\frac{dM}{dU_1}\frac{dU_1}{du_1}\right)$$

$$= \frac{d^2M}{dU_1dU_2}\frac{dU_1}{du_1}\frac{dU_2}{du_2}$$

$$= \frac{d^2M}{dU_1dU_2}e^{-(\beta_1+\beta_2)s}$$

$$= \mathbb{E}[B_1B_2]e^{-(\beta_1+\beta_2)s}$$

where the partial derivatives are yet again evaluated at $u_1=u_2=U_1=U_2=0$, and $B_1$ and $B_2$
denote the SDE jump sizes at the two gene loci. By the definition of covariance:

$$\mathbb{E}[\Lambda_1\Lambda_2] = k\frac{\mathbb{E}[B_1B_2]}{\beta_1+\beta_2}+\mu_1\mu_2 = \frac{k}{\beta_1+\beta_2}(\mathrm{Cov}(B_1,B_2)+\mu_{B_1}\mu_{B_2})+\mu_1\mu_2.$$

Now, supposing the correlation between the burst sizes is $\rho \in [-1,0)$, and considering the covariance
between the transcripts:

$$\mathrm{Cov}(\Lambda_1,\Lambda_2) = k\frac{\mathbb{E}[B_1B_2]}{\beta_1+\beta_2} = \frac{k}{\beta_1+\beta_2}(\rho\sigma_{B_1}\sigma_{B_2}+\mu_{B_1}\mu_{B_2}),$$

which achieves a minimum at $\rho=-1$. Thus, the covariance has a lower limit:

$$\mathrm{Cov}(\Lambda_1,\Lambda_2) \ge \frac{k}{\beta_1+\beta_2}(\mu_{B_1}\mu_{B_2}-\sigma_{B_1}\sigma_{B_2}).$$

Without constructing the joint distribution explicitly, if we suppose the marginal discrete burst
distributions are geometric – i.e., the jump sizes are exponential – then $\mu_{B_i}=\sigma_{B_i}=b_i$, and the
lower limit on covariance is zero. This means that negative correlations cannot possibly result
from a model with geometrically distributed, synchronized jumps. However, other joint burst laws
*can* produce negative correlations, as long as the population correlation coefficient is sufficiently
negative and the burst distributions are sufficiently dispersed.

We can demonstrate the existence of processes with negative count correlations induced by synchronized burst events. First, we suppose that the marginal burst distributions are identical and described by a gamma law with shape $\alpha$ and scale $\theta$, enforcing $\mu_{B_1}=\mu_{B_2}=\alpha\theta$ and $\sigma_{B_1}^2=\sigma_{B_2}^2=\alpha\theta^2$.
Therefore, the covariance of the Poisson intensities takes the following form:

$$\mathrm{Cov}(\Lambda_1,\Lambda_2) = \frac{k}{\beta_1+\beta_2}(\rho\alpha\theta^2+\alpha^2\theta^2)$$

$$= \frac{k\theta^2}{\beta_1+\beta_2}(\rho\alpha+\alpha^2),$$

which achieves $\mathrm{Cov}(\Lambda_1,\Lambda_2)<0$ whenever $\rho\alpha+\alpha^2<0$. Therefore, for any $\rho\in(-1,0)$, every
$\alpha\in(0,-\rho)$ meets this criterion.

It remains to confirm that a bivariate gamma distribution with a negative correlation can exist.
Such a distribution was constructed by Moran, and permits all $\rho\in(-1,1)$ [29,30]. Furthermore, a
simple application of the Cauchy-Schwarz inequality yields [31]:

$$M(u_1,u_2) = \mathbb{E}[e^{u_1B_1+u_2B_2}] \le \sqrt{\mathbb{E}[e^{2u_1B_1}]\mathbb{E}[e^{2u_2B_2}]} < \infty;$$

therefore, the joint MGF of the correlated bivariate gamma distribution is guaranteed to exist.
This demonstrates the existence of continuous moving average processes with negative stationary
correlation, driven by one Poisson process arrival process. Finally, the corresponding Poisson
mixture has identical covariance, and must also have a negative correlation. Therefore, a CME
with marginal negative binomial burst distributions and a carefully chosen joint structure can
achieve negative molecular correlations, even if the bursts are synchronized.

**Multi-gene dynamics emerging from fast processing** Interestingly, there is a set of singlegene systems that recapitulate the multi-gene functional form in the limit of fast splicing. Consider
a source species $\mathcal{T}_0$, which is produced in geometrically distributed bursts and converted to species
$\{\mathcal{T}_i\}$, with $i=1,\ldots,N$, at rates $\beta_i$. These transcripts are degraded at rates $\gamma_i$.

Furthermore, suppose all of the $\beta_i \sim \mathcal{O}(\varepsilon^{-1})$ for small $\varepsilon$, i.e., the source transcript is extremely
unstable. In this limit, $\mathcal{T}_i$ are produced with bursts of size $B\beta_i/r$, where $B$ is the underlying $\mathcal{T}_0$
burst size, $r := \sum_i \beta_i$, and the ratio $\beta_i/r$ is $O(1)$. We define corresponding *weights* $w_i := \beta_i/r$; by
definition, $\sum_i w_i = 1$. This yields:

$$U_0 = Ke^{-rs} + \sum_{i=1}^N \frac{\beta_i u_i}{r-\gamma_i}e^{-\gamma_i s}$$

$$\to \sum_{i=1}^N w_i u_i e^{-\gamma_i s}$$

$$M(U_0) = \frac{1}{1-bU_0} = \frac{1}{1-b\sum_i w_iu_ie^{-\gamma_i s}},$$

where $M$ is recognizable as the joint MGF of a perfectly correlated $N$-variate exponential distribution
with marginal distributions $B_i = w_iB$:

$$M(u_1,\ldots,u_N) = \mathbb{E}\left[e^{\sum_i u_iB_i}\right] = \mathbb{E}\left[e^{(\sum_i w_iu_i)B}\right],$$

i.e., the univariate exponential MGF evaluated at $\sum_{i=1}^N w_iu_i$.
The corresponding discrete PGF is:

$$F(x_1,\ldots,x_N) = \frac{1}{1-b\sum_i w_i(x_i-1)} = \frac{1}{1-b\sum_i(w_ix_i-w_i)}$$

$$= \frac{1}{1+b-b\sum_i w_ix_i}$$

As seen above, this is *not* the perfectly correlated multivariate geometric distribution: the stochasticity of the reaction channel selection is non-negligible. Instead, we can construct a distribution
over $\{0,1\}^N$, with the probability of state $\delta_{ij}$ (i.e., the vector contains a one at position $i$) set to
$w_i$. It is easy to see that the generating function of the random variable $Z\in\{0,1\}^N$ takes the form
derived above:

$$H(x_1,\ldots,x_N) = \mathbb{E}\left[x_1^{Z_1}\ldots x_N^{Z_N}\right] = \sum_i w_ix_i,$$

which amounts to $F(x_1,\ldots,x_N) = F(H(x_1,\ldots,x_N))$; i.e., the effective gene dynamics are described
by a compound distribution.

Upon inserting the characteristics and selecting a set of two genes (arbitrarily indexed by 1 and 2),
we yield:

$$\phi = k\int_0^\infty \left[\frac{1}{1-bw_1u_1e^{-\gamma_1 s}-bw_2u_2e^{-\gamma_2 s}}-1\right]ds$$

$$\frac{d^2e^\phi}{du_1du_2} = \frac{d}{du_1}e^\phi k\int_0^\infty \frac{bw_2e^{-\gamma_2 s}ds}{(1-bw_1u_1e^{-\gamma_1 s}-bw_2u_2e^{-\gamma_2 s})^2}$$

$$= e^\phi k^2\int_0^\infty \frac{bw_1e^{-\gamma_1 s}ds}{(1-bw_1u_1e^{-\gamma_1 s}-bw_2u_2e^{-\gamma_2 s})^2}$$

$$\times \int_0^\infty \frac{bw_2e^{-\gamma_2 s}ds}{(1-bw_1u_1e^{-\gamma_1 s}-bw_2u_2e^{-\gamma_2 s})^2}$$

$$+e^\phi k\int_0^\infty \frac{2b^2w_1w_2e^{-(\gamma_1+\gamma_2)s}ds}{(1-bw_1u_1e^{-\gamma_1 s}-bw_2u_2e^{-\gamma_2 s})^3}.$$

Plugging in $u_1=u_2=0$,

$$\mathbb{E}[\Lambda_1\Lambda_2] = k^2b^2\int_0^\infty e^{-\gamma_1 s}ds\int_0^\infty e^{-\gamma_2 s}ds + 2kb^2w_1w_2\int_0^\infty e^{-(\gamma_1+\gamma_2)s}ds$$

$$= k^2b^2\frac{w_1}{\gamma_1}\frac{w_2}{\gamma_2} + 2kb^2\frac{w_1w_2}{\gamma_1+\gamma_2}$$

$$= \mu_1\mu_2 + \frac{2kb^2w_1w_2}{\gamma_1+\gamma_2},$$

since marginalization with respect to any gene recovers the univariate geometric burst distribution
with scale $bw_i$, which immediately yields $\mu_i = kbw_i/\gamma_i$. This implies:

$$\mathrm{Cov}(\Lambda_1,\Lambda_2) = \frac{2kb^2w_1w_2}{\gamma_1+\gamma_2}.$$

From the marginal results, we still have $\sigma_i^2 = kbw_i(1+bw_i)/\gamma_i$. This yields:

$$\rho = \frac{\mathrm{Cov}(\Lambda_1,\Lambda_2)}{\sigma_1\sigma_2} = \frac{2kb^2w_1w_2}{\gamma_1+\gamma_2}\times \sqrt{\frac{\gamma_1\gamma_2}{k^2bw_1(1+bw_1)bw_2(1+bw_2)}}$$

$$= \frac{2\sqrt{\gamma_1\gamma_2}}{\gamma_1+\gamma_2}\times \sqrt{\frac{b^2w_1^2w_2^2}{w_1w_2(1+bw_1)(1+bw_2)}}$$

$$= \frac{2\sqrt{\gamma_1/\gamma_2}}{1+\gamma_1/\gamma_2}\times \sqrt{\frac{1}{(1+\frac{1}{bw_1})(1+\frac{1}{bw_2})}} \in (0,1).$$

Therefore, fast processing of the source transcript yields dynamics equivalent to a class of multi-gene
models, with positive, but otherwise unconstrained, correlation between the downstream species.

## 2.7 Transient gene dynamics

Thus far, we have primarily focused on stationary systems with time-independent parameters.
Nevertheless, there are classes of physiological phenomena, such as differentiation and cell cycling,
where transient behaviors are crucial, particularly since these processes occur on timescales comparable
to the mRNA lifetimes [1, 32]. Usually, the regulatory events underpinning these processes
are modeled by variation in DNA-localized transcriptional parameters [33, 34].

By examination of the generating function relations, it is easy to see that the current framework is
trivial to extend to *any* deterministic variation in $k$ and $M$:

$$\phi(t) = \int_0^t k(s)[M(\mathbf{U}(s),s)-1]ds,$$

where we have adopted the shorthand $\mathbf{U}$ for the set of exponential sums $U_1(s),\ldots,U_N(s)$ governing
each burst product of the $N$ loci. Therefore, burst frequency, burst size, and even the number of
synchronized gene loci per cell can vary, continuously or discontinuously.

If the reaction rates within $\mathbf{U}$ change over time, the generating function PDE then becomes intractable for all but the simplest models, such as piecewise constant. The gene locus parameters
$b$ and $k$ can also vary stochastically. In principle, certain models can be solved by defining an
appropriate SDE-CME system. However, such dynamics are generally challenging to treat without
recourse to numerical ODE solvers. Further, we restrict our analysis to systems tractable *via* the
PGF, which cannot be applied to continuous-valued parameters.

---

[← 1 Introduction](02-1-introduction.md) · [Up: contents](index.md) · [3 Applications to sequencing data →](04-3-applications-to-sequencing-data.md)
