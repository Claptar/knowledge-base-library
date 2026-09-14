---
title: Sum of squares and Anova
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd
source_file: sources/gtpb-psls20/theory/07-Anova.Rmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Sum of squares and Anova

**Source:** [`theory/07-Anova.Rmd`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/theory/07-Anova.Rmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.Rmd` (lossless)

Similar to simple linear regression we will use sum of squares to derive the F-test.
\vspace{-10pt}
\begin{eqnarray*}
\text{SSR}&=&\sum\limits_{i=1}^n (\hat Y_i -\bar Y)^2\\
&=& \sum\limits_{i=1}^n (\hat{g} (x_{i1},x_{i2}) - \bar Y)^2\\
&=& \sum\limits_{i=1}^n (\hat\beta_0+\hat\beta_1x_{i1}+\hat\beta_2x_{i2}) - \bar Y)^2\\
&=& \sum\limits_{i=1}^{n_1} (\hat\beta_0 - \bar Y)^2 +\sum\limits_{i=1}^{n_2} (\hat\beta_0 + \hat\beta_1 - \bar Y)^2+\sum\limits_{i=1}^{n_3} (\hat\beta_0 + \hat\beta_2 - \bar Y)^2\\
&=& \sum\limits_{i=1}^{n_1} (\bar Y_1- \bar Y)^2 +\sum\limits_{i=1}^{n_2} (\bar Y_2- \bar Y)^2+\sum\limits_{i=1}^{n_3} (\bar Y_3 - \bar Y)^2\\
\end{eqnarray*}
with $n_1$, $n_2$ en $n_3$ the number of observations in each group (here $n-1=n_2=n_3=12$).


\begin{eqnarray*}
\text{SSR}&=&\sum\limits_{i=1}^n (\hat Y_i -\bar Y)^2
\end{eqnarray*}

- Sum of squares is again equivalent with comparison of model (1) and reduced model with an intercept, only.
- For reduced model the intercept is estimated by the sample mean.
- This sum of squares has g-1=2 degrees of freedom:

  - g=3 model parameters - 1 parameter to estimate overall sample mean or
  - g=3 par. in complex model - 1 par. in reduced model.


## Decomposition of Total Sum of Squares

 - The convention in the Anova setting is to denote the sum of squares as SST, the **Sum of Squares of the Treatment (treatment)** or as SSBetween.
- The sum of squares of the regression indeed reflects the variability between the groups.
- The corresponding mean sum of squares becomes  $\text{MST}=\text{SST}/2$.

The decomposition of SSTot can be written as
$$
  \text{SSTot} = \text{SST} + \text{SSE}
$$

##SSTot

\vspace{10pt}

```r
par(mfrow=c(1,2))
jitIk=runif(36,-.2,.2)+rep(1:3,each=12)
plot(prostac~dose,data=prostacyclin,xlab="Arachidonic acid dose ",ylab="Prostacyclin (ng/ml)",cex.axis=1.5,cex.lab=1.5,cex.main=1.5)
points(jitIk,prostacyclin$prostac,col=col,pch=19)
points(jitIk,prostacyclin$prostac,col=4)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=17,col=c("bisque","coral","darkcyan"),cex=1.5)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=2,col=1,cex=1.5)
abline(h=mean(prostacyclin$prostac),lty=1)
for (i in 1:36) lines(rep(jitIk[i],2),c(mean(prostacyclin$prostac),prostacyclin$prostac[i]),col=4,lty=2)
jitIk=runif(36,-.2,.2)+rep(1:3,each=12)

