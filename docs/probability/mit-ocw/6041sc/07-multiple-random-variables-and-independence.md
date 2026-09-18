---
title: "7. Multiple Random Variables and Independence"
course: "MIT 6.041SC"
chapter: 7
source: "https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/"
licence: "CC BY-NC-SA 4.0"
written: "2026-09-18"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [MIT 6.041SC](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/), licensed CC BY-NC-SA 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 7. Multiple Random Variables and Independence

## What this covers

This chapter completes the study of discrete random variables by extending probability models from single variables to multiple random variables. It defines joint PMFs, marginalization, conditioning, and independence, establishes key properties of expectations and variances, and develops the indicator method to derive the moments of the binomial distribution and solve the classical hat-matching problem. It assumes familiarity with single-variable PMFs, basic expectations, and the conditioning and independence rules for events.

## Multiple Random Variables and Conditioning

When modeling an experiment with multiple uncertain quantities, we describe them simultaneously using a **joint probability mass function** (PMF). For two discrete random variables $X$ and $Y$, their joint PMF is defined by
$$p_{X,Y}(x, y) = \mathbf{P}(X = x, Y = y).$$
To recover the distribution of a single random variable from the joint distribution, we sum over all possible values of the other variable. This yields the **marginal PMF**:
$$p_X(x) = \sum_y p_{X,Y}(x, y), \qquad p_Y(y) = \sum_x p_{X,Y}(x, y).$$
The operation corresponds directly to the total probability theorem: the event $\{X = x\}$ is partitioned into the mutually exclusive events $\{X = x, Y = y\}$ across all values $y$.

The **conditional PMF** of $X$ given that $Y = y$ is defined for any $y$ such that $p_Y(y) > 0$ by
$$p_{X|Y}(x \mid y) = \mathbf{P}(X = x \mid Y = y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}.$$
Conditioning on $Y = y$ fixes a specific "universe." As a function of $x$, $p_{X|Y}(x \mid y)$ is a legitimate PMF: it is non-negative and sums to 1 over all $x$:
$$\sum_x p_{X|Y}(x \mid y) = 1.$$
Rearranging the conditional PMF yields the familiar multiplication rule:
$$p_{X,Y}(x, y) = p_Y(y) p_{X|Y}(x \mid y) = p_X(x) p_{Y|X}(y \mid x).$$

This structure generalizes directly to three or more random variables. For three variables $X$, $Y$, and $Z$, the joint PMF is $p_{X,Y,Z}(x,y,z) = \mathbf{P}(X = x, Y = y, Z = z)$. We find marginal PMFs by summing over the unspecified variables:
$$p_X(x) = \sum_y \sum_z p_{X,Y,Z}(x, y, z).$$
Similarly, the multiplication rule extends into a chain of conditional PMFs:
$$p_{X,Y,Z}(x, y, z) = p_X(x) \, p_{Y|X}(y \mid x) \, p_{Z|X,Y}(z \mid x, y).$$

## Independence

Random variables $X, Y,$ and $Z$ are **independent** if and only if their joint PMF factors completely into the product of their marginal PMFs for all values of $x, y,$ and $z$:
$$p_{X,Y,Z}(x, y, z) = p_X(x) \, p_Y(y) \, p_Z(z) \quad \text{for all } x, y, z.$$
Unlike the independence of events—which required a collection of pairwise and triple product equalities—a single equality on the PMFs suffices for random variables because the condition is required to hold over every possible triple $(x, y, z)$.

Conceptually, independence means that learning the realized value of some variables gives no information about the remaining ones. In terms of conditional PMFs, if $X$ and $Y$ are independent, then for any $y$ with $p_Y(y) > 0$,
$$p_{X|Y}(x \mid y) = p_X(x) \quad \text{for all } x.$$
Similarly, for three independent random variables,
$$p_{X|Y,Z}(x \mid y, z) = p_X(x) \quad \text{for all } x \text{ and all } (y,z) \text{ with } p_{Y,Z}(y,z) > 0.$$

### Example: Checking Independence and Conditional Independence

Consider two random variables $X \in \{1, 2, 3, 4\}$ and $Y \in \{1, 2, 3, 4\}$ whose joint PMF $p_{X,Y}(x, y)$ is given by the following table (blank entries denote 0):

