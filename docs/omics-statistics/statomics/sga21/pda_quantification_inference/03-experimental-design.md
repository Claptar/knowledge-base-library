---
title: Experimental Design
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference.Rmd
source_file: sources/statomics-sga21/pda_quantification_inference.Rmd
licence: CC BY-NC-SA 4.0
route: markdown
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`pda_quantification_inference.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference.Rmd) — statomics-sga21, licensed CC BY-NC-SA 4.0. Converted 2026-09-18 from `.Rmd`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Experimental Design

### Sample size

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

### Blocking

$$
\sigma^2= \sigma^2_{bio}+\sigma^2_\text{lab} +\sigma^2_\text{extraction} + \sigma^2_\text{run} + \ldots
$$

- Biological: fluctuations in protein level between mice, fluctations in protein level between cells, ...
- Technical: cage effect, lab effect, week effect, plasma extraction, MS-run, ...

### Nature methods: Points of significance - Blocking

[https://www.nature.com/articles/nmeth.3005.pdf](https://www.nature.com/articles/nmeth.3005.pdf)

### Mouse example

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

#### Assess the impact of blocking in the tutorial session!

- Completely randomized design with only one cell type per mouse (Treg and Tconv)

$$\updownarrow$$

- Randomized complete block design assessing Treg and Tconv on each mouse

## Software & code

- Our R/Bioconductor package [msqrob2](https://www.bioconductor.org/packages/release/bioc/html/msqrob2.html) can be used in R markdown scripts or with a GUI/shinyApp in the [msqrob2gui](https://github.com/statOmics/msqrob2gui) package.

- The GUI is intended as a introduction to the key concepts of proteomics data analysis for users who have no experience in R.

- However, learning how to code data analyses in R markdown scripts is key for open en reproducible science and for reporting your proteomics data analyses and interpretation in a reproducible way.

- More information on our tools can be found in our papers [@goeminne2016], [@goeminne2020] and [@sticker2020]. Please refer to our work when using our tools.

- Clips on the code on importing the data and preprocessing can be found in [Part I Preprocessing](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_preprocessing.html)

- A clip on the code for modelling and statistical inference with msqrob2 is included below

## References

---

[← Francisella tularensis experiment](02-francisella-tularensis-experiment.md) · [Up: contents](index.md)
