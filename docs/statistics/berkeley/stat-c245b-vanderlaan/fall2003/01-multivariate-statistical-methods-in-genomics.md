---
title: Multivariate Statistical Methods in Genomics
source: https://vanderlaan-lab.org/teach-files/fall2003.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/fall2003.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Multivariate Statistical Methods in Genomics

**Source:** [`fall2003.pdf`](https://vanderlaan-lab.org/teach-files/fall2003.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

PH 243 A, MW 12-2, 2305 Tolman Instructor: Mark van der Laan Office: Haviland Hall 108, tel: 643-9866 website: www.stat.berkeley.edu/ laan Technical reports at www.bepress.com/ucbbiostat/ email: laan@stat.berkeley.edu

Page 1

General Topics Covered: 1) Resampling Based Multiple Testing 2) Clustering 3) Cross-validated Selection among Estimators 4) Cross-validated Selection with Censored Data 5) Algorithms for construction of Estimators

Subtopics: Classification and Regression, Regression on multivariate outcomes, Regression on censored outcomes (Prediction of survival), conditional density and hazard estimation.

Page 2

Applications in Genomics:

a) Detection of binding sites in gene expression experiments, b) Regression of single nucleotide polymorphisms (SNP’s), gene expressions, comparitive genome hybridization measurements, and epidemiologic variables, on clinical outcomes such as survival or time till recurrence,

c) Clustering protein structures, classifying or predicting protein structures, clustering genes/patients based on gene expression experiments

d) many others.

Page 3

**Resampling based Multiple Testing with Asymptotic Control of Type-I Error: Single Parameter Hypotheses and Single Step Procedures**

**Mark van der Laan** Division of Biostatistics, UC Berkeley `www.stat.berkeley.edu/~laan` www.bepress.com/ucbbiostat/

Multivariate Statistical Methods in Genomics PH 243A, 2305 Tolman, MW 12-2

Fall 2003 _⃝_ c Copyright 2003, all rights reserved

#### **DATA AND NULL HYPOTHESES**

**Data:** _X_ 1 _, . . . , Xn_ i.i.d. observations of a multidimensional vector _X ∼ P ∈M_ for a model _M_ .

- gene expression measurements

- gene expression, covariates, and outcomes ( _e.g._ : survival)

- SNPs, covariates, and an outcome ( _e.g._ : response to treatment)

- occurance of sequence motifs and gene expression.

**Parameters:** Real valued parameters _µj_ ( _P_ ), _j_ = 1 _, . . . , p_ .

Page 6

#### **Examples of Parameters:**

- location parameters (means, medians, differences in means)

- regression parameters (association between gene _j_ ’s expression and outcome)

- Survival probabilities.

**Null Hypotheses:**

_H_ 0 _,j_ : _µj_ ( _P_ ) = _µ_<sup>0</sup> _j_<sup>_,j_= 1</sup><sup>_, . . . , p,_</sup>

where _µ_<sup>0</sup> _j_<sup>arehypothesizednullvalues.</sup>

Page 7

#### **TEST STATISTICS**

Test _H_ 0 _,j, j_ = 1 _, . . . , p_ , with _Tjn_ defined by

_≡ Tjn µjn − µ_<sup>0</sup> _j µjn − µ_<sup>0</sup> _<u>j</u> ≡_ or _Tjn σ_ ˆ( _µjn_ )<sup>_._</sup>


Page 8

that as _n →∞ D Zn ≡_<sup>_√_</sup> _n_ ( _µn − µ_ ( _P_ )) _⇒ N_ (0 _,_ Σ( _P_ )) _,_ (2) where Σ( _P_ ) = _EP_ ( _IC_ ( _X | P_ ) _IC_ ( _X | P_ )<sup>_⊤_</sup> ) is the covariance of the vector **influence curve** _IC_ ( _X | P_ ) = _{ICj_ ( _X | P_ ) : _j_ = 1 _, . . . , p}_ of _µjn_ . Let _Z ∼ Q_ 0( _P_ ) _≡ N_ (0 _,_ Σ( _P_ )) (3) represent the limit (in distribution) of _Zn_ .

Page 9

#### **ERROR RATES**

Given a vector _c_ , consider a corresponding **multiple testing procedure** _MT_ ( _c_ ) defined by:

Reject _H_ 0 _,j_ , if _| Tjn |> cj_ , _j_ = 1 _, . . . , p_ , (4)

Let:

- _Vn_ ( _c_ ) =<sup>�</sup><sup>_p_</sup> _j_ =1<sup>_I_(</sup><sup>_| Tjn|> cj, µj_(</sup><sup>_P_) =</sup><sup>_µ_</sup> _j_<sup>0)bethenumberoffalse</sup> positives of _MT_ ( _c_ ),

- For a candidate cdf _F_ of _Vn_ , let _θ_ ( _F_ ) _∈_ (0 _,_ 1) measure a particular type-I-error rate satisfying 1) continuity in _F_ and 2) monotonicity in _F_ in the sense that _θ_ ( _F_ ) _≥ θ_ ( _G_ ) if _F ≤ G_ .

Page 10

**Examples of Error rates** _θ_ ( _FVn_ ) **:**

- � _xdFVn_ ( _x_ ) _/p_ = _E_ ( _Vn_ ) _/p_ : per-comparison error rate (PCER),

- _•_ � _xdFVn_ ( _x_ ) = _E_ ( _Vn_ ) : per-family error rate (PFER),

- _•_ 1 _− FVn_ (0) = _Pr_ ( _Vn ≥_ 1): family-wise error rate (FWER),

- 1 _− FVn_ ( _k_ ) = _Pr_ ( _Vn ≥ k_ ) : Generalized family wise error rate (gFWER).

Page 11

**SINGLE STEP CUT-OFF RULE and ERROR CONTROL**

Let _c_ = _c_ ( _Q, α_ ) denote a vector function cut-off rule such that if _Tn ∼ Q_ , then _MT_ ( _c_ ) has the property that _θ_ ( _FRn_ ( _c_ )) = _α_ , where _p Rn_ ( _c_ ) = _I_ ( _| Tjn |> cj_ ) _._ � _j_ =1

**A sensible cut-off rule:** set _cj_ equal to the 1- _δ_ -quantile of the _j_ -th marginal distribution of _Q_ , where _δ_ is fine-tuned to yield control at level _α_ .

So, _MT_ ( _c_ ) = _MT_ ( _c_ ( _Q, α_ )) depends critically on the choice of distribution _Q_ under which the error rate is controlled.

Page 12

We want to choose an estimated distribution _Qn_ so that _cn_ = _c_ ( _Qn, α_ ) satisfies lim sup _n→∞_<sup>_θ_(</sup><sup>_FVn_)</sup><sup>_≤α._</sup>

That is, for large enough sample size, the error rate _αn_ for a sample of size _n_ is bounded from above by the target error rate _α_ .

Page 13

#### **NULL DISTRIBUTIONS**

Let _Qn_ ( _P_ ) be the distribution of the test statistics under _X ∼ P_ . We seek to control the error rate under a **test statistic distribution** that satisfies the overal null hypotheses and is as close as possible to the true test statistic distribution _Qn_ ( _P_ ). Therefore, the correct null distribution is the **projection** of _Qn_ ( _P_ ) onto the space of mean zero distributions.

NOTE: Current approach is to choose a null data generating distribution _P_ 0 _∈M_ 0 = _{P_ : _µ_ ( _P_ ) = _µ_ 0 _}_ , and control error rate under _Qn_ ( _P_ 0).

Page 14

Let _P_ 0 = _P_ 0( _P_ ) _≡_ Π( _P | M_ 0) be a projection (e.g. Kullback-Leibler) of the true data generating distribution onto _M_ 0. Let _Q_ 0 _n_ = _Q_ 0 _n_ ( _P_ ) = Π( _Qn_ ( _P_ ) _| Q_ 0) be the projection of the test-statistic distribution _Qn_ ( _P_ ) onto the space of mean zero distributions. In general,

_n_ lim _→∞_<sup>_Q_0</sup><sup>_n_=</sup><sup>_N_(0</sup><sup>_,_Σ(</sup><sup>_P_))=</sup><sup>_̸_</sup> _n_<sup>lim</sup> _→∞_<sup>_Qn_(</sup><sup>_P_0) =</sup><sup>_N_(0</sup><sup>_,_Σ(</sup><sup>_P_0))</sup><sup>_._</sup>

Page 15


Page 16

**ESTIMATION:** Estimate _Q_ 0 with _Q_ 0 _n_ , _e.g._ :

- _Q_ 0 _n_ = _N_ (0 _,_ Σ _n_ ). Provides asymptotic control.

- Bootstrap method. Provides asymptotic control.

- _Qn_ ( _P_ 0 _n_ ), where _P_ 0 _n_ is an estimated data null distribution. Does **not** provide asymptotic control _unless_

Σ( _P_ 0) = Σ( _P_ ) _._ (6)

Condition (6) is the formal analogue of the **subset pivotality condition** (Westfall and Young, 1993, p.42-43).

Page 17

**BOOTSTRAP ESTIMATED NULL DISTRIBUTION**

Suppose _Tn_ =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _µn − µ_ 0). Let

- _P_<sup>˜</sup> _n_ be an estimator of _P_ according to model _M_ .

_• µ_ ˜ _n_ = _µ_ ( _P_<sup>˜</sup> _n_ ) be the parameter estimate under _P_<sup>˜</sup> _n • µ_<sup>#</sup> _n_<sup>be</sup><sup>_µn_appliedto</sup><sup>_n_i.i.d.copies</sup><sup>_X_</sup> 1<sup>#</sup><sup>_, . . . , X_</sup> _n_<sup>#of</sup><sup>_X_#</sup><sup>_∼P_˜</sup><sup>_n_</sup> _• Q_<sup>#</sup> 0 _n_<sup>bethedistributionof</sup><sup>_Z_</sup> _n_<sup>#=</sup><sup>_√_</sup> _<u>n</u>_ <u>(</u> _µ_<sup>#</sup> _n_<sup>_−µ_˜</sup><sup>_n_)</sup>

**Estimate** _Q_ 0 with _Q_<sup>#</sup> 0 _n_<sup>.Underweakregularityconditions,itis</sup> _D_ known that _Zn_<sup>#</sup> _⇒ Z ∼ Q_ 0 conditional on _P_<sup>˜</sup> _n_ , and hence _Q_ 0 _n_ consistently estimates _Q_ 0.

Page 18

#### **Define**

_p Rn_<sup>#(</sup><sup>_c_)</sup> _≡_ � _I_ ( _| Zjn_<sup>#</sup><sup>_|> cj_)</sup> _j_ =1 and let _cn_ = _c_ ( _Q_<sup>#</sup> 0 _n_<sup>_, α_):thatis,itsatisfies</sup><sup>_θ_</sup> _FR_ # = _α_ . Then, � _n_<sup>(</sup><sup>_c_)</sup> � _MT_ ( _cn_ ) is a **bootstrap based multiple testing procedure** asymptotically controlling _θ_ ( _FVn_ ) at level _α_ .

Page 19

#### **TWO SAMPLE PROBLEM**

Suppose we have _n_ 1 observations from Population 1 with mean _µ_ 1 and _n_ 2 observations from Population 2 with mean _µ_ 2.

**Null Hypotheses:** _H_ 0 _,j_ : _µj ≡ µ_ 2 _,j − µ_ 1 _,j_ = 0 _, j_ = 1 _, . . . , p_ .

#### **Test Statistics:**


<!-- Start of picture text -->
=<br>Djn X ¯2 ,j − X ¯1 ,j, j = 1 , . . . , p<br>X ¯2 ,j − X ¯1 ,j<br>=<br>or Tjn , j = 1 , . . . , p.<br>σ ˆ1 2 ,j /n 1 + ˆ σ 2 2 ,j /n 2<br>�<br><!-- End of picture text -->

Page 20

#### **COMPARISON OF NULL DISTRIBUTIONS**

Let _COV_ ( _Xj, Xj′_ ) be _φ_ 1 in population 1 and _φ_ 2 in population 2.

|Distribution|_V ar_(<br>|_Djn_)<br>|_Cov_(_Djn, Dj′n_)|
|---|---|---|---|
|Permutations|_σ_<sup>2</sup><br>1_,j_<br>|_σ_<sup>2</sup><br>2_,j_|_φ_1<br><sup>+</sup> <sup>_φ_2</sup>|
|Bootstrap|_n_2 <br>_σ_<sup>2</sup><br>1_,j_<br>_n_1|_n_1<br><sup>+</sup><br>_σ_<sup>2</sup><br>2_,j_<br>_n_2|_n_2  <br>_n_1<br>_φ_1<br>_n_1 <sup>+</sup> <sup>_φ_2</sup><br>_n_2|


#### <u>Note:</u>

- _V AR_ ( _Tjn_ ) = 1 for both distributions.

- But the two expressions for _COV_ ( _Tjn, Tj′n_ ) are not equivalent unless _n_ 1 = _n_ 2.

Page 21


Page 22

#### **The correlation example**

Suppose we observe _n_ i.i.d. observations _X_ 1 _, . . . , Xn_ of a vector _X_ = ( _X_ (1) _, X_ (2) _, X_ (3)). For the sake of illustrations, we will assume that the variables are standardized so that VAR( _X_ ( _j_ )) = 1, _j_ = 1 _,_ 2 _,_ 3, and suppose that we assume the parametric model _X ∼ N_ (0 _, ρ_ ), where _ρ_ is the correlation matrix of _X_ . Let _ρj_ , _j ∈ J ≡{_ (12) _,_ (13) _,_ (23) _}_ denote the three unknown correlations. Suppose we are concerned with testing _H_ 0 _,j_ : _ρj_ = 0, _j ∈ J_ . Let _ρjn_ , _j ∈ J_ , be the empirical correlations, and suppose that we use as test-statistics _Tnj_ =<sup>_√_</sup> _<u>nρjn</u>_ . Let _S_ 0 = _{j ∈ J_ : _ρj_ = 0 _}_ be the set of true nulls.

Let _Qn_ 1 = _Qn_ ( _P_ 0) be the null distribution of _Tn_ under the data generating distribution _P_ 0 = _N_ (0 _, I_ ), where _I_ denotes the identity matrix. Let _Qn_ 2 be the distribution of<sup>_√_</sup> _<u>n</u>_ <u>(</u> _ρn − ρ_ ). One wants to choose a null distribution which is such that the sub-distribution corresponding with the components in _S_ 0equals or approximates

Page 23

well the actual distribution of _Tnj, j ∈ S_ 0. It follows immediately that the sub-distribution of _Qn_ 2 corresponding with the components in _S_ 0 equals (by definition) the distribution of _Tnj, j ∈ S_ 0. Consequently, an estimate of the limit distribution of _Qn_ 1 as one obtains with either the nonparametric bootstrap, or model based bootstrap, or influence curve approach, consistently estimates the actual distribution of _Tnj_ , _j ∈ S_ 0. We will now show that the sub-distribution of _Qn_ 1 fails to do this. Firstly, if the components of _X_ are uncorrelated, then it follows immediately that the three empirical correlations are independent. Consequently, by the CLT it follows that _Qn_ ( _P_ 0) converges to a _N_ (0 _, I_ ). However, two empirical correlations corresponding with true nulls are not necessarily (asymptotically) uncorrelated. For example, suppose that _ρ_ 13 = _ρ_ 23 = 0, but _ρ_ 23 _̸_ = 0. Then it follows that _D √n_ ( _ρn_ 12 _, ρn_ 13) _⇒ N_ (0 _,_ Σ0) _,_

Page 24

where the 2 by 2 matrix Σ0 is 1 on the diagonal and _ρ_ 23 off-diagonal.

Page 25

#### **DATA ANALYSIS**

The publicly available data set of Alizadeh _et al._ (2000):

- Blood samples from _n_ = 40 **Diffuse Large B-Cell Lymphoma (DLBCL)** patients

- Expression of _p_ = 13 _,_ 412 clones (relative to a pooled control) measured with cDNA arrays

- Patients belong to two molecularly distinct disease groups:

   - _n_ 1 = 21 **Activated** with mean _µ_ 1

   - _n_ 2 = 19 **Germinal Center (GC)** with mean _µ_ 2

- Survival time _T_ measured on each patient

- Pre-processing:

   - log2

   - replace missing values with the mean for that gene

   - truncate ratios exceeding 20-fold to _±_ log2(20)

Page 26

#### **DIFFERENCE IN MEANS: METHOD**

- Null hypotheses: for _j_ = 1 _, . . . , p_

_H_ 0 _,j_ : _µj ≡ µ_ 2 _,j − µ_ 1 _,j_ = 0 _._

_<u>µjn−</u>_ 0 _X_ ¯2 _<u>,j</u> −X_<sup>¯</sup> 1 _<u>,j</u> •_ Test statistics: _Tjn_ = _sd_ ( _µjn_ )<sup>=</sup> _σ_ ˆ<sup>2</sup> _~~√~~_ 1 _,j_<sup>_/n_1+ˆ</sup><sup>_σ_</sup> 2<sup>2</sup> _,j_<sup>_/n_2</sup><sup>_._</sup>

- Control the usual FWER: _Pr_ ( _V ≥_ 1) = _α_ = 0 _._ 05

- Estimated null distributions and thresholds:

   1. Fine-tuned common quantiles with the non-parametric bootstrap distribution,

   2. Fine-tuned common quantiles with the permutation distribution,

   3. Bonferroni common _threshold_ with the tabled t-distribution.

Page 27

#### **DIFFERENCE IN MEANS: RESULTS**

Null Distribution Rejections Non-parametric bootstrap 186 Permutations 287 T-distribution 32

Number of rejected null hypotheses (out of _p_ = 13 _,_ 412) for three different choices of multiple testing procedure. All 32 of the genes in the t-distribution subset are in both the permutation and the bootstrap subset, and the bootstrap and permutation subsets have 156 genes in common.

Page 28

#### **LOGISTIC REGRESSION: METHOD**

_•_ Logistic Regression Model for each gene: _j_ = 1 _, . . . , p_


_•_ Null hypotheses: for _j_ = 1 _, . . . , p_


_•_ Test statistic:<sup>_√_</sup> _<u>n</u> ∗ β_ 1 _n_ .

- Control the gFWER _Pr_ ( _V ≥ k_ ) = _α_ = 0 _._ 05 for _k_ = 1 _, . . . ,_ 100.

- _•_ Fine-tuned common quantiles.

- Estimated null distributions: Nonparametric bootstrap.

- RESULTS

Page 29

_k_ = 1 10 50 100 200 Rejections 303 303 303 471 553

Table 1: Logistic Regression Parameters. Number of rejected null hypotheses (out of _p_ = 13 _,_ 412) using the non-parametric bootstrap estimated null distribution and controlling the gFWER _P_ ( _Vn > k_ ) for different choices of _k_ , where _Vn_ is the number of false positives. The test statistics used are<sup>_√_</sup> _<u>n</u> ∗_ ( _βn −_ 0).

Page 30

#### **LINEAR REGRESSION: METHOD**

- Accelerated failure time model for each gene: _j_ = 1 _, . . . , p E_ (log( _T_ ) _| Xj_ ) = _γ_ 0 _,j_ + _γ_ 1 _,j ∗ Xj_

- Use an Inverse Probability of Censoring Weighted (IPCW) estimator for _γ_ since survival is right-censored for some patients.

_•_ Null hypotheses: for _j_ = 1 _, . . . , p H_ 0 _,j_ : _γ_ 1 _,j_ = 0 _._

- Test statistic:<sup>_√_</sup> _<u>n</u> ∗ γ_ 1 _n_ .

- Control the gFWER _Pr_ ( _V ≥ k_ ) = _α_ = 0 _._ 05 for _k_ = 1 _, . . . ,_ 100.

- _•_ Fine-tuned common quantiles with the non-parametric bootstrap distribution.

_•_ Could do for each disease group (Activated and GC) separately

Page 31

and compare lists of significant genes.

- RESULTS soon...

Page 32

#### **SIMULTATIONS USING REAL DATA**

- Sample from the data set derived from Alizadeh _et al._ (2000)

- _• p_ = 100 random genes, centered to have mean zero in both groups.

Page 33

||Permutation|Non-parametric<br>Bootstrap|Parametric<br>Bootstrap|
|---|---|---|---|
|_n_1 =|5_, n_2 = 15|||
|_Dj_|0.21|0.025|0.085|
|_Tj_|0.020|0.025|0.020|
|_n_1 =|9_, n_2 = 11|||
|_Dj_|0.13|0.050|0.065|
|_Tj_|0.015|0.065|0.015|
|_n_1 =|10_, n_2 = 10|||
|_Dj_|0.17|0.060|0.070|
|_Tj_|0.020|0.055|0.035|


Estimates _α_ ˆ of the error rate _Pr_ ( _V >_ 10) over _I_ = 200 independent simulated data sets for null distributions of _Dj_ and _Tj_ . The target error rate is _α_ = 0 _._ 05.

Page 34

#### **CONCLUSIONS**

1. _Q_ 0 = _N_ (0 _,_ Σ( _P_ )) is the asymptotically correct null distribution for the test statistics<sup>_√_</sup> _<u>n</u>_ <u>(</u> _µn − µ_<sup>0</sup> ) and it provides asymptotic control of type I error rates that are a function of the distribution of the number of false positives.

2. For a finite sample, _Q_ 0 can be consistently estimated with the standard bootstrap.

3. Common practice of estimating _Q_ 0 via a data null distribution _P_ 0 only provides asymptotic control when Σ( _P_ 0) = Σ( _P_ ).

4. Multiple testing is equivalent with constructing an 0.95-error specific confidence region (e.g. using the bootstrap).

5. Two Sample Problem: Permutation data null distribution _P_ 0 _n_ has the wrong asymptotic covariance unless _n_ 1 = _n_ 2 or Σ1 = Σ2

Page 35

**Resampling based Multiple Testing with Asymptotic Control of Type-I Error: General Hypotheses, Single Step and Step-Down Procedures**

**Mark van der Laan** Division of Biostatistics, UC Berkeley `www.stat.berkeley.edu/~laan` www.bepress.com/ucbbiostat/ 0.75cm Multivariate Statistical Methods in Genomics PH 243A, 2305 Tolman, MW 12-2 Fall 2003

_⃝_ c Copyright 2003, all rights reserved

#### **Multiple hypothesis testing framework**

**Model.** Let _X_ 1 _, . . . , Xn_ be _n_ i.i.d. copies of a random variable _X ∼ P ∈M_ , where _P_ is known to be an element of a particular statistical model _M_ (possibly nonparametric). Let _Mj ⊂M_ be a collection of _m_ submodels and let _H_ 0 _j_ = _I_ ( _P ∈Mj_ ) be the corresponding set of null hypotheses, _j_ = 1 _, . . . , m_ . Thus, _H_ 0 _j_ is true if _P ∈Mj_ and false otherwise.

Let _S_ 0 = _S_ 0( _P_ ) _≡{j_ : _H_ 0 _j_ is true _}_ = _{j_ : _P ∈Mj}_ be the set of _m_ 0 = _|S_ 0 _|_ true null hypotheses, where we note that _S_ 0 depends on the true data generating distribution _P_ . Let _S_ 0<sup>_c_=</sup><sup>_S_</sup> 0<sup>_c_(</sup><sup>_P_)</sup><sup>_≡{j_:</sup><sup>_j̸∈S_0</sup><sup>_}_bethesetof</sup><sup>_m_1=</sup><sup>_m −m_0falsenull</sup> hypotheses, i.e., true positives.

**Example:** _H_ 0 _j_ : _µ_ ( _j_ ) _≤ µ_ 0( _j_ ), where the _µ_ ( _j_ ) = _µ_ ( _j | P_ ) are real-valued parameters

Page 38

**Type I error rates.** Decision to reject or not the null hypotheses are based on test statistics _Tn_ ( _j_ ), _j_ = 1 _, . . . , m_ , where we assume that large values of _Tn_ ( _j_ ) provide evidence against the null hypothesis _H_ 0 _j_ . Let _Tn_ = ( _Tn_ ( _j_ ) : _j_ = 1 _, . . . , m_ ) be the corresponding _m_ -vector of test statistics, with joint distribution _Qn_ = _Qn_ ( _P_ ). The end-product of single-step or stepwise multiple hypothesis testing procedures is a set, _Sn_ = _S_ ( _X_ 1 _, . . . , Xn_ ; _Q_ 0 _, α_ ) _⊆{_ 1 _, . . . , m}_ , of rejected hypotheses, i.e., of null hypotheses believed to be false.

Page 39

_S_ ( _X_ 1 _, . . . , Xn_ ; _Q_ 0 _, α_ ), the set _Sn_ depends on the data, _X_ 1 _, . . . , Xn_ , the choice of null distribution _Q_ 0 for computing cut-offs for the test statistics or _p_ -values, and on _α_ , the nominal level of the test). Two types of errors can be committed: a false positive, or _Type I error_ , is committed by rejecting a true null hypothesis, and a false negative, or _Type II error_ , is committed when the test fails to reject a false null hypothesis.

The situation can be summarized by the table below, where the number of Type I errors is _Vn_ = _|Sn ∩ S_ 0 _|_ and the number of Type II errors is _Un_ = _|Sn_<sup>_C∩S_</sup> 0<sup>_C|_.Notethatboth</sup><sup>_Un_and</sup><sup>_Vn_dependon</sup> the unknown data generating distribution _P_ through _S_ 0 = _S_ 0( _P_ ). The numbers _m_ 0 = _|S_ 0 _|_ and _m_ 1 = _m − m_ 0 of true and false null hypotheses are unknown parameters, the number of rejected hypotheses _Rn_ = _|Sn|_ is an observable random variable, and _m_ 1 _− Un_ , _Un_ , _m_ 0 _− Vn_ , and _Vn_ are unobservable random variables (depending on _P_ , through _S_ 0( _P_ )).

Page 40

Table 2: Type I and Type II errors in multiple hypothesis testing.


<!-- Start of picture text -->
Null hypotheses<br>not rejected rejected<br>true m 0  − Vn Vn (Type I) m 0<br>Null hypotheses<br>false Un (Type II) m 1  − Un m 1<br>m<br>m − Rn Rn<br><!-- End of picture text -->

Page 41

#### **Type-I Error Rate**

In general, we make the following assumptions for the parameter _θ_ ( _FVn_ ) defining a particular Type I error rate. Given the distance measure _d_ ( _F_ 1 _, F_ 2) = max _x∈{_ 0 _,...,m} | F_ 1( _x_ ) _− F_ 2( _x_ ) _|_ for two cumulative distribution functions _F_ 1 and _F_ 2 on _{_ 0 _, . . . , m}_ , we assume that the parameter _θ_ ( _F_ ) satisfies the following properties, where _F_ represents a c.d.f. on _{_ 0 _, . . . , m}_ for _Vn_ . _Monotonicity._ If _F_ 1 _≥ F_ 2, then _θ_ ( _F_ 1) _≤ θ_ ( _F_ 2) _._ (8) _Uniform Continuity._ If _d_ ( _Fn, Gn_ ) _→_ 0, then _θ_ ( _Fn_ ) _− θ_ ( _Gn_ ) _→_ 0 _,_ (9)

Page 42


<!-- Start of picture text -->
or equivalently,<br>sup | θ ( F )  − θ ( G )  |→ 0<br>{ ( F,G ): d ( F,G ) ≤δn}<br>if δn → 0.<br><!-- End of picture text -->

Page 43

#### **Adjusted** _p_ **-values**

As in the single hypothesis setting, multiple testing procedures may be described in terms of _p_ -values. Given any multiple testing procedure, the _adjusted p-value_ corresponding to the test of a single hypothesis _H_ 0 _j_ can be defined as the nominal level of the entire procedure at which _H_ 0 _j_ would just be rejected, given the values of all test statistics involved. In terms of our previous notation, the adjusted _p_ -value for hypothesis _H_ 0 _j_ , given a multiple testing procedure _Sn_ = _S_ ( _X_ 1 _, . . . , Xn_ ; _Q_ 0 _, α_ ), is

_p_ ˜ _n_ ( _j_ ) = inf _{α ∈_ [0 _,_ 1] : _j ∈ S_ ( _X_ 1 _, . . . , Xn_ ; _Q_ 0 _, α_ ) _} ,_ (10)

