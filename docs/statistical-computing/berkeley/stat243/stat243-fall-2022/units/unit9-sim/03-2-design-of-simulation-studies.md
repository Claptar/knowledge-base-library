---
title: 2. Design of simulation studies
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit9-sim.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2. Design of simulation studies

**Source:** [`units/unit9-sim.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit9-sim.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

Consider the paper that is part of PS5. We can think about
designing a simulation study in that context.

First, what are the key issues that need to be assessed to evaluate
their methodology?

Second, what do we need to consider in carrying out a simulation study
to address those issues? I.e., what are the key decisions to be made in
setting up the simulations?

## Basic steps of a simulation study

1.  Specify what makes up an individual experiment (i.e., the individual
    simulated dataset) given a specific set of inputs: sample size,
    distribution(s) to use, parameter values, statistic of interest,
    etc. In other words, exactly how would you generate one simulated
    dataset?

2.  Often you'll want to see how your results will vary if you change
    some of the inputs; e.g., sample sizes, parameter values, data
    generating mechanisms. So determine what factors you'll want to
    vary. Each unique combination of input values will be a scenario.

3.  Write code to carry out the individual experiment and return the
    quantity of interest, with arguments to your code being the inputs
    that you want to vary.

4.  For each combination of inputs you want to explore (each scenario),
    repeat the experiment $m$ times. Note this is an easily
    parallel calculation (in both the data generating dimension and the
    inputs dimension(s)).

5.  Summarize the results for each scenario, quantifying simulation
    uncertainty.

6.  Report the results in graphical or tabular form.

Often a simulation study will compare multiple methods, so you'll need
to do steps 3-6 for each method.

## Various considerations

Since a simulation study is an experiment, we should use the same
principles of design and analysis we would recommend when advising a
practicioner on setting up a scientific experiment.

These include efficiency, reporting of uncertainty, reproducibility and
documentation.

In generating the data for a simulation study, we want to think about
what structure real data would have that we want to mimic in the
simulation study: distributional assumptions, parameter values,
dependence structure, outliers, random effects, sample size ($n$), etc.

All of these may become input variables in a simulation study. Often we
compare two or more statistical methods conditioning on the data context
and then assess whether the differences between methods vary with the
data context choices. E.g., if we compare an MLE to a robust estimator,
which is better under a given set of choices about the data generating
mechanism and how sensitive is the comparison to changing the features
of the data generating mechanism? So the "treatment variable" is the
choice of statistical method. We're then interested in sensitivity to
the conditions (different input values).

Often we can have a large number of replicates ($m$) because the
simulation is fast on a computer, so we can sometimes reduce the
simulation error to essentially zero and thereby avoid reporting
uncertainty. To do this, we need to calculate the simulation standard
error, generally, $s/\sqrt{m}$ and see how it compares to the effect
sizes. This is particularly important when reporting on the bias of a
statistical method.

We might denote the data, which could be the statistical estimator under
each of two methods as $Y_{ijklq}$, where $q$ indexes treatment, $j,k,l$
index different additional input variables, and $i\in\{1,\ldots,m\}$
indexes the replicate. E.g., $j$ might index whether the data are from a
t or normal, $k$ the value of a parameter, and $l$ the dataset sample
size (i.e., different levels of $n$).

One can think about choosing $m$ based on a basic power calculation,
though since we can always generate more replicates, one might just
proceed sequentially and stop when the precision of the results is
sufficient.

When comparing methods, it's best to use the same simulated datasets for
each level of the treatment variable and to do an analysis that controls
for the dataset (i.e., for the random numbers used), thereby removing
some variability from the error term. A simple example is to do a paired
analysis, where we look at differences between the outcome for two
statistical methods, pairing based on the simulated dataset.

One can even use the "same" random number generation for the replicates
under different conditions. E.g., in assessing sensitivity to a $t$ vs.
normal data generating mechanism, we might generate the normal RVs and
then for the $t$ use the same random numbers, in the sense of using the
same quantiles of the $t$ as were generated for the normal - this is
pretty easy, as seen below. This helps to control for random differences
between the datasets.

```r
devs <- rnorm(100)
tdevs <- qt(pnorm(devs), df = 1)
plot(devs, tdevs)
abline(0,1)
```


## Experimental Design (optional)

A typical context is that one wants to know the effect of multiple input
variables on some outcome. Often, scientists, and even statisticians
doing simulation studies will vary one input variable at a time. As we
know from standard experimental design, this is inefficient.

The standard strategy is to discretize the inputs, each into a small
number of levels. If we have a small enough number of inputs and of
levels, we can do a full factorial design (potentially with
replication). For example if we have three inputs and three levels each,
we have $3^{3}$ different treatment combinations. Choosing the levels in
a reasonable way is obviously important.

As the number of inputs and/or levels increases to the point that we
can't carry out the full factorial, a fractional factorial is an option.
This carefully chooses which treatment combinations to omit. The goal is
to achieve balance across the levels in a way that allows us to estimate
lower level effects (in particular main effects) but not all high-order
interactions. What happens is that high-order interactions are aliased
to (confounded with) lower-order effects. For example you might choose a
fractional factorial design so that you can estimate main effects and
two-way interactions but not higher-order interactions.

In interpreting the results, I suggest focusing on the decomposition of
sums of squares and not on statistical significance. In most cases, we
expect the inputs to have at least some effect on the outcome, so the
null hypothesis is a straw man. Better to assess the magnitude of the
impacts of the different inputs.

When one has a very large number of inputs, one can use the Latin
hypercube approach to sample in the input space in a uniform way,
spreading the points out so that each input is sampled uniformly. Assume
that each input is $\mathcal{U}(0,1)$ (one can easily transform to
whatever marginal distributions you want). Suppose that you can run $m$
samples. Then for each input variable, we divide the unit interval into
$m$ bins and randomly choose the order of bins and the position within
each bin. This is done independently for each variable and then combined
to give $m$ samples from the input space. We would then analyze main
effects and perhaps two-way interactions to assess which inputs seem to
be most important.

Even amongst statisticians, taking an experimental design approach to a
simulation study is not particularly common, but it's worth considering.

---

[← 1. Monte Carlo considerations](02-1-monte-carlo-considerations.md) · [Up: contents](index.md) · [3. Implementation of simulation studies →](04-3-implementation-of-simulation-studies.md)
