---
title: part of an iterative optimization to find a maximum likelihood estimator
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit5-programming.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# part of an iterative optimization to find a maximum likelihood estimator

**Source:** [`units/unit5-programming.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit5-programming.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

```

**Challenge 6**: Another problem involving a computation from a
student's PhD research. The following is the probability mass function
for an overdispersed binomial random variable:
$$
P(Y =y )  =  \frac{f(y;n,p,\phi)}{\sum_{k=0}^{n}f(k;n,p,\phi)} \\
$$
$$
f(k;n,p,\phi)  =  {n \choose k}\frac{k^{k}(n-k)^{n-k}}{n^{n}}\left(\frac{n^{n}}{k^{k}(n-k)^{n-k}}\right)^{\phi}p^{k\phi}(1-p)^{(n-k)\phi}
$$

where the denominator serves as a normalizing constant to ensure this is
a valid probability mass function. How would one efficiently code the
computation of the denominator? For our purposes here you can take
$n=10000$, $p=0.3$ and $\phi=0.5$ when you need to actually run your
code. Note that $0^0=1$.

> **Warning**: we always want to do such calculations on the log scale,
only exponentiating at the end if necessary. Otherwise we're likely to
run into overflow or underflow, where the result is too big or too small
to store in the 8-byte floating point representation (more in a later Unit).

Here's a non-vectorized approach:

```r
logLik <- function(k, n, p, phi) {
  klogk <- ifelse(k == 0, 0, k*log(k))
  nmklognmk <- ifelse(n-k == 0, 0, (n-k)*log(n-k))
  exp(lchoose(n, k) + klogk + nmklognmk - n*log(n) + phi*(n*log(n) -
      klogk - nmklognmk) + k*phi*log(p) + (n-k)*phi*log(1-p))
}
n <- 10000
out1 <- sum(sapply(0:n, logLik, n, p, phi))
```

And here's a basic vectorized approach.

```r
normConstVecNaive <- function(n, p, phi) {
    k <- 0:n
    loglik <- lchoose(n, k)
    klogk <- k*log(k)
    klogk[is.nan(klogk)] <- 0
    nmklognmk <- (n-k)*log((n-k))
    nmklognmk[is.nan(nmklognmk)] <- 0
    logLik <- lchoose(n, k) + klogk + nmklognmk - n*log(n) + phi*(n*log(n) - klogk - nmklognmk) +
        k*phi*log(p) + (n - k)*phi*log(1-p)
    return(sum(exp(logLik)))
}
out2 <- normConstVecNaive(n, p, phi)
```

Questions:
  1. List some inefficiencies in `normConstVecNaive`.
  2. Write a faster version.

**Challenge 7:** Suppose we have a matrix in which each row is a vector
of probabilities that add to one, and we want to generate a categorical
sample based on each row. E.g., the first row might be (0.9, 0.05, 0.05)
and the second row might be (0.1, 0.85, .0.5). When we generate the
first sample, it is very likely to be a 1 and the second sample is very
likely to be a 2. We could do this using a for loop over the rows of the
matrix, and the *sample* function, but that is a lot slower than some
other ways we might do it. How can we do it faster?

```r
n <- 100000
p <- 5  ## number of categories

## way to generate a random matrix of row-normalized probabilities:
tmp <- exp(matrix(rnorm(n*p), nrow = n, ncol = p))
probs <- tmp / rowSums(tmp)

smp <- rep(0, n)

## loop by row and use sample()
set.seed(1)
system.time(
    for(i in seq_len(n))
        smp[i] <- sample(p, 1, prob = probs[i, ])
)
```

---

[← in the real code, oneUpdate was called repeatedly in a while loop as](21-in-the-real-code-oneupdate-was-called-repeatedly-in-a-while.md) · [Up: contents](index.md) · [10. Computing on the language (optional) →](23-10-computing-on-the-language-optional.md)
