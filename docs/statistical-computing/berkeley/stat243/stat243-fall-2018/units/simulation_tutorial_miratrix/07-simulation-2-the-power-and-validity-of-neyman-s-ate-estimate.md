---
title: 'Simulation 2: The Power and Validity of Neyman’s ATE Estimate'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/simulation_tutorial_miratrix.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Simulation 2: The Power and Validity of Neyman’s ATE Estimate

**Source:** [`units/simulation_tutorial_miratrix.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/simulation_tutorial_miratrix.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The way to build a simulation experiment is to first write code to run a specific simulation for a specific scenario. Once that is working, we will re-use the code to systematically explore a variety of scenarios so we can see how things change as scenario changes. Next I would build up this system.

For our running example we are going to look at a randomized experiment. We will assume the treatment and control groups are normally distributed with two different means. We will generate a random data set, estimate the treatment effect by taking the difference in means and calculating the associated standard error, and generating a _p_ -value using the normal approximation. (As we will see, this is not a good idea for small sample size since we should be using a _t_ -test style approach.)

#### **Step 1: Write a function for a specific simulation given specific parameters.**

Our function will generate two groups of the given sizes, one treatment and one control, and then calculate the difference in means. It will then test this difference using the normal approximation.

5

The function also calculates and returns the effect size as the treatment effect divided by the control standard deviation (useful for understanding power, shown later on).

```
run.one=function(nC,nT,sd,tau,mu=5){
Y0=mu+rnorm(nC,sd=sd)
Y1=mu+tau+rnorm(nT,sd=sd)
tau.hat=mean(Y1)-mean(Y0)
SE.hat=sqrt(var(Y0)/(nC)+var(Y1)/(nT))
z=tau.hat/SE.hat
pv=2*(1-pnorm(abs(z)))
c(tau.hat=tau.hat,ES=tau/sd,SE.hat=SE.hat,z=z,p.value=pv)
}
```

A single run will generate a data set, analyze it, and give us back a variety of results as a list.

```
run.one(nT=5,nC=10,sd=1,tau=0.5)
```

```
##tau.hatESSE.hatzp.value
##0.34115430.50000000.55520000.61447090.5389042
```

##### **Running our single trial more than once**

The following code borrows a useful function from the older plyr package (you may need to install it). It is a version of `replicate()` that runs a chunk of code a given number of times. The difference is that `rdply` returns everything as a data frame! Sweet!

```
eres<-plyr::rdply(500,run.one(nC=10,nT=10,sd=1,tau=0.5))
```

```
#Eachrowisasimulationrun:
head(eres)
```

```
##.ntau.hatESSE.hatzp.value
##110.89825000.50.41511472.16385960.030475129
##221.19683640.50.37282163.21021190.001326371
##330.66818530.50.50403431.32567410.184947662
##440.70839300.50.34948662.02695320.042667203
##55-0.10823890.50.4858170-0.22279760.823693047
##660.63339320.50.44255151.43123040.152364186
```

We then summarize our results with the `dplyr summarise` function. Our summarization calculates the average treatment effect estimate `E.tau.hat` , the average Standard Error estimate `E.SE.hat` , the average Effect Size `ES` , and the power `power` (defined as the percent of time we reject at alpha=0.05, i.e., the percent of times our _p_ -value was less than our 0.05 threshold):

```
eres%>%summarise(E.tau.hat=mean(tau.hat),
E.SE.hat=mean(SE.hat),
ES=mean(ES),
power=mean(p.value<=0.05))
```

```
##E.tau.hatE.SE.hatESpower
##10.47798930.44418240.50.192
```

We bundle the above into a function that runs our single trial multiple times and summarizes the results:

6

```
run.experiment=function(nC,nT,sd,tau,mu=5,R=500){
```

```
eres=plyr::rdply(R,run.one(nC,nT,sd,tau,mu))
eres%>%summarise(E.tau.hat=mean(tau.hat),
E.SE.hat=mean(SE.hat),
ES=mean(ES),
power=mean(p.value<=0.05))%>%
mutate(nC=nC,nT=nT,sd=sd,tau=tau,mu=mu,R=R)
}
```

Our function also adds in the details of the simulation (the parameters we passed to the `run.one()` call). Test our function to see what we get:

```
run.experiment(10,3,1,0.5)
```

```
##E.tau.hatE.SE.hatESpowernCnTsdtaumuR
##10.52037160.61720250.50.2110310.55500
```

Key point: We want a dataframe back from `run.experiment()` , because, after calling `run.experiment()` many times, we are going to stack the results up to make one long dataframe of results. Happily the `dplyr` package gives us dataframes so this is not a problem here.

#### **Step 2: Make a dataframe of all experimental combinations desired**

We use the above to run a _multi-factor simulation experiment_ . We are going to vary four factors: control group size, treatment group size, standard deviation of the units, and the treatment effect.

We first set up the levels we want to have for each of our factors (these are our _simulation parameters_ ).

```
nC=c(2,4,7,10,50,500)
nT=c(2,4,7,10,50,500)
sds=c(1,2)
tau=c(0,0.5,1)
```

We then, using `expand.grid()` generate a dataframe of all combinations of our factors.

```
experiments=expand.grid(nC=nC,nT=nT,sd=sds,tau=tau)
head(experiments)
```

```
##nCnTsdtau
##12210
##24210
##37210
##410210
##550210
##6500210
```

See what we get? One row will correspond to a single experimental run. Note how the parameters we would pass to `run.experiment()` correspond to the columns of our dataset.

Also, is easy to end up running a lot of experiments!

```
nrow(experiments)
```

```
##[1]216
```

7

We next run an experiment for each row of our dataframe of experiment factor combinations using the `pmap_df()` function which will, for each row in our dataframe, call `run.experiment()` , passing one parameter taken from each column of our dataframe.

```
exp.res<-experiments%>%pmap_df(run.experiment,R=500)
```

The `R=500` after `run.experiment` passes the _same_ parameter of _R_ = 500 to each run (we run the same number of trials for each experiment).

Here is a peek at our results:

```
head(exp.res)
```

```
##E.tau.hatE.SE.hatESpowernCnTsdtaumuR
##1-0.106690530.858354700.17822105500
##20.050350760.782762400.18842105500
##3-0.029669550.710372700.19072105500
##40.024882720.658038500.200102105500
##5-0.020232490.577353400.250502105500
##60.048480680.538236900.3245002105500
```

At this point you should save your simulation results to a file. This is especially true if the simulation happens to be quite time-intensive to run. Usually a csv file is sufficient.

We save using the tidyverse writing command; see “R for Data Science” textbook, 11.5.

```
write_csv(exp.res,"simulation_results.csv")
```

#### **Step 3: Explore results**

Once your simulation is run, you want to evaluate the results. One would often put this code into a seperate ‘.R’ file that loads this saved file to start. This allows for easily changing how one analyzes an experiment without re-running the entire thing.

##### **Visualizing experimental results**

Plotting is always a good way to vizualize simulation results. Here we make our tau and ES into factors, so `ggplot` behaves, and then plot all our experiments as two rows based on one factor ( `sd` ) with the columns being another ( `nT` ). (This style of plotting a bunch of small plots is called “many multiples” and is beloved by Tufte.) Within each plot we have the x-axis for one factor ( `nC` ) and multiple lines for the final factor ( `tau` ). The _y_ -axis is our outcome of interest, power. We add a 0.05 line to show when we are rejecting at rates above our nominal _α_ . This plot shows the relationship of 5 variables.

```
exp.res=read_csv("simulation_results.csv")
```

```
##Parsedwithcolumnspecification:
##cols(
```

```
##E.tau.hat=col_double(),
##E.SE.hat=col_double(),
##ES=col_double(),
##power=col_double(),
```

```
##nC=col_double(),
##nT=col_double(),
##sd=col_double(),
##tau=col_double(),
##mu=col_double(),
```

8

```
##R=col_double()
##)
```

```
exp.res=exp.res%>%mutate(tau=as.factor(tau),
ES=as.factor(ES))
```

```
ggplot(exp.res,aes(x=nC,y=power,group=tau,col=tau))+
facet_grid(sd~nT,labeller=label_both)+
geom_point()+geom_line()+
scale_x_log10()+
```

```
geom_hline(yintercept=0.05,col="black",lty=2)
```


<!-- Start of picture text -->
nT: 2 nT: 4 nT: 7 nT: 10 nT: 50 nT: 500<br>1.00<br>0.75<br>0.50<br>0.25<br>tau<br>0<br>0.00<br>1.00 0.5<br>1<br>0.75<br>0.50<br>0.25<br>0.00<br>10 100 10 100 10 100 10 100 10 100 10 100<br>nC<br>sd: 1<br>power<br>sd: 2<br><!-- End of picture text -->

**Note:** We are seeing elevated rejection rates under the null for small and even moderate sample size! We can zoom in on specific simulations run, to get some more detail such as estimated power under the null for larger groups. Here we check and we are seeing rejection rates of around 0.05, which is what we want. **`filter`** `( exp.res, tau==0, nT >= 50, nC >= 50 )`

|`## `|`# A tibble: 8 `|`× 10`|||||||
|---|---|---|---|---|---|---|---|---|
|`##`|`E.tau.hat`|`E.SE.hat`|`ES power`|`nC`|`nT`|`sd`|`tau`|`mu`|
|`##`|`<dbl>`|`<dbl> `|`<fctr> <dbl> `|`<dbl> `|`<dbl> `|`<dbl> `|`<fctr> `|`<dbl>`|
|`## `|`1 -0.010968634 `|`0.20015520`|`0 0.048`|`50`|`50`|`1`|`0`|`5`|
|`## `|`2 -0.002663422 `|`0.14684854`|`0 0.054`|`500`|`50`|`1`|`0`|`5`|
|`## `|`3`<br>`0.005843591 `|`0.14769551`|`0 0.068`|`50`|`500`|`1`|`0`|`5`|
|`## `|`4`<br>`0.001324795 `|`0.06325634`|`0 0.044`|`500`|`500`|`1`|`0`|`5`|
|`## `|`5 -0.018673192 `|`0.39954294`|`0 0.040`|`50`|`50`|`2`|`0`|`5`|
|`## `|`6 -0.010723597 `|`0.29481583`|`0 0.062`|`500`|`50`|`2`|`0`|`5`|
|`## `|`7 -0.006330527 `|`0.29459019`|`0 0.062`|`50`|`500`|`2`|`0`|`5`|
|`## `|`8 -0.005772006 `|`0.12643916`|`0 0.050`|`500`|`500`|`2`|`0`|`5`|


9

```
###...with1morevariables:R<dbl>
```

We can get fancy and look at rejection rate (power under `tau = 0` ) as a function of both nC and nT using a contour-style plot:

```
exp.res.rej<-exp.res%>%filter(tau==0)%>%
group_by(nC,nT)%>%
```

```
summarize(power=mean(power))
```

```
exp.res.rej=mutate(exp.res.rej,power=round(power*100))
```

```
ggplot(filter(exp.res.rej),aes(x=nC,y=nT))+
geom_contour(aes(z=power),col="darkgrey")+
scale_x_log10()+scale_y_log10()+
geom_tile(aes(fill=power))+
scale_fill_gradient(trans="log")
```


<!-- Start of picture text -->
100<br>power<br>20.085537<br>7.389056<br>10<br>10 100<br>nC<br>nT<br><!-- End of picture text -->

Admittidly, this plot needs some work to really show the areas with rejection rates of well above 0.05. But we see that small tx or co groups are both bad here.

##### **Looking at main effects**

We can ignore a factor and just look at another. This is looking at the **main effect** or **marginal effect** of the factor.

The easy way to do this is to let `ggplot` smooth our individual points on a plot. Be sure to also plot the individual points to see variation, however.

10

```
ggplot(exp.res,aes(x=nC,y=power,group=tau,col=tau))+
facet_grid(sd~.,labeller=label_both)+
geom_jitter(width=0.02,height=0)+
geom_smooth(se=FALSE)+
scale_x_log10(breaks=nC)+
geom_hline(yintercept=0.05,col="black",lty=2)
```


<!-- Start of picture text -->
1.00<br>0.75<br>0.50<br>0.25<br>tau<br>0<br>0.00<br>0.5<br>1.00<br>1<br>0.75<br>0.50<br>0.25<br>0.00<br>2 4 7 10 50 500<br>nC<br>sd: 1<br>power<br>sd: 2<br><!-- End of picture text -->

Note how we see our individual runs that we marginalize over.

To look at our main effects we can also summarize our results, averaging our experimental runs across other factor levels. For example, in the code below we average over the different treatment group sizes and standard deviations, and plot the marginalized results.

To marginalize, we group by the things we want to keep. `summarise()` then averages over the things we want to get rid of.

```
exp.res.sum=exp.res%>%group_by(nC,tau)%>%
summarise(power=mean(power))
head(exp.res.sum)
```

```
##Source:localdataframe[6x3]
##Groups:nC[2]

---

[← 1-sampleproportionstestwithcontinuitycorrection](06-1-sampleproportionstestwithcontinuitycorrection.md) · [Up: contents](index.md) · [nCtaupower →](08-nctaupower.md)
