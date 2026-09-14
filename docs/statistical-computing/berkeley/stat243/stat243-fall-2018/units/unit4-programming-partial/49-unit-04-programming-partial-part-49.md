---
title: Unit 04 — programming partial Part 49 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 49 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

56

**ls** ( **environment** (h)) # objects in that environment ## [1] "g" "y" f <- **function** (){ **print** ( **environment** ()) # execution environment of f() y <- 10 g <- **function** (x) x + y **return** (g) } h <- **f** () ## <environment: 0x520b6b8> **environment** (h) ## <environment: 0x520b6b8> **h** (3) ## [1] 13 **environment** (h)$y ## [1] 10 ## advanced: explain this: **environment** (h)$g ## function(x) x + y ## <environment: 0x520b6b8>

Comprehension problem Here’s a case where something I tried failed and I had to think more carefully about scoping to understand why.

**set.seed** (1) **rnorm** (1) ## [1] -0.626

57

**save** (.Random.seed, file = 'tmp.Rda') **rnorm** (1) ## [1] 0.184 tmp <- **function** () { **load** ('tmp.Rda') **print** ( **rnorm** (1)) } **tmp** () ## [1] -0.836

Question: what was I hoping that code to do, and why didn’t it work?

Detecting non-local variables We can use codetools::findGlobals to detect non-local variables when we are programming.

**library** (codetools) f <- **function** () { y <- 3 **print** (x + y) } **findGlobals** (f) ## [1] "<-" "{" "+" "print" "x"

Is that result what you would expect? What does it say about my statement that using non-local variables is a bad idea?

### 6.9 Environments and the search path

So far we’ve seen lexical scoping in action primarily in terms of finding variables in a single enclosing environment. But what if the variable is not found in either the frame/environment of the function or the enclosing environment? When R goes looking for an object (in the form of a symbol), it starts in the current environment (e.g., the frame/environment of a function) and then runs up through the enclosing environments, until it reaches the global environment, which is where R starts when you open R (it actually continues further up; see below). In general, as we’ve

58

seen, these environments are not the environments of the calling function(s) - i.e., they are not the frames on the stack (see the next Section).

By default objects are created in the global environment, .GlobalEnv. As we’ve seen, the environment within a function call has as its enclosing environment the environment where the function was defined (not the environment from which it was called), and based on lexical scoping this is next place that is searched if an object can’t be found in the frame of the function call. As an example, if an object couldn’t be found within the environment of an lm() function call, R would first look in the environment (i.e., the namespace) of the stats package (since this is the environment where lm() is defined and is therefore the enclosing environment for lm()), then in packages imported by the stats package, then the base package, and then the global environment.

If R can’t find the object when reaching the global environment, it runs through the search path, which you can see with search(). The search path is a set of additional environments. Generally packages are created with namespaces, i.e., each has its own environment, as we see based on search().

**search** ()

---

[← Unit 04 — programming partial Part 48 —](48-unit-04-programming-partial-part-48.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 50 — →](50-unit-04-programming-partial-part-50.md)
