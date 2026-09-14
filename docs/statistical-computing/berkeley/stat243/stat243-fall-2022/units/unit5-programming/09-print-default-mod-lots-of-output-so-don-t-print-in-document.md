---
title: 'print.default(mod) ## lots of output, so don''t print in document...'
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# print.default(mod) ## lots of output, so don't print in document...

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```

```r
stats:::print.lm
```

Surprisingly, the *summary* method generally doesn't actually print
out information; rather it computes things not stored in the original
object and returns it as a new class (e.g., class *summary.lm*), which
is then automatically printed, per my comment above (e.g., using
*print.summary.lm*), unless one assigns it to a new object. Note that
*print.summary.lm* is hidden from user view (it's a private object in the *stats* namespace).

```r
out <- summary(mod)
class(out)
out
print(out)
## One can look at the code for the method (not shown):
## getS3method(f = "print", class = "summary.lm")
```

#### Inheritance

Let's look at the *lm* class, which builds on lists, and *glm* class,
which builds on the *lm* class. Here *mod* is an object (an instance) of
class *lm*.

```r
library(methods)
ybin <- sample(c(0, 1), 10, replace = TRUE)
ycont <- rnorm(10)
x <- rnorm(10)
mod1 <- lm(ycont ~ x)
mod2 <- glm(ybin ~ x, family = binomial)
class(mod1)
class(mod2)
is.list(mod1)
names(mod1)
is(mod2, "lm")
```

Here's an example of why this is useful. We don't have to define methods for
the *glm* class if the given method for the *lm* class would work fine:

```r
model.matrix(mod1)
model.matrix(mod2)
methods(model.matrix)
```

As noted with *lm* and *glm* objects, we can assign more than one class
to an object. Here *summarize* still works, even though the primary
class is *grizzly_bear*.

```r
class(yog) <- c('grizzly_bear', 'bear')
summarize(yog)
```

The classes should nest within one another with the more specific
classes to the left, e.g., here a *grizzly_bear* would have some
additional fields on top of those of a *bear*, perhaps
*number_of_people_killed* (since grizzly bears are much more dangerous
than some other kinds of bears), and perhaps additional or modified
methods. *grizzly_bear* inherits from *bear*, and R uses methods for the
first class before methods for the next class(es).

The above is an example of polymorphism. `yog` is a polymorphic object
and the various methods are polymorphic in that *print* can be used
with the *bear* class, the *grizzly_bear* class, and other classes beyond that.


> **Challenge**
> How would you get R to quit immediately, without asking for any more information, when you simply type `k` (no parentheses!) instead of `quit()`? (Hint: you can do this by understanding what happens when you type `k` and how to exploit the S3 system.)


### Multiple dispatch OOP

S3 method dispatch involves only the first argument to the function. In contrast, [Julia emphasizes the importance of multiple dispatch](https://docs.julialang.org/en/v1/manual/methods) as particularly important for mathematical computation. With multiple dispatch, the specific method can be chosen based on more than one argument.

The old (but still used in some contexts) [S4](http://adv-r.had.co.nz/S4.html) system in R and the (very) new [R7](https://rconsortium.github.io/OOP-WG) system both provide for multiple dispatch.

As a very simple example unrelated to any specific language, multiple dispatch would allow one to do the following with the addition operator:

```
3 + 7    # 10
3 + 'a'  # '3a'
'hi' +  ' there'  # 'hi there'
```

The idea of having the behavior of an operator or function adapt to the type of the input(s) is one aspect of *polymorphism*.

Both S4 and R7 are designed to be more formal than the S3 system (recall how we could just 'create' an S3 class by giving a class name to an existing list). With S4 and R7, you need to define your classes.

## 'Standard' OOP

What I'm calling 'standard' object-oriented programming is the style of OOP used in languages such as Python, C++, and Java. In R, one can use this style via the R6 system (or the older *referenceClass* system).

In this style, objects belong to classes. A class is made up of fields (the data objects) that store information and methods that operate on the fields. Thus, unlike generic function OOP, the verbs are part of the nouns.

We'll illustrate this style of OOP using an example with an R6 class.

### R6 classes

R6 classes are a somewhat new construct in R, with a class-based approach fairly similar to Python and C++. Importantly, they behave like pointers. We'll discuss pointers in detail later. Let's work through an example
where we set up the fields of the class and class
methods, including a constructor.

#### Example

Our example is to create a class for working with random time series. Each object of the class has specific parameter values that control the stochastic behavior of the time series. With a given object we can simulate one or more time series (realizations).

Here's the initial definition of the class, with both public
(user-facing) and private (internal use only) methods and fields.

```r

---

[← 6. Object-oriented programming (OOP)](08-6-object-oriented-programming-oop.md) · [Up: contents](index.md) · [suppress package-loading messages by loading here →](10-suppress-package-loading-messages-by-loading-here.md)
