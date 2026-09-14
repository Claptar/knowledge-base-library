---
title: 1. Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2022/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1. Introduction

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In many longitudinal studies, measurements are taken at irregularly spaced and sparse time points. The sparsity refers to the availability of only a few observations per subject. In the classical longitudinal set-up, a small number of measurements of response and covariates are synchronized within individuals, meaning that they are observed at the same time points, with the measurement times varying across individuals. However, in many applications, observed covariates and response variables may be mismatched over time within individuals, leading to asynchronous data. This greatly complicates the study of the association between response and covariates, with virtually all available longitudinal regression methods developed for the synchronous setting.

Often no synchronous data may be available and existing methods are not applicable to asynchronous data. In educational studies, it is of interest to associate subjective evaluations of students’ performance and objective test results. However, subjective information is usually collected through interviews or phone calls, which are obtained at different time points. In clinical epidemiology, one may study the links between biomarkers, sampled repeatedly at

_Address for correspondence_ : Jason P. Fine, Department of Biostatistics, University of North Carolina at Chapel Hill, 3103B McGavran–Greenberg Hall, Chapel Hill, NC 27599-3260, USA. E-mail: jfine@bios.unc.edu

© 2014 Royal Statistical Society

1369–7412/15/77755

756 _H. Cao, D. Zeng and J. P. Fine_


**Fig. 1.** Observation times of CD4 cell counts ( ) and HIV viral load ( ) by patient

laboratory visits, with self-reported measures of function and quality of life, captured via outpatient phone interviews. In other clinical settings, the relationship between two biomarkers may be of interest, with laboratory visits scheduled at different times by design to address logistical issues which prevent their simultaneous observation. As an example, in a prospective observational cohort study (Wohl _et al._ , 2005), a total of 191 patients were followed for up to 5 years, with human immunodeficiency virus (HIV) viral load and CD4 cell counts measured repeatedly on these patients. Fig. 1 displays the observation times for the two variables: we see clearly that sparse measurements are taken on each variable for each subject and that the study protocol has specified that the viral load and CD4 cell count are obtained at laboratary visits on different days. Hence, there are no synchronous data within individuals, as would be needed by the existing methods. It is well known in the medical literature that HIV viral load and CD4 cell counts are negatively associated (Hoffman _et al._ , 2010). The _ad hoc_ but commonly adopted last value carried forward approach which employs synchronous data methods does not identify this association in the data analysis in Section 5.

The goal of this paper is to develop simple, computationally efficient and theoretically justified estimators for longitudinal regression models based on such sparse asynchronous data. A popular regression model for longitudinal data with time varying response and covariates is the generalized linear model


where _g_ is a known, strictly increasing and continuously twice-differentiable link function, t

_Analysis of Asynchronous Data_ 757

is a univariate time index, X.t/ is a vector of time varying covariates plus intercept term, Y.t/ is a time varying response and _β_ is an unknown time invariant regression parameter. Model (1) characterizes the conditional mean of Y.t/ given X.t/ while leaving its dependence structure and distributional form completely unspecified. Existing methodology (Diggle _et al._ (2002) and references therein) for model (1) assumes that X and Y are observed at the same time points within individuals, with the resulting estimators based on this synchronous data being n<sup>1=2</sup> consistent and asymptotically normal. To our knowledge, estimation via generalized estimating equations (Diggle _et al_ ., 2002) has not been studied with asynchronous data and it is unclear whether parametric rates of convergence are achievable.

A more flexible model is the generalized varying-coefficient model that allows the unknown regression coefficient _β_ .t/ to vary over time in model (1):


For the identity link function, as recently reviewed by Fan and Zhang (2008), estimation for sparse synchronous longitudinal data may be based on two main approaches: global and local. Local methods, which include local likelihood, may be based on local polynomial smoothing (Wu _et al._ , 1998; Hoover _et al._ , 1998; Fan and Zhang, 2000; Wu and Chiang, 2000). Global approaches employ alternative basic function representations for the data and regression coefficients, such as polynomial spline (Huang _et al._ , 2002, 2004), smoothing spline (Hoover _et al._ , 1998; Chiang _et al._ , 2001; Fan and Zhang, 2000) and functional data analytic approximations (Yao _et al._ , 2005; Zhou _et al._ , 2008; Sent¨urk and Muller, 2010; Zhou _et al._ , 2008). Interestingly, whereas the optimal non-parametric rates of convergence for estimation of _β_ .t/ are the same for the local and global approaches with sparse longitudinal data, the global approaches can incorporate within-subject correlation structure in the estimation procedure, similarly to generalized estimating equations (Diggle _et al._ , 2002). Qu and Li (2006) employed penalized splines with quadratic inference functions. Fan _et al._ (2007) studied non-parametric estimation of the covariance function. Other related work can be found in Sun _et al._ (2007) and references therein. Establishing efficiency gains for the global approaches is challenging for the time-dependent parameter estimators, owing to slow rates of convergence.

