---
title: "18. Markov Chain Dynamics and Absorption"
course: "MIT 6.041SC"
chapter: 18
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 18. Markov Chain Dynamics and Absorption

## What this covers

This chapter examines the long-run and transient behavior of discrete-time Markov chains. We apply steady-state analysis to queueing dimensioning through the classic Erlang phone system problem, and develop first-step analysis to compute absorption probabilities, expected times to absorption, and mean first passage times. The chapter assumes familiarity with discrete-time Markov chains, transition probabilities, and steady-state balance equations.

## Long-Run Behavior and Mixing Time

Recall that for a discrete-time Markov chain consisting of transient states and a single recurrent class that is aperiodic, the $n$-step transition probabilities converge to a unique steady-state distribution:

$$\lim_{n\to\infty} r_{ij}(n) = \lim_{n\to\infty} P(X_n = j \mid X_0 = i) = \pi_j$$

The limiting probability $\pi_j$ is independent of the initial state $i$. If the initial state is selected according to some initial distribution, applying the total probability theorem yields the same limit for the unconditional probability $P(X_n = j)$. In the limit as $n \to \infty$, the state $X_n$ becomes independent of the initial state $X_0$.

The steady-state probabilities $\pi_1, \dots, \pi_m$ are obtained as the unique solution to the balance equations together with the normalization equation:

$$\pi_j = \sum_k \pi_k p_{kj}, \quad j = 1, \dots, m, \qquad \sum_{j=1}^m \pi_j = 1$$

Each product $\pi_k p_{kj}$ represents the probability frequency of transitions from state $k$ to state $j$. Summing over all $k$ expresses the principle of conservation of probability flow: the rate at which probability enters state $j$ equals the rate $\pi_j$ at which the chain is found in state $j$.

### Multiple Recurrent Classes

When a Markov chain contains multiple recurrent classes, the long-run distribution depends on which class traps the chain. Once the chain enters a specific recurrent class, it never leaves. Conditional on entering that class, its long-run statistics are governed entirely by the steady-state probabilities computed for that isolated sub-chain. 

If the process begins in a transient state, it will eventually transition into one of the recurrent classes. Determining which class traps the process is probabilistic and requires calculating absorption probabilities.

### Approximations Using Steady-State Probabilities

When the number of elapsed steps $n$ is large, steady-state probabilities provide practical approximations for joint event probabilities. Consider a two-state chain with states $\{1, 2\}$ and known steady-state probabilities $\pi_1 = 2/7$ and $\pi_2 = 5/7$. 

If the chain starts at state 1 ($X_0 = 1$):

1. The joint probability $P(X_1 = 1, X_{100} = 1 \mid X_0 = 1)$ expands as:
   $$P(X_1 = 1 \mid X_0 = 1) P(X_{100} = 1 \mid X_1 = 1, X_0 = 1) = p_{11} r_{11}(99)$$
   By the Markov property, conditioning on $X_1 = 1$ renders past states irrelevant. For large $n = 99$, $r_{11}(99) \approx \pi_1$, yielding:
   $$P(X_1 = 1, X_{100} = 1 \mid X_0 = 1) \approx p_{11} \pi_1$$

2. Similarly, the probability $P(X_{100} = 1, X_{101} = 2 \mid X_0 = 1)$ is:
   $$P(X_{100} = 1 \mid X_0 = 1) P(X_{101} = 2 \mid X_{100} = 1) = r_{11}(100) p_{12} \approx \pi_1 p_{12}$$

3. Over even wider separations, such as $P(X_{100} = 1, X_{200} = 1 \mid X_0 = 1)$:
   $$r_{11}(100) r_{11}(100) \approx \pi_1 \cdot \pi_1$$

### Time Scale and Mixing

The validity of setting $r_{ij}(n) \approx \pi_j$ depends directly on the *mixing time* of the chain—the number of transitions required for the process to forget its initial state. 

Consider two contrasting transition structures:
* If self-loop probabilities are moderate (for example, transitions out of a state occur with probability $0.2$ or $0.5$), the chain switches states every few steps. Over $n = 100$ steps, substantial mixing occurs, and $r_{ij}(100) \approx \pi_j$ is an accurate approximation.
* If $p_{11} = 0.999$ and $p_{22} = 0.998$, the probability of leaving state 1 on any step is only $0.001$. On average, the chain requires $1/0.001 = 1{,}000$ steps just to exit state 1. Over $n = 100$ steps, the process remains trapped in its initial state with high probability. Here, the time scale is slow, and $n$ would need to be on the order of $10{,}000$ before the steady-state approximation applies.

