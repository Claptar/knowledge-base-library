---
title: "13. The Bernoulli Process"
course: "MIT 6.041SC"
chapter: 13
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 13. The Bernoulli Process

## What this covers

This chapter introduces random processes by examining the simplest memoryless, discrete-time model: the Bernoulli process. We explore how to characterize infinite sequences of independent trials, derive the distributions of arrival counts and interarrival times, and analyze operations such as splitting and merging streams.

## The Bernoulli Process and Random Processes

A *random process* (or *stochastic process*) is a mathematical model for a random phenomenon that unfolds over time. Where static probability problems deal with a fixed set of random variables, a random process generates a collection of random variables indexed by time, either discrete ($t = 1, 2, \dots$) or continuous ($t \ge 0$).

The simplest non-trivial discrete-time random process is the **Bernoulli process**. It is a sequence $X_1, X_2, \dots$ of independent, identically distributed (i.i.d.) Bernoulli trials. At each trial $i$:

$$P(X_i = 1) = p \quad (\text{success / arrival})$$
$$P(X_i = 0) = 1 - p \quad (\text{failure / no arrival})$$

where the success parameter $p$ satisfies $0 < p < 1$ and remains constant across all trials. 

Physical examples include:
- Repeatedly buying a weekly lottery ticket, recording wins ($1$) and losses ($0$).
- A stylized daily financial model where a stock index moves up ($1$) or down ($0$).
- Arrival streams at a facility (such as requests to a web server or customers entering a bank), where time is divided into small discrete slots, each containing either an arrival ($1$) or no arrival ($0$).

### Two Views of a Random Process

There are two complementary ways to conceptualize a Bernoulli process:

1. **A sequence of random variables:** We view the process as a list $X_1, X_2, \dots$. For each individual trial $t$, we have:
   $$\mathbf{E}[X_t] = 1\cdot p + 0\cdot(1 - p) = p$$
   $$\text{Var}(X_t) = p(1 - p)$$
   To completely specify a random process from this viewpoint, one must provide the joint distribution for any finite collection of trials, such as $(X_2, X_5, X_7)$. Because the trials are independent, every joint probability mass function (PMF) factors cleanly into the product of marginal PMFs:
   $$P(X_{t_1} = x_1, X_{t_2} = x_2, \dots, X_{t_k} = x_k) = \prod_{i=1}^k P(X_{t_i} = x_i)$$

2. **A single infinite experiment:** We view the process as picking a single sample point from an infinite sample space $\Omega$, where every sample point $\omega \in \Omega$ is an infinite sequence of zeros and ones:
   $$\omega = (x_1, x_2, x_3, \dots), \quad x_i \in \{0, 1\}$$
   Under this perspective, we can ask questions about global events. For example, what is the probability of obtaining an infinite string of successes, $P(X_t = 1 \text{ for all } t)$?
   
   For any finite integer $k$, the event $\{X_t = 1 \text{ for all } t\}$ is a subset of the event $\{X_1 = 1, X_2 = 1, \dots, X_k = 1\}$. Therefore:
   $$P(X_t = 1 \text{ for all } t) \le P(X_1 = 1, \dots, X_k = 1) = p^k$$
   Since this inequality holds for every positive integer $k$, and because $p < 1$:
   $$P(X_t = 1 \text{ for all } t) \le \lim_{k \to \infty} p^k = 0$$
   Thus, the probability of an infinite sequence of all ones is exactly $0$. 

Indeed, if one computes the probability of any specific single infinite sequence, the calculation involves an infinite product of probabilities bounded away from $1$, which evaluates to $0$. This behaves analogously to picking a real number at random from a continuous interval: any specific real number (which can be represented by its binary expansion) has probability zero, yet the entire sample space has total probability one.

## Number of Arrivals in a Time Window

When analyzing arrival processes, two fundamental questions arise:
1. *Fixed time:* How many arrivals occur in a fixed number of slots?
2. *Fixed arrivals:* How much time elapses before a specified number of arrivals occur?

For the first question, let $S$ denote the number of successes (arrivals) observed during the first $n$ time slots:
$$S = \sum_{i=1}^n X_i$$

Because $S$ is the sum of $n$ independent and identically distributed Bernoulli random variables, $S$ follows a binomial distribution with parameters $n$ and $p$:

