---
title: Examples
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/score-fisher.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Examples

**Source:** [`reader/score-fisher.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/score-fisher.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

**Example: i.i.d. sample**

Assume $X_1, \ldots, X_n \simiid p_\theta^{(1)}(x)$, for $\theta \in \Theta \subseteq \RR^d$.

Assume additionally that $p_\theta^{(1)}$ is "regular:" it has common support, and finite derivative w.r.t. $\theta$.

Then the full data density is $p_\theta(x) = \prod_i p_\theta^{(1)}(x_i)$.

Define the single-sample log-likelihood $\ell_1(\theta;x_i) = \log p_\theta^{(1)}(x_i)$; then we have $\ell(\theta;x) = \sum_i \ell_1(\theta;x_i)$.

Then the Fisher information for the full sample is
$$J(\theta) = \Var_\theta(\nabla \ell(\theta; X)) = \sum_{i=1}^n \Var_\theta(\nabla \ell_1(\theta; X_i)) = n J_1(\theta),$$
where $J_1(\theta) = \Var_\theta(\nabla\ell(\theta; X_1))$ is the Fisher information for a single sample.

As a result, we see that the Information bound scales like $n^{-1}$ for regular families; in other words, the standard deviation of an estimator should scale roughly like $1/\sqrt{n}$.

**Example: exponential family**

Suppose we have an exponential family of the form
$$ p_\eta(x) = e^{\eta'T(x) - A(\eta)} h(x).$$

The log-likelihood is $\ell(\eta;X) = \eta'T(X) - A(\eta) + \log h(X)$, and its gradient (the score) is
$$\nabla \ell(\eta;X) = T(X) - \nabla A(\eta) = T(X) - \EE_\eta T(X).$$
Since $\EE_\eta T(X)$ is nonrandom, the variance is
$$ J(\eta) = \Var_\eta (T(X)) = \nabla^2 A(\eta).$$

We could alternatively derive the Fisher information from taking a second derivative with respect to $\eta$, giving
$$ \nabla^2\ell(\eta;X) = -\nabla^2 A(\eta),$$
which is deterministically equal to $-\Var_\eta(T(X))$, so we have confirmed the identity $J(\eta) = -\EE_\eta[\nabla^2 \ell(\eta;X)]$.

**Example: Curved exponential family**

Next, consider a curved version of the previous family, parameterized by $\theta \in \RR$:
$$p_\theta(x) = e^{\eta(\theta)'T(x) - B(\theta)}h(x),\quad \text{ with } B(\theta) = A(\eta(\theta))$$
Again, the log-likelihood is
$$\ell(\theta;X) = \eta(\theta)'T(x) - B(\theta)  + \log h(x),$$
and its first derivative is
$$\begin{aligned}
\dot{\ell}(\theta;X) &= \dot{\eta}(\theta)'T(X) - \dot{\eta}(\theta)'\nabla_\eta A(\eta(\theta))\\
&= \dot{\eta}(\theta) '\left(T(X) - \nabla_\eta A(\eta(\theta))\right)\\
&= \dot{\eta}(\theta)'(T(X) - \EE_\theta T(X)).\end{aligned}$$

As a result, the Fisher information is
$$J(\theta) = \Var_\theta(\dot{\eta}(\theta)'T(X)) =  \dot{\eta}(\theta)'\Var_\theta(T(X))\dot{\eta}(\theta).$$
Note in this model $\dot{\eta}'T(X)$ is a "local complete sufficient statistic" for the model near $\theta$.

---

[← Expand to see proof](07-expand-to-see-proof.md) · [Up: contents](index.md) · [Efficiency →](09-efficiency.md)
