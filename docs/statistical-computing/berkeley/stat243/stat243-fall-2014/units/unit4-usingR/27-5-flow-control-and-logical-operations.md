---
title: 5 Flow control and logical operations
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Flow control and logical operations

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **5.1 Logical operators**

Everyone should be familiar with the comparison operators, _<_ **_,_** _<=_ **_,_** _>_ **_,_** _>=_ **_,_** _==_ **_,_** _!=_ . Logical operators are slightly trickier:

**Logical operators for vectors and subsetting** _&_ and _|_ are the “AND” and “OR” operators used when subsetting - they act in a vectorized way:

x <- **rnorm** (10) x[x > 1 | x < -1] ## [1] -1.46 -1.35 -2.07 -1.34 x <- 1:10 y <- **c** ( **rep** (10, 9), NA) x > 5 | y > 5 _# note that TRUE | NA evaluates to TRUE_ ## [1] TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE TRUE

**Logical operators for** **_if_ statements** _&&_ and _||_ use only the first element of a vector and also proceed from left to right, returning the result as soon as possible and then ignoring the remaining comparisons (this can be handy because in some cases the second condition may give an error if the first condition is not passed). They are used in flow control (i.e., with _if_ statements). Let’s consider how the single and double operators differ:

33

a <- 7 b <- **NULL** a < 8 | b > 3 ## logical(0) a < 8 || b > 3 ## [1] TRUE a <- **c** (0, 3) b <- **c** (4, 2) **if** (a < 7 & b < 7) **print** ("this is buggy code") ## Warning: the condition has length > 1 and only the first element will be used ## [1] "this is buggy code"

**if** (a < 7 && b < 7) **print** ("this is buggy code too, but runs w/o warnings") ## [1] "this is buggy code too, but runs w/o warnings"