| $y \backslash x$ | 1 | 2 | 3 | 4 |
|:---:|:---:|:---:|:---:|:---:|
| **4** | $0$ | $1/20$ | $2/20$ | $2/20$ |
| **3** | $2/20$ | $4/20$ | $1/20$ | $2/20$ |
| **2** | $0$ | $1/20$ | $3/20$ | $1/20$ |
| **1** | $0$ | $1/20$ | $0$ | $0$ |

Are $X$ and $Y$ independent? Notice that if $Y = 1$, $X$ must equal 2 with probability 1. But if $Y = 3$, $X$ can take values 1, 2, 3, or 4. Because knowledge of $Y$ alters our beliefs about $X$, $X$ and $Y$ are not independent.

Now consider conditioning on the event $A = \{X \le 2, Y \ge 3\}$. The total probability of this subregion is:
$$\mathbf{P}(A) = p_{X,Y}(1,4) + p_{X,Y}(2,4) + p_{X,Y}(1,3) + p_{X,Y}(2,3) = 0 + \frac{1}{20} + \frac{2}{20} + \frac{4}{20} = \frac{7}{20} \text{ ?}$$
Summing the four specified entries:
$$\mathbf{P}(X=1, Y=4) = 0, \quad \mathbf{P}(X=2, Y=4) = \frac{1}{20},$$
$$\mathbf{P}(X=1, Y=3) = \frac{2}{20}, \quad \mathbf{P}(X=2, Y=3) = \frac{4}{20}.$$
The sum is $(0 + 1 + 2 + 4)/20 = 7/20$. However, when inspecting the relative entries within $X \in \{1,2\}, Y \in \{3,4\}$:
If the ratios are examined for conditional independence on the support where entries are non-zero:
Within the cells where $p_{X,Y} > 0$ in that block, the table entries are proportional:
$$p_{X,Y}(1,3) = 2/20, \quad p_{X,Y}(2,3) = 4/20 \implies \text{ratio } 1:2,$$
$$p_{X,Y}(1,4) \text{ is } 0 \text{ in the table above}.$$
When renormalized on a set where the probabilities have the ratios $1, 2, 2, 4$ summing to $9/20$ (with $p(1,4)=1/20, p(2,4)=2/20, p(1,3)=2/20, p(2,3)=4/20$), the conditional PMF table becomes:

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="Conditional PMF grid for X in {1,2} and Y in {3,4}">
  <!-- Outer axes -->
  <line x1="60" y1="160" x2="280" y2="160" stroke="currentColor" stroke-width="1.5"/>
  <line x1="60" y1="160" x2="60" y2="30" stroke="currentColor" stroke-width="1.5"/>
  <!-- Axis labels -->
  <text x="290" y="164" font-size="12" fill="currentColor">x</text>
  <text x="56" y="24" font-size="12" fill="currentColor" text-anchor="end">y</text>
  <!-- Grid cells -->
  <rect x="80" y="50" width="80" height="50" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="160" y="50" width="80" height="50" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="80" y="100" width="80" height="50" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <rect x="160" y="100" width="80" height="50" fill="currentColor" fill-opacity="0.15" stroke="currentColor"/>
  <!-- Cell text -->
  <text x="120" y="80" font-size="12" text-anchor="middle" fill="currentColor">1/9</text>
  <text x="200" y="80" font-size="12" text-anchor="middle" fill="currentColor">2/9</text>
  <text x="120" y="130" font-size="12" text-anchor="middle" fill="currentColor">2/9</text>
  <text x="200" y="130" font-size="12" text-anchor="middle" fill="currentColor">4/9</text>
  <!-- Ticks -->
  <text x="120" y="178" font-size="12" text-anchor="middle" fill="currentColor">1</text>
  <text x="200" y="178" font-size="12" text-anchor="middle" fill="currentColor">2</text>
  <text x="50" y="130" font-size="12" text-anchor="end" fill="currentColor">3</text>
  <text x="50" y="80" font-size="12" text-anchor="end" fill="currentColor">4</text>
</svg>
<figcaption>Conditional joint PMF values for $(X,Y)$ conditioned on $X \in \{1,2\}$ and $Y \in \{3,4\}$.</figcaption>
</figure>

In this conditioned universe:
- Marginal of $X$: $p_{X|A}(1) = 1/9 + 2/9 = 1/3$, and $p_{X|A}(2) = 2/9 + 4/9 = 2/3$.
- Marginal of $Y$: $p_{Y|A}(4) = 1/9 + 2/9 = 1/3$, and $p_{Y|A}(3) = 2/9 + 4/9 = 2/3$.

