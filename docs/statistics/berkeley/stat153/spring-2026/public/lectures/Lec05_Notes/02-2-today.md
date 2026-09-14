---
title: 2 Today
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec05_Notes.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lec05_Notes.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Today

**Source:** [`public/lectures/Lec05_Notes.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lec05_Notes.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

## **2.1 Simple linear regression**

Let’s say we want to learn the relationship between two variables _y_ and _x_ - the goal is to predict _y_ given _x_ . For example, we might want to predict the height of an adult man ( _y_ ) given the height of his father ( _x_ ). _y_ is called the response variable or dependent variable, _x_ i the covariate or independent variable. We will start with the more general scenario and then extend this concept specifically to time series.

In simple linear regression, we are predicting _y_ given one covariate _x_ . In the case of multiple _x_ , say _{x_ 1 _, . . . , xp}_ , this is called multiple regression.

For the simple case, we are predicting _y_ from one covariate _x_ . For example: _y_ = _β_ 0 + _β_ 1 _x_ + _ϵ_

_β_ 0 and _β_ 1 are parameters that we will estimate from the data, where _β_ 0 is the intercept, which corresponds to the value of _y_ when _x_ = 0, and _β_ 1 represents the change in _y_ when _x_ changes by one unit.

We could observe, for example, pairs of data ( _x_ 1 _, y_ 1) _, . . . ,_ ( _xn, yn_ ) where each of these samples is a pair of fathers and sons. We then might write:

_yi_ = _β_ 0 + _β_ 1 _xi_ + _ϵi_ .

We can then estimate our _β_<sup>ˆ</sup> 0 and _β_<sup>ˆ</sup> 1 from the data, then use these to predict the value of the response variable _y_ ˆ (height of a new adult man) for a new covariate _x_ . We will talk about how to do this using the Python library `statsmodels` , but we will also talk about how to derive the solution mathematically.

1

For time series regression, we often have some observed data _y_ 1 _, . . . , yn_ that are observations for a single variable _y_ . In this case, we may try two main ways of predicting _y_ :

1. **Use time as a covariate** (many of the examples we’ve seen already do this – for example, the DJIA data, fMRI data, population data over time)


[resume] **Use lagged version of** _y_ **as the covariate.** For this case, we might take _xi_ = _yi_ =1. In this case, we are predicting a current value based on a prior time point. This is called Lagged Regression or AutoRegression.

## **2.2 How do we estimate** _β_ 0 **and** _β_ 1 **?**

There are a couple of ways to estimate _β_ 0 and _β_ 1. Standard libraries such as `statsmodels` use the least squares method. In this method, we minimize the error sum of squares:


### **2.2.1 Ordinary Least Squares (OLS)**

In ordinary least squares, we can solve for:

min _β_ 0 _,β_ 1 E[( _y−β_ 0 _−β_ 1 _x_ )<sup>2</sup> ], which will be the best fitting line at the population level. Solving this gives:

_β_ ˆ0 = _y_ ¯ _− β_ ˆ1 _x_ ¯ and _β_ ˆ1 = <u>∑</u> _ni_ <u>=1</u><sup><u>(</u></sup><sup>_<u>yi−y</u>_¯)(</sup><sup>_xi−x_¯)</sup> ~~∑~~ _<u>ni</u>_ =1<sup>(</sup><sup>_xi−x_¯)2</sup> where _y_ ¯ =<sup>_<u>y</u>_</sup><sup><u>1+</u></sup><sup>_···_</sup> _n_<sup><u>+</u></sup><sup>_<u>yn</u>_</sup> and _x_ ¯ =<sup>_<u>x</u>_</sup><sup><u>1+</u></sup><sup>_···_</sup> _n_<sup><u>+</u></sup><sup>_<u>xn</u>_</sup>

Let’s look at what this looks like in `statsmodels` with an example.

2

---

[← 1 Review](01-1-review.md) · [Up: contents](index.md)
