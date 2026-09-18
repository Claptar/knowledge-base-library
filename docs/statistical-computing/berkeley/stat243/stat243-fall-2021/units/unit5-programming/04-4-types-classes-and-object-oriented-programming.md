---
title: 4 Types, classes, and object-oriented programming
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2021/units/unit5-programming.pdf
licence: CC0-1.0
route: llm
fidelity: reconstructed
converted: '2026-09-18'
---

> **Reconstructed by a model.** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/units/unit5-programming.pdf) — berkeley-stat243 · stat243-fall-2021, licensed CC0-1.0. Converted 2026-09-18 from `.pdf`. The original is a PDF with no usable text layer. A model read the pages and wrote this markdown: the prose is a paraphrase in places and **every equation is unverified**. Treat it as a pointer into the original, never as a citable source.

# 4 Types, classes, and object-oriented programming

### 4.1 Types and classes

You should be familiar with vectors as the basic data structure in R, with character, integer, numeric, etc. classes. Vectors are either *atomic vectors* or *lists*. Atomic vectors generally contain one of the four following types: *logical*, *integer*, *double/numeric*, and *character*.

Objects in general have a *type*, which relates to what kind of values are in the objects and how objects are stored internally in R (i.e., in C).

You can look at Table 7.1 in the Adler book to see some other types.

```r
devs <- rnorm(5)
class(devs)
## [1] "numeric"

typeof(devs)
## [1] "double"

a <- data.frame(x = 1:2)
class(a)
## [1] "data.frame"

typeof(a)
## [1] "list"

is.data.frame(a)
## [1] TRUE

is.matrix(a)
## [1] FALSE

is(a, "matrix")
## [1] FALSE

m <- matrix(1:4, nrow = 2)
class(m)
## [1] "matrix" "array"

typeof(m)
## [1] "integer"
```

Everything in R is an object and all objects have a class. For simple objects class and type are often closely related, but this is not the case for more complicated objects. The class describes what the object contains and standard functions associated with it. In general, you mainly need to know what class an object is rather than its type. Classes can *inherit* from other classes; for example, the *glm* class inherits characteristics from the *lm* class. We'll see more on the details of object-oriented programming shortly.

