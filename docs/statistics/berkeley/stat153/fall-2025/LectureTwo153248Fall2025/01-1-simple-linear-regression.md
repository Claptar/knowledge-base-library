---
title: 1 Simple Linear Regression
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwo153248Fall2025.pdf
source_file: sources/berkeley-stat153/fall-2025/LectureTwo153248Fall2025.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Simple Linear Regression

**Source:** [`LectureTwo153248Fall2025.pdf`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/LectureTwo153248Fall2025.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We want to learn the relationship between two variables _y_ and _x_ , with the aim of predicting _y_ given the value of _x_ . _y_ is called the response variable, and _x_ is called the covariate. For example (this was one of the original applications of regression), _y_ denotes the height of an adult man, and _x_ denotes the height of their father. The linear regression model assumes that _y_ is related to _x_ via the equation:


where _β_ 0 and _β_ 1 are parameters, and _ϵ_ denotes an error term which captures deviations of _y_ from the assumed equation _β_ 0 + _β_ 1 _x_ . The parameters _β_ 0 and _β_ 1 can be interpreted as follows: _β_ 0 denotes the value of _y_ when _x_ = 0 and _β_ 1 represents the change in _y_ when _x_ changes by one unit.

We observe data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) on the covariate and response variables corresponding to _n_ instances (in the height example, we have data on heights for _n_ father-son pairs). Writing the equation (1) for each individual pair ( _xi, yi_ ) we get


The observed data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) will be used to obtain estimates _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 (as well as uncertaintly quantification) for the parameters _β_ 0 and _β_ 1. After obtaining these estimates, one can predict the value of the response variable for a possibly new covariate value _x_ new by _β_ ˆ0 + _β_ ˆ1 _x_ new.

We will implement the equations for obtaining _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 from the observed data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) using the Python library `statsmodels` . We will also study the math behind this process.

To apply linear regression, we need data on both _y_ and _x_ . In the time series context, the observed data is _y_ 1 _, . . . , yn_ which represent observations for a single variable _y_ . There is no additional data on another variable _x_ . In order to apply regression methods to time series, we need to create a covariate variable _x_ . There are two main ways of doing it:

1

1. **Time as covariate** : Here we take the time index as the covariate _x_ . For example, in the time series dataset on the population of the United States for each month from January 1959 to December 2024: _n_ denotes the total number of data points, _xi_ = _i_ and _yi_ denotes the observed population data for the _i_<sup>th</sup> month (first month is January 1959, second month is February 1959 and so on).

2. **Lagged** _y_ **as covariate** : Here we take _xi_ = _yi−_ 1. In other words, the covariate equals the response at the previous time point. This kind of regression is called Lagged Regression or, more commonly, AutoRegression.

For now, we shall focus on the first kind of regression (time as covariate). We shall study AutoRegression in more detail later.

---

[Up: contents](index.md) · [2 Estimation of β 0 and β 1 →](02-2-estimation-of-β-0-and-β-1.md)