where the _nominal_ Type I error rate is the _α_ -level at which the specified procedure is performed. Hypothesis _H_ 0 _j_ is then rejected at nominal Type I error rate _α_ if _p_ ˜ _n_ ( _j_ ) _≤ α_ . This definition of adjusted _p_ -values applies to procedures controlling any type of error rate, e.g., gFWER, PCER, FDR.

Page 44

As in the single hypothesis case, an advantage of reporting adjusted _p_ -values, as opposed to only rejection or not of the hypotheses, is that the level of the test does not need to be determined in advance, that is, results of the multiple testing procedure are provided for all _α_ .

Page 45

#### **Single Step Multiple Testing Procedure**

A hypothesis _H_ 0 _j_ is rejected if _Tn_ ( _j_ ) _> cj_ , for an _m_ -vector of cut-offs _c_ = ( _cj_ : _j_ = 1 _, . . . , m_ ). Denote the number of rejected hypotheses and Type I errors by


respectively, where the notation _R_ ( _c | Q_ ) and _V_ ( _c | Q_ ) acknowledges that the distribution of the above sums is defined by a distribution _Q_ for the test statistics _Tn_ .

Page 46

**Procedure 1. Single-step procedure — control of general Type I error rates** _θ_ ( _FVn_ ) **.** Given a null distribution _Q_ 0, define a vector of cut-offs _c_ ( _Q_ 0 _, δ_ ) = ( _cj_ ( _Q_ 0 _, δ_ ) : _j_ = 1 _, . . . , m_ ) for the test statistics _Tn_ , such that _cj_ ( _Q_ 0 _, δ_ ) is the (1 _− δ_ )–quantile of the marginal distribution _Q_ 0 _j_ , _j_ = 1 _, . . . , m_ . Let _δ_ be chosen as

_δ_ 0 = _δ_ 0( _α_ ) = max _{δ_ : _θ_ ( _FR_ ( _c_ ( _Q_ 0 _,δ_ ) _|Q_ 0)) _≤ α}._ (11)

Here _c_ ( _Q_ 0 _, δ_ 0( _α_ )) is referred to as the common-quantile cut-off rule for type-I-error _θ_ based on the null distribution _Q_ 0. The single-step multiple testing procedure for controlling the Type I error rate _θ_ ( _FVn_ ) at level _α_ is defined by Reject _H_ 0 _j_ if _Tn_ ( _j_ ) _> cj_ ( _Q_ 0 _, δ_ 0( _α_ )), _j_ = 1 _, . . . , m_ .

Page 47

Rather than simply reporting rejection or not of the hypotheses at a prespecified level _α_ , one can report adjusted _p_ -values for Procedure 1, computed under the null distribution _Q_ 0. The adjusted _p_ -value for hypothesis _H_ 0 _j_ is given by _P_ ˜ _n_ ( _j_ ) = _θ_ ( _FR_ ( _c_ ( _Q_ 0 _,δ_ 0 _j_ ) _|Q_ 0)) _,_ where _δ_ 0 _j_ = _Q_<sup>¯</sup> 0 _j_ ( _Tn_ ( _j_ )) (12) and _Q_<sup>¯</sup> 0 _j_ , _j_ = 1 _, . . . , m_ , denote the marginal survival functions corresponding to the null distribution _Q_ 0. The procedure for controlling the Type I error rate at level _α_ can then be stated equivalently as

Reject _H_ 0 _j_ if _P_<sup>˜</sup> _n_ ( _j_ ) _≤ α_ , _j_ = 1 _, . . . , m_ .

Page 48


Page 49

#### **Explicit Proposal for Null Distribution**

Suppose that there exists known _m_ -vectors _θ_ 0 _∈_ IR<sup>_m_</sup> and _τ_ 0 _∈_ IR<sup>_m_</sup> (null values), so that


Page 50

degenerate ( e.g., at _−∞_ ). Then, for this choice of null distribution _Q_ 0 and for all _c_ = ( _cj_ : _j_ = 1 _, . . . , m_ ) and _x_     lim inf _n→∞_<sup>_Pr_</sup> _I_ ( _Tn_ ( _j_ ) _> cj_ ) _≤ x I_ ( _Z_ ( _j_ ) _> cj_ ) _≤ x j∈S_ 0 _j∈S_ 0 <sup>�</sup>  _≥ PrQ_ 0 <sup>�</sup>  _,_

