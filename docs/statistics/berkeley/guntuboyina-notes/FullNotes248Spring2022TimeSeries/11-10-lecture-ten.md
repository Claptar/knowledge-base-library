---
title: 10 Lecture Ten
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 10 Lecture Ten

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **10.1 Summary: General Filtering and Smoothing**

Let us use the following simpler notation. Let _fs|t_ ( _xs_ ) denote the conditional density of _Xs_ given _Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_ evaluated at the point _xs_ .

Filtering recursions for general state space models are (see Lecture Six) the following. The one-step ahead prediction update is


and the filter update is


42

The backward smoothing recursion for general state space models is (see Lecture Nine):


This can be rewritten in the following way. Note first that the denominator (inside the square brackets) equals:


Thus (63) becomes


Note also that the _fs|s_ ( _xs_ ) term on the right hand side can be pulled out of the integral (as it does not depend on _xs_ +1 which is the variable of integration). Thus the smoothing recursion becomes:


### **10.2 Summary: Kalman Filtering and Smoothing**

The general filtering and smoothing recursions can be computed in closed form for the case of the linear Gaussian state space model:


with _X_ 0 _, U_ 1 _, . . . , V_ 0 _, V_ 1 _, . . ._ independent and _Ut ∼ N_ (0 _,_ Σ _t_ ) and _Vt ∼ N_ (0 _, Rt_ ). Here every density _fs|t_ is normal and we shall write _ms|t_ and _Qs|t_ for the mean and covariance corresponding to the (possibly multivariate) normal density _fs|t_ . The one-step ahead prediction update (61) becomes


The filter update (62) becomes


Finally the smoothing backward recursion (63) becomes


where


43

### **10.3 Special Case: Local Level Model**

Let us specialize the Kalman filtering and smoothing recursions for the special case of the local level model:


We have already seen that the Kalman filter for the local level model is:


and

The Kalman smoothing equations become (note that Γ _s_ +1 =


and


This local level model is useful for estimating smooth trends in time series. However it does not work well for estimating nonsmooth trends such as piecewise constant trend functions. For piecewise constant trend functions, using certain non-Gaussian distributions for the evolution errors _{Zt}_ works well. For example, one can use


or


In (65), _C_ (0 _, σZ_<sup>2)denotestheCauchydensitycenteredat0withscaleparameter</sup><sup>_σZ_:</sup>


(66) is a mixture density with two components: the first component is a normal density centered at zero with small variance and the second component is a normal density centered at zero with variance _σ_ 2<sup>2.Forfittingpiecewiseconstanttrendfunctions,wewouldtake</sup><sup>_α_to</sup> be close to 1.

44

When the density of _Zt_ is not normal (as when it is of the form (65) or (66)), the overall model is not “linear Gaussian” so that Kalman filtering and smoothing are not applicable. We will study two ways of solving the filtering and smoothing problems in such models. The first approach is to numerically evaluate the general recursions of Section 10.1 by discretization. This method is described in the next section. The second approach is to use Monte Carlo approximation and we shall discuss this later (this approach is known as “Sequential Monte Carlo” and is the main focus of the Chopin-Papaspiliopoulos book for example).

### **10.4 Numerical Evaluation of** _Xs | Y_ 0 = _y_ 0 _, . . . , Yt_ = _yt, θ_

This method works for arbitrary state space models. It is also conceptually simpler (compared to the Kalman recursions) but it is computationally quite intensive because we need to recursively compute entire densities (as opposed to just means and covariances as in the Kalman recursions).

We shall discretize space by placing a dense grid _x_<sup>(</sup><sup>_g_)</sup> _, g ∈ G_ covering the range of _Xt_ . We shall use the same grid for each _Xt_ for simplicity although in principle different grids may be used for different values of _t_ . We shall reduce all densities to probability mass functions over _{x_<sup>(</sup><sup>_g_)</sup> _, g ∈ G}_ . Let _ps|t_ ( _x_<sup>(</sup><sup>_g_)</sup> ) _, g ∈ G_ denote the probability mass function that approximates the density _fs|t_ ( _·_ ) i.e.,


or, more precisely,


From knowledge of _ps|t_ ( _x_<sup>(</sup><sup>_g_)</sup> ) _, g ∈ G_ , the density _fs|t_ ( _x_ ) cannot be determined precisely for all _x_ but it can be approximated well if the grid _G_ is dense. For example, one can use the approximation


We shall discretize the recursions (61), (62) and(63). The discrete equation corresponding to the one-step ahead prediction update (61) is given by


The normalization constant can be written explicitly as


The discrete equation corresponding to the filtering update (62) is given by


which becomes the following with proper normalization:


Finally the discretized version of the smoothing recursion (63) is


45

These three equations (67), (68) and (69) can be implemented to compute _ps|t_ for all _s ≤ t_ . The recursions can be initialized with


This corresponds to a diffuse prior on _X_ 0.

These recursions are used, for example, to fit the local level model with evolution errors (65) or (66).

### **10.5 Recommended Reading for Today**

1. Kalman smoothing equations for the local level model can be found in Section 2.4 of the Durbin-Koopman book and Example 8.1 of the S¨arkk¨a book

2. The numerical recursions for filtering and smoothing can be found in Section 6.3 of the Kitagawa-Gersch book and Section 14.3 of the Kitagawa book.

3. For estimating smooth trend functions with state space models, see Section 8.2 of the Kitagawa-Gersch book or Chapter 11 of the Kitagawa book.

4. The local level model with Cauchy errors has been used to fit a piecewise constant trend function in Section 14.4 of the Kitagawa book (they actually used the more general Pearson family for the evolution errors). Section 8.4 of the Kitagawa-Gersch book also considers the Pearson family for the evolution errors as well as the normal mixture distribution (66).

---

[← 9 Lecture Nine](10-9-lecture-nine.md) · [Up: contents](index.md) · [11 Lecture Eleven →](12-11-lecture-eleven.md)
