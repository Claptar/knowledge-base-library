---
title: 6. Object-oriented programming (OOP)
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 6. Object-oriented programming (OOP)

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Principles

Some of the standard concepts in object-oriented programming include *encapsulation*, *inheritance*, *polymorphism*, and *abstraction*.

*Encapsulation* involves preventing direct access to internal data in an object from outside the object. Instead the class is designed so that access (reading or writing) happens through the interface set up by the programmer (e.g., 'getter' and 'setter' methods). We'll see this in our R6 class example below.

*Inheritance* allows one class to be based on another class, adding more specialized features. An example in R's S3 system is that the *glm* class inherits from the *lm* class.

*Polymorphism* allows for different behavior of an object or function depending on the context. A polymorphic function behaves differently depending on the input types. A polymorphic object is one that can belong to different classes (e.g., based on inheritance), and a given method name can be used with any of the classes. An example would be having a base or super class called 'algorithm' and various specific machine learning algorithms inheriting from that class. All of the classes might have a 'predict' method.

*Abstraction* involves hiding the details of how something is done (e.g., via the method of a class), giving the user an interface to provide inputs and get outputs. By making the actual computation a black box, the programmer can modify the internals without changing how a user uses the system.

Classes generally have *constructors* that initialize objects of the class and *destructors* that remove objects.


## Generic function OOP

Much of the object-oriented programming in R uses *generic function OOP*, also known as *functional OOP*.
In this style, classes don't have methods. Instead there are *generic functions* (also known as *generic methods*) that change their behavior based on the type of the input(s). Another way to put it is that the nouns and the verbs are separate, unliked in standard OOP.

The use of generic functions is similar in spirit to function or method *overloading* in C++ and Java.

Generic function OOP  is how the (very) old S3 system in R works. It's also a key part of the (fairly) new Julia language.

### S3 classes in R

S3 classes are widely-used, in particular for statistical models in the
*stats* package. S3 classes are very informal in that there's not a
formal definition for an S3 class. Instead, an S3 object is just a
primitive R object such as a list or vector with additional attributes
including a class name.

#### Creating our own class

We can create an object with a new class as follows:

```r
yog <- list(firstname = 'Yogi', surname = 'the Bear', age = 20)
class(yog) <- 'bear'
```

Actually, if we want to create a new class that we'll use again, we want
to create a *constructor* function that initializes new bears:

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

For those of you used to more formal OOP, the following is probably
disconcerting:

```r
class(smoke) <- "celebrity"
```

Generally S3 classes inherit from lists (i.e., are special cases of lists),
so you can obtain components of the object using the \$ operator.

#### Generic methods

The real power of the S3 system comes from defining *class-specific methods*. For example,

```r
x <- rnorm(10)
summary(x)

y <- rnorm(10)
mod <- lm(y ~ x)
summary(mod)
```

Here *summary* is a generic function (or generic method) that, based
on the type of object given to it (the first argument), dispatches a
class-specific function (method) that operates on the object.

The above is equivalent to directly calling the class-specific methods:

```r
identical(summary(x), summary.default(x))
identical(summary(mod), summary.lm(mod))
```


This use of generic functions is convenient in that it allows us to work with a variety of kinds of objects using familiar functions. Consider
the generic methods *plot*, *print*, *summary*, *\[*, and
others. We can look at a function and easily see that it is a generic
method.

```r
summary
```

The `UseMethod` syntax is what causes the dispatching of the class-specific method
associated with `object` and calls that method.
In many cases there will be a default method (here,
*summary.default*), so if no method is defined for the class, R uses
the default. Sidenote: arguments to a generic method are passed along to
the selected method by passing along the calling environment.

We can also see what classes have methods for a given generic
function.

```r
methods(summary)
```

Or from a different angle we can see what specific methods are available for a given class.

```r
methods(class = 'lm')
```

Let's try this functionality  out on our *bear* class.

```r
summary.bear <- function(object)
    with(object, cat("Bear of age ", age,
	" whose name is ", firstname, " ", surname, ".\n",
        sep = ""))
    invisible(NULL)

summary(yog)
```

We can also define a new generic function.

Let's do this for the *bear* class as an illustration, though this won't
provide any functionality beyond what we did with *summary*

```r
summarize <- function(object, ...)
	UseMethod("summarize")
```

```r
summarize.bear <- function(object)
    with(object, cat("Bear of age ", age,
	" whose name is ", firstname, " ", surname, ".\n",
        sep = ""))
    invisible(NULL)

summarize(yog)
```

#### Why use generic functions?

We could have written *summary* as a regular function with a bunch of if statements or if-else clauses (or *switch*) so that it can handle different kinds of input objects.

This has two disadvantages:

  1. We need to write the code that does the checking (and all the code for the different cases all lives inside one potentially very long function, unless we create class-specific helper functions).
  2. Much more importantly, *summary* will only work for existing classes. And users can't easily extend it for new classes that they create because they don't control the *summary* function. So a user could not add the additional conditions/classes in a big if-else statement. The generic function approach makes the system *extensible* -- we can build our own new functionality on what is already in R. For example, we could have written *summary.bear*.

#### The print method

Like *summary*, *print* is a generic method, with various
class-specific methods, such as *print.lm*. We could write our own
*print.bear* specific method.

Note that the *print* function is what is called when you simply type
the name of the object, so we can have object information printed out in
a structured way. Thus, the output when we type the name of an
*lm* object is NOT simply a regurgitation of the elements of the list -
rather *print.lm* is called.

```r
mod
print(mod)
stats:::print.lm(mod)  ## print.lm is private to the stats namespace

---

[← 5. Programming paradigms: object-oriented and functional programming](07-5-programming-paradigms-object-oriented-and-functional-progr.md) · [Up: contents](index.md) · [print.default(mod) ## lots of output, so don't print in document... →](09-print-default-mod-lots-of-output-so-don-t-print-in-document.md)