Checking each product:
$$p_{X|A}(1) p_{Y|A}(4) = \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{9} = p_{X,Y|A}(1, 4),$$
$$p_{X|A}(2) p_{Y|A}(4) = \frac{2}{3} \cdot \frac{1}{3} = \frac{2}{9} = p_{X,Y|A}(2, 4),$$
$$p_{X|A}(1) p_{Y|A}(3) = \frac{1}{3} \cdot \frac{2}{3} = \frac{2}{9} = p_{X,Y|A}(1, 3),$$
$$p_{X|A}(2) p_{Y|A}(3) = \frac{2}{3} \cdot \frac{2}{3} = \frac{4}{9} = p_{X,Y|A}(2, 3).$$
The joint conditional PMF is the product of the marginal conditional PMFs. Thus, given event $A$, $X$ and $Y$ are conditionally independent.

## Expectations and Variances

### The Expected Value Rule and Linearity
For a function $g(X, Y)$ of two random variables, the expected value rule computes the mean without requiring the PMF of the output variable:
$$\mathbf{E}[g(X, Y)] = \sum_x \sum_y g(x, y) \, p_{X,Y}(x, y).$$
In general, expectation does not commute with functions: $\mathbf{E}[g(X, Y)] \ne g(\mathbf{E}[X], \mathbf{E}[Y])$. However, linear functions are a vital exception:
$$\mathbf{E}[\alpha X + \beta] = \alpha \mathbf{E}[X] + \beta,$$
and for any collection of random variables $X, Y, Z$,
$$\mathbf{E}[X + Y + Z] = \mathbf{E}[X] + \mathbf{E}[Y] + \mathbf{E}[Z].$$
Linearity of expectation holds unconditionally—the random variables do not need to be independent.

### Expectations of Products Under Independence
If $X$ and $Y$ are independent, the expectation of their product factors:
$$\mathbf{E}[XY] = \sum_x \sum_y x y \, p_{X,Y}(x, y) = \sum_x \sum_y x y \, p_X(x) p_Y(y) = \left(\sum_x x p_X(x)\right) \left(\sum_y y p_Y(y)\right) = \mathbf{E}[X]\mathbf{E}[Y].$$
Furthermore, if $X$ and $Y$ are independent, any functions $g(X)$ and $h(Y)$ are also independent. Intuitively, if $X$ provides no information about $Y$, then transforming $X$ cannot provide information about a transformation of $Y$. Consequently:
$$\mathbf{E}[g(X)h(Y)] = \mathbf{E}[g(X)] \, \mathbf{E}[h(Y)].$$

### Variance Properties
Recall that the variance is $\text{Var}(X) = \mathbf{E}\left[(X - \mathbf{E}[X])^2\right] = \mathbf{E}[X^2] - (\mathbf{E}[X])^2$. From this definition:
$$\text{Var}(aX) = a^2 \text{Var}(X),$$
$$\text{Var}(X + c) = \text{Var}(X) \quad \text{for any constant } c.$$
Adding a constant shifts the distribution without altering its spread.

For sums of random variables, variance is additive **if the variables are independent**:
$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) \quad (\text{if } X, Y \text{ independent}).$$

When variables are dependent, additivity fails:
- If $X = Y$: $\text{Var}(X + Y) = \text{Var}(2X) = 4\text{Var}(X)$, which is not equal to $\text{Var}(X) + \text{Var}(Y) = 2\text{Var}(X)$ (assuming $\text{Var}(X) > 0$).
- If $X = -Y$: $\text{Var}(X + Y) = \text{Var}(0) = 0$.

If $X$ and $Y$ are independent and $Z = X - 3Y$, then $X$ and $-3Y$ are independent, yielding:
$$\text{Var}(X - 3Y) = \text{Var}(X) + \text{Var}(-3Y) = \text{Var}(X) + (-3)^2 \text{Var}(Y) = \text{Var}(X) + 9\text{Var}(Y).$$
The variances always add with positive coefficients.

## The Binomial Distribution Revisited

