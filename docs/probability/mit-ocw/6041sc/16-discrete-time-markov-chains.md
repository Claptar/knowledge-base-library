---
title: "16. Discrete-Time Markov Chains"
course: "MIT 6.041SC"
chapter: 16
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 16. Discrete-Time Markov Chains

## What this covers

This chapter introduces discrete-time, finite-state Markov chains, a foundational framework for modeling random processes where future states depend on the past solely through the present. We define the Markov property, develop the Chapman-Kolmogorov recursions for multi-step transition probabilities, and examine the long-term behavior of chains through state classification into transient and recurrent classes.

## The State of a System and the Markov Property

In physics, deterministic equations of motion take the form $\text{state}(t + \Delta t) = f(\text{state}(t))$. For example, knowing the position of a flying projectile alone is insufficient to predict where it lands; knowing both position and velocity constitutes a complete state, rendering past positions irrelevant to future predictions.

A Markov process extends this concept to systems evolving under randomness. The current state summarizes all past history that is relevant for forecasting the future.

### Motivating Example: A Supermarket Checkout Counter

Consider a supermarket queue where customers arrive and are served in discrete time intervals $n = 0, 1, 2, \ldots$:
- **Arrivals:** At each time step, a customer arrives with probability $p$, corresponding to a Bernoulli process with parameter $p$ (and geometric interarrival times).
- **Service times:** If at least one customer is in the store, the clerk completes service for the current customer with probability $q$ in that time step. Service duration is geometrically distributed with parameter $q$.
- **Independence:** The coin tosses determining arrivals and departures are independent across time and independent of each other.
- **Capacity:** The store holds at most $10$ customers.

Let $X_n \in \{0, 1, \ldots, 10\}$ denote the number of customers in the system at time $n$. For any interior state $i \in \{1, 2, \ldots, 9\}$, the state transition from time $n$ to $n+1$ depends on the coin flips occurring during step $n$:
- **Upward transition ($i \to i + 1$):** An arrival occurs with no departure, which happens with probability $p(1 - q)$.
- **Downward transition ($i \to i - 1$):** A departure occurs with no arrival, with probability $(1 - p)q$.
- **Self-transition ($i \to i$):** Either both an arrival and a departure occur, or neither occurs, having combined probability $pq + (1 - p)(1 - q)$.

At the boundary states, physical constraints alter the probabilities:
- At state $0$, departures cannot occur. The chain transitions to state $1$ with probability $p$, and remains at $0$ with probability $1 - p$.
- At state $10$, the store is full, preventing further arrivals. The chain drops to state $9$ with probability $q$, and remains at $10$ with probability $1 - q$.

Because $X_n$ captures all information about current occupancy, past occupancy patterns give no additional predictive power.

### Formal Definition of a Markov Chain

Let $X_n$ denote the state of a system at integer time steps $n = 0, 1, 2, \ldots$, taking values in a finite set of states $\mathcal{S} = \{1, 2, \ldots, m\}$.

A sequence of random variables $\{X_n\}$ is a **Markov chain** if it satisfies the **Markov property**:
$$p_{ij} = \mathbf{P}(X_{n+1} = j \mid X_n = i) = \mathbf{P}(X_{n+1} = j \mid X_n = i, X_{n-1} = i_{n-1}, \ldots, X_0 = i_0)$$
for all times $n$, all current and next states $i, j \in \mathcal{S}$, and all possible past trajectories $i_0, \ldots, i_{n-1}$.

The transition probabilities satisfy:
$$p_{ij} \ge 0, \quad \sum_{j=1}^m p_{ij} = 1 \quad \text{for each state } i.$$

Specifying a discrete-time Markov chain requires:
1. Identifying the state space $\mathcal{S}$.
2. Identifying the directed transitions between states.
3. Specifying the numerical transition probabilities $p_{ij}$.

## Multi-Step Transition Probabilities

To make probabilistic predictions over a horizon of $n$ transitions, define the **$n$-step transition probability**:
$$r_{ij}(n) = \mathbf{P}(X_n = j \mid X_0 = i).$$

By definition:
$$r_{ij}(0) = \begin{cases} 1, & \text{if } i = j, \\ 0, & \text{if } i \neq j, \end{cases} \qquad r_{ij}(1) = p_{ij}.$$

### Chapman-Kolmogorov Recursions

To reach state $j$ at time $n$ starting from state $i$ at time $0$, the chain must occupy some intermediate state $k \in \{1, \ldots, m\}$ at time $n-1$.

