---
title: Contents
source: https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf
source_file: sources/berkeley-guntuboyina-notes/FullNotes248Spring2022TimeSeries.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Contents

**Source:** [`FullNotes248Spring2022TimeSeries.pdf`](https://www.stat.berkeley.edu/~aditya/resources/FullNotes248Spring2022TimeSeries.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

|**1**|**Lec**|**ture One**<br>**4**|
|---|---|---|
||1.1|State Space Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>4|
||1.2|Examples of State Space Models<br>. . . . . . . . . . . . . . . . . . . . . . . . .<br>5|
|||1.2.1<br>Direct Examples: Tracking<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>5|
|||1.2.2<br>Trend Estimation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>6|
||1.3|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .<br>7|
|**2**|**Lec**|**ture Two**<br>**7**|
||2.1|Local Level and Local Linear Models . . . . . . . . . . . . . . . . . . . . . . .<br>8|
||2.2|Stochastic Volatility Models . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>9|
||2.3|Dynamic Regression Model<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>9|
||2.4|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .<br>10|
|**3**|**Lec**|**ture Three**<br>**10**|
||3.1|Connection to the Periodogram . . . . . . . . . . . . . . . . . . . . . . . . . .<br>13|
||3.2|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .<br>16|
|**4**|**Lec**|**ture Four**<br>**17**|
||4.1|The Autoregressive Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>19|
||4.2|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .<br>21|
|**5**|**Lec**|**ture Five**<br>**21**|
||5.1|Outline of Approach to Calculate Smoothing Distributions . . . . . . . . . . .<br>22|
||5.2|Linear Gaussian State Space Models . . . . . . . . . . . . . . . . . . . . . . .<br>23|
||5.3|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .<br>23|
|**6**|**Lec**|**ture Six**<br>**24**|
||6.1|General Approach for calculating Filtering Distributions . . . . . . . . . . . .<br>24|
||6.2|The Kalman Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
||6.3|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .<br>27|
|**7**|**Lec**|**ture Seven**<br>**28**|
||7.1|The Kalman Filter . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
||7.2|Some Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
|||7.2.1<br>Tracking One: Velocity Model<br>. . . . . . . . . . . . . . . . . . . . . .<br>29|


1

||7.2.2<br>Tracking Two: Acceleration Model . . . . . . . . . . . . . . . . . . . .<br><br>|29<br>|
|---|---|---|
||7.2.3<br>Tracking Three: Local Linear Model . . . . . . . . . . . . . . . . . . .|31|
|7.3|Use of the Kalman Filter for Parameter Estimation by Maximum Likelihood|31|
|7.4|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .|32|
|**8**<br>**Lect**|**ure Eight**|**32**|
|8.1|Some remarks on the local level model . . . . . . . . . . . . . . . . . . . . . .|32|
|8.2|Application of the Kalman Filter to Linear Regression . . . . . . . . . . . . .|35|
|8.3|Prediction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|8.4|Smoothing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|36|
|8.5|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .|37|
|**9**<br>**Lect**|**ure Nine**|**37**|
|9.1|Smoothing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|37|
|9.2|Backward Recursion for General State Space Models . . . . . . . . . . . . . .|37|
|9.3|Smoothing for Linear Gaussian State Space Models . . . . . . . . . . . . . . .|38|
|9.4|Dealing with missing data in the context of state space models<br>. . . . . . . .|41|
|9.5|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .|41|
|**10 Lect**|**ure Ten**|**42**|
|10.1|Summary: General Filtering and Smoothing . . . . . . . . . . . . . . . . . . .|42|
|10.2|Summary: Kalman Filtering and Smoothing . . . . . . . . . . . . . . . . . . .|43|
|10.3|Special Case: Local Level Model<br>. . . . . . . . . . . . . . . . . . . . . . . . .|44|
|10.4|Numerical Evaluation of _Xs | Y_0 =_y_0_, . . . , Yt_ =_yt, θ_ . . . . . . . . . . . . . . .|45|
|10.5|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .|46|
|**11 Lect**|**ure Eleven**|**46**|
|11.1|Basic Optimization Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . .|46|
||11.1.1 Gradient Ascent<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|46|
||11.1.2 Newton’s Method . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|47|
||11.1.3 Quasi-Newton Method: BFGS<br>. . . . . . . . . . . . . . . . . . . . . .|47|
|11.2|Application to Maximum Likelihood Estimation in State Space Models . . . .|49|
||11.2.1 Fisher Identity for the Score . . . . . . . . . . . . . . . . . . . . . . . .<br>|49|
||11.2.2 _E_(_θ, θ_<sup>(0)</sup>) for state space models<br>. . . . . . . . . . . . . . . . . . . . .|51|
|11.3|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .|52|
|**12 Lect**|**ure Twelve**|**52**|
|12.1|Pairwise Smoothing Distributions . . . . . . . . . . . . . . . . . . . . . . . . .|52|
|12.2|Fisher’s Identity (from last time) . . . . . . . . . . . . . . . . . . . . . . . . .|53|
|12.3|The Score Function for the Local Level Model . . . . . . . . . . . . . . . . . .|53|
|12.4|The EM Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|55|
|12.5|EM for the local level model . . . . . . . . . . . . . . . . . . . . . . . . . . . .|55|
|12.6|Calculation of _E_(_θ, θ_<sup>(0)</sup>) for general state space models . . . . . . . . . . . . .|56|
|12.7|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|**13 Lect**|**ure Thirteen**|**57**|
|13.1|The MM Algorithm<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|57|
|13.2|The EM Algorithm as a special case of MM . . . . . . . . . . . . . . . . . . .|59|
||13.2.1 The Kullback-Leibler Divergence . . . . . . . . . . . . . . . . . . . . .|59|
||13.2.2 EM and MM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|60|
|13.3|Full Smoothing Distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . .|60|
|13.4|Forward Filtering Backward SAMPLING<br>. . . . . . . . . . . . . . . . . . . .|61|
|13.5|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . . . . . .|62|


2

|**14 Lect**<br>|**ure Fourteen**<br>|**63**|
|---|---|---|
|14.1|Local Level Model<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>63|
|14.2|Gibbs Sampler<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>64|
|14.3|Gibbs Sampler for the Local Level Model<br>. . . . . . . . . . . . . . . .|. . . .<br>64|
|14.4|Gibbs sampler for general Linear Gaussian state space models . . . . .|. . . .<br>66|
|14.5|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . .|. . . .<br>66|
|**15 Lect**|**ure Fifteen**|**66**|
|15.1|Approach One: Gibbs Sampling . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>67|
|15.2|Approach Two: Direct Sampling<br>. . . . . . . . . . . . . . . . . . . . .|. . . .<br>67|
|15.3|Approach Three: Posterior Normal Approximation . . . . . . . . . . .|. . . .<br>68|
|15.4|Approach Four: Importance Sampling . . . . . . . . . . . . . . . . . .|. . . .<br>69|
|15.5|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . .|. . . .<br>72|
|**16 Lect**|**ure Sixteen**|**72**|
|16.1|Notation for Discrete Distributions . . . . . . . . . . . . . . . . . . . .|. . . .<br>73|
|16.2|Monte Carlo versions of (99) and (100) . . . . . . . . . . . . . . . . . .|. . . .<br>74|
|16.3|<br> The Bootstrap Particle Filter . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>75|
|16.4|Importance Sampling Recalled<br>. . . . . . . . . . . . . . . . . . . . . .|. . . .<br>76|
|16.5|Bootstrap Particle Filter as Importance Resampling<br>. . . . . . . . . .|. . . .<br>77|
||16.5.1 First Way of Seeing the Connection<br>. . . . . . . . . . . . . . .|. . . .<br>77|
||16.5.2 Second Way of Seeing the Connection . . . . . . . . . . . . . .|. . . .<br>78|
|16.6|Likelihood Approximation from the Bootstrap Particle Filter<br>. . . . .|. . . .<br>78|
|16.7|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . .|. . . .<br>79|
|**17 Lect**|**ure Seventeen**|**79**|
|17.1|Recap: Bootstrap Particle Filter<br>. . . . . . . . . . . . . . . . . . . . .|. . . .<br>79|
|17.2|Unique Values and Particle Degeneracy<br>. . . . . . . . . . . . . . . . .|. . . .<br>80|
|17.3|The Guided Particle Filter Algorithm<br>. . . . . . . . . . . . . . . . . .|. . . .<br>81|
|17.4|Weights when _qt_(_u | x, y, θ_) :=_fX|X_=_xY_=_θ_(_u_)<br>. . . . . . . . . . .|. . . .<br>83|
|17.5|_tt−_1_,ty,_<br> Example: Local Level Model<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>83|
|17.6|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . .|. . . .<br>84|
|**18 Lect**|**ure Eighteen**|**84**|
|18.1|Sequential Importance Resampling . . . . . . . . . . . . . . . . . . . .|. . . .<br>84|
|18.2|Example: Local Level Model with non-Gaussian evolution errors<br>. . .|. . . .<br>85|
|18.3|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . .|. . . .<br>88|
|**19 Lect**|**ure Nineteen**|**89**|
|19.1|Complete Smoothing . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>89|
|19.2|FFBS<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>91|
|19.3|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . .|. . . .<br>93|
|**20 Lect**|**ure Twenty**|**94**|
|20.1|Recap: Complete Smoothing<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>94|
|20.2|Complete Smoothing with partial trajectory resampling . . . . . . . .|. . . .<br>94|
|20.3|Recap: FFBS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>95|
|20.4|Recommended Reading for Today . . . . . . . . . . . . . . . . . . . . .|. . . .<br>96|
|**21 Lect**|**ure Twenty One**|**96**|
|21.1|Model Selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . .<br>96|
|21.2|Akaike Information Criterion (AIC)<br>. . . . . . . . . . . . . . . . . . .|. . . .<br>96|
||21.2.1 The simple case of no parameters . . . . . . . . . . . . . . . . .|. . . .<br>97|


3

|21.2.2 Models with parameters . . . . . . . . . . . . . . . . . .|. . . . . . . .<br>98|
|---|---|
|21.2.3 Digression: MLE asymptotic distribution<br>. . . . . . . .|. . . . . . . .<br>98|
|21.3 Back to AIC<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 104|
|21.4 Recommended Reading for Today . . . . . . . . . . . . . . . . .|. . . . . . . . 105|
|**22 Lecture Twenty Two**|**106**|
|22.1 Recap: AIC . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 106|
|22.2 Bayesian Model Selection<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 107|
|22.3 Two Alternative Expressions for the Evidence . . . . . . . . . .|. . . . . . . . 110|
|22.4 The BIC . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 111|
|22.5 Recommended Reading for Today . . . . . . . . . . . . . . . . .|. . . . . . . . 112|
|**23 Lecture Twenty Three**|**112**|
|23.1 Recap: Frequentist and Bayesian Model Selection . . . . . . . .|. . . . . . . . 112|
|23.2 Example: Normal Mean . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . 113|
|23.3 Application: Linear Regression . . . . . . . . . . . . . . . . . .|. . . . . . . . 114|
|23.4 Recommended Reading for Today . . . . . . . . . . . . . . . . .|. . . . . . . . 117|

---

[Up: contents](index.md) · [1 Lecture One →](02-1-lecture-one.md)
