---
title: p-Values
source: https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2026/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2026/blob/7dc8f80da94dff74532d9e3923afdb16a255262d/reader/testing-interpretation.qmd) — berkeley-stat210a · fall-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.qmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# p-Values

As we have previously defined hypothesis tests, they are characterized by dichotomous accept/reject decisions after choosing a null hypothesis, a test statistic, and a critical threshold. Sometimes we really do need to make a dichotomous decision (for example, the FDA really has to decide whether to approve a drug or not), but this is rare in practice. If our test statistic is large enough to reject $H_0:\;\theta=0$ at the $\alpha = 0.05$ level, we would usually still be interested in questions like:

- Would we have rejected $H_0$ at a stricter $\alpha$ level, like $\alpha = 0.01$ or $\alpha = 0.005$?

- Have we established that $\theta$ is far from zero, or only that it isn't exactly zero?

These questions can be answered by $p$-values and confidence regions, which enrich our dichotomous decision by respectively telling us about the outcome for other $\alpha$ values we could have used, and for other null hypotheses we could have tested.

## Informal definition

The $p$-value $p(X)$ is a measure of whether our data set would have led us to reject the null at various different $\alpha$ values. If we are rejecting for large values of a test statistic $T(X)$ then this boils down to asking how extreme $T(X)$ is relative to its null distribution, leading to the familiar informal definition of the $p$-value:

**Definition (Informal):** The $p$-value is the probability for a test statistic $T(X)$ to be at least as large as its realized value, under the assumption that the null is true. That is, for a fixed value $x\in\cX$, the $p$-value $p(x)$ should be $\PP_{H_0}(T(X)\geq T(x))$, or more precisely
$$
p(x) = \sup_{\theta\in\Theta_0} \PP_{\theta}(T(X) \geq T(x)),
$$
allowing for the possibility of a composite null. Then the random variable $p(X)$ is the $p$-value.

**Example: Binomial** If $X\sim \text{Binom}(n,\theta)$ and we want to test $H_0:\;\theta\leq 0.5$ vs $H_0:\;\theta > 0.5$, the UMP test rejects for large values of $X$. Thus, the $p$-value is
$$
p(x) = \sup_{\theta\leq 0.5} \PP_\theta(X\geq x) = \PP_{0.5}(X\geq x),
$$
since $X$ is stochastically increasing and the probability is therefore maximized at the boundary.

**Example: $Z$-test** If $X\sim N(\theta,1)$ and we are testing $H_0:\;\theta = 0$ vs $H_1:\;\theta \neq 0$, the two-sided test rejects for large $T(X)=|X|$. The two-sided $p$-value is therefore
$$
p(x) = \PP_0(|X|>|x|) = 2(1-\Phi(|x|)).
$$

## Formal definition

Not all tests are easily characterized as rejecting when some $T(X)$ is above a threshold; for example, a two-sided UMPU test rejects when some $T(X)$ is either large or small. Thus it is useful to have a more general definition:

Assume we are testing $H_0:\;\theta\in\Theta_0$ vs $H_1:\;\theta\in\Theta_1$ in a model $\cP$ based on data $X$, and that we have a test $\phi_\alpha$ for every significance $\alpha \in [0,1]$:
$$
\sup_{\theta\in\Theta_0} \EE_\theta \phi_\alpha(X) \leq \alpha.
$$
Assume further that $\phi_{\alpha}$ is non-decreasing in $\alpha$ (when the test rejects for smaller/stricter $\alpha$, it also rejects for larger/more lenient $\alpha$):
$$
\phi_{\alpha_1}(X) \leq \phi_{\alpha_2}(X) \quad \text{ if } \alpha_1\leq \alpha_2.
$$

**Definition (Formal):** Then, we can define the $p$-value with respect to this family of tests as the value of $\alpha$ for which the test barely rejects:
$$
p(x) = \sup \{\alpha:\; \phi_\alpha(x) < 1\} = \inf \{\alpha:\; \phi_\alpha(x) = 1\},
$$
and in terms of the rejection regions:
$$
p(x) = \sup \{\alpha:\; x \notin R_\alpha\} = \inf\{\alpha:\; x \in R_\alpha\}.
$$

