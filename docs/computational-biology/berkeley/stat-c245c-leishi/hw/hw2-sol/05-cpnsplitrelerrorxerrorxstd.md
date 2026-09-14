---
title: CPnsplitrelerrorxerrorxstd
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw2-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# CPnsplitrelerrorxerrorxstd

**Source:** [`hw/hw2-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##10.4000001.00001.2500.076547
##20.1437510.60000.7000.075416
##30.0500030.31250.4000.063246
##40.0000050.21250.3750.061714
plotcp(fit)
```

3

### size of tree


<!-- Start of picture text -->
1 2 4 6<br>Inf 0.24 0.085 0<br>cp<br>rpart.plot(fit)<br>B<br>0.50<br>100%<br>yes FL < 17 no<br>B O<br>0.35 0.82<br>69% 31%<br>CW >= 36 CW >= 44<br>B O<br>0.46 0.65<br>49% 16%<br>BD < 12 FL < 20<br>B B O B O O<br>0.10 0.21 0.93 0.00 0.94 1.00<br>19% 32% 17% 5% 11% 15%<br># Alternative method without "rpart.plot"<br># plot(fit, uniform=TRUE, main="Classification Tree for Crabs")<br>1.4<br>1.2<br>1.0<br>0.8<br>0.6<br>X−val Relative Error<br>0.4<br>0.2<br><!-- End of picture text -->

4

```
#text(fit,use.n=TRUE,all=TRUE,cex=.8)
#trainingerrorandtesterror
```

```
prediction<-predict(fit,newdata=train,type="class")
training.error<-sum(prediction!=train$sp)/length(prediction)
prediction<-predict(fit,newdata=test,type="class")
test.error<-sum(prediction!=test$sp)/length(prediction)
data.frame(training.error,test.error)
```

`## training.error test.error ## 1 0.10625 0.1` The variables used in the tree: FL, CW and BD. The training error and testing error are 10.6% and 10.0% respectively.

**(b)** `set.seed(6789) rf.fit <- randomForest( sp ~ sex + FL + RW + CL + CW + BD, data=train, ntree=1000, mtry=5, importance = T ) varImpPlot(rf.fit)`

---

[← Rootnodeerror:80/160=0.5](04-rootnodeerror-80-160-0-5.md) · [Up: contents](index.md) · [rf.fit →](06-rf-fit.md)
