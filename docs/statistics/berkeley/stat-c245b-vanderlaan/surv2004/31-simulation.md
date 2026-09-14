---
title: Simulation
source: https://vanderlaan-lab.org/teach-files/surv2004.pdf
source_file: sources/berkeley-stat-c245b-vanderlaan/surv2004.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Simulation

**Source:** [`surv2004.pdf`](https://vanderlaan-lab.org/teach-files/surv2004.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Below is simulation with:

1. Analysis time fixed at 8 months

2. AIDS dx is exponential, _λ_ = 0 _._ 25

37

3. Covariate, _X ∼ U_ (0 _,_ 1)

4. Death, _T_ = _exp_ ( _X_ + _e_ ), _e ∼ N_ (0 _,_ 0 _._ 5)

5. _V_ = _T_ + _U_ , _U ∼_ exponential, _λ_ = 0 _._ 5

**Code used to simulate data**

```
x<-runif(1000,0,1)
T<-exp(x+rnorm(1000,0,0.5))
V<-T+pmin(rexp(1000,2),0.5)
cc<-rexp(1000,rate=1/4)
CC<-ta-cc
#Getridofpeoplewhosedxis>analysistime
x<-x[CC>0]
V<-V[CC>0]
T<-T[CC>0]
CC<-CC[CC>0]
ttilde<-pmin(V,CC)
censor<-as.numeric(V<CC)
invcens<-1-censor
```

**Code used to analyze simulated data**

```
##SurvivalTime
surv.cens<-survfit(Surv(ttilde,invcens)~1)
```

```
##Get1-Gn(V)
cens.prob<-get.at.surv.times(surv.cens,ttilde)
##Makeweights
cwts<-censor/cens.prob
```

```
##LinearregressionoflogTonx
logt<-log(T)
init.lm<-lm(logt~x,weights=cwts)
```

**Function to get censoring survival distribution at all** `get.at.surv.times<-function(surv.cens, times) { # # surv.cens is an object created by survfit # times is a vector of times at which you want # an estimate of the survival function # nt <- length(times) outs <- rep(0, nt) survv <- summary(surv.cens)$surv ns <- length(survv) timev <- summary(surv.cens)$time`

38

```
for(iin1:nt){
if(times[i]<timev[1]){
outs[i]<-1
}
elseif(times[i]>=timev[ns]){
outs[i]<-survv[ns]
}
else{
outs[i]<-survv[timev==max(timev[timev<=times[i]])][1]
}
}
no<-length(outs[outs==0])
outs[outs==0]<-rep(survv[ns-1],no)
return(outs)
}
```

Lecture notes for March 10, 2004 Hideaki Nakamura hideakin demog.berkeley.edu

---

[← Weighted Regression](30-weighted-regression.md) · [Up: contents](index.md) · [2 Functional Derivative →](32-2-functional-derivative.md)
