---
title: 2 THEORETICAL FRAMEWORK
source: https://doi.org/10.1101/2022.10.17.512599/
source_file: sources/papers/gorin-2022-transient-delay-cme/gorin-2022-transient-delay-cme.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-10-02'
---

> **Reconstructed by a model.** `gorin-2022-transient-delay-cme.pdf` from [papers/gorin-2022-transient-delay-cme](https://doi.org/10.1101/2022.10.17.512599/) — papers · gorin-2022-transient-delay-cme, licensed CC BY 4.0. Converted 2026-10-02 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 2 THEORETICAL FRAMEWORK

## 2.1 Preliminaries

We seek to model a system with $n$ RNA species with counts $m_1, ..., m_n := \mathbf{m} \in \mathbb{N}_0^n$. The molecules interconvert through monomolecular reactions, which are either Markovian, with waiting time distributed per $\mathrm{Exp}(c_{ik})$ for conversion from species $i$ to species $k$, or delayed, with deterministic waiting time $\tau_i$. The molecules may also be degraded, with analogous allowed waiting time distributions. We assume the interconversion topology is described by a directed acyclic graph (Gorin and Pachter, 2022a).

We consider two models of transcriptional dynamics. In the first, we suppose that the transcription process is entirely memoryless, and molecules are produced in bursts according to a Poisson arrival process with rate $\alpha_i$. This system is fully specified by a probability law $P(\mathbf{m}, t|P^0, 0)$, with the initial condition defined by the distribution $P^0(\mathbf{m})$.

In the second, we propose that the transcribing promoter exists in one of $N$ states, with interconversion rates $H_{jk}$ for transitions from state $j$ to state $k$. Each state has a characteristic transcription rate $\alpha_{j,i}$, for each promoter state and molecule index; transcription occurs according to a Poisson arrival process. This system is fully specified by a probability law $\mathbf{P}(\mathbf{m}, t|\mathbf{w}, \mathbf{P}^0, 0)$, where the entries of $\mathbf{P}$ contain the non-normalized probabilities $P_j(\mathbf{m}, t)$ for each promoter state. The initial conditions include $\mathbf{P}^0$, the set of non-normalized molecule distributions for each promoter state imposed at $t = 0$.

Solutions for these systems typically cannot be obtained in closed form. However, they can be calculated by the Fourier inversion of the probability generating function (PGF), defined as follows:

$$G(\mathbf{x}) = \sum_{\mathbf{m}} \mathbf{x}^{\mathbf{m}} P(\mathbf{m}), \tag{1}$$

where the summation takes place over all microstates $\mathbf{m} \in \mathbb{N}_0^n$, and $\mathbf{x}^{\mathbf{m}}$ is an informal shorthand for $\prod_i x_i^{m_i}$. It is typically more straightforward to consider $G(\mathbf{u})$, with $u_i = x_i - 1$. Further, the multi-state problem affords a PGF-like vector object $\mathbf{G}$, with components $G_j$ such that

$$G_j(\mathbf{x}) = \sum_{\mathbf{m}} \mathbf{x}^{\mathbf{m}} P_j(\mathbf{m}). \tag{2}$$

## 2.2 The transient dynamics of bursty systems

As previously discussed in (Gorin and Pachter, 2022a), $G^h$, the PGF of a Markovian bursty process started at the homogeneous initial condition $\mathbf{m}_0 = 0$ has the following logarithm:

$$\ln G^h(\mathbf{u}, t) = \phi^h(\mathbf{u}, t) = \int_0^t \alpha^T [\mathbf{M}(\mathbf{U}(\mathbf{u}, s)) - \mathbf{1}] \, ds, \tag{3}$$

where the inner product is taken over all distinct combinations of burst processes in the system. The entries of $\alpha$ are the burst process arrival frequencies. The entries of $\mathbf{M}$ are the burst process moment-generating functions (MGFs). $\mathbf{u}$ is a vector of generating function arguments. The interconversion and degradation processes induce a series of *characteristics*, $\mathbf{U}(\mathbf{u}, s)$, which solve the following series of ordinary differential equations:

$$\frac{d\mathbf{U}}{ds} = C\mathbf{U} \text{ s.t. } \mathbf{U}(s = 0) = \mathbf{u}, \tag{4}$$

where $C \in \mathbb{R}_+^{n \times n}$ is a matrix containing the rates of interconversion and degradation of the $n$ species.

To obtain the PGF of a non-homogeneous system, started at a distribution with the arbitrary PGF $G^0(\mathbf{u})$, we take advantage of the fact that the newly transcribed molecules are statistically independent from the pre-existing molecules:

$$G(\mathbf{u}, t; G^0, 0) = G^0(\mathbf{U}(\mathbf{u}, t))G^h(\mathbf{u}, t). \tag{5}$$

This formula can be evaluated using a single integral per value of $\mathbf{u}$.

## 2.3 The transient dynamics of multi-state systems

It is straightforward to extend the foundations in (Gorin and Pachter, 2022a) to include interconversion between promoter states. We assume there are $n$ species, with microstates $\mathbf{m} \in \mathbb{N}_0^n$, and $N$ promoter states, with $j \in \{0, ..., N-1\}$. The species are one-indexed; a reaction from a species to "0" corresponds to degradation, whereas the promoter states are zero-indexed, to reflect the common notation wherein a "0" state is inactive whereas a "1" state is active.

We assume the system contains the following Markovian reactions:

- Interconversion between promoter states.
- Synthesis of new molecules.
- Interconversion of molecular species.
- Degradation of molecular species.

Define the collection of state-specific generating functions $\mathbf{G} := [G_0, ..., G_{N-1}]^T$, such that

$$G_j := \sum_{\mathbf{m}} \mathbf{x}^{\mathbf{m}} P_j(\mathbf{m}). \tag{6}$$

This collection is associated with the $N \times n$ Jacobian matrix:

$$J_{ji} := \frac{\partial G_j}{\partial x_i} = \frac{\partial G_j}{\partial u_i}, \tag{7}$$

defining $u_i = x_i - 1$ for each generating function argument.

By definition, the master equation terms for switching between states contribute the following terms to the PDE system:

$$\left(\frac{\partial G_j}{\partial t}\right)_{\text{switch}} = \sum_{j=0}^{N-1} H_{kj} G_k. \tag{8}$$

$H \in \mathbb{R}^N$ is the matrix encoding the continuous-time Markov chain (CTMC) governing the promoter states, such that $\sum_k H_{jk} = 0$ for all $j$. The diagonal terms encode the net efflux rate from state $j$, such that $H_{jj} := \sum_{k \neq j} H_{jk}$. This set of reactions can be represented in the usual form for a finite CTMC:

$$\left(\frac{\partial \mathbf{G}}{\partial t}\right)_{\text{switch}} = H^T \mathbf{G}. \tag{9}$$

From (Gorin and Pachter, 2022a), the master equation terms for RNA synthesis contribute the following terms to the PDE system:

$$\left(\frac{\partial G_j}{\partial t}\right)_{\text{tx}} = \sum_{i=1}^n \alpha_{j,i} u_i G_j, \tag{10}$$

This set of reactions can be summarized by the matrix $A \in (\mathbb{R}_{\geq 0})^{N \times n}$, such that $A_{ji} = \alpha_{j,i}$ is the rate of production of transcript $i$ while the gene is in state $j$:

$$\left(\frac{\partial \mathbf{G}}{\partial t}\right)_{\text{tx}} = (A\mathbf{u}) \odot \mathbf{G}, \tag{11}$$

where the symbol $\odot$ denotes the Hadamard, or entrywise, product of two matrices of identical dimensions.

Finally, the master equations for monomolecular, non-catalytic interconversion or degradation contribute the following terms:

$$\left(\frac{\partial G_j}{\partial t}\right)_{\text{conv}} = \sum_{i=1}^n \left(-c_{i0} u_i + \sum_{k=1}^n c_{ik}(u_k - u_i)\right) \frac{\partial G_j}{\partial u_i} \tag{12}$$

where $c_{ik}$ is the rate of transitioning from species $i$ to species $k$ and $c_{i0}$ is the degradation rate of species $i$. This set of reactions can be summarized by the matrix $C \in \mathbb{R}^{n \times n}$ encoding the transitions between molecular species, such that $C_{ik} = c_{ik}$ and $C_{ii} = -\sum_{k \neq i} c_{ik} - c_{i0}$:

$$\left(\frac{\partial \mathbf{G}}{\partial t}\right)_{\text{conv}} = J(C\mathbf{u}). \tag{13}$$

The coupled generating function PDEs take the following form:

$$\frac{\partial \mathbf{G}}{\partial t} = H^T \mathbf{G} + (A\mathbf{u}) \odot \mathbf{G} + J(C\mathbf{u})$$
$$-H^T \mathbf{G} - (A\mathbf{u}) \odot \mathbf{G} = -\frac{\partial \mathbf{G}}{\partial t} + J(C\mathbf{u}). \tag{14}$$

For each $j$, we can apply the method of characteristics (Singh and Bokes, 2012):

$$\frac{dG_j}{ds} = \frac{dG_j}{dT}\frac{dT}{ds} + \sum_{i=1}^n \frac{dG_j}{dU_i}\frac{dU_i}{ds}$$
$$\frac{dU_i}{ds} = (C\mathbf{U})_i \tag{15}$$
$$\frac{dT}{ds} = -1$$

Imposing $T(s=0) = t$, we find $T(s) = t - s$. By enforcing $U_i(s=0) = u_i$, we can simultaneously solve the system $\partial_s \mathbf{U} = C\mathbf{U}$. We then yield:

$$-\frac{d\mathbf{G}(\mathbf{U}(s), T(s))}{ds} = H^T \mathbf{G} + (A\mathbf{U}) \odot \mathbf{G}, \tag{16}$$

an initial value problem in $N$ variables, parametrized by the characteristic variable $s$. We seek to obtain $\mathbf{G}$ at $T = t$, i.e., $s = 0$. We possess an initial condition $\mathbf{G}^0$ at $T = 0$, i.e., $s = t$. By numerically integrating $-H^T \mathbf{G} - (A\mathbf{U}) \odot \mathbf{G}$ from $s = t$ to $s = 0$, using $\mathbf{G}^0(\mathbf{U}(t))$ as the initial condition, we yield $\mathbf{G}(\mathbf{u}, t)$.

### 2.3.1 Solution through the lens of matrix ODEs

In practical terms, Equation 16 and its associated initial conditions are the solution to a particular switching system: the ODE can be easily plugged into a standard Runge–Kutta-type solver to obtain the generating function. However, we can, in principle, write down the ODE in more compact form:

$$\mathcal{D}(t) = -H^T - \mathrm{diag}\, A\mathbf{U}$$
$$\frac{d\mathbf{G}}{ds} = \mathcal{D}(s)\mathbf{G}, \tag{17}$$

where $\mathcal{D}$ is the matrix that encodes system $d$ynamics. We observe:

$$\mathcal{D}(t_1)\mathcal{D}(t_2) = \left[H^T + \mathrm{diag}\, A\mathbf{U}(t_1)\right]\left[H^T + \mathrm{diag}\, A\mathbf{U}(t_2)\right] \neq \mathcal{D}(t_2)\mathcal{D}(t_1) \tag{18}$$

in general; the product of diagonal matrices commutes, but the product of $H^T$ and a diagonal matrix does not (except in the trivial case $N = 1$). Therefore, $\mathbf{G}$ cannot be represented by a finite matrix exponential, but can be approximated by a Magnus series (Iserles and MacNamara, 2017).

### 2.3.2 Solution through the lens of special functions

Certain steady-state solutions can be obtained by appealing to the theory of special functions. The stationary PGF of the solution to the standard telegraph model (with $N = 2$ and $n = 1$) is given by the confluent hypergeometric function $_1F_1$ (Iyer-Biswas et al., 2009); transient solutions have an analogous form. The combinatorial extension of the telegraph model (with $N = 2^p$, $p \in \mathbb{N}$), whose state transitions are given by the Hamming graph, has a stationary PGF given by the $p$-fold product of confluent hypergeometric functions. Certain systems with $n=1$ and an irreversible refractory state dynamics have solutions given by the generalized hypergeometric function $_{N-1}F_{N-1}$ (Zhou and Zhang, 2012). Thus, in principle, solutions may be obtained by casting the system of $N$ ODEs in Equation 16 into a single order-$N$ ODE, then solving it using the properties of special functions. However, this tends to be considerably more involved than the original problem, both due to the complexity of manipulating hypergeometric functions and the challenges of actually evaluating them. Further, although hypergeometric representations are available for $n = 1$, the case of $n > 1$ does not even afford a formal solution. We have found the ODE approach yields a satisfactory combination of numerical stability and robustness for most purposes.

## 2.4 Applications to delay master equations

The numerical recipes outlined above can be exploited to solve delay chemical master equations. Instead of using Equation 4 to obtain the characteristics, we solve the downstream system by hand, using Equations S35 and S36 of (Gorin and Pachter, 2022a) for species with Markovian efflux and the identity

$$U_i(s) = u_i\mathbb{I}(s < \tau_i) + U_k(s - \tau_i)\mathbb{I}(s > \tau_i) \tag{19}$$

for species $i$ converted to species $k$ after a deterministic delay $\tau_i$. $\mathbb{I}$ denotes the indicator function, which returns $\mathbb{I}(A) = 1$ if $A$ holds and $0$ otherwise. If species $i$ is degraded after a deterministic delay, its characteristic is simply $u_i\mathbb{I}(s < \tau_i)$. The resulting collection of characteristics can be plugged directly into Equation 5 or 16 and integrated.

---

[← 1 INTRODUCTION](02-1-introduction.md) · [Up: contents](index.md) · [3 RESULTS →](04-3-results.md)
