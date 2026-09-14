---
title: 1 Bagging
source: https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf
source_file: sources/berkeley-stat-c245c-leishi/notes/Lecture_06_Ensemble_methods.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Bagging

**Source:** [`notes/Lecture_06_Ensemble_methods.pdf`](https://leishi-rocks.github.io/courses/ph240c/notes/Lecture_06_Ensemble_methods.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Bagging is also referred to as bootstrap aggregation illustrated in Figure 1. Suppose we have access to a dataset with observations _D_ ≜ _{_ ( _Yi, Xi_ ) _}_<sup>_n_</sup> _i_ =1<sup>,andtheyformanempiricaldistribution</sup><sup>_F_�</sup><sup>_n_.Thealgorithm</sup> works as follows:

1

1. Draw bootstrap samples from _D_ with replacement, denoted as _D_ 1<sup>_∗, . . . , D_</sup> _B_<sup>_∗_;</sup>

2. On each bootstrap sample, we build a classifier _fb_<sup>_∗_(</sup><sup>_x_)(canbetree,oranyofyourfavouritemethods);</sup>

3. Then final bagged classifier is then


Now let’s look into some details of bagging:

- We can clearly see that bagging sets equal weights to different classifier learnt in different bootstrap samples, i.e., _w_ 1 = _. . ._ = _wB_ = 1 _/B_ . This is actually somewhat suboptimal, as we are not efficiently using all the available information in our original data. Note that in each bootstrap sample _Db_<sup>_∗_,not</sup> all original data points in _{_ ( _Yi, Xi_ ) _}_<sup>_n_</sup> _i_ =1<sup>areusedinbuildingtheclassifier</sup><sup>_f_</sup> _b_<sup>_∗_(</sup><sup>_·_)(EfronandTibshirani,</sup> 1997). We can calculate the probability that a given data point is not drawn in a bootstrap sample as


How can we leverage all these unused data points to improve our classifier? The answer of this question is heuristically related to the core idea of Boosting.

- The advantages of bagging is that it is easy to implement, and it reduces variances – so has strong beneficial effect on high variance classifiers. To see the effect of variance reduction, note that bagged estimator has two layers of randomness: one comes from the original data, and another one comes from the bootstrap resampling as we take random samples with replacement from the original data. In fact, each bootstrap sample _Db_<sup>_∗_canbewrittenas</sup>


When _B_ =<sup>_n_</sup> _Pn_ goes through all possible combination of sample with repeated data points, the bagged classifier can be written as


which indicates Var[ _f_ ( _x_ )] _≤_ Var$$ _fb_<sup>_∗_(</sup><sup>_x_)$$(how?).</sup>

- Now we agree that bagging reduces the variance of a single bootstrapped classifier _fb_<sup>_∗_(</sup><sup>_·_),butcanwe</sup> do even better in variance reduction? The variance of _f_ ( _x_ ) is of the form


From this decomposition, we can see that individual tree variance is not the dominant term of the bagged classifier. The covariance between different trees is the main contributing factor for the variance. The intuitive answer of this question leads to the idea of random forest.

- Bagging provides a natural estimate of the test error. We can calculate the “out-of-bag-error” for each learnt classifier on the bootstrap sample. More formally, for each data point ( _Xi, Yi_ ) _∈D_ , define

2

_Si_ = _{b_ : ( _Xi, Yi_ ) _̸ ∈Db}_ to be the set of all classifiers that are not trained based on the data point ( _Xi, Yi_ ). Then the bagged classifier over all these dataset is


And the out-of-bag-error is simply the average error/loss that all these classifiers yield:

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Random forest →](03-2-random-forest.md)
