---
title: Histogram of Y
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Histogram of Y

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

<!-- Start of picture text -->
−40 −20 0 20 40 60<br>0.12<br>0.08<br>Density<br>0.04<br>0.00<br><!-- End of picture text -->

#### Y

We steal the code from above, modifying it slightly for our new function and changing our target parameter from 0 to 1:

```
one.run.exp=function(n){
raw.exps<-plyr::rdply(1000,{
dt=gen.dat(n=n)
analyze.data(dt)
})
```

```
rs<-plyr::ldply(raw.exps[-1],estimator.quality,mu=1,.id="estimator")
rs
}
```

21

`res =` **`one.run.exp`** `( 100 ) res ## estimator RMSE bias SE ## 1 mean 0.3389645 0.003745985 0.3391134 ## 2 trim.mean 0.4524438 -0.437268725 0.1162540 ## 3 median 0.4730820 -0.454916015 0.1299032` And for our experiment we vary the sample size

```
ns=c(10,20,40,80,160,320)
lvls=tibble(n=ns)
```

```
results<-lvls%>%mutate(results=pmap(lvls,one.run.exp))%>%unnest()
head(results)
```

```
###Atibble:6×5
##nestimatorRMSEbiasSE
##<dbl><fctr><dbl><dbl><dbl>
##110mean0.6653075-0.0491178970.6638239
##210trim.mean0.5743417-0.2940332340.4936158
##310median0.5687996-0.3828822830.4208459
##420mean0.4898701-0.0071841890.4900626
##520trim.mean0.4493510-0.3005962300.3341704
##620median0.4888145-0.3871054530.2986271
```

Here we are going to plug multiple outcomes. Often with the simulation study we are interested in different measures of performance. For us, we want to know the standard error, bias, and overall error (RMSE). To plot this we first gather our outcomes to make a long form dataframe of results:

```
res2=gather(results,RMSE,bias,SE,key="Measure",value="value")
res2=mutate(res2,Measure=factor(Measure,levels=c("SE","bias","RMSE")))
```

And then we plot, making a facet for each outcome of interest:

```
ggplot(res2,aes(x=n,y=value,col=estimator))+
facet_grid(.~Measure)+
geom_hline(yintercept=0,col="darkgrey")+
geom_line()+geom_point()+
scale_x_log10(breaks=ns)+
labs(y="")
```

22


<!-- Start of picture text -->
SE bias RMSE<br>0.50<br>estimator<br>0.25<br>mean<br>trim.mean<br>median<br>0.00<br>−0.25<br>10 20 40 80 160 320 10 20 40 80 160 320 10 20 40 80 160 320<br>n<br><!-- End of picture text -->

We see how different estimators have different biases and different uncertainties. The bias is negative for our trimmed estimators because we are losing the big outliers above and so getting answers that are too low.

The RMSE captures the trade-off in terms of what estimator gives the lowest overall _error_ . For this distribution, the mean wins as the sample size increases because the bias basically stays the same and the SE drops. But for smaller samples the trimming is superior. The median (essentially trimming 50% above and below) is overkill and has too much negative bias.

From a simulation study point of view, notice how we are looking at three different qualities of our estimators. Some people really care about bias, some care about RMSE. By presenting all results we are transparent about how the different estimators operate.

Next steps would be to also examine the associated estimated standard errors for the estimators, seeing if these estimates of estimator uncertainty are good or poor. This leads to investigation of coverage rates and similar.

23

---

[← Extension: The Bias-variance tradeoff](10-extension-the-bias-variance-tradeoff.md) · [Up: contents](index.md)
