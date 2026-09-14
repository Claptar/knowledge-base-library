---
title: Question 1
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw1-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Question 1

**Source:** [`hw/hw1-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw1-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

(a) For a logistic model we have the success probability

which in turn gives


```
b0<--4
b1<-0.05
b2<-1
x1_1<-5
x1_2<-3.5
p<-exp(b0+b1*x1_1+b2*x1_2)/(1+exp(b0+b1*x1_1+b2*x1_2))
cat("TheprobabilityofgettinganAforthisstudentis:",round(p,3))
```

```
##TheprobabilityofgettinganAforthisstudentis:0.438
```

- (b) Recall definition of the odds:


For logisitic model we have


```
p_odds<-exp(b0+b1*x1_1+b2*x1_2)#=p/(1-p)
cat("TheoddsofgettinganAforthisstudentis:",round(p_odds,3))
```

```
##TheoddsofgettinganAforthisstudentis:0.779
```

- (c) Note that _p_ = 50 gives a zero log-odds:


Solving for _X_ 1 we have

```
x_1_pred<--(b0+b2*x1_2)/b1
cat("Thisstudentneedstostudyfor",x_1_pred,"hourstogetanA.")
```

```
##Thisstudentneedstostudyfor10hourstogetanA.
```

1

---

[Up: contents](index.md) · [Question 2 →](02-question-2.md)
