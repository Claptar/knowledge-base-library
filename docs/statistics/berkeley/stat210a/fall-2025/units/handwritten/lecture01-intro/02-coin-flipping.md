---
title: Coin Flipping
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture01-intro.pdf
source_file: sources/berkeley-stat210a/fall-2025/units/handwritten/lecture01-intro.pdf
licence: CC BY 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/handwritten/lecture01-intro.pdf`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/handwritten/lecture01-intro.pdf) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Coin Flipping

**Diaconis, Holmes, & Montgomery (2007):**

A coin is a bit more likely to land on the side it started on

Based on physical model (precession)
Predicted $\sim 51\%$ for typical human flipper

**Bartoš et al. (2023):**

$350,757$ coin flips
$48$ flippers using coins from $46$ countries
Found $178,079$ same-side outcomes ($\approx 50.8\%$)

## Frequentist analysis

$95\%$ confidence interval $[50.6\%, 50.9\%]$
Based on binomial model:
- Every flip has same probability $\theta$
- Flips are independent
$\Rightarrow \mathbb{P}_\theta(X \text{ same side flips}) = \frac{n!}{x!(n-x)!} \theta^x (1-\theta)^{n-x}$

Confidence interval construction mathematically ensures
$$\mathbb{P}_\theta(CI(X) \text{ covers } \theta) \ge 95\% \quad (\text{here, almost } =)$$

---

## Bayesian analysis

$95\%$ credible interval $[50.6\%, 50.9\%]$
Same binomial model, plus $\text{Unif}[0,1]$ prior on $\theta$
(Question: whose prior opinion was that?)

Binomial model was wrong!
- Different flippers had different probabilities
- Most flippers improved (got closer to $50\%$) over time

## Kinds of questions we'll ask in this course

### Bayesian and frequentist frameworks

What are pros & cons of each?
Where does the prior come from? (Does it matter?)
What does probability mean in each framework?

### Sufficiency:

Both analyses summarized data as "$X = 178,079$"
Did we lose anything? (Not under binomial model)
What about the model structure lets us do this?

---

## **Estimation:** What's a good way to estimate:

1) Overall $\theta$ in binomial model
no single best estimator for all $\theta$
$X/n$ "obvious choice" if $n = 350\text{k}$ (unless $\theta = 10^{-6}$)
less obvious for $n = 35$

2) $\theta_i$ for individual flipper $i$
new model: $X_i \stackrel{\text{ind.}}{\sim} \text{Binom}(n_i, \theta_i)$ for $i = 1, \dots, m$
how to use data from other flippers?

3) How fast $\theta_{i,t}$ changes from flip $1$ to flip $n_i$
variety of possible models
parametric & nonparametric

## **Testing:** How do we efficiently test hypotheses like

1) $H_0: \theta \le 50\%$ vs $H_1: \theta > 50\%$ (one-sided)
Unique best test exists

2) $H_0: \theta = 50\%$ vs. $H_1: \theta \ne 50\%$ (two-sided)
Natural choice exists

3) $H_0: \theta_i = \theta \text{ for all flippers}$ vs. $H_1: \theta_i \text{ varies}$
**Nuisance parameter** $\theta$ affects null distribution of any test statistic
Many ways for $(\theta_1, \dots, \theta_m)$ to be non-null should affect choice of test!

4) $H_0: \theta_i \text{ constant through time for all flippers}$
vs $H_1: \theta_{i,t} \text{ tends to be decreasing in } t$
Can test this nonparametrically)

---

## **Asymptotics:** No one calculated $350,757!$

Actual model: $X \sim N(n\theta, \, n\theta(1-\theta))$
(or $X_i \stackrel{\text{ind}}{\sim} N(n_i \theta_i, \, n_i \theta_i(1-\theta_i))$)

Want good asymptotic approximations to other models

---

[← Course introduction](01-course-introduction.md) · [Up: contents](index.md)
