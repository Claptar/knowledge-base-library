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

▶ Example 3. selecting the marginal structural model. Code:

a<-obs.data$a

msm.iptw <- cvMSM(y=y, a=a, v=w1, w=w, data=obs.data, model.msm=list(Size=3, Order=c(1,2), Int=1), model.av=list(Model=list(c(1))), model.aw=list(Model=NULL, Size=3,Int=2), mapping=’IPTW’, fitting=’IPTW’, stable.wt=T)

Nov. 8, 2004

23

Result: g(A|W ): CV selects: size = 2 , interactions = 2 with min.risk: 0.5584379

$Formula [1] "Intercept + w1 + w2"

$Coefficients (Intercept) w1 w2 1.204914 -1.356494 1.080563 MSM E(Ya|a, V ) CV selects: size = 2 with min.risk: 1.056349 IPTW estimator: $Formula [1] "Intercept + a + w1" $Coefficients

Nov. 8, 2004

24

(Intercept) a w1 1.5134810 1.9898810 0.9660859

Nov. 8, 2004

25

---

[← R-package cvDSA](09-r-package-cvdsa.md) · [Up: contents](index.md) · [R-package cvDSA →](11-r-package-cvdsa.md)
