---
title: Unit 04 — programming Part 20 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 20 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

We convert between classes using variants on _as()_ : e.g.,

**as.character** ( **c** (1,2,3)) ## [1] "1" "2" "3" **as.numeric** ( **c** ("1", "2.73")) ## [1] 1.00 2.73 **as.factor** ( **c** ("a", "b", "c")) ## [1] a b c ## Levels: a b c

Some common conversions are converting numbers that are being interpreted as characters into actual numbers, converting between factors and characters, and converting between logical TRUE/FALSE vectors and numeric 1/0 vectors. In some cases R will automatically do conversions behind the scenes in a smart way (or occasionally not so smart way). We saw see implicit conversion (also called coercion) when we read in characters into R using _read.table()_ - strings are often automatically coerced to factors. Consider these examples of implicit coercion:

18

x <- **rnorm** (5) x[3] <- 'hat' _# What do you think is going to happen?_ indices <- **c** (1, 2.73) myVec <- 1:10 myVec[indices] ## [1] 1 2 _## @knitr factor-indices_ students <- **factor** ( **c** ("basic", "proficient", "advanced", "basic", "advanced", "minimal")) score <- **c** (minimal = 3, basic = 1, advanced = 13, proficient = 7) score["advanced"] ## advanced ## 13 score[students[3]] ## minimal ## 3 score[ **as.character** (students[3])] ## advanced ## 13

Be careful of using factors as indices:

What has gone wrong and how does it relate to type coercion?

In other languages, converting between different classes is sometimes called _casting_ a variable. Here’s an example we can work through that will help illustrate how type conversions occur behind the scenes in R.

n <- 5 df <- **data.frame** ( **rep** ('a', n), **rnorm** (n), **rnorm** (n)) **apply** (df, 1, **function** (x) x[2] + x[3]) **## Error in x[2] + x[3]: non-numeric argument to binary operator**

19

_# why does that not work?_ **apply** (df[ , 2:3], 1, **function** (x) x[1] + x[2]) ## [1] -0.50953 0.19547 1.80938 0.74519 0.00208 _## let's look at apply() to better understand what is happening_

### **4.4 Object-oriented programming**

Popular languages that use OOP include C++, Java, and Python. In fact C++ is the object-oriented version of C. Different languages implement OOP in different ways.

The idea of OOP is that all operations are built around objects, which have a class, and methods that operate on objects in the class. Classes are constructed to build on (inherit from) each other, so that one class may be a specialized form of another class, extending the components and methods of the simpler class (e.g., _lm_ and _glm_ objects).

Note that in more formal OOP languages, all functions are associated with a class, while in R, only some are.

Often when you get to the point of developing OOP code in R, you’re doing more serious programming, and you’re going to be acting as a software engineer. It’s a good idea to think carefully in advance about the design of the classes and methods.

#### **4.4.1 S3 approach**

S3 classes are widely-used, in particular for statistical models in the _stats_ package. S3 classes are very informal in that there’s not a formal definition for an S3 class. Instead, an S3 object is just a primitive R object such as a list or vector with additional attributes including a class name.

**Inheritance** Let’s look at the _lm_ class, which builds on lists, and _glm_ class, which builds on the _lm_ class. Here _mod_ is an object (an instance) of class _lm_ . An analogy is the difference between a random variable and a realization of that random variable.

**library** (methods) yb <- **sample** ( **c** (0, 1), 10, replace = TRUE) yc <- **rnorm** (10) x <- **rnorm** (10) mod1 <- **lm** (yc ~ x) mod2 <- **glm** (yb ~ x, family = binomial)

20

**class** (mod1) ## [1] "lm" **class** (mod2) ## [1] "glm" "lm" **is.list** (mod1) ## [1] TRUE **names** (mod1) ## [1] "coefficients" "residuals" "effects" ## [4] "rank" "fitted.values" "assign" ## [7] "qr" "df.residual" "xlevels" ## [10] "call" "terms" "model" **is** (mod2, "lm") ## [1] TRUE **methods** (class = "lm") ## [1] add1 alias anova ## [4] case.names coerce confint ## [7] cooks.distance deviance dfbeta ## [10] dfbetas drop1 dummy.coef ## [13] effects extractAIC family ## [16] formula hatvalues influence ## [19] initialize kappa labels ## [22] logLik model.frame model.matrix ## [25] nobs plot predict ## [28] print proj qr ## [31] residuals rstandard rstudent ## [34] show simulate slotsFromS3 ## [37] summary variable.names vcov ## see '?methods' for accessing help and source code