plot(rep(1,36),prostacyclin$prostac-mean(prostacyclin$prostac),xaxt="none",ylab="Deviations",cex.lab=1.5,cex.main=1.5,cex.axis=1.5,col=as.character(prostacyclin$col),xlim=c(1,3),pch=19,xlab="")
points(rep(1,36),prostacyclin$prostac-mean(prostacyclin$prostac),pch=1,col=4)
axis(at=1:3,labels=c(expression(paste(y[i]," - ",bar(y))),expression(paste(bar(y)[j]," - ",bar(y))),expression(paste(y[i]," - ",bar(y)[j]))),side=1,cex.axis=1.5)
```


##SST

\vspace{10pt}

```r
par(mfrow=c(1,2))
plot(prostac~dose,data=prostacyclin,xlab="Arachidonic acid dose ",ylab="Prostacyclin (ng/ml)",cex.axis=1.5,cex.lab=1.5,cex.main=1.5)
points(jitIk,prostacyclin$prostac,col=col,pch=19)
points(jitIk,prostacyclin$prostac,col=4)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=17,col=c("bisque","coral","darkcyan"),cex=1.5)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=2,col=2,cex=1.5)
abline(h=mean(prostacyclin$prostac),lty=1)
for (i in 1:3) lines(rep(i,2),c(mean(prostacyclin$prostac),predict(model1,data.frame(dose=levels(prostacyclin$dose)[i]))),col=2,lty=2)

plot(rep(1,36),prostacyclin$prostac-mean(prostacyclin$prostac),xaxt="none",ylab="Deviations",cex.lab=1.5,cex.main=1.5,cex.axis=1.5,col=as.character(prostacyclin$col),xlim=c(1,3),pch=19,xlab="")
points(rep(1,36),prostacyclin$prostac-mean(prostacyclin$prostac),pch=1,col=4)
points(rep(2,3),predict(model1,data.frame(dose=factor(c(10,25,50))))-mean(prostacyclin$prostac),pch=17,col=unique(prostacyclin$col),cex=1.5)
points(rep(2,3),predict(model1,data.frame(dose=factor(c(10,25,50))))-mean(prostacyclin$prostac),pch=2,cex=1.5,col=2)
axis(at=1:3,labels=c(expression(paste(y[i]," - ",bar(y))),expression(paste(bar(y)[j]," - ",bar(y))),expression(paste(y[i]," - ",bar(y)[j]))),side=1,cex.axis=1.5)
```

##SSE

\vspace{10pt}

```r
par(mfrow=c(1,2))
plot(prostac~dose,data=prostacyclin,xlab="Arachidonic acid dose ",ylab="Prostacyclin (ng/ml)",cex.axis=1.5,cex.lab=1.5,cex.main=1.5)
points(jitIk,prostacyclin$prostac,col=col,pch=19)
points(jitIk,prostacyclin$prostac,col=1)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=17,col=c("bisque","coral","darkcyan"),cex=1.5)
points(1:3,predict(model1,data.frame(dose=factor(c(10,25,50)))),pch=2,col=2,cex=1.5)
for (i in 1:3) lines(c(i-.2,i+.2),rep(predict(model1,data.frame(dose=levels(prostacyclin$dose)[i])),2),col=c("bisque","coral","darkcyan")[i])
abline(h=mean(prostacyclin$prostac),lty=1)
for (i in 1:36) lines(rep(jitIk[i],2),c(prostacyclin$prostac[i],model1$fitted[i]),col=1,lty=2)

