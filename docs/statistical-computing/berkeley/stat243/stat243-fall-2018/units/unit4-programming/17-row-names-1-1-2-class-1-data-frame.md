---
title: '$names ## [1] "x" "y" ## ## $row.names ## [1] 1 2 ## ## $class ## [1] "data.frame"'
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# $names ## [1] "x" "y" ## ## $row.names ## [1] 1 2 ## ## $class ## [1] "data.frame"

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

15

**row.names** (mat) <- **c** ("first", "second") mat ## x y ## first 1 3 ## second 2 4 **attributes** (mat) ## $names ## [1] "x" "y" ## ## $row.names ## [1] "first" "second" ## ## $class ## [1] "data.frame" vec <- **c** (first = 7, second = 1, third = 5) vec['first'] ## first ## 7 **attributes** (vec) ## $names ## [1] "first" "second" "third"

### **4.3 Assignment and coercion**

We assign into an object using either ’ _=_ ’ or ’ _<-_ ’. A rule of thumb is that for basic assignments where you have an object name, then the assignment operator, and then some code, ’ _=_ ’ is fine, but otherwise use ’ _<-_ ’.

Let’s look at these examples to understand the distinction between ‘=’ and ‘<-’ when passing arguments to a function.

16

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x3a9e8c0> ## <environment: namespace:base> x <- 0; y <- 0 out <- **mean** (x = **c** (3,7)) _# usual way to pass an argument to a function ## what does the following do?_ out <- **mean** (x <- **c** (3,7)) _# this is allowable, though perhaps not useful_ out <- **mean** (y = **c** (3,7))

**## Error in mean.default(y = c(3, 7)): argument "x" is missing, with no default** out <- **mean** (y <- **c** (3,7))

What can you tell me about what is going on in each case above?

One situation in which you want to use ’ _<-_ ’ is if it is being used as part of an argument to a

function, so that R realizes you’re not indicating one of the function arguments, e.g.:

_## NOT OK, system.time() expects its argument to be a complete R expression:_ **system.time** (out = **rnorm** (10000))

**## Error in system.time(out = rnorm(10000)): unused argument (out = rnorm(10000))** _# OK:_ **system.time** (out <- **rnorm** (10000)) ## user system elapsed ## 0.000 0.000 0.001

Here’s another example:

mat <- **matrix** ( **c** (1, NA, 2, 3), nrow = 2, ncol = 2) **apply** (mat, 1, sum.isna <- **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) ## [1] 0 1

17

_## What is the side effect of what I have done just above?_ **apply** (mat, 1, sum.isna = **function** (vec) { **return** ( **sum** ( **is.na** (vec)))}) _# NOPE_

**## Error in match.fun(FUN): argument "FUN" is missing, with no default**

R often treats integers as numerics, but we can force R to store values as integers:

vals <- **c** (1, 2, 3) **class** (vals) ## [1] "numeric" vals <- 1:3 **class** (vals) ## [1] "integer" vals <- **c** (1L, 2L, 3L) vals ## [1] 1 2 3 **class** (vals) ## [1] "integer"

We convert between classes using variants on _as()_ : e.g.,

**as.character** ( **c** (1,2,3)) ## [1] "1" "2" "3" **as.numeric** ( **c** ("1", "2.73")) ## [1] 1.00 2.73 **as.factor** ( **c** ("a", "b", "c")) ## [1] a b c ## Levels: a b c

18

Some common conversions are converting numbers that are being interpreted as characters into actual numbers, converting between factors and characters, and converting between logical TRUE/FALSE vectors and numeric 1/0 vectors. In some cases R will automatically do conversions behind the scenes in a smart way (or occasionally not so smart way). We saw see implicit conversion (also called coercion) when we read in characters into R using _read.table()_ - strings are often automatically coerced to factors. Consider these examples of implicit coercion:

x <- **rnorm** (5) x[3] <- 'hat' _# What do you think is going to happen?_ indices <- **c** (1, 2.73) myVec <- 1:10 myVec[indices] ## [1] 1 2

Be careful of using factors as indices:

students <- **factor** ( **c** ("basic", "proficient", "advanced", "basic", "advanced", "minimal")) score <- **c** (minimal = 3, basic = 1, advanced = 13, proficient = 7) score["advanced"] ## advanced ## 13 score[students[3]] ## minimal ## 3 score[ **as.character** (students[3])] ## advanced ## 13

What has gone wrong and how does it relate to type coercion?

In other languages, converting between different classes is sometimes called _casting_ a variable. Here’s an example we can work through that will help illustrate how type conversions occur behind the scenes in R.

19

n <- 5 df <- **data.frame** ( **rep** ('a', n), **rnorm** (n), **rnorm** (n)) **apply** (df, 1, **function** (x) x[2] + x[3]) **## Error in x[2] + x[3]: non-numeric argument to binary operator** _## why does that not work?_ **apply** (df[ , 2:3], 1, **function** (x) x[1] + x[2]) ## [1] 1.586 1.259 0.467 -0.508 1.971 _## let's look at apply() to better understand what is happening_

### **4.4 Object-oriented programming**

Popular languages that use OOP include C++, Java, and Python. In fact C++ is the object-oriented version of C. Different languages implement OOP in different ways.

The idea of OOP is that all operations are built around objects, which have a class, and methods that operate on objects in the class. Classes are constructed to build on (inherit from) each other, so that one class may be a specialized form of another class, extending the components and methods of the simpler class (e.g., _lm_ and _glm_ objects).

Note that in more formal OOP languages, all functions are associated with a class, while in R, only some are.

Often when you get to the point of developing OOP code in R, you’re doing more serious programming, and you’re going to be acting as a software engineer. It’s a good idea to think carefully in advance about the design of the classes and methods.

#### **4.4.1 S3 approach**

S3 classes are widely-used, in particular for statistical models in the _stats_ package. S3 classes are very informal in that there’s not a formal definition for an S3 class. Instead, an S3 object is just a primitive R object such as a list or vector with additional attributes including a class name.

**Inheritance** Let’s look at the _lm_ class, which builds on lists, and _glm_ class, which builds on the _lm_ class. Here _mod_ is an object (an instance) of class _lm_ . An analogy is the difference between a random variable and a realization of that random variable.

20

**library** (methods) yb <- **sample** ( **c** (0, 1), 10, replace = TRUE) yc <- **rnorm** (10) x <- **rnorm** (10) mod1 <- **lm** (yc ~ x) mod2 <- **glm** (yb ~ x, family = binomial) **class** (mod1) ## [1] "lm" **class** (mod2) ## [1] "glm" "lm" **is.list** (mod1) ## [1] TRUE **names** (mod1) ## [1] "coefficients" "residuals" "effects" ## [4] "rank" "fitted.values" "assign" ## [7] "qr" "df.residual" "xlevels" ## [10] "call" "terms" "model" **is** (mod2, "lm") ## [1] TRUE **methods** (class = "lm") ## [1] add1 alias anova ## [4] case.names coerce confint ## [7] cooks.distance deviance dfbeta ## [10] dfbetas drop1 dummy.coef ## [13] effects extractAIC family ## [16] formula hatvalues influence ## [19] initialize kappa labels ## [22] logLik model.frame model.matrix

21

---

[← Unit 04 — programming Part 16 —](16-unit-04-programming-part-16.md) · [Up: contents](index.md) · [Unit 04 — programming Part 18 — →](18-unit-04-programming-part-18.md)
