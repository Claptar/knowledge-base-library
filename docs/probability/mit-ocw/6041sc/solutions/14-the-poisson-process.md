---
title: "Solutions — The Poisson Process"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — The Poisson Process

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 14 Solutions
## October 26, 2010

1. (a) Let $X = (\text{time between successive mosquito bites}) = (\text{time until the next mosquito bite})$.

The mosquito bites occur according to a Bernoulli process with parameter $p = 0.5 \cdot 0.2 = 0.1$. $X$ is a geometric random variable, so, $\mathbf{E}[X] = \frac{1}{p} = \frac{1}{0.1} = 10$.

$$\operatorname{var}(X) = \frac{1 - p}{p^2} = \frac{1 - 0.1}{0.1^2} = 90.$$

(b) Mosquito bites occur according to a Bernoulli process with parameter $p = 0.1$. Tick bites occur according to another independent Bernoulli process with parameter $q = 0.1 \cdot 0.7 = 0.07$. Bug bites (mosquito or tick) occur according to a merged Bernoulli process from the mosquito and tick processes. Therefore, the probability of success at any time point for the merged Bernoulli process is $r = p + q - pq = 0.1 + 0.07 - 0.1 \cdot 0.07 = 0.163$. Let $Y$ be the time between successive bug bites. As before, $Y$ is a geometric random variable, so $\mathbf{E}[Y] = \frac{1}{r} = \frac{1}{0.163} \approx 6.135$.

$$\operatorname{var}(Y) = \frac{1 - r}{r^2} = \frac{1 - 0.163}{0.163^2} \approx 31.503$$

2. (a) In this case, since the trials are independent, the given information is irrelevant.
$$\mathbf{P}(\text{next 2 trials result in 3 tails}) = \left(\frac{1}{8}\right)^2 = \frac{1}{64}.$$

(b) i. The second order Pascal PMF for random variable $N$, as defined in the text, is the probability of the second success comes on the $n^{\text{th}}$ trial. Thus, the random variable, $K$, is a shifted version of the second order Pascal PMF, i.e. $K = N - 1$. So, the probability that 1 success comes in the first $k$ trials, where the next trial will result in the second success, can be expressed as:

$$p_K(k) = \binom{k}{1} \left(\frac{1}{4}\right)^2 \left(\frac{3}{4}\right)^{k-1}, \quad k \ge 1.$$

ii. The number of tails before the first success, $M$, can be written as a random sum:

$$M = X_1 + X_2 + \cdots + X_N,$$

where $X_i$ is the number of tails that occur on (unsuccessful) trial $i$, and $N$ is the number of unsuccessful trials (i.e. trials before the first success). We notice that $X$ is equally likely to be either 1 or 2, and that $N$ is a shifted geometric: $N = R - 1$, where $R$ is a geometric random variable with parameter $\frac{1}{4}$. Now we can apply our random sum formulae.

$$\mathbf{E}[M] = \mathbf{E}[X]\mathbf{E}[N] = \left(\frac{3}{2}\right)(4 - 1) = \frac{9}{2}$$

$$\operatorname{var}(M) = \mathbf{E}[N]\operatorname{var}(X) + (\mathbf{E}[X])^2\operatorname{var}(N) = (4 - 1)\left(\frac{1}{4}\right) + \left(\frac{3}{2}\right)^2(12) = \frac{111}{4}.$$

(c) $N$, the number of trials in Bob's experiment, can be expressed as the sum of 3 independent random variables, $X$, $Y$, and $Z$. $X$ is the number of trials until Bob removes the first coin, $Y$ the number of additional trials until he removes the second coin, and $Z$ the additional number until he removes the third coin. We see that $X$ is a geometric random variable with parameter $\frac{1}{8}$, $Y$ is geometric with parameter $\frac{1}{4}$, and $Z$ geometric with parameter $\frac{1}{2}$. Hence,

$$\mathbf{E}[N] = \mathbf{E}[X] + \mathbf{E}[Y] + \mathbf{E}[Z] = 8 + 4 + 2 = 14.$$

3. Let $M$ be the total number of draws you make until you have signed all $n$ papers. Let $T_i$ be the number of draws you make until drawing the next unsigned paper after having signed $i$ papers. Then $M = T_0 + \cdots + T_{n-1}$.

We can view the process of selecting the next unsigned paper after having signed $i$ papers as a sequence of independent Bernoulli trials with probability of success $p_i = \frac{n-i}{n}$, since there are $n-i$ unsigned papers out of a total of $n$ papers and receiving any paper is equally likely in a particular draw. The PMF governing the number of attempts we make until we succeed in drawing the next unsigned paper after having signed $i$ papers is geometric. More concretely, the probability that it takes $k$ tries to draw the next unsigned paper after having signed $i$ papers is

$$\mathbf{P}(T_i = k) = (1 - p_i)^{k-1}p_i.$$

With this model, the expected value of $M$, the number of draws you make until you sign all $n$ papers is:

$$\mathbf{E}[M] = \mathbf{E}\left[\sum_{i=0}^{n-1} T_i\right] = \sum_{i=0}^{n-1} \mathbf{E}[T_i] = \sum_{i=0}^{n-1} \frac{n}{n-i} = n \sum_{k=1}^n \frac{1}{k}.$$

For large $n$, this is on the order of: $n \int_1^n \frac{1}{x} \, dx = n \log n$.

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 14](../14-the-poisson-process.md)
