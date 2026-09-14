---
title: Let g(A|W) = logit^(-1) (-1 + w1 - w2 + w1w3) p.vec <- diag(4)
source: https://vanderlaan-lab.org/teach-files/dsaslides.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/dsaslides.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Let g(A|W) = logit^(-1) (-1 + w1 - w2 + w1w3) p.vec <- diag(4)

**Source:** [`dsaslides.pdf`](https://vanderlaan-lab.org/teach-files/dsaslides.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

model.aw <- list(formula = list(p.vec[1,], p.vec[2,], p.vec[1,]+p.vec[3,]), coef = c(-1, 1, -5, 1)) # about 60% violations

- # Let E(Y|A, W)=-1+A+w1+w2+w1*w3;

Nov. 8, 2004

27

p.vec <- diag(5) model.yaw <- list(formula=list(p.vec[1,],p.vec[2,],p.vec[3,], p.vec[2,]+p.vec[4,]), coef=c(-1, 1, 1, 1, 1));

obs.data <- create.obs.data(w, afamily=’binomial’, yfamily=’gaussian’, model.yaw, model.aw)

obs.data.ETA <- check.ETA(y=y, a=a, v=w1, w=w, data=obs.data, yfamily=’gaussian’, afamily=’binomial’, model.msm=list(Model=list(c(1,0),c(0,1))), model.aw=list(Model=model.aw$formula), model.av=list(Model=list(c(1))), model.yaw=list(Model=model.yaw$formula), wt.censor=NULL, ncv=5, ncv.nuisance=5, stable.wt=F, fixed.terms=NULL, cv.risk=F, n.b=1000, n.sim=100, index.v.inW=c(1))

Nov. 8, 2004

28

check.ETA()

Bootstrap distribution of IPTW causal coefficients: Without ETA violations

Nov. 8, 2004

29

**Histogram of beta.iptw[, i]**

**Histogram of beta.iptw[, i]**


<!-- Start of picture text -->
1.2 1.3 1.4 1.5 1.6 1.85 1.95 2.05 2.15<br>(Intercept) a<br>Histogram of beta.iptw[, i]<br>0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5<br>30<br>20<br>25<br>15<br>20<br>15<br>10<br>Frequency Frequency 10<br>5<br>5<br>0 0<br>30<br>25<br>20<br>15<br>Frequency<br>10<br>5<br>0<br><!-- End of picture text -->

v

Nov. 8, 2004

30

check.ETA()

Bootstrap distribution of IPTW causal coefficients: With ETA violations

Nov. 8, 2004

31

**Histogram of beta.iptw[, i]**

**Histogram of beta.iptw[, i]**


<!-- Start of picture text -->
−0.8 −0.7 −0.6 −0.5 −0.4 −0.3 0.6 0.7 0.8 0.9 1.0<br>(Intercept) a<br>Histogram of beta.iptw[, i]<br>1.2 1.4 1.6 1.8 2.0<br>25<br>15<br>20<br>15<br>10<br>Frequency 10 Frequency<br>5<br>5<br>0 0<br>25<br>20<br>15<br>10<br>Frequency<br>5<br>0<br><!-- End of picture text -->

v

---

[← R-package cvDSA](12-r-package-cvdsa.md) · [Up: contents](index.md)