**Example: Exponential** Suppose that we are testing $H_0:\;\theta=1$ vs $H_1:\;\theta\neq 1$ in the model $X \sim \text{Exp}(\theta)$. We can use either the equal-tailed test, or the UMPU test. Consider a value $x>1$, which will be in the acceptance region (for sufficiently small $\alpha$) or the right lobe of the rejection region (for sufficiently large $\alpha$). For either test, the acceptance region's right boundary decreases continuously with $\alpha$, so the $p$-value is the unique value of $\alpha$ for which $x$ is on the boundary. For the equal-tailed test, we have at that $\alpha$ value
$$
\alpha/2 = \PP_1(X>x) = e^{-x},
$$
so $p(x) = 2e^{-x}$. For the UMPU test $p(x)$ is defined implicitly as the value of $\alpha$ for which $c_2(\alpha) = x$, which we can solve for numerically.

This formal definition reduces to our informal definition if the test $\phi_\alpha$ rejects for large $T(X)$ and the critical threshold is tight:

**Proposition:** Assume that for each $\alpha$, we reject for large $T(X)$, taking the threshold $c_\alpha$ as small as possible while achieving Type I error control:[^1]
$$
c_\alpha = \min \left\{c:\; \PP_\theta(T(X) > c) \leq \alpha, \text{ for all } \theta\in\Theta_0 \right\},
$$
noting that the minimum is well-defined because (complementary) CDFs are right-continuous.

At the boundary, we either

- (non-randomized $\phi$) reject if $\PP_\theta(T(X) \geq c_\alpha) \leq \alpha$ for all $\theta\in\Theta_0$, or

- (randomized $\phi$) reject with probability
$$
\gamma_\alpha = \max\left\{ \gamma:\; \PP_\theta(T > c_\alpha) + \gamma\PP_\theta(T = c_\alpha)  \leq \alpha, \forall \theta\in\Theta_0\right\}
$$

Then the two definitions of $p(x)$ coincide.

*Proof:* In the non-randomized case, define $\gamma_\alpha = 1$ if we reject at the boundary and $0$ otherwise.

Let $p_1(x) = \sup_{\theta\in\Theta_0} \PP_\theta(T(X)\geq T(x))$, and $p_2(x) = \sup\{\alpha:\; \phi_\alpha(x) < 1\}$. We have
$$
\begin{aligned}
p_1(x) > \alpha
&\iff \PP_\theta(T(X) \geq T(x)) > \alpha, \text{ for some } \theta\in\Theta_0\\
&\iff c_\alpha > x, \text{ or } c_\alpha = x \text{ and } \gamma_\alpha < 1\\
&\iff \phi_\alpha(x) < 1.
\end{aligned}
$$
But then
$$
p_2(x) = \sup\{\alpha:\; p_1(x) > \alpha\} = p_1(x),
$$
as desired.$\blacksquare$

## Super-uniformity

The $p$-value for any valid test $\phi_\alpha$ is **super-uniform** on the null, meaning it is stochastically larger than uniform:
$$
\PP_\theta( p(X) \leq \alpha ) \leq \alpha, \text{ for all } \theta\in\Theta_0.
$$
Note that $p(x) \leq \alpha$ if and only $\phi_{\alpha+\ep}(x) = 1$, for all $\ep>0$. Thus, for $\theta \in \Theta_0$, we have
$$
\begin{aligned}
\PP_\theta(p(X) \leq \alpha)
&= \PP_\theta\left( \phi_{\alpha+\ep}(X) = 1, \text{ for all } \ep>0 \right)\\
&= \lim_{\ep \downarrow 0} \PP_\theta\left(\phi_{\alpha+\ep}(X) = 1\right)\\
&\leq \lim_{\ep \downarrow 0} \EE_\theta \left[ \phi_{\alpha+\ep}(X)\right]\\
&\leq \alpha
\end{aligned}
$$

