---
title: Experimental Design
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference_noFrames.Rmd
source_file: sources/statomics-sga21/pda_quantification_inference_noFrames.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`pda_quantification_inference_noFrames.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference_noFrames.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Experimental Design

## Sample size

$$
 \log_2 \text{FC} = \bar{y}_{p1}-\bar{y}_{p2}
$$

$$
T_g=\frac{\log_2 \text{FC}}{\text{se}_{\log_2 \text{FC}}}
$$

$$
T_g=\frac{\widehat{\text{signal}}}{\widehat{\text{Noise}}}
$$

If we can assume equal variance in both treatment groups:

$$
\text{se}_{\log_2 \text{FC}}=\text{SD}\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}
$$

$\rightarrow$ if number of bio-repeats increases we have a higher power!

- cfr. Study of tamoxifen treated Estrogen Recepter (ER) positive breast cancer patients

## Blocking

$$
\sigma^2= \sigma^2_{bio}+\sigma^2_\text{lab} +\sigma^2_\text{extraction} + \sigma^2_\text{run} + \ldots
$$

- Biological: fluctuations in protein level between mice, fluctations in protein level between cells, ...
- Technical: cage effect, lab effect, week effect, plasma extraction, MS-run, ...

## Nature methods: Points of significance - Blocking

[https://www.nature.com/articles/nmeth.3005.pdf](https://www.nature.com/articles/nmeth.3005.pdf)

## Mouse example

```r
knitr::include_graphics("./figures/mouseTcell_RCB_design.png")
```
Duguet et al. (2017) MCP 16(8):1416-1432. doi: 10.1074/mcp.m116.062745

- All treatments of interest are present within block!
- We can estimate the effect of the treatment within block!
- We can isolate the between block variability from the analysis using linear model:
$$
y \sim \text{type} + \text{mouse}
$$
- Not possible with Perseus!

### Assess the impact of blocking in the tutorial session!

- Completely randomized design with only one cell type per mouse (Treg and Tconv)

$$\updownarrow$$

- Randomized complete block design assessing Treg and Tconv on each mouse

---

[← Francisella tularensis experiment](01-francisella-tularensis-experiment.md) · [Up: contents](index.md)