so that the previous Theorem applies. **Practical remark:** Given the null values _θ_ 0, _τ_ 0 for the mean and variance of the test-statistic distribution (when the null would be true), respectively, this explicit proposal for the null distribution corresponds with 1) simulate a large number _B_ of vectors _Tn_ from the actual true distribution _Qn_ ( _P_ ), 2) compute the marginal expectation _ETn_ and variance VAR( _Tn_ ), and 3) make the _m × B_ -matrix<sup>_√_</sup> _<u>ν</u>_ 0 _n_ <u>(</u> _Tn − ETn_ + _θ_ 0.

Page 51

#### **Step-down Procedures for FWE**

We propose two step-down multiple testing procedures, based on a null distribution _Q_ 0 = _Q_ 0( _P_ ) that provides asymptotic control of the family-wise error rate, without the requirement of subset pivotality. The first procedure involves maxima of the test statistics _Tn_ ( _j_ ) (maxT, Procedure 2) and the second is based on minima of _p_ -values _Pn_ ( _j_ ), also computed under the null _Q_ 0 (minP, Procedure 3).

Page 52

**Procedure 2. Step-down procedure based on maxima of test statistics (maxT) — control of FWER** Let _Tn,_ ( _j_ ) be the ordered test statistics, _Tn,_ (1) _≥ . . . ≥ Tn,_ ( _m_ ), and _Rn_ ( _j_ ) the indices for these order statistics, so that _Tn,_ ( _j_ ) = _Tn_ ( _Rn_ ( _j_ )), _j_ = 1 _, . . . , m_ . Given a null distribution _Q_ 0 and _α ∈_ (0 _,_ 1), define (1 _− α_ )–quantiles, _c_ ( _A_ ) = _c_ ( _A, Q_ 0 _, α_ ) _∈_ IR, for maxima of random variables _Z_ = ( _Z_ ( _j_ ) : _j_ = 1 _, . . . , m_ ) _∼ Q_ 0 over the complements of subsets _A ⊆{_ 1 _, . . . , m}_


Given the indices _Rn_ ( _j_ ) for the order statistics _Tn,_ ( _j_ ), define (1 _− α_ )–quantiles

_Cn_ ( _j_ ) = _c_ ( _{Rn_ (1) _, . . . , Rn_ ( _j −_ 1) _}, Q_ 0 _, α_ )

Page 53

#### and test statistics


<!-- Start of picture text -->
<br>Tn, ( j ) , if Tn, ( j− 1) > Cn ( j − 1)<br>T ∗<br>, j = 1 , . . . , m.<br>n, ( j ) ≡<br><br>otherwise<br> −∞,<br><!-- End of picture text -->

The step-down maxT multiple testing procedure for controlling the FWER at level _α_ is defined by

Reject _H_ 0 _,Rn_ ( _j_ ) if _Tn,_<sup>_∗_</sup> ( _j_ )<sup>_> Cn_(</sup><sup>_j_),</sup> _j_ = 1 _, . . . , m_ .

Page 54

#### **Adjusted P-values**

Note that the definition _Tn,_<sup>_∗_</sup> ( _j_ )<sup>=</sup><sup>_−∞_,if</sup><sup>_Tn,_(</sup><sup>_j−_1)</sup><sup>_≤Cn_(</sup><sup>_j −_1),</sup> ensures that the procedure is indeed step-down, that is, one can only reject a particular hypothesis provided all hypotheses with larger test statistics were rejected beforehand. Rather than simply reporting rejection or not of the hypotheses at a prespecified level _α_ , one can report adjusted _p_ -values for Procedure 2, computed under the null distribution _Q_ 0. The adjusted _p_ -value for hypothesis _H_ 0 _,Rn_ ( _j_ ) is given by


Here the adjusted _p_ -values are conditional on the observed test statistics and their ranks. The procedure for controlling the FWER

Page 55

at level _α_ can then be stated equivalently as _j_ = 1 _, . . . , m_ . Reject _H_ 0 _,Rn_ ( _j_ ) if _P_<sup>˜</sup> _n_ ( _Rn_ ( _j_ )) _≤ α_ ,

Page 56

#### **Assumptions**

In order to prove asymptotic control of the FWER by Procedure 2, we make the following two assumptions.

**Assumption A1T.** There exists an _m_ -dimensional random vector _Z ∼ Q_ 0( _P_ ) so that


We also assume that for _α ∈_ (0 _,_ 1)


**Assumption A2T.** There exists a degenerate maximal value _M_ 1

Page 57


<!-- Start of picture text -->
(e.g., + ∞ ) so that for all M < M 1<br>Pr min → 1 as n →∞<br>Tn ( j )  ≥ M (20)<br>� j∈S 0 c �<br>and<br>M lim ↑M 1 n lim →∞ Pr max j∈S 0 Tn ( j )  ≥ M = 0 . (21)<br>� �<br><!-- End of picture text -->

Note that these assumptions only require that _Tn_ represents a sensible set of test statistics.

Page 58

**Theorem:** Given a null distribution _Q_ 0 and _α ∈_ (0 _,_ 1), denote the number of Type I errors for Procedure 2 by


Suppose Assumptions A1T and A2T on the test statistics _Tn_ ( _j_ ) and null distribution _Q_ 0 hold. Then, Procedure 2 provides asymptotic control of the family-wise error rate at level _α_ , that is, lim sup _n→∞_<sup>_Pr_(</sup><sup>_Vn≥_1)</sup><sup>_≤α._</sup>

If (18) in Assumption A1T holds with equality, then asymptotic control is exact:

_n_ lim _→∞_<sup>_Pr_(</sup><sup>_Vn≥_1) =</sup><sup>_α._</sup>

Page 59

#### **Outline Proof.**

Note that, with probability one in the limit, the first _m_ 1 = _|S_ 0<sup>_c|_</sup> rejected hypotheses correspond to the _m_ 1 false null hypotheses. Thus, no Type I errors are committed for these first _m_ 1 rejections and one can focus on the _m_ 0 least significant statistics, _Tn,_ ( _j_ ), _j_ = _m_ 1 + 1 _, . . . , m_ , which now correspond to the test statistics for the true nulls, _Tn_ ( _j_ ), _j ∈ S_ 0. By definition of the step-down procedure, a Type I error is committed iff max _j∈S_ 0 _Tn_ ( _j_ ) _> Cn_ ( _S_ 0<sup>_c_),</sup> which is controlled at level _α_ . Thus, conditional on having rejected the first _m_ 1 correct rejections, with probability 1 _− α_ the procedure will not reject at step _m_ 1 + 1 and thus result in zero false rejections. **Remark:** Local alternatives cause non-control of FWE for step-down procedures.

Page 60

**Step-down procedure (FWE) based on minima of** _p_ **-values** Procedure 2 above is a step-down analogue of the single-step _common-cut-off_ procedure. One can also prove asymptotic control of the FWER for an analogue of Procedure 2, where maxima of test statistics _Tn_ ( _j_ ) are replaced by minima of unadjusted _p_ -values _Pn_ ( _j_ ), also computed under the proposed null distribution _Q_ 0: _Pn_ ( _j_ ) = _Q_<sup>¯</sup> 0 _j_ ( _Tn_ ( _j_ )), where _Q_<sup>¯</sup> 0 _j_ , _j_ = 1 _, . . . , m_ , denote the marginal survival functions corresponding to the null distribution _Q_ 0. Such a procedure corresponds to (2.10) in Section 2.6 of Westfall and Young (1993), (with the important distinction in the choice of null distribution _Q_ 0) and is a step-down version of the _common-quantile_ procedure in Pollard, van der Laan (2003). Note that procedures based on maxima of test statistics (maxT) and minima of _p_ -values (minP) are equivalent, when the test statistics _Tn_ ( _j_ ) are identically distributed, _j_ = 1 _, . . . , m_ . In this case, the marginal survival functions _Q_<sup>¯</sup> 0 _j_ are the same for each _j_ ,

Page 61

and thus the significance rankings based on _Tn_ ( _j_ ) and _Pn_ ( _j_ ) coincide. In general, however, the two procedures produce different results, and considerations of balance, power, and computational feasibility should dictate the choice between the two approaches. In the case of non-identically distributed test statistics _Tn_ ( _j_ ), not all tests are weighted equally in the maxT procedure and this can lead to unbalanced adjustments. When the null distribution _Q_ 0 is replaced by a resampling-based estimator _Q_<sup>ˆ</sup> 0 _n_ (Section **??** ), procedures based on minima of _p_ -values tend to be more sensitive to the number of resampling steps and more conservative than those based on maxima of test statistics, due to discreteness when estimating quantiles. Also, minP procedures require more computations than maxT procedures, because the unadjusted _p_ -values _Pn_ ( _j_ ) must be estimated before considering the distribution of their successive minima. Finally, note that while nominal _p_ -values computed from a

Page 62

standard normal or other type of distribution may not be correct, a step-down procedure based on minima of such transformed test statistics nonetheless provides asymptotic control of the FWER (e.g., _Pn_ ( _j_ ) = Φ(<sup>¯</sup> _Tn_ ( _j_ )), where Φ<sup>¯</sup> is the standard normal survival function). That is, these _p_ -values can be viewed as just another type of test statistic _Tn_ ( _j_ ) and one can appeal to previous theorems.

Here, however, we propose a step-down multiple testing procedure where _p_ -values are also defined in terms of the null distribution _Q_ 0, that is, _Pn_ ( _j_ ) = _Q_<sup>¯</sup> 0 _j_ ( _Tn_ ( _j_ )). We therefore have a more specific procedure and assumptions for proving asymptotic control of the family-wise error rate. Type I error control by the minP procedure relies on Assumptions A1P and A2P, below.

Page 63

**Procedure 3. Step-down procedure based on minima of** _p_ **-values (minP) — control of the FWER.** Given a null distribution _Q_ 0, define marginal or unadjusted _p_ -values as

_Pn_ ( _j_ ) = _PrQ_ 0( _Z_ ( _j_ ) _≥ Tn_ ( _j_ )) = _Q_<sup>¯</sup> 0 _j_ ( _Tn_ ( _j_ )) _,_ (22)

where _Z_ is an _m_ -dimensional random vector _Z ∼ Q_ 0 and _Q_<sup>¯</sup> 0 _j_ , _j_ = 1 _, . . . , m_ , denote the marginal survival functions corresponding to the null distribution _Q_ 0. Let _Pn,_ ( _j_ ) be the ordered _p_ -values, _Pn,_ (1) _≤ . . . ≤ Pn,_ ( _m_ ), and _Rn_ ( _j_ ) the indices for these order statistics, so that _Pn,_ ( _j_ ) = _Pn_ ( _Rn_ ( _j_ )), _j_ = 1 _, . . . , m_ . Define _α_ –quantiles, _c_ ( _A_ ) = _c_ ( _A, Q_ 0 _, α_ ) _∈_ IR, _α ∈_ (0 _,_ 1), for minima of _p_ -values ( _Q_<sup>¯</sup> 0 _j_ ( _Z_ ( _j_ )) : _j_ = 1 _, . . . m_ ) over the complements of subsets _A ⊆{_ 1 _, . . . , m}_


Page 64

Given the indices _Rn_ ( _j_ ) for the ordered _p_ -values _Pn,_ ( _j_ ), define _α_ –quantiles

_Cn_ ( _j_ ) = _c_ ( _{Rn_ (1) _, . . . , Rn_ ( _j −_ 1) _}, Q_ 0 _, α_ )

and statistics

 _Pn,_ ( _j_ ) _,_ if _Pn,_ ( _j−_ 1) _< Cn_ ( _j −_ 1) _P_<sup>_∗_</sup> _, j_ = 1 _, . . . , m. n,_ ( _j_ )<sup>_≡_</sup>  1 _,_ otherwise 

The step-down minP multiple testing procedure for controlling the FWER at level _α_ is defined by

Reject _H_ 0 _,Rn_ ( _j_ ) if _Pn,_<sup>_∗_</sup> ( _j_ )<sup>_< Cn_(</sup><sup>_j_),</sup><sup>_j_= 1</sup><sup>_, . . . , m_.</sup>

Page 65

#### **Adjusted P-values**

Note that the definition _Pn,_<sup>_∗_</sup> ( _j_ )<sup>= 1,if</sup><sup>_Pn,_(</sup><sup>_j−_1)</sup><sup>_≥Cn_(</sup><sup>_j −_1),ensures</sup> that the procedure is indeed step-down, that is, one can only reject a particular hypothesis provided all hypotheses with smaller unadjusted _p_ -values were rejected beforehand. Adjusted _p_ -values are defined similarly as for Procedure 2. The adjusted _p_ -value for hypothesis _H_ 0 _,Rn_ ( _j_ ) is given by max min _. P_ ˜ _n_ ( _Rn_ ( _j_ )) = _PrQ_ 0 _Q_ ¯0 _j_ ( _Z_ ( _j_ )) _< Pn_ ( _Rn_ ( _k_ )) _k_ =1 _,...,j_ � � _l∈{Rn_ ( _k_ ) _,...,Rn_ ( _m_ ) _}_ �� (23)

Page 66

#### **Assumptions**

Theorem below, proves asymptotic control of the FWER by Procedure 3 under the following two assumptions, which are the _p_ -value analogues of Assumptions A1T and A2T, respectively. **Assumption A1P.** There exists an _m_ -dimensional random vector _Z ∼ Q_ 0( _P_ ) so that


where _Q_<sup>¯</sup> 0 _j_ , _j_ = 1 _, . . . , m_ , denote the marginal survival functions corresponding to the null distribution _Q_ 0 = _Q_ 0( _P_ ). We also assume that for _α ∈_ (0 _,_ 1)


Page 67


<!-- Start of picture text -->
Assumption A2P. For each ϵ >  0,<br>Pr max → 1 as n →∞<br>Pn ( j )  ≤ ϵ (26)<br>� j∈S 0 c �<br>and<br>lim ϵ↓ 0 n lim →∞ Pr j min ∈S 0 Pn ( j )  ≤ ϵ = 0 . (27)<br>� �<br><!-- End of picture text -->

Page 68

**Theorem:** Given a null distribution _Q_ 0 and _α ∈_ (0 _,_ 1), denote the number of Type I errors for Procedure 3 by

_m Vn ≡_ � _I_ ( _Pn,_<sup>_∗_</sup> ( _j_ )<sup>_< Cn_(</sup><sup>_j_)</sup><sup>_, Rn_(</sup><sup>_j_)</sup><sup>_∈S_0)</sup><sup>_._</sup> _j_ =1

Suppose Assumptions A1P and A2P hold, specifically, conditions (24), (25), (26), and (27) are satisfied by the _p_ -values _Pn_ ( _j_ ), i.e., by the test statistics _Tn_ ( _j_ ) and null distribution _Q_ 0. Then, Procedure 3 provides asymptotic control of the family-wise error rate at level _α_ , that is,

lim sup _n→∞_<sup>_Pr_(</sup><sup>_Vn≥_1)</sup><sup>_≤α._</sup>

If (24) in Assumption A1P holds with equality, then asymptotic control is exact

_n_ lim _→∞_<sup>_Pr_(</sup><sup>_Vn≥_1) =</sup><sup>_α._</sup>

Page 69

**Procedure 4. Step-down procedure based on maxima of test statistics (maxT) — control of GFWER** Let _Tn,_ ( _j_ ) be the ordered test statistics, _Tn,_ (1) _≥ . . . ≥ Tn,_ ( _m_ ), and _Rn_ ( _j_ ) the indices for these order statistics, so that _Tn,_ ( _j_ ) = _Tn_ ( _Rn_ ( _j_ )), _j_ = 1 _, . . . , m_ . Given a null distribution _Q_ 0 and _α ∈_ (0 _,_ 1), define (1 _− α_ )–quantiles, _c_ ( _A_ ) = _c_ ( _A, Q_ 0 _, α_ ) _∈_ IR, for maxima of random variables _Z_ = ( _Z_ ( _j_ ) : _j_ = 1 _, . . . , m_ ) _∼ Q_ 0 over the complements of subsets _A ⊆{_ 1 _, . . . , m}_


Given the indices _Rn_ ( _j_ ) for the order statistics _Tn,_ ( _j_ ), define (1 _− α_ )–quantiles

_Cn_ ( _j_ ) = _c_ ( _{Rn_ (1) _, . . . , Rn_ ( _j −_ 1) _}, Q_ 0 _, α_ )

Page 70

#### and test statistics


Let


be the number of test-statistics which are not set to _−∞_ . The step-down maxT multiple testing procedure for controlling the GFWER= _P_ ( _Vn > k_ ) at level _α_ is defined by

Reject _H_ 0 _,Rn_ ( _j_ ) if _Tn,_<sup>_∗_</sup> ( _j_ )<sup>_> Cn_(</sup><sup>_j_),</sup> _j_ = 1 _, . . . , m_ and also reject _{H_ 0 _,Rn_ ( _l∗_ ) _, H_ 0 _,Rn_ ( _l∗_ +1) _, . . . , H_ 0 _,Rn_ ( _l∗_ + _k−_ 1) _}_ .

**Remark.** Note that this procedure is nothing else than first carrying out the Step-down procedure for controlling FWE and subsequently rejecting the next _k_ in the ordered list of

Page 71

test-statistics. Let _Vn_ (1) be the number of False-positives for the procedure 2 controlling FWE, and _Vn_ ( _k_ ) be the number of false positives for Procedure 4 controlling GFWE.. Since the set of rejections for the above procedure equals the union of the set of rejections for Procedure 2 controlling FWE and another _k_ rejections, we have that _Vn_ ( _k_ ) _≤ Vn_ (1) + _k_ . Since lim sup _n→∞ P_ ( _Vn_ (1) _>_ 0) _≤ α_ , it follows that the above procedure satisfies

lim sup _n→∞_<sup>_P_(</sup><sup>_Vn_(</sup><sup>_k_)</sup><sup>_> k_)</sup><sup>_≤α._</sup>

In addition, if lim sup _n→∞ P_ ( _Vn_ (1) _>_ 0) = _α_ , then we have lim sup _n→∞_<sup>_P_(</sup><sup>_Vn_(</sup><sup>_k_) =</sup><sup>_k_) = 1</sup><sup>_−α._</sup>

That is, with probabilty tending to 1- _α_ , this procedure will select precisely _k_ false positives. This gives us the following theorem. This procedure and theorem immedidately generalizes to a step-down procedure based on minima of _p_ -values controlling GFWER.

Page 72

**Theorem for Procedure 4 controlling GFWER:** Given a null distribution _Q_ 0 and _α ∈_ (0 _,_ 1), denote the number of Type I errors for Procedure 4 by


Suppose Assumptions A1T and A2T on the test statistics _Tn_ ( _j_ ) and null distribution _Q_ 0 hold. Then, Procedure 4 provides asymptotic control of the generalized family-wise error rate at level _α_ , that is,

lim sup _n→∞_<sup>_Pr_(</sup><sup>_Vn_(</sup><sup>_k_)</sup><sup>_> k_)</sup><sup>_≤α._</sup>

If (18) in Assumption A1T holds with equality, then asymptotic control is exact:

_n_ lim _→∞_<sup>_Pr_(</sup><sup>_Vn_(</sup><sup>_k_)</sup><sup>_> k_) =</sup><sup>_α,_</sup>

Page 73

and, in fact, in that case, we have _n_ lim _→∞_<sup>_Pr_(</sup><sup>_Vn_(</sup><sup>_k_) =</sup><sup>_k_) = 1</sup><sup>_−α._</sup>

Page 74

**Asymptotic Control for Consistent Estimator Null Distribution** If _Q_<sup>ˆ</sup> 0 _n_ is a consistent estimator of _Q_ 0, then the corollary below shows that procedures based on estimated cut-offs _C_<sup>ˆ</sup> _n_ ( _j_ ) also provide asymptotic control of the Type I error rate. We state the Corollary for the step-down procedure based on maxima of test statistics (Procedure 2), but the same result applies to the general single-step procedure (Procedure 1) and the step-down procedure based on minima of _p_ -values (Procedure 3).

Page 75

**Corollary:** Let _Q_<sup>ˆ</sup> 0 _n_ be such that, given the empirical distribution _Pn_ of _X_ 1 _, . . . , Xn_ , it converges pointwise (i.e., converges weakly) to a limit distribution _Q_ 0 with continuous and strictly increasing marginal cumulative distribution functions _Q_ 0 _j_ , _j_ = 1 _, . . . , m_ . This implies that, conditional on _Pn_ ,


Denote the number of Type I errors for Procedure 2 based on the estimator _Q_<sup>ˆ</sup> 0 _n_ by


Then, the family-wise error rate is controlled asymptotically at level _α_ lim sup _n→∞_<sup>_Pr_( ˆ</sup><sup>_Vn≥_1)</sup><sup>_≤α._</sup>

Page 76

If (18) in Assumption A1 holds with equality, asymptotic control is exact lim _n→∞_<sup>_Pr_( ˆ</sup><sup>_Vn≥_1) =</sup><sup>_α._</sup>

Page 77

#### **Bootstrap Estimator of the Null Distribution**

The asymptotic null distribution _Q_ 0 = _Q_ 0( _P_ ) can be estimated with the non-parametric or model-based bootstrap. Let _P_<sup>˜</sup> _n_ denote an estimator of the true data generating distribution _P_ . For the non-parametric bootstrap, _P_<sup>˜</sup> _n_ is simply the empirical distribution _Pn_ , that is, samples of size _n_ are drawn at random with replacement from the observed _X_ 1 _, . . . , Xn_ . For the model-based bootstrap, _P_<sup>˜</sup> _n_ is based on a model _M_ , such as the _m_ -variate normal distribution. Each bootstrap sample consists of _n_ i.i.d. realizations _X_ 1<sup>#</sup><sup>_, . . . , X_</sup> _n_<sup>#</sup> of a random variable _X_<sup>#</sup> _∼ P_<sup>˜</sup> _n_ . Denote test statistics computed from bootstrap samples by _Tn_<sup>#.Theproposednulldistribution</sup><sup>_Q_0</sup> from Theorems can be estimated by the distribution _Q_<sup>ˆ</sup> 0 _n_ of


Page 78

where


Under regularity conditions, the bootstrap is known to be consistent, in the sense that _Zn_<sup>#</sup><sup>_⇒DZ∼Q_0conditionalon</sup><sup>_P_˜</sup><sup>_n_</sup> In practice, one can only approximate the distribution of _Zn_<sup>#byan</sup> empirical distribution over _B_ bootstrap samples drawn from _P_<sup>˜</sup> _n_ . That is, the estimator _Q_<sup>ˆ</sup> 0 _n_ is the empirical distribution of _Zn_<sup>_b_,</sup> where _Zn_<sup>_b_correspondstotheteststatisticsforthe</sup><sup>_b_thbootstrap</sup> sample, _b_ = 1 _, . . . , B_ . For procedures based on maxima of the test statistics _Tn_ (Procedure 2), the quantiles _c_ ( _A, Q_<sup>ˆ</sup> 0 _n, α_ ) are simply the quantiles of max _j /∈A Zn_<sup>_b_(</sup><sup>_j_)overthe</sup><sup>_B_bootstrapsamples,thatis,</sup>

Page 79


Resampling-based procedures for minima of _p_ -values (Procedure 3) are more complex, as one must first estimate _p_ -values _Pn_ ( _j_ ) = _PrQ_ 0( _Z_ ( _j_ ) _≥ Tn_ ( _j_ )) using _Q_<sup>ˆ</sup> 0 _n_ , before considering the distribution of their successive minima. Unadjusted _p_ -values _Pn_ ( _j_ ) are estimated by


The reader is referred to ? for a fast algorithm for resampling estimation of adjusted _p_ -values for step-down procedures based on minima of _p_ -values.

Page 80

**Example:** _t_ **-statistics for single parameter hypotheses** Consider testing _m_ single parameter null hypotheses of the form _H_ 0 _j_ : _µ_ ( _j_ ) _≤ µ_ 0( _j_ ) against alternative hypotheses _H_ 1 _j_ : _µ_ ( _j_ ) _> µ_ 0( _j_ ), where _µ_ ( _j_ ) = _µ_ ( _j | P_ ) is a real-valued parameter, _j_ = 1 _, . . . , m_ . Then, the set of true null hypotheses can be represented as _S_ 0 = _{j_ : _µ_ ( _j_ ) _≤ µ_ 0( _j_ ) _}_ .

Let _µn_ ( _j_ ) be an asymptotically linear estimator of _µ_ ( _j_ ), with influence curve _ICj_ ( _X | P_ ), that is,


where _E_ [ _ICj_ ( _X | P_ )] = 0 and _IC_ ( _X | P_ ) = ( _ICj_ ( _X | P_ ) : _j_ = 1 _, . . . , m_ ) denotes the _m_ -dimensional vector influence curve. Let


Page 81

be the standardized test statistic, or _t_ -statistics, for the null hypothesis _H_ 0 _j_ , where _σn_ ( _j_ ) is a consistent estimator of _σ_ ( _j_ ) _≡ E_ [ _ICj_ ( _X | P_ )<sup>2</sup> ], _j_ = 1 _, . . . , m_ . Large values of _Tn_ ( _j_ ) provide evidence against _H_ 0 _j_ : _µ_ ( _j_ ) _≤ µ_ 0( _j_ ). Let _Tn_ = ( _Tn_ ( _j_ ) : _j_ = 1 _, . . . , m_ ) be the corresponding _m_ -vector of test statistics, with joint distribution _Qn_ = _Qn_ ( _P_ ).

Page 82

**Choice of null distribution** _Q_ 0

The test statistics _Tn_ = ( _Tn_ ( _j_ ) : _j_ = 1 _, . . . , m_ ) satisfy Assumptions A1T and A2T and Assumptions A1P and A2P, where the null distribution _Q_ 0 = _Q_ 0( _P_ ) is the _m_ -variate normal distribution with mean zero and covariance matrix _ρ_ ( _P_ ), the correlation matrix of the vector influence curve _IC_ ( _X | P_ ). Thus, step-down Procedures 2 and 3, based on _Tn_ and the null distribution _Q_ 0, provide asymptotic control of the FWER for the test of single-parameter null hypotheses of the form _H_ 0 _j_ : _µ_ ( _j_ ) _≤ µ_ 0( _j_ ) against alternative hypotheses _H_ 1 _j_ : _µ_ ( _j_ ) _> µ_ 0( _j_ ), _j_ = 1 _, . . . , m_ .

Page 83

#### **Correspondence with explicit construction**

The above theorems involve a null distribution _Q_ 0 that was derived specifically in terms of the statistics _µn_ in equation (31). It turns out that, under mild regularity conditions, this null distribution _Q_ 0 corresponds to the general proposal _Q_<sup>_∗_</sup> 0<sup>definedastheasymptotic</sup> distribution of _m_ -vectors _Zn_<sup>_∗_,where</sup>

_Z_<sup>_∗_</sup> _n_<sup>(</sup><sup>_j_)</sup><sup>_≡ν_0</sup><sup>_n_(</sup><sup>_j_)</sup> _Tn_ ( _j_ ) + _θ_ 0( _j_ ) _− ETn_ ( _j_ ) _, j_ = 1 _, . . . , m._ � �

The proposal above for the null distribution is defined simply as the asymptotic distribution of _m_ -vectors _Zn_ , where


With _θ_ 0( _j_ ) _≡_ 0 and _τ_ 0( _j_ ) _≡_ 1, one can show that _Zn_<sup>_∗_and</sup><sup>_Zn_have</sup> the same asymptotic joint distribution, that is _Q_ 0 and _Q_<sup>_∗_</sup> 0<sup>coincide.</sup>

Page 84

#### **Example: Tests of means**

A familiar testing problem that falls within this framework is that where _X_ 1 _, . . . , Xn_ are _n_ i.i.d. random _m_ -vectors, _X ∼ P_ , and the parameter of interest is the mean vector

_µ_ = _µ_ ( _P_ ) = ( _µj_ = _µ_ ( _j | P_ ) : _j_ = 1 _, . . . , m_ ) = _EX_ . Null hypotheses _H_ 0 _j_ : _µ_ ( _j_ ) _≤ µ_ 0( _j_ ) then refer to individual components of the mean vector _µ_ and the test statistics _Tn_ ( _j_ ) are the usual one sample _t_ -statistics, where _µn_ ( _j_ ) = _X_<sup>¯</sup> _n_ ( _j_ ) = _n_<sup><u>1</u></sup> � _i_<sup>_Xi_(</sup><sup>_j_)and</sup> _σn_<sup>2(</sup><sup>_j_) =</sup> _n_<sup><u>1</u></sup> � _i_<sup>(</sup><sup>_Xi_(</sup><sup>_j_)</sup><sup>_−X_¯</sup><sup>_n_(</sup><sup>_j_))2areempiricalmeansandvariances</sup> for the _m_ components, respectively.

Page 85

#### **Example: Tests of correlations**

Another common testing problem covered by this framework is that where the parameter of interest in the correlation matrix _ρ_ = _ρ_ ( _P_ ) = ( _ρjk_ ( _P_ )) for the random vectors in the previous example, _ρjk_ = _ρjk_ ( _P_ ) = _Cor_ ( _Xj, Xk_ ), _j, k_ = 1 _, . . . , m_ . Suppose we are interested in testing the _m_ ( _m −_ 1) _/_ 2 null hypotheses that the _m_ components of _X_ are uncorrelated, _Hjk_ : _ρjk_ = 0, _j_ = 1 _, . . . , m_ , _k_ = _j_ + 1 _, . . . , m_ . Common test statistics for this problem are _Tn_ ( _jk_ ) =<sup>_√_</sup> _<u>nrjk</u>_ , where _rjk_ are the sample correlations. As discussed in Westfall and Young (1993), Example 2.2, p. 43, subset pivotality fails for this testing problem. To see this, consider the simple case _m_ = 3 and assume _H_ 12 and _H_ 13 are true, so that _ρ_ 12 = _ρ_ 13 = 0. Then the joint distribution of ( _T_ 12 _, T_ 23) is asymptotically normal with mean vector zero, variance 1, and correlation _ρ_ 23, and thus depends on the truth or falsity of the third hypothesis _H_ 23. In other words, the asymptotic covariance of

Page 86

the vector influence curve for the sample correlations is not the same under the true _P_ as it is under a null distribution _P_ 0 for which _ρjk ≡_ 0 _∀j̸_ = _k_ . However, our proposed null distribution _Q_ 0 (and bootstrap estimator thereof) for the test statistics _Tn_ does control the Type I error rate when used in Procedures 1, 2, and 3. Tests of correlations thus provide an example where standard procedures based on subset pivotality fail, while procedures based on our general null distribution _Q_ 0 achieve the desired control.

Page 87

_F_ **-statistics for multiple parameter hypotheses** Consider random _m_ -vectors _Xk ∼ Pk_ , _k_ = 1 _, . . . , K_ , from _K_ different populations with data generating distributions _Pk_ ***. Denote the mean vector and covariance matrix in population _k_ by _µk_ = _EXk_ and Σ _k_ , respectively. We are interested in testing the _m_ null hypotheses _H_ 0 _j_ : _µk_ ( _j_ ) _≡ µ_ ( _j_ ) _∀k_ , that, for each population, the _j_ th components _µk_ ( _j_ ) of the mean vectors are equal to a common value _µ_ ( _j_ ), _j_ = 1 _, . . . , m_ . As before, let _S_ 0 denote the set of true null hypotheses. Suppose, we observe i.i.d. samples _Xk,_ 1 _, . . . , Xk,nk_ , of size _nk_ from population _k_ , _k_ = 1 _, . . . , K_ . Let _n_ =<sup>�</sup> _k_<sup>_nk_denotethetotalsamplesizeand</sup><sup>_δk,n_=</sup><sup>_nk/n_the</sup> proportion of observations from population _k_ in the sample, where it is assumed that, _∀k_ , _δk,n → δk >_ 0 as _n →∞_ .

Page 88

As test statistics we can use the well-known _F_ -statistics _<u>k</u>_<sup>_nk_</sup><sup><u>(</u></sup><sup>_X_¯</sup><sup>_k_</sup><sup><u>(</u></sup><sup>_<u>j</u>_</sup><sup><u>)</u></sup><sup>_−X_¯</sup><sup><u>(</u></sup><sup>_<u>j</u>_</sup><sup><u>))2</u></sup> _Tn_ ( _j_ ) =<sup>1</sup><sup>_<u>/</u>_</sup><sup><u>(</u></sup><sup>_K −_1)</sup><sup><u>�</u></sup> _j_ = 1 _, . . . , m,_ 1 _/_ ( _n − K_ )<sup><u>�</u></sup> _i,k_<sup>(</sup><sup>_Xk,i_(</sup><sup>_j_)</sup><sup>_−X_</sup><sup><u>¯</u></sup><sup>_k_(</sup><sup>_j_))2</sup><sup>_,_</sup> (32) where _X_<sup>¯</sup> _k_ denotes the sample mean vector for population _k_ and _X_ ¯ =<sup>�</sup> _k_<sup>_δk,nX_¯</sup><sup>_k_denotestheoverallmeanvector.</sup>

Page 89

**Choice of null distribution** _Q_ 0

**Theorem:** The _F_ -statistics _Tn_ = ( _Tn_ ( _j_ ) : _j_ = 1 _, . . . , m_ ) satisfy Assumptions A1T and A2T of Theorem **??** and Assumptions A1P and A2P of Theorem **??** , where the null distribution _Q_ 0 = _Q_ 0( _P_ ) is the joint distribution of the random _m_ -vector _Z_ = _f_ ( _Z_ 1 _, . . . , ZK_ ), defined in terms of independent Gaussian _m_ -vectors _Zk ∼ N_ (0 _,_ Σ _k_ ) and a quadratic function _f_ specified below. Thus, step-down Procedures 2 and 3, based on _Tn_ and the null distribution _Q_ 0, provide asymptotic control of the FWER for the test of multiple parameter null hypotheses _H_ 0 _j_ : _µk_ ( _j_ ) _≡ µ_ ( _j_ ) _∀k_ , _j_ = 1 _, . . . , m_ .

Page 90

#### **Proof of Theorem**

Firstly, note that the denominators of the _F_ -statistics can be written as


where _σ_ ˆ _k,n_<sup>2(</sup><sup>_j_)areconsistentestimatorsofthepopulationvariances</sup> _σk_<sup>2(</sup><sup>_j_),i.e.,ofthediagonalelementsofcovariancematricesΣ</sup><sup>_k_,</sup> _k_ = 1 _, . . . , K_ . Thus, as _n →∞_ ,

_Dn_ ( _j_ ) _⇒P D_ ( _j_ ) = _δkσk_<sup>2(</sup><sup>_j_)</sup><sup>_,_</sup> _j_ = 1 _, . . . , m._ � _k_ The numerator of the _F_ -statistics _Tnn_ ( _j_ ) can be rewritten as 2 1   _Nn_ ( _j_ ) = � � � _δk,nδl,nZl,n_ ( _j_ ) _, K −_ 1 _k l̸_ = _k_ <u>(1</u> _− δk,n_ ) _Zk,n_ ( _j_ ) _−_ <u></u>

The numerator of the _F_ -statistics _Tnn_ ( _j_ ) can be rewritten as

Page 91

where _Zk,n_ =<sup>_√_</sup> _<u>nk</u>_ <u>(</u> _X_<sup>¯</sup> _k − µ_ ), _k_ = 1 _, . . . , K_ . Thus, the _m_ -vector _Tn_ = ( _Tn_ ( _j_ ) : _j_ = 1 _, . . . , m_ ) of _F_ -statistics can be approximated by a random _m_ -vector _Zn_ that is a simple quadratic function _f_ ( _Z_ 1 _,n, . . . , ZK,n_ ) = ( _fj_ ( _Z_ 1 _,n, . . . , ZK,n_ ) : _j_ = 1 _, . . . , m_ ) of the _K_ independent _m_ -vectors _Zk,n_ , _k_ = 1 _, . . . , K_ ,


By the Central Limit Theorem, ( _Zk,n_ ( _j_ ) : _j ∈ S_ 0) _⇒D_ ( _Zk_ ( _j_ ) : _j ∈ S_ 0), where _Zk ∼ N_ (0 _,_ Σ _k_ ), _k_ = 1 _, . . . , K_ . For _j ∈/ S_ 0, _Zk,n_ ( _j_ ) =<sup>_√_</sup> _<u>nk</u>_ <u>(</u> _X_<sup>¯</sup> _k_ ( _j_ ) _− µk_ ( _j_ )) +<sup>_√_</sup> _<u>nk</u>_ <u>(</u> _µk_ ( _j_ ) _− µ_ ( _j_ )) converge to either + _∞_ or _−∞_ for some _k_ . Applying the Continuous Mapping Theorem to the function ( _fj_ ( _Z_ 1 _,n, . . . , ZK,n_ ) : _j ∈ S_ 0) proves that ( _Tn_ ( _j_ ) : _j ∈ S_ 0) converges in distribution to ( _Z_ ( _j_ ) : _j ∈ S_ 0), where _Z_ = _f_ ( _Z_ 1 _, . . . , ZK_ ) and the _Zk_ are independent _m_ -vectors with

Page 92

_Zk ∼ N_ (0 _,_ Σ _k_ ), _k_ = 1 _, . . . , K_ . That is, the limit distribution of ( _Tn_ ( _j_ ) : _j ∈ S_ 0) is directly implied by the multivariate normal distributions _N_ (0 _,_ Σ _k_ ), where Σ _k_ denotes the _m × m_ covariance matrix of _Xk ∼ Pk_ , _k_ = 1 _, . . . , K_ . For _j ∈/ S_ 0, _Tn_ ( _j_ ) _→∞_ . Therefore, the _F_ -statistics _Tn_ satisfy Assumptions A1T and A2T, where the null distribution _Q_ 0 = _Q_ 0( _P_ ) is the joint distribution of the random _m_ -vector _Z_ = _f_ ( _Z_ 1 _, . . . , ZK_ ), for independent _m_ -vectors _Zk ∼ N_ (0 _,_ Σ _k_ ) and the quadratic function _f_ defined in equation (33). In Assumption A2T, _M_ 1 = _∞_ , and condition (19) in Assumption A1T follows immediately by continuity of _Q_ 0. For this definition of _Q_ 0, Assumptions A1P and A2P are also satisfied.

Page 93

**Explicit Null Distribution for** _F_ **-test Statistics**

Page 94

**Multiple Testing with Asymptotic Control of False Discovery Rate**

**Mark van der Laan** Division of Biostatistics, UC Berkeley `www.stat.berkeley.edu/~laan` www.bepress.com/ucbbiostat/

- _⃝_ c Copyright 2003, all rights reserved

**The nonparametric mixture model for test-statistics** Let _T_ 1<sup>_n, . . . , T n_</sup> _m_<sup>be</sup><sup>_m_independentandidenticallydistributedtest</sup> statistics for null hypotheses _H_ 0 _,j_ , _j_ = 1 _, . . . , m_ , with density being a mixture of a known null density _f_ 0 _,n_ and unknown density _f_ 1 _,n_ with unknown mixing proportion _p_ 0:

_Tj_<sup>_n∼fn≡p_0</sup><sup>_f_0</sup><sup>_,n_+ (1</sup><sup>_−p_0)</sup><sup>_f_1</sup><sup>_,n._</sup>

Let _Fn, F_ 0 _,n, F_ 1 _,n_ be the corresponding cdf’s. **Remark:** A more common situation is that the finite sample null distribution _F_ 0 _,n_ can be consistently estimated with an estimator _F_ ˆ0 _,n_ in the sense that

_F_ 0 _,n − F_ 0 _→_ 0 _→ F_ ˆ0 _,n − F_ 0 0 _,_

where _F_ 0 denotes a limit null distribution. In this case, one replaces the null distribution _F_ 0 _,n_ by its estimate _F_<sup>ˆ</sup> 0 _,n_ .

Page 96

Equivalently, let _Bj ∼_ Bernoulli(1 _− p_ 0) be the hidden label, _Tj_<sup>_n_,</sup> given _Bj_ , has density _fBj ,n_ , the full data are _m_ i.i.d copies ( _Bj, Tj_<sup>_n_),</sup> _j_ = 1 _, . . . , p_ , but we only observe the test-statistics _Tj_<sup>_n_.Here</sup> _Bj_ = 1 _− I_ ( _H_ 0 _,j_ is true) indicates if the null-hypothesis _H_ 0 _,j_ is true. Let ( _B, T_<sup>_n_</sup> ) denote the random variables described by: _B ∼_ Bernoulli( _p_ 0), and _T_<sup>_n_</sup> , given _B_ , has density _fB,n_ .

Page 97

**Approximate correspondence between frequentist independence and nonparametric mixture model Frequentist independence model for test-statistics:** Suppose that it is known that the test-statistics are independent, that all the marginal distributions of test statistics corresponding with a true null hypothesis _H_ 0 _,j_ equal a common known distribution _F_ 0 _,n_ , but that distributions _Fj,n_ of _Tj_<sup>_n_,areunknownotherwise.</sup> Let _S_ 0 = _{j_ : _Fj,n_ = _F_ 0 _,n}_ be the set of true nulls. Let _p_ 0 _≡| S_ 0 _| /m_ . Let _F_ 1 _,n_ be the distribution of the mixture of _Fj,n_ , _j ∈ S_ 0<sup>_c_,withuniformmixingdistribution.Foradominating</sup> measure _µ_ , let _f_ 0 _,n ≡ dF_ 0 _,n/dµ_ , and _f_ 1 _,n ≡ dF_ 1 _,n/dµ_ . **Approximate correspondence:** Consider a parameter (such as FDR of the set _{j_ : _Tj_<sup>_n> t}_)ofthedistributionof</sup><sup>_⃗T n_underthe</sup> independence model which only depends on the _m_ -marginal distributions _Fj,n_ through _p_ 0 _, F_ 0 _,n, F_ 1 _,n_ . Then this parameter has

Page 98

approximately the same value under this independence distribution as under the corresponding mixture model distribution defined by _Bj ∼_ Bernoulli( _p_ 0), _Tj_<sup>_n∼fB_</sup> _j_<sup>_,n_,</sup><sup>_j_= 1</sup><sup>_, . . . , p_.Therefore,the</sup> mixture model provides a convenient working model to find the right cut-off _t_ ( _α_ ) so that the FDR of the set _{j_ : _Tj_<sup>_n> t}_equals</sup><sup>_α_.</sup> For example, it can be verified that


where _EIND_ denotes the expectation under the distribution of _⃗Tn_ in the frequentist independence model identified by _S_ 0, _F_ 0 _n_ , _Fjn_ , _j̸ ∈ S_ 0, and _EMIXT_ denotes the expectation under the distribution of ( _⃗Tn,⃗Bn_ ) in the i.i.d. mixture model identified by _p_ 0 = _| S_ 0 _| /m_ , _F_ 1 _n_ = _sumj̸∈S_ 0 _Fjn/ | S_ 0<sup>_c|_,and</sup><sup>_F_0</sup><sup>_n_.</sup>

Page 99

It remains to be seen till what degree we have: _<u>j</u>_ =1<sup>_I_(</sup><sup>_T n_</sup> _<u>j</u>_<sup>_> t, j∈S_0)</sup> _<u>j</u>_ =1<sup>_I_(</sup><sup>_T n_</sup> _<u>j</u>_<sup>_> t, Bj_= 0)</sup> _EIND ≈ EMIXT_ � <u>�</u> _m_ <u>�</u> _<u>mj</u>_ =1<sup>_I_(</sup><sup>_T n_</sup> _j_<sup>_> t_)</sup> � � <u>�</u> _m_ <u>�</u> _<u>mj</u>_ =1<sup>_I_(</sup><sup>_T n_</sup> _j_<sup>_> t_)</sup> One fundamental difference between the two (with each other) corresponding distributions is that under the frequentist model _| S_ 0 _|_ is fixed, while<sup>�</sup> _j_<sup>_I_(</sup><sup>_Bj_= 0)israndomwithmean</sup><sup>_| S_0</sup><sup>_|_.To</sup> obtain a stronger similarity one could enforce in the mixture model the constraint that<sup>�</sup> _j_<sup>_I_(</sup><sup>_Bj_= 0) =</sup><sup>_| S_0</sup><sup>_|_.Theeffectofthis</sup> additional constraint on our calculations in the mixture model might need to be investigated.

_._ �

Page 100

**Finite Sample Identifiability in nonparametric mixture model** Given the actual density _fn_ of the test-statisics and the null density _f_ 0 _,n_ , the proportion of true nulls _p_ 0 and the alternative density _f_ 1 _,n_ are identified up till:


**Parameter of interest in nonparametric mixture model.**

John Storey refers to Φ _n_ ( _Tj_<sup>_n_)as</sup><sup>_q_-valuesinhisworkonFDR,and</sup>

Page 101

therefore we will refer to _θn_ ( _Tj_<sup>_n_)aslocal</sup><sup>_q_-values.</sup>

Page 102

**Unknown Multiple Testing Procedures Controlling FDR** In the following lemmas we adopt the common convention to define the proportion of false discoveries as zero when the set of rejections is empty.

**Lemma** Let _Sn_<sup>_∗≡{j_:</sup><sup>_T n_</sup> _j_<sup>_≤t_</sup> _n_<sup>_∗_(</sup><sup>_α_)</sup><sup>_}_,where</sup> _t_<sup>_∗_</sup> _n_<sup>(</sup><sup>_α_)</sup><sup>_≡_min</sup><sup>_{t_:</sup><sup>_θn_(</sup><sup>_t_)</sup><sup>_≤α}_.Let</sup><sup>_α′_=</sup><sup>_θ_(</sup><sup>_t∗_</sup> _n_<sup>(</sup><sup>_α_)).Then</sup>


If _Sn_<sup>_∗≡{j_:</sup><sup>_θn_(</sup><sup>_T n_</sup> _j_<sup>)</sup><sup>_≤α}_,then</sup>


**Proof:** We prove the last statement. The proof of the first statement is similar. Note


Page 103


<!-- Start of picture text -->
The conditional expecation of this quantity, given T 1 n, . . . , T n p ,<br>equals<br>� j I ( θ ( T n j )  ≤ α ) θ ( T n j )<br>I ( | Sn ∗ |>  0) ≤ αI ( | Sn ∗ |>  0)<br>� j I ( θn ( T n j )  ≤ α )<br><!-- End of picture text -->

Page 104

**Lemma:** Let _Sn ≡{j_ : _Tj_<sup>_n> tn_(</sup><sup>_α_)</sup><sup>_}_,where</sup> _tn_ ( _α_ ) _≡_ min _{t_ : Φ _n_ ( _t_ ) _≤ α}._


**Proof:** We will now only proof the first statement, since the last statement is proved similarly. Note


The conditional expectation of this quantity, given the Bernoulli

Page 105


<!-- Start of picture text -->
indicators I ( T 1 n > tn ( α )) , . . . , I ( T n p > tn ( α )), equals<br>� j I ( T n j > tn ( α ))Φ n ( tn ( α ))<br>I ( | Sn |>  0) =  I ( | Sn |>  0) α ∗ .<br>� j I ( T n j > tn ( α ))<br><!-- End of picture text -->

Page 106

**Remark:** Thus, if _Pr_ ( _| Sn |>_ 0) _≈_ 1, and _α_<sup>_∗_</sup> = _α_ (as is the case for continuous distributions), we have that _Sn_ and _Sn_<sup>_∗_controlthe</sup> FDR exactly at level _α_ . Since Φ _n_ is easier to estimate from the data than _θn_ , we prefer the multiple testing procedure based on estimating _Sn_ (i.e., Φ _n_ ) in comparison with a multiple testing procedure estimating _Sn_<sup>_∗_(i.e.</sup><sup>_θn_).</sup>

Page 107

#### **Equivalence with Benjamini-Hochberg Method**

Under the assumption that Φ( _t_ ) is monotone in _t_ , without any loss we can use

_Sn_ = _{j_ : Φ _n_ ( _Tj_<sup>_n_)</sup><sup>_≤α}._</sup>

We need an estimate of Φ _n_ , and thus of _Fn_ and _p_ 0. Let _p_ ˆ0 be an estimate or upper bound of _p_ 0: e.g., _p_ ˆ0 = 1. A possible estimate of _Fn_ ( _t_ ) is given by:

_p_ 1 = _F_ ˆ _n_ ( _t_ ) � _I_ ( _Tj_<sup>_n≤t_)</sup><sup>_._</sup> _p j_ =1

ˆ¯ _F_ <u>¯0</u> _<u>,n</u>_ <u>(</u> _t_ <u>)</u> Let Φ<sup>ˆ</sup> _n_ = _p_ ˆ0 _Fn_ ( _t_ )<sup>.Let</sup> _pj ≡ F_<sup>¯</sup> 0 _,n_ ( _Tj_<sup>_n_)</sup><sup>_,j_= 1</sup><sup>_, . . . , p_</sup>

denote the _p_ -values, as calculated under the null distribution _F_ 0 _,n_ .

Page 108


<!-- Start of picture text -->
Then<br><!-- End of picture text -->


Page 109

**Asymptotic control of FDR** Under the assumption that the test-statistics _Tj,n_ , _j ∈ S_ 0<sup>_c_,converge</sup> to infinity for _n →∞_ , we have that _F_<sup>¯</sup> 1 _,n_ ( _t_ ) _→_ 1 for all _t_ . Assume that the null distribution converges as well to a limit distribution: _F_ 0 _,n → F_ 0 for _n →∞_ . Then, _Fn → p_ 0 _F_ 0 (or equivalently, _F_ ¯ _n →_ 1 _− p_ 0 _F_ 0), and 1 _− F_ 0( _t_ <u>)</u> Φ _n_ ( _t_ ) _→_ Φ( _t_ ) _≡ p_ 0 1 _− p_ 0 _F_ 0( _t_ )<sup>_._</sup> Let

= _Sn {j_ : _Tj,n > tn_ ( _α_ ) _}, tn_ ( _α_ ) = min _{t_ : Φ _n_ ( _t_ ) _≤ α}_ = _S_<sup>_′_</sup> _n {j_ : _Tj,n > t_ ( _α_ ) _}, t_ ( _α_ ) = min _{t_ : Φ( _t_ ) _≤ α}._ Under the above assumptions and that Φ is differentiable at _t_ ( _α_ ) with non-zero derivative, we have

_Pr_ ( _Sn_ = _Sn_<sup>_′_)</sup><sup>_→_1</sup><sup>_._</sup>

Page 110

We also have:


Since the left-hand side equals _α ∗ Pr_ ( _| Sn |>_ 0), this shows that in order to obtain asymptotic control of the FDR, it suffices to obtain a consistent estimator of Φ and thereby of _t_ ( _α_ ).

Let _p_ ˆ0, _F_<sup>ˆ</sup> _n_ and _F_<sup>ˆ</sup> 0 _,n_ be asymptotically consistent estimators of _p_ 0, _Fn_ (that is, _F_<sup>ˆ</sup> _n − Fn →_ 0), and _F_ 0, and let


be the corresponding consistent estimator of Φ( _t_ ). Let


be the corresponding consistent estimator of _t_ ( _α_ ).

Page 111

The proposed multiple testing procedure is now given by: _S_ ˆ _n ≡{j_ : _Tj,n >_ ˆ _tn_ ( _α_ ) _},_ and it asymptotically controls the FDR: lim sup = lim sup _n→∞_<sup>_E_</sup><sup>_<u>|</u>S_ˆ</sup><sup>_n ∩S_0</sup><sup>_<u>|</u>_</sup> _n→∞_<sup>_αP_(</sup><sup>_|S_ˆ</sup><sup>_n|>_0)</sup><sup>_._</sup> _| S_<sup>ˆ</sup> _n |_

Page 112

**Consistent Conservative Estimation of** _p_ 0 **.** Suppose we have consistent estimators _F_<sup>ˆ</sup> _n_ , _F_<sup>ˆ</sup> 0 _,n_ of _F_ , _F_ 0 available. We note that


for all _t < ∞_ . Thus, instead of using the upper bound _p_ 0 = 1, one can also consistently estimate _p_ 0 with


where _t_ is user supplied. Note, that for finite _n_ , the estimate _p_ ˆ0( _t_ ) of _p_ 0 will be (typically) conservative:


Page 113


<!-- Start of picture text -->
One might improve on this estimate by averaging a range of these<br>estimates over an interval [ a, b ]:<br>1<br>p ˆ0 ≡ p ˆ0( t ) dt.<br>b − a<br>� ab<br><!-- End of picture text -->

Page 114

**Estimation of Null and True Distribution of Test-Statistics Bootstrap:** Suppose _Tj,n_ = _Tj_ ( _X_ 1 _, . . . , Xn_ ), _j_ = 1 _, . . . , p_ , where _Xi_ , _i_ = 1 _, . . . , n_ , are i.i.d. observations from a data generating distribution _P_ . Let _Pn_ be the empirical distribution. We can estimate the distribution _Fj,n_ of _Tj,n_ with the distribution of are i.i.d. observations from the _Tj_ ( _X_ 1<sup>#</sup><sup>_, . . . , X_</sup> _n_<sup>#),where</sup><sup>_X_</sup> _i_<sup>#</sup> empirical distribution _Pn_ . The uniform mixture of these _p_ distributions _F_<sup>ˆ</sup> _j,n_ represents now an estimate of _Fn_ .

Similarly, we can use as an estimate of the asymptotic null distribution _F_ 0 the bootstrap distribution of null-value centered (and scaled) test-statistics: e.g., if _Tj,n_ =<sup>_√_</sup> _<u>n</u>_ <u>(</u> _µj,n − µj_ 0), then we estimate _F_ 0 with the distribution of<sup>_√_</sup> _<u>n</u>_ <u>(</u> _µ_<sup>#</sup> _j,n_<sup>_−µj,n_)(Pollard,van</sup> der Laan, 2003).

Page 115

**Nonparametric control of rate of expected false discoveries. Dependent mixture model** Let _⃗B_ = ( _B_ 1 _, . . . , Bm_ ) be a joint vector of bernoulli indicators _Bj_ = 1 _− I_ ( _H_ 0 _j_ True), and assume that the marginal distributions of _Bj_ is Bernoulli(1 _− p_ 0). Let _Qn|⃗B_ denote the joint conditional distribution of the vector of test-statistics, given _⃗B_ . Assume that the marginal distributions of _Qn|⃗B_ corresponding with the true null hypotheses _H_ 0 _j_ (i.e. _Bj_ = 0) equal a common known distribution _F_ 0 _,n_ , and that the other marginal distributions equal a common unknown distribution _F_ 1 _,n_ . For a dominating measure _µ_ , let _f_ 0<sup>_n≡dF_0</sup><sup>_,n/dµ_,and</sup><sup>_f_1</sup><sup>_,n≡dF_1</sup><sup>_,n/dµ_.Let</sup><sup>_Fn_=</sup><sup>_p_0</sup><sup>_F_0</sup><sup>_,n_+ 1</sup><sup>_−p_0</sup><sup>_F_1</sup><sup>_,n_,</sup> 1 _−F_ 0 _<u>,n</u>_ and Φ _n_ = _p_ 0 1 _−Fn_<sup>.Undertheabovedependentmixturemodel,we</sup> have the following result.

**Lemma:** Let _Sn ≡{j_ : _Tj_<sup>_n> tn_(</sup><sup>_α_)</sup><sup>_}_,where</sup> _tn_ ( _α_ ) _≡_ min _{t_ : Φ _n_ ( _t_ ) _≤ α}._

Page 116

Let _α_<sup>_∗_</sup> = Φ _n_ ( _tn_ ( _α_ )). Then (ratio of expected number of false discoveries, REFD)


**Proof:** Since _REFD_ only depends on the joint distribution of ( _⃗Bn,⃗Tn_ ) through its marginal distributions we have that we can replace its distribution _Qn_ by a distribution _Q_<sup>_∗_</sup> _n_<sup>withthesamebut</sup> independent marginals. Under this independence distribution _Q_<sup>_∗_</sup> _n_ we have


The conditional expectation of this quantaty, given the Bernoulli indicators _I_ ( _T_ 1<sup>_n> tn_(</sup><sup>_α_))</sup><sup>_, . . . , I_(</sup><sup>_T n_</sup> _p_<sup>_> tn_(</sup><sup>_α_)),equals</sup> � _I_ ( _Tj_<sup>_n> tn_(</sup><sup>_α_))Φ</sup><sup>_n_(</sup><sup>_tn_(</sup><sup>_α_)) =</sup><sup>_α∗_�</sup> _I_ ( _Tj_<sup>_n> tn_(</sup><sup>_α_))</sup><sup>_._</sup> _j j_

Page 117

This proves the statement.

Page 118

#### **Large** _p_ **case**

Suppose that the number of tests _p_ = _p_ ( _n_ ) converges to infinity if _n_ converges to infinity. In this case, it is reasonable to assume that


Consequently, under this assumption the multiple testing procedure _S_ ˆ _n_ which controls asymptotically the REFD at level _α_ will also control asymptotically the FDR at level _α_ . This teaches us that the multiple testing procedure _S_<sup>ˆ</sup> _n_ can be applied in many genomics applications in which the independence assumption is invalid, and still control the FDR well.

Page 119

**Data-adaptive Loss-based Estimation with Cross-validation**

**Sandrine Dudoit and Mark J. van der Laan** Division of Biostatistics, UC Berkeley `www.stat.berkeley.edu/~sandrine www.stat.berkeley.edu/~laan`

**PH243A – Fall 2003** Multivariate Statistical Methods in Genomics Version: Multivariate Statistical Methods in Genomics PH 243A, 2305 Tolman, MW 12-2 Fall 2003

_⃝_ c Copyright 2003, all rights reserved

#### **Acknowledgments**

Joint work with **S¨und¨uz Kele¸s** , Division of Biostatistics, UC Berkeley. **Annette Molinaro** , Division of Biostatistics, UC Berkeley. **Matthieu Cornec** , INSEE, France. _Thanks to Joe Gray, Dan Moore, and Fred Waldman (Comprehensive Cancer Center, UCSF) for providing the CGH breast cancer dataset._

Page 122

#### **Outline**

- Motivation: estimator construction, selection, and performance assessment in genomics.

- Estimation road map.

- Loss function.

- Estimator selection using cross-validation: finite sample results and asymptotic optimality.

- Estimator performance assessment using cross-validation: risk confidence intervals.

- Examples.

- Application 1: Likelihood cross-validation for the identification of regulatory motifs.

- Application 2: Tree-based prediction of survival based on microarray data.

Page 123


<!-- Start of picture text -->
transcription translation<br>Protein<br>DNA RNA<br>Sequencing Structure prediction Alignment<br>Assembly Splice site detection Phylogeny<br>Alignment Transcript levels Structure prediction<br>Annotation Functional pathways<br>Gene finding<br>TF binding site detection<br>Polymorphisms<br>Phylogeny<br>Biological/clinical<br>Biological<br>covariates and outcomes<br>metadata<br><!-- End of picture text -->

Page 124

#### **Motivation: Microarray experiments**

**Problem 1.** _Prediction of biological and clinical outcomes using microarray measures of transcript levels or DNA copy number._ Cells respond to various treatments/conditions by activating or repressing the expression of particular genes. DNA microarrays are high-throughput biological assays that can be used to measure gene expression levels on a genomic scale.

E.g. In cancer research, microarrays are used to measure transcript levels (i.e., mRNA levels) and DNA copy number in tumor samples for tens of thousands of genes at a time.

**Statistical question.** Relate microarray measures to biological and clinical outcomes.

Page 125

#### **Motivation: Microarray experiments**

- Outcomes <u>(phenotypes):</u> tumor class, response to treatment, patient survival, affectedness/unaffectedness

   - polychotomous or continuous; censored or uncensored.

- Explanatory variables <u>(genotypes):</u> measures of transcript (i.e., mRNA) levels for thousands of genes, DNA copy number for thousands of genes, age, sex, treatment, clinical predictors

   - polychotomous or continuous.

_Small n, large p._

Page 126

#### **Motivation: Microarray experiments**

- Selecting a _good_ predictor: linear discriminant analysis (LDA), trees, support vector machines (SVMs), neural networks, other?

- _•_ Selecting a _good_ subset of marker genes: How many genes? Which genes?

- Assessing the performance of the resulting predictor. _“Clinical outcome X for cancer Y can be predicted accurately based on gene expression measures.”_

Page 127

#### **Motivation: Sequence analysis**

**Problem 2.** _Identification of regulatory motifs in DNA sequences._ Transcription factors (TF) are proteins that selectively bind to DNA to regulate gene expression.

Transcription factor binding sites, or regulatory motifs, are short DNA sequences (5–25 base pairs) in the upstream control region (UCR) of genes, i.e., in regions roughly 600–1,000 base pairs from the gene start site (in lower eukaryotes such as yeast).

Page 128

#### **Motivation: Sequence analysis**

**E.g.** GAL4 binding sites for different yeast genes (from SCPD). `>YBR019C` TCGGCGATACCTTCACCG `>YBR020W` CGGGCGACGATTACCCG `>YLR081W` TATCGGAGCGTAGGCGGCCGAAC `>YML051W` CGGCATCCTACATGCCG `>YOR120W` TCGGTTCAGACAGGTCCGG

Page 129

#### **Motivation: Sequence analysis**

From unaligned DNA sequence data, estimate motif start sites and base composition, i.e., position specific weight matrix (PWM).

_•_ Likelihood estimation for DNA sequence data. E.g. Bailey & Elkan (1994), Kechris et al. (2002), Kele¸s et al. (2003b), Lawrence & Reilly (1990).

- Prediction of gene expression levels based on sequence features. E.g. Kele¸s et al. (2002).

- Selecting a _good_ model for transcription factor binding sites: Distribution of bases in motif? Distribution of bases in background sequence? Constraints on PWM? Motif length? Number of motifs per sequence?

- Assessing the performance of the resulting estimators.

Page 130

#### **Motivation: Genetic mapping**

**Problem 3.** _Identification of genes associated with complex phenotypes._

- Outcomes <u>(phenotypes):</u> affectedness/unaffectedness, quantitative trait, response to treatment, patient survival

   - polychotomous or continuous; censored or uncensored.

- Explanatory variables <u>(genotypes):</u> thousands of SNP genotypes, IBD status, age, sex — usually polychotomous.

Page 131

#### **General estimation road map**

Our proposed unified strategy for estimator construction, selection, and performance assessment is driven by the choice of a loss function corresponding to the parameter of interest for the full, uncensored data structure.

The term estimator is used in a broad sense, to provide a common treatment of multivariate outcome prediction and density estimation problems based on censored data. Each of these problems can be dealt with by the choice of a suitable loss function. **General framework** : van der Laan & Dudoit (2003). **Special cases and applications** : Dudoit & van der Laan (2003), Kele¸s et al. (2003a,2003b), van der Laan et al. (2003), Molinaro et al. (2003).

Page 132

#### **Estimation road map: Step 1**

**Step 1.** Definition of the parameter of interest in terms of a loss function for the observed data.

- Full, uncensored data: define the parameter of interest as the minimizer of the expected loss, or risk, for a loss function chosen to represent the desired measure of performance.

- Observed, censored data: apply the general estimating function methodology of van der Laan & Robins (2002) to map the full, uncensored data loss function into an observed, censored data loss function having the same expected value and leading to an efficient estimator of this risk based on censored data.

Page 133

#### **Estimation road map: Step 1**

#### Table 3: Examples of loss functions for different estimation problems.

|Estimation problem|Parameter|Loss function|
|---|---|---|
|Regression|Conditional mean of an<br>outcome given covariates|Squared error (L2)|
|Regression|Conditional median of an<br>outcome given covariates|Absolute error (L1)|
|Classification|Posterior class probabilities|Indicator, Gini,<br>negative log-likelihood|
|Density estimation|Density|Negative log-likelihood<br>(deviance, Kullback-Leibler)|


Page 134

#### **Estimation road map: Step 2**

**Step 2.** Construction of candidate estimators based on a loss function for the observed data.

- Generate a finite collection of candidate estimators for the parameter of interest based on a sieve of increasing dimension approximating the complete parameter space.

- For each element of the sieve, the candidate estimator is defined as the minimizer of the empirical risk based on the observed data loss function.

E.g. stepwise variable selection;

recursive binary partitioning of the covariate space in tree-based estimation;

addition/deletion/substitution algorithm (van der Laan & Dudoit, 2003; Sinisi & van der Laan, 2003).

Page 135

#### **Estimation road map: Step 3**

**Step 3.** Cross-validation estimator selection and performance assessment based on a loss function for the observed data.

Use cross-validation to estimate risk based on the observed data loss function and to select an optimal estimator among the candidates in **Step 2** .

van der Laan & Dudoit <u>(2003):</u> unified cross-validation methodology for selection among estimators, finite sample and asymptotic optimality results for the cross-validation selector for general data generating distributions, loss functions (possibly depending on a nuisance parameter), and estimators.

Page 136

#### **Full data structure**

The full data structure is defined as a multivariate stochastic process _X ≡ X_<sup>¯</sup> ( _T_ ) = _{X_ ( _t_ ) : 0 _≤ t ≤ T },_ where _T_ denotes a possibly random endpoint. _• W_ : time-independent, or baseline, covariates.

   - _Z ≡_ log _T_ : log survival time.

- _Z_ ( _t_ ), _t ∈{t_ 0 = 0 _, . . . , tm−_ 1 = _T }_ , _T_ fixed: an outcome process of interest, included in _X_ ( _t_ ).

- Denote the distribution of the full data structure _X_ by _FX,_ 0. In many applications, _X_ = ( _W, Z_ ).

Page 137

#### **Observed data structure**

The observed data structure is _O ≡ T_ ˜ = min( _T, C_ ) _,_ ∆= _I_ ( _T ≤ C_ ) _, X_ ¯ ( ˜ _T_ ) _,_ � � for a censoring variable _C_ with conditional distribution _G_ 0( _·|X_ ), given the full data structure _X_ .

By convention, if _T < C_ , let _C_ = _∞_ . One can then rewrite the observed data structure as _O_ = ( _X_<sup>¯</sup> ( _C_ ) _, C_ ). The distribution, _P_ 0 = _PFX,_ 0 _,G_ 0, of the observed data structure _O_ is indexed by the full data distribution _FX,_ 0 and the conditional distribution _G_ 0( _·|X_ ) of the censoring variable _C_ .

Page 138

#### **Observed data structure**

Coarsening at random (CAR) is assumed for the censoring mechanism _C Pr_ 0( _C_ = _t | C ≥ t, X_<sup>¯</sup> ( _T_ )) = _Pr_ 0( _C_ = _t | C ≥ t, X_<sup>¯</sup> ( _t_ )) _,_ for _t < T._ If _X_ does not include time-dependent covariates (e.g., _X_ = ( _W, Z_ )), then, under CAR, the censoring time _C_ is conditionally independent of the survival time _T_ , given baseline covariates _W_ .

Page 139

#### **Full data loss function**

The parameter of interest, _ψ_ 0, is a mapping, _ψ_ : _S →ℜ_ , from a covariate space _S_ into the real line _ℜ_ . Denote the parameter space by Ψ.

The parameter _ψ_ 0 is defined in terms of a loss function, _L_ ( _X, ψ_ ), as (one of) the minimizer(s) of the expected loss, or risk,

- _L_ ( _x, ψ_ 0) _dFX,_ 0( _x_ ) _≡_ min _L_ ( _x, ψ_ ) _dFX,_ 0( _x_ ) _._

- � _ψ∈_ Ψ �

Note that we do not require uniqueness of the risk minimizer, rather, we simply assume that there is a loss function such that the parameter of interest _ψ_ 0 achieves the minimum risk.

Page 140

#### **Full data loss function**

- **Univariate prediction** , _X_ = ( _W, Z_ ).

**–** Conditional mean: _ψ_ 0( _W_ ) = _E_ 0[ _Z | W_ ]. Quadratic ( _L_ 2), or squared error, loss function: _L_ ( _X, ψ_ ) = ( _Z − ψ_ ( _W_ ))<sup>2</sup> .

   - Conditional median: _ψ_ 0( _W_ ) = Median0[ _Z | W_ ]. Absolute error ( _L_ 1) loss function: _L_ ( _X, ψ_ ) = _|Z − ψ_ ( _W_ ) _|_ .

- **Multivariate prediction** , _X_ = ( _W,_ ( _Z_ ( _t_ 0) _, . . . , Z_ ( _tm−_ 1))). Conditional mean vector: _ψ_ 0( _t, W_ ) = _E_ 0[ _Z_ ( _t_ ) _| W_ ], _t ∈{t_ 0 = 0 _, . . . , tm−_ 1 = _T }_ . Quadratic loss function: For a symmetric matrix function Ω( _W_ ) _m×m_ , _L_ ( _X, ψ_ ) = ( _Z_ ( _·_ ) _− ψ_ ( _·, W_ ))<sup>_⊤_</sup> Ω( _W_ )( _Z_ ( _·_ ) _− ψ_ ( _·, W_ )).

- **Density estimation** , _X_ = ( _T, W_ ). Density: _ψ_ 0( _T, W_ ) = _f_ 0( _T, W_ ). Negative log-likelihood loss function: _L_ ( _X, ψ_ ) = _−_ log _ψ_ ( _T, W_ ).

Page 141

#### **Observed data loss function**

The general estimating function methodology of van der Laan & Robins (2002) maps the full data loss function _L_ ( _X, ψ_ ) into an observed data loss function _L_ ( _O, ψ | η_ 0) with the same risk

_L_ ( _o, ψ | η_ 0) _dP_ 0( _o_ ) = _L_ ( _x, ψ_ ) _dFX,_ 0( _x_ ) _._ <u>� �</u> � � � <u>��</u> � <u>��</u> Observed data Full data

Here, _η_ 0 denotes nuisance parameters _G_ 0 and possibly _Q_ 0, where _G_ 0 identifies the conditional distribution of the censoring variable _C_ given _X_ and _Q_ 0 = _Q_ ( _FX,_ 0) identifies the _FX_ -part of the observed data density under the CAR assumption.

Page 142

#### **IPCW loss function**

The inverse probability of censoring weighted (IPCW) loss function corresponding to the full data loss function _L_ ( _X, ψ_ ) is ∆ _L_ ( _O, ψ | G_ ) _≡ L_ ( _X, ψ_ ) _G_ <u>¯(</u> _T |X_ )<sup>_,_</sup>

where _G_<sup>¯</sup> is a conditional survival function for _C_ given _X_ and ∆= _I_ ( _T ≤ C_ ) is the censoring indicator. Under CAR, _G_<sup>¯</sup> ( _T |X_ ) = _G_<sup>¯</sup> ( _T |W_ ).

Page 143

#### **IPCW loss function**

In regression, _X_ = ( _W, Z_ ) and the parameter of interest is the conditional mean: _ψ_ 0( _W_ ) = _E_ 0[ _Z | W_ ]. Full data loss function: _L_ ( _X, ψ_ ) = ( _Z − ψ_ ( _W_ ))<sup>2</sup> _._ IPCW observed data loss function: ∆ _L_ ( _O, ψ | G_ ) = ( _Z − ψ_ ( _W_ ))<sup>2</sup> _G_ <u>¯(</u> _T |W_ )<sup>_._</sup>

Page 144

#### **DR-IPCW loss function**

The doubly robust inverse probability of censoring weighted (DR-IPCW) loss function is


<!-- Start of picture text -->
L ( O, ψ | Q, G )<br>≡ L ( X, ψ )∆ +<br>EG,Q dMG ( u ) ,<br>G ¯( T |X ) � � LG ¯( X ( T, |ψX )∆) | X ¯ ( u ) , T ˜ ≥ u �<br>where<br>dMG ( u ) =  I (  T ˜ ∈ du,  ∆= 0)  − I (  T ˜ ≥ u ) λc ( u|X ) du<br>and Q  =  Q ( FX ) refers to the FX -part of the density for the<br>observed data, O = (  X ¯ ( C ) , C ), under the CAR assumption.<br><!-- End of picture text -->

Page 145

**DR-IPCW loss function** Double robustness: The loss functions satisfy _L_ ( _o, ψ | Q, G_ ) _dP_ 0( _o_ ) = _L_ ( _x, ψ_ ) _dFX,_ 0( _x_ ) _,_ � � if either _G_ = _G_ 0 or _Q_ = _Q_ 0.

Page 146

#### **The estimator selection problem**

_•_ Suppose we have a learning set of _n_ independent and identically distributed (i.i.d.) observations, _O_ 1 _, . . . , On_ , with _Oi ∼ P_ 0. Let _Pn_ be the empirical distribution of _O_ 1 _, . . . , On_ . _•_ Let _ψ_<sup>ˆ</sup> _k_ ( _·_ ) = _ψk_ ( _· | Pn_ ) _∈_ Ψ, _k_ = 1 _, . . . , Kn_ , be a collection of candidate estimators of the parameter _ψ_ 0( _·_ ). E.g. In tree-based estimation, the _ψ_<sup>ˆ</sup> _k_ are obtained by recursive binary partitioning of the covariate space using one of the above observed data loss functions; _k_ corresponds to tree size.

Page 147

**The estimator selection problem**

The selection problem. Choose a data adaptive _k_<sup>ˆ</sup> = _k_ ( _Pn_ ) so that the distance, or risk difference, _≡ dn_ ( _ψ_<sup>ˆ</sup> _k_ ˆ _, ψ_ 0) _L_ ( _o, ψ_<sup>ˆ</sup> _k_ ˆ _| η_ 0) _− L_ ( _o, ψ_ 0 _| η_ 0) _dP_ 0( _o_ ) � �� (observed data loss function) = _L_ ( _x, ψ_<sup>ˆ</sup> _k_ ˆ) _− L_ ( _x, ψ_ 0) _dFX,_ 0( _x_ ) � �� (full data loss function) _−→_ 0 at asymptotically optimal rate _._

Page 148

#### **The estimator selection problem**

- For the squared error loss function, _L_ ( _X, ψ_ ) = _L_ 2( _X, ψ_ ) = ( _Z − ψ_ ( _W_ ))<sup>2</sup> , the risk difference simplifies to


Page 149

#### **The estimator selection problem**

The optimal benchmark selector. Let

_≡ k_ ˜ _n_ argmin _k dn_ ( _ψ_<sup>ˆ</sup> _k, ψ_ 0)

denote the minimizer of the distance _dn_ ( _ψ_<sup>ˆ</sup> _k, ψ_ 0). This optimal benchmark selector depends on the unknown data generating distribution _P_ 0.

A selector _k_<sup>ˆ</sup> = _k_ ( _Pn_ ) is asymptotically equivalent with the optimal benchmark _k_<sup>˜</sup> _n_ if


In particular, then it is asymptotically optimal.

van der Laan & Dudoit <u>(2003):</u> finite sample and asymptotic optimality results for the cross-validation selector.

Page 150

**The estimator selection problem**

The selection problem involves estimating the conditional risk _θ_ ˜ _n_ ( _k_ ) _≡ L_ ( _o, ψk_ ( _· | Pn_ ) _| η_ 0) _dP_ 0( _o_ ) � for each candidate estimator _ψ_<sup>ˆ</sup> _k_ ( _·_ ) = _ψk_ ( _· | Pn_ ) _∈_ Ψ, _k_ = 1 _, . . . , Kn_ . Cross-validation is a general approach for risk estimation and estimator selection.

Page 151

#### **General framework for cross-validation**

The main idea in cross-validation (CV) is to divide the available learning set into two sets: a training set and a validation set. Observations in the training set are used to compute (or _train_ ) the estimator(s) and the validation set is used to assess the performance of (or _validate_ ) this estimator(s).

The cross-validation estimator _ψ_<sup>ˆ</sup> _k_ ˆ is chosen to have the best performance on the validation set.

Page 152

#### **General framework for cross-validation**

To derive a general representation for the cross-validation selector _k_ ˆ, we introduce a binary random _n_ -vector, or split vector, _Sn ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> , independent of the empirical distribution _Pn_ .

- A realization of _Sn_ = ( _Sn,_ 1 _, . . . , Sn,n_ ) defines a particular split of the learning sample of _n_ observations into a training set and validation set

   - 0 _, i_ th observation is in the training sample,

   - _Sn,i_ =  1 _, i_ th observation is in the validation sample.

   -

- The particular distribution of _Sn_ defines the type of cross-validation procedure.

Page 153

#### **General framework for cross-validation**

Let _Pn,S_<sup>0</sup> _n_<sup>and</sup><sup>_P_</sup> _n,S_<sup>1</sup> _n_<sup>denotetheempiricaldistributionsofthe</sup> training and validation sets, respectively, and let _p_ = _pn_ = _n_ 1 _/n_ be the proportion of observations in the validation set.

A general definition of the cross-validation selector is


Here, _ψk_ ( _· | Pn,S_<sup>0</sup> _n_<sup>)and</sup><sup>_η_</sup> _n,S_<sup>0</sup> _n_<sup>denote,respectively,estimatorsfor</sup> the parameter of interest _ψ_ 0 and the nuisance parameter _η_ 0, using only the training set.

Page 154

#### **General framework for cross-validation**


<!-- Start of picture text -->
Training set Validation set<br>Compute estimator Assess performance<br><!-- End of picture text -->

Figure 1: _Five-fold cross-validation. Sn_ has 5 realizations.

Page 155

#### **General framework for cross-validation**

The particular distribution of the split vector _Sn_ defines the type of cross-validation procedure. This representation covers many types of CV procedures.

- Leave-one-out cross-validation (LOOCV). Each observation in the learning set is used in turn as the validation set and the remaining _n −_ 1 observations are used as the training set. The corresponding distribution of _Sn_ places mass 1 _/n_ on each the _n_ binary vectors _sn_ = ( _sn,_ 1 _, . . . , sn,n_ ) such that<sup>�</sup> _i_<sup>_sn,i_= 1(</sup><sup>_pn_= 1</sup><sup>_/n_).</sup>

_• V_ -fold cross-validation. The learning set is randomly divided into _V_ mutually exclusive and exhaustive sets, each used in turn as the validation sets. The corresponding distribution of _Sn_ places mass 1 _/V_ on each of _V_ binary vectors _sn_<sup>_v_= (</sup><sup>_sv_</sup> _n,_ 1<sup>_, . . . , sv_</sup> _n,n_<sup>),</sup><sup>_v_= 1</sup><sup>_, . . . , V_,</sup> such that<sup>�</sup> _i_<sup>_sv_</sup> _n,i_<sup>_≈n/V_and�</sup> _v_<sup>_sv_</sup> _n,i_<sup>= 1(</sup><sup>_pn_= 1</sup><sup>_/V_).</sup>

Page 156

#### **General framework for cross-validation**

_•_ Monte Carlo cross-validation. The learning set is repeatedly and randomly divided into two sets, a training set of _n_ 0 = _n_ (1 _− p_ ) observations and a validation set of _n_ 1 = _np_ observations. The split vectors _Sn_ are drawn at random with replacement from a distribution that places mass 1 _/_ � _nn_ 1� on each binary vector such that � _i_<sup>_sn,i_=</sup><sup>_n_1.</sup> _•_ Bootstrap-based cross-validation. The training sets are based on bootstrap samples and the validation sets on the corresponding left-out samples. _E_ [ _pn_ ] = _E_ [<sup>�</sup> _i_<sup>_Sn,i/n_] = (1</sup><sup>_−_1</sup><sup>_/n_)</sup><sup>_n≈e−_1</sup><sup>_≈._368.</sup> E.g. _.632 bootstrap estimator_ (Efron, 83).

Page 157

#### **Honest cross-validation**

Prediction error rates, or related measures, are usually reported to

- compare the performance of different predictors;

- support statements such as _“Clinical outcome X for cancer Y can be predicted accurately based on microarray gene expression measures.”_

Page 158

#### **Honest cross-validation**

It is common practice in microarray experiments to screen genes and fine-tune predictor parameters (e.g., number of neighbors _k_ in nearest neighbor classification, kernel in SVMs) using all the learning set and then perform cross-validation only on the predictor building portion of the process.

- = _⇒_ The reported error rates are usually biased downward and give an overly optimistic view of the predictive power of microarray expression measures.

- = _⇒_ Predictors are not compared on an equal footing.

Page 159

#### **Honest cross-validation**

Prediction error rates (risk) can estimated by cross-validation (CV), BUT ...

- These estimates relate only to the experiment that was cross-validated.

- It is essential to perform cross-validation on the entire predictor training process, including feature selection and other training decisions (e.g., choice for the number of neighbors in _k_ -NN, kernel in SVMs).

- Otherwise, risk estimates can be severely biased downward, i.e., overly optimistic.

**Ref.** Ambroise & McLachlan (2002), Dudoit & Fridlyand (2003), West et al. (2001).

Page 160

#### **Honest cross-validation**

**Resubstitution estimation.** The entire learning set is used to perform feature selection, build the classifier, and estimate classification error.

**Internal cross-validation.** Feature selection is done on the entire learning set, CV is applied only to the classifier building process. **External cross-validation.** CV is applied to the feature selection AND the classifier building process.

Page 161

#### **Honest cross-validation**


<!-- Start of picture text -->
DLDA − classification error, out of 49 1−NN − classification error, out of 49<br>Resubstitution<br>Internal LOOCV<br>External LOOCV<br>Resubstitution<br>Internal LOOCV<br>External LOOCV<br>1.0 1.5 2.0 2.5 3.0 3.5 1.0 1.5 2.0 2.5 3.0 3.5<br>log10(G) log10(G)<br>25<br>20<br>15<br>15<br>Error Error<br>10<br>10<br>5<br>5<br>0<br><!-- End of picture text -->

#### (a) DLDA


<!-- Start of picture text -->
(b) 1– NN<br><!-- End of picture text -->

Figure 2: _Estimates of classification error by leave-one-out crossvalidation._ Breast tumor nodal dataset, 25 nodal+ and 24 nodal– tumors (West et al., 2001).

Page 162

#### **Estimator selection using cross-validation**

Define the distance, or risk difference, for estimators based on training samples of size _n_ (1 _− p_ ) as _dn_ (1 _−p_ )( _ψ_<sup>ˆ</sup> _k, ψ_ 0) _≡ ESn L_ ( _o, ψk_ ( _· | Pn,S_<sup>0</sup> _n_<sup>)</sup><sup>_| η_</sup> 0<sup>)</sup><sup>_−L_(</sup><sup>_o, ψ_</sup> 0<sup>(</sup><sup>_·_)</sup><sup>_| η_</sup> 0<sup>)</sup> � _dP_ 0( _o_ ) _._ �� The selector _k_<sup>ˆ</sup> aims to minimize this unknown distance.

Denote the unknown minimizer, i.e., the comparable optimal benchmark selector for _n_ (1 _− p_ ) observations by _k_ ˜ _n_ (1 _−p_ ) _≡_ argmin _k dn_ (1 _−p_ )( ˆ _ψk, ψ_ 0) _._

Page 163

#### **Estimator selection using cross-validation**

**<u>Theorem 1.</u>** (Stated in special case of known _η_ 0, _L_ ( _O, ψ | η_ 0) = _L_ ( _O, ψ_ )). Suppose that

**A1.** the loss function _L_ ( _O, ψ_ ) is uniformly bounded by _M_ 1, and **A2.** there exists an 0 _≤ M_ 2 _< ∞_ so that for all _k_

_L_ ( _o, ψk_ ( _· | Pn,S_<sup>0</sup> _n_<sup>))</sup><sup>_−L_(</sup><sup>_o, ψ_0(</sup><sup>_·_))</sup> �2 _dP_ 0( _o_ ) �� _≤ M_ 2 _L_ ( _o, ψk_ ( _· | Pn,S_<sup>0</sup> _n_<sup>))</sup><sup>_−L_(</sup><sup>_o, ψ_0(</sup><sup>_·_))</sup> � _dP_ 0( _o_ ) a.s. ��

**Finite sample result.** For any _δ >_ 0 and constant _C_ ( _M_ 1 _, M_ 2 _, δ_ ) _≤_ 0 _≤ Edn_ (1 _−p_ )( _ψ_<sup>ˆ</sup> _k_ ˆ _, ψ_ 0) (1 + 2 _δ_ ) _Edn_ (1 _−p_ )( _ψ_<sup>ˆ</sup> _k_ ˜ _n_ (1 _−p_ ) _, ψ_ 0) _._ + _C_ ( _M_ 1 _, M_ 2 _, δ_ )<sup>1 + log(</sup><sup>_Kn_</sup><sup><u>)</u></sup> _np_

Page 164

#### **Estimator selection using cross-validation**


<!-- Start of picture text -->
Asymptotic optimality. If<br>log( Kn )<br>−→ 0 , as n →∞,<br>( np )  Edn (1 −p )(  ψ ˆ k ˜ n (1 −p ) , ψ 0)<br>then<br>Edn (1 −p )( ψ ˆ k ˆ , ψ 0)<br>as n →∞.<br>−→ 1 ,<br>Edn (1 −p )(  ψ ˆ k ˜ n (1 −p ) , ψ 0)<br><!-- End of picture text -->

Page 165

#### **Estimator selection using cross-validation**


<!-- Start of picture text -->
Corollary. In addition to the conditions of Theorem 1, suppose<br>that, as n →∞ , p  =  pn → 0 slowly enough that<br>log( Kn )<br>−→ 0 ,<br>( np )  Edn (1 −p )(  ψ ˆ k ˜ n (1 −p ) , ψ 0)<br>and<br>Edn (  ψ ˆ k ˜ n, ψ 0)<br>−→ 1 .<br>Edn (1 −p )(  ψ ˆ k ˜ n (1 −p ) , ψ 0)<br>Then,<br>Edn (1 −p )( ψ ˆ k ˆ , ψ 0)<br>as n →∞.<br>−→ 1 ,<br>Edn (  ψ ˆ k ˜ n, ψ 0)<br>That is, the data adaptive CV selector k ˆ is asymptotically optimal.<br><!-- End of picture text -->

Page 166

#### **Estimator selection using cross-validation**

- The corresponding convergence in probability of the ratios of risk differences follows by noting that _E|Zn|_ = _O_ ( _g_ ( _n_ )) implies _Zn_ = _OP_ ( _g_ ( _n_ )), for a positive function _g_ ( _n_ ) .

- A more general version of Theorem 1 was derived for loss functions that depend on a nuisance parameter _η_ 0.

- An analog of Theorem 1, which does not require Assumption A2, was derived. In this case, convergence is shown to be _O_ (log( _Kn_ ) _/_<sup>_√_</sup> _<u>np</u>_ ) rather than _O_ (log( _Kn_ ) _/np_ ).

van der Laan & Dudoit (2003)

Page 167

#### **Estimator selection using cross-validation**

- Both theorems consider general distributions of _Sn_ , i.e., general cross-validation procedures with an arbitrary proportion _pn_ of observations included the validation sets.

- The finite sample results hold for any _pn_ , while the asymptotic results require that _npn →∞_ ; the later condition rules out LOOCV.

- The theorems apply to general distributions _P_ 0, general loss functions _L_ ( _O, ψ | η_ 0), and general estimators _ψ_ ( _· | Pn_ ).

Page 168

#### **Estimator performance assessment**

Consider a particular estimator _ψ_<sup>ˆ</sup> ( _·_ ) = _ψ_ ( _· | Pn_ ) and loss function _L_ ( _O, ψ | η_ 0) = _L_ ( _O, ψ_ ) with known _η_ 0. Cross-validation risk estimator (observable random variable)


Conditional risk, _n_ (1 _− p_ ) observations (unknown random variable) _θ_ ˜ _n_ (1 _−p_ ) _≡ ESn L_ ( _o, ψ_ ( _· | Pn,S_<sup>0</sup> _n_<sup>))</sup><sup>_dP_</sup> 0<sup>(</sup><sup>_o_)</sup><sup>_._</sup> � Conditional risk, _n_ observations (unknown random variable) _θ_ ˜ _n ≡ L_ ( _o, ψ_ ( _· | Pn_ )) _dP_ 0( _o_ ) _._ �

Asymptotic risk (unknown parameter)

_θ ≡ L_ ( _o, ψ_ ( _· | P_ 0)) _dP_ 0( _o_ ) _._ �

Page 169

#### **Asymptotic linearity of CV risk estimator**


<!-- Start of picture text -->
Theorem. Suppose the loss function L ( O, ψ ) is uniformly bounded<br>by M 1 and<br>�<br>�<br>� L ( o, ψ ( · | Pn,S 0 n ))  − L ( o, ψ ( · | P 0)) dP 0( o )<br>� � �2<br>ESn =  oP  (1) .<br>� pn<br>Then<br>n<br>θ ˆ n (1 −p )  − θ ˜ n (1 −p ) = 1 � {L ( Oi, ψ ( · | P 0))  − θ}  +  oP  (1 / √ n ) .<br>n<br>i =1<br><!-- End of picture text -->

Page 170

#### **Risk confidence intervals**

An approximate asymptotic (1 _− α_ )100% confidence interval for the conditional risk _θ_<sup>˜</sup> _n_ (1 _−p_ ) is given by

_σ_ ˆ _n θ_ ˆ _n_ (1 _−p_ ) _± z_ 1 _−α/_ 2 _~~√~~_ _<u>n</u>_<sup>_,_</sup> where _σ_ ˆ _n_<sup>2=</sup> ( _IC_ ( _o | Pn_ ))<sup>2</sup> _dPn_ ( _o_ ) _,_ � _IC_ ( _o | Pn_ ) = _L_ ( _o, ψ_ ( _· | Pn_ )) _− L_ ( _o, ψ_ ( _· | Pn_ )) _dPn_ ( _o_ ) _,_ � and Φ( _zα/_ 2) = 1 _− α/_ 2 for the standard normal cumulative distribution function Φ( _·_ ).

Page 171

#### **Simulation study: Consistency and asymptotic linearity**


<!-- Start of picture text -->
2−classes−Model1−10−foldCrossValidation−lda 2−classes−Model1−10−foldCrossValidation−rpart<br>100 200 500 1000 2000 5000 100 200 500 1000 2000 5000<br>size of learning set size of learning set<br>2−classes−Model1−2−foldCrossValidation−lda 2−classes−Model1−2−foldCrossValidation−rpart<br>100 200 500 1000 2000 5000 100 200 500 1000 2000 5000<br>size of learning set size of learning set<br>0.10<br>0.10<br>0.05 0.05<br>0.00<br>0.00<br>thetahapp−thetatildep thetahapp−thetatildep −0.05<br>−0.05<br>−0.10<br>−0.10 −0.15<br>0.10<br>0.10<br>0.05<br>0.05<br>0.00 0.00<br>thetahapp−thetatildep thetahapp−thetatildep<br>−0.05 −0.05<br>−0.10 −0.10<br><!-- End of picture text -->

Figure 3: _Convergence to zero of θ_<sup>ˆ</sup> _n_ (1 _−p_ ) _− θ_<sup>˜</sup> _n_ (1 _−p_ ) _. X|Y ∼_ N( _Y_ 12 _, I_ 2), _Y ∼_ B(1 _/_ 2), LDA, rpart, two- and ten-fold CV, 200 simulations.

Page 172

#### **Simulation study: Risk confidence intervals**


<!-- Start of picture text -->
failure−benchmark%= failure−benchmark%=<br>7.5 7.5<br>failure−conditionnal−risk%= failure−conditionnal−risk%=<br>18 24<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>2−classes−Model1−10−foldCrossValidation−lda−learning−size= 100 2−classes−Model1−10−foldCrossValidation−lda−learning−size= 200<br>failure−benchmark%= failure−benchmark%=<br>6.5 6<br>failure−conditionnal−risk%= failure−conditionnal−risk%=<br>24.5 30.5<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>2−classes−Model1−10−foldCrossValidation−lda−learning−size= 500 2−classes−Model1−10−foldCrossValidation−lda−learning−size= 1000<br>50 50<br>40 40<br>30 30<br>5 5<br>20 20<br>10 10<br>0 0<br>50 50<br>40 40<br>30 30<br>5 5<br>20 20<br>10 10<br>0 0<br><!-- End of picture text -->

Figure 4: _Risk confidence intervals. X|Y ∼_ N( _Y_ 12 _, I_ 2), _Y ∼_ B(1 _/_ 2), _n_ = 100 _,_ 200 _,_ 500 _,_ 1000, LDA, ten-fold CV, _θ_<sup>˜</sup> _n_ (1 _−p_ ) and _θ_<sup>˜</sup> _n_ .

Page 173

#### **Applications of estimation road map**

The above results hold for general cross-validation procedures and apply to general distributions _P_ 0, general loss functions _L_ ( _O, ψ | η_ 0), and general estimators _ψ_ ( _· | Pn_ ). The following problems can be addressed within our general estimation framework by choosing a suitable loss function.

1. Prediction of polychotomous and continuous outcomes.

2. Density estimation.

3. Predictor based on right-censored outcomes.

4. Survival function estimation.

5. Prediction of multivariate outcomes.

6. Counterfactual prediction in causal inference.

van der Laan & Dudoit (2003)

Page 174

#### **Example 1: Predictor selection**

Suppose we have a learning set of _n_ i.i.d. observations _O_ = ( _W, Z_ ) _∼ P_ 0, where _Z_ is an outcome of interest and _W_ a vector of explanatory variables.

Consider the quadratic loss function _L_ ( _O, ψ_ ) = ( _Z − ψ_ ( _W_ ))<sup>2</sup> _._

The parameter of interest, which minimizes the risk _E_ 0[ _L_ ( _O, ψ_ )] = ( _z − ψ_ ( _w_ ))<sup>2</sup> _dP_ 0( _o_ ) _,_ � is the conditional expectation _ψ_ 0( _W_ ) = _E_ 0[ _Z | W_ ].

Page 175

#### **Example 1: Predictor selection**

Given candidate predictors _ψ_<sup>ˆ</sup> _k_ = _ψk_ ( _· | Pn_ ), the risk difference for the quadratic loss simplifies to _dn_ ( _ψ_<sup>ˆ</sup> _k, ψ_ 0) = ( _ψk_ ( _w | Pn_ ) _− ψ_ 0( _w_ ))<sup>2</sup> _dFW,_ 0( _w_ ) _._ �

The cross-validation selector is given by


Page 176

#### **Example 1: Predictor selection**

Prediction of biological and clinical outcomes using microarray gene expression measures or SNP marker genotypes.

- Outcomes <u>(phenotypes),</u> _Z_ : tumor class, response to treatment, patient survival, affectedness/unaffectedness — polychotomous or continuous; censored (see Example 3, below) or uncensored.

- Explanatory variables <u>(genotypes),</u> _W_ : measures of transcript (i.e., mRNA) levels for thousands of genes, DNA copy number for thousands of genes, SNP haplotypes, age, sex, treatment, clinical predictors

   - polychotomous or continuous.

Page 177

#### **Example 1: Predictor selection**

Prediction of gene expression levels using DNA sequence data to identify transcription factor binding sites.


<!-- Start of picture text -->
Gene<br>...ACGTACACGTAAACGTTACTGTAATTTACGTGGACAAA......<br>Expression<br>Motif A Motif B Motif C<br><!-- End of picture text -->

- Outcomes <u>(phenotypes),</u> _Z_ : microarray gene expression measures — multivariate outcomes.

- Explanatory variables <u>(genotypes),</u> _W_ : DNA sequence in upstream control region of genes.

Kele¸s et al. (2002). _Bioinformatics_ .

Page 178

#### **Example 2: Density estimator selection**

Suppose we have a learning set of _n_ i.i.d. observations _O ∼ f_ 0 _≡_<sup>_<u>dP</u>_</sup><sup><u>0</u></sup> _dµ_<sup>.Considerthelog-likelihoodlossfunction(a.k.a.</sup> cross-entropy loss, deviance)

_L_ ( _O, f_ ) = _−_ log( _f_ ( _O_ )) _._

The parameter of interest, which minimizes the risk _E_ 0[ _−L_ ( _O, f_ )] = _−_ log _f_ ( _o_ ) _f_ 0( _o_ ) _dµ_ ( _o_ ) _,_ � is the density itself, _ψ_ 0 = _f_ 0.

Page 179

#### **Example 2: Density estimator selection**

Given candidate density estimators, _ψ_<sup>ˆ</sup> _k_ = _fk_ ( _· | Pn_ ), of _ψ_ 0 = _f_ 0, the risk difference is the Kullback-Leibler divergence between _fk_ ( _· | Pn_ ) and _f_ 0


The cross-validation selector is given by


Page 180

#### **Example 2: Density estimator selection**

Consider the special case when _O_ = ( _W, Z_ ), with _Z|W ∼_ N( _ψ_ 0( _W_ ) _, σ_<sup>2</sup> ), _ψ_ 0( _W_ ) = _E_ 0[ _Z|W_ ], and known variance _σ_<sup>2</sup> . The conditional density of _Z_ given _W_ , corresponding to a candidate estimator _ψk_ ( _·|Pn_ ), is denoted by _fk_ ( _z_ ; _w | Pn_ ).


Page 181

#### **Example 2: Density estimator selection**

Likelihood-based cross-validation for bandwidth selection in kernel density estimation.

- The true density _f_ 0 is standard normal with compact support in the interval [ _−_ 2 _,_ 2].

- _B_ = 20 replicate datasets were generated from _f_ 0 for six different sample sizes, _n_ =50, 100, 200, 400, 800, 1600.

- The Gaussian kernel density estimator, _f_<sup>ˆ</sup> _k_ ( _·_ ) = _fk_ ( _· | Pn_ ), for a learning set _x_ 1 _, · · · , xn_ is given by


where _φ_ ( _._ ) is the standard normal density function and _k_ is the bandwidth. _Kn_ = 100 different bandwidth values _k_ were considered from the interval [0 _._ 02 _,_ 2], so that the difference between any two consecutive bandwidth values is 0.02.

Page 182

#### **Example 2: Density estimator selection**


<!-- Start of picture text -->
0 500 1000 1500<br>sample size<br>3.0<br>2.5<br>ratio<br>2.0<br>1.5<br>1.0<br><!-- End of picture text -->

_dn_ <u>(1</u> _−p_ <u>)(</u> _ψ_<sup>ˆ</sup> _<u>k</u>_ ˆ _,ψ_ 0) Figure 5: _dn_ (1 _−p_ )(<sup>ˆ</sup> _ψkn_ ˜ (1 _−p_ ) _,ψ_ 0)<sup>_vs.n,forp_=1</sup><sup>_/_10.Thebandwidth</sup><sup>_k_ˆ</sup> was selected using ten-fold CV ( _p_ = 1 _/_ 10), for 20 replicate datasets at each of six sample sizes, _n_ .

Page 183

#### **Example 2: Density estimator selection**


<!-- Start of picture text -->
n<br>50 100 200 400 800 1600<br>1.542497 1.400015 1.150882 1.139386 1.068780 1.033064<br><!-- End of picture text -->

_Ed_ ˆ _n_ <u>(1</u> _−p_ <u>)(</u> _ψ_<sup>ˆ</sup> _<u>k</u>_ ˆ _,ψ_ 0) Table 4: ˆ _Edn_ (1 _−p_ )(<sup>ˆ</sup> _ψkn_ ˜ (1 _−p_ ) _,ψ_ 0)<sup>_vs.n,forp_=1</sup><sup>_/_10</sup><sup>_._Theestimated</sup> distance ratios are based on 20 replicate datasets at each of the six different sample sizes _n_ . The bandwidth _k_<sup>ˆ</sup> was selected using ten-fold CV ( _p_ = 1 _/_ 10).

Page 184

#### **Example 2: Density estimator selection**


<!-- Start of picture text -->
n = 50 Bandwidth = 0.3 n = 200 Bandwidth = 0.18 n = 800 Bandwidth = 0.16<br>+ True<br>++****** ++++++++++++++++++++++++++++++++++++++++***************** *******************************************************************************+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ * ************************* Estimated +++++++++++++++++++++++++++++++++++++++++++++++++++++ ********************************** ********************************* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++********************************************************************************* +++++++++++++++++++++++++++++++++++++++++****************************** ********++++++ ++******* ++++++++++++++++++++++++++++++++++++++++++++++++********************* ***********************************************************************************+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ****************+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ******************************* ****** ***************************** **************************************** +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++******************************************* +++++++++++++++++++++++++++++++++++++++++++++++++************************************* ******+ ++************ ++++++++++++++++++++++++++++++++++++++++******************************************** ****************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ **** ************************************************************ *****************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ *************************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ *********************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ *******************<br>−2 −1 0 1 2 −2 −1 0 1 2 −2 −1 0 1 2<br>x x x<br>n = 100 Bandwidth = 0.22 n = 400 Bandwidth = 0.22 n = 1600 Bandwidth = 0.2<br>+***** ++++++++++++++++++++++++++++++++++++************ **************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ *********************++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ************************* ****************** ** * *** ************************* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++******** *********** ******************************************************* +++++++++++++++++++++++++++++++++++++*************** ********************************** ************** ++++++++++**** ++******** ++++++++++++++++++++++++++++++++++++++++++********************* *************************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ *******************************************************+++++++++++++++++++++++++++++++++++++++++++++ *******************************+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ *********** **************************************************************** +++++++++++++++++++++++++++++++++++++++++++************************************* *******++ ++**************** ++++++++++++++++++++++++++++++++++++++++********************************** ***********************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ * ********************************************************************************* **************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ***********************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ************ *********************************************** +++++++++++++++++++++++++++++++++++++++++********************************<br>−2 −1 0 1 2 −2 −1 0 1 2 −2 −1 0 1 2<br>x x x<br>0.4<br>0.4<br>0.4<br>0.3 0.3<br>0.3<br>f(x) 0.2 f(x) f(x) 0.2<br>0.2<br>0.1 0.1 0.1<br>0.0 0.0 0.0<br>0.4 0.4 0.4<br>0.3 0.3 0.3<br>f(x) 0.2 f(x) 0.2 f(x) 0.2<br>0.1 0.1 0.1<br>0.0 0.0 0.0<br><!-- End of picture text -->

- **++**************<sup>**++++++++++++++++++++++++++++++++++++++++**************************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</sup><sup>***********************************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++***************************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</sup><sup>***********************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++**********************************</sup> ********++**

- **++******************<sup>**++++++++++++++++++++++++++++++++++++++++***********************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</sup><sup>**************************************************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++*************************************************************************************++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++</sup><sup>*************************************************************+++++++++++++++++++++++++++++++++++++++++**********************************</sup> *********+** +

Figure 6: _Cross-validation density estimates f_<sup>ˆ</sup> _k_ ˆ _and true density f_ 0 _._ The cross-validation kernel density estimate _fk_ ˆ( _· | Pn_ ) is shown for six sample sizes, _n_ = 50, 100, 200, 400, 800, 1600, for one simulated dataset. The bandwidth _k_<sup>ˆ</sup> was selected using ten-fold CV ( _p_ = 1 _/_ 10).

Page 185

#### **Example 2: Density estimator selection**

### _n_

||50|100|200|400|800|1600|
|---|---|---|---|---|---|---|
|0.05|1.493594|1.465201|1.168274|1.115338|1.089441|1.047685|
|0.1|1.531736|1.391971|1.144236|1.136916|1.075563|1.048454|
|0.15|1.577241|1.473550|1.118831|1.117599|1.076197|1.061919|
|0.20|1.518429|1.417260|1.120498|1.100698|1.065835|1.064060|
|0.25|1.302580|1.443560|1.111674|1.182325|1.060759|1.100572|
|_p_<br>0.30|1.430726|1.388704|1.148916|1.119423|1.080356|1.083632|
|0.35|1.238741|1.414966|1.076628|1.093445|1.092477|1.112602|
|0.40|1.477980|1.617694|1.200306|1.123990|1.091412|1.091008|
|0.45|1.411283|1.483116|1.090528|1.142125|1.134810|1.143657|
|0.50|1.320979|1.398095|1.099359|1.136470|1.146952|1.167325|


_Ed_ ˆ _n_ ( _ψ_<sup>ˆ</sup> _k_ ˆ( _<u>p</u>_ <u>)</u> _,ψ_ 0) ˆ Table 5: _V -fold likelihood cross-validation: vs. n and p. Edn_ ( _ψ_<sup>ˆ</sup> _kn_ ˜ _,ψ_ 0) Estimated distance ratios are based on 20 replicate datasets at six different sample sizes _n_ and for ten different validation set proportions _p_ = 1 _/V_ .

Page 186

#### **Example 2: Density estimator selection**

### _n_

||50|100|200|400|800|1600|
|---|---|---|---|---|---|---|
|0.05|21.778985|30.591547|5.366258|3.488738|2.147304|1.287172|
|0.1|4.969151|8.139912|3.709904|2.105173|1.948626|1.291611|
|0.15|1.972465|5.234631|2.283455|1.831317|1.628340|1.153562|
|0.20|1.836114|10.036376|2.465654|1.377272|1.370639|1.093183|
|0.25|2.495359|4.262036|1.246727|1.232388|1.209813|1.092931|
|_p_<br>0.30|2.260952|4.298054|1.410498|1.149826|1.215430|1.123646|
|0.35|1.553013|3.862468|1.511450|1.111143|1.165148|1.151871|
|0.40|1.446852|1.615702|1.276998|1.123451|1.146859|1.113719|
|0.45|1.583617|1.757668|1.263186|1.170124|1.112150|1.133443|
|0.50|1.333555|2.193936|1.258745|1.164263|1.149889|1.175700|


_Ed_ ˆ _n_ ( _ψ_<sup>ˆ</sup> _k_ ˆ( _<u>p</u>_ <u>)</u> _,ψ_ 0) ˆ Table 6: _Single-split likelihood cross-validation: Edn_ (<sup>ˆ</sup> _ψkn_ ˜ _,ψ_ 0)<sup>_vs.nand_</sup> _p._ Estimated distance ratios are based on 20 replicate datasets at six different sample sizes _n_ and for ten different validation set proportions _p_ .

Page 187

#### **Example 2: Density estimator selection**


<!-- Start of picture text -->
V−fold CV<br>Single split CV<br>50 50 100 100 200 200 400 400 800 800 1600 1600<br>Sample size, n<br>30<br>25<br>20<br>15<br>Distance ratio<br>10<br>5<br>0<br><!-- End of picture text -->

_Ed_ ˆ _n_ (<sup>ˆ</sup> _ψk_ ˆ( _<u>p</u>_ <u>)</u> _,ψ_ 0) ˆ Figure 7: _V -fold vs. single split CV: Edn_ (<sup>ˆ</sup> _ψkn_ ˜ _,ψ_ 0)<sup>_vs.n._Estimated</sup> distance ratios are based on 20 replicate datasets at six different sample sizes _n_ and for ten different validation set proportions _p_ .

Page 188

#### **Application 1: Identification of regulatory motifs**

Incorporating biological knowledge in the identification of regulatory motifs in DNA sequences.

- Palindromic binding sites.

E.g. CACGTG with reverse complement CACGTG.

- Binding sites with gaps.

E.g. GCGNNNNNNNNNNNNTAG.

- Information content profile of the binding site PWM. The information content (IC) of the PWM ( _pwj_ ) at position _w_ is

4

_IC_ ( _w_ ) = 2 + _pwj_ log2 _pwj_ = 2 _−_ Entropy( _w_ ) _∈_ [0 _,_ 2] _._ � _j_ =1

The information content profile of a PWM is a measure of a site’s tolerance for substitution: high IC, low tolerance.

Page 189

   - **Application 1: Identification of regulatory motifs**

- Direct relationship between the structural footprint of a protein on DNA and the information content profile of the PWM (Mirny & Gelfand, 2002).

- Transcription factors that have similar structures bind to sites with similar information content profiles (Eisen, 2002).

- The specific nature of TF–DNA interactions imposes constraints on the types of sequences that are likely to be TF binding sites (Eisen, 2002).

Page 190

**Application 1‘: Identification of regulatory motifs**

**E.g.** GAL4 binding sites for different yeast genes (from SCPD). `>YBR019C` TCGGCGATACCTTCACCG `>YBR020W` CGGGCGACGATTACCCG `>YLR081W` TATCGGAGCGTAGGCGGCCGAAC `>YML051W` CGGCATCCTACATGCCG `>YOR120W` TCGGTTCAGACAGGTCCGG

Page 191

#### **Application 1: Identification of regulatory motifs**


<!-- Start of picture text -->
2.0<br>1.0<br>CGG A T C CCG<br>0.0 GAGGC G C A T GC CGT<br>1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17<br>CCATATGT ATGCGATTGACG<br><!-- End of picture text -->

Figure 8: _GAL4 binding sites sequence logo._ `www-lmmb.ncifcrf. gov/~toms/sequencelogo.html` .

Page 192

#### **Application 1: Identification of regulatory motifs**

Figure 9: _GAL4 binding._ From `www.cryst.bbk.ac.uk/PPS2/.`

Page 193

#### **Application 1: Identification of regulatory motifs**


<!-- Start of picture text -->
GAL4 CRP<br>5 10 15 5 10 15 20<br>location location<br>ABF1 PURR<br>2 4 6 8 10 12 0 5 10 15 20 25<br>location location<br>2.0<br>1.8 1.4<br>1.6<br>1.2<br>1.4<br>1.2 1.0<br>Information content Information content<br>1.0<br>0.8<br>0.8<br>2.0 2.0<br>1.8 1.8<br>1.6 1.6<br>1.4 1.4<br>1.2 1.2<br>Information content 1.0 Information content 1.0<br>0.8 0.8<br>0.6<br><!-- End of picture text -->

#### Figure 10: _Information content profiles_ . GAL4, CRP, ABF1, PURR.

Page 194

#### **Application 1: COMODE**

**Kele¸s et al. (2003b).** COnstrained MOtif DEtection – COMODE. Likelihood-based method for detecting structured regulatory motifs in biological sequences.

- Unaligned DNA sequences are distributed according to independent mixtures of multinomials at each position.

- Specific structural constraints on the motifs are enforced as constraints on the entropy/information content profile and/or individual entries of their position specific weight matrix (PWM).

- Estimation of motif start site and PWM involves constrained maximum likelihood estimation for a multinomial mixture model.

Page 195

#### **Application 1: COMODE**

- Selecting a _good_ model for regulatory motifs: Distribution of bases in motif? Distribution of bases in background sequence? Constraints on PWM? Motif length? Number of motifs per sequence?

- Assessing the performance of the resulting estimators. = _⇒_ likelihood-based cross-validation.

Page 196

#### **Application 1: COMODE**

Examples of constraints on PWM.

- Constraints on the information content profile. E.g. parametric model such as

_IC_ ( _w_ ; _φ_ 1 _, φ_ 2 _, w_<sup>_∗_</sup> ) = _φ_ 1 _−|w − w_<sup>_∗_</sup> _|_ tan _φ_ 2 _, w_ = 1 _, . . . , W._

Structured motifs refer to binding sites with constraints on the IC of the PWM.

- Constraints on the information content of specific positions. E.g. _IC_ ( _w_ ) _> q_ for a given _q_ and _w_ .

- Constraints on specific nucleotide frequencies at a particular position. E.g. _pw_ 1 _>_ 0 _._ 8 = _⇒_ preference for nucleotide _A_ at position _w_ .

Page 197

#### **Application 1: COMODE**


<!-- Start of picture text -->
IC(w)<br>IC ( w ; θ 1, θ 2, w *) = θ 1 − | w − w * | tan θ 2<br>θ1 w = 1,..., W<br>θ2<br>1 w* W w<br><!-- End of picture text -->

Figure 11: _Example of parameterization for the IC profile of a motif PWM._

Page 198

**Application 1: COMODE**

#### **Output**

- **Input Output** _• n_ unaligned sequences _•_ Estimated PWM _•_ Motif length _W •_ Predicted start site _•_ PWM constraint functions for each input sequence

Available from S¨und¨uz Kele¸s, `www.stat.berkeley.edu/~sunduz` .

Page 199

#### **Application 1: COMODE**

_B_ = 100 datasets, each comprising _n_ = 30 sequences of length _L_ = 100, were generated using an i.i.d. background model, with an instance of the weak motif inserted in a varying percentage ( _F_ = 100% _,_ 75% _,_ 50% _,_ 25%) of the sequences.


<!-- Start of picture text -->
2.0<br>1.0<br>T C TATGCGAATCACGCGGA<br>0.0<br>1 2 3 4 5 6 7 8 9 10 11 12 13<br>G CAGAGCCATATGCGCGTATGATCTCAG C T<br><!-- End of picture text -->

Page 200

#### **Application 1: COMODE**

Three different types of constraints for the motif IC profile were supplied to COMODE.

- c.zoops-I: piecewise linear IC profile, V-shaped (two additional parameters _θ_ 1 and _θ_ 2).

- c.zoops-II: ordered IC profile, first and last three positions have equal high IC, middle positions have equal low IC, HHHLLLLLLLHHH.

- c.zoops-III: piecewise linear IC profile, hat-shaped, mirror image of c.zoops-I (two additional parameters _θ_ 1 and _θ_ 2).

Profiles used for c.zoops-I and c.zoops-II roughly match the true IC profile, the profile for c.zoops-III is misspecified.

Page 201

#### **Application 1: COMODE**

A sensitivity measure was computed as follows for each method in each of the _B_ simulated datasets


<!-- Start of picture text -->
�<br>sensb = |Kb |K  ∩ b K | ˆ b| ,<br><!-- End of picture text -->

where _Kb_ = _{_ set of true motif sites in dataset _b}_ , _K_ ˆ _b_ = _{_ set of predicted motif sites in dataset _b}_ .

Page 202

#### **Application 1: COMODE**


<!-- Start of picture text -->
F=100% F=50%<br>zoops c.zoops−I c.zoops−II c.zoops−III zoops c.zoops−I c.zoops−II c.zoops−III<br>100 100<br>80 80<br>60 60<br>40 40<br>20 20<br>0 0<br><!-- End of picture text -->


<!-- Start of picture text -->
F=75% F=25%<br>zoops c.zoops−I c.zoops−II c.zoops−III zoops c.zoops−I c.zoops−II c.zoops−III<br>100 100<br>80 80<br>60 60<br>40 40<br>20 20<br>0 0<br><!-- End of picture text -->

Figure 12: _COMODE._ Boxplot of sensitivity measures for ZOOPS, C.ZOOPS-I, C.ZOOPS-II, and C.ZOOPS-III.

Page 203

**Application 1: Likelihood CV for motif structure selection**

We have applied two-fold likelihood-based cross-validation to choose among these 4 models at _F_ = 100%.

Out of the _B_ = 100 datasets, c.zoops-I was selected 61 times and c.zoops-II was selected 39 times.

Page 204

**Application 1: Likelihood CV for motif width selection**

_B_ = 200 datasets, each comprising _n_ = 20 _,_ 100 sequences of length _L_ = 600, were generated using an i.i.d. background model. A motif of width 10 was inserted in each of the sequences.

Motif start sites and PWM were estimated using COMODE with no constraints on PWM, for motif widths ranging from 6 to 15bp.

Two-fold ( _p_ = 0 _._ 5) and five-fold ( _p_ = 0 _._ 2) cross-validation were used to select motif width.

Page 205

#### **Application 1: Likelihood CV for motif width selection**

|||_n_=|20|_n_=|100|
|---|---|---|---|---|---|
|||2-fold|5-fold|2-fold|5-fold|
||6|0|20|0|22|
||7|24|42|0|10|
||8|40|10|15|14|
||9|11|17|3|3|
|_w_|**10**|**121**|**98**|**147**|**142**|
||11|0|10|35|9|
||12|0|3|0|0|
||13|0|0|0|0|
||14|0|0|0|0|
||15|1|0|0|0|


Table 7: _Likelihood CV for motif width selection._ Number of simulations (out of _B_ = 200) each motif width was selected, for sample sizes _n_ = 20 _,_ 100 and using two- and five-fold CV. The true motif width is 10.

Page 206

**Application 2: Tree-based estimation with censored data**

Tree-based estimation procedures, such as the Classification and Regression Trees (CART) of Breiman et al. (1984), can be formulated in terms of the three main steps of our roadmap and correspond to a particular choice of candidates in Step 2.

**Step 1.** Loss-based definition of parameter of interest. The parameter of interest is defined as the risk minimizer for a particular loss function.

E.g. Regression trees: conditional expected value of an outcome given covariates _−→_ squared error loss function. Classification trees: posterior class probabilities _−→_ indicator loss function, also Gini and negative log-likelihood (entropy).

Page 207

#### **Application 2: Tree-based estimation with censored data**

**Step 2.** Node splitting and tree pruning.

- The sieve of candidate estimators is generated by recursive binary partitioning of a suitably defined covariate space into _nodes_ , using a loss-based node splitting rule. E.g. MSE, Gini, entropy.

- A loss-based pruning algorithm (minimal cost-complexity) is applied to yield a nested decreasing sequence of subtrees. (Cf. _forward_ selection followed by _backward_ deletion.)

- For each candidate tree, an estimator is returned for each set in the resulting partition (i.e., each _terminal node_ , or _leaf_ ) by minimizing the empirical risk.

**Step 3.** Cross-validation estimator selection. Selection of a ’right-sized’ tree by cross-validation.

Page 208

#### **Application 2: Tree-based estimation with censored data**

The outcome is a right-censored survival time. Parameters of interest include

- conditional expected value of (log) survival time given covariates _−→_ squared error loss function;

- conditional median of (log) survival time given covariates _−→_ absolute error loss function;

- conditional density (survival or hazard function) of survival time give covariates _−→_ negative log-likelihood loss function.

Page 209

**Application 2: Tree-based estimation with censored data**

**Problem.** _How to evaluate the loss function with censored data?_ Common approaches for tree-based regression and density estimation bypass the risk estimation problem for censored outcomes by altering the node splitting, tree pruning, and performance assessment criteria in manners that are specific to right-censored survival times.

Page 210

**Application 2: Tree-based estimation with censored data** Within-node homogeneity.

- Breiman <u>(2003).</u> Partition of time-covariate space using negative log-likelihood loss for a constant hazards model within nodes.

- Davis & Anderson <u>(1989).</u> Negative log-likelihood loss for an exponential model within nodes.

- Gordon & Olshen <u>(1985).</u> _Lp_ , _Lp_ Wasserstein, and Hellinger distances for within-node Kaplan-Meir estimates of survival distribution.

- LeBlanc & Crowley <u>(1992).</u> Negative log-likelihood loss based on first step of a full likelihood estimation procedure for a Cox proportional hazards model within nodes. Default method in R `rpart` function (Therneau & Atkinson, 1997).

- Pittman et al. <u>(2003).</u> Bayesian tree prediction, node splitting rule based on Bayes’ factors for Weibull models. On transformed data, use exponential survival distribution and conjugate Gamma priors.

Page 211

**Application 2: Tree-based estimation with censored data**

Between-node heterogeneity.

Ciampi et al. (1986) and Segal (1988) employ two-sample log-rank test statistics for between-node heterogeneity measures.

Abandoning the notion of risk (within-node homogeneity) leads to significant deviations from the standard CART framework for node splitting and tree pruning.

Page 212

**Application 2: Tree-based estimation with censored data**

Using a loss function that is specific to the parameter of interest. One may be interested in other parameters than the conditional survival distribution, such as the conditional mean or median survival time.

In such cases, gains in accuracy may be achieved by employing a loss function that is specific to the parameter of interest (e.g., L2 or L1 loss).

Risk estimation for performance assessment. Existing methods do not provide means for assessing risk for arbitrary loss functions. Current approaches typically rely on the negative log-likelihood loss function or ignore censored observations altogether.

Page 213

**Application 2: Tree-based estimation with censored data**

For any choice of full data loss function _L_ ( _X, ψ_ ), one can use the above IPCW or DR-IPCW observed data loss functions _L_ ( _O, ψ | η_ 0) for node splitting, tree pruning, and performance assessment by cross-validation.

Note that in the absence of censoring, i.e., when ∆= 1, then _L_ ( _O, ψ | η_ 0) = _L_ ( _X, ψ_ ) for both the IPCW and the DR-IPCW loss functions.

This ensures that the censored and full data estimators coincide when there is no censoring.

Page 214

#### **Application 2: Tree-based estimation with censored data**

Estimation road map

- **Step 1.** Specify a full data loss function _L_ ( _X, ψ_ ) for the parameter of interest; obtain the corresponding IPCW observed data loss function _L_ ( _O, ψ | η_ 0).

- **Step 2.** Apply standard node splitting and tree pruning procedures with the new IPCW loss function.

- **Step 3.** Use cross-validation with the IPCW loss function to select the right-sized tree.

Possibly bagging or boosting.

Page 215

**Application 2: Tree-based estimation with censored data**

The proposed tree-based estimation procedures with the IPCW loss function can be implemented using the R `rpart` package (Therneau & Atkinson, 1997), by supplying the IPCW to the `weights` argument of the `rpart` function.

The IPCW and DR-IPCW loss functions can be used for any type of prediction method, including standard linear regression, logic regression, and bagging and boosting procedures.

Page 216

#### **Application 2: Simulation study**

Comparison of survival trees built using two different loss functions for node splitting and tree pruning

- _NLL_ _~~P~~ H_ : negative log-likelihood loss function for Cox proportional hazards model (LeBlanc & Crowley, 1992), `rpart` default for survival data, `method=’’exp’’` ;

- _square IPCW_ : IPCW squared error loss function, `rpart` with `method=’’anova’’` , `weights=IPCW` .

For each loss function, obtain a final partition of the covariate space by five-fold cross-validation. Consider two within-node survival estimation methods

- IPCW mean, squared error loss function;

- Kaplan-Meier (KM) median, absolute error loss function.

Page 217

#### **Application 2: Simulation study**

- Full data structure, _X_ = ( _W, Z_ ): log-survival time _Z_ = log _T_ = _W_<sup>2</sup> + _ϵ_ , where _W ∼ U_ (0 _,_ 1), _ϵ ∼ N_ (0 _, σ_<sup>2</sup> ), _σ_<sup>2</sup> = 0 _._ 25.

- Censoring variable, _C_ : from uniform distributions.

- One hundred simulated learning samples were generated from an observed data distribution with 20% censoring, for sample sizes _n_ = 250, 600, 1250, and 6000.

Risk estimates are based on test samples of size _N_ = 5000 generated from the full data distribution.

Page 218

#### **Application 2: Simulation study**

Table 8: Ratios of average test sample risk for the _square_ _~~I~~ PCW_ loss function to the _NLL_ _~~P~~ H_ loss function, for two different within-node survival estimation methods.

|Sample|Survival estim|ation method|
|---|---|---|
|size, _n_|KM median|IPCW mean|
|250|0.9422|0.8838|
|600|0.9524|0.9062|
|1250|0.9629|0.9244|
|6000|0.9767|0.9533|


**N. B.** _Ratios less than one correspond to improved accuracy for trees based on IPCW loss function — Risk square_ _~~I~~ PCW/Risk NLL_ _~~P~~ H._

Page 219

**Application 2: Breast cancer survival and CGH copy number** Comparative genomic hybridization (CGH) is a microarray-based technique for measuring genome-wide DNA copy number.

DNA copy number alterations have been linked to a number of cancers: gains can over-express oncogenes, losses can inactivate tumor suppressor genes.

In cancer research, CGH analysis produces thousands of DNA copy number measurements for each patient, in addition to epidemiological, histological, and pathological variables. _Predict clinical outcome from thousands of explanatory variables._

Page 220

**Application 2: Breast cancer survival and CGH copy number**

CGH study of breast cancer patients (Waldman et al., in preparation).

- 152 patients, all with initial occurrences of breast cancer (invasive ductal carcinoma).

- <u>Outcome:</u> Time to recurrence (in months) — 52 patients recurred, censoring percentage of 66%.

: _•_ Explanatory variables epidemiological variables (e.g., age at diagnosis, race), histopathological variables (e.g., tumor stage, grade), and DNA copy number measures from a CGH array with 2,254 bacterial artificial chromosomes (BAC).

Page 221

**Application 2: Breast cancer survival and CGH copy number**

- The 152 observations were split at random into a learning set and a test set of 128 and 24 observations, respectively.

- Trees were grown using the learning set with the IPCW squared error loss function.

- Five-fold cross-validation was used to select the ’best’ tree.

- The survival function _G_<sup>¯</sup> 0 in the IPCW loss function was estimated separately for each training sample by fitting a Cox proportional hazards model to the epidemiological and histopathological variables ( `coxph` function).

- Overall performance was assessed on the test sample.

Page 222

#### **Application 2: Breast cancer survival and CGH copy number**


<!-- Start of picture text -->
BAC 294 < 0.02<br>BAC 1226 � -0.16<br>2.944<br>n  = 37<br>BAC 529 � -.01<br>4.328<br>n  = 17<br>Chromosomal<br>Location<br>BAC 542 < -0.12<br>BAC 294 3q26 2.742<br>n  = 19<br>BAC 1226 10q22<br>BAC 529 5q11<br>BAC 542 5q21 3.14 3.743<br>n  = 19  n  = 36<br><!-- End of picture text -->

Figure 13: _Breast cancer survival and CGH copy number dataset._ Learning set survival tree, IPCW mean log survival time (in months).

Page 223

**Application 2: Breast cancer survival and CGH copy number**

The selected two-split tree is based on BACs that fall in chromosomal regions known to contain genes related to breast cancer.

This tree suggests that copy number gains in both regions are associated with longer survival.

Improved prediction accuracy and more information on chromosomal regions related to breast cancer survival may be obtained from aggregation methods such as bagging and boosting and from more aggressive strategies for generating candidate estimators.

Page 224

#### **Application 2: Summary**

- The choice of loss function for node splitting, tree pruning, and within node estimation can have a large impact on accuracy.

- _•_ Gains in accuracy are obtained by using a loss function that is specific to the parameter of interest.

Page 225

#### **Ongoing work**

- More extensive study of the properties of different loss functions for multivariate outcome prediction and density estimation (Step 1).

- More aggressive strategies for generating candidate estimators (Step 2): addition/deletion/substitution algorithm (van der Laan & Dudoit, 2003; Sinisi & van der Laan, 2003).

- Loss-based variable importance statistics.

- R package.

Page 226

#### **References**

### `www.bepress.com/ucbbiostat/ www.bepress.com/sagmb/`

_•_ M. J. van der Laan and S. Dudoit (2003). Unified Cross-validation Methodology for Selection among Estimators: Finite Sample Results, Asymptotic Optimality, and Applications. Division of Biostatistics, UC Berkeley, Technical Report #130. General framework

_•_ S. Dudoit and M. J. van der Laan (2003). Asymptotics of Cross-Validated Risk Estimation in Model Selection and Performance Assessment. Division of Biostatistics, UC Berkeley, Technical Report #126. CV in prediction

_•_ S. Kele¸s, M. J. van der Laan, and S. Dudoit (2003a). Asymptotically Optimal Model Selection Method for Regression on Censored Outcomes. Division of Biostatistics, UC Berkeley, Technical Report #124. CV in prediction with censored data

_•_ M. J. van der Laan, S. Dudoit, and S. Kele¸s (2003). Asymptotic Optimality of Likelihood Based Cross-validation. Division of Biostatistics, UC Berkeley, Technical Report #125. Likelihood CV

_•_ A. Molinaro, S. Dudoit, and M. J. van der Laan (2003). Tree-based Multivariate Regression and Density Estimation based on Right-censored Data. Division of Biostatistics, UC Berkeley, Technical Report #135. Tree-based estimation with censored data

_•_ S. Kele¸s, M. J. van der Laan, S. Dudoit, B. Xing, and M. B. Eisen (2003b). Supervised detection of regulatory motifs in DNA sequences. Statistical Applications in Genetics and Molecular Biology, Vol. 2, No. 1, Article 5. Motif finding

Page 227

**Example 3: Predictor selection for right-censored outcomes**

Let _X_ = ( _Y, W_ ) _∼ FX,_ 0 be the full data structure of interest, where _Y_ = log( _T_ ) is a log survival time and _W_ a vector of explanatory variables (covariates).

Let _C_ be a right-censoring time, with conditional distribution _G_ 0( _· | X_ ). Assume _C ⊥ Y_ , given _W_ .

Suppose we have a learning set of _n_ i.i.d. observations of the right-censored data structure _O_ = min( _Y, C_ ) _,_ ∆= _I_ ( _Y ≤ C_ ) _, W ∼ P_ 0 = _PFX,_ 0 _,G_ 0. � �

Page 228

**Example 3: Predictor selection for right-censored outcomes**

Consider the quadratic loss function _L_ ( _X, ψ_ ) = _L_ 2( _X, ψ_ ) = ( _Y − ψ_ ( _W_ ))<sup>2</sup> _._

The parameter of interest, which minimizes the risk for this loss function, is the conditional expectation _ψ_ 0( _W_ ) = _E_ 0[ _Y | W_ ].

= _ψ_ 0 argmin _ψ L_ 2( _x, ψ_ ) _dFX,_ 0( _x_ ) � = argmin _ψ EFX,_ 0( _Y − ψ_ ( _W_ ))<sup>2</sup> ∆ = _._ argmin _ψ EP_ 0 _L_ 2( _X, ψ_ ) � _G_ <u>¯0(</u> _Y | X_ ) �

Page 229

**Example 3: Predictor selection for right-censored outcomes**

**General problem.** The loss function is a function of the full data structure _X_ = ( _Y, W_ ) — unobservable.

**Solution.** The general estimating function methodology for censored data of van der Laan & Robins (2002) maps full data estimating functions _D_ ( _X_ ) into observed data estimating functions _IC_ ( _O | Q_ ( _FX_ ) _, G, D_ ), indexed by nuisance parameters _G_ and (possibly) _Q_ ( _FX_ ). The estimating functions satisfy _EP_ 0 _IC_ ( _O | Q, G, D_ ) = _EFX,_ 0 _D_ ( _X_ ) if _G_ = _G_ 0 or _Q_ = _Q_ 0.

Thus, we can choose the following loss function for the observable right-censored data structure _O_

_L_ ( _O, ψ | η_ 0 = ( _Q_ 0 _, G_ 0)) = _IC_ ( _O | Q_ 0 _, G_ 0 _, L_ 2( _·, ψ_ )) _._

Page 230

**Example 3: Predictor selection for right-censored outcomes** Inverse probability of censoring weighted (IPCW) estimating function ∆ _IC_ ( _O | G, D_ ) = _D_ ( _X_ ) _G_ <u>¯(</u> _Y | X_ )<sup>_._</sup> For candidate predictors _ψ_<sup>ˆ</sup> _k_ = _ψk_ ( _· | Pn_ ), the cross-validation selector based on the IPCW estimating function is given by ∆ _i k_ ˆ = argmin _k ESn_ � ( _Yi − ψk_ ( _Wi | Pn,S_<sup>0</sup> _n_<sup>))2</sup> _G_ <u>¯</u><sup>0</sup> _n,Sn_<sup>(</sup><sup>_Yi| Wi_)</sup><sup>_._</sup> _{i_ : _Sn,i_ =1 _}_

Page 231

**Example 3: Predictor selection for right-censored outcomes**

Given candidate predictors _ψ_<sup>ˆ</sup> _k_ = _ψk_ ( _· | Pn_ ), the corresponding risk difference for the quadratic loss simplifies to = _dn_ ( _ψ_<sup>ˆ</sup> _k, ψ_ 0) _L_ ( _o, ψ_<sup>ˆ</sup> _k | η_ 0) _− L_ ( _o, ψ_ 0 _| η_ 0) _dP_ 0( _o_ ) � = _L_ 2( _x, ψ_<sup>ˆ</sup> _k_ ) _− L_ 2( _x, ψ_ 0) _dFX,_ 0( _x_ ) � = ( _ψk_ ( _w | Pn_ ) _− ψ_ 0( _w_ ))<sup>2</sup> _dFW,_ 0( _w_ ) _._ �

Page 232

**Example 3: Predictor selection for right-censored outcomes**

**E.g. 1.** Predicting survival of cancer patients based on microarray gene expression profile of cancer tissue.

**E.g. 2.** Predicting survival of AIDS patients from DNA sequence of HIV virus.

Page 233

**Example 3: Predictor selection for right-censored outcomes**

Cross-validation for bin width selection in histogram regression on right-censored outcomes.

- The full data structure is _X_ = ( _Y, W_ ), where _W ∼ U_ (0 _,_ 1) and _Y_ = log _T_ = _W_<sup>2</sup> + _ϵ_ , _ϵ ∼_ N(0 _, σ_<sup>2</sup> ), _σ_<sup>2</sup> = 2, enforced compact support in the interval [ _−_ 10 _,_ 10].

- Censoring times _C_ are generated from an Exponential( _λ_ ) distribution.

- 50 replicate datasets were generated for sample sizes _n_ =50, 100, 200, 400, 800, 1600.

- _Kn_ = 100 different bin widths were considered. For _k_ = 1 _, . . . , Kn_ , the unit interval is divided into _k_ bins with width 1 _/k_ each.

Page 234

#### **Example 3: Predictor selection for right-censored outcomes**


<!-- Start of picture text -->
Data points # of bins: 6<br>0.0 0.2 0.4 0.6 0.8 1.0<br>w w<br># of bins: 2 # of bins: 14<br>w w<br>4<br>0.8<br>2 0.6<br>z 0 0.4<br>0.2<br>−2 prediction<br>0.0<br>−4<br>0.5 1.0<br>0.4<br>0.3 0.5<br>0.2<br>prediction prediction 0.0<br>0.1<br>0.0<br><!-- End of picture text -->

Figure 14: _Histogram regression._ Predictors are indexed by the number of bins and the prediction for a given bin is the mean outcome for observations in that bin.

Page 235

- **Example 3: Predictor selection for right-censored outcomes**


where _G_<sup>¯0</sup> _n,Sn_<sup>(</sup><sup>_· | W_)istheKaplan-Meierestimatorof</sup><sup>_G_¯(</sup><sup>_· | W_).</sup>

- Bin widths were selected by ten-fold cross-validation ( _p_ = 1 _/_ 10).

Page 236

#### **Example 3: Predictor selection for right-censored outcomes**


<!-- Start of picture text -->
Censoring proportion<br>0% 10% 20%<br>50 6.578537 7.133457 7.846112<br>100 1.100901 1.333004 1.974709<br>200 1.022957 1.199649 1.418739<br>n 400 1.013431 1.137665 1.255642<br>800 1.010221 1.119677 1.155544<br>1600 1.003344 1.071642 1.107322<br>dn ( ψ ˆ k ˆ ,ψ 0)<br>Table 9: Ten-fold cross-validation. n for different<br>dn (  ˆ<br>ψkn ˜ ,ψ 0) vs.<br>censoring proportions ( λ  = 0 . 07 and 0 . 15 for 10% and 20% censoring,<br>respectively).<br><!-- End of picture text -->

Page 237

**CROSS-VALIDATED DELETION/SUBSTITUTION/ADDITION ALGORITHM FOR PREDICTION: APPLICATIONS IN GENOMICS**

**Mark van der Laan** www.stat.berkeley.edu/ laan

Joint work with Sandrine Dudoit, Sandra Sinisi, Annette Molinaro, Mike Eisen.

Division of Biostatistics, University of California, Berkeley. www.bepress.com/ucbbiostat/ October 8, 2003 The Constance van Eeden Lecture University of Britisch Columbia, Vancouver

#### **MOTIVATION**

1. Prediction of clinical outcomes based on epidemiological and genomic data such as gene expression/ single nucleotide polymorphism (SNP)/ comparative genomic hybridization (CGH).

2. Prediction of gene-expression from regularitory-DNA-sequence.

3. And so on!

**Interesting features:** High dimensional covariates, censored clinical outcomes such as survival.

Page 239

#### **OVERVIEW**

- The **optimal predictor** in terms of loss function.

- **Selection** among candidate data-based predictors (estimators): Cross-validation selector, theory, take home lesson.

- **Parametrizing** predictors as linear combinations of basis functions (i.e., choose a Sieve).

- **Construction** of a candidate data dependent predictor for each subset of basis functions.

- **Minimizing** criteria (cross-validated risk/empirical risk) for subset-specific predictor over all possible subsets of basis functions: Deletion/Substitution/Addition algorithm.

- **Generalizing** to censored data.

Page 240

**OPTIMAL PREDICTOR IN TERMS OF LOSS FUNCTION** Let _O_ 1 = ( _Y_ 1 _, W_ 1) _, . . . , On_ = ( _Yn, Wn_ ) be _n_ i.i.d. observations of _O_ = ( _Y, W_ ) _∼ P_ 0, where _Y_ denotes an outcome of interest and _W_ is a _d_ -dimensional vector of covariates. Let _M_ be a model for _P_ 0: that is, it is given that _P_ 0 _∈M_ . **Predictor:** A function _W → ψ_ ( _W_ ) from _W_ to an outcome. **Loss function** : Let _L_ ( _O, ψ_ ) = ( _Y − ψ_ ( _W_ ))<sup>2</sup> be the squared error loss function for a candidate predictor _ψ_ . **Risk of predictor** : The risk of a predictor _W → ψ_ ( _W_ ) equals the expected loss (w.r.t. the true distribution _P_ 0). **Optimal predictor** : _ψ_ 0( _W_ ) = _EP_ 0( _Y | W_ ) is the optimal (minimal risk) predictor over a set **Ψ** (e.g., parameter space implied by model _M_ ) of allowed predictors:

= _ψ_ 0 argmin _ψ∈_ **Ψ** _E_ 0 _L_ ( _O, ψ_ ) = argmin _ψ∈_ **Ψ** ( _Y − ψ_ ( _W_ ))<sup>2</sup> _dP_ 0( _Y, W_ ) _._ <u>�</u>

Page 241

**Risk “distance”** : For a given predictor _W → ψ_ ( _W_ ), we have that its risk minus the optimal risk equals the expected squared deviation _ψ_ ( _W_ ) _− ψ_ 0( _W_ ): _≡ d_ ( _ψ, ψ_ 0) _{L_ ( _O, ψ_ ) _− L_ ( _O, ψ_ 0) _} dP_ 0( _O_ ) � = ( _ψ_ ( _W_ ) _− ψ_ 0( _W_ ))<sup>2</sup> _dP_ 0( _W_ ) _._ �

Page 242

#### **SELECTION**

Let _Pn_ be the empirical distribution of the observed sample _O_ 1 _, . . . , On_ .

**Estimator:** An estimator of the optimal predictor _ψ_ 0( _W_ ) is a mapping (i.e., an algorithm) from _Pn_ into a particular predictor in **Ψ** . Notation: _Pn → ψ_ ( _Pn_ ) _∈_ **Ψ** . **Candidate estimators:** Let _Pn → ψk_ ( _Pn_ ) _∈_ **Ψ** , _k_ = 1 _, . . . , K_ ( _n_ ), be a collection of estimators of _ψ_ 0 (i.e., algorithms which map data into a predictor).

Page 243

#### **THE ORACLE SELECTOR**

The oracle selector _k_<sup>˜</sup> _n_ chooses the estimator with minimal (true) risk. Equivalently

_k_ ˜ _n_ = argmin _k_ ( _ψk_ ( _Pn_ )( _W_ ) _− ψ_ 0( _W_ ))<sup>2</sup> _dP_ 0( _W_ ) _._ �

Since risk depends on the true distribution _P_ 0 this selector is not available in practice.

**Asymptotic equivalence with oracle selector:** Given the _K_ ( _n_ ) candidate estimators, a selector _k_<sup>ˆ</sup> = _k_<sup>ˆ</sup> ( _Pn_ ) _∈{_ 1 _, . . . , K_ ( _n_ ) _}_ is asymptotically equivalent with the oracle selector if the risk of the estimator chosen by the selector approaches (when sample size converges to infinity) as fast to the optimal risk of _ψ_ 0 as the risk of the estimator chosen by the oracle selector: that is,

_d_ <u>(</u> _ψk_ ˆ( _Pn_ <u>)</u> _, ψ_ 0) _d_ ( _ψk_ ˜ _n_ ( _Pn_ ) _, ψ_ 0)<sup>_→_1inprobability.</sup>

Page 244

**THE CROSS-VALIDATION SELECTOR**

**Empirical risk estimate:** Given an estimator _ψ_ ( _Pn_ ), the empirical risk estimate is simply the empirical mean of the squared error loss _L_ ( _O, ψ_ ( _Pn_ )) = ( _Y − ψ_ ( _Pn_ )( _W_ ))<sup>2</sup> :


**Cross-validated risk estimate:** In this case, one applies the estimator to a part of the sample (training sample) and one computes the average loss of the obtained estimator over the remaining sample (validation sample). One averages this risk estimate over a particular number of splits of the sample.

Page 245

Formally, define a random vector _Sn ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> for splitting the sample into a validation and a training sample.

 0 if i-th observation is in the training sample _Sn,i_ =  1 if i-th observation is in the validation sample  Different choices of _Sn_ cover all types of cross-validation schemes including _V −_ fold cross-validation, monte carlo cross validation, and bootstrap cross-validation. For example, in 5-fold cross-validation _Sn_ has 5 possible outcomes.

Page 246


Page 247

Let _p_ = _n_ 1 _/n_ be the proportion constituting the validation sample. Let _Pn,S_<sup>0</sup> _n_<sup>,</sup><sup>_P_</sup> _n,S_<sup>1</sup> _n_<sup>betheempiricaldistributionsofthetrainingand</sup> validation sample, respectively.

The cross-validated risk estimate of a candidate estimator _Pn → ψk_ ( _Pn_ ) is defined by:

1 _ESn_ � ( _Yi − ψk_ ( _Pn,S_<sup>0</sup> _n_<sup>)(</sup><sup>_Wi_))2</sup><sup>_._</sup> _np i_ : _Sn_ ( _i_ )=1

**Cross-validation selector:** The cross-validation selector chooses the estimator minimizing the cross-validated risk estimate of the risk of _ψk_ ( _Pn_ ), _k_ = 1 _, . . . , K_ ( _n_ ).

Page 248

**EQUIVALENCE WITH ORACLE SELECTOR** If 1) the proportion _p_ = _p_ ( _n_ ) constituting the validation sample converges to zero with sample size _n_ , and 2) the **logarithm** of the number of estimators, _K_ ( _n_ ), **divided by** the validation sample size, _np_ , converges faster to zero than the risk distance of the oracle choice estimator and _ψ_ 0, then the cross-validation selector _k_<sup>ˆ</sup> is asymptotically equivalent (and thus optimal) with the oracle selector.

**Sensitivity to proportion** _p_ **:** Simulations (and theoretical argument) show that, in practice, the sensitivity of the performance of the cross-validation selector to the choice of _p_ is remarkably low: e.g. 2-fold performs well!

Page 249

**DESCRIBING/PARAMETRIZING PREDICTORS** We describe any of the allowed predictors in **Ψ** with linear combinations _W →_<sup>�</sup> _j∈I_<sup>_βj_Φ</sup><sup>_j_(</sup><sup>_W_)ofbasisfunctions</sup><sup>_W→_Φ</sup><sup>_j_(</sup><sup>_W_)</sup> indexed by an index set _I_ .

**Tensor products of univariate basis functions:** For example, if we use a polynomial basis, then for each _⃗p_ = ( _p_ 1 _, . . . , pd_ ), we have a basis function _φ⃗p_ ( _X_ ) = _X_ 1<sup>_p_1</sup><sup>_· · · X_</sup> _d_<sup>_pd_.</sup> Each index set _I_ = _{⃗p_ 1 _, . . . ,⃗pk}_ , corresponds now with a linear regression model in variables being tensor products of polynomial powers.

**Indicators of sets of a partition:** Let _W_ be the covariate space. Given a region _R_ in _W_ , let Φ _R_ ( _·_ ) = _I_ ( _· ∈ R_ ) be the indicator of this region. Each partition _I_ = _{R_ 1 _, . . . , Rk}_ of _W_ corresponds with a linear regression model in variables being indicators of sets _Rj_ : thus, a histogram regression model.

Page 250

**SUBSET SPECIFIC LEAST-SQUARES ESTIMATOR** For each index set _I_ (indicating tensor products of univariate basis functions, or indicators of sets corresponding with a partition), let Ψ _I_ ( _Pn_ )

be the minimizer of residual sum of squared errors (i.e., empirical mean of squared error loss function) over the linear regression model _{ψI,β_ : _β}_ corresponding with the subset of basis functions identified by _I_ .

Page 251

**ESTIMATING THE SUBSET OF BASIS FUNCTIONS** The optimal subset would be the minimizer over all subsets _I_ of the true risk (say) _f_ 0( _I_ ) of the corresponding estimator _ψI_ ( _Pn_ ). So we need to estimate this true risk function. **Subset Estimator 1:** Minimize the empirical risk estimate over all subsets of basis functions of size _k_ , but choose _k_ by minimizing the cross-validated risk estimate. **Subset Estimator 2:** Minimize the cross-validated risk estimate over all subsets of basis functions. That is, minimize

1 _I → ESn_ � _{Yi −_ Ψ _I_ ( _Pn,S_<sup>0</sup> _n_<sup>)(</sup><sup>_Wi_)</sup><sup>_}_2</sup><sup>_._</sup> _np i_ : _Sn_ ( _i_ )=1

Below, we specify a DELETION/SUBSTITUTION/ADDITION (D/S/A) algorithm for minimizing over _I_ the empirical risk estimate _fRSS_ ( _I_ ) or cross-validated risk estimate _fCV.RSS_ ( _I_ ) of _ψI_ ( _Pn_ ).

Page 252

**DELETION/SUBSTITUTION/ADDITION ALGORITHM** The D/S/A algorithm aims to minimize a function _I → f_ ( _I_ ) (e.g., _fRSS_ , _fCV.RSS_ ) over subsets of basis functions, and is defined by three set functions _DEL_ ( _I_ 0), _SUB_ ( _I_ 0), and _ADD_ ( _I_ 0), which maps a current subset _I_ 0 into a collection of subsets of size _| I_ 0 _| −_ 1 (deletion moves), _| I_ 0 _|_ (substitution moves), and _| I_ 0 _|_ +1 (addition moves), respectively.

Page 253

#### **ALGORITHM**

I0 = ∅, **Initiate Algorithm** { } _f2_ (I0) = ESn ∫ L(Oi,ψI(o|P<sup>0</sup> n, Sn<sup>))</sup><sup>_d_P1</sup> n, Sn<sup>(O)</sup>

Page 254

#### **ALGORITHM**

I0 = ∅, **Initiate Algorithm** { } _f2_ (I0) = ESn ∫ L(Oi,ψI(o|P<sup>0</sup> n, Sn<sup>))</sup><sup>_d_P1</sup> n, Sn<sup>(O)</sup>

**Addition**

_f2_ (I<sup>+</sup> ) =  argmin _f2_ (I) I ∈Add(I0)

Page 255

#### **ALGORITHM**


<!-- Start of picture text -->
I0 = ∅,<br>Initiate Algorithm { }<br>f2  (I0) = ESn ∫ L(Oi,ψI(o|P 0 n, Sn )) d P1 n, Sn (O)<br>Addition<br><!-- End of picture text -->


<!-- Start of picture text -->
f2  (I + ) <  f2  (I0)<br>I0 = I +<br>Addition<br>f2  (I + ) =  argmin  f2  (I)<br>I ∈Add(I0)<br><!-- End of picture text -->

Page 256

#### **ALGORITHM**


<!-- Start of picture text -->
I0 = ∅,<br>Initiate Algorithm { }<br>f2  (I0) = ESn ∫ L(Oi,ψI(o|P 0 n, Sn )) d P1 n, Sn (O)<br>Deletion<br>f2  (I - ) =  argmin  f2  (I)<br>I ∈Del(I0) f2  (I - ) <  f2  (I0)<br>I0 = I -<br>f2  (I - ) ≥ f2  (I0)<br>f2  (I + ) <  f2  (I0)<br>I0 = I +<br>Addition<br>f2  (I + ) =  argmin  f2  (I)<br>I ∈Add(I0)<br><!-- End of picture text -->

Page 257


<!-- Start of picture text -->
ALGORITHM<br>I0 = ∅,<br>Initiate Algorithm { }<br>f2  (I0) = ESn ∫ L(Oi,ψI(o|P 0 n, Sn )) d P1 n, Sn (O)<br>Deletion<br>f2  (I - ) =  argmin  f2  (I)<br>I ∈Del(I0) f2  (I - ) <  f2  (I0)<br>I0 = I -<br>f2  (I - ) ≥ f2  (I0)<br>Substitution<br>f2  (I = ) =  argmin  f2  (I)<br>I ∈Sub(I0)<br>f2  (I + ) <  f2  (I0)<br>I0 = I +<br>Addition<br>f2  (I + ) =  argmin  f2  (I)<br>I ∈Add(I0)<br><!-- End of picture text -->

Page 258


<!-- Start of picture text -->
ALGORITHM<br>I0 = ∅,<br>Initiate Algorithm { }<br>f2  (I0) = ESn ∫ L(Oi,ψI(o|P 0 n, Sn )) d P1 n, Sn (O)<br>Deletion<br>f2  (I - ) =  argmin  f2  (I)<br>I ∈Del(I0) f2  (I - ) <  f2  (I0)<br>I0 = I -<br>f2  (I - ) ≥ f2  (I0) f2  (I = ) <  f2  (I0)<br>Substitution<br>I0 = I =<br>f2  (I = ) =  argmin  f2  (I)<br>I ∈Sub(I0)<br>f2  (I + ) <  f2  (I0)<br>f2  (I = ) ≥ f2  (I0)<br>I0 = I +<br>Addition<br>f2  (I + ) =  argmin  f2  (I)<br>I ∈Add(I0)<br><!-- End of picture text -->

Page 259


<!-- Start of picture text -->
ALGORITHM<br>I0 = ∅,<br>Initiate Algorithm { }<br>f2  (I0) = ESn ∫ L(Oi,ψI(o|P 0 n, Sn )) d P1 n, Sn (O)<br>Deletion<br>f2  (I - ) =  argmin  f2  (I)<br>I ∈Del(I0) f2  (I - ) <  f2  (I0)<br>I0 = I -<br>f2  (I - ) ≥ f2  (I0) f2  (I = ) <  f2  (I0)<br>Substitution<br>I0 = I =<br>f2  (I = ) =  argmin  f2  (I)<br>I ∈Sub(I0)<br>f2  (I + ) <  f2  (I0)<br>f2  (I = ) ≥ f2  (I0)<br>I0 = I +<br>Addition<br>f2  (I + ) =  argmin  f2  (I)<br>I ∈Add(I0)<br>f2  (I + ) ≥ f2  (I0)<br>Stop Algorithm<br><!-- End of picture text -->

Page 260

**PROPOSAL FOR TENSOR PRODUCT MOVES Deletion moves.** _DEL_ ( _I_ 0) maps into the _k_ subsets of size _k −_ 1 corresponding with deleting one of the _k_ basis functions in _I_ 0. **Substitution moves.** Given a basis function indexed by _⃗p ∈ I_ 0, replace it by the basis function indexed by _⃗p ±⃗ej_ , where _⃗ej_ denotes the _j_ -th unit vector, _j_ = 1 _, . . . , d_ . Apply this to each basis function in _I_ 0, which gives a total of 2 _d × k_ substitution moves.

Page 261

**Illustration:**   ( _p_ 1 + 1 _, p_ 2 _, p_ 3 _, . . . , pd_ )       ( _p_ 1 _, p_ 2 + 1 _, p_ 3 _, . . . , pd_ )       ...     ( _p_ 1 _, p_ 2 _, p_ 3 _, . . . , pd_ + 1) _p →_    ( _p_ 1 _−_ 1 _, p_ 2 _, p_ 3 _, . . . , pd_ )       ( _p_ 1 _, p_ 2 _−_ 1 _, p_ 3 _, . . . , pd_ )       ...     ( _p_ 1 _, p_ 2 _, p_ 3 _, . . . , pd −_ 1) for each _⃗p ∈ I_ 0.

**Addition moves.** Given the current index set _I_ 0, the addition moves are obtained by adding to _I_ 0 the basis functions indexed by one of the unit vectors or by one of the basisi functions in _SUB_ ( _I_ 0). This gives a total of 3 _d_ addition moves.

Page 262

#### **Illustration:**


<!-- Start of picture text -->
<br><br> (1 ,  0 , . . . ,  0)<br><br><br><br><br><br> ...<br><br><br><br><br><br><br> (0 , . . . ,  0 ,  1)<br><br><br><br><br> ( p 1 + 1 , p 2 , p 3 , . . . , pd )<br><br><br>pk +1 = ...<br><br><br><br><br><br> ( p 1 , p 2 , p 3 , . . . , pd  + 1)<br><br><br><br><br> ( p 1  − 1 , p 2 , p 3 , . . . , pd )<br><br><br><br><br><br><br> ...<br><br><br><br> ( p 1 , p 2 , p 3 , . . . , pd − 1)<br><br><!-- End of picture text -->

By replacing the jumps of size 1 in the definition of _SUB_ ( _I_ 0) and _ADD_ ( _I_ 0) by jumps of size in _{_ 1 _, . . . , S}_ , this algorithm can be made increasingly agressive.

Page 263

**SIMPLE EXAMPLE FOR POLYNOMIAL BASIS** Let _d_ = 4 and _Y_ = _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε_.Then</sup><sup>_k_= 2,</sup> _p_ 1 = (1 _,_ 1 _,_ 1 _,_ 0), _⃗p_ 2 = (0 _,_ 1 _,_ 0 _,_ 5).

A deletion move simply means removing one of the terms of the current model and fitting a model of size _k −_ 1.

The substitution moves involve replacing the _s_<sup>th</sup> term for _s_ = 1 _, . . . , k_ with a new term, keeping the size of the model fixed at _k_ .

Page 264

#### The possible substitution moves are given by:

|<br><br><br><br>_X_<sup>2</sup><br>1<sup>_X_</sup>2<sup>_X_</sup>3 <sup>+</sup><sup>_X_</sup>2<sup>_X_5</sup><br>4 <sup>+</sup><sup>_ε_</sup>|_p_1 = (2_,_1_,_1_,_0)|
|---|---|
|<br><br><br><br><br><br>_X_1_X_<sup>2</sup><br>2<sup>_X_</sup>3 <sup>+</sup><sup>_X_</sup>2<sup>_X_5</sup><br>4 <sup>+</sup><sup>_ε⃗_</sup>|_p_1 = (1_,_2_,_1_,_0)|
|<br><br><br><br><br><br><br>_X_1_X_2_X_<sup>2</sup><br>3 <sup>+</sup><sup>_X_</sup>2<sup>_X_5</sup><br>4 <sup>+</sup><sup>_ε⃗_</sup>|_p_1 = (1_,_1_,_2_,_0)|
|<br><br><br><br><br><br>_X_1_X_2_X_3_X_4+_X_2_X_<sup>5</sup><br>4 <sup>+</sup><sup>_ε⃗_</sup>|_p_1 = (1_,_1_,_1_,_1)|
|<br><br><br><br><br><br>_X_2_X_3+_X_2_X_<sup>5</sup><br>4 <sup>+</sup><sup>_ε⃗_</sup>|_p_1 = (0_,_1_,_1_,_0)|
|<br><br><br><br><br><br>_X_1_X_3+_X_2_X_<sup>5</sup><br>4 <sup>+</sup><sup>_ε⃗_</sup>|_p_1 = (1_,_0_,_1_,_0)|
|_Y_ =<br><br><br>_X_1_X_2+_X_2_X_<sup>5</sup><br>4 <sup>+</sup><sup>_ε⃗_</sup>|_p_1 = (1_,_1_,_0_,_0)|
|<br><br><br><br><br><br>_X_1_X_2_X_<sup>5</sup><br>4 <sup>+</sup><sup>_X_</sup>1<sup>_X_</sup>2<sup>_X_</sup>3 <sup>+</sup><sup>_ε_</sup>|_p_2 = (1_,_1_,_0_,_5)|
|<br><br><br><br><br><br>_X_<sup>2</sup><br>2<sup>_X_5</sup><br>4 <sup>+</sup><sup>_X_</sup>1<sup>_X_</sup>2<sup>_X_</sup>3 <sup>+</sup><sup>_ε⃗_</sup>|_p_2 = (0_,_2_,_0_,_5)|
|<br><br><br><br><br><br>_X_2_X_3_X_<sup>5</sup><br>4 <sup>+</sup><sup>_X_</sup>1<sup>_X_</sup>2<sup>_X_</sup>3 <sup>+</sup><sup>_ε⃗_</sup>|_p_2 = (0_,_1_,_1_,_5)|
|<br><br><br><br><br><br>_X_2_X_<sup>6</sup><br>4 <sup>+</sup><sup>_X_</sup>1<sup>_X_</sup>2<sup>_X_</sup>3 <sup>+</sup><sup>_ε⃗_</sup>|_p_2 = (0_,_1_,_0_,_6)|
|<br><br><br><br><br><br><br>_X_<sup>5</sup><br>4 <sup>+</sup><sup>_X_</sup>1<sup>_X_</sup>2<sup>_X_</sup>3 <sup>+</sup><sup>_ε⃗_</sup>|_p_2 = (0_,_0_,_0_,_5)|
|<br><br><br>_X_2_X_<sup>4</sup><br>4 <sup>+</sup><sup>_X_</sup>1<sup>_X_</sup>2<sup>_X_</sup>3 <sup>+</sup><sup>_ε⃗_</sup>|_p_2 = (0_,_1_,_0_,_4)|


Page 265

If none improve RSS, then find the best fit among the following _addition_ moves:

 _X_ 1 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε_</sup> _p_ 3 = (1 _,_ 0 _,_ 0 _,_ 0)     _X_ 2 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 1 _,_ 0 _,_ 0)      _X_ 3 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 0 _,_ 1 _,_ 0)     _X_ 4 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 0 _,_ 0 _,_ 1)    _X_ 1<sup>2</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε_</sup> _p_ 3 = (2 _,_ 1 _,_ 1 _,_ 0)      _X_ 1 _X_ 2<sup>2</sup><sup>_X_3+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (1 _,_ 2 _,_ 1 _,_ 0)     _X_ 1 _X_ 2 _X_ 3<sup>2+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (1 _,_ 1 _,_ 2 _,_ 0)     _X_ 1 _X_ 2 _X_ 3 _X_ 4 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (1 _,_ 1 _,_ 1 _,_ 1) _Y_ =  _X_ 2 _X_ 3 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 1 _,_ 1 _,_ 0)     _X_ 1 _X_ 3 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (1 _,_ 0 _,_ 1 _,_ 0)     _X_ 1 _X_ 2 + _X_ 1 _X_ 2 _X_ 3 + _X_ 2 _X_ 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (1 _,_ 1 _,_ 0 _,_ 0)      _X_ 1 _X_ 2 _X_ 4<sup>5+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε_</sup> _p_ 3 = (1 _,_ 1 _,_ 0 _,_ 5)    _X_ 2<sup>2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 2 _,_ 0 _,_ 5)     _X_ 2 _X_ 3 _X_ 4<sup>5+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 1 _,_ 1 _,_ 5)      _X_ 2 _X_ 4<sup>6+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 1 _,_ 0 _,_ 6)    _X_ 4<sup>5+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 0 _,_ 0 _,_ 5)   _X_ 2 _X_ 4<sup>4+</sup><sup>_X_1</sup><sup>_X_2</sup><sup>_X_3+</sup><sup>_X_2</sup><sup>_X_</sup> 4<sup>5+</sup><sup>_ε⃗_</sup> _p_ 3 = (0 _,_ 1 _,_ 0 _,_ 4)

