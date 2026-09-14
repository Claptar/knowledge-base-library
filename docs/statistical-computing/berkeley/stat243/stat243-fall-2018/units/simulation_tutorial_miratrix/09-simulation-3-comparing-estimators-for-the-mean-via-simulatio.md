---
title: 'Simulation 3: Comparing Estimators for the Mean via Simulation'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Simulation 3: Comparing Estimators for the Mean via Simulation

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The above ideas readily extend to when we wish to compare different forms of estimator for estimating the same thing. We still generate data, evaluate it, and see how well our evaluation works. The difference is we now evaluate it multiple ways, storing how the different ways work.

For our simple working example we are going to compare estimation of the center of a symmetric distribution via mean, trimmed mean, and median (so the mean and median are the same).

We are going to break this down into lots of functions to show the general framework. This framework can readily be extended to more complicated simulation studies.

15

For our data-generation function we will use the scaled _t_ -distribution so the standard deviation will always be 1 but we will have different fatness of tails (high chance of outliers):

```
gen.data=function(n,df0){
rt(n,df=df0)/sqrt(df0/(df0-2))
}
```

The variance of a _t_ is _df/_ ( _df −_ 2), so if we divide our observations by the square root of this, we will standardize them so they have unit variance. See, the standard deviation is 1 (up to random error, and as long as df0 > 2)!:

```
sd(gen.data(100000,df0=3))
```

```
##[1]0.9934177
```

We next define the parameter we want (this, the mean, is what we are trying to estimate):

```
mu=0
```

Our analysis methods bundled in a function. We return a vector of the three estimates:

```
analyze.data=function(data){
mn=mean(data)
md=median(data)
mn.tr=mean(data,trim=0.1)
data.frame(mean=mn,trim.mean=mn.tr,median=md)
}
```

Let’s test:

```
dt=gen.data(100,3)
analyze.data(dt)
```

```
##meantrim.meanmedian
##1-0.044964130.00089061630.05742946
```

To evaluate, do a bunch of times, and assess results. Let’s start by looking at a specific case. We generate 1000 datasets of size 10, and estimate the center using our three different estimators.

```
raw.exps<-plyr::rdply(1000,{
dt=gen.data(n=10,df0=5)
analyze.data(dt)
```

```
})
```

We now have 1000 estimates for each of our estimators:

```
head(raw.exps)
```

```
##.nmeantrim.meanmedian
##110.171120570.340049000.52930650
##220.418439410.366298050.37020937
##330.153376500.03130291-0.06930059
##44-0.33214689-0.24003774-0.19326752
##55-0.027753660.062705540.04614414
##66-0.20154089-0.13609502-0.10153322
```

We then want to assess estimator performance for each estimator. We first write a function to calculate what we want from 1000 estimates:

```
estimator.quality=function(estimates,mu){
RMSE=sqrt(mean((estimates-mu)^2))
bias=mean(estimates-mu)
```

16

```
c(RMSE=RMSE,bias=bias,SE=sd(estimates))
}
```

```
estimator.quality(raw.exps$mean,mu)
```

```
##RMSEbiasSE
##0.3171771760.0066251130.317266650
```

We now borrow another oldie-but-goodie from the `plyr` package. The function `ldply` is a transforming function that takes a list ( `l` ) and for everything in the list calls a given function. It packs up the results as a dataframe ( `d` ). For the record, `llply` would return everything as a list, `ddply` would take a dataframe and return a dataframe, and so forth. For us, `raw.exps[-1]` is a list of vectors, i.e., all the columns (except the first) of our dataframe of simulations. (Remember that a dataframe is a list of the variables in the dataframe.)

```
plyr::ldply(raw.exps[-1],estimator.quality,mu=mu,.id="estimator")
```

```
##estimatorRMSEbiasSE
##1mean0.31717720.0066251130.3172666
##2trim.mean0.29396710.0045844750.2940784
##3median0.31295170.0061460370.3130479
```

Note the `mu = 0` line after estimator.quality. We can pass extra arguments to the function by putting them after the function name. The function will take as its first argument the elements from the `raw.exps[-1]` list.

Aside: There is probably a nice way to do this in the `dplyr` package, but I don’t know what it is.

To continue, we pack up the above into a function, as usual. Our function takes our two parameters of sample size and degrees of freedom, and returns a data frame of results.

```
one.run=function(n,df0){
raw.exps<-plyr::rdply(1000,{
dt=gen.data(n=n,df0=df0)
analyze.data(dt)
})
rs<-plyr::ldply(raw.exps[-1],estimator.quality,mu=0,.id="estimator")
rs
}
```

Our function will take our two parameters, run a simulation, and give us the results. We see here that none of our estimators are particularly biased and the trimmed mean has, possibly, the smallest RMSE, although it is a close call.

```
one.run(10,5)
```

```
##estimatorRMSEbiasSE
##1mean0.3178515-0.0056413350.3179605
##2trim.mean0.2948322-0.0066893400.2949038
##3median0.3240756-0.0202178140.3236062
```

