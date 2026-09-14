---
title: All defaults
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd
source_file: sources/statomics-sga21/sequencing_rnaseqIntro.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# All defaults

**Source:** [`sequencing_rnaseqIntro.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/sequencing_rnaseqIntro.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

include_graphics("./images_sequencing/deAnalysis_para.png")
```

The authors write that they are "employing treatment type, time point and sample ID as factors in the model". Concerning experimental variables, this suggests they have added covariates defining the treatment and time point for each sample. The sample ID in the text refers to the original tissue sample and therefore corresponds to the donor patient. While there is also a variable called `sample` in the `colData`, this is not what the authors refer to. Note the ambiguity here and since the authors didn't share their code, this is hard to check! But, more on reproducibility later...

**Question**. What are the authors assuming when using this structure for the mean model? Do you think that there are extensions or simplifications of the mean model that would be relevant?

<details><summary> Answer. </summary><p>
The authors are acknowledging the relatedness of samples derived from the same donor patient by adding it as a fixed effect to the model, which is great. This blocking strategy has been extensively discussed in the proteomics part of this course.
However, by only adding a main effect for treatment and time, they are assuming that the effect of time is identical for all treatments, i.e., the average gene expression in-/decrease at 48h versus 24h is identical for the DPN, OHT or the control samples, which seems like a quite stringent assumption.
We can make the model more flexible by allowing for a `treatment * time` interaction.
</p></details>

## Parameter estimation and empirical Bayes

 - Even in limited sample size settings, the parameters $\beta$ of the mean model may be estimated reasonably efficiently, and we have previously discussed the IRLS algorithm to do so.
 - However, estimating parameters for the variance (this is, the dispersion parameter $\phi$ from the negative binomial or the variance parameter $\sigma$ from the Gaussian) is typically quite a bit harder.
 - In genomics, we often take advantage of the parallel structure of the thousands of regression models (one for each gene) to **borrow information across genes** in a procedure called **empirical Bayes**, as also seen in the proteomics part of this course.
 - In the Bayesian setting, we use not only the data, but also a prior distribution, to derive our parameter estimates. In a traditional Bayesian analysis, one assumes an *a priori* known prior distribution, which reflects our prior belief into all possible values of the parameter. This prior distribution is completely independent of the observed data and the idea is that one specifies the prior distribution before observing the data. One can then use the data and prior distribution to derive a **posterior distribution** for the parameter(s) $\theta$ of interest through Bayes rule
 $$
 p(\theta | \mathbf{Y}) = \frac{p(\mathbf{Y} | \theta) p(\theta)}{\int_{\theta \in \Theta} p(\mathbf{Y} | \theta) p(\theta) d\theta}.
 $$
    Here, the posterior distribution $p(\theta | \mathbf{Y})$ is calculated using the data likelihood $p(\mathbf{Y} | \theta)$, prior distribution $p(\theta)$ and the 'marginal likelihood' $\int_{\theta \in \Theta} p(\mathbf{Y} | \theta) p(\theta) d\theta$, where $\Theta$ denotes the parameter space of $\theta$. We can see that the posterior probability for a specific value of the parameter $\theta$ will be high if both the data likelihood as well as prior probability are high.

 - In empirical Bayes, we basically take a semi-Bayesian approach to parameter estimation. Indeed, we do not assume a known prior distribution, but estimate it empirically using the data. This empirically estimated prior $\hat{p}(\theta)$ is then used to calculate the posterior distribution.
 - While in some settings one can easily calculate the posterior distribution, sometimes it can be a hard problem. In such cases, it may be useful to restrict ourselves to calculating the **maximum a posteriori (MAP)** estimate, which corresponds to the mode of the posterior distribution. This can be considered to be analogous to point estimation in the frequentist setting.
 - In our setting, we use genes with a similar average expression to moderate the dispersion estimate for a particular gene. The basic assumption for this to make sense is that genes with similar means might have similar dispersion parameters (or variances), owing to the mean-variance trend.

 ---

 - Once initial estimates for the gene-wise dispersions have been derived ($\hat{\Phi}_g^{ML}$ in the figure), we use a parametric model to estimate its distribution (typically as a function of the mean) across genes. This distribution is the **prior distribution**.
 - Then, each initial estimate is shrunken towards that empirically estimated prior distribution. The amount of shrinkage being performed is data-driven, and depends on the data, taking into account the precision of our initial estimate (i.e., shape of the likelihood) and the variability of the prior distribution.
 - These strategies result in impressive performance gains in terms of differential expression analysis and are implemented in all popular differential expression analysis software packages (though in slightly differing ways) like `limma`, `edgeR` and `DESeq2`.

```r

---

[← Challenge III: Parameter estimation (under limited information setting)](20-challenge-iii-parameter-estimation-under-limited-information.md) · [Up: contents](index.md) · [All defaults →](22-all-defaults.md)
