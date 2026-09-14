---
title: 4. Types and data structures
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 4. Types and data structures

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

## Data structures

Please see the [data structures section of Unit 2](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit2-dataTech.html#data-structures) for some general discussion of data structures.

We'll also see more complicated data structures when we consider objects in the next section on object-oriented programming.


## Types and classes

### Overview and static vs. dynamic typing

The term 'type' refers to how a given piece of information is stored and what operations can be done with the information.
'Primitive' types are the most basic types that often relate directly to how data are stored in memory or on disk (e.g., boolean, integer, numeric (real-valued, aka *double* or *floating point*), character, pointer (aka *address*, *reference*).

In compiled languages like C and C++, one has to define the type of each variable. Such languages are *statically* typed.
Interpreted (or scripting) languages such as Python and R have *dynamic* types. One can associate different types of information with a given variable name at different times and without declaring the type of the variable:

```r
x <- 'hello'
print(x)
x <- 7
x*3
```

In contrast in a language like C, one has to declare a variable based on its type before using it:

```
double y;
double x = 3.1;
y = x * 7.1;
```

Dynamic typing can be quite helpful from the perspective of quick implementation and avoiding tedious type definitions and problems from minor inconsistencies between types (e.g., multiplying an integer by a real-valued number).
But static typing has some critical advantages from the perspective of software development, including:

  - protecting against errors from mismatched values and unexpected user inputs, and
  - generally much faster execution because the type of a variable does not need to be checked when the code is run.

More complex types in R (and in Python) often use references (*pointers*, aka *addresses*) to the actual locations of the data. We'll see this in detail later in the Unit.

### Types and classes in R

You should be familiar with vectors as the basic data structure in R,
with character, integer, numeric, etc. classes. Vectors are either
*atomic vectors* or *lists*. Atomic vectors generally contain one of the
four following types: *logical*, *integer*, *double* (i.e., *numeric*), and
*character*.

Everything in R is an object and all objects have a class. For simple
objects class and type are often closely related, but this is not the
case for more complicated objects. As we'll see later in the Unit, the class describes what the object
contains and standard functions associated with it. In general, you
mainly need to know what class an object is rather than its type.

> **Note**
> You can look at Table 7.1 in the Adler book to see some other types.

Let's look at the type and class of various data structures in R.
We'll first see that real-valued are stored as double-precision (8 byte) floating point numbers
internally in R (as 'doubles' in C, as the R interpreter is a program written in C).

```r
devs <- rnorm(5)
class(devs)
typeof(devs)
a <- data.frame(x = 1:2)
class(a)
typeof(a)
is.data.frame(a)
is.matrix(a)
is(a, "matrix")
m <- matrix(1:4, nrow = 2)
class(m)
typeof(m)
```

In most cases integer-valued numbers are stored as numeric values in R, but there are exceptions such as the result of using the
sequence operater, `:`, above. We can force R to store values
as integers:

```r
vals <- c(1, 2, 3)
class(vals)
vals <- 1:3
class(vals)
vals <- c(1L, 2L, 3L)
vals
class(vals)
```


### Attributes

We saw the notion of attributes when looking at HTML and XML, where the information was stored as
key-value pairs that in many cases had additional information in the form of attributes.

In R, *attributes* are information about an object attached to an object as
something that looks like a named list. Attributes are often copied when
operating on an object. This can lead to some weird-looking formatting when
in subsequent operations the *names* attribute is carried along:

```r
x <- rnorm(10 * 365)
attributes(x)
qs <- quantile(x, c(.025, .975))
attributes(qs)
qs
qs[1] + 3
object.size(qs)
```

We can get rid of the attribute:

```r
names(qs) <- NULL
qs
object.size(qs)
```

A common use of attributes is that rows and columns may be named in
matrices and data frames, and elements in vectors:

```r
df <- data.frame(x = 1:2, y = 3:4)
attributes(df)
row.names(df) <- c("first", "second")
df
attributes(df)
vec <- c(first = 7, second = 1, third = 5)
vec['first']
attributes(vec)
```

### Converting between types

This also goes by the term *coercion* and *casting*.
Casting often needs to be done explicitly in compiled languages and somewhat less so in interpreted languages like R.

We convert between classes using variants on *as*: e.g.,

```r
as.character(c(1,2,3))
as.numeric(c("1", "2.73"))
as.factor(c("a", "b", "c"))
```

Some common conversions are converting numbers that are being
interpreted as characters into actual numbers, converting between
factors and characters, and converting between logical TRUE/FALSE
vectors and numeric 1/0 vectors.

In some cases R will automatically do
conversions behind the scenes in a smart way (or occasionally not so
smart way). Consider these examples of implicit coercion:

```r
x <- rnorm(5)
x[3] <- 'hat' # What do you think is going to happen?
indices <- c(1, 2.73)
myVec <- 1:10
myVec[indices]
```

Here's an example we can work through that will help illustrate how type
conversions occur behind the scenes in R.

```r
n <- 5
df <- data.frame(label = rep('a', n), val1 = rnorm(n), val2 = rnorm(n))
df
## Why does the following not work?
try( apply(df, 1, function(x) x[2] + x[3]) )
## Instead, this will work. Why?
apply(df[ , 2:3], 1, function(x) x[1] + x[2])
```

Be careful of using factors as indices:

```r
students <- factor(c("basic", "proficient", "advanced",
                     "basic", "advanced", "minimal"))
score <- c(minimal = 65, basic = 75, proficient = 85, advanced = 95)
score["advanced"]
students[3]
score[students[3]]
score[as.character(students[3])]
```

What has gone wrong and how does it relate to type coercion?


## Data frames and related concepts

### Some notes on data frames and operations on data frames

Base R provides a variety of functions for manipulating data frames, but
now many researchers use add-on packages (many written by Hadley Wickham
as part of a group of packages called the *tidyverse*) to do these
manipulations in a more elegant way. [Module 6 of the R bootcamp](https://https://berkeley-scf.github.io/r-bootcamp-fall-2022/modules/module6_tidyverse) describes some of these new tools in more details, but I'll touch on some aspects of this here, without showing much of the tidyverse syntax.

### split-apply-combine

Often analyses are done in a stratified fashion - the same operation or
analysis is done on subsets of the data set. The subsets might be
different time points, different locations, different hospitals,
different people, etc.

The split-apply-combine framework is intended to operate in this kind of
context: first one splits the dataset by one or more variables, then one
does something to each subset, and then one combines the results. The
*dplyr* package implements this framework (as does the *pandas* package
for Python). One can also do similar operations using various flavors of
the *lapply* family of functions such as *by*, *tapply*, and
*aggregate*, but the dplyr-based tools are often nicer to use.

split-apply-combine is also closely related to the famous Map-Reduce framework
underlying big data tools such as Hadoop and Spark.

It's also very similar to standard SQL queries involving filtering, grouping, and
aggregation.

### Long and wide formats

Finally, we may want to convert between so-called 'long' and 'wide'
formats, which we can motivate in the context of longitudinal data
(multiple observations per subject) and panel data (temporal data for
each of multiple units such as in econometrics). The wide format has
repeated measurements for a subject in separate columns, while the long
format has repeated measurements in separate rows, with a column for
differentiating the repeated measurements.

```r
long <- data.frame(id = c(1, 1, 1, 2, 2, 2),
                   time = c(1980, 1990, 2000, 1980, 1990, 2000),
                   value = c(5, 8, 9, 7, 4, 7))
wide <- data.frame(id = c(1, 2),
                   value_1980 = c(5, 7), value_1990 = c(8, 4), value_2000 = c(9, 7))
long
wide
```

The wide format can be useful in some situations for treating each row as a (multivariate observation),
but the long formatwhile the long format is often what is needed for analyses such as
mixed models. ANOVA, or for plotting, such as with *ggplot2*.

There are a variety of functions for converting between wide and long
formats. I recommend *pivot_longer* and *pivot_wider* in the *tidyr* package. There are also older *tidyr* functions
called *gather* and *spread*. There are also the *melt* and
*cast* in the *reshape2* package. These are easier to use than the
functions in base R such as *reshape* or *stack* and *unstack*
functions*.*

### Piping

Piping was introduced into R in conjuction with *dplyr* and the *tidyverse*.

The tidyverse pipe is `%>%` while the new base R pipe is `|>`.
These are based on the UNIX pipe, which we saw in Unit 3, though
they behave somewhat differently in that the output of the previous function
is passed in as the *first* argument of the next function. In the shell,
the pipe connects *stdout* from the previous command to *stdin* for the next command.


### Non-standard evaluation and the tidyverse

Many tidyverse packages use non-standard evaluation to make it easier to
code. For example in the following dplyr example, you can refer directly
to *country* and *unemp*, which are variables in the data frame, without
using `data$country` or `data$unemp` and without using quotes around the
variable names, as in `"country"` or `"unemp"`. Referring directly to
the variables in the data frame is not standard R usage, hence the term
"non-standard evaluation". One reason it is not standard is that *country*
and *unemp* are not themselves independent R variables so R can't find
them in the usual way using scoping (discussed later in the Unit).

```r
library(dplyr)
cpds <- read.csv(file.path('..', 'data', 'cpds.csv'))

cpds2 <- cpds %>% group_by(country) %>%
                  mutate(mean_unemp = mean(unemp))

head(cpds2)
```


This 'magic' is done by capturing the code expression you write and
evaluating it in a special way in the context of the data frame. I
believe this uses R's environment class (discussed later in the Unit), but
haven't looked more deeply.

While this has benefits, this so-called non-standard evaluation makes it
harder to program functions in the usual way, as illustrated in the
following code chunk, where neither attempt to use the function works.

```r
add_mean <- function(data, group_var, summarize_var) {
    data %>% group_by(group_var) %>%
             mutate(mean_of_var = mean(summarize_var))
}

try(cpds2 <- add_mean(cpds, country, unemp))
try(cpds2 <- add_mean(cpds, 'country', 'unemp'))
```


For more details on how to avoid this problem when writing functions
that involve tidyverse manipulations, see
[this tidyverse programming guide](https://dplyr.tidyverse.org/articles/programming.html).

Note that the tidyverse is not the only place where non-standard
evaluation is used. Consider this *lm* call:

```r
lm(y ~ x, weights = w, data = mydf)
```

> **Challenge**
> Where is the non-standard evaluation there?

---

[← 3. Packages and namespaces](05-3-packages-and-namespaces.md) · [Up: contents](index.md) · [5. Programming paradigms: object-oriented and functional programming →](07-5-programming-paradigms-object-oriented-and-functional-progr.md)
