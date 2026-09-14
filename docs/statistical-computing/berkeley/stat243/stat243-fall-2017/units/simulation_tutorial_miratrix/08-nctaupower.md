---
title: nCtaupower
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# nCtaupower

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##<dbl><fctr><dbl>
##1200.2031667
##220.50.2406667
##3210.3228333
```

11

```
##4400.1153333
```

```
##540.50.1766667
##6410.3255000
```

```
ggplot(exp.res.sum,aes(x=nC,y=power,group=tau,col=tau))+
geom_line()+geom_point()+
scale_x_log10(breaks=nC)+
geom_hline(yintercept=0.05,col="black",lty=2)
```


<!-- Start of picture text -->
0.6<br>tau<br>0.4 0<br>0.5<br>1<br>0.2<br>2 4 7 10 50 500<br>nC<br>power<br><!-- End of picture text -->

We can try to get clever and look at other aspects of our experimental runs. The above suggests that the smaller of the two groups is dictating things going awry, in terms of elevated rejection rates under the null. We can also look at things in terms of some other more easily interpretable parameter (here we switch to effect size instead of raw treatment effect).

Given this, we might decide to look at total sample size or the smaller of the two groups sample size and make plots that way (we are also subsetting to just the `sd=1` cases as there is nothing interesting in both, really):

```
exp.res<-exp.res%>%mutate(n=nC+nT,
```

```
n.min=pmin(nC,nT))
```

```
ggplot(filter(exp.res,sd==1),aes(x=n,y=power,group=ES,col=ES))+
geom_jitter(width=0.05,height=0)+
geom_smooth(se=FALSE)+
scale_x_log10()+
geom_hline(yintercept=0.05,col="black",lty=2)
```

12


<!-- Start of picture text -->
1.00<br>0.75<br>ES<br>0<br>0.50 0.5<br>1<br>0.25<br>0.00<br>10 100 1000<br>n<br>power<br><!-- End of picture text -->

```
ggplot(filter(exp.res,sd==1),aes(x=n.min,y=power,group=ES,col=ES))+
geom_jitter(width=0.05,height=0)+
geom_smooth(se=FALSE)+
scale_x_log10()+
```

```
geom_hline(yintercept=0.05,col="black",lty=2)
```


<!-- Start of picture text -->
1.25<br>1.00<br>ES<br>0.75<br>0<br>0.5<br>0.50<br>1<br>0.25<br>0.00<br>10 100<br>n.min<br>power<br><!-- End of picture text -->

Note the few observations out in the high `n.min` region for the second plot—this plot is a bit strange in that the different levels along the x-axis are assymetric with respect to each other. It is not balanced.

#### **Addendum: Saving more details**

Our `exp.res` dataframe from above has all our simulations, one simulation per row, with our measured outcomes. This is ideally all we need to analyze.

That being said, sometimes we might want to use a lot of disk space and keep much more. In particular, each row of `exp.res` corresponds to the summary of a whole collection of individual runs. We might instead store all of these runs.

To do this we just take the summarizing step out of our `run.experiment()`

13

```
run.experiment.raw=function(nC,nT,sd,tau,mu=5,R=500){
eres=plyr::rdply(R,run.one(nC,nT,sd,tau,mu))
eres<-mutate(eres,nC=nC,nT=nT,sd=sd,tau=tau,mu=mu,R=R)
eres
}
```

Each call to `run.experiment.raw()` gives one row per run. We replicate our simulation parameters for each row.

```
run.experiment.raw(10,3,1,0.5,R=4)
```

|`##`|`.n`|`tau.hat`|`ES`|`SE.hat`|`z`|`p.value `|`nC nT sd`|`tau `|`mu R`|
|---|---|---|---|---|---|---|---|---|---|
|`## 1`|`1 `|`-0.450945068 `|`0.5 `|`0.5721977 `|`-0.7880931360 `|`0.43064223 `|`10`<br>`3`<br>`1`|`0.5`|`5 4`|
|`## 2`|`2`|`0.000324705 `|`0.5 `|`0.3887987`|`0.0008351493 `|`0.99933365 `|`10`<br>`3`<br>`1`|`0.5`|`5 4`|
|`## 3`|`3`|`0.978188814 `|`0.5 `|`0.5914475`|`1.6538895212 `|`0.09814996 `|`10`<br>`3`<br>`1`|`0.5`|`5 4`|
|`## 4`|`4`|`0.138354391 `|`0.5 `|`0.6345716`|`0.2180280170 `|`0.82740728 `|`10`<br>`3`<br>`1`|`0.5`|`5 4`|