## Dimensioning a Phone System: The Erlang Problem

A classic application of Markov chains is the dimensioning of telecommunication systems, originally formulated and solved by A. K. Erlang. 

Suppose a community generates telephone calls according to a Poisson process with arrival rate $\lambda$. Each call has an independently and exponentially distributed duration with parameter $\mu$ (mean duration $1/\mu$). The system provides $B$ parallel telephone lines. If a call arrives when all $B$ lines are busy, the call is blocked and lost. The engineering objective is to choose $B$ small enough to control installation costs, but large enough that the probability of a call being blocked remains below a specified tolerance (such as $1\%$).

### Discrete-Time Formulation

We discretize the continuous time axis into tiny intervals of length $\delta > 0$, where $\delta$ is sufficiently small that the probability of more than one event (arrival or termination) occurring within a single slot is of order $O(\delta^2)$ and can be neglected.

Define the state $X_n \in \{0, 1, 2, \dots, B\}$ to be the number of active telephone lines (busy circuits) during time slot $n$:
* **Call arrivals:** In any interval $\delta$, the probability of a new call arriving is $\lambda \delta$. If $i < B$, this shifts the state from $i$ to $i+1$.
* **Call terminations:** If $i$ calls are active simultaneously, each call terminates independently with probability $\mu \delta$. The aggregate probability that one of the $i$ calls terminates is $i \mu \delta$ (equivalent to the superposition of $i$ independent Poisson processes of rate $\mu$). This shifts the state from $i$ down to $i-1$.
* **Self-transitions:** With probability $1 - \lambda \delta - i\mu \delta$, no arrival or departure occurs, and the state remains at $i$.

<figure>
<svg viewBox="0 0 540 140" role="img" aria-label="State transition diagram for the Erlang phone system model">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- States -->
  <circle cx="50" cy="70" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="50" y="75" text-anchor="middle" font-size="13" fill="currentColor">0</text>
  
  <circle cx="160" cy="70" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="160" y="75" text-anchor="middle" font-size="13" fill="currentColor">1</text>
  
  <circle cx="270" cy="70" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="270" y="75" text-anchor="middle" font-size="12" fill="currentColor">i-1</text>
  
  <circle cx="380" cy="70" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="380" y="75" text-anchor="middle" font-size="13" fill="currentColor">i</text>
  
  <circle cx="490" cy="70" r="22" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <text x="490" y="75" text-anchor="middle" font-size="13" fill="currentColor">B</text>

  <!-- Forward transitions -->
  <path d="M 70 58 Q 105 38 138 58" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="105" y="42" text-anchor="middle" font-size="11" fill="currentColor">λδ</text>
  
  <path d="M 182 70 L 225 70" fill="none" stroke="currentColor" stroke-dasharray="3,3" stroke-width="1.5"/>
  <path d="M 225 70 L 246 70" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <path d="M 290 58 Q 325 38 358 58" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="325" y="42" text-anchor="middle" font-size="11" fill="currentColor">λδ</text>

  <path d="M 402 70 L 445 70" fill="none" stroke="currentColor" stroke-dasharray="3,3" stroke-width="1.5"/>
  <path d="M 445 70 L 466 70" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>

  <!-- Backward transitions -->
  <path d="M 140 82 Q 105 102 72 82" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="105" y="106" text-anchor="middle" font-size="11" fill="currentColor">μδ</text>

  <path d="M 360 82 Q 325 102 292 82" fill="none" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="325" y="106" text-anchor="middle" font-size="11" fill="currentColor">iμδ</text>
</svg>
<figcaption>Birth-death transition structure for the $B$-line telephone system model.</figcaption>
</figure>

### Solving the Detailed Balance Equations

This system has a birth-death structure. Equating probability flow across a vertical cut placed between states $i-1$ and $i$:

$$\lambda \delta \pi_{i-1} = i \mu \delta \pi_i$$

Canceling $\delta$ yields the recurrence:

