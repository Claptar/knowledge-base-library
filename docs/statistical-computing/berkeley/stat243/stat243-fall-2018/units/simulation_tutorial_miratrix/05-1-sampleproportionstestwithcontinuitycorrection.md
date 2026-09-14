---
title: 1-sampleproportionstestwithcontinuitycorrection
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1-sampleproportionstestwithcontinuitycorrection

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##
##data:sum(hits)outoflength(hits),nullprobability0.95
##X-squared=0.13158,df=1,p-value=0.7168
##alternativehypothesis:truepisnotequalto0.95
##95percentconfidenceinterval:
##0.93749680.9649054
##sampleestimates:
##p
##0.953
```

We have no evidence that our coverage is not what it should be: 95%.

Things working out should hardly be surprising. The _t_ -test is designed for normal data and we generated normal data. In other words, our test is following theory when we meet our assumptions. Now let’s look at an exponential distribution to see what happens when we don’t have normally distributed data. We are simulating to see what happens when we voilate our assumptions behind the _t_ -test. Here, the true mean is 1 (the mean of a standard exponential is 1).

```
rps=replicate(1000,{
dat=rexp(10)
tt=t.test(dat)
findInterval(1,tt$conf.int)
})
table(rps)
```

```
##rps
##012
##689995
```

Our interval is often entirely too low and very rarely does our interval miss because it is entirely too high. Furthermore, our average coverage is not 95% as it should be:

3

```
mean(rps==1)
```

```
##[1]0.899
```

Again, to take simulation uncertainty into account we do a proportion test. Here we have a confidence interval of our true coverage under our model misspecification:

```
hits=as.numeric(rps==1)
prop.test(sum(hits),length(hits))
```

```

---

[← OneSamplet-test](04-onesamplet-test.md) · [Up: contents](index.md) · [1-sampleproportionstestwithcontinuitycorrection →](06-1-sampleproportionstestwithcontinuitycorrection.md)