Hybrids of models (1) and (2) have been widely investigated with synchronous longitudinal data, where some of the regression parameters are time invariant and some are time dependent. The so-called partial linear model is a variant in which the intercept term is time varying whereas other coefficients are constant. In general, the time-independent parameter may be estimated at the usual parametric rates. An important discovery that was made by Lin and Carroll (2001) is that the commonly used forms of the kernel methods cannot incorporate within-subject correlation to improve efficiency of the time invariant parameter estimator. Wang (2003) proposed an innovative kernel method, which assumes knowledge of the true correlation structure, yielding efficiency gains. The idea was extended by Wang _et al._ (2005) to achieve the semiparametric efficientboundthatwascomputedinLinandCarroll(2001)forthetime-independentparameter. A counting process approach on the observation time was adopted by Martinussen and Scheike (1999, 2001), Cheng and Wei (2000) and Lin and Ying (2001), which enables n<sup>1=2</sup> -consistent estimation of the time-independent parameter without explicit smoothing.

In this paper, we propose estimators for models (1) and (2) with asynchronous longitudinal data. Extending Martinussen and Scheike’s (2010) representation of synchronous data, we formulate the observation process by using a bivariate counting process for the observation times of the covariate and response variables. For subject i = 1, ::: , n,


758 _H. Cao, D. Zeng and J. P. Fine_

counts the number of observation times up to t on the response and up to s on the covariates, where Tij, j = 1, ::: , Li, are the observation times for the response and Sik, k = 1, ::: , Mi, are the observation times for the covariates, i.e., with sparse asynchronous longitudinal data, we observe for i = 1, ::: , n


where Li and Mi are finite with probability 1. To use existing methods for synchronous longitudinal data, where Li = Mi and Tij = Sij, j = 1, ::: , Li, for each observed response, one may carry forward the most recently observed covariate. As evidenced by the numerical studies in Sections 4 and 5, this _ad hoc_ approach may incur substantial bias.

To obtain estimators for models (1) and (2) with asynchronous data, we adapt local kernel weighting techniques to estimating equations that have previously been developed for synchronous data. Our main idea is intuitive: we downweight those observations which are distant in time, either from each other or from a known fixed time. This enables the use of all covariate observations for each observed response. These methods require similar smoothness assumptions on the covariate trajectories to those employed with synchronous data. In practice, there may be scenarios where it is necessary to preprocess the covariate X.t/ when applying the methodologies ofthepaper.Withasuitablechoiceofthebandwidthcontrollingthekernelweighting,theestimators for the time invariant coefficient and time-dependent coefficient are shown to be consistent and asymptotically normal, with simple plug-in variance estimators. The usual cross-validation for bandwidth selection does not work because the data are non-synchronous but we develop a novel data-adaptive bandwidth selection procedure which works well in simulation studies. The choice of the local method _versus_ a global method is based in part on computational and inferential simplicity and, in part, by the fact that it is unclear that efficiency gains are achievable given the slow rates of convergence of the estimators. The optimal rates of convergences for our local estimators for models (1) and (2) with asynchronous data are slower than the corresponding optimal rates which may be achieved with synchronous data. In addition, the estimator for the time-independent model converges more slowly than the parametric rate n<sup>−1=2</sup> for synchronous data. Given this lack of n<sup>−1=2</sup> -consistency, the extent to which efficiency gains with synchronous data for time-independent parameter estimation by using global methods carry over to the asynchronous setting is not obvious. These results are detailed in Sections 2 and 3.

The remainder of the paper is organized as follows. In Section 2, we discuss estimation for model (1) with time-independent coefficients by using asynchronous data and provide the corresponding theoretical findings. The results for the time-dependent model (2) are given in Section 3. Section 4 reports simulation studies and Section 5 applies our procedure to data from the HIV study, exhibiting improved performance _versus_ the last value carried forward approach with synchronous data methods. Concluding remarks are given in Section 6. Proofs of results from Sections 2 and 3 are given in Appendix A.

The data that are analysed in the paper and the programs that were used to analyse them can be obtained from

http://wileyonlinelibrary.com/journal/rss-datasets

---

[← Hongyuan Cao](01-hongyuan-cao.md) · [Up: contents](index.md) · [2. Time invariant coefficient →](03-2-time-invariant-coefficient.md)
