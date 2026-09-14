---
title: 4.2. Time-dependent coefficient
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2022/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.2. Time-dependent coefficient

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We next study the properties of the estimator for the time-dependent coefficient in model (2). We consider a wide range of functional forms, including _β_ .t/ = 0:4t + 0:5, _β_ .t/ = sin.2 _π_ t/ and _β_ .t/ = t<sup>1=2</sup> . The responses were generated from the model


_Analysis of Asynchronous Data_ 765

**Table 1.** Simulation results with time invariant coefficient for the linear and logistic models

|_n_|_BD_|_Re_|_sults for li_|_near regr_|_ession mo_|_del_|_Res_|_ults for logi_|_stic regre_|_ssion mo_|_del_|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||_Bias_|_RB_|_SD_|_SE_|_CP (%)_|_Bias_|_RB_|_SD_|_SE_|_CP (%)_|
|100|n<sup>−0:5</sup><br>|−0.056|−0.038|0.119|0.107|88|−0.069|−0.046|0.210|0.204|92|
||n<sup>−0:6</sup><br>|−0.036|−0.024|0.125|0.111|90|−0.023|−0.015|0.255|0.241|92|
||n<sup>−0:8</sup><br>|−0.014|−0.009|0.146|0.130|91|0.056|0.037|0.387|0.355|94|
||n<sup>−0:9</sup>|−0.010|−0.007|0.163|0.146|91|0.110|0.073|0.494|0.445|94|
||auto<br>|−0.005|−0.003|0.159|0.141|90|0.083|0.055|0.457|0.396|92|
|400|n<sup>−0:5</sup><br>|−0.027|−0.018|0.063|0.061|92|−0.044|−0.030|0.133|0.132|94|
||n<sup>−0:6</sup><br>|−0.016|−0.011|0.070|0.068|92|−0.013|−0.009|0.174|0.168|94|
||n<sup>−0:8</sup><br>|−0.004|−0.003|0.101|0.096|92|0.043|0.029|0.308|0.292|94|
||n<sup>−0:9</sup>|−0.004|−0.003|0.130|0.120|92|0.109|0.073|0.457|0.398|94|
||auto<br>|−0.002|−0.001|0.117|0.106|92|0.058|0.039|0.360|0.331|94|
|900|n<sup>−0:5</sup><br>|−0.024|−0.016|0.047|0.044|91|−0.029|−0.020|0.092|0.104|96|
||n<sup>−0:6</sup><br>|−0.011|−0.007|0.053|0.052|94|−0.007|−0.005|0.123|0.139|97|
||n<sup>−0:8</sup><br>|−0.001|−0.001|0.089|0.084|92|0.035|0.024|0.278|0.269|94|
||n<sup>−0:9</sup>|−0.003|−0.002|0.116|0.112|93|0.090|0.060|0.389|0.386|96|
||auto|0.006|0.004|0.096|0.096|95|0.055|0.037|0.361|0.308|92|


The simulation set-up is identical to that in Section 4.1, except that we increase the Poisson intensity to 10. We employ the same bandwidth for the response and the covariate observation times. In addition to a fixed bandwidth, we also adopt a data-adaptive bandwidth selection procedure as described in Section 3.

Theresults(Table2)aresimilartothoseforthetime-independentcoefficient.Forallfunctional forms of _β_ .t/, as the sample size increases, the bias is well controlled, the empirical and modelbased standard errors agree reasonably well and the empirical coverage probability is close to the nominal 0.95-level. The performance tends to improve as the sample size increases. The empirical results appear to support the .nh1h2/<sup>1=2</sup> rate of convergence in theorem 2, with the empirical standard errors diminishing roughly proportionally to this rate.

Similar results were obtained for a time-dependent logistic regression and have been omitted.

---

[← 4.1. Time invariant coefficient](08-4-1-time-invariant-coefficient.md) · [Up: contents](index.md) · [4.3. Comparison with last value carried forward method →](10-4-3-comparison-with-last-value-carried-forward-method.md)