## Interpreting the $p$-value

One important thing to remember when we interpret the $p$-value that it depends on which statistical test we choose (as well as the data, the model, and the null hypothesis). When the null and/or alternative hypothesis are composite, there may be a range of different but justifiable choices of test. In that case, it would be a mistake to think of the $p$-value for  any one of those tests as the canonical summary of the evidence in the data against the null.

**Example: (Multivariate Gaussian)** Suppose we observe $X \sim N_d(\mu, I_d)$ and wish to test the point null $H_0: \mu = 0$ against the composite alternative $H_1: \mu \neq 0$. For $d \geq 1$, the alternative is bi-directional, but most analysts will agree on the standard two-sided test. By constrast, for $d\geq 2$, the alternative is *multidirectional*, so there are different tests we could choose depending on our beliefs about which alternatives are more likely than others; the higher the dimension of the problem, the higher the stakes of this choice.

For example, if we want our test to be invariant to the direction $\frac{\theta}{\|\theta\|}$, we should reject for large values of the two-norm $\|X\|_2$. But suppose instead we expect $\theta$ to be sparse if it is nonzero; then $\|X\|_\infty = \max_{i=1}^d |X_i|$ might be a much better choice. The first test is called the $\chi^2$ test, because $\|X\|_2^2$ has a $\chi_d^2$ distribution under the null, and the second is called the max test; each dominates the other in different sparsity regimes.

The widget below shows the power curves as a function of $\theta$ when $\mu$ is a $k$-sparse unit vector with equal nonzero entries and total norm $\|\mu\|_2=\theta$:
$$
\mu = \theta \cdot \frac{1}{\sqrt{k}} \binom{1_k}{0_{d-k}},
$$
where $1_n$ and $0_n$ are respectively the all-ones and all-zeros vectors in $\RR^n$. By playing with $d$ and $k$ you can see that the max-test outperforms the $\chi^2$ test when $\mu$ is sufficiently sparse, but the reverse is true if $\mu$ is dense; and the differences become more pronounced as $d$ grows larger.

```r
#| echo: false
#| output: false

# We'll compute power curves for a grid of d and k values
# and pass them to OJS as data

library(tidyverse)

# Function that computes power curve for given d and k
compute_power_curve <- function(d_val, k_val) {
  theta_max <- 3 * d_val^0.25
  theta_vals <- seq(0, theta_max, length.out = 101)

  critical_chi <- qchisq(0.95, df = d_val)

  tibble(
    d = d_val,
    k = k_val,
    theta = theta_vals,
    chi_power = sapply(theta_vals, function(theta) {
      mu_val <- theta / sqrt(k_val)
      ncp <- k_val * mu_val^2
      pchisq(critical_chi, df = d_val, ncp = ncp, lower.tail = FALSE)
    })
  )
}

# Pre-compute for a reasonable range of d and k
d_vals <- 2:100
k_vals <- 1:20

power_data <- map_dfr(d_vals, function(d_val) {
  map_dfr(k_vals[k_vals <= 20], function(k_val) {
    compute_power_curve(d_val, k_val)
  })
})

ojs_define(power_data_r = power_data)
```

