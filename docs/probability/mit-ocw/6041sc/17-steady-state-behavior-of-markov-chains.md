---
title: "17. Steady-State Behavior of Markov Chains"
course: "MIT 6.041SC"
chapter: 17
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 17. Steady-State Behavior of Markov Chains

## What this covers

This chapter examines the long-run behavior of discrete-time, discrete-state Markov chains, asking whether state occupancy probabilities settle to stationary values independent of initial conditions. We establish the steady-state convergence theorem, formulate the balance equations through a visit-frequency lens, and apply these tools to solve birth-death processes and simple queueing models in closed form. We assume familiarity with the Markov property, transition probability matrices, and the classification of recurrent and transient states.

## Long-Run Behavior and the Steady-State Theorem

Let $\{X_n, n = 0, 1, 2, \dots\}$ be a discrete-time Markov chain with finite state space $S = \{1, 2, \dots, m\}$ and stationary (time-homogeneous) transition probabilities:
$$p_{ij} = \mathbf{P}(X_{n+1} = j \mid X_n = i)$$

The $n$-step transition probabilities are denoted:
$$r_{ij}(n) = \mathbf{P}(X_n = j \mid X_0 = i)$$
These satisfy the fundamental Chapman-Kolmogorov recursion obtained via the total probability theorem:
$$r_{ij}(n) = \sum_{k} r_{ik}(n - 1)p_{kj}$$

For short horizons, calculating $r_{ij}(n)$ by enumerating every possible trajectory of length $n$ is possible, but the number of sample paths grows exponentially as $m^n$. The recursive formula organizes this computation systematically so that each additional step requires only a matrix-vector product.

A central question in probability is whether the probabilities $r_{ij}(n)$ stabilize as $n \to \infty$:
$$\lim_{n \to \infty} r_{ij}(n) \stackrel{?}{=} \pi_j$$
where $\pi_j$ is a steady-state distribution that no longer depends on the initial state $i$.

This convergence does not hold for all Markov chains. Two main structural obstacles can prevent it:

1. **Multiple Recurrent Classes:** A state $i$ is recurrent if, starting from $i$, any state reachable from $i$ can also lead back to $i$. A collection of recurrent states that all communicate with each other (and from which no other states can be reached) forms a recurrent class. States that are not recurrent are transient; the chain will eventually exit the transient states and become trapped in one of the recurrent classes. If there are two or more recurrent classes, the initial state dictates which class traps the process. The long-run probability of occupying state $j$ depends permanently on where the chain began.
2. **Periodicity:** A recurrent class is periodic if its states can be partitioned into $d > 1$ disjoint subsets $S_1, S_2, \dots, S_d$ such that transitions from $S_k$ always lead to $S_{k+1}$ (with $S_d$ leading to $S_1$). In a periodic chain, the state probabilities oscillate deterministically with period $d$ rather than settling down. A simple, sufficient check for aperiodicity is the existence of a self-transition: if $p_{ii} > 0$ for at least one recurrent state $i$, the chain cannot be partitioned in this cyclic manner and is therefore aperiodic.

<figure>
<svg viewBox="0 0 460 140" role="img" aria-label="Structural conditions for steady-state convergence showing recurrent classes and periodic partitions">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Transient and two recurrent classes -->
  <rect x="15" y="45" width="55" height="40" rx="6" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <text x="42" y="69" text-anchor="middle" font-size="12" fill="currentColor">Transient</text>
  <rect x="110" y="15" width="70" height="40" rx="6" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="145" y="39" text-anchor="middle" font-size="12" fill="currentColor">Class 1</text>
  <rect x="110" y="75" width="70" height="40" rx="6" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="145" y="99" text-anchor="middle" font-size="12" fill="currentColor">Class 2</text>
  <line x1="70" y1="55" x2="102" y2="40" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <line x1="70" y1="75" x2="102" y2="90" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Divider -->
  <line x1="225" y1="10" x2="225" y2="130" stroke="currentColor" stroke-dasharray="4,4" stroke-width="1"/>

  <!-- Periodic structure -->
  <circle cx="285" cy="65" r="22" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-width="1.2"/>
  <text x="285" y="69" text-anchor="middle" font-size="12" fill="currentColor">S₁</text>
  <circle cx="395" cy="65" r="22" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="395" y="69" text-anchor="middle" font-size="12" fill="currentColor">S₂</text>
  <path d="M 302 48 C 325 32, 355 32, 378 48" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
  <path d="M 378 82 C 355 98, 325 98, 302 82" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow)"/>