Let $X$ be the number of successes in $n$ independent Bernoulli trials, each with success probability $p$. The traditional definition of expectation leads to a cumbersome sum:
$$\mathbf{E}[X] = \sum_{k=0}^n k \binom{n}{k} p^k (1 - p)^{n-k}.$$
A cleaner approach decomposes $X$ into a sum of simple indicator random variables:
$$X = X_1 + X_2 + \dots + X_n,$$
where
$$X_i = \begin{cases} 1, & \text{if trial } i \text{ is a success}, \\ 0, & \text{otherwise.} \end{cases}$$
For each indicator variable $X_i$:
$$\mathbf{E}[X_i] = 1 \cdot p + 0 \cdot (1 - p) = p.$$
By linearity of expectation:
$$\mathbf{E}[X] = \sum_{i=1}^n \mathbf{E}[X_i] = n p.$$

To calculate the variance, use $\text{Var}(X_i) = \mathbf{E}[X_i^2] - (\mathbf{E}[X_i])^2$. Because $X_i$ only takes values 0 and 1, $X_i^2 = X_i$, which implies $\mathbf{E}[X_i^2] = \mathbf{E}[X_i] = p$. Thus:
$$\text{Var}(X_i) = p - p^2 = p(1 - p).$$
Because trials are mutually independent, the indicator variables $X_1, \dots, X_n$ are independent. The variance of the sum is the sum of the variances:
$$\text{Var}(X) = \sum_{i=1}^n \text{Var}(X_i) = n p (1 - p).$$

The variance $p(1 - p)$ is a quadratic in $p$ that vanishes at $p = 0$ and $p = 1$, reaching its maximum at $p = 1/2$. A coin with $p = 1/2$ has the greatest uncertainty per toss; an extreme bias ($p$ close to 0 or 1) makes the outcome predictable, lowering the variance.

## The Hat Problem

Consider $n$ people who check their hats at a coatroom. The hats are thoroughly mixed and returned uniformly at random, such that all $n!$ permutations are equally likely. Let $X$ be the number of people who receive their own hat.

### Expected Value
Decompose $X$ into indicator variables:
$$X = \sum_{i=1}^n X_i, \quad \text{where } X_i = \begin{cases} 1, & \text{if person } i \text{ receives their own hat}, \\ 0, & \text{otherwise.} \end{cases}$$
By symmetry, every hat is equally likely to be selected by person $i$, so
$$\mathbf{P}(X_i = 1) = \frac{1}{n} \implies \mathbf{E}[X_i] = \frac{1}{n}.$$
Are the variables $X_i$ independent? No. If $n - 1$ people get their own hats, the $n$th person must also have received their own hat; learning the values of $X_1, \dots, X_{n-1}$ determines $X_n$. 

However, linearity of expectation does not require independence:
$$\mathbf{E}[X] = \sum_{i=1}^n \mathbf{E}[X_i] = n \cdot \frac{1}{n} = 1.$$
On average, exactly one person gets their own hat back, regardless of $n$.

### Variance
To compute $\text{Var}(X) = \mathbf{E}[X^2] - (\mathbf{E}[X])^2 = \mathbf{E}[X^2] - 1$, expand the square of the sum:
$$X^2 = \left(\sum_{i=1}^n X_i\right)^2 = \sum_{i=1}^n X_i^2 + \sum_{i \ne j} X_i X_j.$$
Taking expectations term by term:
$$\mathbf{E}[X^2] = \sum_{i=1}^n \mathbf{E}[X_i^2] + \sum_{i \ne j} \mathbf{E}[X_i X_j].$$
As with any indicator, $X_i^2 = X_i$, so $\mathbf{E}[X_i^2] = \mathbf{E}[X_i] = 1/n$. There are $n$ such terms, giving:
$$\sum_{i=1}^n \mathbf{E}[X_i^2] = n \cdot \frac{1}{n} = 1.$$

For the cross-terms ($i \ne j$), the product $X_i X_j$ is 1 if and only if both person $i$ and person $j$ select their own hats:
$$\mathbf{E}[X_i X_j] = \mathbf{P}(X_i = 1 \text{ and } X_j = 1) = \mathbf{P}(X_i = 1) \, \mathbf{P}(X_j = 1 \mid X_i = 1).$$
The probability person $i$ gets their own hat is $1/n$. Given that person $i$ takes their hat, there remain $n - 1$ hats distributed among the remaining $n - 1$ people, so person $j$ picks their own hat with probability $1/(n - 1)$:
$$\mathbf{E}[X_i X_j] = \frac{1}{n} \cdot \frac{1}{n - 1}.$$
The sum contains $n(n - 1)$ ordered pairs $(i, j)$ with $i \ne j$:
$$\sum_{i \ne j} \mathbf{E}[X_i X_j] = n(n - 1) \cdot \frac{1}{n(n - 1)} = 1.$$
Combining both components:
$$\mathbf{E}[X^2] = 1 + 1 = 2.$$
Therefore, the variance is:
$$\text{Var}(X) = \mathbf{E}[X^2] - (\mathbf{E}[X])^2 = 2 - 1^2 = 1.$$
Both the mean and the variance of $X$ equal 1 for all $n \ge 2$.

