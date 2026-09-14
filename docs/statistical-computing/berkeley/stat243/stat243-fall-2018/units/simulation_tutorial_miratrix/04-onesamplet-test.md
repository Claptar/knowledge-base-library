---
title: OneSamplet-test
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# OneSamplet-test

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##
##data:dat
##t=7.7336,df=9,p-value=2.898e-05
##alternativehypothesis:truemeanisnotequalto0
##95percentconfidenceinterval:
##1.8084563.303855
##sampleestimates:
##meanofx
##2.556156
#evaluatetheresults
findInterval(3,tt$conf.int)==1
```

##### `## [1] TRUE`

The above shows the canonical form of a single simulation trial: make the data, analyze the data, decide how well we did.

2

Now let’s look at coverage by doing the above many, many times and seeing how often we capture the true parameter:

```
rps=replicate(1000,{
dat=rnorm(10)
tt=t.test(dat)
findInterval(0,tt$conf.int)
})
table(rps)
##rps
##012
##2195326
mean(rps==1)
```

```
##[1]0.953
```

We got about 95% coverage, which is good news. We can also assess _simulation uncertainty_ by recognizing that our simulation results are an i.i.d. sample of the infinite possible simulation runs. We analyze this sample to see a range for our true coverage.

```
hits=as.numeric(rps==1)
prop.test(sum(hits),length(hits),p=0.95)
```

```

---

[← OneSamplet-test](03-onesamplet-test.md) · [Up: contents](index.md) · [1-sampleproportionstestwithcontinuitycorrection →](05-1-sampleproportionstestwithcontinuitycorrection.md)
