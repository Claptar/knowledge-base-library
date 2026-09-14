---
title: 4 Types, classes, and object-oriented programming
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Types, classes, and object-oriented programming

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.1 Types and classes**

You should be familiar with vectors as the basic data structure in R, with character, integer, numeric, etc. classes. Vectors are either _atomic vectors_ or _lists_ . Atomic vectors generally contain one of the four following types: _logical_ , _integer_ , _double/numeric_ , and _character_ .

Objects in general have a type, which relates to what kind of values are in the objects and how objects are stored internally in R (i.e., in C).

You can look at Table 7.1 in the Adler book to see some other types.

devs <- **rnorm** (5) **class** (devs) ## [1] "numeric"

13

**typeof** (devs) ## [1] "double" a <- **data.frame** (x = 1:2) **class** (a) ## [1] "data.frame" **typeof** (a) ## [1] "list" **is.data.frame** (a) ## [1] TRUE **is.matrix** (a) ## [1] FALSE **is** (a, "matrix") ## [1] FALSE m <- **matrix** (1:4, nrow = 2) **class** (m) ## [1] "matrix" **typeof** (m) ## [1] "integer"

Everything in R is an object and all objects have a class. For simple objects class and type are often closely related, but this is not the case for more complicated objects. The class describes what the object contains and standard functions associated with it. In general, you mainly need to know what class an object is rather than its type. Classes can _inherit_ from other classes; for example, the _glm_ class inherits characteristics from the _lm_ class. We’ll see more on the details of object-oriented programming shortly.

14

We can create objects with our own defined class (an S3 class in this simple example - we’ll discuss S3 classes in Section 4.4.1).

bart <- **list** (firstname = 'Bart', surname = 'Simpson', hometown = "Springfield") **class** (bart) <- 'personClass' _## it turns out R already has a 'person' class_ **class** (bart) ## [1] "personClass" **is.list** (bart) ## [1] TRUE **typeof** (bart) ## [1] "list" **typeof** (bart$firstname) ## [1] "character"

### **4.2 Attributes**

_Attributes_ are information about an object attached to an object as something that looks like a named list. Attributes are often copied when operating on an object. This can lead to some weirdlooking formatting:

x <- **rnorm** (10 * 365) **attributes** (x) ## NULL qs <- **quantile** (x, **c** (.025, .975)) **attributes** (qs) ## $names ## [1] "2.5%" "97.5%"

15

qs ## 2.5% 97.5% ## -1.93 2.01 qs[1] + 3 ## 2.5% ## 1.07 **object.size** (qs) ## 352 bytes

Thus in any subsequent operations with _qs_ , the _names_ attribute will often get carried along. We can get rid of it:

**names** (qs) <- **NULL** qs ## [1] -1.93 2.01 **object.size** (qs) ## 64 bytes

A common use of attributes is that rows and columns may be named in matrices and data frames, and elements in vectors:

**row.names** (mtcars)[1:6] ## [1] "Mazda RX4" "Mazda RX4 Wag" ## [3] "Datsun 710" "Hornet 4 Drive" ## [5] "Hornet Sportabout" "Valiant" **names** (mtcars) ## [1] "mpg" "cyl" "disp" "hp" "drat" "wt" "qsec" ## [8] "vs" "am" "gear" "carb"

**attributes** (mtcars)

16

---

[← 3 Text manipulation, string processing and regular expressions (regex)](15-3-text-manipulation-string-processing-and-regular-expression.md) · [Up: contents](index.md) · [Unit 05 — programming Part 17 — →](17-unit-05-programming-part-17.md)