We can create objects with our own defined class (an S3 class in this simple example - we'll discuss S3 classes in Section 4.4.1).

```r
bart <- list(firstname = 'Bart', surname = 'Simpson',
             hometown = "Springfield")
class(bart) <- 'personClass'
## it turns out R already has a 'person' class
class(bart)
## [1] "personClass"

is.list(bart)
## [1] TRUE

typeof(bart)
## [1] "list"

typeof(bart$firstname)
## [1] "character"
```

### 4.2 Attributes

*Attributes* are information about an object attached to an object as something that looks like a named list. Attributes are often copied when operating on an object. This can lead to some weird-looking formatting:

```r
x <- rnorm(10 * 365)
attributes(x)
## NULL

qs <- quantile(x, c(.025, .975))
attributes(qs)
## $names
## [1] "2.5%"  "97.5%"

qs
##  2.5% 97.5%
## -1.95  1.94

qs[1] + 3
##  2.5%
##  1.05

object.size(qs)
## 352 bytes
```

Thus in any subsequent operations with *qs*, the *names* attribute will often get carried along. We can get rid of it:

```r
names(qs) <- NULL
qs
## [1] -1.95  1.94

object.size(qs)
## 64 bytes
```

A common use of attributes is that rows and columns may be named in matrices and data frames, and elements in vectors:

```r
row.names(mtcars)[1:6]
## [1] "Mazda RX4"         "Mazda RX4 Wag"     "Datsun 710"
## [4] "Hornet 4 Drive"    "Hornet Sportabout" "Valiant"

names(mtcars)
## [1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec" "vs"   "am"   "gear"
## [11] "carb"

attributes(mtcars)
## $names
##  [1] "mpg"  "cyl"  "disp" "hp"   "drat" "wt"   "qsec"
##  [8] "vs"   "am"   "gear" "carb"
##
## $row.names
##  [1] "Mazda RX4"           "Mazda RX4 Wag"
##  [3] "Datsun 710"          "Hornet 4 Drive"
##  [5] "Hornet Sportabout"   "Valiant"
##  [7] "Duster 360"          "Merc 240D"
##  [9] "Merc 230"            "Merc 280"
## [11] "Merc 280C"           "Merc 450SE"
## [13] "Merc 450SL"          "Merc 450SLC"
## [15] "Cadillac Fleetwood"  "Lincoln Continental"
## [17] "Chrysler Imperial"   "Fiat 128"
## [19] "Honda Civic"         "Toyota Corolla"
## [21] "Toyota Corona"       "Dodge Challenger"
## [23] "AMC Javelin"         "Camaro Z28"
## [25] "Pontiac Firebird"    "Fiat X1-9"
## [27] "Porsche 914-2"       "Lotus Europa"
## [29] "Ford Pantera L"      "Ferrari Dino"
## [31] "Maserati Bora"       "Volvo 142E"
##
## $class
## [1] "data.frame"

mat <- data.frame(x = 1:2, y = 3:4)
attributes(mat)
## $names
## [1] "x" "y"
##
## $class
## [1] "data.frame"
##
## $row.names
## [1] 1 2

row.names(mat) <- c("first", "second")
mat
##        x y
## first  1 3
## second 2 4

attributes(mat)
## $names
## [1] "x" "y"
##
## $class
## [1] "data.frame"
##
## $row.names
## [1] "first"  "second"

vec <- c(first = 7, second = 1, third = 5)
vec['first']
## first
##     7

attributes(vec)
## $names
## [1] "first"  "second" "third"
```

### 4.3 Assignment and coercion

We assign into an object using either '=' or '<-'. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, '=' is fine, but otherwise use '<-'.

Let's look at these examples to understand the distinction between '=' and '<-' when passing arguments to a function.

```r
mean
## function (x, ...)
## UseMethod("mean")
## <bytecode: 0x556916aba2c8>
## <environment: namespace:base>

x <- 0; y <- 0
out <- mean(x = c(3,7)) # usual way to pass an argument to a function by name
out <- mean(c(3,7))     # or by position
## what does the following do?
out <- mean(x <- c(3,7)) # this is allowable, but confusing
out <- mean(y = c(3,7))  # why doesn't this work?
## Error in mean.default(y = c(3, 7)): argument "x" is missing, with
no default

out <- mean(y <- c(3,7)) # again, allowable, but confusing
```

What can you tell me about what is going on in each case above?

One situation in which you want to use '<-' is if it is being used as part of an argument to a function, so that R realizes you're not indicating one of the function arguments, e.g.:

```r
## NOT OK, system.time() expects its argument to be a complete R expression:
system.time(out = rnorm(10000))
## Error in system.time(out = rnorm(10000)): unused argument (out
= rnorm(10000))

# OK:
system.time(out <- rnorm(10000))
##    user  system elapsed
##   0.001   0.000   0.001
```

Here's another example:

```r
mat <- matrix(c(1, NA, 2, 3), nrow = 2, ncol = 2)
apply(mat, 1, sum.isna <- function(vec) {return(sum(is.na(vec)))})
## [1] 0 1

## What is the side effect of what I have done just above?
apply(mat, 1, sum.isna = function(vec) {return(sum(is.na(vec)))}) # NOPE
## Error in match.fun(FUN): argument "FUN" is missing, with no default
```

R often treats integers as numerics, but we can force R to store values as integers:

```r
vals <- c(1, 2, 3)
class(vals)
## [1] "numeric"

vals <- 1:3
class(vals)
## [1] "integer"

vals <- c(1L, 2L, 3L)
vals
## [1] 1 2 3

class(vals)
## [1] "integer"
```

We convert between classes using variants on `as()`: e.g.,

```r
as.character(c(1,2,3))
## [1] "1" "2" "3"

as.numeric(c("1", "2.73"))
## [1] 1.00 2.73

as.factor(c("a", "b", "c"))
## [1] a b c
## Levels: a b c
```

Some common conversions are converting numbers that are being interpreted as characters into actual numbers, converting between factors and characters, and converting between logical TRUE/FALSE vectors and numeric 1/0 vectors. In some cases R will automatically do conversions behind the scenes in a smart way (or occasionally not so smart way). Consider these examples of *implicit coercion*:

```r
x <- rnorm(5)
x[3] <- 'hat' # What do you think is going to happen?
indices <- c(1, 2.73)
myVec <- 1:10
myVec[indices]
## [1] 1 2
```

Be careful of using factors as indices:

```r
students <- factor(c("basic", "proficient", "advanced",
                     "basic", "advanced", "minimal"))
score <- c(minimal = 3, basic = 1, advanced = 13, proficient = 7)
score["advanced"]
## advanced
##       13

score[students[3]]
## minimal
##       3

score[as.character(students[3])]
## advanced
##       13
```

What has gone wrong and how does it relate to type coercion?

In other languages, converting between different classes is sometimes called *casting* a variable.

Here's an example we can work through that will help illustrate how type conversions occur behind the scenes in R.

```r
n <- 5
df <- data.frame(rep('a', n), rnorm(n), rnorm(n))
apply(df, 1, function(x) x[2] + x[3])
## Error in x[2] + x[3]: non-numeric argument to binary operator

## why does that not work?
apply(df[ , 2:3], 1, function(x) x[1] + x[2])
## [1]  0.663 -0.300 -0.385  2.024 -0.482

## let's look at apply() to better understand what is happening
```

### 4.4 Object-oriented programming

Popular languages that use OOP include C++, Java, and Python. In fact C++ is the object-oriented version of C. Different languages implement OOP in different ways.

The idea of OOP is that all operations are built around objects, which have a *class*, and *methods* (i.e., class-specific functions) that operate on objects in the class. Classes are constructed to build on (inherit from) each other, so that one class may be a specialized form of another class, extending the components and methods of the simpler class (e.g., *lm* and *glm* objects).

Note that in more formal OOP languages, all functions are associated with a class, while in R, only some are.

Often when you get to the point of developing OOP code in R, you're doing more serious programming, and you're going to be acting as a software engineer. It's a good idea to think carefully in advance about the design of the classes and methods.

#### 4.4.1 S3 approach

S3 classes are widely-used, in particular for statistical models in the *stats* package. S3 classes are very informal in that there's not a formal definition for an S3 class. Instead, an S3 object is just a primitive R object such as a list or vector with additional attributes including a class name.

**Inheritance** Let's look at the *lm* class, which builds on lists, and *glm* class, which builds on the *lm* class. Here `mod` is an object (an instance) of class *lm*. An analogy is the difference between a random variable and a realization of that random variable.

```r
library(methods)
yb <- sample(c(0, 1), 10, replace = TRUE)
yc <- rnorm(10)
x <- rnorm(10)
mod1 <- lm(yc ~ x)
mod2 <- glm(yb ~ x, family = binomial)
class(mod1)
## [1] "lm"

class(mod2)
## [1] "glm" "lm"

is.list(mod1)
## [1] TRUE

names(mod1)
##  [1] "coefficients"  "residuals"      "effects"
##  [4] "rank"          "fitted.values" "assign"
##  [7] "qr"            "df.residual"   "xlevels"
## [10] "call"          "terms"         "model"

is(mod2, "lm")
## [1] TRUE

methods(class = "lm")
##  [1] add1           alias          anova
##  [4] case.names     coerce         confint
##  [7] cooks.distance deviance       dfbeta
## [10] dfbetas        drop1          dummy.coef
## [13] effects        extractAIC     family
## [16] formula        hatvalues      influence
## [19] initialize     kappa          labels
## [22] logLik         model.frame    model.matrix
## [25] nobs           plot           predict
## [28] print          proj           qr
## [31] residuals      rstandard      rstudent
## [34] show           simulate       slotsFromS3
## [37] summary        variable.names vcov
## see '?methods' for accessing help and source code
```

Often S3 classes inherit from lists (i.e., are special cases of lists), so you can obtain components of the object using the `$` operator.

**Creating our own class** We can create an object with a new class as follows:

```r
yog <- list(firstname = 'Yogi', surname = 'the Bear', age = 20)
class(yog) <- 'bear'
```

Actually, if we want to create a new class that we'll use again, we want to create a *constructor* function that initializes new bears:

```r
bear <- function(firstname = NA, surname = NA, age = NA){
  # constructor for 'indiv' class
  obj <- list(firstname = firstname, surname = surname,
              age = age)
  class(obj) <- 'bear'
  return(obj)
}
smoke <- bear('Smokey','Bear')
```

For those of you used to more formal OOP, the following is probably disconcerting:

```r
class(yog) <- "silly"
class(yog) <- "bear"
```

**Methods** The real power of OOP comes from defining methods. For example,

```r
mod <- lm(yc ~ x)
summary(mod)
gmod <- glm(yb ~ x, family = 'binomial')
summary(gmod)
```

Here `summary()` is a generic method (or generic function) that, based on the type of object given to it (the first argument), dispatches a class-specific function (method) that operates on the object. This is convenient for working with objects using familiar functions. Consider the generic methods `plot()`, `print()`, `summary()`, `[`, and others. We can look at a function and easily see that it is a generic method. We can also see what classes have methods for a given generic method.

```r
summary
## function (object, ...)
## UseMethod("summary")
## <bytecode: 0x556919f90cf8>
## <environment: namespace:base>

methods(summary)
##  [1] summary,ANY-method
##  [2] summary,DBIObject-method
##  [3] summary.aov
##  [4] summary.aovlist*
##  [5] summary.aspell*
##  [6] summary.check_packages_in_dir*
##  [7] summary.connection
##  [8] summary.data.frame
##  [9] summary.Date
## [10] summary.default
## [11] summary.ecdf*
## [12] summary.factor
## [13] summary.glm
## [14] summary.infl*
## [15] summary.lm
## [16] summary.loess*
## [17] summary.manova
## [18] summary.matrix
## [19] summary.mlm*
## [20] summary.nls*
## [21] summary.packageStatus*
## [22] summary.POSIXct
## [23] summary.POSIXlt
## [24] summary.ppr*
## [25] summary.prcomp*
## [26] summary.princomp*
## [27] summary.proc_time
## [28] summary.rlang_error*
## [29] summary.rlang_trace*
## [30] summary.srcfile
## [31] summary.srcref
## [32] summary.stepfun
## [33] summary.stl*
## [34] summary.table
## [35] summary.tukeysmooth*
## [36] summary.vctrs_sclr*
## [37] summary.vctrs_vctr*
## [38] summary.warnings
## see '?methods' for accessing help and source code
```

In many cases there will be a default method (here, `summary.default()`), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

We can define new generic methods:

```r
summarize <- function(object, ...)
  UseMethod("summarize")
```

Once `UseMethod()` is called, R searches for the specific method associated with the class of object and calls that method, without ever returning to the generic method. Let's try this out on our *bear* class. In reality, we'd write either `summary.bear()` or `print.bear()` (and of course the generics for summary and print already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I'll write a summarize method.

```r
summarize.bear <- function(object)
  return(with(object, cat("Bear of age ", age,
  " whose name is ", firstname, " ", surname, ".\n",
  sep = "")))

summarize(yog)
## Bear of age 20 whose name is Yogi the Bear.
```

**The print method** Like `summary()`, `print()` is a generic method, with various class-specific methods, such as `print.lm()`.

Note that the `print()` function is what is called when you simply type the name of the object, so we can have object information printed out in a structured way. Recall that the output when we type the name of an *lm* object is NOT simply a regurgitation of the elements of the list - rather `print.lm()` is called.

Similarly, when we used `print(object.size(x))` we were invoking the *object_size*-specific print method which gets the value of the size and then formats it. So there's actually a fair amount going on behind the scenes.

Surprisingly, the `summary()` method generally doesn't actually print out information; rather it computes things not stored in the original object and returns it as a new class (e.g., class *summary.lm*), which is then automatically printed, per my comment above, using `print.summary.lm()`, unless one assigns it to a new object. Note that `print.summary.lm()` is hidden from user view.

```r
out <- summary(mod)
out
print(out)
getS3method(f="print",class="summary.lm")
```

**More on inheritance** As noted with *lm* and *glm* objects, we can assign more than one class to an object. Here `summarize()` still works, even though the primary class is *grizzly_bear*.

```r
class(yog) <- c('grizzly_bear', 'bear')
summarize(yog)
## Bear of age 20 whose name is Yogi the Bear.
```

The classes should nest within one another with the more specific classes to the left, e.g., here a *grizzly_bear* would have some additional objects on top of those of a *bear*, perhaps *number_of_people_eaten* (since grizzly bears are much more dangerous than some other kinds of bears), and perhaps additional or modified methods. *grizzly_bear* inherits from *bear*, and R uses methods for the first class before methods for the next class(es), unless no such method is defined for the first class. If no methods are defined for any of the classes, R looks for `method.default()`, e.g., `print.default()`, `plot.default()`, etc..

**Why use class-specific methods?** We could have implemented different functionality (e.g., for `summary()`) for different objects using a bunch of `if` statements (or `switch()`) to figure out what class of object is the input, but then we need to have all that checking. Furthermore, we don't control the `summary()` function, so we would have no way of adding the additional conditions in a big if-else statement. The OOP framework makes things extensible, so we can build our own new functionality on what is already in R.

**Final thoughts** Consider the *Date* class discussed in the R bootcamp. This is another example of an S3 class, with methods such as `julian()`, `weekdays()`, etc.

**Challenge:** how would you get R to quit immediately, without asking for any more information, when you simply type 'k' (no parentheses!) instead of 'quit()'?

What we've just discussed are the old-style R (and S) object orientation, called S3 methods. An old, but somewhat newer style is called S4 and we'll discuss it next. S3 is still commonly used, in part because S4 can be slow. S4 is more structured than S3.

#### 4.4.2 S4 approach (optional)

S4 methods are used a lot in bioconductor, a project that provides a lot of bioinformatics-related code. They're also used in *lme4*, among other packages. Tools for working with S4 classes are in the *methods* package.

Note that components of S4 objects are obtained as `object@component` so they do not use the usual list syntax. The components are called *slots*, and there is careful checking that the slots are specified and valid when a new object of a class is created. You can use the `prototype` argument to `setClass()` to set default values for the slots. There is a default constructor (the method is actually called `initialize()`), but you can modify it. One can create methods for operators and for replacement functions too. For S4 classes, there is a default method invoked when `print()` is called on an object in the class (either explicitly or implicitly) - the method is actually called `show()` and it can also be modified. Let's reconsider our *bear* class example in the S4 context.

```r
library(methods)
setClass("bear",
    representation(
        name = "character",
        age = "numeric",
        birthday = "Date"
    )
)
yog <- new("bear", name = 'Yogi', age = 20,
           birthday = as.Date('91-08-03'))
## next notice the missing age slot
yog <- new("bear", name = 'Yogi',
           birthday = as.Date('91-08-03'))
## finally, apparently there's not a default object of class Date
yog <- new("bear", name = 'Yogi', age = 20)
## Error in validObject(.Object): invalid class "bear" object: invalid
object for slot "birthday" in class "bear": got class "S4", should
be or extend class "Date"

yog
## An object of class "bear"
## Slot "name":
## [1] "Yogi"
##
## Slot "age":
## numeric(0)
##
## Slot "birthday":
## [1] "91-08-03"

yog@age <- 60
```

S4 methods are designed to be more structured than S3, with careful checking of the slots.

```r
setValidity("bear",
    function(object) {
        if(!(object@age > 0 && object@age < 130))
            return("error: age must be between 0 and 130")
        if(length(grep("[0-9]", object@name)))
            return("error: name contains digits")
        return(TRUE)
        # what other validity check would make sense given the slots?
    }
)
## Class "bear" [in ".GlobalEnv"]
##
## Slots:
##
## Name:       name       age  birthday
## Class: character   numeric      Date

sam <- new("bear", name = "5z%a", age = 20,
           birthday = as.Date('91-08-03'))
## Error in validObject(.Object): invalid class "bear" object: error:
name contains digits

sam <- new("bear", name = "Z%a B''*", age = 20,
           birthday = as.Date('91-08-03'))
sam@age <- 150 # so our validity check is not foolproof
```

To deal with this latter issue of the user mucking with the slots, it's recommended when using OOP that slots only be accessible through methods that operate on the object, e.g., a `setAge()` method, and then check the validity of the supplied age within `setAge()`.

Here's how we create generic and class-specific methods. Note that in some cases the generic will already exist.

```r
## generic method
setGeneric("isVoter", function(object, ...) {
    standardGeneric("isVoter")
})
## [1] "isVoter"

# class-specific method
isVoter.bear <- function(object){
    if(object@age > 17){
        cat(object@name, "is of voting age.\n")
    } else cat(object@name, "is not of voting age.\n")
}
setMethod(isVoter, signature = c("bear"), definition = isVoter.bear)
isVoter(yog)
## Yogi is of voting age.
```

We can have method signatures involve multiple objects. Here's some syntax where we'd fill in the function body with appropriate code - perhaps the plus operator would create a child.

```r
setMethod(`+`, signature = c("bear", "bear"),
    definition = function(bear1, bear2) {
        ## method code goes here
    }
```

As with S3, classes can inherit from one or more other classes. Chambers calls the class that is being inherited from a *superclass*.

```r
setClass("grizzly_bear",
    representation(
        number_of_people_eaten = "numeric"
    ),
    contains = "bear"
)
sam <- new("grizzly_bear", name = "Sam", age = 20,
           birthday = as.Date('91-08-03'), number_of_people_eaten = 3)

isVoter(sam)
## Sam is of voting age.

is(sam, "bear")
## [1] TRUE
```

For a more relevant example suppose we had spatially-indexed time series. We could have a time series class, a spatial location class, and a "location time series" class that inherits from both. Be careful that there are not conflicts in the slots or methods from the multiple classes. For conflicting methods, you can define a method specific to the new class to deal with this. Also, if you define your own `initialize()` method, you'll need to be careful that you account for any initialization of the superclass(es) and for any classes that might inherit from your class (see help on `new()` and Chambers, p. 360).

You can inherit from other S4 classes (which need to be defined or imported into the environment in which your class is created), but not S3 classes. You can inherit (at most one) of the basic R types, but not environments, symbols, or other non-standard types. You can use S3 classes in slots, but this requires that the S3 class be declared as an S4 class. To do this, you create S4 versions of S3 classes use `setOldClass()` - this creates a virtual class. This has been done, for example, for the `data.frame` class:

```r
showClass("data.frame")
## Class "data.frame" [package "methods"]
##
## Slots:
##
## Name:                .Data     names
## Class:                list character
##
## Name:            row.names  .S3Class
## Class: data.frameRowLabels character
##
## Extends:
## Class "list", from data part
## Class "oldClass", directly
## Class "vector", by class "list", distance 2
```

You can use `setClassUnion()` to create what Adler calls superclass and what Chambers calls a virtual class that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a "named lifeform" virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can't directly create an object in the virtual class.

#### 4.4.3 R6 classes

R6 classes are a somewhat new construct in R. They are classes somewhat similar to S4. Importantly, they behave like pointers (the fields in the objects are 'mutable'). We'll discuss pointers in Section 6.5. Let's work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor.

Here's the initial definition of the class, with both public (user-facing) and private (internal use only) methods and fields.

```r
library(R6)

tsSimClass <- R6Class("tsSimClass",
    ## class for holding time series simulators
    public = list(
        initialize = function(times, mean = 0, corParam = 1){
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
        changeTimes = function(newTimes){
            private$times <- newTimes
            private$calcMats()
        },
        getTimes = function(){
            return(private$times)
        },
        print = function(){ # 'print' method
            cat("R6 Object of class 'tsSimClass' with ",
                private$n, " time points.\n", sep = '')
            invisible(self)
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

We can add methods after defining the class (but those methods wouldn't be accessible to objects of the class that have already been created.

```r
tsSimClass$set("public", "simulate", function() {
    if(!private$currentU)
        private$calcMats()
    ## analogous to mu+sigma*z for generating N(mu, sigma^2)
    return(private$mean + crossprod(private$U, rnorm(private$n)))
})
```

That's just for demonstration. In general we would define simulate when we define the class originally.

Now let's see how we would use the class.

```r
myts <- tsSimClass$new(1:100, 2, 1)
## Loading required package: spam
## Loading required package: dotCall64
## Loading required package: grid
## Spam version 2.6-0 (2020-12-14) is loaded.
## Type ’help( Spam)’ or ’demo( spam)’ for a short introduction
## and overview of this package.
## Help for individual functions is also obtained by adding the
## suffix ’.spam’ to the function name, e.g. ’help( chol.spam)’.
##
## Attaching package: ’spam’
## The following objects are masked from ’package:base’:
##
##     backsolve, forwardsolve
## Loading required package: viridis
## Loading required package: viridisLite
## See https://github.com/NCAR/Fields for
## an extensive vignette, other supplements and source code
## Done updating correlation matrix and Cholesky factor.

myts
## R6 Object of class 'tsSimClass' with 100 time points.

set.seed(1)
## here's a simulated time series
y <- myts$simulate()

plot(myts$getTimes(), y, type = 'l', xlab = 'time',
     ylab = 'process values')
## here's a second simulated time series
y2 <- myts$simulate()
lines(myts$getTimes(), y2, lty = 2)

myts2 <- tsSimClass$new(1:100, 2, 3)
## Done updating correlation matrix and Cholesky factor.

set.seed(1)
## here's a simulated time series with a different value of
## the correlation parameter (corParam)
y <- myts2$simulate()
lines(myts2$getTimes(), y, col = 'red')
```

## That simulated time series is less wiggly because the corParam value

---

[← 3 Packages and namespaces](03-3-packages-and-namespaces.md) · [Up: contents](index.md) · [is larger than before. →](05-is-larger-than-before.md)
