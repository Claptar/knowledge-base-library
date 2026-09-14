---
title: 2 Advanced topics in working with functions
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit6-Rprog.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 Advanced topics in working with functions

**Source:** [`units/unit6-Rprog.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit6-Rprog.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

R is a functional programming language. All operations are carried out by functions including assignment, various operators, printing to the screen, etc.

### **2.1 Pointers**

By way of contrast to R’s pass by value system, I want to briefly discuss the idea of a pointer, common in compiled languages such as C.

int x = 3;

int* ptr; ptr = &x; *<sup>ptr</sup> *<sup>7;//returns21</sup> Here _ptr_ is the address of the integer _x_ .

Vectors in C are really pointers to a block of memory:

int x[10];

In this case _x_ will be the address of the first element of the vector. We can access the first element as x[0] or *x.

Why have we gone into this? In C, you can pass a pointer as an argument to a function. The result is that only the scalar address is copied and not the entire vector, and inside the function, one can modify the original vector, with the new value persisting on exit from the function. For example:

int myCal(int *ptr){

*<sup>ptr=</sup> *<sup>ptr+</sup> *<sup>ptr;</sup> }

When calling C or C++ from R, one (implicitly) passes pointers to the vectors into C. Let’s see an example:

out <- rep(0, n)

out <- .C(“logLik”, out = as.double(out),

theta = as.double(theta))$out

In C, the function definition looks like this:

void logLik(double* out, double* theta)

17

### **2.2 Alternatives to pass by value in R**

There are occasions we do not want to pass by value. The main reason is when we want a function to modify a complicated object without having to return it and re-assign it in the parent environment. There are several work-arounds:

1. We can use Reference Class objects. Reference classes are new in R. We’ll discuss these in Section 4.

2. We can access the object in the enclosing environment as a ’global variable’, as we’ve seen when discussing scoping. More generally we can access the object using _get()_ , specifying the environment from which we want to obtain the variable. Recall that to specify the location of an object, we can generally specify (1) a position in the search path, (2) an explicit environment, or (3) a location in the call stack by using _sys.frame()_ . However we cannot change the value of the object in the parent environment without some additional tools.

   - (a) We can use the ’<<-’ operator to assign into an object in the parent environment (provided an object of that name exists in the parent environment).

   - (b) We can also use _assign()_ , specifying the environment in which we want the assignment to occur.

3. We can use replacement functions (Section 2.4), which hide the reassignment in the parent environment from the user. Note that a second copy is generally created in this case, but the original copy is quickly removed.

4. We can use a closure. This involves creating functions within a function call and returning the functions as a list (or a single function, as we saw when discussing scoping in Unit 4). When one executes the enclosing function, the list is created and one can call the functions of that object. Those functions then can access objects in the enclosing environment (the environment of the original function) and can use ‘<<-‘ to assign into the enclosing environment, to which all the functions have access. Chambers provides an example of this in Sec. 5.4.

x <- **rnorm** (10) f <- **function** (input) { data <- input g <- **function** (param) **return** (param * data)

18

**return** (g) } myFun <- **f** (x) **rm** (x) _# to demonstrate we no longer need x_ **myFun** (3) ## [1] 2.7604 1.8395 0.6086 -5.4911 1.3466 -1.5746 -4.0919 -1.5413 ## [9] -1.5635 5.3104 x <- **rnorm** (1e+07) myFun <- **f** (x) **object.size** (myFun) _# hmmm_ ## 1560 bytes **object.size** ( **environment** (myFun)$data) ## 80000040 bytes Here’s a fun example. You might do this with an _apply()_ variant, in particular _replicate()_ , but this is slick: make_container <- **function** (n) { x <- **numeric** (n) i <- 1 **function** (value = **NULL** ) { **if** ( **is.null** (value)) { **return** (x) } **else** { x[i] <<- value i <<- i + 1 } } } nboot <- 100 bootmeans <- **make_container** (nboot) data <- faithful[, 1] _# length of Old Faithful geyser eruption times_

19

**for** (i **in** 1:nboot) **bootmeans** ( **mean** ( **sample** (data, **length** (data), replace = TRUE _# this will place results in x in the function env't and you can grab it out # as_

**bootmeans** ()

---

[← Unit 06 — Rprog Part 04 —](04-unit-06-rprog-part-04.md) · [Up: contents](index.md) · [Unit 06 — Rprog Part 06 — →](06-unit-06-rprog-part-06.md)
