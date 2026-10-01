---
title: "76. Regression with Correlated Errors"
course: "Berkeley Stat 210A"
chapter: 76
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 76. Regression with Correlated Errors

## What this covers

This chapter works through one exam problem — linear regression with correlated Gaussian errors —
as a worked example of exponential-family and sufficiency machinery in action. It assumes the
reader already has full-rank exponential families, sufficiency and completeness, maximum
likelihood in exponential families, the multivariate normal distribution and its behaviour under
affine maps, and Basu's theorem. The question it answers: given a linear model whose errors are
correlated and Gaussian, how do you estimate the coefficients when the error covariance is known,
and how do you separate the estimation of the coefficients from the estimation of the covariance
itself when it is not known?

## The setup

Observations $i = 1, \dots, n$ come with fixed covariates $x_i \in \mathbb{R}^d$ and a response
$$Y_i = x_i'\beta + \varepsilon_i,$$
for an unknown coefficient vector $\beta \in \mathbb{R}^d$. Stacking the $x_i'$ into rows of a
design matrix $X \in \mathbb{R}^{n\times d}$,
$$Y = X\beta + \varepsilon, \qquad \varepsilon \sim N_n(0, \Sigma),$$
with $\Sigma \in \mathbb{R}^{n\times n}$ positive definite. The errors are correlated across
observations — $\Sigma$ need not be diagonal — which is the whole point: this is not the usual
i.i.d.-noise regression model. Throughout, $n \ge d \ge 1$ and $X$ has full column rank.

