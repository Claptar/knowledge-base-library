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

▶ Example 4. Checking the Experimental Treatment Assignment assumption. (No ETA violation) Code:

obs.data.ETA <- check.ETA(y=y, a=a, v=w1, w=cbind(w1,w2), data=obs.data, yfamily=’gaussian’, afamily=’binomial’, model.msm=list(Model=list(c(1,0),c(0,1))), model.aw=list(Model=list(c(1,0),c(0,1))), model.av=list(Model=list(c(1))),

model.yaw=list(Model=list(c(1,0,0),c(0,1,0),c(0,0,1),c(0,1,1))), model.yyaw=list(Size=5, Int=2), accuracy=1e-5, stable.wt=F, n.b=1000, n.sim=100, index.v.inW=c(1))

Nov. 8, 2004

26

---

[← R-package cvDSA](10-r-package-cvdsa.md) · [Up: contents](index.md) · [R-package cvDSA →](12-r-package-cvdsa.md)