Page 266

**DOES THE DSA ALGORITHM DO THE JOB?** Is the algorithm capable to find the global minimum (i.e., the optimal predictor _W → ψ_ 0( _W_ ) = _E_ 0( _Y | W_ )) when _n_ is large enough?

We generated _n_ = 1000 observations from the following three true regression models with zero error, _d_ = 100, _Xj ∼ U_ (0 _,_ 1), and we check if the D/S/A algorithm finds the truth. _E_ 1[ _Y |X_ ] = _X_ 1 _X_ 12 _X_ 13<sup>2</sup><sup>_X_</sup> 22<sup>_X_</sup> 24<sup>_X_</sup> 54<sup>_X_</sup> 79<sup>_X_</sup> 83<sup>_X_</sup> 95<sup>+</sup><sup>_X_</sup> 15<sup>_X_</sup> 18<sup>_X_</sup> 37<sup>_X_</sup> 42<sup>_X_</sup> 68<sup>+</sup> _X_ 6 _X_ 22 _X_ 33<sup>3</sup><sup>_X_</sup> 40<sup>_X_</sup> 58<sup>_X_</sup> 75<sup>_X_</sup> 82<sup>_X_</sup> 87<sup>+</sup><sup>_X_</sup> 15<sup>_X_</sup> 31

