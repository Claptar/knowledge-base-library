---
title: Introduction
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Ch6_Regularization.pdf
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Ch6_Regularization.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`public/lectures/Ch6_Regularization.pdf`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Ch6_Regularization.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

��������������������������������������������� �����������������������������������

��������������� ����������������������� ���������������������������

# 6 Linear Model Selection and Regularization


In the regression setting, the standard linear model


is commonly used to describe the relationship between a response _Y_ and a set of variables _X_ 1 _, X_ 2 _, . . . , Xp_ . We have seen in Chapter 3 that one typically fits this model using least squares.

In the chapters that follow, we consider some approaches for extending the linear model framework. In Chapter 7 we generalize (6.1) in order to accommodate non-linear, but still additive, relationships, while in Chapters 8 and 10 we consider even more general non-linear models. However, the linear model has distinct advantages in terms of inference and, on realworld problems, is often surprisingly competitive in relation to non-linear methods. Hence, before moving to the non-linear world, we discuss in this chapter some ways in which the simple linear model can be improved, by replacing plain least squares fitting with some alternative fitting procedures. Why might we want to use another fitting procedure instead of least squares? As we will see, alternative fitting procedures can yield better _prediction accuracy_ and _model interpretability_ .

- _Prediction Accuracy_ : Provided that the true relationship between the response and the predictors is approximately linear, the least squares estimates will have low bias. If _n ≫ p_ —that is, if _n_ , the number of observations, is much larger than _p_ , the number of variables—then the least squares estimates tend to also have low variance, and hence will perform well on test observations. However, if _n_ is not much larger than _p_ , then there can be a lot of variability in the least squares fit, resulting in overfitting and consequently poor predictions on future observations not used in model training. And if _p > n_ , then there is no longer a unique least squares coefficient estimate: there are infinitely

© Springer Nature Switzerland AG 2023

229

G. James et al., _An Introduction to Statistical Learning_ , Springer Texts in Statistics, https://doi.org/10.1007/978-3-031-38747-0_6

230 6. Linear Model Selection and Regularization

many solutions. Each of these least squares solutions gives zero error on the training data, but typically very poor test set performance due to extremely high variance.<sup>1</sup> By _constraining_ or _shrinking_ the estimated coefficients, we can often substantially reduce the variance at the cost of a negligible increase in bias. This can lead to substantial improvements in the accuracy with which we can predict the response for observations not used in model training.

- _Model Interpretability_ : It is often the case that some or many of the variables used in a multiple regression model are in fact not associated with the response. Including such _irrelevant_ variables leads to unnecessary complexity in the resulting model. By removing these variables—that is, by setting the corresponding coefficient estimates to zero—we can obtain a model that is more easily interpreted. Now least squares is extremely unlikely to yield any coefficient estimates that are exactly zero. In this chapter, we see some approaches for automatically performing _feature selection_ or _variable selection_ —that is, feature for excluding irrelevant variables from a multiple regression model. selection

selection variable selection

There are many alternatives, both classical and modern, to using least squares to fit (6.1). In this chapter, we discuss three important classes of methods.

- _Subset Selection_ . This approach involves identifying a subset of the _p_ predictors that we believe to be related to the response. We then fit a model using least squares on the reduced set of variables.

- _Shrinkage_ . This approach involves fitting a model involving all _p_ predictors. However, the estimated coefficients are shrunken towards zero relative to the least squares estimates. This shrinkage (also known as _regularization_ ) has the effect of reducing variance. Depending on what type of shrinkage is performed, some of the coefficients may be estimated to be exactly zero. Hence, shrinkage methods can also perform variable selection.

- _Dimension Reduction_ . This approach involves _projecting_ the _p_ predictors into an _M_ -dimensional subspace, where _M < p_ . This is achieved by computing _M_ different _linear combinations_ , or _projections_ , of the variables. Then these _M_ projections are used as predictors to fit a linear regression model by least squares.

In the following sections we describe each of these approaches in greater detail, along with their advantages and disadvantages. Although this chapter describes extensions and modifications to the linear model for regression seen in Chapter 3, the same concepts apply to other methods, such as the classification models seen in Chapter 4.

> 1When _p ≫ n_ , the least squares solution that has the smallest sum of squared coefficients can sometimes perform quite well. See Section 10.8 for a more detailed discussion.

6.1 Subset Selection 231

---

[Up: contents](index.md) · [6.1 Subset Selection →](02-6-1-subset-selection.md)