$$\lambda \pi_{i-1} = i \mu \pi_i \implies \pi_i = \frac{\lambda}{i\mu} \pi_{i-1}$$

Repeated substitution from state 0 gives:

$$\pi_i = \pi_0 \frac{\lambda^i}{\mu^i i!}, \quad i = 0, 1, \dots, B$$

To determine $\pi_0$, enforce normalization $\sum_{i=0}^B \pi_i = 1$:

$$\pi_0 = \frac{1}{\sum_{i=0}^B \dfrac{\lambda^i}{\mu^i i!}}$$

The probability that an arriving call is blocked equals the steady-state probability that all lines are in use, $\pi_B$:

$$\pi_B = \frac{\dfrac{\lambda^B}{\mu^B B!}}{\sum_{i=0}^B \dfrac{\lambda^i}{\mu^i i!}}$$

This relation is known as the **Erlang B formula**.

### Numerical Design Example

Suppose telephone calls arrive at rate $\lambda = 30\text{ calls/minute}$, and the mean duration of a call is $1/\mu = 3\text{ minutes}$ ($\mu = 1/3$).

On average, the traffic offered to the system is:
$$\frac{\lambda}{\mu} = 30 \times 3 = 90\text{ calls}$$

If the system had an infinite number of lines, the expected number of concurrently active calls would be 90. Provisioning exactly $B = 90$ lines, however, would result in frequent call blocking due to statistical fluctuations. To achieve a blocking probability $\pi_B \le 0.01$ (a 1% blocking threshold), numerical evaluation of the Erlang B formula reveals that $B \approx 106$ lines are required. The extra 16 lines serve as a safety margin against random surges in demand.

## Absorption Probabilities

In chains containing transient states and two or more recurrent classes (or absorbing states), we seek the probability that the process settles into a specific absorbing target.

Let the chain have absorbing states (or absorbing recurrent sets). We designate one particular absorbing state (or absorbing set) as state $s^*$. Define the absorption probability:

$$a_i = P(\text{process eventually enters } s^* \mid X_0 = i)$$

To find $a_i$, we use **first-step analysis**: condition on the destination of the very first transition out of state $i$.

1. **Boundary conditions:**
   * If the chain is already in the target state: $a_{s^*} = 1$.
   * If the chain starts in any other absorbing state $k \neq s^*$: $a_k = 0$.

2. **Transient states:**
   For any transient state $i$, by the total probability theorem:
   $$a_i = \sum_{j} P(X_1 = j \mid X_0 = i) P(\text{eventually enters } s^* \mid X_1 = j) = \sum_j p_{ij} a_j$$

This yields a system of linear equations in the unknowns $\{a_i\}$ for all transient states $i$. This linear system always possesses a unique solution.

### Aggregating Absorbing Sets

When a recurrent class contains multiple states, we do not need to analyze the internal dynamics of that class. Because the chain can never escape the class once entered, the entire recurrent class functions as a single absorbing entity. The probability of transitioning from a transient state $i$ into that class is the sum of the transition probabilities from $i$ to all individual states in the class.

## Expected Time to Absorption

Suppose state $s^*$ is an absorbing state, and from any transient state the chain is guaranteed to reach $s^*$ eventually. We define the expected time to absorption from state $i$:

$$\mu_i = E[\text{number of transitions until reaching } s^* \mid X_0 = i]$$

Applying first-step analysis:
* If the chain is already at the target: $\mu_{s^*} = 0$.
* For any transient state $i$, the chain consumes 1 transition step to move to some neighbor $j$ with probability $p_{ij}$, from which point the expected remaining time is $\mu_j$:

$$\mu_i = 1 + \sum_j p_{ij} \mu_j, \quad \text{for all } i \neq s^*$$

This system of linear equations has a unique solution.

### Multiple Absorbing States

If a chain has multiple absorbing states and we wish to find the expected time until the chain hits *any* absorbing state, we lump all absorbing states into a single target set $\mathcal{A}$. Setting $\mu_k = 0$ for all $k \in \mathcal{A}$, the same linear system holds for all transient states $i \notin \mathcal{A}$:

$$\mu_i = 1 + \sum_{j \notin \mathcal{A}} p_{ij} \mu_j$$

## Mean First Passage and Recurrence Times