_E_ 2[ _Y |X_ ] =

_X_ 7 _X_ 25 _X_ 31 _X_ 59 _X_ 63 _X_ 68 _X_ 70 _X_ 83 _X_ 88 _X_ 98 + _X_ 0 _X_ 32 _X_ 47 _X_ 54 _X_ 66 _X_ 72 _X_ 73 _X_ 77 + _X_ 82 + _X_ 7 _X_ 49 _X_ 55 _X_ 73 _X_ 80 + _X_ 33 _X_ 40 + _X_ 18 _X_ 21 _X_ 40 _X_ 56 _X_ 59 _X_ 71 _X_ 91 + _X_ 9 _X_ 13 _X_ 18 _X_ 20 _X_ 41 _X_ 53 _X_ 69 _X_ 95 + _X_ 3 _X_ 38 _X_ 78 _X_ 96 + _X_ 0 _X_ 20 _X_ 64 _X_ 88 _X_ 91 _X_ 96 + _X_ 2 _X_ 6 _X_ 16 _X_ 37 _X_ 45 _X_ 46 _X_ 61 _X_ 68 _X_ 91 _X_ 95

Page 267

_E_ 3[ _Y |X_ ] = _X_ 0 _X_ 1<sup>2</sup><sup>_X_</sup> 4<sup>4</sup><sup>_X_</sup> 99<sup>10+</sup><sup>_X_</sup> 45<sup>+</sup> _X_<sup>2</sup> 2<sup>_X_</sup> 8<sup>_X_</sup> 14<sup>_X_</sup> 20<sup>_X_</sup> 22<sup>_X_</sup> 29<sup>_X_</sup> 36<sup>_X_</sup> 39<sup>_X_</sup> 41<sup>_X_</sup> 44<sup>_X_</sup> 48<sup>_X_</sup> 56<sup>_X_</sup> 62<sup>_X_</sup> 63<sup>_X_</sup> 65<sup>_X_</sup> 87<sup>+</sup> _X_ 27 _X_ 48 _X_ 63 _X_ 77 _X_ 78 _X_ 93 _X_ 94 + _X_ 71 + _X_ 12 _X_ 18 _X_ 22 _X_ 44 _X_ 50 _X_ 55 _X_ 57 _X_ 64 _X_ 73<sup>2</sup><sup>_X_</sup> 80<sup>_X_</sup> 83<sup>_X_</sup> 93<sup>_X_</sup> 94<sup>_X_</sup> 96<sup>+</sup><sup>_X_</sup> 69<sup>_X_</sup> 91<sup>+</sup> _X_ 2 _X_ 4 _X_ 22 _X_ 23 _X_ 28 _X_ 36 _X_ 53 _X_ 79 _X_ 88 + _X_ 48 _X_ 70 _X_ 82 _X_ 97 + _X_ 3 _X_ 24 _X_ 29 _X_ 54 _X_ 64 _X_ 80

