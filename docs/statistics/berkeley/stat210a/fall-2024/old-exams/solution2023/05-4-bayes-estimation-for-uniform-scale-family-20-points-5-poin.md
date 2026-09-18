---
title: 4. Bayes estimation for Uniform Scale family (20 points, 5 points / part).
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2023.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`old-exams/solution2023.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2023.pdf) — berkeley-stat210a · fall-2024, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4. Bayes estimation for Uniform Scale family (20 points, 5 points / part).

Some useful facts for this problem:

- The $\text{Unif}[0, \theta]$ distribution for $\theta > 0$ has density
$$p_\theta(x) = \frac{1}{\theta}, \quad \text{for } x \in [0, \theta].$$
Its mean and variance are $\theta/2$ and $\theta^2/12$.

- The Pareto distribution with minimum value $x_0 > 0$ and shape parameter $\alpha > 0$ is called $\text{Pareto}(x_0, \alpha)$ and has density
$$p_{x_0,\alpha}(x) = \frac{\alpha x_0^\alpha}{x^{\alpha+1}}, \quad \text{for } x \ge x_0.$$
Its mean is $\frac{\alpha x_0}{\alpha - 1}$ if $\alpha > 1$ and is infinite otherwise, and its variance is $\frac{\theta_0^2\alpha}{(\alpha-1)^2(\alpha-2)}$ if $\alpha > 2$ and infinite otherwise.

Assume that we observe a uniformly distributed random variable
$$X \sim \text{Unif}[0, \theta].$$
Assume for parts (a) - (b) below that the relevant loss is the standard squared error loss $L(\hat{\theta}, \theta) = (\hat{\theta} - \theta)^2$.

(a) Show that $\theta \sim \text{Pareto}(\theta_0, \alpha)$ is conjugate to this family and find the posterior distribution and Bayes estimator for $\theta$.

**Solution:**
The prior is $\lambda(\theta) \propto_\theta \frac{1}{\theta^{\alpha+1}} \mathbf{1}\{\theta \ge \theta_0\}$, and the likelihood is $p_\theta(x) = \frac{1}{\theta} \mathbf{1}\{x \le \theta\}$, so the posterior distribution is
$$\begin{aligned}
\lambda(\theta \mid x) &\propto_\theta \frac{1}{\theta^{\alpha+2}} \mathbf{1}\{\theta \ge \theta_0\}\mathbf{1}\{\theta \ge x\} \\
&= \frac{1}{\theta^{\alpha+2}} \mathbf{1}\{\theta \ge \max(x, \theta_0)\} \\
&\propto_\theta \text{Pareto}(\max(x, \theta_0), \alpha + 1).
\end{aligned}$$
As a result the posterior mean (which is the Bayes estimator for squared error loss) is $\hat{\theta} = \frac{1+\alpha}{\alpha} \max(\theta_0, X) = (1 + 1/\alpha) \max(\theta_0, X)$.

**Common mistake:** The posterior is not $\text{Pareto}(\theta_0, \alpha+1)$ (if it were, it wouldn't depend on the data). A good number of students forgot to mind the indicators. I think people made that mistake because we have often been lackadaisical in class and on homework about keeping explicit track of the support of distributions. It is usually fine not to worry about the support, since there is usually a base measure for the family that determines the support for all densities in the problem, and so it goes without saying that all densities we work with for that problem have the same support. But for both the uniform and Pareto families in this problem, the support depends on the parameter so we have to keep track of it if we want to get the calculations right.

(b) Next consider the prior $\lambda(\theta) = 2\theta \cdot \mathbf{1}\{0 \le \theta \le 1\}$. Find the Bayes estimator and Bayes risk.

**Solution:**
The posterior is
$$\lambda(\theta \mid x) \propto_\theta 2\theta \cdot \mathbf{1}\{\theta \le 1\} \cdot \frac{1}{\theta} \mathbf{1}\{x \le \theta\} = 2 \cdot \mathbf{1}\{x \le \theta \le 1\} \propto_\theta \text{Unif}[x, 1].$$
The Bayes estimator is therefore $(1 + X)/2$, and the MSE is
$$\begin{aligned}
\text{MSE}(\theta) &= \left( \mathbb{E}_\theta \left[ \frac{1 + X}{2} \right] - \theta \right)^2 + \text{Var}_\theta \left( \frac{1 + X}{2} \right) \\
&= \left( \frac{1}{2} - \frac{3\theta}{4} \right)^2 + \theta^2/48 \\
&= \left( \frac{9}{16} + \frac{1}{48} \right) \theta^2 - \frac{3}{4}\theta + \frac{1}{4} \\
&= \frac{7}{12}\theta^2 - \frac{3}{4}\theta + \frac{1}{4},
\end{aligned}$$
and the Bayes risk is
$$\begin{aligned}
\int_0^1 2\theta \left( \frac{7}{12}\theta^2 - \frac{3}{4}\theta + \frac{1}{4} \right) \, d\theta &= \int_0^1 \left( \frac{7}{6}\theta^3 - \frac{3}{2}\theta^2 + \frac{1}{2}\theta \right) \, d\theta \\
&= \frac{7}{24} - \frac{1}{2} + \frac{1}{4} = \frac{1}{24}.
\end{aligned}$$
**Common mistake:** Many of the same people who got part (a) wrong got this wrong too, giving $\text{Unif}[0, 1]$ as the posterior. I felt bad taking points off again for a similar mistake so I gave partial credit, but not too much; it is a failure of statistical intuition to think that the data is not going to determine the posterior in this problem.

(c) (*) Is the minimax risk for this problem finite? Show that it is infinite or find an upper bound on the minimax risk.

(**Hint:** It might help to consider a subproblem where $\theta$ is bounded above by $B > 0$.)

**Solution:**
Consider the prior $\frac{2\theta}{B^2} \mathbf{1}\{0 \le \theta \le B\}$. We can repeat essentially the same calculation as in (b) to get that the estimator is $(X + B)/2$.

But if $Y = X/B$ and $\zeta = \theta/B$, then we have $\zeta \sim 2\zeta \cdot \mathbf{1}\{\zeta < 1\}$, and $Y \mid \zeta \sim \text{Unif}[0, \zeta]$, and the Bayes risk is
$$\mathbb{E}[((X + B)/2 - \theta)^2] = B^2 \mathbb{E}[((Y + 1)/2 - \zeta)^2] = B^2/24.$$
Because any Bayes risk is a lower bound for the minimax risk, the minimax risk must be infinite.

(d) Now consider instead the squared relative error loss $L(\hat{\theta}, \theta) = \left( \frac{\hat{\theta} - \theta}{\theta} \right)^2$. Find the best linear estimator; i.e. if we take our estimator as $aX$, for $a > 0$, find the $a$ that minimizes the corresponding risk and give the risk as a function of $\theta$.

**Solution:**
The risk is
$$\begin{aligned}
R(\theta) &= \frac{1}{\theta^2} \mathbb{E}[(aX - \theta)^2] \\
&= \frac{1}{\theta^2} \left[ (a\mathbb{E}_\theta X - \theta)^2 + a^2 \text{Var}_\theta(X) \right] \\
&= (a/2 - 1)^2 + a^2/12 \\
&= (1/4 + 1/12)a^2 - a + 1 \\
&= a^2/3 - a + 1.
\end{aligned}$$
Differentiating, we find the minimum is at $a = 3/2$, giving constant risk of $1/4$.

---

[← 3. Nonparametric two-sample problem (20 points, 5 points / part).](04-3-nonparametric-two-sample-problem-20-points-5-points-part.md) · [Up: contents](index.md)