Ok, now we want to see how sample size impacts our different estimators. If we also vary degrees of freedom we have a _three_ -factor experiment, where one of the factors is our estimator itself. We are going to use a new clever trick. As before, we use `pmap()` , but now we store the entire dataframe of results we get back from our function in a new column of our original dataframe. See R for DS, Chapter 25.3. This trick works best if we have everything as a `tibble` which is basically a dataframe that prints a lot nicer and doesn’t try to second-guess what you are up to all the time.

17

```
ns=c(10,50,250,1250)
dfs=c(3,5,15,30)
lvls=expand.grid(n=ns,df=dfs)
```

```
#Soitstoresourdataframeresultsinourlvlsdataproperly.
lvls=as_tibble(lvls)
```

```
results<-lvls%>%mutate(results=pmap(lvls,one.run))
```

We have stored our results (a bunch of dataframes) in our main matrix of simulation runs. **<mark>`head`</mark>** <mark>`( results )`</mark>

```
###Atibble:6×3
##ndfresults
##<dbl><dbl><list>
##1103<data.frame[3×4]>
##2503<data.frame[3×4]>
##32503<data.frame[3×4]>
##412503<data.frame[3×4]>
##5105<data.frame[3×4]>
##6505<data.frame[3×4]>
```

The unnest() function will unpack our dataframes and put everything together, all nice like. See (hard to read) R for DS Chapter 25.4.

```
results<-unnest(results)
results
```

```
###Atibble:48×6
##ndfestimatorRMSEbiasSE
##<dbl><dbl><fctr><dbl><dbl><dbl>
##1103mean0.29688802-0.00681601510.29695829
##2103trim.mean0.239194640.00080887180.23931296
##3103median0.24581301-0.00080596860.24593469
##4503mean0.138568620.00550256540.13852860
##5503trim.mean0.104604560.00291926290.10461614
##6503median0.10989340-0.00146697350.10993859
##72503mean0.06169849-0.00071360530.06172523
##82503trim.mean0.04682161-0.00068399940.04684004
##92503median0.04958600-0.00074642790.04960519
##1012503mean0.02795388-0.00040267230.02796496
###...with38morerows
```

And plot:

```
ggplot(results,aes(x=n,y=RMSE,col=estimator))+
facet_wrap(~df,nrow=1)+
geom_line()+geom_point()+
scale_x_log10(breaks=ns)
```

18


<!-- Start of picture text -->
3 5 15 30<br>0.3<br>estimator<br>mean<br>0.2<br>trim.mean<br>median<br>0.1<br>10 50 250 125010 50 250 125010 50 250 125010 50 250 1250<br>n<br>RMSE<br><!-- End of picture text -->

The above doesn’t show differences clearly because all the RMSE goes to zero. It helps to log our outcome, or otherwise rescale. The logging version shows differences are relatively constant given changing sample size. **`ggplot`** `( results,` **`aes`** `(x=n, y=RMSE, col=estimator) ) +` **`facet_wrap`** `( ~ df, nrow=1 ) +` **`geom_line`** `() +` **`geom_point`** `() +` **`scale_x_log10`** `( breaks=ns ) +` **`scale_y_log10`** `()`


<!-- Start of picture text -->
3 5 15 30<br>estimator<br>0.1 mean<br>trim.mean<br>median<br>10 50 250 125010 50 250 125010 50 250 125010 50 250 1250<br>n<br>RMSE<br><!-- End of picture text -->

Better is to rescale using our knowledge of standard errors. If we scale by the square root of sample size, we should get horizontal lines. We now clearly see the trends.

```
results<-mutate(results,scaleRMSE=RMSE*sqrt(n))
```

```
ggplot(results,aes(x=n,y=scaleRMSE,col=estimator))+
facet_wrap(~df,nrow=1)+
geom_line()+geom_point()+
scale_x_log10(breaks=ns)
```

19


<!-- Start of picture text -->
3 5 15 30<br>1.2<br>1.1<br>estimator<br>1.0 mean<br>trim.mean<br>0.9 median<br>0.8<br>10 50 250 125010 50 250 125010 50 250 125010 50 250 1250<br>n<br>scaleRMSE<br><!-- End of picture text -->

Overall, we see the scaled error of the mean it is stable across the different distributions. The trimmed mean is a real advantage when the degrees of freedom are small. We are cropping outliers that destabilize our estimate which leads to great wins. As the distribution grows more normal, this is no longer an advantage and we get closer to the mean in terms of performance. Here we are penalized slightly bye having dropped 10% of our data, so the standard errors will be slightly larger.

The median is not able to take advantage of the nuances of a data set because it is entirely determined by the middle value. When outliers cause real concern, this cost is minimal. When outliers are not a concern, the median is just worse.

Overall, the trimmed mean seems an excellent choice: in the presence of outliers it is far more stable than the mean, and when there are no outliers the cost of using it is small.

In terms of thinking about designing simulation studies, we see clear visual displays of simulation results can tell very clear stories. Eschew complicated tables with lots of numbers.

---

[← nCtaupower](08-nctaupower.md) · [Up: contents](index.md) · [Extension: The Bias-variance tradeoff →](10-extension-the-bias-variance-tradeoff.md)
