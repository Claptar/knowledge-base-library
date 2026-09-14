---
title: 6 Formulas
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 6 Formulas

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Formulas were initially introduced into R to specify linear models, but are now used more generally.

Here are some examples of formulas in R, used to specify a model structure:

- Additive model:

y ~ x1 + x2 + x3

39

- Additive model without the intercept:

y ~ x1 + x2 + x3 -1

- All the other variables in the data frame are used as covariates:

   - y ~ .

- All possible interactions:

   - y ~ x1 * x2 * x3

- Only specified interactions (in this case _x1_ by _x2_ ) (of course, you’d rarely want to fit this without _x2_ ):

y ~ x1 + x3 + x1:x2

- Creating a factor on the fly:

   - y ~ x1 + factor(x2)

- Protecting arithmetic expressions:

   - y ~ x1 + I(x1^2) + I(x1^3)

- Using functions of variables

y ~ x1 + log(x2) + sin(x3)

In some contexts, such as _lattice_ package graphics, the “|” indicates conditioning, so y ~ x | z would mean to plot _y_ on _x_ within groups of _z_ . In the context of lme-related packages (e.g., _lme4_ , _nlme_ , etc.), variables after “|” are _grouping_ variables (e.g., if you have a random effect for each hospital, hospital would be the grouping variable) and multiple grouping variables are separated by “ _/_ ”.

We can manipulate formulae as objects, allowing automation. Consider how this sort of thing could be used to write code for automated model selection.

resp <- "y ~" covTerms <- "x1" **for** (i **in** 2:5) { covTerms <- **paste** (covTerms, "+ x", i, sep = "") } form <- **as.formula** ( **paste** (resp, covTerms, sep = "")) _# lm(form, data = dat)_ form ## y ~ x1 + x2 + x3 + x4 + x5

40

**class** (form) ## [1] "formula"

The for loop is a bit clunky/inefficient - let’s do better:

resp <- "y ~" covTerms <- **paste** ("x", 1:5, sep = "", collapse = " + ") form <- **as.formula** ( **paste** (resp, covTerms)) form ## y ~ x1 + x2 + x3 + x4 + x5 _# lm(form, data = dat)_

Standard arguments in model fitting functions, in addition to the formula are _weights_ , _data_ (indicating the data frame in which to interpret the variable names), _subset_ (for using a subset of data), and _na.action_ . Note that the default _na.action_ in R is set in _options()$na.action_ and is _na.omit_ , so be wary in fitting models in that you are dropping cases with NAs and may not be aware of it.

There is some more specialized syntax given in _R-intro.pdf_ on CRAN.

---

[← 5 Flow control and logical operations](27-5-flow-control-and-logical-operations.md) · [Up: contents](index.md) · [7 Functions, variable scoping, and frames →](29-7-functions-variable-scoping-and-frames.md)