In a Markov chain with a single recurrent class, every state is visited infinitely often. We can calculate the expected time required to reach a specific target state for the first time.

### Mean First Passage Time

Fix a recurrent target state $s$. The **mean first passage time** from state $i$ to state $s$ is:

$$t_i = E[\min\{n \ge 0 : X_n = s\} \mid X_0 = i]$$

Because $t_s = 0$ (the target is reached immediately if the chain starts there), what occurs after reaching $s$ is irrelevant. The target $s$ can be temporarily converted into an absorbing state without altering any $t_i$. First-step analysis gives the unique linear system:

$$\begin{aligned}
t_s &= 0 \\
t_i &= 1 + \sum_j p_{ij} t_j, \quad \text{for all } i \neq s
\end{aligned}$$

### Mean Recurrence Time

The **mean recurrence time** $t_s^*$ of a state $s$ is the expected number of steps until the chain returns to $s$, given that it started in $s$:

$$t_s^* = E[\min\{n \ge 1 : X_n = s\} \mid X_0 = s]$$

Unlike $t_s$, $t_s^*$ requires at least one transition step ($n \ge 1$). Conditioning on the first transition out of state $s$:

$$t_s^* = 1 + \sum_j p_{sj} t_j$$

Here, $t_j$ is the mean first passage time from state $j$ to $s$ obtained from the preceding system of equations.

## Exercises

### Exercise 1: Fish in a Lake
There are $n$ fish in a lake, some of which are green and the rest blue. Each day, Helen catches 1 fish. She is equally likely to catch any one of the $n$ fish in the lake. She throws back all the fish, but paints each green fish blue before throwing it back in. Let $G_i$ denote the state that there are $i$ green fish left in the lake.

1. Show how to model this fishing exercise as a Markov chain where the states are the number of green fish $i \in \{0, 1, \dots, n\}$. Explain why this model satisfies the Markov property.
2. Find the transition probabilities $p_{ij}$ for all $i, j$.
3. Identify all transient and recurrent states of this Markov chain.

### Exercise 2: Transient Analysis by Inspection
Consider a Markov chain with states $\{s_0, s_1, s_2, s_3, s_4, s_5\}$ and the following transition probabilities:
* From $s_0$: transitions to $s_1$, $s_3$, and $s_5$ each with probability $1/3$.
* From $s_1$: self-loop with probability 1 (absorbing state).
* From $s_2$: transitions to $s_1$ with probability $1/2$, and self-loop with probability $1/2$.
* From $s_3$: transitions to $s_2$ with probability $1/4$, transitions to $s_4$ with probability $1/2$, and self-loop with probability $1/4$.
* From $s_4$: transitions to $s_5$ with probability $1/2$, and self-loop with probability $1/2$.
* From $s_5$: self-loop with probability 1 (absorbing state).

Given that the process is in state $s_0$ immediately before the first trial ($X_0 = s_0$):

1. Determine the probability that the process enters state $s_2$ for the first time as the result of the $k$th trial ($k \ge 1$).
2. Determine the probability that the process never enters state $s_4$.
3. Determine the probability that the process enters state $s_2$ and then leaves $s_2$ on the very next trial.
4. Determine the probability that the process enters state $s_1$ for the first time on the third trial.
5. Determine the probability that the process is in state $s_3$ immediately after the $n$th trial.

## Sources

* Review of steady-state behavior, balance equations, and time-scale mixing: Slide "Review", Slide "Example", Transcript lines 00:00–15:28.
* Dimensioning a phone system (Erlang model) and birth-death balance: Slide "The phone company problem", Transcript lines 15:28–33:55.
* Absorption probabilities and set aggregation: Slide "Calculating absorption probabilities", Transcript lines 34:01–42:00.
* Expected time to absorption: Slide "Expected time to absorption", Transcript lines 42:12–47:54.
* Mean first passage and recurrence times: Slide "Mean first passage and recurrence times", Transcript lines 47:55–51:30.
* Exercises: Problems 1 and 3 from Recitation 18. Problem 2 was omitted in the source material due to copyright restrictions.

---

[← 17. Steady-State Behavior of Markov Chains](17-steady-state-behavior-of-markov-chains.md) · [Contents](index.md) · [19. Limit Theorems and Sample Means →](19-limit-theorems-and-sample-means.md)
