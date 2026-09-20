---
title: "Solutions — Joint and Conditional Continuous Densities"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — Joint and Conditional Continuous Densities

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 9 Solutions
## October 7, 2010

1. We first compute the probability that $X$ is in interval $[n, n + 1]$ for an arbitrary nonnegative $n$. Then, we will add the probabilities for all odd positive integer values of $n$.

We could integrate the PDF of $X$ over the given interval but we will use the CDF here. Using the CDF for the exponential random variable,

$$
\begin{aligned}
\mathbf{P}(n \le X \le n + 1) &= F_X(n + 1) - F_X(n) \\
&= \left(1 - e^{-\lambda(n+1)}\right) - \left(1 - e^{-\lambda n}\right) \\
&= e^{-\lambda n} \left(1 - e^{-\lambda}\right).
\end{aligned}
$$

Since the intervals are disjoint, we can sum this probability for all odd integers $n$ to find the probability of interest:

$$
\begin{aligned}
\mathbf{P}(\{X \in [n, n + 1] \text{ for some odd } n\}) \\
&= \sum_{n \text{ odd}} e^{-\lambda n} \left(1 - e^{-\lambda}\right) \\
&= \left(1 - e^{-\lambda}\right) \sum_{k=0}^{\infty} e^{-\lambda(2k+1)} \\
&= \left(1 - e^{-\lambda}\right) e^{-\lambda} \sum_{k=0}^{\infty} \left(e^{-2\lambda}\right)^k \\
&= \left(1 - e^{-\lambda}\right) e^{-\lambda} \frac{1}{1 - e^{-2\lambda}} \\
&= \left(1 - e^{-\lambda}\right) e^{-\lambda} \frac{1}{\left(1 - e^{-\lambda}\right)\left(1 + e^{-\lambda}\right)} \\
&= \frac{e^{-\lambda}}{1 + e^{-\lambda}}.
\end{aligned}
$$

2. See Example 3.13 in the textbook on page 165.

3. Problem 3.23, page 191 in text. See online solutions.

4. Problem 3.22, part (i), page 191 in text (see online solution).

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Tutorial/Recitation 9: Solutions

1. Problem 7.1, page 380 in textbook. See online solutions.

2. (a) Recurrent: 1, 2, 4, 5 , 6; Transient: 3; Periodic: 4,5,6.

   (b) $0.2^n$

   (c) This is a geometric random variable with parameter $p = 0.5 + 0.3$. Hence, the expected number of trials up to and includ ing the trial on which the process leaves state 3 is $\mathbf{E}[X] = 1/p = 5/4$.

   (d) 3/8

   (e) $\mathbf{P}(A) = 0.3 + 0.2^3 0.3 + 0.2^6 0.3 + 0.2^9 0.3 = 0.3024$.

   (f) $0.3/\mathbf{P}(A) = 0.992$.

3. Problem 7.13, page 385 in textbook. See online solutions.

---

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

### Department of Electrical Engineering & Computer Science
### 6.041/6.431: Probabilistic Systems Analysis
### (Fall 2010)

## Problem Set 9 Solutions

1. (a) Yes, to 0. Applying the weak law of large numbers, we have
   $$\mathbf{P}(|U_i - \mu| > \epsilon) \to 0 \text{ as } i \to \infty\text{, for all } \epsilon > 0$$
   Here $\mu = 0$ since $X_i \sim U(-1.0, 1.0)$.

   (b) Yes, to 1. Since $W_i \le 1$, we have for $\epsilon > 0$,
   $$\begin{aligned}
   \lim_{i \to \infty} \mathbf{P}(|W_i - 1| > \epsilon) &= \lim_{i \to \infty} \mathbf{P}(\max\{X_1, \dots, X_i\} < 1 - \epsilon) \\
   &= \lim_{i \to \infty} \mathbf{P}(X_1 < 1 - \epsilon) \cdots \mathbf{P}(X_i < 1 - \epsilon) \\
   &= \lim_{i \to \infty} \left(1 - \frac{\epsilon}{2}\right)^i \\
   &= 0.

   (c) Yes, to 0.
   $$|V_n| \le \min\{|X_1|, |X_2|, \dots, |X_n|\}$$
   but $\min\{|X_1|, |X_2|, \dots, |X_n|\}$ converges to 0 in probability. So, since $|V_n| \ge 0$, $|V_n|$ converges to 0 in probability. To see why $\min\{|X_1|, |X_2|, \dots, |X_n|\}$ converges to 0 in probability, note that:
   $$\begin{aligned}
   \lim_{i \to \infty} \mathbf{P}(|\min\{|X_1|, \dots, |X_i|\} - 0| > \epsilon) &= \lim_{i \to \infty} \mathbf{P}(\min\{|X_1|, \dots, |X_i|\} > \epsilon) \\
   &= \lim_{i \to \infty} \mathbf{P}(|X_1| > \epsilon) \cdot \mathbf{P}(|X_2| > \epsilon) \cdots \mathbf{P}(|X_i| > \epsilon) \\
   &= \lim_{i \to \infty} (1 - \epsilon)^i \text{ since } |X_i| \text{ is uniform between 0 and 1} \\
   &= 0.

