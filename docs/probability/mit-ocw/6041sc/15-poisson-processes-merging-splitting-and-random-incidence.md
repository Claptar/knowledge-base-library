---
title: "15. Poisson Processes: Merging, Splitting, and Random Incidence"
course: "MIT 6.041SC"
chapter: 15
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 15. Poisson Processes: Merging, Splitting, and Random Incidence

## What this covers

This chapter deepens the study of the Poisson process by exploring operations on arrival streams and subtle sampling phenomena. It examines how independent Poisson processes can be merged and split, applies memorylessness to compute order-statistic expectations without integration, and explains the apparent paradox of random incidence in Poisson and renewal processes. The chapter assumes familiarity with the definition of the Poisson process, the exponential distribution, and basic continuous conditional expectation.

## Review of the Poisson Process

A Poisson process models arrivals occurring randomly in continuous time. It can be viewed as the continuous-time limit of a Bernoulli process, where an interval of duration $\tau$ is partitioned into a huge number of tiny slots of duration $\delta$. The process satisfies three defining properties:

1. **Time homogeneity:** The probability distribution of the number of arrivals in an interval depends solely on its duration $\tau$, not on its absolute location in time.
2. **Independence:** The numbers of arrivals in disjoint time intervals are statistically independent random variables.
3. **Small-interval probabilities:** For an infinitesimal interval of duration $\delta$, the probability of an arrival is proportional to $\delta$:
   $$P(k, \delta) \approx \begin{cases} 1 - \lambda\delta, & \text{if } k = 0, \\ \lambda\delta, & \text{if } k = 1, \\ 0, & \text{if } k > 1, \end{cases}$$
   where terms of order $O(\delta^2)$ are neglected, and $\lambda > 0$ represents the arrival rate (expected arrivals per unit time).

From these assumptions, the number of arrivals $N_\tau$ over any interval of length $\tau$ follows the Poisson probability mass function (PMF) with parameter $\lambda\tau$:
$$P(k, \tau) = \frac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}, \quad k = 0, 1, 2, \dots$$
with mean and variance given by
$$\mathbf{E}[N_\tau] = \text{var}(N_\tau) = \lambda\tau.$$

Viewed along the time axis, the interarrival times $T_1, T_2, \dots$ between successive events are independent, identically distributed (i.i.d.) exponential random variables with parameter $\lambda$:
$$f_{T_k}(t) = \lambda e^{-\lambda t}, \quad t \ge 0, \quad \mathbf{E}[T_k] = \frac{1}{\lambda}.$$

Because interarrival times are exponential, the process possesses the **memoryless property**: if an arrival has not occurred by time $t$, the remaining time until the arrival has the identical distribution $f_{T_1}(t)$ as a fresh start. Statistically, "used is as good as new."

The total waiting time $Y_k = T_1 + \dots + T_k$ until the $k$th arrival follows an Erlang distribution of order $k$:
$$f_{Y_k}(y) = \frac{\lambda^k y^{k-1} e^{-\lambda y}}{(k - 1)!}, \quad y \ge 0.$$

### Example: Poisson Fishing

Suppose fish are caught according to a Poisson process with rate $\lambda = 0.6$ per hour. An angler adopts the following rule: fish for 2 hours; if at least one fish is caught, stop and go home; if no fish are caught, continue fishing until the first fish is caught, and then go home.

1. **Probability of fishing for more than 2 hours:**
   The angler fishes past hour 2 if and only if zero fish are caught in the interval $[0, 2]$:
   $$\mathbf{P}(\text{fish } > 2\text{ hours}) = P(0, 2) = e^{-\lambda \cdot 2} = e^{-0.6 \cdot 2} = e^{-1.2} \approx 0.3012.$$
   Equivalently, this is the probability that the first arrival occurs after time 2: $\mathbf{P}(T_1 > 2) = \int_2^\infty \lambda e^{-\lambda t}\,dt = e^{-2\lambda}$.

2. **Probability of fishing between 2 and 5 hours:**
   This requires zero fish caught in $[0, 2]$, followed by catching the first fish in the next 3 hours (interval $[2, 5]$). By the independence of disjoint intervals:
   $$\mathbf{P}(2 < \text{time} < 5) = \mathbf{P}(N_2 = 0) \cdot \mathbf{P}(N_{[2, 5]} \ge 1) = e^{-2\lambda} (1 - e^{-3\lambda}) = e^{-1.2}(1 - e^{-1.8}).$$

