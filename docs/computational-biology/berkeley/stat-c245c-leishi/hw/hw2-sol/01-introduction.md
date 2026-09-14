---
title: Introduction
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw2-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Introduction

**Source:** [`hw/hw2-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# Homework2_sol

Lei Shi

12/6/2021

### **R Markdown**

**Question 1**

(a) See Figure 1.


Figure 1: Tree

(b) See Figure 2. _No Y es Y es No_ (c) (2,1): _X_ 2 _< −_ 1 _._ 55? _−−→ X_ 2 _<_ 1 _._ 25? _−−→ X_ 1 _<_ 2 _._ 25? _−−→ X_ 1 _< −_ 1 _._ 8? _−−→_ Classified to _−_ 1.

1


Figure 2: Tree

2

#### **Question 2**

```
data<-MASS::crabs
set.seed(6789)
sex.levels<-levels(data$sex)
sp.levels<-levels(data$sp)
train<-data.frame()
test<-data.frame()
for(sexinsex.levels){
for(spinsp.levels){
stratum<-data%>%filter(sex==!!sex&sp==!!sp)
train.index<-sample(seq_len(nrow(stratum)),size=floor(0.8*nrow(stratum)))
train<-rbind(train,stratum[train.index,])
test<-rbind(test,stratum[-train.index,])
}
}
train<-subset(train,select=-index)
test<-subset(test,select=-index)
```

#### **(a)**

```
fit<-rpart(sp~.,method="class",data=train,
control=rpart.control(minsplit=1,
minbucket=1,
xval=10,
cp=0,
maxdepth=3))
printcp(fit)
```

```

---

[Up: contents](index.md) · [Classificationtree →](02-classificationtree.md)
