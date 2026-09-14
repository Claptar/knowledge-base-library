---
title: 'Extension: The Bias-variance tradeoff'
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/simulation_tutorial_miratrix.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Extension: The Bias-variance tradeoff

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/simulation_tutorial_miratrix.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We can use the above simulation to examine these same estimators when we the median is not the same as the mean. Say we want the mean of a distribution, but have systematic outliers. If we just use the median, or trimmed mean, we might have bias if the outliers tend to be on one side or another. For example, consider the exponential distribution:

```
nums=rexp(100000)
mean(nums)
```

```
##[1]0.99737
```

```
mean(nums,trim=0.1)
```

```
##[1]0.8283047
```

```
median(nums)
```

```
##[1]0.6905491
```

Our trimming, etc., is _biased_ if we think of our goal as estimating the mean. But if the trimmed estimators are much more stable, we might still wish to use them. Let’s find out.

20

Let’s generate a mixture distribution, just for fun. It will have a nice normal base with some extreme outliers. We will make sure the overall mean, including the outliers, is always 1, however. (So our target, _µ_ is now 1, not 0.)

```
gen.dat=function(n,prob.outlier=0.05){
nN=rbinom(1,n,prob.outlier)
nrm=rnorm(n-nN,mean=0.5,sd=1)
outmean=(1-(1-prob.outlier)/2)/prob.outlier
outs=rnorm(nN,mean=outmean,sd=10)
c(nrm,outs)
}
```

Let’s look at our distribution

```
Y=gen.dat(10000000,prob.outlier=0.05)
mean(Y)
```

```
##[1]0.9999024
sd(Y)
```

```
##[1]3.270383
hist(Y,breaks=30,col="grey",prob=TRUE)
```

---

[← Simulation 3: Comparing Estimators for the Mean via Simulation](09-simulation-3-comparing-estimators-for-the-mean-via-simulatio.md) · [Up: contents](index.md) · [Histogram of Y →](11-histogram-of-y.md)
