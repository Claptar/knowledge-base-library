---
title: 5 Why is this called “Partial” Autocorrelation?
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf
source_file: sources/berkeley-stat153/spring-2025/LectureTwenty153248Spring2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Why is this called “Partial” Autocorrelation?

**Source:** [`LectureTwenty153248Spring2025.pdf`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/LectureTwenty153248Spring2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Why should the quantity _ϕ_<sup>ˆ</sup> _h_ (obtained by fitting AR( _h_ ) to the data) be called the Sample Partial Autocorrelation? It turns out that there is a connection between regression coefficients and something called “partial correlation” (see e.g., `https://en.wikipedia.org/ wiki/Partial_correlation` ).

Suppose we have data on two variables _x_ and _y_ : ( _x_ 1 _, y_ 1) _, . . ._ ( _xn, yn_ ). The correlation between them is defined in the usual way as:


Correlation is also related to regression. If we regress _yi_ on _xi_ and obtain the usual least squares estimators _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1, then


where var( _x_ ) =<sup>�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_xi −x_¯)2andvar(</sup><sup>_y_)=�</sup><sup>_n_</sup> _i_ =1<sup>(</sup><sup>_yi −y_¯)2.Notethat,inthissection,corr</sup> and var refer to things calculated on the observed data (as opposed to random variables).

Now instead of just having data on _x_ and _y_ , we also have data on other variables _z_ 1 _, . . . , zk_ . The dataset now is ( _yi, xi, zi_ 1 _, . . . , zik_ ) for _i_ = 1 _, . . . , n_ . The partial correlation between _x_ and _y_ given the variables _z_ 1 _, . . . , zk_ is denoted by corr( _x, y | z_ 1 _, . . . , zk_ ) and is defined as the correlation between the residual of _x_ given _z_ 1 _, . . . , zk_ and the residual of _y_ given _z_ 1 _, . . . , zk_ .

Here, residual of _x_ given _z_ 1 _, . . . , zk_ refers to the residual in the linear regression of _x_ given _z_ 1 _, . . . , zk_ :


5

where _β_<sup>ˆ</sup> 0<sup>_x, . . . ,β_ˆ</sup> _k_<sup>_x_arethefittedregressioncoefficientsof</sup><sup>_xi_on1</sup><sup>_, zi_1</sup><sup>_, . . . , zik_.</sup>

Similarly the residual in the linear regression of _y_ given _z_ 1 _, . . . , zk_ is


where _β_<sup>ˆ</sup> 0<sup>_y, . . . ,β_ˆ</sup> _k_<sup>_y_arethefittedregressioncoefficientsof</sup><sup>_yi_on1</sup><sup>_, zi_1</sup><sup>_, . . . , zik_.</sup> Therefore:


Similar to (2), there is a nice relationship between fitted regression coefficients in multiple linear regression and partial correlation. Consider the multiple regression of _y_ on _x_ as well _z_ 1 _, . . . , zk_ . Let the fitted regression coefficients be: _β_<sup>ˆ</sup> 0 _, β_<sup>ˆ</sup> _x, β_<sup>ˆ</sup> 1 _, . . . , β_<sup>ˆ</sup> _k_ :


Then it turns out that


This is the connection between a fitted regression coefficient (corresponding to a specific covariate) in multiple linear regression and the partial correlation between the response and the covariate given the other covariates.

Now let us come to the time series setting with data _y_ 1 _, . . . , yn_ . We fit AR(p) models using the regression:


Following the formula (3), we write


When the AR(p) model is stationary (we shall see in the next lecture on conditions for AR(p) models to be stationary), the population analogues of the variance terms above (var( _e_<sup>_yt|yt−_1</sup><sup>_,...,yt−p_+1</sup> ) and var( _e_<sup>_yt−p|yt−_1</sup><sup>_,...,yt−p_+1</sup> )) turn out to be equal, and they are nearly same in the sample so they can be dropped and we get


corr( _yt−p, yt | yt−_ 1 _, . . . , yt−p_ +1) can be called the partial autocorrelation at lag _p_ . This is the reason why the plot of _ϕ_<sup>ˆ</sup> _h_ (when the AR( _h_ ) model is fit to the data) is referred to as the sample PACF plot.

---

[← 4 Sample PACF](04-4-sample-pacf.md) · [Up: contents](index.md) · [6 Additional Optional Reading →](06-6-additional-optional-reading.md)