3. **Probability of catching at least 2 fish:**
   Under the stopping rule, if no fish are caught in the first 2 hours, the angler stops immediately after the 1st catch. Therefore, the angler can catch 2 or more fish only if at least 2 fish were caught during the initial 2 hours:
   $$\mathbf{P}(\text{catch } \ge 2) = \sum_{k=2}^\infty \frac{(2\lambda)^k e^{-2\lambda}}{k!} = 1 - P(0, 2) - P(1, 2) = 1 - e^{-2\lambda} - 2\lambda e^{-2\lambda} = 1 - e^{-1.2}(1 + 1.2).$$
   Equivalently, this equals $\mathbf{P}(Y_2 \le 2)$, where $Y_2$ is the arrival time of the second fish.

4. **Expected total number of fish caught:**
   Decompose the total count into the fish caught in $[0, 2]$ plus the fish caught after time 2:
   $$\mathbf{E}[\text{fish}] = \mathbf{E}[N_2] + \mathbf{E}[\text{fish after } t = 2].$$
   In the first 2 hours, $\mathbf{E}[N_2] = 2\lambda = 1.2$. After time 2, the angler catches 1 fish if $N_2 = 0$, and 0 fish if $N_2 \ge 1$. Hence:
   $$\mathbf{E}[\text{fish after } t = 2] = 1 \cdot \mathbf{P}(N_2 = 0) + 0 \cdot \mathbf{P}(N_2 \ge 1) = e^{-2\lambda}.$$
   Thus, $\mathbf{E}[\text{total fish}] = 1.2 + e^{-1.2}$.

5. **Expected total fishing time:**
   The angler fishes for 2 hours unconditionally. Additional fishing occurs only if $N_2 = 0$, in which case the remaining time until the next catch is an exponential random variable with mean $1/\lambda$:
   $$\mathbf{E}[\text{total fishing time}] = 2 + \mathbf{P}(N_2 = 0) \cdot \frac{1}{\lambda} = 2 + \frac{e^{-1.2}}{0.6}.$$

6. **Expected future fishing time given 4 hours fished:**
   If the angler is still fishing at $t = 4$, no fish has arrived in $[0, 4]$. By memorylessness, the past duration is irrelevant; the time to the first catch from $t = 4$ forward is exponential with rate $\lambda$:
   $$\mathbf{E}[\text{future time} \mid \text{fished 4 hours}] = \frac{1}{\lambda} = \frac{1}{0.6} \text{ hours}.$$

## Merging Poisson Processes

Consider two independent Poisson processes with rates $\lambda_1$ and $\lambda_2$. Let the *merged process* record an arrival whenever an arrival occurs in either of the two streams.

<figure>
<svg viewBox="0 0 420 170" role="img" aria-label="Two independent Poisson arrival streams merging into a single Poisson stream.">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0 1, 8 4, 0 7" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Stream 1 -->
  <text x="15" y="35" font-size="12" fill="currentColor">Stream 1 (λ₁)</text>
  <line x1="105" y1="30" x2="390" y2="30" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr)"/>
  <circle cx="160" cy="30" r="3.5" fill="currentColor"/>
  <circle cx="280" cy="30" r="3.5" fill="currentColor"/>
  <!-- Stream 2 -->
  <text x="15" y="85" font-size="12" fill="currentColor">Stream 2 (λ₂)</text>
  <line x1="105" y1="80" x2="390" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr)"/>
  <circle cx="210" cy="80" r="3.5" fill="currentColor"/>
  <circle cx="340" cy="80" r="3.5" fill="currentColor"/>
  <!-- Merged -->
  <text x="15" y="140" font-size="12" fill="currentColor">Merged (λ₁+λ₂)</text>
  <line x1="105" y1="135" x2="390" y2="135" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr)"/>
  <circle cx="160" cy="135" r="3.5" fill="currentColor"/>
  <circle cx="210" cy="135" r="3.5" fill="currentColor"/>
  <circle cx="280" cy="135" r="3.5" fill="currentColor"/>
  <circle cx="340" cy="135" r="3.5" fill="currentColor"/>
