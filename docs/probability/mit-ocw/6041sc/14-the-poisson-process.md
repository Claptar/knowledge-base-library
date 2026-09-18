---
title: "14. The Poisson Process"
course: "MIT 6.041SC"
chapter: 14
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 14. The Poisson Process

## What this covers

This chapter introduces the Poisson process as the continuous-time analog of the Bernoulli process. It defines the process via its fundamental assumptions of time homogeneity, independent increments, and small-interval arrival probabilities, and derives the distributions governing arrival counts and interarrival times. It assumes familiarity with the Bernoulli process, geometric and binomial distributions, and elementary limits.

## The Continuous-Time Limit of Bernoulli Trials

In a Bernoulli process, time is divided into discrete slots. In each slot, an independent trial produces a success (an arrival) with probability $p$. The number of arrivals in $n$ trials follows a binomial distribution, the time until the first arrival follows a geometric distribution, and the time until the $k$-th arrival follows a Pascal distribution (a sum of $k$ independent geometric variables).

To model phenomena in continuous time—such as customers entering a bank, photons hitting a detector, radioactive decays, or email messages arriving in an inbox—we imagine shrinking the slot duration to an infinitesimal length $\delta$. Instead of recording whether an event occurred in discrete millisecond or microsecond bins, we record the exact continuous times at which arrivals happen.

<figure>
<svg viewBox="0 0 420 110" role="img" aria-label="Approximation of continuous time by finely spaced intervals of length delta">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Time axis -->
  <line x1="30" y1="70" x2="390" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="395" y="74" font-size="12" fill="currentColor">Time</text>
  <line x1="40" y1="65" x2="40" y2="75" stroke="currentColor" stroke-width="1.5"/>
  <text x="37" y="88" font-size="12" fill="currentColor">0</text>
  <!-- Intervals -->
  <line x1="80" y1="65" x2="80" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="120" y1="65" x2="120" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="65" x2="160" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="200" y1="65" x2="200" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="240" y1="65" x2="240" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="280" y1="65" x2="280" y2="75" stroke="currentColor" stroke-width="1"/>
  <line x1="320" y1="65" x2="320" y2="75" stroke="currentColor" stroke-width="1"/>
  <!-- Delta label -->
  <line x1="120" y1="45" x2="160" y2="45" stroke="currentColor" stroke-width="1"/>
  <line x1="120" y1="42" x2="120" y2="48" stroke="currentColor" stroke-width="1"/>
  <line x1="160" y1="42" x2="160" y2="48" stroke="currentColor" stroke-width="1"/>
  <text x="140" y="38" text-anchor="middle" font-size="12" fill="currentColor">&#948;</text>
  <!-- Arrivals marked with dots -->
  <circle cx="102" cy="70" r="3.5" fill="currentColor"/>
  <circle cx="218" cy="70" r="3.5" fill="currentColor"/>
  <circle cx="305" cy="70" r="3.5" fill="currentColor"/>
</svg>
<figcaption>Partitioning continuous time into microscopic slots of width &#948;, each containing at most one arrival.</figcaption>
</figure>

## Definition of the Poisson Process

Let $P(k, \tau)$ denote the probability of observing exactly $k$ arrivals during an interval of duration $\tau$. The Poisson process with arrival rate (or intensity) $\lambda > 0$ is characterized by three core assumptions:

1. **Time homogeneity:** The distribution of the number of arrivals in any interval depends only on the length $\tau$ of that interval, not on its location along the time axis.
2. **Independent increments:** The numbers of arrivals in disjoint time intervals are independent random variables.
3. **Small-interval probabilities:** For an extremely small interval of length $\delta \to 0$, the probability of an arrival is proportional to $\delta$, while multiple arrivals are negligible:
   $$P(k, \delta) \approx \begin{cases} 1 - \lambda\delta, & \text{if } k = 0, \\ \lambda\delta, & \text{if } k = 1, \\ 0, & \text{if } k > 1. \end{cases}$$

