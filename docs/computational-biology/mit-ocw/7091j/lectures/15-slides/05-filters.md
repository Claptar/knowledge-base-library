---
title: Filters
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/15-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/15-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# Filters

1. expression of the modulator and of the TF must be statistically independent
2. the modulator expression must have sufficient range
3. may be filtered by additional criteria—for example, molecular functions.

Source: Wang, Kai, Masumichi Saito, et al. "Genome-wide Identification of Post-translational Modulators of Transcription Factor Activity in Human B cells."
*Nature Biotechnology* 27, no. 9 (2009): 829-37.

Genome-wide identification of post-translational modulators of transcription factor activity in human B cells
Kai Wang, Masumichi Saito, Brygida C Bisikirska, Mariano J Alvarez, Wei Keat Lim, Presha Rajbhandari, Qiong Shen, Ilya Nemenman, Katia Basso, Adam A Margolin, Ulf Klein, Riccardo Dalla-Favera & Andrea Califano
Nature Biotechnology 27, 829 - 837 (2009) Published online: 9 September 2009
doi:10.1038/nbt.1563

---

Estimate conditional mutual information

Source: Wang, Kai, Masumichi Saito, et al. "Genome-wide Identification of Post-translational Modulators of Transcription Factor Activity in Human B cells."
*Nature Biotechnology* 27, no. 9 (2009): 829-37.

Genome-wide identification of post-translational modulators of transcription factor activity in human B cells
Kai Wang, Masumichi Saito, Brygida C Bisikirska, Mariano J Alvarez, Wei Keat Lim, Presha Rajbhandari, Qiong Shen, Ilya Nemenman, Katia Basso, Adam A Margolin, Ulf Klein, Riccardo Dalla-Favera & Andrea Califano
Nature Biotechnology 27, 829 - 837 (2009) Published online: 9 September 2009
doi:10.1038/nbt.1563

---

Supplementary Table 12. Inferring the biological activity of a MINDy modulator. MoA: MINDy mode of action; $\rho$: Pearson correlation between *TF* and the target gene $t$; $\mu_t^+$: the mean expression of $t$ in the most and least expressed condition of the modulator. BA: biological activity. The schematic scatter plots shown in the table demonstrate the relationship between *TF* and $t$ when the modulator is most (red dots) and least (blue dots) expressed.

| MoA | $\rho$ | $\mu_t^+ - \mu_t^-$ | Plot | BA | $\operatorname{Sign}(\rho(\mu_t^+ - \mu_t^-))$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| + | + | + | | Activator | + |
| + | + | - | | Antagonist | |
| + | - | - | | Activator | + |
| + | - | + | | Antagonist | |
| - | + | - | | Antagonist | |
| - | + | + | | Activator | + |
| - | - | + | | Antagonist | |
| - | - | - | | Activator | + |

$$\begin{cases}
\text{activator} & \text{if } \rho(\mu_t^+ - \mu_t^-) > 0 \\
\text{antagonist} & \text{if } \rho(\mu_t^+ - \mu_t^-) < 0 \\
\text{undetermined} & \text{if } \rho(\mu_t^+ - \mu_t^-) \approx 0
\end{cases}$$

where $\rho$ is the Pearson correlation between TF and $t_i$, and $\mu_t^+$ is the mean expression of $t_i$ in $L_m^+$. In practice, however, the difference between $\mu_t^+$ has to be assessed statistically. In this work, we choose to use the two sample Student t-test (two sided) that assess the null hypothesis of $\mu_t^+ = \mu_t^-$. If the null hypothesis can not be rejected at $\alpha = 0.1$, we assign the mode to be undermined; otherwise, $M_j$ is considered an activator or antagonist (depending on which tail is tested) of the interaction between TF and $t_i$.

**Note than none of these curve saturate**

Source: Wang, Kai, Masumichi Saito, et al. "Genome-wide Identification of Post-translational Modulators of Transcription Factor Activity in Human B cells."
*Nature Biotechnology* 27, no. 9 (2009): 829-37.

---

## What regulates MYC?

### Input:
254 expression profiles in B cells (normal and tumor)
various sets of candidate regulators

### Evaluation:
1. comparison to known modulators
2. experimental tests of four candidates

---

## What regulates MYC?

Source: Wang, Kai, Masumichi Saito, et al. "Genome-wide Identification of Post-translational Modulators of Transcription Factor Activity in Human B cells."
*Nature Biotechnology* 27, no. 9 (2009): 829-37.

---

## Limitations

- Need huge expression datasets
- Can't find:
  - modulator that do not change in expression
  - modulator that are highly correlated with target
  - modulators that both activate and repress

---

## Huge networks!

This is just the nearest neighbors of one node of interest from ARACNe!

Nature Medicine 18, 436–440 (2012) doi:10.1038/nm.2610

Source: Della Gatta, Giusy, Teresa Palomero, et al. "Reverse Engineering of TLX Oncogenic Transcriptional Networks Identifies RUNX1 as Tumor Suppressor in T-ALL." *Nature Medicine* 18, no. 3 (2012): 436-40.

---

## Huge networks!

Conditional MI network of miR modulators

248,000 interactions

http://www.sciencedirect.com/science/article/pii/S0092867411011524

Courtesy of Elsevier B.V. Used with permission.
Source: Sumazin, Pavel, Xuerui Yang, et al. "An Extensive MicroRNA-mediated Network of RNA-RNA Interactions Regulates Established Oncogenic Pathways in Glioblastoma." *Cell* 147, no. 2 (2011): 370-81.

---

## MINDy modulators

### Potential Modulators

| Source of targets | Signaling (542) | TFs (598) | Any (3,131) |
| :--- | :---: | :---: | :---: |
| Database | 91 | 99 | |
| ARACNe | 80 | 85 | |
| ALL | [25/296] | [32/296] | 296 |

MINDy selects between 10-20% of candidates!

---

## Outline

- Bayesian Networks for PPI prediction
- Gene expression
  - Distance metrics
  - Clustering
  - Signatures
  - Modules
    - Bayesian networks
    - Regression
    - Mutual Information
    - Evaluation on real and simulated data

---

NATURE METHODS | ANALYSIS

## Wisdom of crowds for robust gene network inference

Daniel Marbach, James C Costello, Robert Küffner, Nicole M Vega, Robert J Prill, Diogo M Camacho, Kyle R Allison, The DREAM5 Consortium, Manolis Kellis, James J Collins & Gustavo Stolovitzky

Affiliations | Contributions | Corresponding author

*Nature Methods* **9**, 796–804 (2012) | doi:10.1038/nmeth.2016
Received 31 October 2011 | Accepted 22 May 2012 | Published online 15 July 2012

---

## AUPR = area under precision-recall curve

Area under precision-recall curve

Wisdom of crowds for robust gene network inference
*Nature Methods* 9, 796–804 (2012) doi:10.1038/nmeth.2016

Source: Marbach, Daniel, James C. Costello, et al. "Wisdom of Crowds for Robust Gene Network Inference." *Nature Methods* 9, no. 8 (2012): 796-804.

---

---

[← Wisdom of crowds for robust gene network inference](04-wisdom-of-crowds-for-robust-gene-network-inference.md) · [Up: contents](index.md) · [AUPR = area under precision-recall curve →](06-aupr-area-under-precision-recall-curve.md)
