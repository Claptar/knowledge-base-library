---
title: P4 – Association Studies (5 points)
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/05-questions.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `psets/05-questions.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# P4 – Association Studies (5 points)

**(A) (3 points)** Consider the following data case-control data. We will perform a chi-square test for association with a SNP.

| | A | T |
| :--- | :--- | :--- |
| Case | 90 | 110 |
| Control | 50 | 250 |

(i) Fill in the following table with the counts you would expect if you assumed independence. Show your work.

| | A | T |
| :--- | :--- | :--- |
| Case | 56 | 144 |
| Control | 84 | 216 |

(ii) Now, compute the Chi-Square statistic and state the conclusion for the p-value cutoff of 0.05.

$$\chi^2 = \sum_i \frac{(O_i - E_i)^2}{E_i} = \frac{(90 - 56)^2}{56} + \frac{(50 - 84)^2}{84} + \frac{(110 - 144)^2}{144} + \frac{(250 - 216)^2}{216} = 47.8$$

The result is significant (there is an association between the SNP and the disease).

**(B) (1 point)** You perform a large scale analysis and generate a list of significant SNPs and would now like to prioritize SNPs for further study. How might you use what you have learned from using the Segway model to do so?
Segway outputs a segmentation of the genome into its constitutive elements. We can look where SNPs cluster in particular cell types to identify particular genes and regulatory elements, as annotated by Segway. For example, a significant SNP may lie in an enhancer element or affect the motif of a regulator involved in the disease.

**(C) (1 point)** Describe why it is better to do association tests using a likelihood test based on reads instead of first calling variants and then using a statistical test on the binary variant calls.
When genotypes are known, we can just do a chi-square test. Uncertainty in the variant calls adds another layer of error in determining association, especially with sequencing at low depth.

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← P3 – Heritability (5 points)](03-p3-heritability-5-points.md) · [Up: contents](index.md)
