---
title: GPS probabilistically models ChIP-Seq read spatial distribution using a mixture
  model
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/lectures/07-slides.pdf
licence: CC BY-NC-SA 4.0
route: llm
fidelity: reconstructed
converted: '2026-09-20'
---

> **Reconstructed by a model.** `lectures/07-slides.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) — ocw-7091j, licensed CC BY-NC-SA 4.0. Converted 2026-09-20 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# GPS probabilistically models ChIP-Seq read spatial distribution using a mixture model

#### (single-base resolution)

$M$ Possible events
$N$ Observed reads

Likelihood of observed reads:
$$p(R \mid \pi) = \prod_{n=1}^N \sum_{m=1}^M \pi_m p(r_n \mid m), \quad \sum_{m=1}^M \pi_m = 1$$

Prob. of event $m$
Mixing prob.

---

Likelihood of observed reads:
$$p(R \mid \pi) = \prod_{n=1}^N \sum_{m=1}^M \pi_m p(r_n \mid m), \quad \sum_{m=1}^M \pi_m = 1$$

Read assignment is latent
$$\begin{aligned}
g(z_n = m) = 1 & \quad \text{Read n came from event m} \\
g(z_n = m) = 0 & \quad \text{Read n did not come from event m}
\end{aligned}$$

$$\pi = \arg\max_\pi p(R \mid \pi)$$

#### Expectation-Maximization (EM) algorithm with component elimination

##### E step
$$\gamma(z_n = m) = \frac{\pi_m p(r_n \mid m)}{\sum_{m'=1}^M \pi_{m'} p(r_n \mid m')}$$

$\gamma(z_n = m)$: the fraction of read $n$ assigned to event $m$

##### M step
$$\hat{\pi}_m^{(i)} = \frac{N_m}{\sum_{m'=1}^M N_{m'}}$$
$$N_m = \sum_{n=1}^N \gamma(z_n = m)$$

$N_m$: the effective number of reads assigned to event $m$

---

#### Expectation-Maximization (EM) algorithm with component elimination

##### Initialization
$$\pi_j = \frac{1}{M}$$

##### Strength of binding event at end
$$N_m = \sum_{n=1}^N \gamma(z_n = m)$$

$N_m$: the effective number of reads assigned to event $m$

#### Expectation-Maximization (EM) algorithm with component elimination

##### E step
$$\gamma(z_n = m) = \frac{\pi_m p(r_n \mid m)}{\sum_{m'=1}^M \pi_{m'} p(r_n \mid m')}$$

$\gamma(z_n = m)$: the fraction of read $n$ assigned to event $m$

##### M step
$$\hat{\pi}_m^{(i)} = \frac{N_m}{\sum_{m'=1}^M N_{m'}}$$
$$N_m = \sum_{n=1}^N \gamma(z_n = m)$$

$N_m$: the effective number of reads assigned to event $m$

---

### Synthetic data, EM, no prior
#### (events at 500 and 550 bp)

---

### GPS deconvolves homotypic events and improves spatial accuracy

Example of a predicted joint CTCF event that contains coordinately located CTCF motifs

---

Likelihood of observed reads:
$$p(R \mid \pi) = \prod_{n=1}^N \sum_{m=1}^M \pi_m p(r_n \mid m), \quad \sum_{m=1}^M \pi_m = 1$$

A sparse prior on mixture components (binding events)
$$p(\pi) \propto \prod_{m=1}^M \frac{1}{(\pi_m)^\alpha}, \alpha > 0 \qquad \text{(Figueiredo and Jain, 2002)}$$

#### Expectation-Maximization (EM) algorithm with component elimination

##### E step
$$\gamma(z_n = m) = \frac{\pi_m p(r_n \mid m)}{\sum_{m'=1}^M \pi_{m'} p(r_n \mid m')}$$

$\gamma(z_n = m)$: the fraction of read $n$ assigned to event $m$

##### M step
$$\hat{\pi}_m^{(i)} = \frac{\max(0, N_m - \alpha)}{\sum_{m'=1}^M \max(0, N_{m'} - \alpha)}$$
$$N_m = \sum_{n=1}^N \gamma(z_n = m)$$

$N_m$: the effective number of reads assigned to event $m$

---

### Synthetic data, EM, sparse prior
#### (events at 500 and 550 bp)

---

### EM – Sparse prior

---

### GPS EM iteration #1

---

### GPS deconvolves homotypic events and improves spatial accuracy

Example of a predicted joint CTCF event that contains coordinately located CTCF motifs

---

### mES cell Oct4 ChIP Seq

---

### We compute a p-value with a binomial test for significance

Null Model –

$F(k,n,P)$ - Probability $n-k$ reads observed in IP channel by chance with $k$ reads observed in control. $P = 0.5$ equal chance reads occurred in control and IP channels for null model.

$$F(k, n, P) = \sum_{l=0}^{\lfloor k \rfloor} \binom{n}{l} P^l (1 - P)^{(n - l)}$$

$k$: scaled control read count
$n$: total count of IP and scaled control reads
$P$: probability that reads occur from IP data, $P = 0.5$.

---

### We determine significant events by Benjamini Hochberg at a desired false discovery rate (FDR)

Benjamini-Hochberg correction

$$Q-\text{value} = P-\text{value} \times \frac{\text{Count}}{\text{Rank}}$$

$\text{Count}$: total number of binding events tested.
$\text{Rank}$: Rank of event in list of p-values, from most significant ($\text{rank} = 1$) to least ($\text{rank} = \text{Count}$)

Accept events (reject null) of $\text{rank} = 1 \dots k$ up to the point that the Q-value is greater than the desired FDR.

---

### Irreproducible Discovery Rate (IDR) Analysis

- We have two replicates of an experiment
- How do we choose events are consistent in the two replicates?

---

### Spearman’s rank correlation provides a metric for replicate consistency but does not select events

- Consider two ranked lists of $n$ detected events $X$ and $Y$, one from each replicate, each ranked by scores from most significant to least significant.
- For matched event $i$ ranks are $x_i$ and $y_i$ in $X$ and $Y$

$$\rho = \frac{\sum_i (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_i (x_i - \bar{x})^2 \sum_i (y_i - \bar{y})^2}}$$

---

### Irreproducible Discovery Rate (IDR) Analysis

- $\Psi_n(t)$ is the fraction of the $n$ events that are paired in the top $n*t$ events in both $X$ and $Y$. It is roughly linear from $t=0$ to the point when events are no longer reproducible (not shared between replicates within the ranking)
- $\Psi'_n(t)$ is first derivative of $\Psi_n(t)$ with respect to $t$. It allows us to visualize when we transition from reproducible to irreproducible events as $t$ increases

---

### Irreproducible Discovery Rate (IDR) Analysis

FIG. 1. *An illustration of the correspondence profile in an idealized case, where top 50% are genuine signals and bottom 50% are noise. In this case, all signals are ranked higher than noise; two rank lists have perfect correspondence for signals and no correspondence for noise. (a) Correspondence curve. (b) Change of correspondence curve.*

Courtesy of Institute of Mathematical Statistics. Used with permission.
Source: Li, Qunhua, James B. Brown, et al. "Measuring Reproducibility of High-throughput Experiments." *The Annals of Applied Statistics* 5, no. 3 (2011): 1752-79.

---

### Irreproducible Discovery Rate (IDR) Analysis

- Consider that the lists $X$ and $Y$ are a mixture of two kinds of events – reproducible and irreproducible.
- Model the ranking scores as a two component mixture and learn the parameters of the reproducible and irreproducible components
- For IDR $\alpha$, select top $l$ pairs using their scores such that the probability that the rate of pairs from the irreproducible part of the mixture is $\alpha$

---

### Irreproducible Discovery Rate Results

FIG. 7. *The coverage of high-confidence CTCF motif at different numbers of selected ChIP-seq peaks, plotted at various idr cutoffs for nine peak callers on a CTCF Chip-seq experiment from ENCODE. The bars on the curves of Peakseq, MACS, SPP, Fseq and Hotspot show the number of peaks selected at $\text{IDR} = 0.05$. No selection is made for the rest of the peak callers because model selection favors the one-component model for peaks identified by these callers.*

Courtesy of Institute of Mathematical Statistics. Used with permission.
Source: Li, Qunhua, James B. Brown, et al. "Measuring Reproducibility of High-throughput Experiments." *The Annals of Applied Statistics* 5, no. 3 (2011): 1752-79.

---

### Genome-wide Event finding and Motif discovery

ChIP-Seq Reads + DNA Sequences $\longrightarrow$ **GEM**

1. Bias motif discovery towards binding sites (Event finding $\longrightarrow$ Motif discovery)
2. Biases binding event predictions towards motif positions (Motif discovery $\longrightarrow$ Event finding)

$\longrightarrow$ Binding events and explanatory DNA motifs

---

### Motif-based positional prior biases the binding event prediction

#### Mixture model
$$p(R \mid \pi) = \prod_{n=1}^N \sum_{m=1}^M \pi_m p(r_n \mid m), \quad \sum_{m=1}^M \pi_m = 1$$

#### Position-specific priors
- Events are sparse
- Events occurs more likely at motif positions

$$p(\pi) \propto \prod_{m=1}^M (\pi_m)^{-\alpha_s + \alpha_m}$$

$\alpha_s$: uniform sparse prior parameter governing the degree of sparseness, $\alpha_s > 0$;
$\alpha_m$: position specific motif-based prior

---

### GEM improves in resolving joint binding events

TF A
TF A

(Human GABP Data : Valouev et al., 2008)

Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." PLoS Computational Biology 8, no. 8 (2012): e1002638.

---

### GEM improves spatial accuracy in binding event prediction

(Human GABP Data Valouev et al., 2008)
(Mouse CTCF data Chen, et. al. 2008)

Motif $\longleftrightarrow$ Event call

Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." PLoS Computational Biology 8, no. 8 (2012): e1002638.

---

### GEM improves the spatial resolution of ChIP-exo data event prediction

Motif $\longleftrightarrow$ Event call
(Rhee and Pugh, 2011)

Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." PLoS Computational Biology 8, no. 8 (2012): e1002638.

---

### GEM reveals transcription factor spatial binding constraints

Total ~7500 Oct4 sites, ~2500 sites are within 100bp of Sox2 sites

Oct4 Sox2

Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." PLoS Computational Biology 8, no. 8 (2012): e1002638.

---

### K562

Source: Guo, Yuchun, Shaun Mahony, et al. "High Resolution Genome Wide Binding Event Finding and Motif Discovery Reveals Transcription Factor Spatial Binding Constraints." PLoS Computational Biology 8, no. 8 (2012): e1002638.

---

### GEM Summary

- GEM incorporates motif information as a position-specific prior to bias binding event prediction
- GEM achieves exceptional spatial resolution, and further improves joint event deconvolution
- GEM systematic analysis reveals *in vivo* transcription factor spatial binding constraints in human and mouse cells, provides testable models for transcription factor interactions

---

### Concept of a Transcriptional Regulatory Code

Harbison et al., *Nature* 431: 99 (2004)

**What regulators contribute to control of each gene?**
**What sequences do they bind (cis-elements)?**
**When do the regulators bind these sequences?**

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Harbison, Christopher T., D. Benjamin Gordon, et al. "Transcriptional Regulatory Code of a Eukaryotic Genome." *Nature* 431, no. 7004 (2004): 99-104.

### Samples of the Draft Transcriptional Regulatory Code

#### Chromosome II
Positions 370000:379300

Rox1
Phd1
Sut1
Phd1
YBR069C (TAT1)

Phd1
Gcn4 Leu3
Yap7 Gcn4
YBR068C (BAP2)

Nrg1 Skn7
Nrg1 Ste12
YBR067C (TIP1)

YBR066C (NRG2)

#### Chromosome IV
Positions 1358800:1366600

Skn7
YDR453(TSA1)

YDR452W(PPN1)

Fkh1 Phd1 Phd1
Ndd1 Swi6 Sok2
Mcm1 Fkh1 Fkh1
Ndd1 Fkh2 Fkh1
Mbp1 Mbp1 Fkh2
YDR451C(YHP1)

Fhl1
Rap1
Fhl1
Rap1
YDR450W(RPS18A)
YDR449C

#### Chromosome V
Positions 1359000:1366000

Ume6
Met4
Bas1
Gcn4
Bas1
Bas1
Gcn4
YGL183C(MND1) YGL184C(STR3)

YGL185C

Bas1
Gcn4
YGL186C(TPN1)

Hap5
Hap3
Hap2
Hap1
YGL187C(COX4)

Courtesy of Macmillan Publishers Limited. Used with permission.
Source: Harbison, Christopher T., D. Benjamin Gordon, et al. "Transcriptional Regulatory Code of a Eukaryotic Genome." Nature 431, no. 7004 (2004): 99-104.

---

### Is conservation a good predictor of conserved binding events across species?

Mouse image courtesy of David Deen. Used with permission.
©2006 David Deen http://www.daviddeen.com

---

### Promoter proximal binding is not well conserved in liver (FOXA2, HNF1A, HNF4A, HNF6)

| No Binding | 2160 (54%) | Human: ABC1
| :--- | :--- | :--- |
| **All Events Conserved** | 132 (3%) | Human: ABC1
| **Some Events Conserved** | 320 (8%) | Human: ABC1

| No Events Conserved | 740 (19%) | Human: ABC1
| :--- | :--- | :--- |
| | 536 (13%) | Human: ABC1
| | 144 (4%) | Human: ABC1

D. Odom, R. Dowell E. Fraenkel, D. Gifford Labs
Nature Genetics, 2007

Source: Odom, Duncan T., Robin D. Dowell, et al. "Tissue-specific Transcriptional Regulation has Diverged Significantly between Human and Mouse." Nature Genetics 39, no. 6 (2007): 730-32.

---

## FIN

---

MIT OpenCourseWare
http://ocw.mit.edu

7.91J / 20.490J / 20.390J / 7.36J / 6.802J / 6.874J / HST.506J Foundations of Computational and Systems Biology
Spring 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← Lecture 7](01-lecture-7.md) · [Up: contents](index.md)