<figure>
<svg viewBox="0 0 460 170" role="img" aria-label="Decomposition of paths from state i to state j through intermediate state k at time n-1">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Time 0 -->
  <circle cx="50" cy="85" r="16" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="50" y="89" text-anchor="middle" font-size="12" fill="currentColor">i</text>
  <text x="50" y="125" text-anchor="middle" font-size="11" fill="currentColor">time 0</text>

  <!-- Time n-1 states -->
  <circle cx="230" cy="35" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="230" y="39" text-anchor="middle" font-size="11" fill="currentColor">1</text>

  <circle cx="230" cy="85" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="230" y="89" text-anchor="middle" font-size="11" fill="currentColor">k</text>

  <circle cx="230" cy="135" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="230" y="139" text-anchor="middle" font-size="11" fill="currentColor">m</text>
  <text x="230" y="165" text-anchor="middle" font-size="11" fill="currentColor">time n-1</text>

  <!-- Time n state -->
  <circle cx="410" cy="85" r="16" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="410" y="89" text-anchor="middle" font-size="12" fill="currentColor">j</text>
  <text x="410" y="125" text-anchor="middle" font-size="11" fill="currentColor">time n</text>

  <!-- Transitions from i to intermediate states -->
  <path d="M 66 80 C 120 50, 160 35, 216 35" fill="none" stroke="currentColor" stroke-dasharray="3 3" stroke-width="1.2" marker-end="url(#arrow)"/>
  <path d="M 66 85 L 214 85" fill="none" stroke="currentColor" stroke-dasharray="3 3" stroke-width="1.2" marker-end="url(#arrow)"/>
  <path d="M 66 90 C 120 120, 160 135, 216 135" fill="none" stroke="currentColor" stroke-dasharray="3 3" stroke-width="1.2" marker-end="url(#arrow)"/>

  <!-- Path label -->
  <text x="135" y="75" text-anchor="middle" font-size="11" fill="currentColor">r_{ik}(n-1)</text>

  <!-- Single step transitions from intermediate to j -->
  <path d="M 244 35 C 300 35, 340 50, 394 80" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 244 85 L 394 85" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <path d="M 244 135 C 300 135, 340 120, 394 90" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Single step label -->
  <text x="325" y="75" text-anchor="middle" font-size="11" fill="currentColor">p_{kj}</text>
</svg>
<figcaption>Conditioning on the state occupied at time $n-1$ to compute the $n$-step transition probability $r_{ij}(n)$.</figcaption>
</figure>

By applying the Total Probability Theorem and conditioning on the state $X_{n-1}$:
$$r_{ij}(n) = \sum_{k=1}^m \mathbf{P}(X_{n-1} = k \mid X_0 = i) \mathbf{P}(X_n = j \mid X_{n-1} = k, X_0 = i).$$

By the Markov property, conditional on $X_{n-1} = k$, the past state $X_0 = i$ provides no extra information about $X_n$. Hence $\mathbf{P}(X_n = j \mid X_{n-1} = k, X_0 = i) = p_{kj}$, leading to the recursion:
$$r_{ij}(n) = \sum_{k=1}^m r_{ik}(n-1) p_{kj}.$$

Alternatively, by conditioning on the state reached after the very first step, $X_1 = k$:
$$r_{ij}(n) = \sum_{k=1}^m p_{ik} r_{kj}(n-1).$$

When the initial state is selected according to a probability distribution $\mathbf{P}(X_0 = i)$, the unconditional probability of occupying state $j$ at time $n$ is:
$$\mathbf{P}(X_n = j) = \sum_{i=1}^m \mathbf{P}(X_0 = i) r_{ij}(n).$$

### A Two-State Numerical Example

Consider a chain with states $\{1, 2\}$ and transition probabilities:
$$p_{11} = 0.5, \quad p_{12} = 0.5, \quad p_{21} = 0.2, \quad p_{22} = 0.8.$$

<figure>
<svg viewBox="0 0 340 130" role="img" aria-label="Two-state Markov chain transition diagram">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- State 1 -->
  <circle cx="80" cy="65" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="80" y="70" text-anchor="middle" font-size="13" fill="currentColor">1</text>
  <!-- State 2 -->
  <circle cx="260" cy="65" r="18" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="260" y="70" text-anchor="middle" font-size="13" fill="currentColor">2</text>

  <!-- Self loops -->
  <path d="M 66 54 C 45 25, 45 105, 66 76" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <text x="28" y="69" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>

  <path d="M 274 54 C 295 25, 295 105, 274 76" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <text x="312" y="69" text-anchor="middle" font-size="11" fill="currentColor">0.8</text>

  <!-- Cross transitions -->
  <path d="M 97 55 C 145 40, 195 40, 243 55" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <text x="170" y="40" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>

  <path d="M 243 75 C 195 90, 145 90, 97 75" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow2)"/>
  <text x="170" y="105" text-anchor="middle" font-size="11" fill="currentColor">0.2</text>