</svg>
<figcaption>Left: Multiple recurrent classes trap trajectories, preserving initial conditions. Right: A periodic structure with period 2 induces permanent oscillation between subsets.</figcaption>
</figure>

### The Steady-State Convergence Theorem

If a Markov chain has a **single recurrent class** and is **aperiodic** (not periodic), then for every state $j$:
$$\lim_{n \to \infty} r_{ij}(n) = \pi_j$$
for all initial states $i$. 

The values $\pi_j$ satisfy:
$$\pi_j \ge 0, \quad \sum_{j} \pi_j = 1$$

Intuitively, consider two independent copies of the process running under the same transition rules but launched from different initial states. Because the state space is finite, connected by a single recurrent class, and aperiodic, the random trajectories will eventually visit the same state at the same time. Once they collide, their probabilistic futures become identical. This mechanism guarantees that the chain asymptotically washes out all memory of where it began.

Convergence here is a property of the probability distribution, not the physical state: $X_n$ never freezes in place, but continues to jump between states forever.

## Balance Equations and Visit Frequencies

Taking the limit on both sides of the multi-step recursion:
$$\lim_{n \to \infty} r_{ij}(n) = \sum_k \left( \lim_{n \to \infty} r_{ik}(n-1) \right) p_{kj}$$
yields the **balance equations**:
$$\pi_j = \sum_k \pi_k p_{kj}, \quad \text{for all } j$$
along with the normalization condition:
$$\sum_j \pi_j = 1$$

Without the normalization condition $\sum_j \pi_j = 1$, the system $\pi_j = \sum_k \pi_k p_{kj}$ is singular: the all-zero vector $\pi_j = 0$ is always a solution, and the rows are linearly dependent. Adding the normalization constraint produces a unique solution.

### Visit Frequency Interpretation

The balance equations have an intuitive physical meaning based on long-run frequencies:

- $\pi_j$ represents the long-run fraction of time the chain spends at state $j$.
- In any single transition, the probability that the transition originates at state $k$ and targets state $j$ is $\pi_k p_{kj}$. This is the long-run frequency of transitions of type $k \to j$.
- Summing over all predecessors $k$, the total long-run frequency of transitions into state $j$ is $\sum_k \pi_k p_{kj}$.

Because the chain is in state $j$ at time $n$ if and only if the step at time $n$ arrived in state $j$, the frequency of being in state $j$ must equal the total frequency of transitions entering state $j$.

### A Two-State Example

Consider a two-state Markov chain with states $\{1, 2\}$ and transition probabilities:
$$p_{11} = 0.5, \quad p_{12} = 0.5, \quad p_{21} = 0.2, \quad p_{22} = 0.8$$

The chain has a single recurrent class and is aperiodic (due to the presence of self-transitions $p_{11}, p_{22} > 0$). Writing out the balance equations:
$$\pi_1 = 0.5\pi_1 + 0.2\pi_2 \implies 0.5\pi_1 = 0.2\pi_2$$
$$\pi_2 = 0.5\pi_1 + 0.8\pi_2 \implies 0.2\pi_2 = 0.5\pi_1$$

Both equations state the identical relation $5\pi_1 = 2\pi_2$. Incorporating the normalization equation:
$$\pi_1 + \pi_2 = 1 \implies \pi_1 + \frac{5}{2}\pi_1 = 1 \implies \frac{7}{2}\pi_1 = 1$$

Thus:
$$\pi_1 = \frac{2}{7}, \quad \pi_2 = \frac{5}{7}$$

After running for a large number of steps $n$, the probability that the system is in state 1 is approximately $2/7$, regardless of whether it started in state 1 or state 2.

## Birth-Death Processes

A **birth-death process** is a Markov chain on states $\{0, 1, 2, \dots, m\}$ where transitions are permitted only to adjacent states or back to the same state. From state $i$:
- Upward transition (birth): $p_{i, i+1} = p_i$
- Downward transition (death): $p_{i, i-1} = q_i$
- Self-transition: $p_{ii} = 1 - p_i - q_i$

At the boundary states, $q_0 = 0$ and $p_m = 0$.

