---
title: 4 Design of simulation studies
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit12-sim.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit12-sim.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Design of simulation studies

**Source:** [`units/unit12-sim.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit12-sim.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Let’s pose a concrete example. This is based on a JASA paper that you’ll look at more carefully in a problem set. Suppose one is modeling data as being from a mixture of normal distributions:


where _f_ ( _y_ ; _µh, σh_ ) is a normal density with mean _µh_ and s.d. _σh_ . A statistician has developed methodology for carrying out a hypothesis test for _H_ 0 : _m_ = _m_ 0 vs. _Ha_ : _m > m_ 0.

First, what are the key issues that need to be assessed to evaluate their methodology? What do we want to know to assess a hypothesis test?

Second, what do we need to consider in carrying out a simulation study to address those issues?

### **4.1 Basic steps of a simulation study**

1. Specify what makes up an individual experiment: sample size, distributions, parameters, statistic of interest, etc.

2. Determine what inputs, if any, to vary; e.g., sample sizes, parameters, data generating mechanisms

3. Write code to carry out the individual experiment and return the quantity of interest

4. For each combination of inputs, repeat the experiment _m_ times. Note this is an embarrassingly parallel calculation (in both the data generating dimension and the inputs dimension(s).

5. Summarize the results for each combination of interest, quantifying simulation uncertainty

6. Report the results in graphical or tabular form

18

### **4.2 Overview**

Since a simulation study is an experiment, we should use the same principles of design and analysis we would recommend when advising a practicioner on setting up an experiment.

These include efficiency, reporting of uncertainty, reproducibility and documentation.

In generating the data for a simulation study, we want to think about what structure real data would have that we want to mimic in the simulation study: distributional assumptions, parameter values, dependence structure, outliers, random effects, sample size ( _n_ ), etc.

All of these may become input variables in a simulation study. Often we compare two or more statistical methods conditioning on the data context and then assess whether the differences between methods vary with the data context choices. E.g., if we compare an MLE to a robust estimator, which is better under a given set of choices about the data generating mechanism and how sensitive is the comparison to changing the features of the data generating mechanism? So the “treatment variable” is the choice of statistical method. We’re then interested in sensitivity to the conditions.

Often we can have a large number of replicates ( _m_ ) because the simulation is fast on a computer, so we can sometimes reduce the simulation error to essentially zero and thereby avoid reporting uncertainty. To do this, we need to calculate the simulation standard error, generally, _s/_<sup>_√_</sup> _<u>m</u>_ and see how it compares to the effect sizes. This is particularly important when reporting on the bias of a statistical method.

We might denote the data, which could be the statistical estimator under each of two methods as _Yijklq_ , where _i_ indexes treatment, _j, k, l_ index different additional input variables, and _q ∈ {_ 1 _, . . . , m}_ indexes the replicate. E.g., _j_ might index whether the data are from a t or normal, _k_ the value of a parameter, and _l_ the dataset sample size (i.e., different levels of _n_ ).

One can think about choosing _m_ based on a basic power calculation, though since we can always generate more replicates, one might just proceed sequentially and stop when the precision of the results is sufficient.

When comparing methods, it’s best to use the same simulated datasets for each level of the treatment variable and to do an analysis that controls for the dataset (i.e., for the random numbers used), thereby removing some variability from the error term. A simple example is to do a paired analysis, where we look at differences between the outcome for two statistical methods, pairing based on the simulated dataset.

One can even use the “same” random number generation for the replicates under different conditions. E.g., in assessing sensitivity to a _t_ vs. normal data generating mechanism, we might generate the normal RVs and then for the _t_ use the same random numbers, in the sense of using the same quantiles of the _t_ as were generated for the normal - this is pretty easy, as seen below. This helps to control for random differences between the datasets.

19

devs <- **rnorm** (100) tdevs <- **qt** ( **pnorm** (devs), df = 1) **plot** (devs, tdevs) **abline** (0,1)


<!-- Start of picture text -->
G<br>GGGG G GGG GG GGGG G G G G GG GG GGGGG G GGGG G GG G GGG G GGGG G G G GGGG G GGG<br>−2 −1 0 1 2<br>devs<br>80<br>40<br>tdevs<br>0<br><!-- End of picture text -->

### **4.3 Experimental Design**

A typical context is that one wants to know the effect of multiple input variables on some outcome. Often, scientists, and even statisticians doing simulation studies will vary one input variable at a time. As we know from standard experimental design, this is inefficient.

The standard strategy is to discretize the inputs, each into a small number of levels. If we have a small enough number of inputs and of levels, we can do a full factorial design (potentially with replication). For example if we have three inputs and three levels each, we have 3<sup>3</sup> different treatment combinations. Choosing the levels in a reasonable way is obviously important.

As the number of inputs and/or levels increases to the point that we can’t carry out the full factorial, a fractional factorial is an option. This carefully chooses which treatment combinations to omit. The goal is to achieve balance across the levels in a way that allows us to estimate lower level effects (in particular main effects) but not all high-order interactions. What happens is that high-order interactions are aliased to (confounded with) lower-order effects. For example you might choose a fractional factorial design so that you can estimate main effects and two-way interactions but not higher-order interactions.

In interpreting the results, I suggest focusing on the decomposition of sums of squares and not on statistical significance. In most cases, we expect the inputs to have at least some effect on the

20

outcome, so the null hypothesis is a straw man. Better to assess the magnitude of the impacts of the different inputs.

When one has a very large number of inputs, one can use the Latin hypercube approach to sample in the input space in a uniform way, spreading the points out so that each input is sampled uniformly. Assume that each input is _U_ (0 _,_ 1) (one can easily transform to whatever marginal distributions you want). Suppose that you can run _m_ samples. Then for each input variable, we divide the unit interval into _m_ bins and randomly choose the order of bins and the position within each bin. This is done independently for each variable and then combined to give _m_ samples from the input space. We would then analyze main effects and perhaps two-way interactions to assess which inputs seem to be most important.

---

[← 3 Generating random variables](04-3-generating-random-variables.md) · [Up: contents](index.md) · [5 Implementation of simulation studies →](06-5-implementation-of-simulation-studies.md)
