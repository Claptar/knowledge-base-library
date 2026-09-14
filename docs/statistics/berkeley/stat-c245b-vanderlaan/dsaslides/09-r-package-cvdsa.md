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

▶ Example 2. selecting the nuisance parameter models. Code:

a<-obs.data$a

cv.model.aw<-cvGLM(y=a, x=w, ncv=5, yx.model=list(Size=3, Order=c(2,2), Int=2), myfamily=’binomial’, printout=T, detail=T)

y<-obs.data$y

cv.model.yaw<-cvGLM(y=y, x=cbind(a,w), ncv=5, yx.model=list(Size=5, Order=c(1,2,1), Int=2), printout=T)

Nov. 8, 2004

20

Result: g(A|W ): CV selects: size = 2 , interactions = 2 with min.risk: 0.5584379 $Formula [1] "Intercept + w1 + w2" $Coefficients (Intercept) w1 w2 1.204914 -1.356494 1.080563

Nov. 8, 2004

21

E(Y |A, W ): CV selects: size = 4 , interactions = 2 with min.risk: 1.018344 $Formula [1] "Intercept + a + w1 + w2 + w1*w2" $Coefficients (Intercept) a w1 w2 w1*w2 0.959001 2.002093 1.475317 1.089650 -1.026595

Nov. 8, 2004

22

---

[← R-package cvDSA](08-r-package-cvdsa.md) · [Up: contents](index.md) · [R-package cvDSA →](10-r-package-cvdsa.md)
