---
title: Unit 04 — programming partial Part 47 —
source: https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf
source_file: sources/berkeley-stat243/stat243-fall-2018/units/unit4-programming-partial.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming partial Part 47 —

**Source:** [`units/unit4-programming-partial.pdf`](https://github.com/berkeley-stat243/stat243-fall-2018/blob/be0e210baad11c83cecdb23dcb9e91f609bc536a/units/unit4-programming-partial.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Challenge: why did I not do print(sys.status()) directly?

If you’re interested in parsing a somewhat complicated example of frames in action, Adler provides a user-defined timing function that evaluates statements in the calling frame.

### 6.5 Operators

Operators, such as ’+’, ’[’ are just functions, but their arguments can occur both before and after the function call:

a <- 7; b <- 3 # let's think about the following as a mathematical function # -- what's the function call? a + b ## [1] 10 **`+`** (a, b) ## [1] 10

47

In general, you can use back-ticks to refer to the operators as operators instead of characters. In some cases single or double quotes also work. We can look at the code of an operator as follows using back-ticks to escape out of the standard R parsing, e.g., ‘%*%‘.

Finally, since an operator is just a function, you can use it as an argument in various places:

|x <br>**ou**|<- 1:<br>**ter**(x|3; y <- **c**(100,200,300)<br>, y, `+`)|
|---|---|---|
|##||[,1] [,2] [,3]|
|##|[1,]|101<br>201<br>301|
|##|[2,]|102<br>202<br>302|
|##|[3,]|103<br>203<br>303|
|my|List|<- **list**(**list**(a = 'new york', b = 1:5), **list**(a = 'california', b = 6:1|
|re|sult|<- **lapply**(myList, `[[`, 2)|
|re|sult||
|##|[[1]|]|
|##|[1]|1 2 3 4 5|
|##|||
|##|[[2]|]|
|##|[1]|6<br>7<br>8<br>9 10|
|##|note|that the index "2" is the additional argument to the [[ function|
|my|Mat <|- **sapply**(myList, `[[`, 2)|
|my|Mat||
|##||[,1] [,2]|
|##|[1,]|1<br>6|
|##|[2,]|2<br>7|
|##|[3,]|3<br>8|
|##|[4,]|4<br>9|
|##|[5,]|5<br>10|
|**cb**|**ind**(m|yList[[1]][[2]], myList[[2]][[2]])<br>## equivalent but doesn't scale|
|##||[,1] [,2]|
|##|[1,]|1<br>6|
|##|[2,]|2<br>7|


48

---

[← Unit 04 — programming partial Part 46 —](46-unit-04-programming-partial-part-46.md) · [Up: contents](index.md) · [Unit 04 — programming partial Part 48 — →](48-unit-04-programming-partial-part-48.md)