</svg>
<figcaption>Merging two independent Poisson processes produces a new Poisson process whose rate is the sum of the individual rates.</figcaption>
</figure>

In a tiny interval of duration $\delta$, the probability of an arrival in the merged process is:
$$\mathbf{P}(\text{arrival in } \delta) = \mathbf{P}(\text{arrival in 1}) + \mathbf{P}(\text{arrival in 2}) - \mathbf{P}(\text{arrival in both}) \approx \lambda_1\delta + \lambda_2\delta - O(\delta^2) = (\lambda_1 + \lambda_2)\delta.$$
Disjoint intervals in the merged process depend only on disjoint intervals in the constituent processes, preserving independence. Thus, the merged process is Poisson with parameter $\lambda = \lambda_1 + \lambda_2$.

### Origin of Merged Arrivals

When an arrival occurs in the merged process, which stream produced it? Conditioning on an arrival in an infinitesimal slot of length $\delta$:
$$\mathbf{P}(\text{from stream 1} \mid \text{arrival}) = \frac{\lambda_1\delta}{(\lambda_1 + \lambda_2)\delta} = \frac{\lambda_1}{\lambda_1 + \lambda_2}.$$
Similarly, the probability that the arrival came from stream 2 is $\lambda_2 / (\lambda_1 + \lambda_2)$.

Because disjoint intervals in the underlying processes are independent, knowing the origin of an arrival at time $t$ provides zero information about the origin of an arrival at any other time $s \neq t$. Assigning origins is equivalent to tossing an independent biased coin with probability $\lambda_1 / (\lambda_1 + \lambda_2)$ at each merged arrival.

### Example: The Three Light Bulbs

Suppose three light bulbs have independent, exponentially distributed lifetimes with identical parameter $\lambda$. They are all installed and switched on at time $t = 0$. What is the expected time until the last bulb burns out?

Let $X_1, X_2, X_3 \sim \text{Exponential}(\lambda)$ be the lifetimes. We seek $\mathbf{E}[\max(X_1, X_2, X_3)]$. Rather than integrating the maximum density directly, we embed the lifetimes as the first arrival times of three independent Poisson processes running in parallel.

1. **Time until first failure ($V_1$):**
   With all 3 bulbs operating, a failure occurs whenever the merged process of 3 independent Poisson processes records an arrival. The merged rate is $3\lambda$. The time until the first failure is exponentially distributed with rate $3\lambda$:
   $$\mathbf{E}[V_1] = \frac{1}{3\lambda}.$$

2. **Time from first to second failure ($V_2$):**
   At the moment the first bulb dies, 2 surviving bulbs remain. By memorylessness, the remaining lifetimes of these two bulbs are still independent, exponential random variables with rate $\lambda$. They form a merged Poisson process of rate $2\lambda$. Therefore:
   $$\mathbf{E}[V_2] = \frac{1}{2\lambda}.$$

3. **Time from second to third failure ($V_3$):**
   When the second bulb dies, 1 bulb remains. By memorylessness, its remaining life is exponential with rate $\lambda$:
   $$\mathbf{E}[V_3] = \frac{1}{\lambda}.$$

The total time until the last bulb fails is $V_1 + V_2 + V_3$. By linearity of expectation:
$$\mathbf{E}[\max(X_1, X_2, X_3)] = \mathbf{E}[V_1] + \mathbf{E}[V_2] + \mathbf{E}[V_3] = \frac{1}{3\lambda} + \frac{1}{2\lambda} + \frac{1}{\lambda} = \frac{11}{6\lambda}.$$

## Splitting of Poisson Processes

The reverse operation of merging is *splitting* (or *thinning*). Suppose arrivals occur according to a Poisson process with rate $\lambda$. Each arrival is routed independently to stream 1 with probability $p$, or to stream 2 with probability $1 - p$.

In a small time slot $\delta$:
$$\mathbf{P}(\text{arrival routed to stream 1}) = \lambda\delta \cdot p = (p\lambda)\delta.$$
The independence of disjoint time slots and the independence of routing decisions guarantee that the resulting streams are independent Poisson processes with rates $p\lambda$ and $(1 - p)\lambda$, respectively.

