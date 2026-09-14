---
title: DevianceResiduals
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw2-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# DevianceResiduals

**Source:** [`hw/hw2-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##Min1QMedian3QMax
```

11

`## -0.9643 -0.9079 -0.8842 1.4243 1.5935 ## ## Coefficients: ## Estimate Std. Error z value Pr(>|z|) ## (Intercept) -0.85972 0.41364 -2.078 0.0377 * ## drug1.dose -0.09043 0.13030 -0.694 0.4877 ## drug2.dose 0.15679 0.13294 1.179 0.2382 ## --## Signif. codes: 0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1 ## ## (Dispersion parameter for binomial family taken to be 1) ## ## Null deviance: 1018.9 on 799 degrees of freedom ## Residual deviance: 1017.3 on 797 degrees of freedom ## AIC: 1023.3 ## ## Number of Fisher Scoring iterations: 4` _`# Compute training error`_ `pred.train <- factor(as.numeric(predict(fit.logit, newdata = train) > 0.5)) levels(pred.train) <- c("1", "0") train.error <- sum(pred.train != train$effectiveness)/length(train$effectiveness)` _`# Compute testing error`_ `pred.test <- factor(as.numeric(predict(fit.logit, newdata = test) > 0.5)) levels(pred.test) <- c("1", "0") test.error <- sum(pred.test != test$effectiveness)/length(test$effectiveness) data.frame(train.error, test.error) ## train.error test.error ## 1 0.66625 0.635` **SVM with Gaussian Kernel** `fit.svm <- svm(effectiveness ~ ., data = train) summary(fit.svm) ## ## Call: ## svm(formula = effectiveness ~ ., data = train) ## ## ## Parameters: ## SVM-Type: C-classification ## SVM-Kernel: radial ## cost: 1 ## ## Number of Support Vectors: 201 ## ## ( 101 100 ) ## ## ## Number of Classes: 2 ## ## Levels:`

12

#### `## 0 1`

_`# Compute training error`_ `pred.train <- predict(fit.svm, newdata = train, type = "class") train.error <- sum(pred.train != train$effectiveness)/length(train$effectiveness)` _`# Compute testing error`_ `pred.test <- predict(fit.svm, newdata = test, type = "class") test.error <- sum(pred.test != test$effectiveness)/length(test$effectiveness) data.frame(train.error, test.error) ## train.error test.error ## 1 0.085 0.095` **Classification Tree** `fit.tree <- rpart(effectiveness ~ ., method="class", data = train, control = rpart.control(minsplit =1, minbucket=1, xval = 10, cp=0, maxdepth = 3))` _`# Compute training error`_ `pred.train <- predict(fit.tree, newdata = train, type = "class") train.error <- sum(pred.train != train$effectiveness)/length(train$effectiveness)` _`# Compute testing error`_ `pred.test <- predict(fit.tree, newdata = test, type = "class") test.error <- sum(pred.test != test$effectiveness)/length(test$effectiveness) data.frame(train.error, test.error)`

`## train.error test.error ## 1 0.29625 0.355` **Random Forest** `fit.rf <- randomForest( effectiveness ~ ., data = train, ntree = 1000, mtry = 2, importance = T ) print(fit.rf) ## ## Call: ## randomForest(formula = effectiveness ~ ., data = train, ntree = 1000, mtry = 2, importance = T) ## Type of random forest: classification ## Number of trees: 1000 ## No. of variables tried at each split: 2 ## ## OOB estimate of error rate: 9.38% ## Confusion matrix:`

13

```
##01class.error
##0498350.06566604
##1402270.14981273
```

```
#Computetrainingerror
pred.train<-predict(fit.rf,newdata=train,type="class")
train.error<-sum(pred.train!=train$effectiveness)/length(train$effectiveness)
```

```
#Computetestingerror
pred.test<-predict(fit.rf,newdata=test,type="class")
test.error<-sum(pred.test!=test$effectiveness)/length(test$effectiveness)
```

```
data.frame(train.error,test.error)
```

```
##train.errortest.error
##100.095
```

#### **Adaboost**

```
fit.boost<-boosting(effectiveness~.,data=train,mfinal=30)
rpart.plot(fit.boost$trees[[1]])
```

```
##Warning:Cannotretrievethedatausedtobuildthemodel(socannotdetermineroundintandis.binary
##Tosilencethiswarning:
##Callrpart.plotwithroundint=FALSE,
```

```
##orrebuildtherpartmodelwithmodel=TRUE.
```


<!-- Start of picture text -->
0<br>0.32<br>100%<br>yes drug2.dose < 3.2 no<br>0 0<br>0.30 0.45<br>88% 12%<br>drug1.dose < 2.4 drug1.dose >= 2.3<br>0 0<br>0.22 0.37<br>41% 47%<br>drug2.dose < 2.5 drug2.dose >= 2.3<br>1 0 1<br>0.83 0.12 0.87<br>11% 31% 16%<br>drug2.dose < 2.7 drug1.dose >= 2.5 drug1.dose < 2.6<br>1 1 0<br>0.55 0.64 0.26<br>3% 3% 3%<br>drug2.dose >= 2.6 drug2.dose >= 2.8 drug2.dose < 2<br>0 0 1 1 0 0 1 0 1 1 0 1<br>0.00 0.10 0.92 0.92 0.07 0.14 0.87 0.00 0.67 1.00 0.07 0.97<br>30% 1% 2% 8% 28% 1% 2% 2% 1% 13% 7% 5%<br><!-- End of picture text -->

```
#Computetrainingerror
```

```
pred.train<-predict(fit.boost,newdata=train,type="class")
train.error<-sum(pred.train$class!=train$effectiveness)/length(train$effectiveness)
```

```
#Computetestingerror
```

```
pred.test<-predict(fit.boost,newdata=test,type="class")
```

14

```
test.error<-sum(pred.test$class!=test$effectiveness)/length(test$effectiveness)
```

```
data.frame(train.error,test.error)
```

```
##train.errortest.error
##100.1
```

For this classification problem, logistic regression is based on a misspecified model, so we don’t expect a high prediction accuracy. The other algorithms(svm with gaussian kernel and tree type methods) fit with the structure of the data and demonstrate high prediction accuracy.

We are not grading based on accuracy though so take it easy!

15

---

[← Call](07-call.md) · [Up: contents](index.md)
