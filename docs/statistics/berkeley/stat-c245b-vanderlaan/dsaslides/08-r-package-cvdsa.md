---
title: R-package cvDSA
source: https://vanderlaan-lab.org/teach-files/dsaslides.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/dsaslides.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# R-package cvDSA

**Source:** [`dsaslides.pdf`](https://vanderlaan-lab.org/teach-files/dsaslides.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

- Example 1. Generating an observed data set. Let sample size N = 2000, W = {W1, W2}, W1 ∼ U (0, 1), W2 ∼ U (0, 1), the treatment model is

   - g(A|W ) = logit<sup>−1</sup> (1 − W1 + W2),

the Fx-part model is

- Q(Y |A, W ) = 1 + 2A + 1.5W1 + W2 − W1 × W2.

Nov. 8, 2004

18

Code: n <- 1000 w1 <- runif(n, 0, 1); w2 <- runif(n, 0, 1); w <- cbind(w1=w1, w2=w2);

model.aw <- list(formula=list(c(1,0),c(0,1)), coef=c(1,-1,1));

model.yaw <- list(formula=list(c(1,0,0),c(0,1,0), c(0,0,1), c(0,1,1)), coef=c(1, 2, 1.5, 1, -1));

obs.data <- create.obs.data(w, afamily=’binomial’, yfamily=’gaussian’, model.yaw, model.aw)

Nov. 8, 2004

19

---

[← R-package cvDSA](07-r-package-cvdsa.md) · [Up: contents](index.md) · [R-package cvDSA →](09-r-package-cvdsa.md)
