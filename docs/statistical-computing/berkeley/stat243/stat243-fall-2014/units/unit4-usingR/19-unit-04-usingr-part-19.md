---
title: Unit 04 — usingR Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 19 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.2 Type vs. class**

You should be familiar with vectors as the basic data structure in R, with character, integer, numeric, etc. classes. Objects also have a type, which relates to what kind of values are in the objects and how objects are stored internally in R (i.e., in C).

Let’s look at Adler’s Table 7.1 to see some other types.

a <- **data.frame** (x = 1:2) **class** (a) ## [1] "data.frame" **typeof** (a) ## [1] "list" m <- **matrix** (1:4, nrow = 2) **class** (m) ## [1] "matrix" **typeof** (m) ## [1] "integer"

Everything in R is an object and all objects have a class. For simple objects class and type are often closely related, but this is not the case for more complicated objects. The class describes what the object contains and standard functions associated with it. In general, you mainly need to know what class an object is rather than its type. Classes can _inherit_ from other classes; for example, the _glm_ class inherits characteristics from the _lm_ class. We’ll see more on the details of object-oriented programming in the R programming unit.

We can create objects with our own defined class.

13

me <- **list** (firstname = "Chris", surname = "Paciorek") **class** (me) <- "personClass" _# it turns out R already has a 'person' class_ **class** (me) ## [1] "personClass" **is.list** (me) ## [1] TRUE **typeof** (me) ## [1] "list" **typeof** (me$firstname) ## [1] "character"

### **3.3 Information about objects**

Some functions that give information about objects are:

**is** (me, "personClass") ## [1] TRUE **str** (me) ## List of 2 ## $ firstname: chr "Chris" ## $ surname : chr "Paciorek" ## - attr(*, "class")= chr "personClass" **attributes** (me) ## $names ## [1] "firstname" "surname" ## ## $class ## [1] "personClass"

14

mat <- **matrix** (1:4, 2) **class** (mat) ## [1] "matrix" **typeof** (mat) ## [1] "integer" **length** (mat) ## [1] 4 _# recall that a matrix can be thought of as a vector # with dimensions_ **attributes** (mat) ## $dim ## [1] 2 2 **dim** (mat) ## [1] 2 2

_Attributes_ are information about an object attached to an object as something that looks like a named list. Attributes are often copied when operating on an object. This can lead to some weird-looking formatting: x <- **rnorm** (10 * 365) qs <- **quantile** (x, **c** (0.025, 0.975)) qs ## 2.5% 97.5% ## -1.98 1.98 qs[1] + 3 ## 2.5% ## 1.02

15

Thus in an subsequent operations with _qs_ , the _names_ attribute will often get carried along. We can get rid of it:

**names** (qs) <- **NULL** qs ## [1] -1.98 1.98

A common use of attributes is that rows and columns may be named in matrices and data frames, and elements in vectors:

**row.names** (mtcars)[1:6] ## [1] "Mazda RX4" "Mazda RX4 Wag" ## [3] "Datsun 710" "Hornet 4 Drive" ## [5] "Hornet Sportabout" "Valiant" **names** (mtcars) ## [1] "mpg" "cyl" "disp" "hp" "drat" "wt" "qsec" ## [8] "vs" "am" "gear" "carb" mat <- **data.frame** (x = 1:2, y = 3:4) **row.names** (mat) <- **c** ("first", "second") mat ## x y ## first 1 3 ## second 2 4 vec <- **c** (first = 7, second = 1, third = 5) vec["first"] ## first ## 7

### **3.4 The workspace**

Objects exist in a workspace, which in R is called an environment.

16

_# objects() # what objects are in my workspace_ **identical** ( **ls** (), **objects** ()) _# synonymous_ ## [1] TRUE dat <- 7 dat2 <- 9 subdat <- 3 obj <- 5 obj2 <- 7 **objects** (pattern = "^dat") ## [1] "dat" "dat2" **rm** (dat2, subdat) **rm** (list = **c** ("obj", "obj2")) _# a bit confusing - the 'list' argument should be a # character vector_ **rm** (list = **ls** (pattern = "^dat")) **exists** ("dat") _# can be helpful when programming_ ## [1] FALSE **rm** (list = **ls** ()) _# what does this do?_ dat <- **rnorm** (5e+05) **object.size** (dat) ## 4000040 bytes **print** ( **object.size** (dat), units = "Mb") _# this seems pretty clunky!_ ## 3.8 Mb _# but we'll understand why it's clunky when we see S3 # classes in detail_

17

### **3.5 Some other details**

**Special objects** There are also some special objects, which often begin with a period, like hidden files in UNIX. One is _.Last.value_ , which stores the last result.

**rnorm** (10) ## [1] -0.949 -1.164 1.161 -0.348 1.454 1.732 -0.745 ## [8] -0.156 1.034 0.669 _# .Last.value # this should return the 10 random normals # but knitr is messing things up, commented out here_

**Scientific notation** R uses the syntax _“xep”_ to mean _x ∗_ 10<sup>_p_</sup> . x <- 1e+05 **log10** (x) y <- 1e+05 x <- 1e-08

**Information about functions** To get help on functions (I’m having trouble evaluating these with knitr, so just putting these in as text here):

?lm # or help(lm) help.search('lm') apropos('lm') help('[[') # operators are functions too args(lm)

**Strings and quotation** Working with strings and quotes (see ?Quotes in R). Generally one uses double quotes to denote text. If we want a quotation symbol in text, we can do something like the following, either combining single and double quotes or escaping the quotation:

ch1 <- "Chris's\n" ch2 <- "He said, \"hello.\"\n" ch3 <- "He said, \"hello.\"\n"

18

Be careful when cutting and pasting from documents that are not text files as you may paste in something that looks like a single or double quote, but which R cannot interpret as a quote because it’s some other ASCII quote character.

---

[← 3 Objects in R](18-3-objects-in-r.md) · [Up: contents](index.md) · [4 Working with data structures →](20-4-working-with-data-structures.md)
