---
title: 23 Lecture Twenty Three
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes201AFall2022.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 23 Lecture Twenty Three

**Source:** [`FullNotes201AFall2022.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes201AFall2022.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **23.1 Comments on the Coefficient Interpretation in Last Class’s Regression Model**

In the last class, we studied a regression model for _y_ = log(Earnings) in terms of _x_ = Years of Experience. The interpretation I described for the coefficient parameters in that model was incorrect. The correct interpretation is given below. The simplest model for _y_ in terms of _x_ is the linear model which corresponds to the equation (without the error term):


The interpretation of _β_ 0 and _β_ 1 in this model are very clear. _β_ 0 is the simply the value of _y_ = log(Earnings) when _x_ = 0 (i.e., for someone just joining the workforce). To obtain the interpretation for _β_ 1, first plug in _x_ = 1 in (114) and then _x_ = 0 and subtract the second equation from the first. This gives


HEre _E_ 0 and _E_ 1 are Earnings for _x_ = 0 and _x_ = 1 respectively, and in the last equality, we used log( _u_ ) _≈ u −_ 1 for _u ≈_ 1. Thus 100 _β_ 1 represents the increment (in percent) in salary from year 0 to year 1. For example, _β_ 1 = 0 _._ 05 means that the salary increases by 5% from year 0 to year 1.

Now let us consider the model


Here the interpretation of _β_ 0 and _β_ 1 are exactly the same as for the model (114). _β_ 0 again represents log(Earnings) for _x_ = 0 and _β_ 1 represents the increment (in percent) from year 0

118

to year 1. What is the interpretation for _β_ 2? It is easy to see that:


Thus


Thus 100 _β_ 2 represents the change in the percent increment between years 1 and 2 compared to the percent increment between years 0 and 1. For example, _β_ 2 = 0 _._ 0003 means that the percent increment decreases by 0 _._ 03 after year 2. If _β_ 1 = 0 _._ 05, we would have a 5% increment after year 1 and a 5 _−_ 0 _._ 03 = 4 _._ 97% increment after year 2.

Now consider the model that we actually used last time:


Here the interpretation for _β_ 0 _, β_ 1 _, β_ 2 are just the same as in Model (115). More generally, the interpretation for _βj, j ≥_ 2 is as follows: 100 _βj_ is the change in the percent increment between years _j −_ 1 and _j_ compared to the percent increment between years _j −_ 2 and _j −_ 1. For a concrete example, suppose


then

1. weekly earnings for someone just joining the workforce is exp(5 _._ 74) = $311 _._ 06,

2. increment after year 1 is 5%,

3. increment after year 2 is (5 _−_ 0 _._ 03) = 4 _._ 97%,

4. increment after year 3 is (4 _._ 97 _−_ 0 _._ 08) = 4 _._ 89%,

5. increment after year 4 is (4 _._ 89 _−_ 0 _._ 1) = 4 _._ 79%, and so on.

If all _βj, j ≥_ 2 are negative, then, after a while, the increments may become negative which means that the salary actually starts decreasing after a certain number of years of experience.

It should be clear from the above that _β_ 0, _β_ 1 and _βj, j ≥_ 2 are different kinds of parameters (they have different units for instance). In particular, we would expect _βj, j ≥_ 2 to be quite small. In the last class, we analyzed model (116) with the prior


for a parameter _τ >_ 0 (and large _C_ ). This analysis seems to treat _β_ 1 as well as _βj, j ≥_ 2 in the same way. A better prior would be:


### **23.2 Comments on Regularization**

Parameter estimation for the model (116) using the prior (117) is an example of regularization. Regularization is one of the most important ideas in statistics and machine learning in the past 30 years. The reason for regularization is that, in models with lots of parameters such as (116), standard (unregularized) estimation procedures give nonsensical answers. For

119

example, for the model (116) applied to 500 randomly selected observations from the full `ex1029` dataset from the R package `Sleuth3` , the usual least squares estimates are given by


The interpretation would then become

1. weekly earnings for someone just joining the workforce is exp(5 _._ 55) = $257 _._ 24,

2. increment after year 1 is 4 _._ 5%,

3. increment after year 2 is (4 _._ 5 + 31 _._ 2) = 35 _._ 7%,

4. increment after year 3 is (35 _._ 7 _−_ 43 _._ 1) = _−_ 7 _._ 4%,

5. increment after year 4 is ( _−_ 7 _._ 4 + 29 _._ 9) = 22 _._ 5%, and so on.

These increments fluctuate wildly so as to make these numbers nonsensical. This is the reason why one regularizes while dealing with many parameters. In the context of the model (116), regularization is done in the following ways:

1. **The common approach** : The common approach estimates _β_ 0 _, . . . , βm_ (here _m_ = 64) by minimizing the least squares criterion plus a penalty term which encourages _β_ 2 _, . . . , βm_ to be small. One way of doing this is via the minimization of


for a suitable tuning parameter _λ_ . When _λ_ is large, the minimizer of the above criterion will have _βj,_ 2 _≤ j ≤ m_ small. But if _λ_ is too large, then _βj,_ 2 _≤ j ≤ m_ will be very close to zero. On the other hand, if _λ_ is too small, then _βj,_ 2 _≤ j ≤ m_ will be close to the least squares estimates. The choice of _λ_ is obviously quite crucial. For this, one uses the idea that “Regularized estimates often lead to better predictions”. To use this idea in practice for selecting _λ_ , the original dataset is divided into two subsets: training and test datasets. One would fit a regularized model to the training dataset by minimizing the above criterion for each value of _λ_ . The value of _λ_ which minimizes average prediction error on the test dataset would then be selected. This is the basic idea underlying methods such as cross-validation. This approach is quite common although there are some issues such as: (a) there are no principled approaches for doing the training-test splits, and often different splits lead to different answers, and (b) the value of _λ_ leading to best predictions on the test dataset might lead to estimates of _βj_ ’s that still fluctuate quite a bit (although not as much as the unpenalized least squares estimates).

2. **The Probability/Bayesian approach** : This is the approach that we discussed in the last lecture. The starting point is the observation that the usual least squares estimate can be seen as Bayesian estimates corresponding to the prior:


for a large _C_ . To achieve regularization, one changes the above model to


where _τ >_ 0 is an unknown parameter. The modeling assumption (119) is more flexible than (118). Indeed, (119) includes (118) as a special case when _τ_ = _√C_ . Using the

120

prior assumption (119), one can calculate the (marginal) likelihood of _σ_ and _τ_ by integrating the conditional density of the data given _β_ with respect to the prior (119):


The best value of _τ_ would then be obtained by maximizing this integrated likelihood over _τ_ and _σ_ .

These two methods for performing regularization are actually quite different. There is no training-test split in the Bayesian approach. On the other hand, there is no such thing as integrated or marginal likelihood in the common approach. For a comparative discussion on the benefits of the Bayesian approach, see `http://www.inference.org.uk/mackay/Bayes_ FAQ.html#cv` .

If you want to read more into the Bayesian approach for high-dimensional models, I strongly recommend the 1992 paper titled _Bayesian Interpolation_ by David MacKay (MacKay gives a short summary of this paper in this blog post: `https://statmodeling.stat. columbia.edu/2011/12/04/david-mackay-and-occams-razor/` ).

---

[← 22 Lecture Twenty Two](23-22-lecture-twenty-two.md) · [Up: contents](index.md) · [24 Lecture Twenty Four →](25-24-lecture-twenty-four.md)
