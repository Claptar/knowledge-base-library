---
title: 7.36/7.91 recitation
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/recitations/2014-02-19-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `recitations/2014-02-19-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 7.36/7.91 recitation

2-19-2014
CB Lecture #4

---

## Announcements / Reminders

### Homework:
- PS#1 due Feb. 20th at noon.
- Late policy: 1/2 credit if received within 24 hrs of due date, otherwise no credit
- Answer key will be posted 24 hrs after due date

### Project:
- Teams, Title, 1 paragraph summary due Tuesday Feb. 25
- Teams of 1-5 people unless approved by instructor

---

## Basic Linear Algebra Review

- way to compactly represent and operate on sets of linear equations:

$$\begin{aligned}
2x_1 + 4x_2 &= 10 \\
-5x_1 + x_2 &= -3
\end{aligned}$$

can be written in row form (lecture): $\vec{x} A = \vec{b}$

or in column form: $A^T \vec{x}^T = \vec{b}^T$

where

$$\vec{x} = (x_1, \ x_2) \qquad A = \begin{bmatrix} 2 & -5 \\ 4 & 1 \end{bmatrix} \qquad \vec{b} = (10, \ -3)$$

---

## Basic Linear Algebra Review

### Simple operations:
- Dot product of two row vectors $\vec{x} = (x_1, \ x_2, \ x_3) \quad \vec{y} = (y_1, \ y_2, \ y_3)$

$$\vec{x} \cdot \vec{y} = (x_1, \ x_2, \ x_3) \cdot (y_1, \ y_2, \ y_3) = x_1 y_1 + x_2 y_2 + x_3 y_3$$

- Matrix multiplication:

$$A = \begin{bmatrix} \text{---} & \vec{a}_1 & \text{---} \\ \text{---} & \vec{a}_2 & \text{---} \\ & \vdots & \\ \text{---} & \vec{a}_m & \text{---} \end{bmatrix} \quad B = \begin{bmatrix} \mid & \mid & & \mid \\ \vec{b}_1^T & \vec{b}_2^T & \dots & \vec{b}_p^T \\ \mid & \mid & & \mid \end{bmatrix} \implies A * B = \begin{bmatrix} \vec{a}_1 \cdot \vec{b}_1 & \vec{a}_1 \cdot \vec{b}_2 & \dots & \vec{a}_1 \cdot \vec{b}_p \\ \vec{a}_2 \cdot \vec{b}_1 & \vec{a}_2 \cdot \vec{b}_2 & \dots & \vec{a}_2 \cdot \vec{b}_p \\ \vdots & \vdots & \ddots & \vdots \\ \vec{a}_m \cdot \vec{b}_1 & \vec{a}_m \cdot \vec{b}_2 & \dots & \vec{a}_m \cdot \vec{b}_p \end{bmatrix}$$

- Note that inner dimensions must agree:

$$\text{If } A \in \mathbb{R}^{m \times n} \text{ and } B \in \mathbb{R}^{n \times p} \text{ then } A * B \in \mathbb{R}^{m \times p}$$

---

## Markov Models (Chains)

- Defined by a set of $n$ possible states $s_1, \dots, s_n$ at each timepoint.
- **Markov property:** Transition from state $i$ to $j$ (with probability $P_{i,j}$) depends only on the previous state, not any states before that. In other words, the future is conditionally independent of the past given the present:

$$P(S_{t+1} = k | S_1 = s_1, \dots, S_t = s_t) = P(S_{t+1} = k | S_t = s_t)$$

**Example:** if we know individual 3's genotype, there's no additional information that individuals 1 and 2 can give us about 5's genotype

- Probability of having a class having an exam that week
  - not Markov: prob. of having an exam during a week influenced by events further back than just 1 week (if there was an exam 2 weeks ago, likely not an exam this week)

- Board games whose moves are entirely determined by dice
  - **Markov:** prob. of future event depends only on the current board and outcome of dice roll

---

## Markov Chains

- Instead of realizing a set of states (one particular state with probability 1 and all others with probability 0 at each timepoint), we can model more general processes by defining a probability *distribution* over states at each timepoint:

$$\vec{q}^{\ t} = (q_1, \dots, q_n) \qquad 0 \le q_i \le 1, \sum_{i=1}^n q_i = 1$$

- Probability distribution changes over time according to transition matrix $P$

$$\vec{q}^{\ t+1} = \vec{q}^{\ t} P \qquad\qquad \vec{q}^{\ t+k} = \vec{q}^{\ t} P^k$$

---

## Markov Models (Chains)

- Defined by a set of $n$ possible states $s_1, \dots, s_n$ at each timepoint.
- **Markov property:** Transition from state $i$ to $j$ (with probability $P_{i,j}$) depends only on the previous state, not any states before that. In other words, the future is conditionally independent of the past given the present:

$$P(S_{t+1} = k | S_1 = s_1, \dots, S_t = s_t) = P(S_{t+1} = k | S_t = s_t)$$

- Size and constraints on transition matrix P ? Size: $n \times n$

$$P = \begin{bmatrix} P_{1,1} & P_{1,2} & \dots & P_{1,n} \\ P_{2,1} & P_{2,2} & \dots & P_{2,n} \\ \vdots & \ddots & \ddots & \vdots \\ P_{n,1} & P_{n,2} & \dots & P_{n,n} \end{bmatrix} \qquad\qquad \sum_{j=1}^n P_{i,j} = 1 \quad \forall i$$

Interpretation: From current state $i$, you must end up in *some* state $j$ after transition

---

## Markov Models (Chains)

- Defined by a set of $n$ possible states $s_1, \dots, s_n$ at each timepoint.
- **Markov property:** Transition from state $i$ to $j$ (with probability $P_{i,j}$) depends only on the previous state, not any states before that. In other words, the future is conditionally independent of the past given the present:

$$P(S_{t+1} = k | S_1 = s_1, \dots, S_t = s_t) = P(S_{t+1} = k | S_t = s_t)$$

- If at time $t$ the probability distribution over the $n$ states is

$$\vec{q}^{\ t} = (q_1^t, q_2^t, \dots, q_n^t)$$

what is the probability of being in state $i$ at time $t+1$?

$$q_i^{t+1} = \sum_{s=1}^n q_s^t P_{s,i}$$

$$P = \begin{bmatrix} P_{1,1} & P_{1,2} & \dots & P_{1,n} \\ P_{2,1} & P_{2,2} & \dots & P_{2,n} \\ \vdots & \ddots & \ddots & \vdots \\ P_{n,1} & P_{n,2} & \dots & P_{n,n} \end{bmatrix}$$

---

## Markov Chains

- If all entries of $P$ are strictly positive ($P_{i,j} > 0$), there is a "stationary" (or "limiting") distribution in the limit of infinite time:

$$\lim_{t \to \infty} \vec{q}^{\ t} = \lim_{t \to \infty} \vec{q} P^t = \vec{r}$$

- The stationary distribution satisfies: $\vec{r} = \vec{r} P$

- Since all entries of distribution must sum to 1, can set up system of eqns to solve:

$$\vec{r} = \left( r_1, r_2, \dots, 1 - \sum_{i=1}^{n-1} r_i \right)$$

- May also notice that $\vec{r}$ is an eigenvector of P with eigenvalue 1. Can use eigenvector approaches instead of systems of eqns to determine $\vec{r}$ if you're familiar with those

---

## Practice Problem

- You decided to make a model of purine (R) and pyrimidine (Y) evolution. Multiple sequence alignment of promoters (50% R, 50% Y) leads to:

$$PAM_1 = \begin{bmatrix} 0.995 & 0.005 \\ 0.015 & 0.985 \end{bmatrix}, P_{R,R} = 0.995, P_{R,Y} = 0.005, P_{Y,R} = 0.015, P_{Y,Y} = 0.985$$

- What is the composition of a sequence evolving under this model after a long time?

$$\text{Let } P_Y = 1 - P_R : \quad (P_R, 1 - P_R) = (P_R, 1 - P_R) \begin{bmatrix} 0.995 & 0.005 \\ 0.015 & 0.985 \end{bmatrix}$$

$$\implies (P_R, P_Y) = (0.75, 0.25)$$

- What is PAM$\infty$?

Since the (0.75, 0.25) outcome must be the same no matter where we start from (e.g. (1, 0) or (0, 1)):

$$\lim_{t \to \infty} PAM_t = \begin{bmatrix} 0.75 & 0.25 \\ 0.75 & 0.25 \end{bmatrix}$$

---

## Practice Problem

- You decided to make a model of purine (R) and pyrimidine (Y) evolution. Multiple sequence alignment of promoters (50% R, 50% Y) leads to:

$$PAM_1 = \begin{bmatrix} 0.995 & 0.005 \\ 0.015 & 0.985 \end{bmatrix}, P_{R,R} = 0.995, P_{R,Y} = 0.005, P_{Y,R} = 0.015, P_{Y,Y} = 0.985$$

- What would be the average % sequence identity between an initial sequence (composition 50% R, 50% Y) and the sequence evolved from this initial sequence under the PAM$\infty$ matrix?

  - In PAM$\infty$, $P_{R,R} = 0.75$ and $P_{Y,Y} = 0.25$. We start with 50% R and 50% Y. The fraction of R's remaining the same is $(0.75)(0.50) = 0.375$ and the fraction of Y's remaining the same is $(0.25)(0.50) = 0.125$. Therefore the total % sequence identity is $0.375 + 0.125 = 0.50$ or 50%.

---

---

[Up: contents](index.md) · [PAM vs. BLOSUM →](02-pam-vs-blosum.md)
