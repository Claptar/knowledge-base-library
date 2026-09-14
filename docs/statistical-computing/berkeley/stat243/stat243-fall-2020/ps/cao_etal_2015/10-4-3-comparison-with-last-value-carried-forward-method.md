---
title: 4.3. Comparison with last value carried forward method
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/ps/cao_etal_2015.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4.3. Comparison with last value carried forward method

**Source:** [`ps/cao_etal_2015.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/ps/cao_etal_2015.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

In longitudinal studies, a naive approach to analysing asynchronous data is the last value carried forward method. If data at a certain time point are missing, then the observation at the most recent time point in the past is used in an analysis for synchronous data. It is well known that this method is theoretically biased. However, in practice, it is often employed, owing to its conceptual simplicity and ease of implementation. In this subsection, we study its performance in simulation studies under the time-independent coefficient model (1).

The simulation set-up is the same as in Section 4.1. For the last value carried forward procedure, in applying generalized estimating equations for synchronous data (Diggle _et al_ ., 2002), for a response observed at time tij, the covariate at time tij was taken to be the covariate observed at time s = max.x ⩽ tij, x ∈ _{_ si1, ::: , simi _}_ /. This corresponds to the most recent observation time relative to the response. For a response, if no covariate is observed before the response’s observation time, then the observed response is omitted from the analysis.

Table 3 summarizes the results based on linear and logistic link functions when _β_ 1 = 1:5. The results for other choices of _β_ 1 are very similar and we omit the details. The bias is substantial and

766 _H. Cao, D. Zeng and J. P. Fine_

**Table 2.** Simulation results with time-dependent coefficient for linear regression

|_Model_|_t_||_Resu_|_lts for n_=|_400_|||_Results fo_|_r n_=_900_||
|---|---|---|---|---|---|---|---|---|---|---|
|||_BD_|_RB_|_SD_|_SE_|_CP (%)_|_RB_|_SD_|_SE_|_CP (%)_|
|_β_.t/=0:4t+0:5|0.1|n<sup>−1=2</sup>|−0.011|0.113|0.109|92|0.006|0.101|0.091|92|
|||auto<br>|−0.004|0.105|0.111|95|−0.047|0.086|0.090|96|
||0.3|n<sup>−1=2</sup>|−0.023|0.126|0.112|95|−0.004|0.095|0.094|94|
|||auto<br>|0.009|0.114|0.103|96|−0.024|0.084|0.092|95|
|_β_.t/=<sup>√</sup>t|0.1|n<sup>−1=2</sup>|0.006|0.103|0.108|92|−0.025|0.084|0.094|96|
|||auto<br>|0.003|0.105|0.111|95|−0.072|0.086|0.090|98|
||0.3|n<sup>−1=2</sup>|−0.013|0.120|0.111|92|−0.005|0.112|0.096|95|
|||auto<br>|0.011|0.114|0.103|96|−0.025|0.084|0.092|95|
|_β_.t/=sin.2_π_t/|0.1|n<sup>−1=2</sup>|−0.006|0.107|0.107|95|−0.006|0.114|0.094|91|
|||auto<br>|−0.024|0.108|0.111|95|−0.024|0.096|0.091|95|
||0.3|n<sup>−1=2</sup>|−0.016|0.115|0.125|92|−0.009|0.092|0.106|98|
|||auto|−0.012|0.120|0.101|96|−0.021|0.090|0.090|96|


**Table 3.** Summary statistics by using the last value carried forward approach

|n|_R_|_esults for li_|_near regre_|_ssion mod_|_el_|_Re_|_sults for logi_|_stic regre_|_ssion mode_|_l_|
|---|---|---|---|---|---|---|---|---|---|---|
||_Bias_|_RB_|_SD_|_SE_|_CP (%)_|_Bias_|_RB_|_SD_|_SE_|_CP (%)_|
|100|−0.122|−0.081|0.094|0.091|73|−0.199|−0.133|0.113|0.174|78|
|400|−0.123|−0.082|0.046|0.047|24|−0.206|−0.137|0.054|0.087|33|
|900|−0.123|−0.082|0.032|0.031|3|−0.208|−0.138|0.032|0.058|0|


does not attenuate as the sample size increases. Because of decreasing variance, as the sample size increases, the coverage probability deteriorates. This is especially true for the logistic regression which has 0 coverage probability when the sample size n = 900.

---

[← 4.2. Time-dependent coefficient](09-4-2-time-dependent-coefficient.md) · [Up: contents](index.md) · [5. Application to human immunodeficiency virus data →](11-5-application-to-human-immunodeficiency-virus-data.md)