<figure>
<svg viewBox="0 0 460 110" role="img" aria-label="State transition diagram for a birth-death process with a local balance cut between state i and state i plus 1">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- States -->
  <circle cx="60" cy="55" r="18" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="60" y="59" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <circle cx="160" cy="55" r="18" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="59" text-anchor="middle" font-size="12" fill="currentColor">1</text>
  <circle cx="260" cy="55" r="18" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="260" y="59" text-anchor="middle" font-size="12" fill="currentColor">i</text>
  <circle cx="360" cy="55" r="18" fill="none" stroke="currentColor" stroke-width="1.2"/>
  <text x="360" y="59" text-anchor="middle" font-size="12" fill="currentColor">i+1</text>

  <!-- Transitions 0 to 1 -->
  <path d="M 76 43 C 98 28, 122 28, 144 43" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="110" y="27" text-anchor="middle" font-size="11" fill="currentColor">p₀</text>
  <path d="M 144 67 C 122 82, 98 82, 76 67" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="110" y="93" text-anchor="middle" font-size="11" fill="currentColor">q₁</text>

  <!-- Dots between 1 and i -->
  <text x="210" y="59" text-anchor="middle" font-size="14" fill="currentColor">···</text>

  <!-- Transitions i to i+1 -->
  <path d="M 276 43 C 298 28, 322 28, 344 43" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="310" y="27" text-anchor="middle" font-size="11" fill="currentColor">pᵢ</text>
  <path d="M 344 67 C 322 82, 298 82, 276 67" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="310" y="93" text-anchor="middle" font-size="11" fill="currentColor">qᵢ₊₁</text>

  <!-- Cut line -->
  <line x1="310" y1="8" x2="310" y2="102" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4,4"/>
</svg>
<figcaption>Transition diagram of a birth-death process. A vertical cut separating state i from i+1 requires the upward transition rate to balance the downward transition rate.</figcaption>
</figure>

### Local Balance Equations

Instead of solving the full $(m+1) \times (m+1)$ system of global balance equations, we place a vertical boundary (or "cut") between states $i$ and $i+1$. 

Over any sample path, every time the process moves from $i$ to $i+1$, it must return from $i+1$ to $i$ before it can cross upward again. Across a long trajectory of $N$ steps, the total number of crossings from $i \to i+1$ can differ from the number of crossings from $i+1 \to i$ by at most 1. In the limit as $N \to \infty$, the long-run frequency of crossings to the right must equal the frequency of crossings to the left:
$$\pi_i p_i = \pi_{i+1} q_{i+1}, \quad i = 0, 1, \dots, m-1$$

This provides a direct one-step recurrence:
$$\pi_{i+1} = \pi_i \frac{p_i}{q_{i+1}}$$

Expressing each $\pi_i$ recursively in terms of $\pi_0$:
$$\pi_i = \pi_0 \prod_{k=0}^{i-1} \frac{p_k}{q_{k+1}}$$
Using $\sum_{i=0}^m \pi_i = 1$, we solve for $\pi_0$:
$$\pi_0 = \frac{1}{1 + \sum_{i=1}^m \prod_{k=0}^{i-1} \frac{p_k}{q_{k+1}}}$$

### Constant Transition Probabilities and Queueing

Consider the homogeneous case where the birth and death rates do not depend on the state:
$$p_i = p \quad \text{and} \quad q_i = q \quad \text{for all interior states}$$

We define the **load factor** (or traffic intensity) as:
$$\rho = \frac{p}{q}$$

The local balance equations simplify to:
$$\pi_{i+1} = \rho \pi_i \implies \pi_i = \pi_0 \rho^i, \quad i = 0, 1, \dots, m$$

Using the normalization condition:
$$\sum_{i=0}^m \pi_i = \pi_0 \sum_{i=0}^m \rho^i = 1 \implies \pi_0 = \frac{1}{\sum_{i=0}^m \rho^i}$$

Two important cases arise:

1. **Symmetric Random Walk ($\rho = 1$):**
   When $p = q$, the chain has no drift in either direction:
   $$\pi_0 = \frac{1}{m+1} \implies \pi_i = \frac{1}{m+1} \quad \text{for all } i = 0, 1, \dots, m$$
   In the long run, the process is equally likely to be in any state.

