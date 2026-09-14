---
title: Introduction
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/RPractice/R-practice-solutions.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Introduction

**Source:** [`sections/RPractice/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

```r
knitr::opts_chunk$set(echo = TRUE)
```

## Creating data structures
### 1. Creating vectors
#### a.
```r
1:50
seq(1, 50)
```

#### b.
```r
!as.logical(1:50%%2)
```

#### c.
```r
50:1
seq(50, 1)
```

#### d.
```r
c(1:50, 49:1)
```

#### e.
```r
-10:10
seq(-10, 10)
```
#### f.
```r
3*1:16
seq(3, 48, by = 3)
```

#### g.
```r
as.character(seq(3, 48, by = 3))
```

#### h.
```r
rep(c("a", "b", "c", "d"), c(4, 3, 2, 1))
```

#### i.
```r
as.factor(rep(c("a", "b", "c", "d"), c(4, 3, 2, 1)))
```

#### j.
```r
seq(-1,1, length.out=200)
```

### 2.
#### a.
```r
x <- 1:50
```

#### b.
```r
y <- cos(x)
```

#### c.
```r
z <- tan(y)
```

#### d.
```r
w <- y*z
```

#### e.
```r
f <- x %in% 10:29
```

#### f.
```r
df1 <- data.frame(x = x, y = y, z = z, w = w, f = f)
```

#### g.
```r
names(df1) <- toupper(names(df1))
```

#### h.
```r

---

[Up: contents](index.md) · [don't need to use x because rownames are alaready 1:50 →](02-don-t-need-to-use-x-because-rownames-are-alaready-1-50.md)