$$P(S = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k \in \{0, 1, \dots, n\}$$

Using the linearity of expectation and the independence of the trials:
$$\mathbf{E}[S] = np$$
$$\text{Var}(S) = np(1 - p)$$

## Interarrival Times and Memorylessness

To address the second question, let $T_1$ denote the number of trials up to and including the first arrival. 

The event $\{T_1 = t\}$ means that trials $1, 2, \dots, t-1$ were failures ($0$) and trial $t$ was a success ($1$). By independence, this probability is:
$$P(T_1 = t) = (1 - p)^{t - 1} p, \quad t = 1, 2, 3, \dots$$

This is the geometric distribution with parameter $p$. Its expectation and variance are:
$$\mathbf{E}[T_1] = \frac{1}{p}$$
$$\text{Var}(T_1) = \frac{1 - p}{p^2}$$

### The Memoryless Property

The Bernoulli process possesses the **memoryless property**, which is a direct consequence of trial independence. If the process is observed up to time $t$, the future trials $X_{t+1}, X_{t+2}, \dots$ are completely independent of what occurred in slots $1, \dots, t$. They form a fresh Bernoulli process with the identical parameter $p$.

Crucially, this fresh-start property holds not just at fixed, deterministic times, but also at random times determined by the history of the process—provided that the stopping criterion uses **no foresight** into future trials. 

If an observer waits until the first success occurs and then begins recording subsequent trials, the future trials are independent Bernoulli trials with parameter $p$. However, if an observer were signaled to start watching because someone looked ahead and determined that the upcoming trial was guaranteed to be a success, independence would be destroyed.

<figure>
<svg viewBox="0 0 460 110" role="img" aria-label="Diagram showing interarrival times T1, T2, and T3 along a discrete time axis">
  <!-- Axis line -->
  <line x1="30" y1="70" x2="430" y2="70" stroke="currentColor" stroke-width="1.5"/>
  <!-- Arrowhead on axis -->
  <polygon points="430,66 440,70 430,74" fill="currentColor"/>
  
  <!-- Tick marks and trials -->
  <!-- t=1 (0) -->
  <line x1="60" y1="65" x2="60" y2="75" stroke="currentColor" stroke-width="1.2"/>
  <text x="60" y="60" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <!-- t=2 (1) Success 1 -->
  <line x1="110" y1="65" x2="110" y2="75" stroke="currentColor" stroke-width="1.2"/>
  <circle cx="110" cy="56" r="3.5" fill="currentColor"/>
  <text x="110" y="47" text-anchor="middle" font-size="11" fill="currentColor">1st</text>
  <!-- t=3 (0) -->
  <line x1="160" y1="65" x2="160" y2="75" stroke="currentColor" stroke-width="1.2"/>
  <text x="160" y="60" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <!-- t=4 (0) -->
  <line x1="210" y1="65" x2="210" y2="75" stroke="currentColor" stroke-width="1.2"/>
  <text x="210" y="60" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <!-- t=5 (1) Success 2 -->
  <line x1="260" y1="65" x2="260" y2="75" stroke="currentColor" stroke-width="1.2"/>
  <circle cx="260" cy="56" r="3.5" fill="currentColor"/>
  <text x="260" y="47" text-anchor="middle" font-size="11" fill="currentColor">2nd</text>
  <!-- t=6 (0) -->
  <line x1="310" y1="65" x2="310" y2="75" stroke="currentColor" stroke-width="1.2"/>
  <text x="310" y="60" text-anchor="middle" font-size="12" fill="currentColor">0</text>
  <!-- t=7 (1) Success 3 -->
  <line x1="360" y1="65" x2="360" y2="75" stroke="currentColor" stroke-width="1.2"/>
  <circle cx="360" cy="56" r="3.5" fill="currentColor"/>
  <text x="360" y="47" text-anchor="middle" font-size="11" fill="currentColor">3rd</text>

  <!-- Brackets / spans for T1, T2, T3 -->
  <line x1="30" y1="88" x2="110" y2="88" stroke="currentColor" stroke-width="1"/>
  <text x="70" y="103" text-anchor="middle" font-size="12" fill="currentColor">T₁ = 2</text>
  
  <line x1="110" y1="88" x2="260" y2="88" stroke="currentColor" stroke-width="1"/>
  <text x="185" y="103" text-anchor="middle" font-size="12" fill="currentColor">T₂ = 3</text>
  
  <line x1="260" y1="88" x2="360" y2="88" stroke="currentColor" stroke-width="1"/>
  <text x="310" y="103" text-anchor="middle" font-size="12" fill="currentColor">T₃ = 2</text>
</svg>
<figcaption>A realization of the Bernoulli process showing trial outcomes and interarrival intervals $T_1, T_2, T_3$.</figcaption>
</figure>

### Example: Length of the First String of Losing Days

Suppose you buy a lottery ticket every day. What is the distribution of the length $L$ of the first string of consecutive losing days?

A sequence might begin with several wins, followed by a non-empty sequence of losses, followed by a win:
$$1, 1, \dots, 1, \underbrace{0, 0, \dots, 0}_{L \text{ losses}}, 1$$

One might be tempted to argue that if an observer waits right before the first failure starts, the number of steps until the next success is geometric, which would make $L + 1$ geometric. However, this reasoning is invalid:
- A geometric random variable takes values in $\{1, 2, 3, \dots\}$, which would imply $L$ can take the value $0$. But by definition, a string of losing days must contain at least one loss ($L \ge 1$).
- To position someone right before the string begins requires foresight—knowing that the upcoming trial is guaranteed to be a loss.

The correct formulation relies on a valid past-dependent stopping time:
1. Let the process run until the **first loss** occurs. The observer is called into the room immediately after this trial is completed.
2. From this moment onward, the remaining outcomes are ordinary i.i.d. Bernoulli trials, completely independent of the past, with probability of success $p$.
3. We count the number of trials until the next success. By definition of a fresh Bernoulli process, the number of trials up to and including the next success is geometrically distributed with parameter $p$.

Because the original interval of losses $L$ has the exact same duration as this fresh waiting time, $L$ itself follows a geometric distribution with parameter $p$:
$$P(L = \ell) = (1 - p)^{\ell - 1} p, \quad \ell = 1, 2, 3, \dots$$

## The Time of the $k$th Arrival

Let $T_k$ denote the $k$th *interarrival time*—the number of time slots between the $(k-1)$st arrival and the $k$th arrival. 

By the memoryless property, once the $(k-1)$st arrival occurs, the future evolution is an independent replica of the original Bernoulli process. Consequently:
- Each $T_i$ is a geometric random variable with parameter $p$:
  $$P(T_i = t) = (1 - p)^{t-1}p, \quad t = 1, 2, \dots$$
- The interarrival times $T_1, T_2, \dots, T_k$ are mutually independent.

The time of the $k$th arrival, denoted $Y_k$, is the total time elapsed up to that arrival:
$$Y_k = \sum_{i=1}^k T_i$$

### Moments of $Y_k$
Because $Y_k$ is the sum of $k$ independent, identically distributed geometric random variables, its expectation and variance follow directly from the properties of sums of independent variables:
$$\mathbf{E}[Y_k] = \sum_{i=1}^k \mathbf{E}[T_i] = \frac{k}{p}$$
$$\text{Var}(Y_k) = \sum_{i=1}^k \text{Var}(T_i) = \frac{k(1 - p)}{p^2}$$

### The PMF of $Y_k$ (Pascal Distribution)
Rather than computing the $k$-fold convolution of geometric PMFs, we can determine $P(Y_k = t)$ by decomposing the event into two independent components:
1. In the first $t - 1$ slots, there must be exactly $k - 1$ arrivals.
2. At slot $t$, there must be an arrival.

The number of arrivals in the first $t - 1$ slots follows a binomial distribution. Because time slot $t$ is independent of the preceding $t - 1$ slots, we multiply their probabilities:

$$P(Y_k = t) = \underbrace{\binom{t - 1}{k - 1} p^{k - 1} (1 - p)^{(t - 1) - (k - 1)}}_{\text{Probability of } k-1 \text{ arrivals in } t-1 \text{ slots}} \times \underbrace{p}_{\text{Arrival at slot } t}$$

Simplifying the exponents yields the Pascal PMF of order $k$:
$$P(Y_k = t) = \binom{t - 1}{k - 1} p^k (1 - p)^{t - k}, \quad t = k, k + 1, k + 2, \dots$$
Notice that $t$ must be at least $k$, since $k$ distinct arrivals require at least $k$ discrete time slots.

## Splitting and Merging Processes

We can build more complex networks of arrival streams by splitting or merging Bernoulli processes.

### Splitting a Bernoulli Process
Consider an arrival stream modeled as a Bernoulli process with parameter $p$. Whenever an arrival occurs, we route it to Stream 1 with probability $q$, or to Stream 2 with probability $1 - q$, decided by flipping a separate, independent coin.

<figure>
<svg viewBox="0 0 380 140" role="img" aria-label="A single Bernoulli arrival stream splitting into two separate streams">
  <!-- Main incoming line -->
  <line x1="30" y1="70" x2="150" y2="70" stroke="currentColor" stroke-width="1.5"/>
  <text x="85" y="60" text-anchor="middle" font-size="12" fill="currentColor">Bernoulli(p)</text>
  
  <!-- Split node -->
  <circle cx="150" cy="70" r="4" fill="currentColor"/>
  
  <!-- Branch 1 (top) -->
  <line x1="150" y1="70" x2="210" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <line x1="210" y1="30" x2="330" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="330,26 340,30 330,34" fill="currentColor"/>
  <text x="175" y="42" text-anchor="middle" font-size="11" fill="currentColor">prob q</text>
  <text x="270" y="22" text-anchor="middle" font-size="12" fill="currentColor">Bernoulli(pq)</text>
  
  <!-- Branch 2 (bottom) -->
  <line x1="150" y1="70" x2="210" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <line x1="210" y1="110" x2="330" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <polygon points="330,106 340,110 330,114" fill="currentColor"/>
  <text x="175" y="105" text-anchor="middle" font-size="11" fill="currentColor">prob 1-q</text>
  <text x="270" y="128" text-anchor="middle" font-size="12" fill="currentColor">Bernoulli(p(1-q))</text>
</svg>
<figcaption>Splitting a Bernoulli process with independent coin tosses yields two Bernoulli processes.</figcaption>
</figure>

In any given slot:
- Stream 1 sees an arrival if and only if an arrival occurred in the base process AND the routing coin selected Stream 1. By independence, this probability is $p \cdot q$.
- Stream 2 sees an arrival with probability $p(1 - q)$.

Because the arrival decisions at different time slots depend on disjoint sets of independent coin tosses, trials across distinct slots remain statistically independent. Thus:
- Stream 1 is a Bernoulli process with parameter $pq$.
- Stream 2 is a Bernoulli process with parameter $p(1 - q)$.

### Merging Bernoulli Processes
Conversely, consider two independent Bernoulli processes running in parallel: Stream 1 with parameter $p$, and Stream 2 with parameter $q$. We combine them into a single merged process. 

In a discrete-time model, both streams could register an arrival in the same slot. We define the merged process by recording whether *at least one* arrival occurred in that slot:

$$X_t^{\text{merged}} = \begin{cases} 1 & \text{if Stream 1 has an arrival or Stream 2 has an arrival (or both)} \\ 0 & \text{if neither stream has an arrival} \end{cases}$$

For any slot $t$, the probability of receiving no arrival in the merged process is the probability that both streams are idle:
$$P(X_t^{\text{merged}} = 0) = (1 - p)(1 - q)$$

Therefore, the probability of an arrival in slot $t$ is:
$$P(X_t^{\text{merged}} = 1) = 1 - (1 - p)(1 - q) = p + q - pq$$

Because the trials in both streams are independent across different time slots, what happens in the merged process at slot $t$ is independent of what happens at any other slot $s \ne t$. Hence, the merged stream is itself a Bernoulli process with parameter $p + q - pq$.

## Exercises

### Problem 1
Let $X$, $Y$, and $Z$ be discrete random variables. Recall the Law of Iterated Expectations, $\mathbf{E}[W] = \mathbf{E}[\mathbf{E}[W \mid V]]$. Prove the following generalizations:
1. $\mathbf{E}[Z] = \mathbf{E}[\mathbf{E}[Z \mid X, Y]]$
2. $\mathbf{E}[Z \mid X] = \mathbf{E}[\mathbf{E}[Z \mid X, Y] \mid X]$
3. $\mathbf{E}[Z] = \mathbf{E}[\mathbf{E}[\mathbf{E}[Z \mid X, Y] \mid X]]$

### Problem 2
We start with a stick of length $\ell$. We break it at a point chosen randomly and uniformly over its length, keeping the piece containing the left end. We then repeat this uniform breaking process on the remaining piece.
1. What is the expected value of the length of the piece remaining after breaking twice?
2. What is the variance of the length of the piece remaining after breaking twice?

### Problem 3
Widgets are stored in boxes, and all boxes are assembled into a crate. Let $X$ denote the number of widgets in a particular box, and let $N$ denote the number of boxes in a crate. Assume that $X$ and $N$ are independent integer-valued random variables, each with an expected value of $10$ and a variance of $16$. Determine the expected value and the variance of $T$, the total number of widgets in a crate.

## Sources

- **Lecture 13 Slides & Transcript:** Bernoulli process definition, sample space of infinite sequences, binomial count distribution, geometric interarrival times, memoryless property, the first string of losing days example, Pascal distribution for $k$th arrival time, splitting and merging of independent Bernoulli processes.
- **Recitation 13 Problem Set:** Iterated expectations generalizations (Problem 1), broken stick length moments (Problem 2), and total widget count in a crate (Problem 3).

Solutions: [chapter 13](solutions/13-the-bernoulli-process.md)


---

[← 12. Iterated Expectations and Total Variance](12-iterated-expectations-and-total-variance.md) · [Contents](index.md) · [14. The Poisson Process →](14-the-poisson-process.md)
