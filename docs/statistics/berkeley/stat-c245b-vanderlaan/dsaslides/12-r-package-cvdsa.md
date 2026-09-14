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

- Example 5. Checking the Experimental Treatment Assignment assumption. (With ETA violations) Code:

n<-2000;

w1<-runif(n);w2<-runif(n); w3<-runif(n); w4<-runif(n); w<-cbind(w1,w2,w3,w4);

---

[← R-package cvDSA](11-r-package-cvdsa.md) · [Up: contents](index.md) · [Let g(A|W) = logit^(-1) (-1 + w1 - w2 + w1w3) p.vec <- diag(4) →](13-let-g-a-w-logit--1--1-w1---w2-w1w3-p-vec---diag-4.md)
