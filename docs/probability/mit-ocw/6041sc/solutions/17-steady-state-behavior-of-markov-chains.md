---
title: "Solutions — Steady-State Behavior of Markov Chains"
source: https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/
licence: CC BY-NC-SA 4.0
---

> **Worked solutions.** From the course's own solution sets, licensed CC BY-NC-SA 4.0.

# Solutions — Steady-State Behavior of Markov Chains

## Department of Electrical Engineering & Computer Science
## 6.041/6.431: Probabilistic Systems Analysis
## (Fall 2010)

## Recitation 17 Solutions
## November 4, 2010

1. (a) $K$ has a Poisson distribution with average arrival time $\mu = \lambda_c T$
$$p_K(k) = \frac{(\lambda_c T)^k e^{-\lambda_c T}}{k!}, \quad k = 0, 1, 2, \dots; T \ge 0.$$

(b) i. $\mathbf{P}(\text{conscious response}) = \left(\frac{\lambda_c}{\lambda_c + \lambda_s}\right)$.
ii. $\mathbf{P}(\text{conscious correct response}) = \mathbf{P}(\text{conscious resp}) \mathbf{P}(\text{correct resp} \mid \text{conscious resp}) = \left(\frac{\lambda_c}{\lambda_c + \lambda_s} p_c\right)$.

(c) Since the conscious and subconscious responses are generated independently,
$$\begin{aligned}
\mathbf{P}&(r \text{ conscious responses and } s \text{ subconscious responses in interval } T) \\
&= \mathbf{P}(r \text{ conscious responses in } T)\mathbf{P}(s \text{ unconscious responses in } T) \\
&= \frac{(\lambda_c T)^r e^{-\lambda_c T}}{r!} \cdot \frac{(\lambda_s T)^s e^{-\lambda_s T}}{s!}
\end{aligned}$$

(d) Let $X_s =$ the time from the start of the exam to the time of the 1st subconscious response, and $X_c =$ the time from the 1st subconscious response to the time of the next conscious response.
Note that $X_s$ and $X_c$ are independent exponentially distributed random variables with parameters $\lambda_s$ and $\lambda_c$, respectively.
$$\begin{aligned}
f_{X_s}(x_s) &= \lambda_s e^{-\lambda_s x_s} \text{ when } x_s \ge 0 \\
&= 0 \text{ otherwise} \\
f_{X_c}(x_c) &= \lambda_c e^{-\lambda_c x_c} \text{ when } x_c \ge 0 \\
&= 0 \text{ otherwise}
\end{aligned}$$
$X = X_s + X_c$. So its PDF is the convolution of the two exponential distributions. For $x \ge 0$
$$\begin{aligned}
f_X(x) &= \int_{-\infty}^{\infty} \lambda_s e^{-\lambda_s(x - x_c)} \lambda_c e^{-\lambda_c x_c} \, dx_c \\
&= \int_0^x \lambda_s \lambda_c e^{-\lambda_s x} e^{(\lambda_s - \lambda_c)x_c} \, dx_c \text{ because } x - x_c > 0 \\
&= \lambda_s \lambda_c e^{-\lambda_s x} \int_0^x e^{(\lambda_s - \lambda_c)x_c} \, dx_c \\
&= \frac{\lambda_s \lambda_c}{\lambda_s - \lambda_c} e^{-\lambda_s x} (e^{(\lambda_s - \lambda_c)x} - 1) \text{ because } \lambda_s \neq \lambda_c \\
&= \frac{\lambda_s \lambda_c}{\lambda_s - \lambda_c} (e^{-\lambda_c x} - e^{-\lambda_s x})
\end{aligned}$$

2. (a) Since we are looking for the number of "trials" up to and including the first "success," $N$ is a geometric random variable with parameter $p$.
$$p_N(n) = (1 - p)^{n-1}p, \quad n \ge 1.$$

(b) The length of time spent driving to each intersection is exponentially distributed with parameter $\lambda$. Since the probability of Shem observing an accident at a given intersection is $p$, the distribution of the length of time in between accident reports is exponential but with parameter $p\lambda$ (think of Poisson splitting). Thus,
$$f_Q(q) = (p\lambda)e^{-qp\lambda}, \quad q \ge 0.$$

(c) Since the interarrival time of accidents is exponentially distributed with parameter $p\lambda$, the number of arrivals in a given amount of time $\tau$ is a Poisson random variable with parameter $p\lambda\tau$. Thus,
$$\mathbf{P}(m \text{ arrivals in 2 hours}) = p_M(m) = \frac{e^{-2p\lambda}(2p\lambda)^m}{m!}, \quad m \ge 0.$$

(d) We can view the radio calls to Shem and the accident reports as independent Poisson processes with arrival rates $\mu$ and $p\lambda$, respectively. When the two independent Poisson processes are joined, the resultant is a Poisson process with arrival rate $\mu + p\lambda$. Furthermore, the probability of an arrival from the radio calls is $\frac{\mu}{\mu + p\lambda}$. Since we are interested in the number of reported accidents between two radio calls, we can view this is a shifted Geometric random variable with parameter $\frac{\mu}{\mu + p\lambda}$. Thus,
$$p_K(k) = \left(\frac{p\lambda}{\mu + p\lambda}\right)^k \left(\frac{\mu}{\mu + p\lambda}\right), \quad k \ge 0.$$

(e) If we begin to observe Shem's radio calls at some random instant in time, due to the memoryless property of Poisson interarrivals, the distribution until he recieves the next call will still be exponential with parameter $\mu$. Also, the time from the previous call until the point at which we begin to observe Shem is also an exponential distribution with parameter $\mu$. Thus, $W = X_1 + X_2$, where $X_1$ and $X_2$ have exponential distributions, i.e. $W$ is a second order Erlang PDF.
$$f_W(w) = (\mu)^2 w e^{-w\mu}$$

3. See problem 6.27, page 337 in the textbook.

---

MIT OpenCourseWare
http://ocw.mit.edu

6.041SC Probabilistic Systems Analysis and Applied Probability
Fall 2013

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← back to chapter 17](../17-steady-state-behavior-of-markov-chains.md)
