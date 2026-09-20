---
title: "Solutions — Limit Theorems and Sample Means"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — Limit Theorems and Sample Means

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 19 Solutions: November 16, 2010

1. (a) The Markov chain is shown below.

By inspection, the states 6-1, 6-2, and 6-3 are all transient, since they each have paths leading to either state 9 or state 15, from which there is no return. Therefore she eventually leaves course 6 with probability 1.

(b) This is the absorption probability for the recurrent class consisting of the state course-15. Let us denote the probability of being absorbed by state 15 conditioned on being in state $i$ as $a_i$. Then

$$a_{15} = 1$$
$$a_9 = 0$$
$$a_{6-1} = \frac{1}{2}a_{6-1} + \frac{1}{8}(1) + \frac{1}{8}a_{6-2} + \frac{1}{8}(0) + \frac{1}{8}a_{6-3}$$
$$a_{6-2} = \frac{1}{2}(1) + \frac{3}{8}a_{6-1} + \frac{1}{8}a_{6-3}$$
$$a_{6-3} = \frac{1}{4}(0) + \frac{3}{8}a_{6-1} + \frac{3}{8}a_{6-2}$$

Solving this system of equations yields

$$a_{6-1} = \frac{105}{184} \approx 0.571$$

We will keep the other $a_i$'s around as well - they will be useful later:

$$a_{6-2} = 0.77717$$
$$a_{6-3} = 0.50543$$

---

(c) This is the expected time until absorption for the transient state $6-1$. Let $\mu_i$ be the expected time until absorption conditioned on being in state $i$. Then

$$\mu_{15} = 0$$
$$\mu_9 = 0$$
$$\mu_{6-1} = 1 + \frac{1}{2}\mu_{6-1} + \frac{1}{8}(0) + \frac{1}{8}\mu_{6-2} + \frac{1}{8}(0) + \frac{1}{8}\mu_{6-3}$$
$$\mu_{6-2} = 1 + \frac{1}{2}(0) + \frac{3}{8}\mu_{6-1} + \frac{1}{8}\mu_{6-3}$$
$$\mu_{6-3} = 1 + \frac{1}{4}(0) + \frac{3}{8}\mu_{6-1} + \frac{3}{8}\mu_{6-2}$$

Solving this system of equations yields

$$\mu_{6-1} = \frac{162}{46} = \frac{81}{23} \approx 3.522$$

(d) The student buys one ice cream cone every time she goes from 6-2 to 6-1 or from 6-3 to 6-1, and buys no more than 2 ice cream cones. Let us denote $v_i(j)$ as the conditional probability that given that she is in state $i$, that she transitions from $6-2$ to $6-1$ or from $6-3$ to $6-1$ $j$ additional times. Then we are interested in the expected value of the random variable $N$, which denotes the number of cones bought before leaving course 6, and takes on the values 0, 1, or 2. So

$$E[N] = (0)v_{6-1}(0) + (1)v_{6-1}(1) + (2)(1 - v_{6-1}(0) - v_{6-1}(1))$$

We use the total probability theorem, conditioning on the next day, to yield the following set of equations:

$$v_{15}(0) = 1$$
$$v_9(0) = 1$$
$$v_{6-1}(0) = \frac{1}{2}v_{6-1}(0) + \frac{1}{8}v_{6-2}(0) + \frac{1}{8}v_{6-3}(0) + \frac{1}{8}(1) + \frac{1}{8}(1)$$
$$v_{6-2}(0) = \frac{3}{8}(0) + \frac{1}{8}v_{6-3}(0) + \frac{1}{2}(1)$$
$$v_{6-3}(0) = \frac{3}{8}(0) + \frac{3}{8}v_{6-2}(0) + \frac{1}{4}(1)$$

Solving this system of equations yields:

$$v_{6-1}(0) = \frac{46}{61} \approx 0.754$$

We still need to find $v_{6-1}(1)$, and we do this by again conditioning on the following day and solving the following set of equations:

$$v_{6-1}(1) = \frac{1}{2}v_{6-1}(1) + \frac{1}{8}v_{6-2}(1) + \frac{1}{8}v_{6-3}(1) + \frac{1}{8}(0) + \frac{1}{8}(0)$$
$$v_{6-2}(1) = \frac{3}{8}v_{6-1}(0) + \frac{1}{8}v_{6-3}(1) + \frac{1}{2}(0)$$
$$v_{6-3}(1) = \frac{3}{8}v_{6-1}(0) + \frac{3}{8}v_{6-2}(1) + \frac{1}{4}(0)$$

---

Notice in the second and third equations that when she transitions into state 6-1, there should be no additional transitions from 6-2 to 6-1 or from 6-3 to 6-1 after the second day in order for there to be a total of one such transition. Solving this system of equations yields:

$$v_{6-1}(1) = \frac{690}{3721} \approx 0.185$$

Finally, we can solve for the expected number of cones:

$$\begin{aligned}
E[N] &= (0)v_{6-1}(0) + (1)v_{6-1}(1) + (2)(1 - v_{6-1}(0) - v_{6-1}(1)) \\
&= \frac{690}{3721} + 2\left(\frac{225}{3721}\right) \\
&= \frac{1140}{3721} \approx 0.306
\end{aligned}$$

(e) We want to find the expected time to absorption conditioned on the event that the student eventually ends up in state 15, which we will call $A$. So

$$\begin{aligned}
P_{i,j|A} &= P(X_{n+1} = j | X_n = i, A) \\
&= \frac{P(A | X_{n+1} = j, X_n = i)P(X_{n+1} = j | X_n = i)}{P(A | X_n = i)} \\
&= \frac{P(A | X_{n+1} = j)P(X_{n+1} = j | X_n = i)}{P(A | X_n = i)} \\
&= \frac{a_j P_{i,j}}{a_i}
\end{aligned}$$

