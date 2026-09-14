---
title: 1.1 Basic Statistical Concepts
source: https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/Identification.md
source_file: sources/statomics-sga2020-ghpages/pages/Identification.md
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 1.1 Basic Statistical Concepts

**Source:** [`pages/Identification.md`](https://github.com/statOmics/SGA2020/blob/ded99ebf046477d39ae1950eed10a4ba901b948d/pages/Identification.md) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.md` (lossless)

We first introduce some notation. With x we denote the PSM score and we assume that larger score values indicate a better match to the theoretical spectrum. Then the scores will follow a mixture distribution:

$$ f(x)=\pi_0 f_0 (x)+(1-\pi_0 ) f_1 (x), $$

with \$ f(x) \$ the target PSM score distribution, \$ f_0(x) \$ the mixture component corresponding to incorrect PSMs, \$ f_0(x) \$  the mixture component corresponding to the correct PSMs and \$ \pi_0 \$ the fraction of incorrect PSMs.
Based on the mixture distribution we can calculate the posterior probability that a PSM with score x is a bad match:

$$ P[\text{Bad hit} \vert \text{score }x]=\frac{\pi_0 f_0 (x)}{f(x)}, $$

which is also referred to as the posterior error probability (PEP) in mass spectrometry based proteomics.
Based on the mixture model, we can also calculate the posterior probability that a random PSM in the set of all PSMs with scores above a score threshold t is a bad hit (see e.g. Figure 1):

$$ P[\text{Bad hit} \vert \text{score }x>t]=\pi_0 \frac{\int\limits_{x=t}^{+\infty} f_0(x)dx}{\int\limits_{x=t}^{+\infty} f(x)dx}, $$

with \$\int\limits_{x=t}^{+\infty} f_0(x)dx \$ the probability to observe a bad PSM hit above the threshold and,  \$\int\limits_{x=t}^{+\infty} f_0(x)dx \$  the probability to observe a target PSM hit above the threshold. The probability \$ P[\text{Bad hit} \vert \text{score }x>t] \$ is also referred to as the false discovery rate (FDR) of the set of PSMs with scores above the threshold t. Hence, the FDR has the interpretation of the expected fraction of bad hits in the set of all target hits that are returned in the final PSM list.

<img src="./figs/tdaPyro.png" height="200">

 We would like to calculate the FDR corresponding to the set op PSMs with a target score above the threshold t.
In order to calculate the FDR, we thus have to characterize the distribution of the bad hits and of all PSMs.
In proteomics this is done by the use of the target/decoy approach.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [1.2. Target Decoy Approach →](03-1-2-target-decoy-approach.md)
