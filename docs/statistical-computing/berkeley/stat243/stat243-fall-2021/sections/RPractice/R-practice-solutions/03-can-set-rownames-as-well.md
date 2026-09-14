---
title: can set rownames as well
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/sections/RPractice/R-practice-solutions.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# can set rownames as well

**Source:** [`sections/RPractice/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/sections/RPractice/R-practice-solutions.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

df1 <- data.frame(y = y, z = z, w = w, f = f, row.names = x)
```

## Subsetting datastructures
### 1.
#### a.
```r
m1 <- df1[, sapply(df1, is.numeric)]
```

#### b.
```r
m2 <- m1[f, ]
```

#### c.
```r
df2 <- df1[df1$z >= 0, names(df1) != 'z']
```

#### d.
```r
df3 <- df1[-c(3, 17), ]
```

#### e.
```r
df4 <- df1[seq(2, nrow(df1), 2), ]
```

## Vectorized calculations
### 1.
```r
x <- seq(1, 3, .1)
exp(2 * x) * x ^ sqrt(x)
```

### 2.
#### a.
```r
x <- matrix(0, nrow = 5, ncol = 5)
```

#### b.
```r
row(x)
col(x)
```

#### c.
```r
x[abs(row(x) - col(x)) == 1] = 1
```

#### d.
```r
abs(row(x) - col(x))
```

### 3.
#### a.
```r
outer(0:4, 0:4, "+")
```

#### b.
```r
outer(0:4, 0:4, "+") %% 5
```

## Using ```apply```, ```sapply```, and ```lapply```
### 1.
#### a.
```r
m1 <- matrix(data = runif(n = 30, min = 1, max = 100), nrow = 5, ncol = 6)
```

#### b.
They are not the same, if we do it this way. R is column major
```r
m2 <- apply(X = m1, MARGIN = 1, FUN = function(x){ x / sum(x)})
dim(m1) == dim(m2)
```

Now they match.
```r
m2 <- t(apply(X = m1, MARGIN = 1, FUN = function(x){x / sum(x)}))
dim(m1) == dim(m2)
```

#### c.
```r

---

[← don't need to use x because rownames are alaready 1:50](02-don-t-need-to-use-x-because-rownames-are-alaready-1-50.md) · [Up: contents](index.md) · [check that the rows sum to 1 →](04-check-that-the-rows-sum-to-1.md)