```ojs
//| echo: false

// Standard normal CDF approximation
normalCDF = (x) => {
  const t = 1 / (1 + 0.2316419 * Math.abs(x));
  const d = 0.3989423 * Math.exp(-x * x / 2);
  const prob = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274))));
  return x > 0 ? 1 - prob : prob;
}

// Interactive controls
viewof d = Inputs.range([2, 100], {value: 10, step: 1, label: "d"})
viewof k = Inputs.range([1, 20], {value: 3, step: 1, label: "k"})

// Filter power data for current d and k
chiPowerData = transpose(power_data_r).filter(row => row.d === d && row.k === k)

// Infinity norm critical value
criticalInf = {
  const alpha = 0.05;
  let low = 0, high = 5;
  while (high - low > 0.0001) {
    const mid = (low + high) / 2;
    const pNull = 1 - Math.pow(2 * normalCDF(mid) - 1, d);
    if (pNull > alpha) low = mid;
    else high = mid;
  }
  return (low + high) / 2;
}

// Calculate power functions
data = chiPowerData.map(row => {
  const theta = row.theta;
  const muVal = k > 0 ? theta / Math.sqrt(k) : 0;

  // Chi-squared test power from R
  const powerChi = row.chi_power;

  // Infinity norm test power
  const probOneSignalBelow = normalCDF(criticalInf - muVal) - normalCDF(-criticalInf - muVal);
  const probOneNonSignalBelow = 2 * normalCDF(criticalInf) - 1;

  const powerInf = 1 - Math.pow(probOneSignalBelow, k) * Math.pow(probOneNonSignalBelow, d - k);

  return {
    theta: theta,
    chi: Math.max(0, Math.min(1, powerChi)),
    inf: Math.max(0, Math.min(1, powerInf))
  };
})

// Create the plot
Plot.plot({
  width: 800,
  height: 400,
  marginTop: 60,
  marginLeft: 100,
  marginBottom: 100,
  marginRight: 120,
  style: {
    fontSize: "18px"
  },
  x: {
    domain: [0, 3 * Math.pow(d, 0.25)],
    label: "θ",
    labelAnchor: "center",
    labelOffset: 60
  },
  y: {
    domain: [0, 1],
    label: "Power",
    labelAnchor: "center",
    labelOffset: 70
  },
  marks: [
    Plot.line(data, {x: "theta", y: "chi", stroke: "steelblue", strokeWidth: 2}),
    Plot.line(data, {x: "theta", y: "inf", stroke: "red", strokeWidth: 2}),
    Plot.ruleY([0]),
    Plot.ruleY([0.05], {stroke: "gray", strokeDasharray: "4 4"}),
    Plot.text(["Power Comparison: Chi-Squared Test vs Infinity Norm Test"], {
      x: 1.5 * Math.pow(d, 0.25),
      y: 1.08,
      fontSize: 18,
      fontWeight: "bold",
      textAnchor: "middle"
    }),
    // Legend for chi-squared test (top left)
    Plot.lineX([{x: 0.3, y: 0.95},
                {x: 0.7, y: 0.95}], {
      x: "x", y: "y",
      stroke: "steelblue",
      strokeWidth: 2
    }),
    Plot.text(["‖X‖₂ test"], {
      x: 0.75,
      y: 0.95,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    }),
    // Legend for infinity norm test (top left)
    Plot.lineX([{x: 0.3, y: 0.88},
                {x: 0.7, y: 0.88}], {
      x: "x", y: "y",
      stroke: "red",
      strokeWidth: 2
    }),
    Plot.text(["‖X‖∞ test"], {
      x: 0.75,
      y: 0.88,
      fontSize: 16,
      fill: "black",
      textAnchor: "start"
    })
  ]
})
```

Thus, depending on what test we use on the same data set, we can get very different $p$-values.

<!-- ### Randomized $p$-values -->

<!-- We do not usually bother to randomize the $p$-value, but if we want to, we can augment the data with a uniform random variable $U \sim \text{Unif}[0,1]$ independently of $X$, and define a new test on the augmented sample space: -->
<!-- $$ -->
<!-- \tilde\phi_\alpha(x,u) = 1\{\phi_\alpha(x) > 1-u\}. -->
<!-- $$ -->
<!-- The test $\tilde\phi$ has conditional rejection probability $\phi_\alpha(x)$ given $X=x$,  so -->
<!-- $$ -->
<!-- \EE_\theta \tilde\phi_\alpha(X,U) = \EE_\theta \phi_\alpha(X), -->
<!-- $$ -->
<!-- and it is is monotone in $\alpha$ if $\phi_\alpha$ was. Then we can define  -->

---

[Up: contents](index.md) · [Confidence Regions →](02-confidence-regions.md)
