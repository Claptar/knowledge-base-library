---
title: 1. Solution.
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf
source_file: sources/berkeley-stat210a/fall-2024/old-exams/solution2019.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Solution.

**Source:** [`old-exams/solution2019.pdf`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/old-exams/solution2019.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- (a) By inspection the Poisson density _e_<sup>_X_log</sup><sup>_θ−θ_</sup> _/x_ ! is an exponential family, so the MLE solves _EθX_ = _X_ ; the MLE is therefore _θ_<sup>ˆ</sup> = _X_ . Its risk is


- (b) The posterior density is


Hence _θ | X ∼_ Gamma( _X_ + _k, β_ + 1). This is true for any setting of the prior parameters so the prior is conjugate.

- (c) The Bayes estimator solves


- (d) For the minimization problem in the last part, the minimized value is


- (e) Taking arbitrary _k >_ 1, the sequence Γ( _k, βn_ ) has limiting risk equal to 1, which is also the sup-risk of the MLE. Hence it is a least-favorable sequence and the MLE is minimax.

3

- (f) For the usual squared error loss, the Bayes estimator is the posterior mean and the conditional expectation of the loss (given _X_ ) is therefore the posterior variance, which is ( _X_ + _k_ + 1) _/_ (1 + _β_ )<sup>2</sup> . The Bayes risk is then


where we use E _X_ = E _θ_ = _k/β_ . If we fix _k >_ 1 and send _β →_ 0, the Bayes risk tends to _∞_ . The minimax risk is larger than any Bayes risk, so it is also infinite.

4

---

[← 1. Poisson minimax estimation (24 points, 4 points / part).](03-1-poisson-minimax-estimation-24-points-4-points-part.md) · [Up: contents](index.md) · [2. ANOVA with random effects (25 points, 5 points / part). →](05-2-anova-with-random-effects-25-points-5-points-part.md)
