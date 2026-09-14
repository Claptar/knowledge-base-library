---
title: IndependentFiltering2
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/images_sequencing/independentFiltering2.pdf
source_file: sources/statomics-sga21/images_sequencing/independentFiltering2.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# IndependentFiltering2

**Source:** [`images_sequencing/independentFiltering2.pdf`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/images_sequencing/independentFiltering2.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
A Null distributions for UII B Gene−level error SD estimates (filtered) C True null limma p−values<br>Given UI > u*<br>limma fit<br>Unconditional<br>Unconditional<br>−4 −2 0 2 4 0 2 4 6 8 10 0.0 0.2 0.4 0.6 0.8 1.0<br>UII si p<br><!-- End of picture text -->

Fig. 2. (A) The null distribution of the test statistic is affected by filtering on the maximum of within-class averages. In this example, all genes have a known common variance, the filter statistic is the maximum of within-class means, and the test statistic is a z-score. The unconditional distribution of the test statistic for nondifferentially expressed genes is a standard normal. Its conditional null distribution, given that the filter statistic (U<sup>I</sup> ) exceeds a certain threshold (u<sup>�</sup> ), however, has much heavier tails. Using the unconditional null distribution to compute p -values after filtering would therefore be inappropriate. See SI Text for full details. (Band C) Overall variance filtering and the limma moderated t-statistic. Data for 5,000 nondifferentially expressed genes were generated according to the limma Bayesian model (n1 ¼ n2 ¼ 2, d0 ¼ 3, s<sup>2</sup> 0<sup>¼ 1). (B) Filtering on overall variance (θ¼ 0.5) preferentially eliminated genes with small si, causing gene-</sup> level standard deviation estimates for genes passing the filter (histogram) to be shifted relative to the unconditional distribution used to generate the data (dashed curve). The limma inverse χ<sup>2</sup> model was unable to provide a good fit (solid curve) to the si passing the filter. (C) The fitting problems lead to a posterior degrees-of-freedom estimate of ∞. As a consequence, p -values were computed using an inappropriate null distribution, producing too many true-null p -values close to zero, i.e., loss of type I error rate control. An analogous analysis comparing biological replicates from the ALL study—so that real array data were used but no gene was expected to exhibit significant differential expression—yielded qualitatively similar results.

---

[Up: contents](../index.md)
