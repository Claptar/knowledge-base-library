---
title: suppress package-loading messages by loading here
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# suppress package-loading messages by loading here

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

library(fields)
```

```r
library(R6)

tsSimClass <- R6Class("tsSimClass",
    ## class for holding time series simulators
    public = list(
        initialize = function(times, mean = 0, corParam = 1) {
            library(fields)
            stopifnot(is.numeric(corParam), length(corParam) == 1)
            stopifnot(is.numeric(times))
            private$times <- times
            private$n <- length(times)
            private$mean <- mean
            private$corParam <- corParam
            private$currentU <- FALSE
            private$calcMats()
        },

        setTimes = function(newTimes) {
            private$times <- newTimes
            private$calcMats()
        },

        getTimes = function() {
            return(private$times)
        },

        print = function() { # 'print' method
            cat("R6 Object of class 'tsSimClass' with ",
                private$n, " time points.\n", sep = '')
            invisible(self)
        },

        simulate = function() {
            if(!private$currentU)
                private$calcMats()
            ## analogous to mu+sigma*z for generating N(mu, sigma^2)
            return(private$mean + crossprod(private$U, rnorm(private$n)))
        }
    ),

    ## private methods and functions not accessible externally
    private = list(
        calcMats = function() {
            ## calculates correlation matrix and Cholesky factor
            lagMat <- fields::rdist(private$times) # local variable
            corMat <- exp(-lagMat^2 / private$corParam^2)
            private$U <- chol(corMat) # square root matrix
            cat("Done updating correlation matrix and Cholesky factor.\n")
            private$currentU <- TRUE
            invisible(self)
        },
        n = NULL,
        times = NULL,
        mean = NULL,
        corParam = NULL,
        U = NULL,
        currentU = FALSE
    )
)

```


Now let's see how we would use the class.

```r
myts <- tsSimClass$new(1:100, 2, 1)
myts
set.seed(1)
## here's a simulated time series
y1 <- myts$simulate()
plot(myts$getTimes(), y1, type = 'l', xlab = 'time',
     ylab = 'process values')
## simulate a second series
y2 <- myts$simulate()
lines(myts$getTimes(), y2, lty = 2)
```

We could set up a different object that has different parameter values.
That new simulated time series is less wiggly because the `corParam` value
 is larger than before.


```r
myts2 <- tsSimClass$new(1:100, 2, 4)
set.seed(1)
## here's a simulated time series with a different value of
## the correlation parameter (corParam)
y3 <- myts2$simulate()

plot(myts$getTimes(), y1, type = 'l', xlab = 'time',
     ylab = 'process values')
lines(myts$getTimes(), y2, lty = 2)
lines(myts2$getTimes(), y3, col = 'red')
```

#### Copies and references

Next let's think about when copies are made. In the next example `mytsRef` is a copy of `myts`
in the sense that both names point to the same underlying object.
But no data were copied when the assignment to `mytsRef` was done.

```r
mytsRef <- myts
## 'mytsRef' and 'myts' are names for the same underlying object
mytsFullCopy <- myts$clone()

## Now let's change the values of a field
myts$setTimes(seq(0,1000, length = 100))
myts$getTimes()[1:5]
mytsRef$getTimes()[1:5] # the same as `myts`
mytsFullCopy$getTimes()[1:5] # different from `myts`
```

In contrast `mytsFullCopy` is a reference to a different object, and
all the data from `myts` had to be copied over to `mytsFullCopy`. This takes additional memory (and time), but is also safer, as it avoids the possibility that the user might modify `myts` and not realize that they were also affecting `mytsRef`.

#### Encapsulation

Why have private fields (i.e., encapsulation)? The use of private fields shields them from
    modification by users. In this case, that prevent users from modifying the
*times* field. Why is this important? In this example, the correlation matrix and
    the Cholesky factor U are both functions of the vector of times. So
    we don't want to allow a user to directly modify *times*. If they did, it would leave the fields of the object in inconsistent states. Instead we
    force them to use *setTimes*, which correctly keeps all the fields
    in the object internally consistent (by calling *calcMats*). It also allows us to improve efficiency
by controlling when computationally expensive operations are carried out.

```r
try(myts$times <- 1:10)
```

#### Final comments

  -   As we saw above, a copy of an object is just a pointer to the original object, unless we explicitly invoke the *clone* method.
  -   Classes can inherit from other classes. E.g., if we had a *simClass* and we wanted the *tsSimClass* to inherit from it:

      ```
      R6Class(tsSimClass, inherit = simClass, ...)
      ```
  -   If you need to refer to methods and fields you refer to the entire object as either *self* or *private*.


More details on R6 classes can be found in the [Advanced R book](https://adv-r.hadley.nz/r6.html).

---

[← print.default(mod) ## lots of output, so don't print in document...](09-print-default-mod-lots-of-output-so-don-t-print-in-document.md) · [Up: contents](index.md) · [7. Functional programming →](11-7-functional-programming.md)
