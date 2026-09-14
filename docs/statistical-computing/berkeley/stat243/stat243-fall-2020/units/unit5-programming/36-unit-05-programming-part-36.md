---
title: Unit 05 — programming Part 36 —
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2020/units/unit5-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 05 — programming Part 36 —

**Source:** [`units/unit5-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/units/unit5-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Here’s a fun example. You might do this with an _apply()_ variant, in particular _replicate()_ , but this is slick:

make_container <- **function** (n) { x <- **numeric** (n) i <- 1 **function** (value = **NULL** ) { **if** ( **is.null** (value)) { **return** (x) } **else** { x[i] <<- value i <<- i + 1 } } } nboot <- 100 bootmeans <- **make_container** (nboot) data <- faithful[ , 1] _# Old Faithful geyser eruption lengths_ **for** (i **in** 1:nboot)

60

**bootmeans** ( **mean** ( **sample** (data, **length** (data),

replace=TRUE)))

_## this will place results in x in the function env't and you can grab it out_ **bootmeans** () ## [1] 3.59 3.41 3.47 3.46 3.43 3.48 3.51 3.48 3.50 3.46 ## [11] 3.41 3.62 3.46 3.46 3.49 3.50 3.56 3.50 3.58 3.60 ## [21] 3.46 3.45 3.50 3.41 3.46 3.59 3.35 3.50 3.51 3.37 ## [31] 3.46 3.38 3.58 3.52 3.45 3.58 3.50 3.47 3.54 3.57 ## [41] 3.53 3.58 3.40 3.50 3.50 3.56 3.41 3.45 3.50 3.53 ## [51] 3.49 3.57 3.46 3.50 3.43 3.48 3.54 3.45 3.53 3.53 ## [61] 3.46 3.36 3.41 3.58 3.58 3.47 3.51 3.50 3.56 3.48 ## [71] 3.39 3.48 3.62 3.54 3.51 3.52 3.47 3.49 3.43 3.45 ## [81] 3.40 3.52 3.43 3.49 3.51 3.56 3.55 3.46 3.30 3.56 ## [91] 3.47 3.49 3.41 3.40 3.46 3.43 3.43 3.44 3.45 3.42

### **6.7 Environments and the search path**

So far we’ve seen lexical scoping in action primarily in terms of finding variables in a single enclosing environment. But what if the variable is not found in either the frame/environment of the function or the enclosing environment? When R goes looking for an object (in the form of a symbol), it starts in the current environment (e.g., the frame/environment of a function) and then runs up through the enclosing environments, until it reaches the global environment, which is where R starts when you open R (it actually continues further up; see below). In general, as we’ve seen, these environments are not the environments of the calling function(s) - i.e., they are _not_ the frames on the stack (see the next Section).

By default objects are created in the global environment, _.GlobalEnv_ . As we’ve seen, the environment within a function call has as its enclosing environment the environment where the function was defined (not the environment from which it was called), and based on lexical scoping this is next place that is searched if an object can’t be found in the frame of the function call. As an example, if an object couldn’t be found within the environment of an _lm()_ function call, R would first look in the environment (i.e., the _namespace_ ) of the stats package (since this is the environment where _lm()_ is defined and is therefore the enclosing environment for _lm()_ ), then in packages imported by the stats package, then the base package, and then the global environment.

If R can’t find the object when reaching the global environment, it runs through the search path, which you can see with _search()_ . The search path is a set of additional environments. Generally

61

packages are created with namespaces, i.e., each has its own environment, as we see based on

_search()_ .

**search** ()

|##<br>[1]|".GlobalEnv"|"package:codetools"|
|---|---|---|
|##<br>[3]|"package:fields"|"package:maps"|
|##<br>[5]|"package:spam"|"package:grid"|
|##<br>[7]|"package:dotCall64"|"package:R6"|
|##<br>[9]|"package:dplyr"|"package:pryr"|
|## [11]|"package:knitr"|"package:stats"|
|## [13]|"package:graphics"|"package:grDevices"|
|## [15]|"package:utils"|"package:datasets"|
|## [17]|"package:SCF"|"package:methods"|
|## [19]|"Autoloads"|"package:base"|


**searchpaths** ()

---

[← [1] "{" "+" "<-" "print" "x"](35-1---print-x.md) · [Up: contents](index.md) · [Unit 05 — programming Part 37 — →](37-unit-05-programming-part-37.md)