For example, if incoming email to a server arrives as a Poisson process with rate $\lambda$, and each message is independently addressed to a domestic server with probability $p$ and a foreign server with probability $1 - p$, domestic traffic forms a Poisson process with rate $p\lambda$, foreign traffic forms a Poisson process with rate $(1 - p)\lambda$, and the two streams are statistically independent.

## Random Incidence

Consider a Poisson arrival process with rate $\lambda$ that has been running from the remote past to the indefinite future. Suppose an observer arrives at an arbitrary, fixed time instant $t^*$ (often phrased casually as showing up at a "random time"). What is the expected length of the interarrival interval containing $t^*$?

<figure>
<svg viewBox="0 0 420 140" role="img" aria-label="Diagram showing random incidence falling into an interarrival interval.">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
      <polygon points="0 1, 8 4, 0 7" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="20" y1="70" x2="400" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <circle cx="60" cy="70" r="3.5" fill="currentColor"/>
  <circle cx="150" cy="70" r="3.5" fill="currentColor"/>
  <circle cx="310" cy="70" r="3.5" fill="currentColor"/>
  <circle cx="370" cy="70" r="3.5" fill="currentColor"/>
  <!-- Inspection time -->
  <line x1="230" y1="20" x2="230" y2="65" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr2)"/>
  <text x="230" y="15" text-anchor="middle" font-size="12" fill="currentColor">t*</text>
  <!-- Durations -->
  <line x1="150" y1="95" x2="230" y2="95" stroke="currentColor" stroke-width="1"/>
  <line x1="230" y1="95" x2="310" y2="95" stroke="currentColor" stroke-width="1"/>
  <text x="190" y="112" text-anchor="middle" font-size="11" fill="currentColor">T₁′</text>
  <text x="270" y="112" text-anchor="middle" font-size="11" fill="currentColor">T₁</text>
  <text x="390" y="60" font-size="12" fill="currentColor">t</text>
</svg>
<figcaption>An observer arrives at time t*, partitioning the current interarrival interval into backward time T₁′ and forward time T₁.</figcaption>
</figure>

Let $L$ be the total length of the interval enclosing $t^*$. This interval is divided by $t^*$ into two segments:
- $T_1$: the forward waiting time from $t^*$ until the next arrival.
- $T_1'$: the backward time from $t^*$ to the previous arrival.

By the forward memoryless property of the Poisson process, the future after $t^*$ is independent of the past, so $T_1$ is an exponential random variable with parameter $\lambda$, giving:
$$\mathbf{E}[T_1] = \frac{1}{\lambda}.$$

