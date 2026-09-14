---
title: Unit 04 — programming Part 23 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 23 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

You can use _setClassUnion()_ to create what Adler calls _superclass_ and what Chambers calls a _virtual class_ that allows for methods that apply to multiple classes. So if you have a person class and a pet class, you could create a “named lifeform” virtual class that has methods for working with name and age slots, since both people and pets would have those slots. You can’t directly create an object in the virtual class.

#### **4.4.3 Reference classes**

Reference classes are a new construct in R. They are classes somewhat similar to S4 that allow us to access their fields by reference. Importantly, they behave like pointers (the fields in the objects are ’mutable’). Let’s work through an example where we set up the fields of the class (like S4 slots) and class methods, including a constructor. Note that one cannot add fields to an already existing class.

Here’s the initial definition of the class.

tsSimClass <- **setRefClass** ("tsSimClass", fields = **list** ( n = "numeric", times = "numeric", corMat = "matrix", lagMat = "matrix", corParam = "numeric", U = "matrix", currentU = "logical"), methods = **list** ( initialize = **function** (times = 1:10, corParam = 1, ...){

30

_# we seem to need default values for the copy()_ **require** (fields) times <<- times _# field assignment requires using_ n <<- **length** (times) corParam <<- corParam currentU <<- FALSE **calcMats** () **callSuper** (...) _# calls initializer of base class_ }, calcMats = **function** (){ _# Python-style doc string_ ' calculates correlation matrix and Cholesky factor lagMat <- **rdist** (times) _# local variable_ corMat <<- **exp** (-lagMat / corParam) _# field assignment_ U <<- **chol** (corMat) _# field assignment_ **cat** ("Done updating correlation matrix and Cholesky currentU <<- TRUE }, changeTimes = **function** (newTimes){ times <<- newTimes **calcMats** () }, show = **function** (){ _# 'print' method_ **cat** ("Object of class 'tsSimClass' with ", n, " time } )

)

---

[← Unit 04 — programming Part 22 —](22-unit-04-programming-part-22.md) · [Up: contents](index.md) · [Unit 04 — programming Part 24 — →](24-unit-04-programming-part-24.md)
