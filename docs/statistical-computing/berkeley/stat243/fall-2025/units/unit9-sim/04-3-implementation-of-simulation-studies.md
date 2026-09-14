---
title: 3. Implementation of simulation studies
source: https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit9-sim.qmd
source_file: sources/berkeley-stat243/fall-2025/units/unit9-sim.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 3. Implementation of simulation studies

**Source:** [`units/unit9-sim.qmd`](https://github.com/berkeley-stat243/fall-2025/blob/035a19ebd7ab88cffca907cade6d40212d575a1f/units/unit9-sim.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Luke Miratrix (a UCB Stats PhD alum) has prepared a nice tutorial on
carrying out a simulation study, including helpful R code. So if the
discussion here is not concrete enough or you want to see how to
effectively implement such a study, see
*simulation_tutorial_miratrix.pdf* and the similarly named R code file.

## Computational efficiency

Parallel processing is often helpful for simulation studies. The reason
is that simulation studies are embarrassingly parallel - we can send
each replicate to a different computer processor and then collect the
results back, and the speedup should scale directly with the number of
processors we used. Since we often need to some sort of looping, writing
code in C/C++ and compiling and linking to the code from Python may also be a
good strategy, albeit one not covered in this course.

A handy function in Python is `itertools.product` to get all combinations of
a set of vectors.

```python
import itertools

thetaLevels = ["low", "med", "hi"]
n = [10, 100, 1000]
tVsNorm = ["t", "norm"]
levels = list(itertools.product(thetaLevels, tVsNorm, n))
```


## Analysis and reporting

Often results are reported simply in tables, but it can be helpful to
think through whether a graphical representation is more informative
(sometimes it's not or it's worse, but in some cases it may be much
better). Since you'll often have a variety of scenarios to display,
using trellis plots in ggplot2 via the `facet_wrap` function will often
be a good approach to display how results vary as a function of multiple
inputs in R. In Python, it looks like there are various ways (`RPlot` in pandas,
seaborn, plotly), but I don't know what the most standard way is.

You should set the seed when you start the experiment, so that it's
possible to replicate it. It's also a good idea to save the current
value of the seed whenever you save interim results, so that you can
restart simulations (this is particularly helpful for MCMC) at the exact
point you left off, including the random number sequence.

To enhance reproducibility, it's good practice to post your simulation
code (and potentially simulated data) on GitHub, on your website, or as
supplementary material with the journal. Another person should be able
to fully reproduce your results, including the exact random number
generation that you did (e.g., you should provide code for how you set
the random seed for your randon number generator).

Many journals are requiring increasingly detailed documentation of the
code and data used in your work, including code and data for
simulations. Here are the American Statistical Association's
requirements on documenting computations in its journals:

"The ASA strongly encourages authors to submit datasets, code, other
programs, and/or extended appendices that are directly relevant to their
submitted articles. These materials are valuable to users of the ASA's
journals and further the profession's commitment to reproducible
research. Whenever a dataset is used, its source should be fully
documented and the data should be made available as on online
supplement. Exceptions for reasons of security or confidentiality may be
granted by the Editor. Whenever specific code has been used to implement
or illustrate the results of a paper, that code should be made available
if possible. $$\....snip\....$$ Articles reporting results based on
computation should provide enough information so that readers can
evaluate the quality of the results. Such information includes estimated
accuracy of results, as well as descriptions of pseudorandom-number
generators, numerical algorithms, programming languages, and major
software components used."

---

[← 2. Design of simulation studies](03-2-design-of-simulation-studies.md) · [Up: contents](index.md) · [4. Random number generation (RNG) →](05-4-random-number-generation-rng.md)