2. **Infinite Buffer with Drift Toward Zero ($\rho < 1, m \to \infty$):**
   When the capacity is unbounded ($m \to \infty$) and arrivals occur slower than service ($p < q$, so $\rho < 1$), the geometric series converges:
   $$\sum_{i=0}^\infty \rho^i = \frac{1}{1 - \rho}$$
   Therefore:
   $$\pi_0 = 1 - \rho$$
   and the steady-state distribution is:
   $$\pi_i = (1 - \rho)\rho^i, \quad i = 0, 1, 2, \dots$$

This is a shifted geometric PMF (supported on $\{0, 1, 2, \dots\}$ rather than starting at 1). Under this distribution, the expected number of customers in the system in steady state is:
$$\mathbf{E}[X] = \sum_{i=0}^\infty i \pi_i = (1 - \rho) \sum_{i=0}^\infty i \rho^i = (1 - \rho) \frac{\rho}{(1 - \rho)^2} = \frac{\rho}{1 - \rho}$$

As the load factor approaches 1 from below (e.g., $\rho = 0.99$), the expected queue length grows without bound ($\mathbf{E}[X] \to \infty$).

## Exercises

### Exercise 1: Dual-Stream Examination Responses

Iwana Passe is taking an exam with an infinite number of questions. Independently, her conscious and subconscious faculties generate answers in a Poisson manner:
- Conscious responses arrive at rate $\lambda_c$ per minute; each is correct with probability $p_c$, independently.
- Subconscious responses arrive at rate $\lambda_s$ per minute; each is correct with probability $p_s$, independently.
Assume $\lambda_c \neq \lambda_s$, that both faculties always work on different questions, and that response recording time is negligible.

1. Find the probability mass function $p_K(k)$ of the number of conscious responses generated in an interval of $T$ minutes.
2. For an arbitrary question answered by Iwana, determine the probability that the answer:
   - Represents a conscious response.
   - Represents a conscious correct response.
3. For a given time window of $T$ minutes, find the probability that she records exactly $r$ conscious responses and $s$ subconscious responses.
4. Let $X$ be the time from the start of the exam until she makes her first conscious response that was preceded by at least one subconscious response. Find the probability density function of $X$.

### Exercise 2: Patrolling and Radio Calls

Shem drives between intersections with independent driving times, each exponentially distributed with parameter $\lambda$. At each intersection, he reports an accident with probability $p$. Independently, he receives brief radio calls modeled as a Poisson process with rate $\mu$ calls per hour.

1. Find the PMF of $N$, the number of intersections Shem visits up to and including the one where he reports his first accident.
2. Determine the PDF of $Q$, the total driving time between two consecutive reported accidents.
3. Find the PMF of $M$, the number of accidents Shem reports during a two-hour window.
4. Find the PMF of $K$, the number of accidents reported between two successive radio calls.
5. Observing Shem at a random instant long after his shift begins, let $W$ be the total elapsed time between his last radio call and his next radio call. Determine the PDF of $W$.

### Exercise 3: Random Incidence in an Erlang Process

Consider an arrival process where interarrival times are independent Erlang random variables of order 2, with mean $2/\lambda$. The process has been running for a very long time. An observer inspects the system at a fixed time $t$. Find the PDF of the total length of the interarrival interval containing $t$.

## Sources

- Slides 1–6 and Transcript [00:00]–[11:20]: Markov chain fundamentals, multi-step recursion, path probability calculations, and computational complexity of path enumeration.
- Slides 7–9 and Transcript [11:20]–[18:40]: Recurrence, transience, recurrent classes, trapping behavior, and definition/checks for periodicity.
- Slides 10–12 and Transcript [18:40]–[33:49]: Steady-state convergence theorem, balance equations, visit frequency interpretation, and the two-state Markov chain example.
- Slides 13–14 and Transcript [33:49]–[50:40]: Birth-death processes, local balance equations across cuts, load factor $\rho$, symmetric random walks, and infinite-capacity queueing derivations ($\pi_0 = 1-\rho$, $\mathbf{E}[X] = \rho/(1-\rho)$).
- Recitation 17 Problems: Exercises 1, 2, and 3. Note that while Lecture 17 covered Markov chains, the recitation material focused on Poisson processes, merging/splitting, and renewal random incidence.

Solutions: [chapter 17](solutions/17-steady-state-behavior-of-markov-chains.md)


---

[← 16. Discrete-Time Markov Chains](16-discrete-time-markov-chains.md) · [Contents](index.md) · [18. Markov Chain Dynamics and Absorption →](18-markov-chain-dynamics-and-absorption.md)