2. Consider a random variable $X$ with PMF
   $$p_X(x) = \begin{cases}
   p, & \text{if } x = \mu - c; \\
   p, & \text{if } x = \mu + c; \\
   1 - 2p, & \text{if } x = \mu.
   \end{cases}$$
   The mean of $X$ is $\mu$, and the variance of $X$ is $2pc^2$. To make the variance equal $\sigma^2$, set $p = \frac{\sigma^2}{2c^2}$. For this random variable, we have
   $$\mathbf{P}(|X - \mu| \ge c) = 2p = \frac{\sigma^2}{c^2},$$
   and therefore the Chebyshev inequality is tight.

3. (a) Let $t_i$ be the expected time until the state $HT$ is reached, starting in state $i$, i.e., the mean first passage time to reach state $HT$ starting in state $i$. Note that $t_S$ is the expected number of tosses until first observing heads directly followed by tails. We have,
   $$\begin{aligned}
   t_S &= 1 + \frac{1}{2}t_H + \frac{1}{2}t_T \\
   t_T &= 1 + \frac{1}{2}t_H + \frac{1}{2}t_T \\
   t_H &= 1 + \frac{1}{2}t_H
   and by solving these equations, we find that the expected number of tosses until first observing heads directly followed by tails is
   $$t_S = 4.$$

   (b) To find the expected number of additional tosses necessary to again observe heads followed by tails, we recognize that this is the mean recurrence time $t_{HT}^*$ of state $HT$. This can be determined as
   $$\begin{aligned}
   t_{HT}^* &= 1 + p_{HT,H} t_H + p_{HT,T} t_T \\
   &= 1 + \frac{1}{2} \cdot 2 + \frac{1}{2} \cdot 4 \\
   &= 4.

   (c) Let's consider a Markov chain with states $S, H, T, TT$, where $S$ is a starting state, $H$ indicates heads on the current toss, $T$ indicates tails on the current toss (without tails on the previous toss), and $TT$ indicates tails over the last two tosses. The transition probabilities for this Markov chain are illustrated below in the state transition diagram:

   Let $t_i$ be the expected time until the state $TT$ is reached, starting in state $i$, i.e., the mean first passage time to reach state $TT$ starting in state $i$. Note that $t_S$ is the expected number of tosses until first observing tails directly followed by tails. We have,
   $$\begin{aligned}
   t_S &= 1 + \frac{1}{2}t_H + \frac{1}{2}t_T \\
   t_T &= 1 + \frac{1}{2}t_H \\
   t_H &= 1 + \frac{1}{2}t_H + \frac{1}{2}t_T
   and by solving these equations, we find that the expected number of tosses until first observing two consecutive tails is
   $$t_S = 6.$$

   (d) To find the expected number of additional tosses necessary to again observe heads followed by tails, we recognize that this is the mean recurrence time $t_{TT}^*$ of state $TT$. This can be determined as
   $$\begin{aligned}
   t_{TT}^* &= 1 + p_{TT,H} t_H + p_{TT,TT} t_{TT} \\
   &= 1 + \frac{1}{2} \cdot 6 + \frac{1}{2} \cdot 0 \\
   &= 4.

   It may be surprising that the average number of tosses until the first two consecutive tails is greater than the average number of tosses until heads is directly followed by tails, considering that the mean recurrence time between pairs of tosses with heads directly followed by tails equals the mean recurrence time between pairs of tosses that are both tails (or equivalently, the long-term frequency of pairs of tosses with heads followed by tails equals the long-term frequency of pairs of tosses with two consecutive tails[^1]). This is a start-up artifact. Note that the distribution of the first passage time to reach state $HT$ (or $TT$) starting in state $S$ is the same as the conditional distribution of the recurrence time of state $HT$ (or $TT$), given that it is greater than 1. Although in both cases the *expected values* of the recurrence times are equal (this is what parts (b) and (d) tell us), the *conditional expected values* of the recurrence time given that it is greater than 1 is not the same in both cases (possible, because the unconditional distributions are not equal).

