---
title: Gaussian SVM
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw1-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Gaussian SVM

**Source:** [`hw/hw1-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
svm.gaussian<-svm(y~.,data=data_run)
summary(svm.gaussian)
```

```
##
##Call:
##svm(formula=y~.,data=data_run)
##
##
##Parameters:
##SVM-Type:C-classification
##SVM-Kernel:radial
##cost:1
##
##NumberofSupportVectors:159
##
##(8079)
##
##
##NumberofClasses:2
##
##Levels:
##01
#Insampleprediction
y.pred.gaussian<-predict(svm.gaussian,x)
table(y.pred.gaussian,y)
##y
##y.pred.gaussian01
##014334
##120104
```

---

[← Data importing and preprocessing](04-data-importing-and-preprocessing.md) · [Up: contents](index.md) · [Polynomial →](06-polynomial.md)