The advantage of this is we can then generate new outcome measures, as they occur to us, later on. The disadvantage is this result file will be _R_ times as many rows as the older file, which can get quite, quite large.

But disk space is cheap! Here we run the same experiment with our more complete storage. Note how the `pmap_df` stacks the multiple rows from each run, giving us everything nicely bundled up:

```
exp.res.full<-experiments%>%pmap_df(run.experiment.raw,R=500)
head(exp.res.full)
```

```
##.ntau.hatESSE.hatzp.valuenCnTsdtaumuR
##11-2.119972400.7128445-2.97396220.00293981322105500
##22-0.435502001.1252865-0.38701440.69874557022105500
##33-0.998496300.6073760-1.64395080.10018637222105500
##440.366888700.48235160.76062510.44688105022105500
##55-0.121320300.2667031-0.45488880.64918922622105500
##66-0.786155500.6349178-1.23820040.21564175622105500
```

We end up with a lot more rows:

```
nrow(exp.res.full)
```

```
##[1]108000
nrow(exp.res)
```

```
##[1]216
```

We next save our results:

```
write_csv(exp.res.full,"simulation_results_full.csv")
```

Compare the file sizes: one is several k, the other is around 12 megabytes.

```
file.size("simulation_results.csv")/1024
```

```
##[1]16.06738
```

```
file.size("simulation_results_full.csv")/1024
```

```
##[1]11860.98
```

14

##### **Getting results ready for analysis**

If we generated raw results then we need to collapse them by experimental run before analyzing our results so we can explore the trends across the experiments. We do this by borrowing the summarise code from inside `run.experiment()` :

```
exp.res.sum<-exp.res.full%>%
group_by(nC,nT,sd,tau,mu)%>%
summarise(R=n(),
E.tau.hat=mean(tau.hat),
SE=sd(tau.hat),
E.SE.hat=mean(SE.hat),
ES=mean(ES),
power=mean(p.value<=0.05))
```

Note how I added an extra estimation of the true _SE_ , just because I could! This is an easier fix, sometimes, than running all the simulations again after changing the `run.experiment()` method.

The results of summarizing during the simulation vs. after as we just did leads to the same place, however, although the order of rows in our final dataset are different (and we have a tibble instead of a data.frame, a consequence of using the `tidyverse` , but this is not something to worry about):

```
head(exp.res.sum)
```

|`## `|`Source: `|`local `|`data `|`frame `|`[6 x 11`|`]`||||
|---|---|---|---|---|---|---|---|---|---|
|`## `|`Groups: `|`nC, n`|`T, sd, `|`tau [`|`6]`|||||
|`##`||||||||||
|`##`|`nC`|`nT`|`sd`|`tau`|`mu`|`R`|`E.tau.hat`|`SE`|`E.SE.hat`|
|`##`|`<dbl> `|`<dbl> `|`<dbl> `|`<dbl> `|`<dbl> `|`<int>`|`<dbl>`|`<dbl>`|`<dbl>`|
|`## `|`1`<br>`2`|`2`|`1`|`0.0`|`5`|`500`|`0.0235374919 `|`1.0419384 `|`0.8832385`|
|`## `|`2`<br>`2`|`2`|`1`|`0.5`|`5`|`500`|`0.5097628502 `|`0.9924804 `|`0.8962110`|
|`## `|`3`<br>`2`|`2`|`1`|`1.0`|`5`|`500`|`1.0314230696 `|`0.9998192 `|`0.8840027`|
|`## `|`4`<br>`2`|`2`|`2`|`0.0`|`5`|`500 `|`-0.0001394172 `|`2.0251479 `|`1.8025675`|
|`## `|`5`<br>`2`|`2`|`2`|`0.5`|`5`|`500`|`0.5423638414 `|`2.0436671 `|`1.8226802`|
|`## `|`6`<br>`2`|`2`|`2`|`1.0`|`5`|`500`|`1.0222488645 `|`1.9164870 `|`1.7779536`|
|`## `|`# ... w`|`ith 2 `|`more v`|`ariabl`|`es: ES `|`<dbl>,`|`power <dbl>`|||


```
nrow(exp.res.sum)
```

```
##[1]216
nrow(exp.res)
```

```
##[1]216
```

---

[← Simulation 2: The Power and Validity of Neyman’s ATE Estimate](07-simulation-2-the-power-and-validity-of-neyman-s-ate-estimate.md) · [Up: contents](index.md) · [Simulation 3: Comparing Estimators for the Mean via Simulation →](09-simulation-3-comparing-estimators-for-the-mean-via-simulatio.md)