4. (a) The long-term frequency of winning can be found as sum of the long-term frequency of transitions from 1 to 2 and 2 to 2. These can be found from the steady-state probabilities $\pi_1$ and $\pi_2$, which are known to exist as the chain is aperiodic and recurrent. The local balance and normalization equations are as follows:
   $$\begin{aligned}
   \frac{7}{15}\pi_1 &= \frac{5}{9}\pi_2, \\
   \pi_1 + \pi_2 &= 1.
   Solving these we obtain,
   $$\pi_1 = \frac{25}{46} \approx 0.54, \quad \pi_2 = \frac{21}{46} \approx 0.46.$$
   The probability of winning, which is the long-term frequency of the transitions from 1 to 2 and 2 to 2, can now be found as
   $$\mathbf{P}(\text{winning}) = \pi_1 p_{12} + \pi_2 p_{22} = \frac{25}{46}\frac{7}{15} + \frac{21}{46}\frac{4}{9} = \frac{21}{46} \approx 0.46.$$
   Note that from the balance equation for state 2,
   $$\pi_2 = \pi_1 p_{12} + \pi_2 p_{22},$$
   the long-term probability of winning always equals $\pi_2$.

   (b) This question is one of determining the probability of absorption into the recurrent class $\{1A, 2A\}$. This probability of absorption can be found by recognizing that it will be the ratio of probabilities
   $$\frac{p_{1,1A}}{p_{1,1A} + p_{1,1B}} = \frac{\frac{2}{15}}{\frac{2}{15} + \frac{1}{15}} = \frac{2}{3}.$$
   More methodically, if we define $a_i$ as the probability of being absorbed into the class $\{1A, 2A\}$, starting in state $i$, we can solve for the $a_i$ by solving the system of equations
   $$\begin{aligned}
   a_1 &= p_{1,1A} + p_{11}a_1 + p_{12}a_2 \\
   &= \frac{2}{15} + \frac{1}{3}a_1 + \frac{7}{15}a_2 \\
   a_2 &= p_{21}a_1 + p_{22}a_2 \\
   &= \frac{5}{9}a_1 + \frac{4}{9}a_2,
   from which we determine that $a_1 = \frac{p_{1,1A}}{p_{1,1A} + p_{1,1B}} = \frac{2}{3}$.

   (c) Let $A, B$ be the events that Jack eventually plays with decks $1A$ & $2A$, $1B$ & $2B$, respectively, when starting in state 1. From part (b), we know that $\mathbf{P}(A) = a_1 = \frac{2}{3}$ and $\mathbf{P}(B) = 1 - a_1 = \frac{1}{3}$. The probability of winning can be determined as
   $$\mathbf{P}(\text{winning}) = \mathbf{P}(\text{winning}|A)\mathbf{P}(A) + \mathbf{P}(\text{winning}|B)\mathbf{P}(B).$$
   By considering the appropriate recurrent class and solving a problem similar to part (a), $\mathbf{P}(\text{winning}|A)$ and $\mathbf{P}(\text{winning}|B)$ can be determined; in these cases, the steady-state probabilities of each recurrent class are defined under the assumption of being absorbed into that particular recurrent class. Let's begin with $\mathbf{P}(\text{winning}|A)$. The local balance and normalization equations for the recurrent class $\{1A, 2A\}$ are
   $$\begin{aligned}
   \frac{3}{5}\pi_{1A} &= \frac{1}{5}\pi_{2A}, \\
   \pi_{1A} + \pi_{2A} &= 1.
   Solving these we obtain,
   $$\pi_{1A} = \frac{1}{4}, \quad \pi_{2A} = \frac{3}{4},$$
   and hence conclude that
   $$\mathbf{P}(\text{winning}|A) = p_{1A,2A}\pi_{1A} + p_{2A,2A}\pi_{2A} = \pi_{2A} = \frac{3}{4}.$$
   Similarly, the local balance and normalization equations for the recurrent class $\{1B, 2B\}$ are
   $$\begin{aligned}
   \frac{3}{4}\pi_{1B} &= \frac{1}{8}\pi_{2B}, \\
   \pi_{1B} + \pi_{2B} &= 1.
   Solving these we obtain,
   $$\pi_{1B} = \frac{1}{7}, \quad \pi_{2B} = \frac{6}{7},$$
   and hence conclude that
   $$\mathbf{P}(\text{winning}|B) = p_{1B,2B}\pi_{1B} + p_{2B,2B}\pi_{2B} = \pi_{2B} = \frac{6}{7}.$$
   Putting these pieces together, we have that
   $$\begin{aligned}
   \mathbf{P}(\text{winning}) &= \mathbf{P}(\text{winning}|A)\mathbf{P}(A) + \mathbf{P}(\text{winning}|B)\mathbf{P}(B) \\
   &= \frac{3}{4} \cdot \frac{2}{3} + \frac{6}{7} \cdot \frac{1}{3} \\
   &= \frac{11}{14} \approx 0.79,
   meaning that Jack substantially increases the odds to his favor by slipping additional cards into the decks.

   (d) The expected time until Jack slips cards into the deck is the same as the expected time until the Markov chain enters a recurrent state. Let $\mu_i$ be the expected amount of time until a recurrent state is reached from state $i$. We have the equations
   $$\begin{aligned}
   \mu_1 &= 1 + p_{11}\mu_1 + p_{12}\mu_2 = 1 + \frac{1}{3}\mu_1 + \frac{7}{15}\mu_2 \\
   \mu_2 &= 1 + p_{21}\mu_1 + p_{22}\mu_2 = 1 + \frac{5}{9}\mu_1 + \frac{4}{9}\mu_2,
   which when solved, yields the expected time until Jack slips cards into the deck,
   $$\mu_1 = 9.2.$$

   (e) Let $S$ be the number of times that the dealer switches from deck #2 to deck #1, which equals the number of times that he/she switches from deck #1 to deck #2. Let $p$ be the probability that $S = 0$, which is the sum of the probability of all ways for the first change of state to be from state 1 to state 1A or state 1B,
   $$p = \left(\frac{2}{15} + \frac{1}{15}\right) + \left(\frac{1}{3}\right)\left(\frac{2}{15} + \frac{1}{15}\right) + \left(\frac{1}{3}\right)^2\left(\frac{2}{15} + \frac{1}{15}\right) + \dots = \frac{1}{1 - 1/3} \cdot \frac{3}{15} = \frac{3}{10}.$$
   Alternatively, $p$ is the probability of absorption of the following modified chain into an absorbing state ($1A$ or $1B$), when started in state 1:

   As $\mathbf{P}(S > 0) = 1 - p$, and similarly, $\mathbf{P}(S > k + 1 | S > k) = 1 - p$, it should be clear that $S$ will be a shifted geometric, and thus
   $$p_S(k) = \left(\frac{7}{10}\right)^k \frac{3}{10}, \quad k = 0, 1, 2, \dots.$$

   (f) Note that $S$ from part (e) is the total number of cycles from 1 to 2 and back to 1. During the $i$th cycle, the number of wins, $W_i$, is a geometric random variable with parameter $q = \frac{5}{9}$. Thus the total number of wins by Jack before he slips extra cards into the deck is
   $$W = W_1 + W_2 + \dots + W_S,$$
   which is a random number of random variables, all of which are independent. Conditioned on $S > 0$, $W$ is a geometric (with parameter $p$) number of geometric (with parameter $q$) random variables, all conditionally independent, and thus from the theory of splitting Bernoulli processes,
   $$p_{W|S>0}(k) = (1 - pq)^{k-1}pq \quad k = 1, 2, \dots,$$
   where $pq = \frac{3}{10} \cdot \frac{5}{9} = \frac{1}{6}$. When $S = 0$, it follows that $W = 0$, and thus by total probability,
   $$p_W(k) = \begin{cases}
   \frac{3}{10} & k = 0 \\
   \left(\frac{7}{10}\right) \left(\frac{5}{6}\right)^{k-1} \frac{1}{6} & k = 1, 2, \dots.
   \end{cases}$$

   (g) Let $W$ be the total number of wins before slipping cards into the deck (as in part (f)), and similarly let $L$ be the total number of losses before absorption. We know from part (d) that $\mathbf{E}[W + L] = \mu_1 = 9.2$. From part (f) we can find $\mathbf{E}[W]$ by total expectation,
   $$\mathbf{E}[W] = \mathbf{E}[W|S = 0]\mathbf{P}(S = 0) + \mathbf{E}[W|S > 0]\mathbf{P}(S > 0) = \frac{7/10}{1/6} = \frac{42}{10} = 4.2,$$
   because when conditioned on $S > 0$, the number of wins, $W$, is a geometric random variable with parameter $pq = \frac{1}{6}$. From linearity of expectation, we find
   $$\mathbf{E}[L - W] = \mathbf{E}[W + L] - 2\mathbf{E}[W] = 9.2 - 2 \cdot 4.2 = 0.8.$$

   (h) Using $A$ to again denote the probability of being absorbed into the recurrent class $\{1A, 2A\}$, starting in state 1,
   $$\begin{aligned}
   \mathbf{P}(X_n = 2A | X_{n+1} = 1A) &= \frac{\mathbf{P}(X_{n+1} = 1A | X_n = 2A)\mathbf{P}(X_n = 2A)}{\mathbf{P}(X_{n+1} = 1A)} \\
   &= \frac{\mathbf{P}(X_{n+1} = 1A | X_n = 2A)\mathbf{P}(X_n = 2A | A)\mathbf{P}(A)}{\mathbf{P}(X_{n+1} = 1A | A)\mathbf{P}(A)} \\
   &\approx \frac{p_{2A,1A}\pi_{2A}}{\pi_{1A}} \\
   &= \frac{\frac{1}{5} \cdot \frac{3}{4}}{\frac{1}{4}} \\
   &= \frac{3}{5}.
   Note that the right hand side above equals $p_{1A,2A}$, as clear from the local balance equation $\pi_{1A}p_{1A,2A} = \pi_{2A}p_{2A,1A}$.

