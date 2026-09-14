---
title: Moral
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework5.tex
source_file: sources/berkeley-stat210a/fall-2026/homework/homework5.tex
licence: CC BY 4.0
route: pandoc-latex
fidelity: high
converted: '2026-09-14'
---

# Moral

**Source:** [`homework/homework5.tex`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/homework/homework5.tex) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.tex` (high)

Using different loss functions often gives other appealing summaries of the posterior distribution besides the posterior mean. Using these loss functions as the prediction error in regression problems can also lead to appealing methods such as quantile regression.

**Problem 4** (Motivation for the Jeffreys prior).

Recall that the *Kullback–Leibler (KL) Divergence* from a density $p$ to an approximating density $q$ (on a sample space $\mathcal{X}$ with respect to base measure $\mu$) is $$D_{\text{KL}}(p \,\|\, q) = \mathbb{E}_p\left[\log\frac{p(X)}{q(X)}\right] = \int_\mathcal{X}p(x)\log\frac{p(x)}{q(x)}\,d\mu(x),$$ where the integrand is treated as zero wherever $p(x) = 0$. For a density $p$ and a family $\mathcal{P}$, define the KL ball of radius $\varepsilon$ around $p$ as $$B_\varepsilon(p) = \{q\in\mathcal{P}:\; D_{\text{KL}}(p\,\|\,q) < \varepsilon\}$$

Now, assume we have a family $\mathcal{P}$ of positive densities $p_\theta$ parameterized by $\theta \in \Theta \subseteq \mathbb{R}^d$, with enough regularity for us to freely take derivatives under the integral, and for those derivatives to be continuous. In particular, assume the Fisher information $J(\theta)$ is continuous and (strictly) positive definite, so $|J(\theta)|>0$.

In this problem you will show that the Jeffreys prior $\Lambda$ spreads its prior mass evenly on $\mathcal{P}$, in the sense that for distinct values $\theta_1,\theta_2\in\Theta^{\circ}$ (the interior of $\Theta$), we have $$\lim_{\varepsilon\to 0} \frac{\Lambda(B_\varepsilon(p_{\theta_1}))}{\Lambda(B_\varepsilon(p_{\theta_2}))} = 1.$$ Here $\Lambda$ could refer either to the probability distribution with density proportional to $|J(\theta)|^{1/2}$ (if the Jeffreys prior is proper) or an infinite measure with density equal to $|J(\theta)|^{1/2}$. Note the slight abuse of notation where we use $\Lambda$ to refer both to the Jeffreys prior on $\Theta$ and to the corresponding prior on $\mathcal{P}= \{p_{\theta}:\;\theta\in \Theta\}$.

To rule out perversities, assume also that for each $\theta$ there is some radius $r_\theta$ such that $d_\theta(\zeta) = D_{\text{KL}}(p_{\theta}\,\|\,p_{\zeta})$ is convex for $\|\zeta-\theta\| \leq r$, and $\inf_{\|\zeta - \theta\| > r} d_\theta(\zeta) > 0$ (in particular, this implies identifiability). That is, small KL balls in $\mathcal{P}$ are not going to include $p_\zeta$ with faraway values of $\zeta$. You don’t need to explicitly use this condition; you can just not pay attention to what’s happening away from infinitesimal neighborhoods around $\theta_1$ and $\theta_2$ and assume everything is fine.

1.  For $\theta\in\Theta^{\circ}$, and any vector $a\in\mathbb{R}^d$, show that $$\begin{equation}
        \label{eq:lim-ratio}
    \lim_{\varepsilon\to 0} \frac{1}{\varepsilon^2} D_{\text{KL}}(p_{\theta} \,\|\, p_{\theta + \varepsilon a}) = \frac{1}{2}a'J(\theta)a,
    \end{equation}$$ or equivalently $D_{\text{KL}}(p_{\theta} \,\|\, p_{\theta + a}) = \frac{1}{2}a'J(\theta)a + o(\|a\|^2)$.

    **Hint 1:** Try differentiating the KL divergence and recall that, for $f:\;\mathbb{R}^d\to\mathbb{R}$, where $x,a\in \mathbb{R}^d$ and $\varepsilon\in \mathbb{R}$, we have $$\begin{align*}
      \frac{d}{d\varepsilon}f(x+\varepsilon a) &= a'\nabla f(x+\varepsilon a)\\
      \frac{d^2}{d\varepsilon^2}f(x+\varepsilon a) &= a'\nabla^2 f(x+\varepsilon a)a
    \end{align*}$$

    **Hint 2:** You are welcome to jump to the general case $d\geq 1$, but it may help to warm up with the case $d=1$, in which case the above boils down to $$\lim_{\varepsilon\to 0} \frac{1}{\varepsilon^2} D_{\text{KL}}(p_{\theta} \,\|\, p_{\theta + \varepsilon a}) = \frac{a^2}{2}J(\theta)$$ or more simply $$\lim_{\varepsilon\to 0} \frac{1}{\varepsilon^2} D_{\text{KL}}(p_{\theta} \,\|\, p_{\theta + \varepsilon}) = \frac{1}{2}J(\theta)$$

2.  Next, show that for any $\theta\in\Theta^{\circ}$, we have

    $$\lim_{\varepsilon\to 0}\frac{1}{\varepsilon^{d/2}} \Lambda\left(\{\zeta:\; (\zeta - \theta)'J(\theta)(\zeta - \theta) < \varepsilon\}\right) = \begin{cases} V_d/C_\Lambda &\text{if } \Lambda \text{ is proper and } \lambda(\theta) \propto_\theta |J(\theta)|^{1/2}\\ V_d &\text{if } \Lambda \text{ is improper and } \lambda(\theta) = |J(\theta)|^{1/2}\end{cases}.$$ where $V_d = \int_{\mathbb{R}^d}1\{\|u\|<1\} du$ is the volume of a unit ball in $\mathbb{R}^d$ and $C_\Lambda = \int_{\Theta} |J(\theta)|^{1/2} \,d\theta$ is the normalizing constant for the Jeffreys prior, when it is finite.

    **Hint:** Try the change of variables $\zeta(a) = \theta + J(\theta)^{-1/2}a$.

3.  Now, finish the argument by showing that we have $$\lim_{\varepsilon\to 0} \frac{1}{\varepsilon^{d/2}} \Lambda(B_{\varepsilon/2}(p_\theta)) = \begin{cases} V_d/C_\Lambda &\text{if } \Lambda \text{ is proper and } \lambda(\theta) \propto_\theta |J(\theta)|^{1/2}\\ V_d &\text{if } \Lambda \text{ is improper and } \lambda(\theta) = |J(\theta)|^{1/2}\end{cases}.$$

    **Hint:** Try to relate the sublevel sets of $f_\theta(\zeta) = D_{\text{KL}}(p_{\theta}\,\|\,p_\zeta)$ to sublevel sets of $\frac{1}{2}(\zeta-\theta)'J(\theta)(\zeta-\theta)$.

---

[← Moral](03-moral.md) · [Up: contents](index.md) · [Moral →](05-moral.md)