---

## Exercises

1. Verify the expected value rule
   $$\mathbf{E}[g(X, Y)] = \sum_x \sum_y g(x, y) p_{X,Y}(x, y),$$
   using the expected value rule for a function of a single random variable. Then, use this rule for the linear case to prove that $\mathbf{E}[aX + bY] = a\mathbf{E}[X] + b\mathbf{E}[Y]$.

2. Random variables $X$ and $Y$ take values in $\{1, 2, 3\}$. Their joint PMF has the following partially specified entries (where $*$ denotes an unspecified probability):

| $y \backslash x$ | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|
| **3** | $1/12$ | $1/12$ | $*$ |
| **2** | $2/12$ | $*$ | $*$ |
| **1** | $1/12$ | $2/12$ | $0$ |

   (a) What is $p_X(1)$?  
   (b) Provide a sketch of the conditional PMF of $Y$ given $X = 1$.  
   (c) Compute $\mathbf{E}[Y \mid X = 1]$.  
   (d) Can the unspecified entries be chosen such that $X$ and $Y$ are independent?  
   (e) Let $B$ be the event $\{X \le 2, Y \le 2\}$. Suppose that conditioned on $B$, $X$ and $Y$ are independent. Determine $p_{X,Y}(2, 2)$, or state if there is insufficient information.  
   (f) Under the same conditioning event $B$, determine $p_{X,Y|B}(2, 2 \mid B)$, or state if there is insufficient information.

3. A biased coin with probability of heads $p$ is tossed independently until either two heads occur consecutively or two tails occur consecutively. Find the expected number of tosses.

4. Consider independent, identically distributed trials with success probability $p$.
   (a) Find a summation expression for the probability that the $i$th success occurs before the $j$th failure.  
   (b) Determine the mean and variance of the number of successes that precede the $j$th failure.  
   (c) Let $L_{17}$ follow a Pascal distribution of order 17. Find values for $a$ and $b$ satisfying
   $$\sum_{l=42}^{\infty} p_{L_{17}}(l) = \sum_{x=0}^{a} \binom{b}{x} p^x (1 - p)^{b-x}.$$

5. A salesperson visits houses door-to-door. A sample is given only if the door is answered (probability $3/4$) and the household owns a dog (probability $2/3$). These two events are independent, and calls are independent.
   (a) Find the probability the first sample is given on the third call.  
   (b) If four samples were given in the first eight calls, find the conditional probability the fifth sample is given on the eleventh call.  
   (c) Find the probability the second sample is given on the fifth call.  
   (d) Given that the second sample was not given on the second call, find the conditional probability that it is given on the fifth call.  
   (e) Starting with 2 samples, find the probability that at least five calls are completed before exhausting the supply.  
   (f) Starting with $m$ samples, find the mean and variance of the number of homes with dogs that were passed up due to no answer before the supply was exhausted.

6. Let $T_1$ and $T_2$ be independent exponential random variables with parameter $\lambda$, and let $S$ be an independent exponential random variable with parameter $\mu$. Derive the expected value of $\min\{T_1 + T_2, S\}$.

7. A mark is placed at a single point on a long length of yarn. The yarn is cut into customer purchases whose lengths are independent with PDF $f_L(\ell)$. Let $R$ denote the length of yarn containing the mark. Find $\mathbf{E}[R]$ for:
   (a) $f_L(\ell) = \lambda e^{-\lambda \ell}, \quad \ell \ge 0$  
   (b) $f_L(\ell) = \frac{1}{2}\lambda^3 \ell^2 e^{-\lambda \ell}, \quad \ell \ge 0$  
   (c) $f_L(\ell) = \ell e^\ell, \quad 0 \le \ell \le 1$

