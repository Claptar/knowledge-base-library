---
title: Misinterpreting Hypothesis Tests
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-interpretation.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/testing-interpretation.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Misinterpreting Hypothesis Tests

**Source:** [`reader/testing-interpretation.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/testing-interpretation.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Hypothesis tests ubiquitous in science
Common misinterpretations:

1. p < 0.05, therefore there is an effect (or the effect size = the estimate)
2. p > 0.05, therefore there is no effect
3. p = 10^-6, therefore the effect is huge
4. p < 10^-6, therefore the data are significant and everything about our model is correct (in most naive interpretation)
5. Effect CI for men is [0.2, 3.2], for women is [-0.2, 2.8], therefore there is an effect for men and not for women

Dichotomous test doesn't eliminate uncertainty
CIs usually less misleading to novices

Interpreting tests is not easy or automatic
Hypothesis tests let us ask specific questions under specific modeling assumptions
Interpreting them requires care and experience

Top-tier medical journals let people publish claims reporting p-values without saying what model was used or what test was employed
Pretty bad when you think about it

Hyp. tests can be a good companion to critical thinking, never a substitute
All models are wrong, some are useful, but need experience and theory to understand when assumptions do or don't cause real trouble

### Common Objections to Hypothesis Testing

1. Why should I test $\theta = 0$? Is $\theta$ ever exactly 0?

   A: a. Test $H_0: |\theta| < \epsilon$ if you want
      If $\sigma_{\hat{\theta}} \ll \epsilon$, not much difference

   b. Most two-sided tests justify directional interest:
      If $T > c$, declare $\theta > 0$, if $T < -c$, declare $\theta < 0$ with $\mathbb{P}(\text{false claim}) < \alpha$

   c. Harder to answer in non-parametric problems
      e.g. $H_0: P = Q$ vs $H_1: P \neq Q$ for perm test, but alternative frameworks like Bayes force very strong assumptions on us

2. People only like frequentist results like p-values, CIs because they mistake them for Bayesian results
   "95% chance $\theta > 0$" is misinterpreted as a claim about $\mathbb{P}(\theta > 0 | X)$

   A: True, but subjective Bayesian results often misinterpreted as the posterior dist. of $\theta$ when really should be "posterior opinion about $\theta$"

---

[← Confidence Regions](02-confidence-regions.md) · [Up: contents](index.md)