</svg>
<figcaption>Transition diagram for a two-state Markov chain.</figcaption>
</figure>

The recursion for $r_{11}(n)$ is:
$$r_{11}(n) = r_{11}(n-1) p_{11} + r_{12}(n-1) p_{21} = 0.5 \, r_{11}(n-1) + 0.2 \, r_{12}(n-1).$$
Since the chain must be in either state $1$ or state $2$, $r_{12}(n) = 1 - r_{11}(n)$.

Evaluating step by step starting from state $1$:
- $n = 0$: $r_{11}(0) = 1$, $r_{12}(0) = 0$.
- $n = 1$: $r_{11}(1) = 0.5$, $r_{12}(1) = 0.5$.
- $n = 2$: $r_{11}(2) = (0.5)(0.5) + (0.5)(0.2) = 0.25 + 0.10 = 0.35$, $r_{12}(2) = 0.65$.

Iterating further reveals that as $n$ grows, the probabilities converge to stationary values:
$$r_{11}(n) \to \frac{2}{7} \approx 0.2857, \qquad r_{12}(n) \to \frac{5}{7} \approx 0.7143.$$

Starting from state $2$, a parallel calculation produces:
$$r_{21}(0) = 0, \quad r_{22}(0) = 1; \qquad r_{21}(1) = 0.2, \quad r_{22}(1) = 0.8; \qquad r_{21}(2) = 0.26, \quad r_{22}(2) = 0.74.$$
As $n \to \infty$, these also converge to:
$$r_{21}(n) \to \frac{2}{7}, \qquad r_{22}(n) \to \frac{5}{7}.$$

Once the occupancy probabilities equal $2/7$ and $5/7$, applying the recursion preserves them:
$$\left(\frac{2}{7}\right)(0.5) + \left(\frac{5}{7}\right)(0.2) = \frac{1}{7} + \frac{1}{7} = \frac{2}{7}.$$

This illustrates two key behaviors:
1. **Convergence:** The probabilities $r_{ij}(n)$ approach steady-state values. The random variable $X_n$ does not freeze; transitions between states occur indefinitely, but the *probability distribution* over states stabilizes.
2. **Loss of initial conditions:** The limiting probability of occupying a state does not depend on the starting state:
   $$\lim_{n \to \infty} r_{11}(n) = \lim_{n \to \infty} r_{21}(n) = \frac{2}{7}.$$
State $2$ has a higher limiting probability ($5/7$) than state $1$ ($2/7$) because it is more "sticky"—the probability of remaining in state $2$ on any step is $0.8$, whereas the chain leaves state $1$ with probability $0.5$.

## Convergence and Chain Structure

The favorable convergence properties shown above do not hold for all Markov chains. Two main structural obstacles can alter or prevent convergence: periodicity and multiple absorbing/recurrent structures.

### Periodic Behavior

Consider a chain with three states $\{1, 2, 3\}$ where state $2$ transitions to states $1$ and $3$ each with probability $0.5$, while states $1$ and $3$ transition back to state $2$ with probability $1$.

<figure>
<svg viewBox="0 0 320 130" role="img" aria-label="Periodic three-state Markov chain">
  <defs>
    <marker id="arrow3" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <circle cx="60" cy="65" r="16" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="70" text-anchor="middle" font-size="12" fill="currentColor">1</text>

  <circle cx="160" cy="65" r="16" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="70" text-anchor="middle" font-size="12" fill="currentColor">2</text>

  <circle cx="260" cy="65" r="16" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="260" y="70" text-anchor="middle" font-size="12" fill="currentColor">3</text>

  <!-- 2 to 1 and 1 to 2 -->
  <path d="M 144 55 C 120 40, 100 40, 76 55" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <text x="110" y="40" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>

  <path d="M 76 75 C 100 90, 120 90, 144 75" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="currentColor">1</text>

  <!-- 2 to 3 and 3 to 2 -->
  <path d="M 176 55 C 200 40, 220 40, 244 55" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <text x="210" y="40" text-anchor="middle" font-size="11" fill="currentColor">0.5</text>

  <path d="M 244 75 C 220 90, 200 90, 176 75" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow3)"/>
  <text x="210" y="105" text-anchor="middle" font-size="11" fill="currentColor">1</text>
</svg>
<figcaption>A periodic chain alternating deterministically between state 2 and the set {1, 3}.</figcaption>
</figure>

