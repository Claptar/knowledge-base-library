---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2019/section/08/parallelR.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`section/08/parallelR.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/section/08/parallelR.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(echo = TRUE)
set.seed(0)
```


Many tasks that are computationally expensive are embarrassingly parallel. A few
common tasks that fit the description:

- Simulations with independent replicates
- Bootstrapping
- Cross-validation
- Multivariate Imputation by Chained Equations (MICE)
- Fitting multiple regression models
- cross-validation


## `lapply` Refresher

`lapply` takes one parameter (a vector/list), feeds that variable into the
function, and returns a list:

```r
  lapply(1:3, function(x) c(x, x^2, x^3))
```

You can feed it additional values by adding named parameters:

```r
  lapply(1:3/3, round, digits=3)
```

These tasks are embarrassingly parallel as the elements are calculated independently,
i.e. second element is independent of the result from the first element. After
learning to code using `lapply` parallelizing your code is simple.

\newpage
## `future` Package

The [future](https://cran.r-project.org/web/packages/future/index.html) package
attempts to provide a simple and uniform framework for evaluating expressions on
various resources.

```r
library(future)

v %<-% {
  cat("Hello world!\n")
  3.14
}

v
```

Notice, the definition is evaluated when the variable is called, instead of when
the variable is defined. There are several methods for controlling how futures are
evaluated. The types of futures are listed in \ref{table:res}, and implemented as `plan()`s.

\begin{table}
\centering
\caption{Future Resolution Strategies}
\begin{tabular}{ c c c }
 \hline
 \textbf{Name} & \textbf{OS} & \textbf{Description} \\
 \textit{synchronous} & & \textit{non-parallel} \\
 sequential & all & sequentially in current  R process \\
 transparent & all & as sequential w/ early signaling and w/out local \\
 \textit{asynchronous} &  & \textit{parallel} \\
 multiprocess & all & multicore if possible, multisession otherwise \\
 multisession & all & background R sessions (current machine) \\
 multicore & not Windows/Rstudio & forked process \\
 cluster & all & external R session, current or local machines \\
 remote & all & remote R sessions \\
 \hline
\end{tabular}
\label{table:res}
\end{table}

Futures can also be evaluated *asynchronously* in a different R process by setting
the `plan()` to one of the *asynchronous* options.
```r
plan(strategy = multiprocess)

w %<-% {
  cat("Hello world!\n")
  3.14
}

w
```

The `future` package is extended by the `future.apply` package, which implements
the *apply* family of functions from base `R`.

```r
library(future.apply)

---

[Up: contents](index.md) · [set evaluation plan →](02-set-evaluation-plan.md)
