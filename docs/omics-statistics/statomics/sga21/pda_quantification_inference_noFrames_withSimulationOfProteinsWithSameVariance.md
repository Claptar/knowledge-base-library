---
title: Pda quantification inference noFrames withSimulationOfProteinsWithSameVariance
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference_noFrames_withSimulationOfProteinsWithSameVariance.Rmd
source_file: sources/statomics-sga21/pda_quantification_inference_noFrames_withSimulationOfProteinsWithSameVariance.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Pda quantification inference noFrames withSimulationOfProteinsWithSameVariance

**Source:** [`pda_quantification_inference_noFrames_withSimulationOfProteinsWithSameVariance.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/pda_quantification_inference_noFrames_withSimulationOfProteinsWithSameVariance.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a>


```r
library(tidyverse)
set.seed(1243)
simSameVar<-sapply(1:1066,function(m,n) rnorm(n,sd=1),n=6) %>% t
sds <- apply(simSameVar,1,function(y,group) lm(y ~ group) %>% sigma, group=rep(0:1,each=3))
varSq <- limma::squeezeVar(sds^2,4)

data.frame(sdOrig = sds, sdMod = varSq$var.post^.5) %>%
  ggplot(aes(sdOrig,sdMod)) +
  geom_point() +
  xlim(range(sds)) +
  ylim(range(sds))
```

---

[Up: contents](index.md)