Starting from state $2$:
- After any odd number of steps ($n = 1, 3, 5, \ldots$), the chain is either at state $1$ or state $3$. Thus $r_{22}(n) = 0$.
- After any even number of steps ($n = 0, 2, 4, \ldots$), the chain must return to state $2$. Thus $r_{22}(n) = 1$.

The sequence $r_{22}(n)$ oscillates indefinitely between $0$ and $1$, failing to converge. Determining $r_{22}(n)$ requires checking the parity of time $n$.

### Multiple Communicating Structures

Consider a four-state chain where:
- State $1$ is absorbing: $p_{11} = 1$.
- State $2$ can transition to state $1$ with probability $0.5$, or to state $3$ with probability $0.5$.
- States $3$ and $4$ transition back and forth to each other ($p_{34} = 1$, $p_{43} = 1$).

Starting in different states yields fundamentally different long-term behavior:
- Starting from state $1$, the chain cannot leave: $r_{11}(n) = 1$ for all $n$, so $\lim_{n \to \infty} r_{11}(n) = 1$.
- Starting from state $3$, the chain oscillates between states $3$ and $4$, with no path to state $1$: $r_{31}(n) = 0$ for all $n$, so $\lim_{n \to \infty} r_{31}(n) = 0$.
- Starting from state $2$, the chain eventually leaves state $2$. By symmetry, it has equal probability $1/2$ of moving to state $1$ or to the $\{3, 4\}$ subsystem. Hence for large $n$:
  $$r_{21}(n) \to \frac{1}{2}.$$

Here, limits exist, but the long-term probabilities depend heavily on the initial state because some states cannot reach others.

## Classification of States

To understand chain behavior systematically, we classify states by whether the process can always return to them.

### Recurrent and Transient States

- **Accessible / Reachable:** A state $j$ is accessible from state $i$ if there is a positive-probability path from $i$ to $j$ in some number of steps ($r_{ij}(n) > 0$ for some $n \ge 0$).
- **Recurrent State:** A state $i$ is **recurrent** if, starting from $i$, wherever the chain can go, there is a path to return to $i$. Formally, for every state $j$ accessible from $i$, state $i$ is accessible from $j$.
- **Transient State:** A state $i$ is **transient** if it is not recurrent. That is, there is at least one state $j$ accessible from $i$ from which returning to $i$ is impossible.

If a state $i$ is transient, every time the chain visits $i$, there is a strictly positive probability of transitioning into a region of the state space from which $i$ is unreachable. Consequently:
- A transient state $i$ is visited only a finite number of times with probability $1$.
- As the number of transitions grows, the occupancy probability vanishes:
  $$\lim_{n \to \infty} \mathbf{P}(X_n = i) = 0.$$

Eventually, a finite-state Markov chain leaves all transient states permanently and enters a recurrent set.

### Recurrent Classes

A **recurrent class** is a non-empty set of recurrent states $C$ such that:
1. Every state in $C$ communicates with every other state in $C$ (each is accessible from the other).
2. No state outside $C$ is accessible from any state inside $C$.

Once the chain enters a recurrent class, it remains within that class indefinitely.

