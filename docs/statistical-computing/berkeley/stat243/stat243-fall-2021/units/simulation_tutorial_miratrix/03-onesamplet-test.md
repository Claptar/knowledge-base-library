---
title: OneSamplet-test
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/simulation_tutorial_miratrix.pdf
licence: CC0-1.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# OneSamplet-test

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/simulation_tutorial_miratrix.pdf) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##
##data:dat
##t=10.134,df=9,p-value=3.202e-06
##alternativehypothesis:truemeanisnotequalto0
```

1

```
##95percentconfidenceinterval:
##2.2088743.478401
##sampleestimates:
##meanofx
##2.843637
#examinetheresults
tt$conf.int
```

```
##[1]2.2088743.478401
##attr(,"conf.level")
##[1]0.95
```

For us, we have a true mean of 3. Did we capture it? To find out, we use `findInterval()` **<mark>`findInterval`</mark>** <mark>`( 3, tt$conf.int )`</mark>

```
##[1]1
```

`findInterval()` checks to see where the first number lies relative to the range given in the second argument. E.g., **<mark>`findInterval`</mark>** <mark>`( 1,`</mark> **<mark>`c`</mark>** <mark>`(20, 30) )`</mark>

```
##[1]0
findInterval(25,c(20,30))
```

```
##[1]1
findInterval(40,c(20,30))
```

```
##[1]2
```

So, for us, `findInterval == 1` means we got it! Packaging the above gives us the following code:

```
#makefakedata
dat=rnorm(10,mean=3,sd=1)
#conductthetest
tt=t.test(dat)
tt

---

[← Simulation 1: the performance of the t -test](02-simulation-1-the-performance-of-the-t--test.md) · [Up: contents](index.md) · [OneSamplet-test →](04-onesamplet-test.md)