---

G1$^{\dagger}$. With $a > 0$ and $c \ge 0$,
$$\begin{aligned}
\mathbf{P}(X - \mu \ge a) &= \mathbf{P}(X - \mu + c \ge a + c) \\
&\le \mathbf{P}\left((X - \mu + c)^2 \ge (a + c)^2\right) \\
&\le \frac{\mathbf{E}\left[(X - \mu + c)^2\right]}{(a + c)^2} \\
&= \frac{(\sigma^2 + c^2)}{(a + c)^2}
where the first inequality follows from the fact that $a + c > 0$, and the second inequality follows from the Markov inequality.

To tighten the bound, we treat $(\sigma^2 + c^2)/(a + c)^2$ as a function of $c$, and find $c$ such that the derivative is 0. The minimum occurs at $c = \sigma^2/a$. Therefore,
$$\mathbf{P}(X - \mu \ge a) \le \frac{\left(\sigma^2 + \frac{(\sigma^4)}{a^2}\right)}{\left(a + \frac{\sigma^2}{a}\right)^2} = \frac{\sigma^2}{(\sigma^2 + a^2)}$$

$^{\dagger}$Required for 6.431; optional challenge problem for 6.041

---

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

[^1]: See problem 7.34 on page 399 of the text for a detailed explanation of this correspondence between mean recurrence times and steady-state probabilities.

---

[← back to chapter 9](../09-joint-and-conditional-continuous-densities.md)
