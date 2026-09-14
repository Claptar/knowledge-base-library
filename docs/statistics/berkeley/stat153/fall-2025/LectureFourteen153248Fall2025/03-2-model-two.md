---
title: 2 Model Two
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFourteen153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureFourteen153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Model Two

**Source:** [`LectureFourteen153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureFourteen153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This model is given by:


The parameters are _τ_ 1<sup>2</sup><sup>_, . . . , τ_</sup> _n_<sup>2.Since these represent variances, we refer to this as a “variance</sup> model”. _τt_ can be interpreted as the magnitude of _yt_ . This model is useful when we care only about the magnitudes of the observations _yt_ (and not their signs).

Model (2) (similar to Model One from the previous section) is also a high-dimensional model because the number of parameters is the same as the number of observations.

The likelihood for this model is proportional to


Note that the likelihood depends on the data only through the squares _y_ 1<sup>2</sup><sup>_, . . . , y_</sup> _n_<sup>2.Therefore</sup> the squares _y_ 1<sup>2</sup><sup>_, . . . , y_</sup> _n_<sup>2formthe“sufficientstatistic”inthismodel.Under(2),wehave</sup>


where _χ_<sup>2</sup> 1<sup>denotes the chi-squared distribution with 1 degree of freedom.Instead of writing the</sup> likelihood in terms of the raw data _yt_ , we can also write the likelihood using the squares _yt_<sup>2.</sup> This will lead to a slightly different form for the likelihood that should still be proportional to (3). To see this, observe that the density of _χ_<sup>2</sup> 1<sup>is proportional to</sup><sup>_x−_1</sup><sup>_/_2 exp(</sup><sup>_−x/_2) so that</sup> the density of _τt_<sup>2</sup><sup>_χ_2</sup> 1<sup>isproportionalto</sup>


2

The likelihood written in terms of _y_ 1<sup>2</sup><sup>_, . . . , y_</sup> _n_<sup>2isthus</sup>


The term ( _yt_<sup>2)</sup><sup>_−_1</sup><sup>_/_2above can be dropped as it is a constant not depending on the parameters</sup> _τt_<sup>2.Droppingitleadsto(3).</sup>

The log-likelihood is:


It is a convention to write optimization problems for computing estimators as minimization problems (as opposed to maximization). For this, we write the negative log-likelihood which is given by:


As _τt_ is a standard deviation parameter that is constrained to be positive, it is better to deal with _αt_ = log _τt_ instead of _τt_ directly. This reparameterization has the following benefits:

- **Unconstrained Optimization** : Unlike _τt_ , which must be positive, _αt_ can take any real value, allowing for more stable numerical optimization.

- **Improved Computational Stability** : Variance parameters can vary over several orders of magnitude, and working in the log scale reduces numerical precision issues.

Because of these benefits, many variance modeling approaches use log-variance transformations (see e.g., stochastic volatility models).

Writing the negative log-likelihood in terms of _αt_ = log _τt_ , we get


If we minimize the above (without any additional regularization) with respect to _αt_ , we obtain _αt_ = log _|yt|_ , or equivalently, _τt_<sup>2=</sup><sup>_y_</sup> _t_<sup>2.Inotherwords,theparameters</sup><sup>_τ_2</sup> _t_<sup>willfully</sup> interpolate (overfit) the sufficient statistics _yt_<sup>2.</sup>

For a more useful estimation procedure, we need to introduce regularization. If we assume that _αt_ is smooth, we can add the penalty<sup>�</sup><sup>_n_</sup> _t_ =2<sup>_−_1((</sup><sup>_αt_+1</sup><sup>_−αt_)</sup><sup>_−_(</sup><sup>_αt−αt−_1))2or �</sup><sup>_n_</sup> _t_ =2<sup>_−_1</sup><sup>_|_(</sup><sup>_αt_+1</sup><sup>_−_</sup> _αt_ ) _−_ ( _αt − αt−_ 1) _|_ to the negative log-likelihood. This leads to the estimators _α_ ˆ _t_<sup>ridge</sup> ( _λ_ ) and _α_ ˆ _t_<sup>lasso</sup> ( _λ_ ) which are defined as the minimizers of

and


respectively. The penalties encourage smoothness in _{αt}_ , leading to more stable and interpretable variance estimates. These optimizations are convex and they can be solved, for example, using functions from the python library `cvxpy` just as we solved _β_<sup>ˆridge</sup> ( _λ_ ) and _β_ ˆ<sup>lasso</sup> ( _λ_ ) from the previous section.

3

---

[← 1 Model One](02-1-model-one.md) · [Up: contents](index.md) · [3 Model Three →](04-3-model-three.md)