**if** (a[1] < 7 && b[1] < 7) **print** ("this code is correct and the condition is ## [1] "this code is correct and the condition is TRUE"

You can use ! to indicate negation:

a <- 7 b <- 5 !(a < 8 & b < 6) ## [1] FALSE

### **5.2 If statements**

If statements are at the core of programming. In R, the syntax is if(condition) statement else other_statement, e.g.,

34

x <- 5 **if** (x > 7) { x <- x + 3 } **else** { x <- x - 3 }

When one of the statements is a single statement, you don’t need the curly braces around that statement.

**<mark>if</mark>** <mark>(x > 7) x <- x + 3</mark> **<mark>else</mark>** <mark>x <- x - 3</mark>

An extension of _if_ looks like:

x <- -3 **if** (x > 7) { x <- x + 3 **print** (x) } **else if** (x > 4) { x <- x + 1 **print** (x) } **else if** (x > 0) { x <- x - 3 **print** (x) } **else** { x <- x - 7 **print** (x) } ## [1] -10

Finally, be careful that _else_ should not start its own line, unless it is preceded by a closing brace on the same line. Why?

if(x > 7) { statement1 } # what happens at this point? else{ # what happens now? statement2 }

35

There’s also the _ifelse()_ function, which operates in a vectorized fashion:

x <- **rnorm** (6) truncx <- **ifelse** (x > 0, x, 0) truncx ## [1] 0.000 0.000 0.000 0.769 1.698 0.000

Common bugs in the condition of an if statement include the following:

1. Only the first element of _condition_ is evaluated. You should be careful that _condition_ is a single logical value and does not evaluate to a vector as this would generally be a bug. [see p. 152 of Chambers]

2. Use _identical()_ or _all.equal()_ rather than “ _==_ ” to ensure that you deal properly with vectors and always get a single logical value back. We’ll talk more about issues that can arise when comparing decimal numbers on a computer later in the course.

3. If _condition_ includes some R code, it can fail and produce something that is neither TRUE nor FALSE. Defensive programming practice is to check the condition for validity.

vals <- **c** (1, 2, NA); eps <- 1e-9

_# now pretend vals comes from some other chunk of code that we don't_

**if** ( **min** (vals) > eps) _# not good practice_

{ **print** (vals) }

**## Error: missing value where TRUE/FALSE needed**

_# better practice:_ minval <- **min** (vals) **if** (! **is.na** (minval) && minval > eps) { **print** (vals) }

36

### **5.3 switch()**

_switch()_ is handy for choosing amongst multiple outcomes depending on an input, avoiding a long set of if-else syntax. The first argument is a statement that determines what choice is made and the second is a list of the outcomes, in order or by name:

x <- 2; y <- 10 **switch** (x, **log** (y), **sqrt** (y), y) ## [1] 3.16 center <- **function** (x, type){ **switch** (type, mean = **mean** (x), _# make sure to use = and not <-_ median = **median** (x), trimmed = **mean** (x, trim = .1)) } x <- **rgamma** (100, 1) **center** (x, 'median') ## [1] 0.628 **center** (x, 'mean') ## [1] 0.915

### **5.4 Loops**

Loops are at the core of programming in other functional languages, but in R, we often try to avoid them as they’re often (but not always) slow. In many cases looping can be avoided by using vectorized calculations, versions of _apply()_ , and other tricks. But sometimes they’re unavoidable and for quick and dirty coding and small problems, they’re fine. And in some cases they may be faster than other alternatives. One case we’ve already seen is that in working with lists they may be faster than their _lapply_ -style counterpart, though often they will not be.

The workhorse loop is the _for_ loop, which as the syntax: for(var in sequence) statement, where, as with the _if_ statement, we need curly braces around the body of the loop if it contains more than one valid R statement:

37

nIts <- 500 means <- **rep** (NA, nIts) **for** (it **in** 1:nIts) { means[it] <- **mean** ( **rnorm** (100)) **if** ( **identical** (it%%100, 0)) **cat** ("Iteration", it, **date** (), "\n") } ## Iteration 100 Sat Sep 13 14:42:48 2014 ## Iteration 200 Sat Sep 13 14:42:48 2014 ## Iteration 300 Sat Sep 13 14:42:48 2014 ## Iteration 400 Sat Sep 13 14:42:48 2014 ## Iteration 500 Sat Sep 13 14:42:48 2014

Challenge: how do I do this much faster?

You can also loop over a non-numeric vector of values.

**for** (state **in c** ("Ohio", "Iowa", "Georgia")) { sub <- **row.names** (state.x77) == state **print** (state.x77[sub, "Income"]) } ## [1] 4561 ## [1] 4628 ## [1] 4091

Challenge: how can I do this faster?

Note that to print to the screen in a loop you explicitly need to use _print()_ or _cat()_ ; just writing the name of the object will not work. This is similar to _if_ statements and functions.

**<mark>for</mark>** <mark>(i</mark> **<mark>in</mark>** <mark>1:10) i</mark>

You can use the commands _break_ (to end the looping) and _next_ (to go to the next iteration) to control the flow:

**for** (i **in** 1:10) { **if** (i == 5) **break**

38

**print** (i) } ## [1] 1 ## [1] 2 ## [1] 3 ## [1] 4 **for** (i **in** 1:5) { **if** (i == 2) **next print** (i) } ## [1] 1 ## [1] 3 ## [1] 4 ## [1] 5

_while_ loops are used less frequently, but can be handy: while(condition) statement, e.g. in optimization. See p. 59 of Venables and Ripley, 4th ed., whose code I’ve included in the demo code file.

A common cause of bugs in for loops is when the range ends at zero or a missing value:

mat <- **matrix** (1:4, 2) submat <- mat[mat[1, ] > 5] **for** (i **in** 1: **nrow** (submat)) **print** (i) **## Error: argument of length 0**

---

[← Unit 04 — usingR Part 26 —](26-unit-04-usingr-part-26.md) · [Up: contents](index.md) · [6 Formulas →](28-6-formulas.md)