More precisely, $P(1, \delta) = \lambda\delta + o(\delta)$ and $\sum_{k=2}^\infty P(k, \delta) = o(\delta)$, meaning:
$$\lim_{\delta \to 0} \frac{P(1, \delta)}{\delta} = \lambda, \quad \text{and} \quad \lim_{\delta \to 0} \frac{P(k, \delta)}{\delta} = 0 \quad (k \ge 2).$$

The parameter $\lambda$ represents the expected number of arrivals per unit time. Over a small duration $\delta$, the expected number of arrivals is:
$$\mathbf{E}[N_\delta] \approx 1 \cdot (\lambda\delta) + 0 \cdot (1 - \lambda\delta) = \lambda\delta.$$

## Number of Arrivals in an Interval

To find the distribution of the total number of arrivals $N_\tau$ over an interval of arbitrary length $\tau$, we subdivide $[0, \tau]$ into $n = \tau/\delta$ non-overlapping subintervals of length $\delta$.

Because disjoint intervals are independent and each holds at most one arrival with probability $p \approx \lambda\delta = \lambda\tau/n$, the process across these $n$ subintervals is approximately a Bernoulli process with $n$ trials and success probability $p$. The count of arrivals $N_\tau$ is approximately binomial:
$$P(k, \tau) \approx \binom{n}{k} p^k (1 - p)^{n - k} = \binom{n}{k} \left(\frac{\lambda\tau}{n}\right)^k \left(1 - \frac{\lambda\tau}{n}\right)^{n - k}.$$

Taking the limit as $\delta \to 0$, or equivalently $n \to \infty$ while holding the expected number of arrivals $np = \lambda\tau$ constant:
$$\lim_{n \to \infty} \binom{n}{k} \left(\frac{\lambda\tau}{n}\right)^k = \lim_{n \to \infty} \frac{n(n-1)\cdots(n-k+1)}{n^k} \frac{(\lambda\tau)^k}{k!} = \frac{(\lambda\tau)^k}{k!},$$
and
$$\lim_{n \to \infty} \left(1 - \frac{\lambda\tau}{n}\right)^{n - k} = \lim_{n \to \infty} \left(1 - \frac{\lambda\tau}{n}\right)^n \left(1 - \frac{\lambda\tau}{n}\right)^{-k} = e^{-\lambda\tau} \cdot 1 = e^{-\lambda\tau}.$$

Multiplying these factors yields the **Poisson probability mass function**:
$$P(k, \tau) = \frac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}, \quad k = 0, 1, 2, \dots$$

### Mean and Variance

For a discrete binomial random variable, the mean is $np$ and the variance is $np(1 - p)$. Under the limiting regime $n \to \infty$ and $p \to 0$ with $np = \lambda t$:
$$\mathbf{E}[N_t] = \lim_{n \to \infty} np = \lambda t,$$
$$\operatorname{var}(N_t) = \lim_{n \to \infty} np(1 - p) = \lambda t \lim_{p \to 0}(1 - p) = \lambda t.$$
For a Poisson random variable, the mean and the variance are equal to each other, both scaling linearly with the duration of the observation window.

### Example: Email Arrivals

Suppose emails arrive according to a Poisson process at a rate of $\lambda = 5$ messages per hour. You check your inbox after a 30-minute window ($t = 0.5$ hours). The expected number of messages is:
$$\lambda t = 5 \times 0.5 = 2.5.$$

The probability of receiving no new messages during this half-hour is:
$$P(0, 0.5) = \frac{(2.5)^0 e^{-2.5}}{0!} = e^{-2.5} \approx 0.082.$$

The probability of receiving exactly one new message is:
$$P(1, 0.5) = \frac{(2.5)^1 e^{-2.5}}{1!} = 2.5 e^{-2.5} \approx 0.205.$$

## Interarrival Times and the Erlang Distribution

Let $Y_1$ be the time until the first arrival, and let $Y_k$ denote the time elapsed from the origin until the $k$-th arrival occurs.