Page 268

#### **Simulation Results for Three Models**

#### Zero error


<!-- Start of picture text -->
X n d RSS<br>E [ Y |X ] p<br>E 1[ Y |X ] U (0 ,  1) 1000 100 1.0 0.000000<br>E 2[ Y |X ] U (0 ,  1) 1000 100 1.0 0.000000<br>E 3[ Y |X ] U (0 ,  1) 1000 100 0.8 0.000001<br><!-- End of picture text -->

Page 269

#### **SIMULATIONS**

Consider the nonparametric polynomial regression (NPR) model for _E_ [ _Y |X_ ], defined by the collection of sums of tensor-product polynomial basis functions:


<!-- Start of picture text -->
size d<br>Y = X ps ( j )<br>βs +  ε, E ( ε|⃗X ) = 0 .<br>� � j<br>s =1 j =1<br><!-- End of picture text -->

To assess the DSA algorithm’s ability to minimize residual sum of squares over this NPR-model for large sample size, we randomly generated true regressions in this NPR-model and set _ϵ_ = 0, and verified if the algorithm found the truth.

Page 270

The true regression model is randomly generated as follows: _size ∼U{_ 1 _, . . . ,_ 5 _}_ � _d ps_ ( _j_ ) _∼U{_ 1 _, . . . ,_ 5 _} j_ =1 _ps ∼_ Multinomial(<sup>�</sup><sup>_d_</sup> _j_ =1<sup>_ps_(</sup><sup>_j_)</sup><sup>_, d,_(</sup> _d_<sup><u>1</u></sup><sup>_, . . . ,_</sup> _d_<sup><u>1</u>))</sup> After randomly choosing _size_ and _⃗ps_ , each formed<sup>�</sup> _j_<sup>_X_</sup> _j_<sup>_ps_(</sup><sup>_j_)</sup> tensor-product was ensured to be unique. The sum of these randomly generated unique terms and _ε_ yielded the true response variable _Y_ .

