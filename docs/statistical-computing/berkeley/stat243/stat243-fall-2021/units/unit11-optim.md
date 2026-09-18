---
title: Unit 11 — optim
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit11-optim.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit11-optim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit11-optim.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Unit 11 — optim

unique optimum provided $x^*$ satisfies the constraints, and no optimum exists if it does not.

Here's a simple example: suppose we want to minimize $x^\top x$ s.t. $Ax = b$. The Lagrangian is $L(x, \lambda) = x^\top x + \lambda^\top (Ax - b)$. Since $L(x, \lambda)$ is quadratic in $x$, the infimum is found by setting $\nabla_x L(x, \lambda) = 2x + A^\top \lambda = 0$, yielding $x = -\frac{1}{2}A^\top \lambda$. So the dual function is obtained by plugging this value of $x$ into $L(x, \lambda)$, which gives
$$d(\lambda) = -\frac{1}{4}\lambda^\top AA^\top \lambda - b^\top \lambda,$$
which is concave quadratic. In this case we can solve the original constrained problem in terms of this unconstrained dual problem.

Another example is the primal and dual forms for finding the SVM classifier (see the Wikipedia article). In this algorithm, we want to develop a classifier using $n$ pairs of $y \in \Re^1$ and $x \in \Re^p$. The dual form is easily derived because the minimization over $x$ occurs in a function that is quadratic in $x$. Expressing the problem in the primal form gives an optimization in $\Re^p$ while doing so in the dual form gives an optimization in $\Re^n$. So one reason to use the dual form would be if you have $n \ll p$.

## 9.5 KKT conditions (optional)

Karush-Kuhn-Tucker (KKT) theory provides sufficient conditions under which a constrained optimization problem has a minimum, generalizing the Lagrange multiplier approach. The Lange and Boyd books have whole sections on this topic.

Suppose that the function and the constraint functions are continuously differentiable near $x^*$ and that we have the Lagrangian as before:
$$L(x, \lambda, \mu) = f(x) + \sum_i \lambda_i g_i(x) + \sum_j \mu_j h_j(x).$$

For nonconvex problems, if $x^*$ and $(\lambda^*, \mu^*)$ are the primal and dual optimal points and there is no duality gap, then the KKT conditions hold:
$$\begin{aligned}
h_j(x^*) &\le 0 \\
g_i(x^*) &= 0 \\
\mu_j^* &\ge 0 \\
\mu_j^* h_j(x^*) &= 0 \\
\nabla f(x^*) + \sum_i \lambda_i^* \nabla g_i(x^*) + \sum_j \mu_j^* \nabla h_j(x^*) &= 0.
\end{aligned}$$

For convex problems, we also have that if the KKT conditions hold, then $x^*$ and $(\lambda^*, \mu^*)$ are primal and dual optimal and there is no duality gap.

We can consider this from a slightly different perspective, in this case requiring that the Lagrangian be twice differentiable.

First we need a definition. A tangent direction

---

[Up: contents](../index.md)