21

Often S3 classes inherit from lists (i.e., are special cases of lists), so you can obtain components of the object using the $ operator.

**Creating our own class** We can create an object with a new class as follows: yog <- **list** (firstname = 'Yogi', surname = 'the Bear', age = 20) **class** (yog) <- 'bear'

Actually, if we want to create a new class that we’ll use again, we want to create a _constructor_ function that initializes new bears:

bear <- **function** (firstname = NA, surname = NA, age = NA){ _# constructor for 'indiv' class_ obj <- **list** (firstname = firstname, surname = surname, age = age) **class** (obj) <- 'indiv' **return** (obj) } smoke <- **bear** ('Smokey','Bear')

For those of you used to more formal OOP, the following is probably disconcerting:

**class** (yog) <- "silly" **class** (yog) <- "bear"

**Methods** The real power of OOP comes from defining _methods_ . For example,

mod <- **lm** (yc ~ x) **summary** (mod) gmod <- **glm** (yb ~ x, family = 'binomial') **summary** (gmod)

Here _summary()_ is a generic method (or generic function) that, based on the type of object given to it (the first argument), dispatches a class-specific function (method) that operates on the object. This is convenient for working with objects using familiar functions. Consider the generic methods _plot()_ , _print()_ , _summary()_ , _‘[‘_ , and others. We can look at a function and easily see that it is a generic method. We can also see what classes have methods for a given generic method.

22

mean ## function (x, ...) ## UseMethod("mean") ## <bytecode: 0x4d026a0> ## <environment: namespace:base> **methods** (mean) ## [1] mean.Date mean.default mean.difftime ## [4] mean.POSIXct mean.POSIXlt ## see '?methods' for accessing help and source code

In many cases there will be a default method (here, _mean.default()_ ), so if no method is defined for the class, R uses the default. Sidenote: arguments to a generic method are passed along to the selected method by passing along the calling environment.

We can define new generic methods:

summarize <- **function** (object, ...) **UseMethod** ("summarize")

Once _UseMethod()_ is called, R searches for the specific method associated with the class of _object_ and calls that method, without ever returning to the generic method. Let’s try this out on our _indiv_ class. In reality, we’d write either _summary.indiv()_ or _print.indiv()_ (and of course the generics for _summary_ and _print_ already exist) but for illustration, I wanted to show how we would write both the generic and the specific method, so I’ll write a _summarize_ method.

summarize.bear <- **function** (object) **return** ( **with** (object, **cat** ("Bear of age ", age, " whose name is ", firstname, " ", surname, ".\n", sep = ""))) **summarize** (yog) ## Bear of age 20 whose name is Yogi the Bear.

Note that the _print()_ function is what is called when you simply type the name of the object, so we can have object information printed out in a structured way. Recall that the output when we type the name of an _lm_ object is NOT simply a regurgitation of the elements of the list - rather _print.lm()_ is called.

23

Similarly, when we used print(object.size(x)) we were invoking the _object_size_ - specific print method which gets the value of the size and then formats it. So there’s actually a fair amount going on behind the scenes.

Surprisingly, the _summary()_ method generally doesn’t actually print out information; rather it computes things not stored in the original object and returns it as a new class (e.g., class _summary.lm_ ), which is then automatically printed, per my comment above, using _print.summary.lm()_ , unless one assigns it to a new object. Note that _print.summary.lm()_ is hidden from user view.

out <- **summary** (mod) out **print** (out) **getS3method** (f="print",class="summary.lm")

**More on inheritance** As noted with _lm_ and _glm_ objects, we can assign more than one class to an object. Here _summarize()_ still works, even though the primary class is _grizzly_bear_ .

**class** (yog) <- **c** ('grizzly_bear', 'bear') **summarize** (yog)

---

[← Unit 04 — programming Part 19 —](19-unit-04-programming-part-19.md) · [Up: contents](index.md) · [Bear of age 20 whose name is Yogi the Bear. →](21-bear-of-age-20-whose-name-is-yogi-the-bear.md)
