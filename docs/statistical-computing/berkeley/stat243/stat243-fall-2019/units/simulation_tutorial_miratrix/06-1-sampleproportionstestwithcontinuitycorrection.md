---
title: 1-sampleproportionstestwithcontinuitycorrection
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1-sampleproportionstestwithcontinuitycorrection

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##
##data:sum(hits)outoflength(hits),nullprobability0.5
##X-squared=635.21,df=1,p-value<2.2e-16
##alternativehypothesis:truepisnotequalto0.5
##95percentconfidenceinterval:
##0.87823160.9166333
##sampleestimates:
##p
##0.899
```

Our coverage is _too low_ . Our _t_ -test based confidence interval is missing the true value (1) more than it should.

Finally, we want to examine how the coverage changes as the sample size varies. So let’s do a one-factor experiment, with the factor being sample size. I.e., we will conduct the above simulation for a variety of sample sizes and see how coverage changes.

We first make a function, wrapping up our _specific, single-scenario_ simulation into a bundle so we can call it under a variety of different scenarios.

```
run.experiment=function(n){
rps=replicate(10000,{
dat=rexp(n)
tt=t.test(dat)
findInterval(1,tt$conf.int)
})
mean(rps==1)
}
```

Now we run `run.experiment` for different _n_ . We do this with `map_dbl()` , which takes a list and calls a function for each value in the list (See R for DS, Chapter 21.5).

```
ns=c(5,10,20,40,80,160,320,740)
cover=map_dbl(ns,run.experiment)
```

Make a data.frame of our results and plot:

```
res=data.frame(n=ns,coverage=cover)
ggplot(res,aes(x=n,y=100*coverage))+
geom_line()+geom_point(size=4)+
geom_hline(yintercept=95,col="red")+
scale_x_log10(breaks=ns)+
labs(title="Coverageratesfort-testonexponentialdata",
x="n(samplesize)",y="coverage(%)")
```

4

### Coverage rates for t−test on exponential data


<!-- Start of picture text -->
94<br>92<br>90<br>88<br>5 10 20 40 80 160 320 740<br>n (sample size)<br>coverage (%)<br><!-- End of picture text -->

Note the plot is on a log scale for the x-axis.

So far we have done a very simple simulation to assess how well a statistical method works in a given circumstance. We have run a single factor experiment, systematically varying the sample size to examine how the behavior of our estimator changes. In this case, we find that coverage is poor for small sample sizes, and still a bit low for higher sample sizes is well. The overall framework is to repeatidly do the following:

- Generate data according to some decided upon data generation process (DGP). This is our model.

- Analyze data according to some other process (and possibly some other assumed model).

- Assess whether the analysis “worked” by some measure of working (such as coverage).

We next extend this general simulation framework to look at how to very multiple things at once. This is called a multifactor experiment.

---

[← 1-sampleproportionstestwithcontinuitycorrection](05-1-sampleproportionstestwithcontinuitycorrection.md) · [Up: contents](index.md) · [Simulation 2: The Power and Validity of Neyman’s ATE Estimate →](07-simulation-2-the-power-and-validity-of-neyman-s-ate-estimate.md)
