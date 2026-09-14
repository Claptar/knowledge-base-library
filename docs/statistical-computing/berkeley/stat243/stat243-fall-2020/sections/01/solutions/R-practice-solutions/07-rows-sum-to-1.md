---
title: rows sum to 1
source: https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2020/sections/01/solutions/R-practice-solutions.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# rows sum to 1

**Source:** [`sections/01/solutions/R-practice-solutions.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2020/blob/fd024cc8537586f4869f79be1492009acfe62d76/sections/01/solutions/R-practice-solutions.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

apply(X = m2, MARGIN = 2, FUN = function(x){sum(x) == 1})
```

### 2.
#### a.
```r
x <- seq.int(from = 1, to = 10, by = 0.1)
```

#### b.
```r
y <- 2 * x + rnorm(n = length(x))
```

#### c.
```r
plot(x, y)
```

#### d.
```r
my_lm <- lm(y ~ x)
```

#### e.
```r
lapply(X = my_lm, FUN = "class")
```

#### f.
```r
sapply(X = my_lm, FUN = "class")
```

#### g.
They are the same here, because a list is the best simplified type of object. ```sapply``` is a "simplified apply", ie, the output is simiplified to something deemed intelligent, like a vector or a list etc.

## Functions
### 1.
#### 0.
```r
absMedDiff <- function(x){
	return(sum(abs(x - median(x = x))))
}
```

### a.
```r
absMedDiff2 <- function(x){
	# check if numeric
	stopifnot(is.numeric(x = x))

	# if numeric, do work and return
	return(sum(abs(x - median(x = x))))
}
```

#### b.
```r
absMedDiff3a <- function(x, na.rm = FALSE){
	# check if numeric
	stopifnot(is.numeric(x = x))

	# if numeric, do work and return
	return(sum(abs(x - median(x = x, na.rm = na.rm)), na.rm = na.rm))
}
```

### 2.
#### a.
```r
x <- sample(x = 0:1, size = 100, replace = TRUE)
y <- sample(x = 0:1, size = 100, replace = TRUE)
```

#### b.
It doesn't make sense to call set.seed within the function, because the function would always return the same sample.
```r
sumHeads <- function(num_flips){
	# do flipping
	x <- sample(x = c(0,1), size = num_flips, replace = TRUE)

	# return heads
	return(sum(x))
}
```

#### c.
```r
sums_vec <- replicate(n = 10000, expr = sumHeads(num_flips = 200))
```

#### d.
```r
hist(sums_vec)
```

### 3.
```r
basicFunc <- function(x, y, operation = "add"){
	switch(operation,
				 "add" = x + y,
				 "subtract" = x - y,
				 "multiply" = x * y,
				 "divide" = x / y,
				 "Warning: Not a designated option")
}
```

### 4.
```r
cumSum <- function(x){
	# setup return vector
	ret_vec <- numeric(length = length(x) - 1)

	# set first element
	ret_vec[1] <- x[1]

	# loop over rest
	for(i in 2:length(x)){
		ret_vec[i] <- ret_vec[i - 1] + x[i]
	}

	# return result
	return(ret_vec)
}
```

## Loading (and saving) data
### 1.
Note, you will need to install the ```foreign``` package with ```install.packages("foreign")``` if it is not already.  The working directory is assumed to be the sections/01 folder in the stat243-fall-2020 Github.
```r
library(foreign)
earnings <- read.dta("../data/heights.dta")
```

#### a.
```r
class(earnings)
```

#### b.
```r
str(earnings)
```

#### c.
```r
length(earnings)
```

#### d.
```r
dim(earnings)
```

#### e.
```r
sapply(earnings, FUN = class)
```

#### f.
```r
sapply(earnings[, grep("height", colnames(earnings))], summary)
```

#### g.
```r
```

#### h.
```r
hist(earnings$yearbn)
```

### 2.
```r

---

[← dimensions are the same](06-dimensions-are-the-same.md) · [Up: contents](index.md) · [read csv →](08-read-csv.md)
