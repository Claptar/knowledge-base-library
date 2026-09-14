---
title: 4 Object-oriented programming (OOP)
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 4 Object-oriented programming (OOP)

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Popular languages that use OOP include C++, Java, and Python. In fact C++ is the object-oriented version of C. Different languages implement OOP in different ways.

The idea of OOP is that all operations are built around objects, which have a class, and methods that operate on objects in the class. Classes are constructed to build on (inherit from) each other, so that one class may be a specialized form of another class, extending the components and methods of the simpler class (e.g., _lm_ and _glm_ objects).

38

Note that in more formal OOP languages, all functions are associated with a class, while in R, only some are.

Often when you get to the point of developing OOP code in R, you’re doing more serious programming, and you’re going to be acting as a software engineer. It’s a good idea to think carefully in advance about the design of the classes and methods.

### **4.1 S3 approach**

S3 classes are widely-used, in particular for statistical models in the _stats_ package. S3 classes are very informal in that there’s not a formal definition for an S3 class. Instead, an S3 object is just a primitive R object such as a list or vector with additional attributes including a class name.

**Inheritance** Let’s look at the _lm_ class, which builds on lists, and _glm_ class, which builds on the _lm_ class. Here _mod_ is an object (an instance) of class _lm_ . An analogy is the difference between a random variable and a realization of that random variable.

**library** (methods) yb <- **sample** ( **c** (0, 1), 10, replace = TRUE) yc <- **rnorm** (10) x <- **rnorm** (10) mod1 <- **lm** (yc ~ x) mod2 <- **glm** (yb ~ x, family = binomial) **class** (mod1) ## [1] "lm" **class** (mod2) ## [1] "glm" "lm" **is.list** (mod1) ## [1] TRUE **names** (mod1) ## [1] "coefficients" "residuals" "effects" "rank" ## [5] "fitted.values" "assign" "qr" "df.residual" ## [9] "xlevels" "call" "terms" "model"

39

**is** (mod2, "lm")

---

[← Unit 06 — Rprog Part 16 —](16-unit-06-rprog-part-16.md) · [Up: contents](index.md) · [[1] TRUE →](18-1-true.md)
