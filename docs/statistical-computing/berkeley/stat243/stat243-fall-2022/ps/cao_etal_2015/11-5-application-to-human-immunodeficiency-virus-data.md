---
title: 5. Application to human immunodeficiency virus data
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2022/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5. Application to human immunodeficiency virus data

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We now illustrate the proposed inferential procedures for models (1) and (2) with a comparison with the last value carried forward approach on data from the HIV study that was described in Section 1. A total of 190 HIV patients were followed from July 1997 to September 2002. Details of the study design, methods and medical implications are given in Wohl _et al_ . (2005). During this study, all patients were scheduled to have their measurements taken during semiannual visits, with HIV viral load and CD4 cell counts obtained separately at different laboratories. Because many patients missed visits and the HIV infection occurred randomly during the study, there are unequal numbers of repeated measurements on viral load and CD4 cell count and there are different measurement times for the two variables. These data are sparse and purely asynchronous.

In our analysis, we took the CD4 cell counts as the covariate and HIV viral load as the response. Both CD4 cell count and HIV viral load are continuous variables with skewed distribution. As is customary, we log-transformed these variables before the analysis. Since the measurement timescale is not in Unif.0,1/, we use the interquantile range to do adjustment. We

_Analysis of Asynchronous Data_

767

**Table 4.** Summary statistics for _β_<sup>ˆ</sup> 1 based on model (11)

|_Parameter_|_R_|_esults for the fo_|_llowing values_|_of_ h_(_n<sup>−</sup><sup>_γ_</sup>_):_||
|---|---|---|---|---|---|
||_289(_n<sup>−0:3</sup>_)_|_101(_n<sup>−0:5</sup>_)_|_35(_n<sup>−0:7</sup>_)_|_134(auto)_|_lvcf_|
|ˆ_β_1|−1.182|−1.130|−1.074|−1.178|0.003|
|SE. <sup>ˆ</sup>_β_1/|0.685|0.832|1.143|0.816|1.806|
|z-value|−1.727|−1.359|−0.940|−1.444|0.0001|


first fit model (1) with bandwidths h = 2.Q3 − Q1/n<sup>−</sup><sup>_γ_</sup> , where Q3 is the 0.75-quantile and Q1 is the 0.25-quantile of the pooled sample of measurement times for the covariate and response, n is the number of patients and _γ_ = 0:3,0:5,0:7. The time-independent coefficient model is


Coefficient estimates were obtained by the estimating equation (3) based on different bandwidths and data-driven bandwidth selection procedure, auto. For comparison, we also use the last value carried forward approach, lvcf, for coefficient estimation. The resulting estimates and standard errors are given in Table 4.

FromTable4,usingtheestimatesfromequation(3),wecanclearlyseethenegativerelationship between CD4 cell counts and HIV viral load, which has been verified in earlier medical studies. For different choices of bandwidth, the point estimate does not change much, but the variance decreases as the bandwidth increases, as expected. Overall, on the basis of these analyses, there appears to be at least some evidence that CD4 cell count and HIV viral load are associated. In contrast, the last value carried forward approach suggests a very weak positive association, in a direction which is opposite to that observed in previous studies and in the current analysis using estimating equation (3).

To investigate whether the relationship between CD4 cell counts and HIV viral load varies over time, we fit the varying-coefficient model


In Fig. 2, we depict the coefficient estimates and 95% confidence intervals based on automatic bandwidth selection. From the plot, we see that the negative association is relatively constant over time and comparable in magnitude with that obtained under model (11). The pointwise intervals cover 0 at all time points. The results seem to support the use of a simpler model based on an assumption of time-independent regression parameters.

To check conditions 1 and 1<sup>′</sup> on the observation intensity, one may construct plots of the observation times. For condition 1, a histogram (which has been omitted) of the differences between Tij and the closest Sik was roughly normal and centred near 0, suggesting that the assumption holds in this data set. For condition 1<sup>′</sup> , we plotted Tij _versus_ Sik (which has been omitted) and found that, for time points between 400 and 1400, there was sufficient information on the diagonal where s = t to permit estimation of _β_ .t/:

---

[← 4.3. Comparison with last value carried forward method](10-4-3-comparison-with-last-value-carried-forward-method.md) · [Up: contents](index.md) · [6. Concluding remarks →](12-6-concluding-remarks.md)
