---
title: Unit 04 — usingR Part 21 —
source: https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf
source_file: sources/berkeley-stat243/stat243-fall-2014/units/unit4-usingR.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — usingR Part 21 —

**Source:** [`units/unit4-usingR.pdf`](https://github.com/berkeley-stat243/stat243-fall-2014/blob/49fcee4ef42342d81d010e586b69d92a94bbb12f/units/unit4-usingR.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Note that to operate on a data frame, which is a list, we’ll generally want to use _lapply()_ or _sapply()_ , as _apply()_ is really designed for working with elements that are all of the same type:

**apply** (CO2, 2, class) _# hmmm_ ## Plant Type Treatment conc ## "character" "character" "character" "character" ## uptake ## "character" **sapply** (CO2, class) ## $Plant ## [1] "ordered" "factor" ## ## $Type ## [1] "factor" ## ## $Treatment ## [1] "factor" ## ## $conc ## [1] "numeric" ## ## $uptake ## [1] "numeric"

20

Here’s a nice trick to pull out a specific component from each element of a list. (Note the use of the additional argument(s) to _sapply()_ - this can also be done in the other _apply()_ variants.)

params <- **list** (a = **list** (mn = 7, sd = 3), b = **list** (mn = 6, sd = 1), c = **list** (mn = 2, sd = 1)) **sapply** (params, "[[", 1) ## a b c ## 7 6 2

Finally, we can flatten a list with _unlist()_ .

**unlist** (x) ## a1 a2 b1 b2 sam1 sam2 sam3 ## 1.000 2.000 3.000 4.000 -0.631 1.878 0.422 ## sam4 ## 1.622

**Calculations in the context of stratification** Note that some of the basic R functionality for doing stratified analysis is mentioned here. For a new way to do such split-apply-combine operations see the _plyr_ package.

We can also use an _apply()_ variant to do calculations on subgroups, defined based on a factor or factors.

**tapply** (mtcars$mpg, mtcars$cyl, mean) ## 4 6 8 ## 26.7 19.7 15.1

**tapply** (mtcars$mpg, **list** (mtcars$cyl, mtcars$gear), mean)

---

[← 4 Working with data structures](20-4-working-with-data-structures.md) · [Up: contents](index.md) · [3 4 5 ## 4 21.5 26.9 28.2 ## 6 19.8 19.8 19.7 ## 8 15.1 NA 15.4 →](22-3-4-5-4-21-5-26-9-28-2-6-19-8-19-8-19-7-8-15-1-na-15-4.md)