Two standard normal facts are used repeatedly. For $\mu \in \mathbb{R}^n$ and positive definite
$\Sigma$, the density of $Z \sim N_n(\mu,\Sigma)$ is
$$p_{\mu,\Sigma}(z) = |2\pi\Sigma|^{-1/2}\exp\left\{-\tfrac12 (z-\mu)'\Sigma^{-1}(z-\mu)\right\},$$
and if $A \in \mathbb{R}^{k\times n}$, $b\in\mathbb{R}^k$ are fixed, then $AZ+b \sim N_k(A\mu+b,
A\Sigma A')$.

The problem splits into two regimes: first $\Sigma$ known and only $\beta$ to estimate, then
$\Sigma$ unknown as well.

## $\Sigma$ known: the model is a full-rank exponential family

Write out the density of $Y$ and collect terms by how they depend on $\beta$:
$$
\begin{aligned}
p_\beta(y) &= |2\pi\Sigma|^{-1/2}\exp\left\{-\tfrac12(y-X\beta)'\Sigma^{-1}(y-X\beta)\right\}\\[2pt]
&= \exp\left\{\beta'X'\Sigma^{-1}y - \tfrac12\beta'X'\Sigma^{-1}X\beta\right\}
   \cdot |2\pi\Sigma|^{-1/2}\exp\left\{-\tfrac12 y'\Sigma^{-1}y\right\}\\[2pt]
&= e^{\beta'T(y) - A(\beta)}\,h(y),
\end{aligned}
$$
with
$$T(y) = X'\Sigma^{-1}y, \qquad A(\beta) = \tfrac12\beta'X'\Sigma^{-1}X\beta, \qquad
h(y) = |2\pi\Sigma|^{-1/2}\exp\{-\tfrac12 y'\Sigma^{-1}y\}.$$
This is exactly the canonical exponential-family form, with natural parameter $\beta$ and
sufficient statistic $T(Y) = X'\Sigma^{-1}Y$. Because $\beta$ ranges over all of $\mathbb{R}^d$ —
nothing restricts the natural parameter space — the family is full rank, and a full-rank
exponential family's canonical sufficient statistic is automatically complete. So $T(Y)$ is
complete sufficient for $\beta$.

## The MLE is the generalized least squares estimator

Exponential families have a standard trick for finding the MLE: since the log-likelihood is
$\ell(\beta) = \beta'T(y) - A(\beta)$, the score equation $\nabla_\beta \ell = 0$ reads
$$T(y) = \nabla A(\beta) = \mathbb{E}_\beta[T(Y)].$$
That is, the MLE matches the observed value of the sufficient statistic to its expectation. Here
$\mathbb{E}_\beta T(Y) = X'\Sigma^{-1}X\beta$, so
$$X'\Sigma^{-1}Y = X'\Sigma^{-1}X\hat\beta \iff \hat\beta = (X'\Sigma^{-1}X)^{-1}X'\Sigma^{-1}Y,$$
which is invertible because $X$ has full column rank and $\Sigma^{-1}$ is positive definite. This
is the generalized least squares estimator: it reduces to ordinary least squares when $\Sigma$ is
a multiple of the identity, and reweights observations according to how correlated and how noisy
they are otherwise.

Since $\hat\beta$ is a fixed linear map applied to $Y \sim N_n(X\beta,\Sigma)$, the affine-map
fact above gives its exact distribution:
$$\hat\beta \sim N\!\left(\beta,\ (X'\Sigma^{-1}X)^{-1}\right).$$

## $\Sigma$ unknown: a replicated design

Now suppose $\Sigma$ is unknown and must be estimated too. To do that here requires more than one
draw of the response vector: assume $m$ independent replicates of the *whole* experiment (same
$X$, same $\beta$, fresh noise each time),
$$Y^{(k)} = X\beta + \varepsilon^{(k)}, \qquad \varepsilon^{(k)} \overset{\text{i.i.d.}}{\sim}
N_n(0,\Sigma), \qquad k = 1,\dots,m.$$
Only the errors differ across $k$; $X$ and $\beta$ are shared. Define the natural moment
estimators
$$\overline Y = \frac1m\sum_{k=1}^m Y^{(k)}, \qquad
\widehat\Sigma = \frac{1}{m-1}\sum_{k=1}^m (Y^{(k)} - \overline Y)(Y^{(k)} - \overline Y)'.$$
The question is whether $\overline Y$ and $\widehat\Sigma$ are independent — the multivariate,
correlated-error analogue of the classical fact that the sample mean and sample variance of an
i.i.d. Gaussian sample are independent.

## Independence via Basu's theorem, on a larger model

The direct approach fails: in the model where the mean is constrained to lie in the $d$-dimensional
subspace $\{X\beta : \beta\in\mathbb{R}^d\}$ with $d < n$, $\overline Y$ is *not* complete
sufficient, so Basu's theorem does not apply directly to $(\overline Y,\beta)$.

The fix is to stop constraining the mean. Consider the larger model where the $Y^{(k)}$ are i.i.d.
$N_n(\mu,\Sigma)$ for an *arbitrary* $\mu \in \mathbb{R}^n$ — no longer required to be of the form
$X\beta$ — with $\Sigma$ still known. Stacking the $m$ replicates and applying the exponential
family argument of the previous section (with the role of $X$ played by the identity $I_n$, since
now every $\mu\in\mathbb{R}^n$ is reachable), the natural parameter $\mu$ ranges over all of
$\mathbb{R}^n$, so $\Sigma^{-1}\overline Y$ — a bijective rescaling of the sufficient statistic
$\sum_k \Sigma^{-1}Y^{(k)}$ — is complete sufficient for $\mu$.

Meanwhile $\widehat\Sigma$ is a function of the centered observations $Y^{(k)} - \overline Y =
\varepsilon^{(k)} - \bar\varepsilon$, which do not involve $\mu$ at all: its distribution is the
same for every $\mu$, i.e. $\widehat\Sigma$ is ancillary for $\mu$ in this larger model (for any
fixed $\Sigma$). Basu's theorem then says the complete sufficient statistic $\Sigma^{-1}\overline
Y$ — and hence $\overline Y$ itself, since $\Sigma$ is invertible — is independent of
$\widehat\Sigma$.

This independence holds for *every* $\mu \in \mathbb{R}^n$ and every positive definite $\Sigma$,
because that is what the larger model's Basu argument establishes. In particular it holds when
$\mu = X\beta$ for any $\beta$ — which is exactly the original, mean-constrained model. The
restriction to $\mu = X\beta$ only breaks the *completeness* argument (there are extra degrees of
freedom in $\mathbb{R}^n$ that $X\beta$ does not reach, so $\overline Y$ stops being complete
there); it does not change the joint distribution of $(\overline Y, \widehat\Sigma)$ for a given
$\mu$, so the conclusion transfers unchanged. Enlarging the parameter space until completeness
holds, running Basu there, and then specializing back down is the reusable idea in this argument,
not just a trick for this one problem.

**Common mistake to flag**: it is tempting to try to invoke Basu directly on $\overline Y$ within
the $\beta$-parametrised model. That fails when $d < n$, because $\overline Y$ is not complete
sufficient there — completeness is exactly what is lost by constraining the mean.

## Unbiasedness of $\widehat\Sigma$

It remains to check that $\widehat\Sigma$ is an unbiased estimator of $\Sigma$, entry by entry.
Since $Y^{(k)} - \overline Y = \varepsilon^{(k)} - \bar\varepsilon$, for each pair of indices
$i,j$,
$$
\mathbb{E}\,\widehat\Sigma_{ij}
= \frac{1}{m-1}\,\mathbb{E}\left[\sum_{k=1}^m (\varepsilon_i^{(k)}-\bar\varepsilon_i)
  (\varepsilon_j^{(k)}-\bar\varepsilon_j)\right].
$$
Because the $\varepsilon^{(k)}$ are i.i.d., each term in the sum has the same expectation, so the
sum's expectation is $m$ times the $k=1$ term's. Writing
$\varepsilon_i^{(1)} - \bar\varepsilon_i = \frac{m-1}{m}\varepsilon_i^{(1)} -
\frac1m\sum_{k>1}\varepsilon_i^{(k)}$ and expanding the product, the cross terms between
independent, mean-zero errors vanish, leaving
$$
\mathbb{E}\left[(\varepsilon_i^{(1)}-\bar\varepsilon_i)(\varepsilon_j^{(1)}-\bar\varepsilon_j)\right]
= \left(\frac{m-1}{m}\right)^{\!2}\Sigma_{ij} + \frac{m-1}{m^2}\Sigma_{ij}
= \frac{m-1}{m}\,\Sigma_{ij}.
$$
Putting the two steps together,
$$
\mathbb{E}\,\widehat\Sigma_{ij} = \frac{m}{m-1}\cdot\frac{m-1}{m}\,\Sigma_{ij} = \Sigma_{ij},
$$
so $\widehat\Sigma$ is unbiased for $\Sigma$. The $(m-1)$ in the denominator of $\widehat\Sigma$ is
exactly what makes this cancel, the same Bessel-type correction as in the univariate sample
variance.

## Sources

This chapter reconstructs the first problem of the Fall 2021 STAT210A final examination
(Prof. Will Fithian), "Regression with correlated errors" (25 points, parts (a)–(d) as supplied;
the exam's own preamble notes that parts (c)–(e) assume $\Sigma$ unknown, but part (e)'s statement
was not present in the supplied material and so is not reproduced or exercised here). The source
files are the LLM-reconstructed markdown conversions of `old-exams/solution2021.pdf` from the
`berkeley-stat210a` GitHub repositories — the same PDF, mirrored across the `fall-2024`,
`fall-2025` (`old-exams/` and `units/old-exams/`) and `fall-2026` course trees:

- `docs/statistics/berkeley/stat210a/fall-2024/old-exams/solution2021/01-final-examination-question-booklet.md`
- `docs/statistics/berkeley/stat210a/fall-2024/old-exams/solution2021/02-1-regression-with-correlated-errors-25-points-5-points-part.md`
  (and the equivalent files under the `fall-2025`, `fall-2025/units`, and `fall-2026` trees, which
  are the same content re-fetched from different course-year mirrors)

The source markdown carries its own conversion caveat: the original PDF has no extractable text
layer, so a model read the pages and transcribed them, and every equation is marked unverified.
This chapter reproduces the algebra as given and it is internally consistent (the unbiasedness
computation's final cancellation checks out), but it has not been checked against the original
scanned exam. The source text also breaks off mid-sentence at the end of part (d), partway into an
"alternative" matrix-form derivation of the same unbiasedness result — that alternative derivation
is not reconstructed here, since only the italicized single fragment `$$\sum_{k=1}^m
(\varepsilon^{(k)} - \bar{\varepsilon})(\varepsilon^{(k)} - \bar{\varepsilon})' = \left(\sum_{k=1}^`
was present in the supplied file. Exam administrative boilerplate (student ID instructions, "no
electronic devices," grading notes) is omitted as non-mathematical content.

---

[← 75. UMVU, Shrinkage, and Exact Testing](75-umvu-shrinkage-and-exact-testing.md) · [Contents](index.md) · [77. Sufficiency, Testing, and Bayes: A Final Exam →](77-sufficiency-testing-and-bayes-a-final-exam.md)