<figure>
<svg viewBox="0 0 420 120" role="img" aria-label="Timeline showing interarrival times T1, T2 and the arrival time Yk">
  <defs>
    <marker id="arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="80" x2="390" y2="80" stroke="currentColor" stroke-width="1.5" marker-end="url(#arr)"/>
  <line x1="40" y1="75" x2="40" y2="85" stroke="currentColor" stroke-width="1.5"/>
  <text x="37" y="98" font-size="12" fill="currentColor">0</text>
  <!-- First arrival -->
  <line x1="120" y1="75" x2="120" y2="85" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="120" cy="80" r="3" fill="currentColor"/>
  <text x="115" y="98" font-size="12" fill="currentColor">Y₁</text>
  <!-- Second arrival -->
  <line x1="220" y1="75" x2="220" y2="85" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="220" cy="80" r="3" fill="currentColor"/>
  <text x="215" y="98" font-size="12" fill="currentColor">Y₂</text>
  <!-- kth arrival -->
  <line x1="340" y1="75" x2="340" y2="85" stroke="currentColor" stroke-width="1.5"/>
  <circle cx="340" cy="80" r="3" fill="currentColor"/>
  <text x="335" y="98" font-size="12" fill="currentColor">Y_k</text>
  <!-- Interval T1 -->
  <line x1="40" y1="55" x2="120" y2="55" stroke="currentColor" stroke-width="1"/>
  <text x="76" y="48" font-size="12" fill="currentColor">T₁</text>
  <!-- Interval T2 -->
  <line x1="120" y1="55" x2="220" y2="55" stroke="currentColor" stroke-width="1"/>
  <text x="166" y="48" font-size="12" fill="currentColor">T₂</text>
</svg>
<figcaption>Interarrival times $T_i$ and cumulative arrival times $Y_k = T_1 + \dots + T_k$.</figcaption>
</figure>

### Distribution of the First Arrival Time

The first arrival occurs after time $t$ if and only if there are zero arrivals in the interval $[0, t]$:
$$\mathbf{P}(Y_1 > t) = P(0, t) = e^{-\lambda t}, \quad t \ge 0.$$
The cumulative distribution function is $F_{Y_1}(t) = 1 - e^{-\lambda t}$. Differentiating with respect to $t$ gives the probability density function:
$$f_{Y_1}(t) = \lambda e^{-\lambda t}, \quad t \ge 0.$$
The time until the first arrival is an **exponential random variable** with parameter $\lambda$.

### Memorylessness and Interarrival Times

Just as in the Bernoulli process, the Poisson process has no memory. If you begin observing the process at an arbitrary time $t$ (or immediately after an arrival has occurred), the future evolution is statistically identical to a fresh Poisson process started at time 0.

Consequently, if $T_k = Y_k - Y_{k-1}$ is the $k$-th interarrival time (with $Y_0 = 0$), then $T_1, T_2, \dots, T_k$ are **independent and identically distributed** exponential random variables, each with parameter $\lambda$.

This gives an efficient method for simulating a Poisson process: instead of finely discretizing time into small bins $\delta$, generate independent exponential variables $T_i \sim \operatorname{Exponential}(\lambda)$ and set each successive arrival time to $Y_k = \sum_{i=1}^k T_i$.

### Distribution of the $k$-th Arrival Time (Erlang Distribution)

Because $Y_k = T_1 + T_2 + \dots + T_k$, the total time to the $k$-th arrival is the sum of $k$ independent, identically distributed exponential random variables. We can find its PDF directly using an interval argument.

Consider an infinitesimal interval $[y, y + \delta]$. For the $k$-th arrival to occur in this window, two independent events must occur simultaneously (ignoring $o(\delta)$ terms):
1. Exactly $k - 1$ arrivals occur during $[0, y]$.
2. Exactly 1 arrival occurs during $[y, y + \delta]$.

Therefore:
$$f_{Y_k}(y)\delta \approx P(k - 1, y) \cdot P(1, \delta) = \left( \frac{(\lambda y)^{k-1} e^{-\lambda y}}{(k - 1)!} \right) (\lambda \delta).$$

Dividing by $\delta$ gives the **Erlang distribution** of order $k$:
$$f_{Y_k}(y) = \frac{\lambda^k y^{k-1} e^{-\lambda y}}{(k - 1)!}, \quad y \ge 0.$$

For $k = 1$, this expression reduces directly to $f_{Y_1}(y) = \lambda e^{-\lambda y}$, the exponential PDF.

## Bernoulli and Poisson Correspondence

The Poisson process is the continuous-time analog of the Bernoulli process. Every fundamental concept in the discrete-time Bernoulli process translates directly to a counterpart in continuous time:

| Property | Bernoulli Process | Poisson Process |
| :--- | :---: | :---: |
| **Times of arrival** | Discrete ($n = 1, 2, \dots$) | Continuous ($t \ge 0$) |
| **Arrival rate** | $p$ per trial | $\lambda$ per unit time |
| **Arrivals in duration $\tau$** | Binomial PMF: $\binom{n}{k} p^k (1-p)^{n-k}$ | Poisson PMF: $\frac{(\lambda\tau)^k e^{-\lambda\tau}}{k!}$ |
| **Interarrival time $T_1$** | Geometric PMF: $p(1-p)^{t-1}$ | Exponential PDF: $\lambda e^{-\lambda y}$ |
| **Time of $k$-th arrival $Y_k$** | Pascal PMF: $\binom{t-1}{k-1} p^k (1-p)^{t-k}$ | Erlang PDF: $\frac{\lambda^k y^{k-1} e^{-\lambda y}}{(k-1)!}$ |

## Merging Poisson Processes

Consider two independent Poisson processes: Process 1 with rate $\lambda_1$, and Process 2 with rate $\lambda_2$. Suppose the arrivals from both processes are recorded together into a single merged process.

<figure>
<svg viewBox="0 0 420 150" role="img" aria-label="Two Poisson processes merged into a single process">
  <defs>
    <marker id="marr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="currentColor"/>
    </marker>
  </defs>
  <!-- Process 1 -->
  <text x="25" y="34" font-size="12" fill="currentColor">Process 1 (&#955;₁)</text>
  <line x1="140" y1="30" x2="390" y2="30" stroke="currentColor" stroke-width="1.5" marker-end="url(#marr)"/>
  <circle cx="190" cy="30" r="3.5" fill="currentColor"/>
  <circle cx="310" cy="30" r="3.5" fill="currentColor"/>
  <!-- Process 2 -->
  <text x="25" y="74" font-size="12" fill="currentColor">Process 2 (&#955;₂)</text>
  <line x1="140" y1="70" x2="390" y2="70" stroke="currentColor" stroke-width="1.5" marker-end="url(#marr)"/>
  <circle cx="250" cy="70" r="3.5" fill="currentColor"/>
  <circle cx="350" cy="70" r="3.5" fill="currentColor"/>
  <!-- Merged -->
  <text x="25" y="114" font-size="12" fill="currentColor">Merged</text>
  <line x1="140" y1="110" x2="390" y2="110" stroke="currentColor" stroke-width="1.5" marker-end="url(#marr)"/>
  <circle cx="190" cy="110" r="3.5" fill="currentColor"/>
  <circle cx="250" cy="110" r="3.5" fill="currentColor"/>
  <circle cx="310" cy="110" r="3.5" fill="currentColor"/>
  <circle cx="350" cy="110" r="3.5" fill="currentColor"/>
</svg>
<figcaption>Superposition of two independent Poisson streams yields a new Poisson stream with rate $\lambda_1 + \lambda_2$.</figcaption>
</figure>

To determine the properties of the merged stream, examine a small interval of length $\delta$:
- An arrival occurs in Process 1 with probability $\lambda_1 \delta + o(\delta)$, and does not occur with probability $1 - \lambda_1 \delta + o(\delta)$.
- An arrival occurs in Process 2 with probability $\lambda_2 \delta + o(\delta)$, and does not occur with probability $1 - \lambda_2 \delta + o(\delta)$.

By independence, the probabilities of joint events in this interval are:
- **Arrival in both processes:** $(\lambda_1 \delta)(\lambda_2 \delta) = \lambda_1 \lambda_2 \delta^2 = o(\delta)$.
- **Arrival only in Process 1:** $(\lambda_1 \delta)(1 - \lambda_2 \delta) = \lambda_1 \delta + o(\delta)$.
- **Arrival only in Process 2:** $(1 - \lambda_1 \delta)(\lambda_2 \delta) = \lambda_2 \delta + o(\delta)$.
- **No arrivals in either process:** $(1 - \lambda_1 \delta)(1 - \lambda_2 \delta) = 1 - (\lambda_1 + \lambda_2)\delta + o(\delta)$.

The probability of an arrival in the merged process during interval $\delta$ is:
$$\mathbf{P}(\text{arrival in merged}) = \lambda_1 \delta + \lambda_2 \delta + o(\delta) = (\lambda_1 + \lambda_2)\delta + o(\delta).$$

Disjoint intervals remain independent, and time homogeneity is preserved. Thus, the merged stream is itself a **Poisson process** with rate:
$$\lambda = \lambda_1 + \lambda_2.$$

Furthermore, if an arrival is recorded in the merged stream, the conditional probability that it originated from Process 1 is the ratio of their small-interval rates:
$$\mathbf{P}(\text{from Process 1} \mid \text{arrival}) = \frac{\lambda_1 \delta}{(\lambda_1 + \lambda_2)\delta} = \frac{\lambda_1}{\lambda_1 + \lambda_2}.$$
Similarly, the probability that it came from Process 2 is $\frac{\lambda_2}{\lambda_1 + \lambda_2}$.

## Exercises

1. You are visiting the rainforest, but unfortunately your insect repellent has run out. As a result, at each second, a mosquito lands on your neck with probability $0.5$. If one lands, with probability $0.2$ it bites you, and with probability $0.8$ it never bothers you, independently of other mosquitoes.
   (a) What is the expected time between successive mosquito bites? What is the variance of the time between successive mosquito bites?
   (b) In addition, a tick lands on your neck with probability $0.1$. If one lands, with probability $0.7$ it bites you, and with probability $0.3$, it never bothers you, independently of other ticks and mosquitoes. Now, what is the expected time between successive bug bites? What is the variance of the time between successive bug bites?

2. Al performs an experiment comprising a series of independent trials. On each trial, he simultaneously flips a set of three fair coins.
   (a) Given that Al has just had a trial with 3 tails, what is the probability that both of the next two trials will also have this result?
   (b) Whenever all three coins land on the same side in any given trial, Al calls the trial a success.
       i. Find the PMF for $K$, the number of trials up to, but **not** including, the second success.
       ii. Find the expectation and variance of $M$, the number of tails that occur **before** the first success.
   (c) Bob conducts an experiment like Al's, except that he uses 4 coins for the first trial, and then he obeys the following rule: Whenever all of the coins land on the same side in a trial, Bob permanently removes one coin from the experiment and continues with the trials. He follows this rule until the **third** time he removes a coin, at which point the experiment ceases. Find $\mathbf{E}[N]$, where $N$ is the number of trials in Bob's experiment.

3. Suppose there are $n$ papers in a drawer. You draw a paper and sign it, and then, instead of filing it away, you place the paper back into the drawer. If any paper is equally likely to be drawn each time, independent of all other draws, what is the expected number of papers that you will draw before signing all $n$ papers? You may leave your answer in the form of a summation.

## Sources

- MIT OpenCourseWare 6.041SC (Fall 2013), Lecture 14: The Poisson Process (slides and lecture transcript).
- MIT OpenCourseWare 6.041 (Fall 2010), Recitation 14 problem set.

---

[← 13. The Bernoulli Process](13-the-bernoulli-process.md) · [Contents](index.md) · [15. Poisson Processes: Merging, Splitting, and Random Incidence →](15-poisson-processes-merging-splitting-and-random-incidence.md)
