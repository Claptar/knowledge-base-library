---
title: Scientific Method
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd
source_file: sources/gtpb-psls20/theory/01-intro.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Scientific Method

**Source:** [`theory/01-intro.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/01-intro.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

- Empirical data is key in the life sciences.
- Research is largely driven by data.

```r
plot(0,0,col=0,xaxt="none",yaxt="none",axes=FALSE,xlab="",ylab="",cex=4,ylim=c(-.5,1.5),xlim=c(-.5,1.5))
lines(c(0,1),c(0,0),lwd=4)
lines(c(0,.5),c(0,1),lwd=4)
lines(c(.5,1),c(1,0),lwd=4)
text(0.5,1.2,"Nature",cex=2)
text(0.8,.5,"Experiment",cex=2,pos=4,col="darkred")
text(1,0,"Data",cex=2,pos=4)
text(0.2,.5,"Theory",cex=2,pos=2,col="darkred")
text(0,0,"Model",cex=2,pos=2)
text(0.5,-0.3,"Statistical\nInference",cex=2,col="darkred")
```

- *Nature*: biological process which we study

- *Deduction*: deduce logical consequences of  the theory/hypothesis that can be experimentally validated.

- *Experiment*: collect data on the process. The data are a manifestation of the real process. The experiment has to be *representative* and *reproducible* and should challenge the theory. *Experimental Design*!

- *Statistical inference*: Bridge to confront the model/hypothesis to the data $\rightarrow$ Cornerstone of the scientific method.

- *Falsification principle*: Data cannot be used to prove a model/hypothesis, only to reject it.

- *Data-exploration and analysis* is typically used to refine the theory and to generate new hypotheses.

---

---

[← Salk Study](03-salk-study.md) · [Up: contents](index.md) · [Role of Statistics in the Life Sciences →](05-role-of-statistics-in-the-life-sciences.md)
