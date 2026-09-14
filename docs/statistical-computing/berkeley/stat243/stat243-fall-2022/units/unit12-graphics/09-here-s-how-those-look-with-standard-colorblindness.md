---
title: here's how those look with standard colorblindness
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit12-graphics.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# here's how those look with standard colorblindness

**Source:** [`units/unit12-graphics.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit12-graphics.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

showpal(dichromat(palette()))
```

I like `fields::tim.colors()` for spatial images. How does it do in terms of color-blindness?
Based on the images below, not too bad.


```r
library(fields, quietly = TRUE)
n <- 20; xs <- ys <- 1:n
gr <- expand.grid(xs, ys);
U <- chol(exp(-rdist(gr)/6))
par(mfrow = c(1, 2))
vals <- matrix(crossprod(U, rnorm(n^2)), n, n)
## how does tim.colors fair with color-blindness?
image.plot(1:n, 1:n, vals, col = tim.colors(32),
                xlab = '', ylab = '', main = 'ordinary vision')
image.plot(1:n, 1:n, vals,
     col = dichromat(tim.colors(32)),  # actually not too bad
     xlab = '', ylab = '', main = 'colorblind vision')
```

---

[← 4. Colors](08-4-colors.md) · [Up: contents](index.md)