Now consider $T_1'$. Because a Poisson process viewed backward in time is statistically identical to a Poisson process running forward (just as a backward Bernoulli process of independent coin flips has identical statistics), $T_1'$ is also an exponential random variable with parameter $\lambda$:
$$\mathbf{E}[T_1'] = \frac{1}{\lambda}.$$

Since $L = T_1 + T_1'$, the expected length of the chosen interval is:
$$\mathbf{E}[L] = \mathbf{E}[T_1'] + \mathbf{E}[T_1] = \frac{1}{\lambda} + \frac{1}{\lambda} = \frac{2}{\lambda}.$$

### The Inspection Paradox

The naive expectation is that an interarrival interval has mean $1/\lambda$. Yet the interval enclosing $t^*$ has an expected length of $2/\lambda$—twice as large.

This discrepancy stems from sampling bias. There are two entirely different ways to define a "typical" interval:
1. **Index-based sampling:** Pick an arrival by its index (e.g., the 100th bus). Every interval has equal probability of being chosen, yielding the true mean duration $1/\lambda$.
2. **Time-based sampling (Random Incidence):** Drop an arbitrary point $t^*$ onto the continuous time axis. The probability of hitting a given interval is proportional to its length. A time-based observer is far more likely to land in an unusually long interval than an unusually short one.

### Random Incidence in Renewal Processes

The same sampling bias occurs in general renewal processes, where interarrival times are i.i.d. draws from a general non-exponential distribution.

Suppose bus interarrival times are equally likely to be 5 minutes or 10 minutes:
$$\mathbf{P}(T = 5) = 0.5, \quad \mathbf{P}(T = 10) = 0.5.$$
The average interarrival time across buses is:
$$\mathbf{E}[T] = 0.5(5) + 0.5(10) = 7.5\text{ minutes}.$$

Suppose a passenger arrives at an arbitrary time $t^*$. Intervals of length 10 occupy twice as much time along the time axis as intervals of length 5. Thus, the probability that the passenger arrives inside a 10-minute interval is:
$$\mathbf{P}(\text{fall in 10}) = \frac{10}{5 + 10} = \frac{2}{3}, \qquad \mathbf{P}(\text{fall in 5}) = \frac{5}{5 + 10} = \frac{1}{3}.$$
The expected length of the interval selected by random incidence is:
$$\mathbf{E}[L] = \frac{1}{3}(5) + \frac{2}{3}(10) = \frac{25}{3} \approx 8.33\text{ minutes} > 7.5\text{ minutes}.$$

The expected waiting time until the next bus is similarly lengthened by the bias toward landing in long intervals. Whenever an entity samples an environment proportional to duration or size—whether passengers sampling bus intervals, people sampling family sizes, or inspectors sampling cookies—the observed average exceeds the population average.

## Exercises

### Exercise 1: Bulb Replacements with Two Types

Beginning at time $t = 0$, a room is illuminated using bulbs one at a time, replaced immediately upon failure. Each new bulb is selected independently as an equally likely choice between a type-A bulb and a type-B bulb. The lifetime $X$ of any bulb is independent of everything else, with probability density functions:
$$f_X(x) = \begin{cases} e^{-x}, & x \ge 0 \\ 0, & \text{otherwise} \end{cases} \quad \text{for type-A}, \qquad f_X(x) = \begin{cases} 3e^{-3x}, & x \ge 0 \\ 0, & \text{otherwise} \end{cases} \quad \text{for type-B}.$$

1. Find the expected time until the first failure.
2. Find the probability that there are no bulb failures before time $t$.
3. Given that there are no failures until time $t$, determine the conditional probability that the first bulb used is a type-A bulb.
4. Determine the probability that the total period of illumination provided by the first two type-B bulbs is longer than that provided by the first type-A bulb.
5. Suppose the process terminates as soon as a total of exactly 12 bulb failures have occurred. Determine the expected value and variance of the total period of illumination provided by type-B bulbs while the process is in operation.
6. Given that there are no failures until time $t$, find the expected value of the time until the first failure.

### Exercise 2: Two-Type Service Station

A service station processes jobs of types A and B simultaneously. Arrivals of the two types are independent Poisson processes with rates $\lambda_A = 3$ and $\lambda_B = 4$ per minute, respectively. Type A jobs remain in service for exactly 1 minute. Each type B job stays for an integer amount of time that is geometrically distributed with mean 2, independent of everything else. The station has been operating from the remote past.

1. What is the mean, variance, and PMF of the total number of jobs that arrive within a given 3-minute interval?
2. During a 10-minute interval, exactly 10 new jobs arrive. What is the probability that exactly 3 of them are of type A?
3. At time 0, no job is present in the service station. What is the PMF of the number of type B jobs that arrive in the future before the first type A arrival?

### Exercise 3: Ordering of Exponential Lifetimes

Let $X$, $Y$, and $Z$ be independent exponential random variables with parameters $\lambda$, $\mu$, and $\nu$, respectively. Find $\mathbf{P}(X < Y < Z)$ using the properties of merged Poisson processes.

## Sources

- Lecture slides: "Poisson process — II", MIT Course 6.041SC, Fall 2013.
- Lecture transcript: John Tsitsiklis, Lecture 15 captions, MIT Course 6.041SC, Fall 2013.
- Problem set: Recitation 15 problems (Problems 6.14 and 6.15 from the course text, and ordering of three exponentials), MIT Course 6.041/6.431, Fall 2010.

Solutions: [chapter 15](solutions/15-poisson-processes-merging-splitting-and-random-incidence.md)


---

[← 14. The Poisson Process](14-the-poisson-process.md) · [Contents](index.md) · [16. Discrete-Time Markov Chains →](16-discrete-time-markov-chains.md)