where $a_k$ is the absorption probability of eventually ending up in state 15 conditioned on being in state $k$, which we found in part (b). So we may modify our chain with these new conditional probabilities and calculate the expected time to absorption on the new chain. Note that state 9 now disappears. Also, note that $P_{j,j|A} = P_{j,j}$, but $P_{i,j|A} \neq P_{i,j}$ for $i \neq j$, which means that we may not simply renormalize the transition probabilities in a uniform fashion after conditioning on this event. Let us denote the new expected time to absorption, conditioned on being in state $i$ as $\tilde{\mu}_i$. Our system of equations now becomes

$$\tilde{\mu}_{15} = 0$$
$$\tilde{\mu}_{6-1} = 1 + \frac{a_{6-1}}{a_{6-1}}\frac{1}{2}\tilde{\mu}_{6-1} + 0 + \frac{a_{6-2}}{a_{6-1}}\frac{1}{8}\tilde{\mu}_{6-2} + 0 + \frac{a_{6-3}}{a_{6-1}}\frac{1}{8}\tilde{\mu}_{6-3}$$
$$\tilde{\mu}_{6-2} = 1 + 0 + \frac{a_{6-1}}{a_{6-2}}\frac{3}{8}\tilde{\mu}_{6-1} + \frac{a_{6-3}}{a_{6-2}}\frac{1}{8}\tilde{\mu}_{6-3}$$
$$\tilde{\mu}_{6-3} = 1 + 0 + \frac{a_{6-1}}{a_{6-3}}\frac{3}{8}\tilde{\mu}_{6-1} + \frac{a_{6-2}}{a_{6-3}}\frac{3}{8}\tilde{\mu}_{6-2}$$

Solving this system of equations yields

$$\tilde{\mu}_{6-1} = \frac{1763}{483} \approx 3.65$$

(f) The new Markov chain is shown below.

---

This is another expected time to absorption question on the new chain. Let us define $\mu_k$ to be the expected number of days it takes the student to go from state $k$ to state 9 in this new Markov chain:

$$\mu_{6-1} = 1 + \frac{1}{2}\mu_{6-1} + \frac{1}{6}\mu_{6-2} + \frac{1}{6}\mu_{6-3} + \frac{1}{6}(0)$$
$$\mu_{6-2} = 1 + \frac{3}{4}\mu_{6-1} + \frac{1}{4}\mu_{6-3}$$
$$\mu_{6-3} = 1 + \frac{3}{8}\mu_{6-1} + \frac{3}{8}\mu_{6-2} + \frac{1}{4}(0)$$

Solving this system of equations yields:

$$\mu_{6-1} = \frac{86}{13} \approx 6.615$$

(g) States 6-1, 6-2 and 6-3 are now transient. States 9 and 15 form a recurrent class. By symmetry, 9 and 15 have the same steady state probability of 1/2.

States 6-1, 6-2 and 6-3 are now transient. States 9 and 15 form a recurrent class. By symmetry, 9 and 15 have the same steady state probability of 1/2.

---

(h) The corresponding Markov chain is the same as the one in part (a) except $p_{9,6-1} = \frac{1}{8}$, $p_{9,9} = \frac{7}{8}$, $p_{15,6-1} = \frac{1}{8}$, $p_{15,15} = \frac{7}{8}$ instead of $p_{9,9} = 1$, $p_{15,15} = 1$.
We can consider state 6-1 as an absorbing state. Let $\mu_k$ be the expected number of transitions until absorption if we start at state $k$

$$\mu_9 = \frac{1}{8} + \frac{7}{8}(1 + \mu_9) \Rightarrow \mu_9 = 8$$
$$\mu_{15} = \frac{1}{8} + \frac{7}{8}(1 + \mu_{15}) \Rightarrow \mu_{15} = 8$$
$$\mu_{6-3} = \frac{3}{8} + \frac{3}{8}(1 + \mu_{6-2}) + \frac{1}{4}(1 + \mu_9)$$
$$\mu_{6-2} = \frac{3}{8} + \frac{1}{8}(1 + \mu_{6-3}) + \frac{1}{2}(1 + \mu_{15})$$
$$\Rightarrow \mu_{6-2} = \frac{344}{61}, \mu_{6-3} = \frac{312}{61}$$

Let $R$ be the number of days until she is 6-1 again. We find $E[R]$ by using the total expectation theorem, conditioned on what happens on the first transition.

$$\begin{aligned}
E[R] &= E[E[R|X_2]] \\
&= \frac{1}{2}(1) + \frac{1}{8}(1 + \mu_9) + \frac{1}{8}(1 + \mu_{15}) + \frac{1}{8}(1 + \mu_{6-2}) + \frac{1}{8}(1 + \mu_{6-3}) \\
&= \frac{265}{61}
\end{aligned}$$

Notice that this chain consists of a single recurrent aperiodic class. Another approach to solving this problem uses the steady state probabilities of this chain, which are $\pi_{6-1} = \frac{61}{265}, \pi_{6-2} = \frac{11}{265}, \pi_{6-3} = \frac{9}{265}, \pi_9 = \frac{79}{265}, \pi_{15} = \frac{105}{265}$. The expected frequency of visits to 6-1 is $\pi_{6-1}$, so the expected number of days between visits to 6-1 is $\frac{1}{\pi_{6-1}}$.$^1$ Since she is currently 6-1, the expected number of days until she is 6-1 again is $\frac{1}{\pi_{6-1}} = \frac{265}{61}$.

---

$^1$See problem 7.34 on page 399 of the text for a more detailed explanation of this correspondence between mean recurrence times and steady-state probabilities.

---

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 19](../19-limit-theorems-and-sample-means.md)
