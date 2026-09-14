---
title: rf.fit
source: https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf
source_file: sources/berkeley-stat-c245c-leishi/hw/hw2-sol.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# rf.fit

**Source:** [`hw/hw2-sol.pdf`](https://leishi-rocks.github.io/courses/ph240c/hw/hw2-sol.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
FL BD<br>BD FL<br>CW CW<br>CL CL<br>RW RW<br>sex sex<br>10 30 50 70 0 5 10 15 20<br>MeanDecreaseAccuracy MeanDecreaseGini<br><!-- End of picture text -->

5

```
prediction<-predict(rf.fit,newdata=train,type="class")
training.error<-sum(prediction!=train$sp)/length(prediction)
prediction<-predict(rf.fit,newdata=test,type="class")
test.error<-sum(prediction!=test$sp)/length(prediction)
```

```
data.frame(training.error,test.error)
```

`## training.error test.error ## 1 0 0.125` **(c)** `set.seed(6789) train.error <- c() test.error <- c() M_candidate <- c(10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1000)` **`for`** `(M` **`in`** `M_candidate){ fit <- boosting(sp ~ .,data=train, mfinal=M)` _`# Compute training error`_ `pred.train <- predict(fit, newdata = train, type = "class") train.error <- c(train.error, sum(pred.train$class != train$sp)/length(train$sp))` _`# Compute testing error`_ `pred.test <- predict(fit, newdata = test, type = "class") test.error <- c(test.error, sum(pred.test$class != test$sp)/length(test$sp)) cat("Running M=", M, "\n") } ## Running M= 10 ## Running M= 20 ## Running M= 30 ## Running M= 50 ## Running M= 70 ## Running M= 100 ## Running M= 200 ## Running M= 300 ## Running M= 500 ## Running M= 700 ## Running M= 1000 error.df <- data.frame(M = rep(M_candidate, 2), error = c(train.error, test.error), type = rep(c("training","test"), each=length(M_candidate))) ggplot(error.df, aes(x=M, y=error, col=type)) + geom_line()`

6


<!-- Start of picture text -->
0.12<br>0.08<br>type<br>test<br>training<br>0.04<br>0.00<br>0 250 500 750 1000<br>M<br>error<br><!-- End of picture text -->

```
#withM=30
```

```
fit<-boosting(sp~.,data=train,mfinal=30)
rpart.plot(fit$trees[[1]])
```

```
##Warning:Cannotretrievethedatausedtobuildthemodel(socannotdetermineroundintandis.binary
##Tosilencethiswarning:
```

- `## Call rpart.plot with roundint=FALSE,`

- `## or rebuild the rpart model with model=TRUE.`

7


<!-- Start of picture text -->
B<br>0.44<br>100%<br>B yes FL <  17 no<br>0.27<br>69%<br>CW  >= 36 B<br>0.39<br>48%<br>B BD <  13<br>0.16<br>35%<br>CW  >= 31 B<br>0.25<br>22%<br>BD < 9.8<br>B B B O O O<br>0.00 0.00 0.00 0.56 1.00 0.84<br>21% 12% 12% 10% 13% 31%<br><!-- End of picture text -->

```
data.frame(train.error[3],test.error[3])
```

`## train.error.3. test.error.3. ## 1 0 0.075` Alternatively we can use another package:

```
set.seed(6789)
train.error<-c()
test.error<-c()
```

```
M_candidate<-c(1:10,20,30,50,70,100,200,300,500,700,1000)
for(MinM_candidate){
fit<-adaboost(sp~.,data=train,nIter=M)
#Computetrainingerror
pred.train<-predict(fit,newdata=train,type="class")
train.error<-c(train.error,sum(pred.train$class!=train$sp)/length(train$sp))
#Computetestingerror
pred.test<-predict(fit,newdata=test,type="class")
test.error<-c(test.error,sum(pred.test$class!=test$sp)/length(test$sp))
cat("RunningM=",M,"\n")
}
```

```
##RunningM=1
##RunningM=2
##RunningM=3
##RunningM=4
##RunningM=5
```

8

```
##RunningM=6
##RunningM=7
##RunningM=8
##RunningM=9
##RunningM=10
##RunningM=20
##RunningM=30
##RunningM=50
##RunningM=70
##RunningM=100
##RunningM=200
##RunningM=300
##RunningM=500
##RunningM=700
##RunningM=1000
```

```
error.df<-data.frame(M=rep(M_candidate,2),
```

```
error=c(train.error,test.error),
```

```
type=rep(c("training","test"),each=length(M_candidate)))
ggplot(error.df,aes(x=M,y=error,col=type))+geom_line()
```


<!-- Start of picture text -->
0.15<br>0.10 type<br>test<br>training<br>0.05<br>0.00<br>0 250 500 750 1000<br>M<br>error<br><!-- End of picture text -->

Choose M = 10(or 20, 30, 50) works well in this problem, since larger M won’t lead to significant increase in the training and testing accuracy but will render the algorithm more time-consuming.

(d) A table summarizing the accuracy:

9

|Points|Training|Testing|
|---|---|---|
|tree|0.10625|0.1|
|rF|0|0.125|
|adaboost|0|0.075|


Based on our results, we can see that Adaboost performs the best, with a testing error of 7.5% as opposed to 10.0% with the Classification tree and 12.5% with the Random Forest. In terms of variable important, the same variables are considered the most important by all methods in classifying the crab species.: FL, BD and CW.

10

#### **Question 3**

#### **Data importing and preprocessing**

```
load("dataHW2.Rda")
data<-drug.effectiveness%>%rename(effectiveness=effectivness)
data$effectiveness<-as.factor(data$effectiveness)
```

```
train_index<-sample(nrow(data),size=floor(0.8*nrow(data)))
train<-data[train_index,]
test<-data[-train_index,]
```

#### **Simple EDA** :

```
ggplot(data,aes(x=drug1.dose,y=drug2.dose,color=effectiveness))+
geom_point()
```


<!-- Start of picture text -->
4<br>3<br>effectiveness<br>0<br>1<br>2<br>1<br>1 2 3 4<br>drug1.dose<br>drug2.dose<br><!-- End of picture text -->

#### **Logistic regression**

```
fit.logit<-glm(effectiveness~.,data=train,family="binomial")
summary(fit.logit)
```

```

---

[← CPnsplitrelerrorxerrorxstd](05-cpnsplitrelerrorxerrorxstd.md) · [Up: contents](index.md) · [Call →](07-call.md)