Page 271

#### **REPORTED QUANTATIES**

The following quantities are represented in the tables summarizing simulation results:

- _p_ : proportion of correctly fitted terms given the true model

- _• p_ ¯: average proportion of correctly fitted terms across the number of repetitions

- _RSS_ : residual sum of squares of fitted model

- _RSS_ : average RSS across the number of repetitions

Page 272

#### **Results for Randomly Generated Polynomial Regressions**

#### Zero error

|X|n|d|nsims|¯_p_|_RSS_|
|---|---|---|---|---|---|
|_U_(0_,_1)|1000|5|1000|1.000|0.0000|
|_U_(0_,_1)|1000|100|500|1.000|0.0000|
|Bernoulli(p)|1000|5|100|0.996|0.0000|
|Bernoulli(p)|2000|10|100|0.921|0.0000|
|Bernoulli(p)|1000|25|100|0.884|0.0000|
|Bernoulli(0.6)|500|5|100|1.000|0.0000|
|Bernoulli(0.6)|500|25|100|1.000|0.0000|


Page 273

**Comparing** _ε_ = 0 **to** _ε ∼N_ (0 _,_ 1)

The following two models were generated, first with _ε_ = 0 and then with _ε ∼N_ (0 _,_ 1). _E_ 3[ _Y |X_ ] = _X_ 0 _X_ 1<sup>2</sup><sup>_X_</sup> 2<sup>2+</sup><sup>_X_0</sup><sup>_X_1</sup><sup>_X_</sup> 2<sup>2</sup><sup>_X_3+</sup><sup>_X_</sup> 2<sup>3+</sup><sup>_X_</sup> 4<sup>4</sup>