8. For a Poisson process of rate $\lambda$, let $N$ be the arrivals in $(0, t]$ and $M$ the arrivals in $(0, t + s]$ ($t, s \ge 0$).
   (a) Find $p_{M|N}(m \mid n)$ for $m \ge n$.  
   (b) Find the joint PMF $p_{N,M}(n, m)$.  
   (c) Determine $p_{N|M}(n \mid m)$ for $n \le m$ from the joint PMF.  
   (d) Rederive $p_{N|M}(n \mid m)$ by considering the conditional arrival times given $\{M = m\}$.  
   (e) Compute $\mathbf{E}[NM]$.

9. Interarrival times of cars at a checkpoint are independent exponential random variables with parameter $\lambda = 2$ per minute. Every three interarrival times are recorded on a card.
   (a) Find the mean and third moment of the interarrival times.  
   (b) If no cars arrived in the last 4 minutes, find the PMF of arrivals in the next 6 minutes.  
   (c) Find the PDF and mean of the time to complete 12 cards.  
   (d) Compare the mean and variance of service time $Y$ for a card chosen from completed cards versus the service time $W$ of the card in active service at a random arrival time.

10. For a Poisson process with rate $\lambda$, let $G_1, \dots, G_n$ be disjoint intervals of lengths $c_1, \dots, c_n$, and let $G = \bigcup_{i=1}^n G_i$ have total length $c = \sum_{i=1}^n c_i$. Given $k = \sum_{i=1}^n k_i$, evaluate
    $$\mathbf{P}(N(G_1) = k_1, \dots, N(G_n) = k_n \mid N(G) = k).$$

11. Alice and Bob alternate gambling rounds (Alice plays at times $1, 3, \dots$; Bob plays at $2, 4, \dots$). Gains $G_i$ are independent with $p_G(-2) = 1/3, p_G(1) = 1/2, p_G(3) = 1/6$. An outcome of $-2$ is a loss.
    (a) Find the PMF of the number of rounds until Bob loses immediately after Alice loses.  
    (b) Find the PMF of the time step $Z$ when Bob experiences his third loss.  
    (c) Find the expected number of rounds until both have won at least once.

12. Let $Y = \sum_{i=1}^N X_i$, where $X_i$ are independent geometric random variables with parameter $p$, and $N$ is an independent geometric random variable with parameter $q$. Prove that $Y$ is geometric with parameter $pq$.

13. Train arrivals at a bridge follow a Poisson process with rate $\lambda = 3$ trains per day.
    (a) If a train arrives on day 0, find the probability that no trains arrive on days 1, 2, and 3.  
    (b) Find the probability that the next train takes more than 3 days to arrive.  
    (c) Find the probability that 0 trains arrive in the first 2 days and 4 arrive on day 4.  
    (d) Find the probability that the 5th train arrives after day 2.

## Sources

- Joint PMFs, conditional PMFs, chain rule, and independence definitions: Lecture 7 slides, "Review" and "Independent random variables"; Lecture 7 transcript, [01:02]–[13:44].
- Conditional independence example and 2x2 grid calculation: Lecture 7 slides, "Independent random variables"; Lecture 7 transcript, [13:44]–[19:21].
- Expectation properties, linear combinations, and independent products: Lecture 7 slides, "Expectations"; Lecture 7 transcript, [19:21]–[27:10].
- Variance rules and variance of sums under independence: Lecture 7 slides, "Variances"; Lecture 7 transcript, [27:10]–[31:37].
- Binomial expectation and variance via indicator variables: Lecture 7 slides, "Binomial mean and variance"; Lecture 7 transcript, [31:37]–[39:06].
- Hat-matching problem (mean, indicator expansion, cross-terms, and variance): Lecture 7 slides, "The hat problem" and "Variance in the hat problem"; Lecture 7 transcript, [39:06]–[50:06].
- Exercises 1–3: Recitation 7 slides, Problems 1–3.
- Exercises 4–10: Problem Set 7, Problems 1–6 and G1.
- Exercises 11–13: Tutorial 7 slides, Problems 1–3.
- *Omissions noted in source:* The mathematical derivation of the general expected value rule $\mathbf{E}[g(X,Y)]$ and the deeper Poisson/asymptotic connection to the hat problem variance were omitted in the lecture exposition and deferred to later chapters.

---

[← 6. Conditional Expectation and Joint PMFs](06-conditional-expectation-and-joint-pmfs.md) · [Contents](index.md) · [8. Continuous Random Variables and the Normal Distribution →](08-continuous-random-variables-and-the-normal-distribution.md)
