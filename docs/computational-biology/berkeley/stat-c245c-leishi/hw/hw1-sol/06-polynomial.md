---
title: Polynomial
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw1-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Polynomial

**Source:** [`hw/hw1-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
svm.poly<-svm(y~.,data=data_run,kernel="polynomial")
summary(svm.poly)
```

```
##
##Call:
```

4

```
##svm(formula=y~.,data=data_run,kernel="polynomial")
##
##
##Parameters:
##SVM-Type:C-classification
##SVM-Kernel:polynomial
##cost:1
##degree:3
##coef.0:0
##
##NumberofSupportVectors:235
##
##(118117)
##
##
##NumberofClasses:2
##
##Levels:
##01
#Insampleprediction
y.pred.poly<-predict(svm.poly,x)
table(y.pred.poly,y)
##y
##y.pred.poly01
##016181
##1257
```

**Sigmoid** `svm.sigmoid <- svm(y ~ ., data = data_run, kernel = "sigmoid") summary(svm.sigmoid) ## ## Call: ## svm(formula = y ~ ., data = data_run, kernel = "sigmoid") ## ## ## Parameters: ## SVM-Type: C-classification ## SVM-Kernel: sigmoid ## cost: 1 ## coef.0: 0 ## ## Number of Support Vectors: 165 ## ## ( 82 83 ) ## ## ## Number of Classes: 2 ## ## Levels: ## 0 1`

5

```
#Insampleprediction
y.pred.sigmoid<-predict(svm.sigmoid,x)
table(y.pred.sigmoid,y)
```

```
##y
##y.pred.sigmoid01
##014438
##119100
```

6

---

[← Gaussian SVM](05-gaussian-svm.md) · [Up: contents](index.md)