_E_ 4[ _Y |X_ ] = _X_ 7 _X_ 25 _X_ 31 _X_ 59 _X_ 63 _X_ 68 _X_ 70 _X_ 83 _X_ 88 _X_ 98 + _X_ 0 _X_ 32 _X_ 47 _X_ 54 _X_ 66 _X_ 72 _X_ 73 _X_ 77 + _X_ 82 + _X_ 7 _X_ 49 _X_ 55 _X_ 73 _X_ 80 + _X_ 33 _X_ 40 + _X_ 18 _X_ 21 _X_ 40 _X_ 56 _X_ 59 _X_ 71 _X_ 91 + _X_ 9 _X_ 13 _X_ 18 _X_ 20 _X_ 41 _X_ 53 _X_ 69 _X_ 95 + _X_ 3 _X_ 38 _X_ 78 _X_ 96 + _X_ 0 _X_ 20 _X_ 64 _X_ 88 _X_ 91 _X_ 96 + _X_ 2 _X_ 6 _X_ 16 _X_ 37 _X_ 45 _X_ 46 _X_ 61 _X_ 68 _X_ 91 _X_ 95

Page 274

The following quantities are used in the next table:

- _RSSn_ : _RSS/_ ( _n − k_ ) represents the estimate of the variance of the error where k is the number of independent variables in fitted model

- _RSS_ 0: the RSS of the true model

- *: indicates the model for which _ε ∼N_ (0 _,_ 1)

Page 275

#### Comparing _ε_ = 0 to _ε ∼N_ (0 _,_ 1)*

|_E_[_Y |X_]|X|n|d|_p_|_RSSn_|_RSS_0|
|---|---|---|---|---|---|---|
|_E_3[_Y |X_]|_N_(5_,_0_._25)|1000|5|1.0|0.0000|0.0000|
|_E_3[_Y |X_]<sup>_∗_</sup>|_N_(5_,_0_._25)|10000|5|1.0|0.9886|0.9890|
|_E_4[_Y |X_]|_N_(5_,_0_._25)|1000|100|1.0|0.0000|0.0000|
|_E_4[_Y |X_]<sup>_∗_</sup>|_N_(5_,_0_._25)|10000|100|1.0|0.9955|0.9961|


Page 276

**DSA ALGORITHM VERSUS stepAIC() R-FUNCTION** The DSA algorithm creates variables data-adaptively and therefore does not require enumeration of all potential variables. The stepAIC() for linear regression does require enumeration of all variables. To compare the two black-box algorithms (data _→_ predictor), we enumerated all main terms and two way interactions. The following three true regression models were generated where _Xj ∼U_ (1 _,_ 10), _j_ = 1 _, . . . , d_ , and _ε ∼N_ (0 _,_ 1). _E_ 1[ _Y |X_ ] = _X_ 1 + _X_ 2<sup>2</sup>

_E_ 2[ _Y |X_ ] = _X_ 1 _X_ 3

_E_ 3[ _Y |X_ ] = _X_ 1 _X_ 3 + _X_ 5<sup>2+</sup><sup>_X_7</sup><sup>_X_10</sup>

Page 277

The following quantities are represented in the table:

- _k_<sup>ˆ</sup> : size of the final fitted model for each method

- RISK: estimate of the true risk, based on 20,000 independent observations, of the final model given by both methods

Page 278

##### COMPARING `STEP-AIC` and CV-DSA

|_E_[_Y |X_]|n|d|ˆ_kAIC_|ˆ_kCV_|STEP-AIC|DSA-CV|
|---|---|---|---|---|---|---|
|_E_1[_Y |X_]|5000|3|2|2|0.9963|0.9963|
|_E_2[_Y |X_]|5000|10|19|1|0.9995|0.9932|
|_E_3[_Y |X_]|5000|10|22|3|1.0174|1.0106|


Page 279

#### **PROPOSAL FOR PARTITION-MOVES**

Given a partition _I_ 0 = _{R_ 1 _, . . . , Rk}_ of the covariate space _W_ , we propose the following moves.

**deletion moves:** Replace two indicators _IRi, IRj_ of sets _Ri, Rj_ by the indicator _IRi∪Rj_ of the union _Ri ∪ Rj_ .

**substitution moves:** See below.

**addition moves:** Replace an indicator _IRi_ of a set _Ri_ by two indicators of _Ri ∩{Wl < c}_ and _Ri ∩{Wl > c}_ .

Page 280

#### **POSSIBLE SUBSTITUTIONS**


<!-- Start of picture text -->
r s1 r s2<br>1.<br>r 1 a b c d<br>2.<br>a b d c<br>a b<br>3.<br>c d a b<br>r 2<br>4.<br>c d b a<br>c d<br>5.<br>a c b d<br>6.<br>a d b c<br><!-- End of picture text -->

Page 281


<!-- Start of picture text -->
x1<br>x2<br>Beta<br><!-- End of picture text -->

Page 282

#### **INDICATOR OF SET REPRESENTATION**


<!-- Start of picture text -->
(a111,b111] (a121,b121] (a11m,b11m]<br>and and and<br>(a211,b211] (a221,b221] (a21m,b21m]<br>and and and<br>. . . or . . . or . . . or . . .<br>. . . . . . . . .<br>. . . . . . . . .<br>and and and<br>(ap11,bp11] (ap21,bp21] (ap1m,bp1m]<br><!-- End of picture text -->

Page 283

**DSA vs. RECURSIVE PARTITIONING**

Page 284

Table 10: 100 repetitions of full data simulated from _y_ = _x_<sup>2</sup> + _er_ , where _x ∼ N_ (0 _,_ 1) and _er ∼ N_ (0 _, ._ 25). Conditional risk of our method ( _ours_ ), rpart (R-implementation of CART) with 1-SE ( _rpart_ ) and rpart by minimizing CV-error ( _rpart0_ ).

|_n_|Method|Mean|Std.Dev.|Avg. size|Ratio|
|---|---|---|---|---|---|
||ours|0.26125|0.09384|7.44|1|
|250|rpart|0.45305|0.14195|5.69|.577|
||rpart0|0.35172|0.09927|14.45|.743|
||ours|0.18935|0.07318|9.95|1|
|500|rpart|0.27216|0.08574|9.55|.696|
||rpart0|0.22187|0.07544|21.26|.853|
||ours|0.14080|0.04016|12.06|1|
|1000|rpart|0.18489|0.05206|13.02|.762|
||rpart0|0.15403|0.04916|28.44|.914|


Page 285

#### **PREDICTING GENE EXPRESSION FROM SEQUENCE**


<!-- Start of picture text -->
Gene<br>...ACGTACACGTAAACGTTACTGTAATTTACGTGGACAAA......<br>Expression<br>Motif A Motif B Motif C<br><!-- End of picture text -->

Goal: To identify binding sites (regulatory motifs). n

Data:

- Gene Expression Data: _P × N_ matrix with entries _Yij, i_ = 1 _, · · · , P, j_ = 1 _, · · · , N_ . _Yij_ is the logarithm of the relative gene expression for gene _i_ in experiment _j_ .

- Upstream Control Region <u>(UCR):</u> Roughly 600 to 1000 base pairs of the gene start site.

Page 286

WHAT ARE BINDING SITES AND WHY ARE THEY IMPORTANT?

DNA binding proteins (transcription factors) bind to DNA in a sequence specific manner. These short DNA sequences (5-25 base pairs) are called binding sites or regulatory motifs. All cells from bacteria to mammals respond to various treatments by activating or repressing the expression of particular genes. Gene expression is regulated by transcription factors binding selectively to their specific binding sites.

Page 287

#### **GAL4 BINDING**

From `http://www.cryst.bbk.ac.uk/PPS2/.`

Page 288

#### **CELL CYLE IN YEAST**

We used the DSA algorithm with polynomial basis to regress the 512 = 1024 _/_ 2 indicators of “Presence of length 5 motiff” on gene expression at each time-point in the 16 time point cell cycle experiment in yeast (Cho et al., 1998).

In the DSA algorithm we use 2-fold cross-validation, maximal size of model _K_ = 5, and Subset Estimator 1 for the subset _I_ of basis functions.

Page 289

||**T=**|**30 min**|||
|---|---|---|---|---|
|ˆ_kCV_|Run time|ˆ<br>_θfull_|ˆ<br>_θmain_|ˆ<br>_θfull/_<sup>ˆ</sup><br>_θmain_|
|3|6.2 hrs|1176.144|1176.746|0.999|
|Selected pentamers|�_n_<br>_i_=1|<sup>_Xi,_</sup><br>_Xi_ =|_{_0_,_1_}_||
|_•_ ACGCG [MCB]||774|||
|_•_ 10-way interaction:||60|||
|AAATC||2116|||
|AACTA||2023|||
|AATAT||2492|||
|ACAAA||2410|||
|ACGCG [MCB]||774|||
|AGCCG||937|||
|ATGAA||2207|||
|CAAGA||2051|||
|CCACC||960|||
|GAAAC||1967|||
|_•_ 10-way interaction:||26|||
|AACTT||2150|||
|ACGCG [MCB]||774|||
|AGATA||2127|||
|AGCAA||2009|||
|ATAAC||2027|||
|ATATG||2122|||
|CTGCC||1078|||
|CTGTC||1188|||
|GGCCC||615|||
|TGACA||1603|||


Page 290

||**T**|**=50 min**|||
|---|---|---|---|---|
|ˆ_kCV_|Run time|ˆ<br>_θfull_|ˆ<br>_θmain_|ˆ<br>_θfull/_<sup>ˆ</sup><br>_θmain_|
|1|10.9 hrs|1149.242|1138.828*|1.009|
|Selected pentamers|�_n_<br>_i_=1|<sup>_Xi,_</sup><br>_Xi_ =|_{_0_,_1_}_||
|_•_ 15-way interaction:||62|||
|AAGAG||2120|||
|AAGCA||1994|||
|AAGGA||2118|||
|AATCA||2038|||
|ACAAA||2410|||
|AGGAA *||2146|||
|AGGCC||798|||
|AGTGG||1278|||
|ATTCA||2022|||
|ATTTA||2398|||
|CAACA||1852|||
|GATTA||1811|||
|GCTTA||1522|||
|TACTA||2002|||
|TGGAA||1915|||


Page 291

||**T=70 min**|||
|---|---|---|---|
|ˆ_kCV_|Run time<br>ˆ<br>_θfull_|ˆ<br>_θmain_|ˆ<br>_θfull/_<sup>ˆ</sup><br>_θmain_|
|4|8.4 hrs<br>1296.356|1295.034*|1.001|
|Selected pentamers|�_n_<br>_i_=1 <sup>_Xi,_</sup><br>_Xi_ =|_{_0_,_1_}_||
|_•_ 2-way interaction:|2590|||
|AAAAG|2676|||
|GAAAA [ECB]|2676|||
|_•_ 4-way interaction:|676|||
|AAAAT|2679|||
|AAACA *[STE 12]|2406|||
|AAATA|2649|||
|ACGCG [MCB]|774|||
|_•_ 11-way interaction:|103|||
|AAAAG|2676|||
|AAACA [STE 12]|2406|||
|AATTG|2059|||
|ACATG|1300|||
|ATAAA|2609|||
|ATACG|1480|||
|ATATA|2434|||
|CGCGA|743|||
|GAATA|2213|||
|GTTCA|1545|||
|TCAAA|2326|||


Page 292

||**T=**|**70 min**|||
|---|---|---|---|---|
|ˆ_kCV_|Run time|ˆ<br>_θfull_|ˆ<br>_θmain_|ˆ<br>_θfull/_<sup>ˆ</sup><br>_θmain_|
|4|8.4 hrs|1296.356|1295.034*|1.001|
|Selected pentamers|�_n_<br>_i_=1|<sup>_Xi,_</sup><br>_Xi_ =|_{_0_,_1_}_||
|_•_ 15-way interaction:||49|||
|AAAAT||2679|||
|ACGCG [MCB]||774|||
|AAACA [STE 12]||2406|||
|AAATA||2649|||
|AACAC||1670|||
|AACAG||1895|||
|AATCC||1370|||
|AGGTG||1290|||
|CAAAA||2538|||
|CTTCA||1912|||
|GATAA||2069|||
|GGAAA||2312|||
|GGGAA||1631|||
|TATCA||2120|||
|TGTAA||2102|||


Page 293

||**T=**|**110 min**|||
|---|---|---|---|---|
|ˆ_kCV_|Run time|ˆ<br>_θfull_|ˆ<br>_θmain_|ˆ<br>_θfull/_<sup>ˆ</sup><br>_θmain_|
|1|11.8 hrs|1245.625|1232.567*|1.011|
|Selected pentamers|�_n_<br>_i_=1|<sup>_Xi,_</sup><br>_Xi_ =|_{_0_,_1_}_||
|_•_ 9-way interaction:||178|||
|AAAAT||2679|||
|AAACA [STE 12]||2406|||
|AAAGT||2349|||
|AATAG||2247|||
|ACGCG *[MCB]||774|||
|AGAAG||2150|||
|ATAAG||2095|||
|GACGC||855|||
|TCTCA||1695|||


Page 294

**PREDICTION OF SURVIVAL with CV-DSA**

Let _T_ be a log-survival time, and suppose that our goal is to estimate the optimal predictor _ψ_ 0( _W_ ) = _E_ 0( _T | W_ ). However, due to right-censoring by a variable _C_ , we only observe _Oi_ = ( _T_<sup>˜</sup> _i ≡_ min( _Ti, Ci_ ) _,_ ∆ _i_ = _I_ ( _Ti ≤ Ci_ ) _, Wi_ ). Let _G_ ( _· | T, W_ ) be the conditional distribution of censoring _C_ , given ( _T, W_ ), and we assume that censoring is independent of survival time, given _W_ : i.e., _G_ ( _· | T, W_ ) = _G_ ( _· | W_ ).

The CV-DSA algorithm above for estimating the optimal predictor _ψ_ 0( _W_ ) based on the full (uncensored) data ( _Ti, Wi_ ), _i_ = 1 _, . . . , n_ , is 100% driven by the squared error loss function _L_ ( _T, W, ψ_ ). We can replace in the CV-DSA the squared error loss function _L_ ( _T, W, ψ_ ) by a function of the observed data _O_ with the same expectation.

Page 295

The **Inverse Probability of Censoring Weighted** (IPCW) Squared Error Loss Function ∆ ∆ _L_ ( _O, ψ | G_ ) _≡ L_ ( _T, W, ψ_ ) _PG_ (∆= 1 _| W_ )<sup>= (</sup><sup>_T−ψ_(</sup><sup>_W_))2</sup> _G_ <u>¯(</u> _T | W_ )<sup>_._</sup>

For the optimal (that is, minimal variance, and maximally robust) **double robust IPCW loss function** , we refer to van der Laan, Robins (2002).

**Remark** Given an estimator _G_ ( _Pn_ ) (e.g., Kaplan-Meier, or Cox-proportional hazards) of the censoring distribution _G_ , the cross-validation selector is now given by: _n_ ∆ _i k_ ˆ = argmin _k_ � _I_ ( _Sn_ ( _i_ ) = 1)( _Ti−ψk_ ( _Wi | Pn,S_<sup>0</sup> _n_<sup>))2</sup> _i_ =1 _G_ <u>¯(</u> _Pn,S_<sup>0</sup> _n_<sup>)(</sup><sup>_Ti| Wi_)</sup><sup>_._</sup>

Page 296

#### **CONCLUDING REMARKS**

_•_ Cross-validated DSA algorithms provide black-box algorithms for estimating parameters which minimize the expectation of a given loss function (e.g., regression, conditional density, conditional survival function).

_•_ Simulations show that the DSA-algorithm is asymptotically surprisingly capable of truly minimizing the cross-validated/empirical risk function over all subsets of basis functions.

- In complex (i.e., genomic) studies we should let cross-validation make the choices: e.g, if we choose the parametrization/basis with cross-validation, then the estimator becomes adaptive to the truth.

- Any such algorithm is immediately generalizable to censored data by replacing the full-data loss function by the (double

Page 297

robust) IPCW loss function.

Page 298

#### **SIMULATIONS**

Consider the nonparametric polynomial regression (NPR) model for _E_ [ _Y |X_ ], defined by the collection of sums of tensor-product polynomial basis functions:


To assess the DSA algorithm’s ability to minimize residual sum of squares over this NPR-model, we randomly generated true regressions in this NPR-model and set _ϵ_ = 0, and verified if the algorithm found the truth.

Page 299

The true regression model is randomly generated as follows: _size ∼U{_ 1 _, . . . ,_ 5 _}_ � _d ps_ ( _j_ ) _∼U{_ 1 _, . . . ,_ 5 _} j_ =1 _ps ∼_ Multinomial(<sup>�</sup><sup>_d_</sup> _j_ =1<sup>_ps_(</sup><sup>_j_)</sup><sup>_, d,_(</sup> _d_<sup><u>1</u></sup><sup>_, . . . ,_</sup> _d_<sup><u>1</u>))</sup> After randomly choosing _size_ and _⃗ps_ , each formed<sup>�</sup> _j_<sup>_X_</sup> _j_<sup>_ps_(</sup><sup>_j_)</sup> tensor-product was ensured to be unique. The sum of these randomly generated unique terms and _ε_ yielded the true response variable _Y_ .

Page 300

#### **REPORTED QUANTATIES**

The following quantities are represented in the tables summarizing simulation results:

- _p_ : proportion of correctly fitted terms given the true model

- _• p_ ¯: average proportion of correctly fitted terms across the number of repetitions

- _RSS_ : residual sum of squares of fitted model

- _RSS_ : average RSS across the number of repetitions

Page 301

#### **Simulation Results for Randomly Generated Polynomials**

#### Zero error

|X|n|d|nsims|¯_p_|_RSS_|
|---|---|---|---|---|---|
|_U_(0_,_1)|1000|5|1000|1.000|0.0000|
|_U_(0_,_1)|1000|100|500|1.000|0.0000|
|Bernoulli(p)|1000|5|100|0.996|0.0000|
|Bernoulli(p)|2000|10|100|0.921|0.0000|
|Bernoulli(p)|1000|25|100|0.884|0.0000|
|Bernoulli(0.6)|500|5|100|1.000|0.0000|
|Bernoulli(0.6)|500|25|100|1.000|0.0000|


Page 302

**Simulations: Increase complexity of true regression**

In the previous simulations, _size ∼U{_ 1 _, . . . ,_ 5 _}_ , but now we increase both the size and the allowed sum of the powers of the polynomials within a tensor product as follows: _size ∼U{_ 1 _, . . . ,_ 10 _}_ , � _d ps_ ( _j_ ) _∼U{_ 1 _, . . . ,_ 20 _}_ , with _d_ = 100. In _j_ =1 these simulations, _RSS ≤_ 0 _._ 000001 was used as a stopping criterion.

Page 303

The following three true regression models were generated: _E_ 1[ _Y |X_ ] = _X_ 1 _X_ 12 _X_ 13<sup>2</sup><sup>_X_</sup> 22<sup>_X_</sup> 24<sup>_X_</sup> 54<sup>_X_</sup> 79<sup>_X_</sup> 83<sup>_X_</sup> 95<sup>+</sup><sup>_X_</sup> 15<sup>_X_</sup> 18<sup>_X_</sup> 37<sup>_X_</sup> 42<sup>_X_</sup> 68<sup>+</sup> _X_ 6 _X_ 22 _X_ 33<sup>3</sup><sup>_X_</sup> 40<sup>_X_</sup> 58<sup>_X_</sup> 75<sup>_X_</sup> 82<sup>_X_</sup> 87<sup>+</sup><sup>_X_</sup> 15<sup>_X_</sup> 31

_E_ 2[ _Y |X_ ] =

_X_ 7 _X_ 25 _X_ 31 _X_ 59 _X_ 63 _X_ 68 _X_ 70 _X_ 83 _X_ 88 _X_ 98 + _X_ 0 _X_ 32 _X_ 47 _X_ 54 _X_ 66 _X_ 72 _X_ 73 _X_ 77 + _X_ 82 + _X_ 7 _X_ 49 _X_ 55 _X_ 73 _X_ 80 + _X_ 33 _X_ 40 + _X_ 18 _X_ 21 _X_ 40 _X_ 56 _X_ 59 _X_ 71 _X_ 91 + _X_ 9 _X_ 13 _X_ 18 _X_ 20 _X_ 41 _X_ 53 _X_ 69 _X_ 95 + _X_ 3 _X_ 38 _X_ 78 _X_ 96 + _X_ 0 _X_ 20 _X_ 64 _X_ 88 _X_ 91 _X_ 96 + _X_ 2 _X_ 6 _X_ 16 _X_ 37 _X_ 45 _X_ 46 _X_ 61 _X_ 68 _X_ 91 _X_ 95

Page 304

#### **Simulation Results for Two Models**

Zero error X n d _RSS E_ [ _Y |X_ ] _p E_ 1[ _Y |X_ ] _U_ (0 _,_ 1) 1000 100 1.0 0.000000 _E_ 2[ _Y |X_ ] _U_ (0 _,_ 1) 1000 100 1.0 0.000000

Page 305

**Comparing** _ε_ = 0 **to** _ε ∼N_ (0 _,_ 1)

The following two models were generated, first with _ε_ = 0 and then with _ε ∼N_ (0 _,_ 1). _E_ 3[ _Y |X_ ] = _X_ 0 _X_ 1<sup>2</sup><sup>_X_</sup> 2<sup>2+</sup><sup>_X_0</sup><sup>_X_1</sup><sup>_X_</sup> 2<sup>2</sup><sup>_X_3+</sup><sup>_X_</sup> 2<sup>3+</sup><sup>_X_</sup> 4<sup>4</sup>

_E_ 4[ _Y |X_ ] = _X_ 7 _X_ 25 _X_ 31 _X_ 59 _X_ 63 _X_ 68 _X_ 70 _X_ 83 _X_ 88 _X_ 98 + _X_ 0 _X_ 32 _X_ 47 _X_ 54 _X_ 66 _X_ 72 _X_ 73 _X_ 77 + _X_ 82 + _X_ 7 _X_ 49 _X_ 55 _X_ 73 _X_ 80 + _X_ 33 _X_ 40 + _X_ 18 _X_ 21 _X_ 40 _X_ 56 _X_ 59 _X_ 71 _X_ 91 + _X_ 9 _X_ 13 _X_ 18 _X_ 20 _X_ 41 _X_ 53 _X_ 69 _X_ 95 + _X_ 3 _X_ 38 _X_ 78 _X_ 96 + _X_ 0 _X_ 20 _X_ 64 _X_ 88 _X_ 91 _X_ 96 + _X_ 2 _X_ 6 _X_ 16 _X_ 37 _X_ 45 _X_ 46 _X_ 61 _X_ 68 _X_ 91 _X_ 95

Page 306

The following quantities are used in the next table:

- _RSSn_ : _RSS/_ ( _n − k_ ) represents the estimate of the variance of the error where k is the number of independent variables in fitted model

- _RSS_ 0: the RSS of the true model

- *: indicates the model for which _ε ∼N_ (0 _,_ 1)

Page 307

#### Comparing _ε_ = 0 to _ε ∼N_ (0 _,_ 1)*

|_E_[_Y |X_]|X|n|d|_p_|_RSSn_|_RSS_0|
|---|---|---|---|---|---|---|
|_E_3[_Y |X_]|_N_(5_,_0_._25)|1000|5|1.0|0.0000|0.0000|
|_E_3[_Y |X_]<sup>_∗_</sup>|_N_(5_,_0_._25)|10000|5|1.0|0.9886|0.9890|
|_E_4[_Y |X_]|_N_(5_,_0_._25)|1000|100|1.0|0.0000|0.0000|
|_E_4[_Y |X_]<sup>_∗_</sup>|_N_(5_,_0_._25)|10000|100|1.0|0.9955|0.9961|


Page 308

**DSA ALGORITHM VERSUS stepAIC() R-FUNCTION** The DSA algorithm creates variables and therefore does not require enumeration of all potential variables.

The stepAIC() for linear regression does require enumeration of all variables. To compare the two black-box algorithms (data _→_ model fit), we enumerated all main terms and two way interactions.

The following three true regression models were generated where _Xj ∼U_ (1 _,_ 10), _j_ = 1 _, . . . , d_ , and _ε ∼N_ (0 _,_ 1). _E_ 1[ _Y |X_ ] = _X_ 1 + _X_ 2<sup>2</sup>

_E_ 2[ _Y |X_ ] = _X_ 1 _X_ 3

_E_ 3[ _Y |X_ ] = _X_ 1 _X_ 3 + _X_ 5<sup>2+</sup><sup>_X_7</sup><sup>_X_10</sup>

Page 309

The following quantities are represented in the table:

- _k_<sup>ˆ</sup> : size of the final fitted model for each method

- _θ_<sup>ˆ</sup> _opt_ : estimate of the true risk, based on 20,000 independent observations, of the final model given by both methods

Page 310

##### Comparing `stepAIC` to Cross-Validated Del/Sub/Add

|_E_[_Y |X_]|n|d|ˆ_kR_|ˆ_kCV_|ˆ_θopt,R_|ˆ_θopt,CV_|
|---|---|---|---|---|---|---|
|_E_1[_Y |X_]|5000|3|2|2|0.9963|0.9973|
|_E_2[_Y |X_]|5000|10|19|1|0.9995|0.9932|
|_E_3[_Y |X_]|5000|10|22|3|1.0174|1.0106|


Page 311

---

[Up: contents](index.md) · [CROSS-VALIDATED ϵ -NET ESTIMATOR →](02-cross-validated-ϵ--net-estimator.md)
