---
title: Contents
source: https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf
source_file: sources/berkeley-guntuboyina-notes/FullLectureNotes201AFall2019.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Contents

**Source:** [`FullLectureNotes201AFall2019.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullLectureNotes201AFall2019.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|**1**<br>**Rev**|**iew of**|**Undergraduate Probability**|**9**|
|---|---|---|---|
|1.1|Samp|le spaces, Events, Probability . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>9|
|1.2|Condi|tional Probability and Independence of Events . . . . . . . . . .|. . . . . . . . . .<br>10|
|1.3|Bayes|Rule<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>11|
|1.4|Rand|om Variables<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>14|
|1.5|Expec|tations of Random Variables . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>15|
|1.6|Varia|nce . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>17|
|1.7|Indep|endence of Random Variables . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>18|
|1.8|Comm|on Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>19|
||1.8.1|Bernoulli _Ber_(_p_) Distribution . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>19|
||1.8.2|Binomial _Bin_(_n, p_) Distribution<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>19|
||1.8.3|Poisson Distribution . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>20|
||1.8.4|Geometric Distribution<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>22|
||1.8.5|Negative Binomial Distribution . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>23|
|1.9|Conti|nuous Distributions<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>23|
||1.9.1|Normal or Gaussian Distribution . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>24|
||1.9.2|Uniform Distribution . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>24|
||1.9.3|The Exponential Distribution . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>24|


3

_CONTENTS_

|4|_CONTENTS_|
|---|---|
||1.9.4<br>The Gamma Density . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
|1.10|Variable Transformations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>26|
|1.11|Quantiles and The Quantile Transform . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
|1.12|Joint Densities<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>30|
|1.13|Joint Densities under Transformations . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>31|
||1.13.1 Detour to Convolutions<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>32|
|1.14|Joint Densities under transformations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>33|
||1.14.1 Linear Transformations<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>34|
||1.14.2 Invertible Linear Transformations . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>34|
||1.14.3 General Invertible Transformations . . . . . . . . . . . . . . . . . . . . . . . . . .<br>36|
|1.15|Joint Densities under general invertible transformations<br>. . . . . . . . . . . . . . . . . .<br>37|
|1.16|Joint Densities under Non-Invertible Transformations<br>. . . . . . . . . . . . . . . . . . .<br>39|
|1.17|Joint Density of Order Statistics<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>40|
|1.18|More on Order Statistics: The density of _X_(_i_) for a fixed _i_ . . . . . . . . . . . . . . . . .<br>41|
||1.18.1 Method One<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>42|
||1.18.2 Method Two<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>42|
||1.18.3 Method Three<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>43|
|1.19|Order Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>43|
||1.19.1 Uniform Order Statistics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>44|
||1.19.2 Maximum of Independent Uniforms<br>. . . . . . . . . . . . . . . . . . . . . . . . .<br>44|
||1.19.3 Minimum of Independent Exponentials . . . . . . . . . . . . . . . . . . . . . . . .<br>45|
||1.19.4 Minimum of Independent Non-Identically Distributed Exponentials . . . . . . . .<br>45|
||1.19.5 Minimum of Independent Non-identically distributed Geometrics . . . . . . . . .<br>45|
|1.20|Covariance, Correlation and Regression<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>46|
|**2**<br>**Con**|**ditioning**<br>**49**|


|_CONTE_|_NTS_|5|
|---|---|---|
||2.0.1<br>Basics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|49|
||2.0.2<br>Conditional Distributions, Law of Total Probability and Bayes Rule for Discrete<br>Random Variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|50|
|2.1|Conditional Densities for Continuous Random Variables . . . . . . . . . . . . . . . . . .|52|
|2.2|Conditional Densities for Continuous Random Variables . . . . . . . . . . . . . . . . . .|54|
|2.3|Conditional Density is Proportional to Joint Density . . . . . . . . . . . . . . . . . . . .|56|
|2.4|Conditional Densities and Independence . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|2.5|Law of Total Probability for Continuous Random Variables . . . . . . . . . . . . . . . .|58|
|2.6|Bayes Rule for Continuous Random Variables . . . . . . . . . . . . . . . . . . . . . . . .|60|
|2.7|LTP and Bayes Rule for general random variables<br>. . . . . . . . . . . . . . . . . . . . .|62|
||2.7.1<br>_X_ and Θ are both discrete<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|62|
||2.7.2<br>_X_ and Θ are both continuous . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|62|
||2.7.3<br>_X_ is discrete while Θ is continuous . . . . . . . . . . . . . . . . . . . . . . . . . .|62|
||2.7.4<br>_X_ is continuous while Θ is discrete . . . . . . . . . . . . . . . . . . . . . . . . . .|62|
|2.8|Conditional Joint Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|64|
|2.9|Conditional Joint Densities<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|67|
||2.9.1<br>Application to the Normal prior-Normal data model . . . . . . . . . . . . . . . .|68|
|2.10|Conditional Expectation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|70|
||2.10.1 Law of Iterated/Total Expectation . . . . . . . . . . . . . . . . . . . . . . . . . .|70|
|2.11|Law of Iterated/Total Expectation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|72|
||2.11.1 Application of the Law of Total Expectation to Statistical Risk Minimization . .|73|
|2.12|Conditional Variance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|76|
|**3**<br>**The**|**Central Limit Theorem**|**79**|
|3.1|Convergence in Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|81|
|3.2|Moment Generating Functions<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|83|


|6|_CONTENTS_|
|---|---|
|3.3|Proof of the CLT using MGFs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>85|
|3.4|Two Remarks on the CLT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>86|
|3.5|Convergence in Distribution and Convergence in Probability . . . . . . . . . . . . . . . .<br>87|
|3.6|Examples of Convergence in Probability . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>89|
||3.6.1<br>The Weak Law of Large Numbers<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>89|
||3.6.2<br>A sufficient condition for convergence in probability in terms of mean and variance 89|
||3.6.3<br>Consistency and examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>90|
|3.7|Slutsky’s Theorem, Continuous Mapping Theorem and Applications<br>. . . . . . . . . . .<br>91|
|3.8|Delta Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>95|
|3.9|Application of the Delta Method to Variance Stabilizing Transformations<br>. . . . . . . .<br>97|
||3.9.1<br>Motivating Variance Stabilizing Transformations . . . . . . . . . . . . . . . . . .<br>97|
||3.9.2<br>Construction of the Variance Stabilizing Transformation . . . . . . . . . . . . . .<br>97|
||3.9.3<br>Back to the Bernoulli Example . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>98|
||3.9.4<br>Back to the Poisson Example . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>99|
||3.9.5<br>Chi-squared Example<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100|
||3.9.6<br>Geometric Example<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100|
|3.10|Delta Method when _g_<sup>_′_</sup>(_θ_) = 0 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101|
|**4**<br>**Sec**|**ond Order Theory of Random Vectors**<br>**103**|
|4.1|Random Vectors<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103|
|4.2|Detour – Spectral Theorem for Symmetric Matrices<br>. . . . . . . . . . . . . . . . . . . . 104|
||4.2.1<br>Orthonormal Basis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105|
||4.2.2<br>Spectral Theorem<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106|
||4.2.3<br>Three Applications of the Spectral Theorem . . . . . . . . . . . . . . . . . . . . . 107|
|4.3<br>4.4|Best Linear Predictor<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109<br>Residual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112|


|_CONTE_|_NTS_|7|
|---|---|---|
|4.5|Detour: Schur Complements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 112|
|4.6|Partial Correlation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 113|
|4.7|Partial Correlation and Inverse Covariance . . . . . . . . . . . . . . . . . . . . . .|. . . . 115|
|4.8|Partial Correlation and Best Linear Predictor . . . . . . . . . . . . . . . . . . . .|. . . . 117|
|4.9|BLP when _Y_ is a random vector<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 119|
|**5**<br>**The**|**Multivariate Normal Distribution**|**121**|
|5.1|Moment Generating Functions of Random Vectors<br>. . . . . . . . . . . . . . . . .|. . . . 121|
|5.2|The Multivariate Normal Distribution . . . . . . . . . . . . . . . . . . . . . . . .|. . . . 122|
||5.2.1<br>Moment Generating Function of a Multivariate Normal<br>. . . . . . . . . .|. . . . 122|
||5.2.2<br>Connection to i.i.d _N_(0_,_1) random variables<br>. . . . . . . . . . . . . . . .|. . . . 123|
|5.3|Joint Density of the Multivariate Normal Distribution . . . . . . . . . . . . . . .|. . . . 123|
|5.4|Properties of Multivariate Normal Random Variables . . . . . . . . . . . . . . . .|. . . . 124|
|5.5|Idempotent Matrices and Chi-Squared distributions<br>. . . . . . . . . . . . . . . .|. . . . 125|
|5.6|Additional Remarks on Multivariate Normals and Chi-Squared Distributions<br>. .|. . . . 129|
|5.7|Conditional Distributions of Multivariate Normals<br>. . . . . . . . . . . . . . . . .|. . . . 131|


8 _CONTENTS_

## **Chapter 1**

---

[Up: contents](index.md) · [Review of Undergraduate Probability →](02-review-of-undergraduate-probability.md)
