---
title: 1.2. Target Decoy Approach
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/Identification.md
source_file: sources/statomics-sga2020-ghpages/pages/Identification.md
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1.2. Target Decoy Approach

**Source:** [`pages/Identification.md`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/Identification.md) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.md` (lossless)

When using a competitive target decoy search, the FDR of the set of returned PSMs is estimated by dividing the number of accepted decoys PSMs by the number of accepted target PSMs above a certain score cutoff [1].

$$ \widehat{\text{FDR}}(t)=\frac{\# decoys | x>t}{\#targets |x>t} $$

This can be rewritten as:

$$ \widehat{\text{FDR}}(t)=\frac{\#decoys}{\#targets}\frac{\frac{\# decoys | x>t}{\#decoys}}{\frac{\#targets |x>t}{\#targets}} $$

$$ \widehat{\text{FDR}}(x) =
{\hat{\pi}_0}\frac{\widehat{\int\limits_t^{+\infty} f_0(x) dx}}{\widehat{\int\limits_t^{+\infty} f(x)dx}} $$

Hence, the proportion of bad hits \$ \pi_0 \$ is estimated as the number of decoys divided by the number of targets, and the competitive TDA assumes that it is equally likely that a bad hit matches to a bad target or to a decoy; the probability of  a (bad) target PSM hit above the threshold is estimated based on the empirical cumulative distribution in the sample, i.e. as the fraction of targets (decoys) that are above the threshold. Hence, a second assumption is that the decoy matches provide a good simulation of the target matches. See e.g. [2]. These assumptions can be evaluated with our EvalDecoyShiny App.

Figure 2. Illustration of the target and decoy distributions, in grey the histogram of the target PSM scores, the blue bars are the histogram of the decoy PSM scores. We indeed see that the decoy PSMs match well with  the incorrect targets that are more likely to occur at low scores. The red bars are an estimate of the correct target distribution and are equal to the target counts (gray histogram) minus the decoy counts (blue bars).

##### 1. Pyrococcus dataset

The Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1) reference proteome. The resulting database has 2,051 proteins in total (https://www.uniprot.org/uniprot/?query=taxonomy:186497, taxonomy:"Pyrococcus furiosus (strain ATCC 43587 / DSM 3638 / JCM 8422 / Vc1) [186497]").

The data can be found on [https://github.com/statOmics/SGA2020/tree/data](https://github.com/statOmics/SGA2020/tree/data).
Use the mzid file for the pyrococcus example, which can be found at data/identification/pyrococcusMSGF+.mzid

First run the command

```
source('https://statomics.github.io/SGA2020/assets/EvalTargetDecoys.R')
```

to load the function evalTargetDecoy.

Follow the [vignette](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/assets/exampleEvalTDA.html) and alter a script to assess the decoy quality in the pyrococcus.
Note, that the decoys are stored in the `is.decoy` column and that the score   `ms-gf:specevalue`.

##### 1. Assess the search you performed in "Tutorial 1. Peptide and Protein Identification" at https://compomics.com/bioinformatics-for-proteomics/identification/
Open the search from tutorial 1.3. in Peptide Shaker and export the search to an mzid file by clicking export > Peptide Shaker Project As > mzIdentML. Evaluate the TDA for the ommsa, X!Tandem and the Peptide Shaker score.

Evaluate the TDA for the  X!Tandem, OMSSA and Peptide Shaker scores. What do you observe and try to explain. [1.4.a]

##### 2. Pyrococcus - Peptide Shaker - Uniprot search

Do the analysis for the search MSGF+, X!Tandem, OMSSA and Peptide Shaker scores based on all Pyrococcus proteins in a search against all pyrococcus peptides in Uniprot (data/identification/pyroUniprot.mzid).

What do you observe explain. [1.4.b]

##### 3. Pyrococcus/Peptide Shaker - Swiss prot search
Do the analysis for the search MSGF+, X!Tandem, OMSSA and Peptide Shaker scores for Pyrococcus based on the curated proteins from swissprot only (data/identification/pyroSwissprot.mzid). What do you observe. Try to explain. [1.4.c]

##### 4. FDR Elias and Gygi, 2007
Elias and Gygi, 2007, reported the following target decoy FDR estimation:

$$\widehat{\text{FDR}}(t)=\frac {2 \times (\#decoys >t)}{\#decoys > t + \#targets > t}$$

Do you agree with this expression? Why, why not? [1.4.d]

---

[← 1.1 Basic Statistical Concepts](02-1-1-basic-statistical-concepts.md) · [Up: contents](index.md) · [References →](04-references.md)