<figure>
<svg viewBox="0 0 460 210" role="img" aria-label="Markov chain state diagram illustrating transient states and two distinct recurrent classes">
  <defs>
    <marker id="arrow4" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>

  <!-- Recurrent Class 1 Shading -->
  <rect x="25" y="70" width="70" height="70" rx="10" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-dasharray="2 2"/>
  <text x="60" y="60" text-anchor="middle" font-size="11" fill="currentColor">Class R₁</text>

  <!-- State 5 (Absorbing) -->
  <circle cx="60" cy="105" r="15" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="60" y="109" text-anchor="middle" font-size="12" fill="currentColor">5</text>
  <path d="M 45 105 C 28 85, 28 125, 45 105" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- Transient Region Shading -->
  <rect x="145" y="30" width="170" height="150" rx="10" fill="currentColor" fill-opacity="0.08" stroke="currentColor" stroke-dasharray="2 2"/>
  <text x="230" y="22" text-anchor="middle" font-size="11" fill="currentColor">Transient States</text>

  <!-- Transient States: 1, 2, 3, 4 -->
  <circle cx="180" cy="65" r="15" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="69" text-anchor="middle" font-size="12" fill="currentColor">1</text>

  <circle cx="280" cy="65" r="15" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="280" y="69" text-anchor="middle" font-size="12" fill="currentColor">2</text>

  <circle cx="180" cy="145" r="15" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="149" text-anchor="middle" font-size="12" fill="currentColor">3</text>

  <circle cx="280" cy="145" r="15" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="280" y="149" text-anchor="middle" font-size="12" fill="currentColor">4</text>

  <!-- Internal Transient Transitions -->
  <path d="M 195 65 L 263 65" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>
  <path d="M 280 80 L 280 128" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>
  <path d="M 265 145 L 197 145" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>
  <path d="M 180 130 L 180 82" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>

  <!-- Exit to Class 1 -->
  <path d="M 165 65 C 120 65, 100 85, 77 100" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- Recurrent Class 2 Shading -->
  <rect x="365" y="30" width="70" height="150" rx="10" fill="currentColor" fill-opacity="0.15" stroke="currentColor" stroke-dasharray="2 2"/>
  <text x="400" y="22" text-anchor="middle" font-size="11" fill="currentColor">Class R₂</text>

  <!-- Recurrent States: 6, 7, 8 -->
  <circle cx="400" cy="55" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="400" y="59" text-anchor="middle" font-size="11" fill="currentColor">6</text>

  <circle cx="400" cy="105" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="400" y="109" text-anchor="middle" font-size="11" fill="currentColor">7</text>

  <circle cx="400" cy="155" r="14" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="400" y="159" text-anchor="middle" font-size="11" fill="currentColor">8</text>

  <!-- Exit to Class 2 -->
  <path d="M 295 145 L 384 112" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow4)"/>

  <!-- Class 2 Internal Transitions -->
  <path d="M 393 68 L 393 91" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>
  <path d="M 407 91 L 407 68" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>
  <path d="M 393 118 L 393 141" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>
  <path d="M 407 141 L 407 118" fill="none" stroke="currentColor" stroke-width="1.2" marker-end="url(#arrow4)"/>
</svg>
<figcaption>Classification of states into transient states {1, 2, 3, 4} and two disconnected recurrent classes: $R_1 = \{5\}$ and $R_2 = \{6, 7, 8\}$.</figcaption>
</figure>

In this decomposition:
- **Transient states $\{1, 2, 3, 4\}$:** Paths exist leading to state $5$ and to the set $\{6, 7, 8\}$, but there are no returning paths from those destinations.
- **Recurrent class $R_1 = \{5\}$:** State $5$ can transition only to itself. Once reached, the chain remains there permanently.
- **Recurrent class $R_2 = \{6, 7, 8\}$:** States $6, 7,$ and $8$ communicate with one another, but cannot reach any state outside $R_2$.

Because $R_1$ and $R_2$ do not communicate, the long-term behavior depends fundamentally on the starting state:
- Starting in $R_1$, the probability of ending up in $R_1$ is $1$.
- Starting in $R_2$, the probability of ending up in $R_1$ is $0$.
- Starting in the transient set, the chain will eventually enter either $R_1$ or $R_2$ with positive probabilities, after which it remains trapped in that recurrent class forever.

For a chain to have a unique limiting distribution that is completely independent of the starting state, it must contain exactly one recurrent class and have no periodic structure.

## Exercises

### Exercise 16.1

A two-stage random process operates as follows:
1. A fair four-sided die with faces labeled $\{0, 1, 2, 3\}$ is rolled, resulting in an outcome $N$ distributed uniformly over $\{0, 1, 2, 3\}$.
2. Conditional on the value of $N$, a fair coin is tossed $N$ times. Let $K$ denote the total number of heads observed from these coin tosses (with $K = 0$ if $N = 0$).

(a) Specify the probability mass function (PMF) $p_N(n)$ of the die roll $N$.

(b) Find the joint PMF $p_{N, K}(n, k)$ for all valid pairs $(n, k)$.

(c) Determine the conditional PMF of the number of heads given that the die showed $2$, that is, $p_{K \mid N}(k \mid 2)$.

(d) Determine the conditional PMF of the die outcome given that exactly two heads were obtained, that is, $p_{N \mid K}(n \mid 2)$.

## Sources

- **Lecture 16 Slides and Transcript:** Introduction of discrete-time Markov chains; checkout counter model; definition of the Markov property and transition probabilities; forward and backward Chapman-Kolmogorov recursions for $r_{ij}(n)$; two-state convergence example; failure of convergence due to periodicity; dependence on initial conditions; classification of states into transient and recurrent; recurrent classes.
- **Problem Video ("No 16 ch1 flipcoinrandomnumber"):** Exercise 16.1 on the hierarchical model involving a four-sided die roll followed by conditionally independent coin tosses.

---

[← 15. Poisson Processes: Merging, Splitting, and Random Incidence](15-poisson-processes-merging-splitting-and-random-incidence.md) · [Contents](index.md) · [17. Steady-State Behavior of Markov Chains →](17-steady-state-behavior-of-markov-chains.md)