plot(rep(1,36),prostacyclin$prostac-mean(prostacyclin$prostac),xaxt="none",ylab="Deviations",cex.lab=1.5,cex.main=1.5,cex.axis=1.5,col=as.character(prostacyclin$col),xlim=c(1,3),pch=19,xlab="")
points(rep(1,36),prostacyclin$prostac-mean(prostacyclin$prostac),pch=1,col=4)
points(rep(2,3),predict(model1,data.frame(dose=factor(c(10,25,50))))-mean(prostacyclin$prostac),pch=17,col=unique(prostacyclin$col),cex=1.5)
points(rep(2,3),predict(model1,data.frame(dose=factor(c(10,25,50))))-mean(prostacyclin$prostac),pch=2,col=2,cex=1.5)
points(rep(3,36),model1$res,pch=19,col=as.character(prostacyclin$col))
points(rep(3,36),model1$res,pch=1)
axis(at=1:3,labels=c(expression(paste(y[i]," - ",bar(y))),expression(paste(bar(y)[j]," - ",bar(y))),expression(paste(y[i]," - ",bar(y)[j]))),side=1,cex.axis=1.5)
```


## Anova test

Test $H_0: \beta_1=\beta_2=0$ with $F$-test.
$$
  F = \frac{\text{MST}}{\text{MSE}}
$$

with

- $\text{MST}=\text{SST}/(g-1)$
\vspace{10pt}
- $\text{MSE}=\text{SSE}/(n-p)$
\vspace{10pt}
- Test statistic compares the variability explained by  model (MST) with the residual variability (MSE)

or

- Variability between groups (MST) to variability within groups (MSE)
\vspace{10pt}
- Under $H_0$: $F \sim F_{g-1,n-g}$, with g=3.


## Anova Table

| |Df|Sum Sq|Mean Sq|F value|Pr(>F)|
|---|---|---|---|---|---|
|Treatment|d.f. SST|SST|MST|F-statistiek|p-waarde|
|Error|d.f. SSE|SSE|MSE| | |

```r
anova(model1)
```


### F-distribution with critical value  ($\alpha$=5%) and observed F-statistic for prostacyclin example
```r
grid <- seq(0,17,.01)
df1=anova(model1)[1,1]
df2=anova(model1)[2,1]
fval=anova(model1)[1,4]
crit=qf(0.95,df1,df2)
reject=c(crit,grid[which(grid>crit)])
accept=c(grid[which(grid<crit)],crit)
plot(grid,df(grid,df1,df2),type="l",ylab="Density",xlab="F-statistic",cex.axis=1.5,cex.lab=1.5)
polygon(c(0,accept,crit,0),c(0,df(accept,df1,df2),0,0),col="blue",border="blue")
text(crit/2,.97,labels="accept\n95%",col="blue",cex=1.5)
polygon(c(crit,reject,15,crit),c(0,df(reject,df1,df2),0,0),col="red",border="red")
abline(v=crit,col="red",lwd=2)
text(crit+(fval-crit)/2,.97,labels="reject\n5%",col="red",cex=1.5)
text(pos=4,crit,df(crit,2,33),labels=paste0("F(0.05,",df1,",",df2,")"),col="red",cex=1.5)
text(pos=4,fval,df(crit,df1,df2),labels=paste0("f=",round(fval,1)),col="darkorange",cex=1.5)
abline(v=fval,col="darkorange",lwd=2,lty=2)
text(15.5,.97,labels=paste0("p-value\n",format(anova(model1)[1,5],digits=2)),col="darkorange",cex=1.5)
arrows(x0=17.5,x1=fval,y0=.9,y1=.9,col="darkorange")
```


### F-distributions with different number of degrees of freedom in the nominator and denominator
```r
plot(grid,df(grid,1,5),type="l",ylab="Density",xlab="F-statistic",xlim=c(0,5),ylim=c(0,1.5),lwd=2,cex.axis=1.5,cex.lab=1.5)
lines(grid,df(grid,5,5),type="l",col=2,lwd=2)
lines(grid,df(grid,10,30),type="l",col=3,lwd=2)
lines(grid,df(grid,20,30),type="l",col=4,lwd=2)
lines(grid,df(grid,50,50),type="l",col=5,lwd=2)
legend("topright",lty=1,col=c(1,2,3,4,5),legend=c("F(1,5)","F(5,5)","F(10,30)","F(20,30)","F(50,50)"),lwd=2,cex=1.5)
```

###Prostacyclin example: which groups are different?

```r
summary(model1)
```

With model output we can assess if the mean prostacyclin concentration differs between middle and low dose group ($\beta_1$: dose25), and, between high and low dose group ($\beta_2$: dose50).

The p-values do not account for multiple testing.

---

[← Analyse of Variance](02-analyse-of-variance.md) · [Up: contents](index.md) · [Post hoc analysis: Multiple comparisons of means →](04-post-hoc-analysis-multiple-comparisons-of-means.md)
