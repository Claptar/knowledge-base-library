---
title: "74. Sufficiency, Minimax, and Asymptotic Theory"
course: "Berkeley Stat 210A Fall 2024"
chapter: 74
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 74. Sufficiency, Minimax, and Asymptotic Theory

## What this covers

This chapter works through a complete final examination from Berkeley's STAT210A (Fall 2019,
Prof. Will Fithian), together with its model solutions, as a review of four pieces of the course's
estimation-theory toolkit in action: minimax and Bayes estimation under a non-standard loss,
sufficiency and exact inference in a Gaussian variance-components model, sufficiency and
large-sample theory for a capture-recapture model, and maximum likelihood together with a
finite-sample permutation test in a nonlinear regression model. It assumes the standard machinery
of point estimation and testing: sufficiency, minimal sufficiency, completeness, exponential
families, Bayes estimators and Bayes risk, minimax risk, consistency, the asymptotic normality of
the MLE, the delta method, and the $t$, $F$ and $\chi^2$ families that arise from Gaussian samples.
Each problem is presented as a worked example — problem statement, then the full argument — rather
than as an exercise to be solved separately, since the solutions *are* the material being reviewed.

## Problem 1: minimax estimation of a Poisson mean under relative squared error

**Setup.** Observe a single $X \sim \text{Pois}(\theta)$ and estimate $\theta > 0$ under the loss

$$
L(d, \theta) = \frac{(d - \theta)^2}{\theta}.
$$

This is ordinary squared error rescaled by $1/\theta$. Because $\text{Var}_\theta(X) = \theta$
grows with $\theta$, an estimator's absolute squared error naturally grows with $\theta$ too;
dividing by $\theta$ puts every value of $\theta$ on the same footing, and this rescaling is what
makes a finite minimax risk possible at all — part (f) shows that under plain squared error the
minimax risk for this problem is infinite.

**(a) The MLE and its risk.** Writing the Poisson density as $e^{x\log\theta - \theta}/x!$ exhibits
it as an exponential family with natural parameter $\log\theta$ and sufficient statistic $X$, so the
likelihood equation sets the mean parameter equal to the data: $\mathbb{E}_\theta X = X$, giving
$\hat\theta = X$. Its risk under $L$ is

$$
R(\theta) = \frac{1}{\theta}\,\mathbb{E}_\theta\big[(X-\theta)^2\big] = \frac{\text{Var}_\theta(X)}{\theta} = 1,
$$

a *constant* risk function — exactly the rescaling the loss was designed to produce.

**(b) A conjugate prior.** Take $\theta \sim \text{Gamma}(k,\beta)$ in the rate parametrization,
density $\propto \theta^{k-1}e^{-\beta\theta}$. Multiplying by the Poisson likelihood
$\theta^x e^{-\theta}$ gives posterior density $\propto \theta^{x+k-1}e^{-\theta(\beta+1)}$, i.e.

$$
\theta \mid X \sim \text{Gamma}(X+k,\ \beta+1).
$$

The posterior stays in the same family for any choice of $(k,\beta)$, so the Gamma family is
conjugate for the Poisson.

**(c) The Bayes estimator.** Expand the loss as $(d-\theta)^2/\theta = d^2/\theta - 2d + \theta$, so
the posterior expected loss is $d^2\,\mathbb{E}[\theta^{-1}\mid X] - 2d + \mathbb{E}[\theta\mid X]$,
a quadratic in $d$ minimized at

$$
\delta(X) = \frac{1}{\mathbb{E}[\theta^{-1}\mid X]}.
$$

Using the stated fact $\mathbb{E}[\theta^{-1}] = \beta/(k-1)$ for $\text{Gamma}(k,\beta)$ applied to
the posterior $\text{Gamma}(X+k,\beta+1)$,

$$
\delta(X) = \frac{X+k-1}{\beta+1}.
$$

Note this is *not* the posterior mean $(X+k)/(\beta+1)$ — because the loss weights errors by
$1/\theta$, the optimal Bayes rule under $L$ differs from the one under ordinary squared error, and
is shifted down slightly.

**(d) Bayes risk.** At the minimizer, $\delta(X)^2\,\mathbb{E}[\theta^{-1}\mid X] = \delta(X)$ (since
$\delta(X)\,\mathbb{E}[\theta^{-1}\mid X]=1$), so the minimized posterior risk collapses to

$$
-\delta(X) + \mathbb{E}[\theta\mid X] = -\frac{X+k-1}{\beta+1} + \frac{X+k}{\beta+1} = \frac{1}{\beta+1},
$$

a constant independent of $X$, so the Bayes risk of this prior is exactly $1/(1+\beta)$.

**(e) The MLE is minimax.** The MLE has constant risk $1$ everywhere (part a). To show it is
minimax it suffices to exhibit a *least favorable sequence*: priors whose Bayes risk approaches $1$,
the MLE's sup-risk. Fix any $k>1$ and let $\beta_n \to 0$; the Bayes risk $1/(1+\beta_n) \to 1$.
Since no estimator can beat the Bayes risk of any prior, and this sequence of Bayes risks climbs to
the MLE's constant risk, the MLE cannot be beaten anywhere and is minimax.

**(f) Why the loss was rescaled.** Under ordinary squared error $L_{\text{SE}}(d,\theta)=(d-\theta)^2$,
the Bayes estimator is the posterior mean and the posterior risk is the posterior variance,
$(X+k+1)/(1+\beta)^2$ (using the Gamma solutions above). Its Bayes risk is

$$
\mathbb{E}\left[\frac{X+k+1}{(1+\beta)^2}\right] = \frac{k/\beta + k + 1}{(1+\beta)^2},
$$

using $\mathbb{E}X = \mathbb{E}\theta = k/\beta$ for the prior. Fixing $k>1$ and sending
$\beta \to 0$ sends this to $\infty$. Since the minimax risk is at least every Bayes risk, the
minimax risk under plain squared error is infinite — the estimation problem simply has no useful
worst case unless the loss is compensated for the way variance scales with $\theta$, which is
exactly what $L$ does.

## Problem 2: sufficiency and exact inference in a Gaussian random-effects model

**Setup.** Observe $X_{ij}$, $i=1,\dots,m$ groups of $j=1,\dots,n$ replicates, under

$$
\alpha_i \overset{\text{iid}}{\sim} N(0,\tau^2), \qquad X_{ij}\mid\alpha \overset{\text{ind}}{\sim} N(\mu+\alpha_i,\sigma^2).
$$

The $\alpha_i$ are unobserved random effects, not parameters; $\mu\in\mathbb{R}$, $\tau^2\ge 0$,
$\sigma^2>0$ are the unknowns. Write $\overline X_i$ for the group means, $S_i^2$ for the
within-group sample variances, $\overline X$ for the grand mean, and $S_B^2$ for the *between*-group
sample variance of the $\overline X_i$'s.

**(a) Independence and distribution of the variance pieces.** $\overline X_i$ and $S_i^2$ are
functions of the $i$th group's data only, and different groups are independent (the $\alpha_i$ and
all the noise are independent across $i$), so $(\overline X_1,S_1^2),\dots,(\overline X_m,S_m^2)$
are mutually independent across $i$. Within a group, conditionally on $\alpha_i$ the $X_{ij}$ are an
iid Gaussian sample, so Basu's theorem gives $\overline X_i \perp S_i^2$ (the ancillary $S_i^2$ is
independent of the complete sufficient statistic $\overline X_i$ for the location $\mu+\alpha_i$).
Altogether, the $2m$ random variables $\overline X_1,\dots,\overline X_m,S_1^2,\dots,S_m^2$ are
mutually independent, with

$$
\overline X_i \overset{\text{iid}}{\sim} N\!\left(\mu,\ \tau^2+\tfrac{\sigma^2}{n}\right), \qquad
S_i^2 \overset{\text{iid}}{\sim} \frac{\sigma^2}{n-1}\chi^2_{n-1}.
$$

$S_B^2$, being the between-group sample variance of $(\overline X_1,\dots,\overline X_m)$ — iid
Gaussians with variance $\tau^2+\sigma^2/n$ — is itself distributed as
$\frac{\tau^2+\sigma^2/n}{m-1}\chi^2_{m-1}$, and is independent of $(S_1^2,\dots,S_m^2)$ because it
is a function only of the group means, which were just shown independent of the $S_i^2$'s.

**(b) A confidence interval for $\mu$.** $\overline X \sim N(\mu,\ \tau^2/m+\sigma^2/(nm))$ since it
is the average of the $\overline X_i$, each with variance $\tau^2+\sigma^2/n$. Because $S_B^2$ is
an independent, chi-squared-scaled unbiased estimate of exactly this variance (up to the factor
$m$), the usual studentization argument gives

$$
\sqrt m\,\frac{\overline X - \mu}{\sqrt{S_B^2}} \sim t_{m-1},
$$

so $\overline X \pm \sqrt{S_B^2/m}\; t_{m-1}(\alpha/2)$ is an exact $1-\alpha$ confidence interval —
note it never involves $\sigma^2$ or $\tau^2$ separately, only through $S_B^2$.

**(c) Testing $H_0:\tau^2=0$.** A tempting but wrong approach is to use $S_B^2$ alone: its null
distribution still depends on the nuisance parameter $\sigma^2$, so no fixed critical value works
for every $\sigma^2$. The fix is to compare $S_B^2$ against an independent estimate of $\sigma^2$
built from the within-group variances,

$$
S_W^2 = \frac1m\sum_i S_i^2 \sim \frac{\sigma^2}{m(n-1)}\chi^2_{m(n-1)},
$$

which is independent of $S_B^2$. Then

$$
\frac{S_B^2}{S_W^2} \sim \left(\frac{\tau^2}{\sigma^2}+\frac1n\right) F_{m-1,\,m(n-1)}
\quad\Longrightarrow\quad
n\,\frac{S_B^2}{S_W^2} \sim \left(n\frac{\tau^2}{\sigma^2}+1\right) F_{m-1,\,m(n-1)} \overset{H_0}{=} F_{m-1,\,m(n-1)}.
$$

Reject $H_0$ when $nS_B^2/S_W^2$ exceeds $F_{m-1,m(n-1)}(\alpha)$ — an exact, nuisance-free test
because dividing out by $S_W^2$ eliminates $\sigma^2$ entirely.

**(d) A confidence interval for $\tau^2/\sigma^2$.** The same pivot works for a general null
$H_0:\tau^2/\sigma^2=\rho$: $T_\rho = \frac{n}{n\rho+1}S_B^2/S_W^2 \sim F_{m-1,m(n-1)}$ under $H_0$.
Inverting the equal-tailed rejection region $\{T_\rho \notin (b,a)\}$, with
$a=F_{m-1,m(n-1)}(\alpha/2)$ and $b=F_{m-1,m(n-1)}(1-\alpha/2)$, gives the confidence interval

$$
C(X) = \left[\frac{S_B^2}{aS_W^2} - \frac1n,\ \ \frac{S_B^2}{bS_W^2}-\frac1n\right].
$$

**(e) An exponential family and a complete sufficient statistic.** Grouping each group's data as a
vector $X_i \in \mathbb{R}^n$, the $X_i$ are iid $N(\mu\mathbf 1, \Sigma)$ with compound-symmetric
covariance $\Sigma = \sigma^2 I_n + \tau^2 \mathbf{1}\mathbf{1}'$. Its inverse has the same
compound-symmetric form, $\Sigma^{-1} = \theta I_n + \zeta\mathbf 1\mathbf 1'$ for functions
$\theta(\tau^2,\sigma^2)>0$ and $\zeta(\tau^2,\sigma^2)<0$. Expanding the Gaussian log-density in
this basis, the joint likelihood depends on the data only through

$$
T = \left(\sum_i \|X_i\|^2,\ \sum_i \overline X_i^2,\ \overline X\right),
$$

and since the natural parameter space (as $(\tau^2,\sigma^2,\mu)$ ranges over $\tau^2>0,\sigma^2>0,
\mu\in\mathbb{R}$) contains an open set, this is a full-rank three-parameter exponential family, so
$T$ is complete and sufficient. Finally the two "ANOVA identities"

$$
(m-1)S_B^2 + m\overline X^2 = \sum_i \overline X_i^2, \qquad (n-1)S_i^2 + n\overline X_i^2 = \|X_i\|^2
$$

show $T$ and $(\overline X, S_B^2, \sum_i S_i^2)$ are invertible functions of each other, so the
latter — the natural "ANOVA-table" statistics — is also complete sufficient. This is why every
exact procedure above could be built from just those three numbers.

## Problem 3: sufficiency and asymptotics in a capture-recapture model

**Setup.** An ecologist visits a reserve on two consecutive days looking for reindeer. There are
$n$ reindeer present (the parameter of interest), each independently seen on each day with
probability $\pi$ (a nuisance parameter). $N_{11}$ is the number seen both days, $N_{10}$ seen only
day one, $N_{01}$ only day two; $N_{00}$, seen neither day, is unobserved. This is a
capture-recapture (mark-recapture) design.

**(a) Sufficiency via factorization.** Each reindeer independently falls into outcome $00,01,10,11$
with probabilities $p_{00}=(1-\pi)^2$, $p_{01}=p_{10}=\pi(1-\pi)$, $p_{11}=\pi^2$, so the counts are
multinomial: $(N_{00},N_{01},N_{10},N_{11}) \sim \text{Multinom}(n,(p_{00},p_{01},p_{10},p_{11}))$.
Writing the multinomial density and simplifying,

$$
\left(\frac{\pi}{1-\pi}\right)^{2N_{11}+N_{10}+N_{01}} \cdot \frac{n!}{(n-N_{11}-N_{01}-N_{10})!}
\cdot \frac{1}{N_{01}!\,N_{10}!\,N_{11}!}.
$$

The first two factors depend on the data only through $T=(N_{11}, N_{10}+N_{01})$ and on the
parameters $(n,\pi)$; the last factor depends only on the data. By the factorization theorem, $T$
is sufficient. (The subtlety here — flagged as a common mistake — is that $n$ is an *unknown
parameter*, so $n!/(n-N_{11}-N_{10}-N_{01})!$ is itself a function of the parameter and must be
kept in the parameter-dependent factor, not treated as a data-only normalizing constant.)

**(b) Minimal sufficiency.** A sufficient statistic is minimal if it can be recovered from the
collection of all likelihood ratios between parameter pairs. The likelihood ratio between
$(n,\pi)$ and $(\tilde n,\tilde\pi)$ is

$$
\left(\frac{\pi(1-\tilde\pi)}{\tilde\pi(1-\pi)}\right)^{2N_{11}+N_{10}+N_{01}}
\cdot \frac{n!}{\tilde n!}\cdot\frac{(\tilde n - N_{11}-N_{10}-N_{01})!}{(n-N_{11}-N_{10}-N_{01})!}.
$$

Setting $n=\tilde n$ and varying $\pi/\tilde\pi$ reveals $2N_{11}+N_{10}+N_{01}$; setting
$\pi=\tilde\pi$ and varying $n,\tilde n$ reveals $N_{11}+N_{10}+N_{01}$. Knowing both is equivalent
to knowing $T=(N_{11},N_{10}+N_{01})$, so $T$ is minimal sufficient.

**(c) Consistency of a quadratic estimator.** Consider

$$
\hat n = \frac{(N_{01}+N_{10}+2N_{11})^2}{4N_{11}}
$$

— the numerator's base is the total number of sightings (each reindeer-day). Each $N_{ij}/n$ is an
average of $n$ iid Bernoulli$(p_{ij})$ indicators, so $N_{ij}/n \overset{p}{\to} p_{ij}$ by the LLN.
Dividing numerator by $n^2$ and denominator by $n$ and applying the continuous mapping theorem
(valid since $p_{11}=\pi^2>0$),

$$
\frac{\hat n}{n} \overset{p}{\to} \frac{(2p_{01}+2p_{11})^2}{4p_{11}} = \frac{(2\pi(1-\pi)+2\pi^2)^2}{4\pi^2} = 1,
$$

so $\hat n$ is consistent: $\hat n/n \overset{p}{\to} 1$.

**(d) Asymptotic distribution.** Grouping the two symmetric miss/detect cells, the reduced
multinomial $(N_{00}, N_{10}+N_{01}, N_{11}) \sim \text{Multinom}(n,(p_{00},2p_{01},p_{11}))$ is
itself a sum of $n$ iid trinomial vectors, so the CLT applied to the two observed coordinates gives

$$
\frac1{\sqrt n}\left(\begin{pmatrix}N_{10}+N_{01}\\N_{11}\end{pmatrix} - \begin{pmatrix}2np_{01}\\np_{11}\end{pmatrix}\right) \Rightarrow N_2(0,\Sigma),
$$

with $\Sigma$ the corresponding multinomial covariance matrix. Applying the delta method to
$f(t_1,t_2) = (t_1+2t_2)^2/(4t_2)$ — so that $\hat n/n = f\big((N_{10}+N_{01})/n,\ N_{11}/n\big)$ —
with gradient $\nabla f(t_1,t_2) = (1+t_1/2t_2,\ 1-t_1^2/4t_2^2)$ gives

$$
\sqrt n\left(\frac{\hat n}{n} - 1\right) \Rightarrow N(0,\sigma^2), \qquad \sigma^2 = \nabla f(2p_{01},p_{11})'\,\Sigma\,\nabla f(2p_{01},p_{11}),
$$

which simplifies, after algebra, to $\sigma^2 = (1-\pi)^2/\pi^2$. The takeaway pattern is general:
reduce a multinomial to the coordinates you can actually observe, apply the CLT there, and push the
answer through a nonlinear estimator with the delta method.

## Problem 4: MLE and a permutation test in nonlinear regression

**Setup.** Observe $n$ pairs $(x_i,Y_i)$ with $x_i$ fixed and

$$
Y_i = g(\alpha+\beta x_i) + \varepsilon_i, \qquad \varepsilon_i \overset{\text{ind}}{\sim} N(0,\sigma^2 h(x_i)),
$$

$g$ a known strictly increasing, smooth link, $h>0$ a known variance-shape function, and
$(\alpha,\beta,\sigma^2)$ the unknown parameters estimated jointly by maximum likelihood. Write
$r_i = Y_i - g(\hat\alpha+\hat\beta x_i)$ for the residual at the fitted values.

**(a) Score equations for $\alpha,\beta$.** The log-likelihood is (up to constants) a weighted sum
of squared residuals, $-\frac{1}{2\sigma^2}\sum_i (Y_i-g(\alpha+\beta x_i))^2/h(x_i)$. Differentiating
with respect to $\alpha$ and $\beta$ and setting the score to zero gives

$$
\sum_i w_i r_i = 0, \qquad \sum_i w_i r_i x_i = 0, \qquad \text{where } w_i = \frac{\dot g(\hat\alpha+\hat\beta x_i)}{h(x_i)}.
$$

The weight $w_i$ combines two effects: it downweights points with noisier observations
(large $h(x_i)$), and it upweights points where the link $g$ is locally steep (large $\dot g$) —
those are the points whose residuals are most informative about $\alpha,\beta$. This is a
necessary, not sufficient, condition for a local optimum; the likelihood can in principle have
several local optima or, in pathological cases, no maximizer at all.

**(b) The MLE for $\sigma^2$.** Differentiating the log-likelihood with respect to $\sigma^2$ and
plugging in $(\hat\alpha,\hat\beta)$ gives the natural weighted residual variance,

$$
\hat\sigma^2 = \frac1n \sum_{i=1}^n \frac{(Y_i - g(\hat\alpha+\hat\beta x_i))^2}{h(x_i)}.
$$

Because the score equations for $\alpha,\beta$ in part (a) do not involve $\sigma^2$ at all, the
same $(\hat\alpha,\hat\beta)$ solves them whether or not $\sigma^2$ is known — a fact used directly
in part (c).

**(c) Asymptotic normality with random covariates.** Now let $X_1,\dots,X_n$ be iid, bounded
($|X_i|\le B$) and continuous, with the other parameters fixed as $n\to\infty$. Assume $\sigma^2$ is
known first. The score for $(\alpha,\beta)$ is $\frac1{\sigma^2}\big(\sum_i r_iw_i,\ \sum_i r_iw_iX_i\big)$,
with mean zero given $X$, so the Fisher information is the expectation of its conditional variance:

$$
J(\alpha,\beta) = \frac n{\sigma^2}\,\mathbb{E}\!\left[\frac{\dot g(\alpha+\beta X)^2}{h(X)} \begin{pmatrix}1 & X\\ X & X^2\end{pmatrix}\right],
$$

which needs $h$ to stay bounded away from $0$ near where $X$ has positive density, or the
expectation diverges. Given the usual regularity conditions and consistency of the MLE, the standard
asymptotic-normality theorem for the MLE gives

$$
\sqrt n \left(\begin{pmatrix}\hat\alpha\\\hat\beta\end{pmatrix} - \begin{pmatrix}\alpha\\\beta\end{pmatrix}\right) \Rightarrow N_2\big(0,\ J(\alpha,\beta)^{-1}\big).
$$

If $\sigma^2$ is instead unknown, nothing changes: by part (b), $(\hat\alpha,\hat\beta)$ is exactly
the same random variable regardless of whether $\sigma^2$ is known or estimated (it only rescales
the log-likelihood), so it has the same limiting law either way.

**(d) A finite-sample test that does not need to know $g$.** Now fix the $x_i$ again, set
$h\equiv 1$, and treat $g$ as completely unknown apart from being strictly increasing and smooth.
Test $H_0:\beta\le 0$ against $H_1:\beta>0$ without ever using a formula for $g$. Let
$\mu_i = g(\alpha+\beta x_i)$; if $\beta=0$ the means are all equal and the $Y_i$ are iid, hence
exchangeable, so a permutation test is exact at that boundary: using $T(Y)=x'Y$ as the statistic and
rejecting when $T(Y)$ is among the $\lfloor a(B+1)\rfloor$ largest of $T(Y),T(\pi_1Y),\dots,T(\pi_BY)$
over $B$ random permutations gives rejection probability exactly $a$ under $\beta=0$.

For the rest of the composite null, $\beta<0$, the argument extends by a monotonicity (rearrangement)
argument. Since $g$ is increasing and $\beta<0$, the means $\mu_i$ are decreasing wherever $x_i$ is
increasing, so for *every* permutation $\pi$, $x'\mu \le x'(\pi\mu)$ — the identity arrangement
minimizes the dot product of an increasing and a decreasing sequence. Writing
$T(\pi Y) = x'(\pi\mu) + x'(\pi\varepsilon)$, the noise part $\big(x'\varepsilon, x'(\pi_1\varepsilon),
\dots\big)$ is exchangeable regardless of $\beta$, while the signal part only makes $T(Y)$ smaller
relative to its permuted competitors. So $T(Y)$ is *less* likely than $1/(B+1)$-per-rank to land
among the top $\lfloor a(B+1)\rfloor$ values than it would be at $\beta=0$, and the rejection
probability is at most $a$ throughout $\beta\le 0$, for every valid choice of $g,\alpha,\sigma^2$ —
exactly the finite-sample validity a test of a composite null needs.

## Sources

All four problems and their solutions come from the same reconstructed document: Berkeley
STAT210A (Prof. Will Fithian), Fall 2019 final examination and model solutions, as converted to
markdown at
`docs/statistics/berkeley/stat210a/fall-2024/old-exams/solution2019/` in the knowledge-base-library
(identical copies of the same file are filed under the `fall-2025`, `fall-2025/units` and
`fall-2026` course-instance directories in the same repository; only one copy was used here). The
per-problem correspondence:

- Front matter and exam instructions — `01-final-examination-question-booklet.md`.
- Problem 1 (Poisson minimax estimation) and its solution —
  `02-1-poisson-minimax-estimation-24-points-4-points-part.md`, `03-1-solution.md`.
- Problem 2 (ANOVA with random effects) and its solution —
  `04-2-anova-with-random-effects-25-points-5-points-part.md`, `05-2-solution.md`.
- Problem 3 (capture-recapture, "And if you ever saw it...") and its solution —
  `06-3-and-if-you-ever-saw-it-24-points-6-points-part.md`, `07-3-solution.md`.
- Problem 4 (nonlinear regression) and its solution —
  `08-4-nonlinear-regression-24-points-6-points-part.md`, `09-4-solution.md`.

No slides or lecture transcript were supplied for this chapter — the exam booklet and its solutions
were the only input. The source file itself carries a conversion notice worth repeating here: the
original PDF had no extractable text layer, so this markdown is a model's reconstruction of scanned
pages, and every displayed equation in it is flagged there as unverified against the original scan.

---

[← 73. A Curved Gaussian Family](73-a-curved-gaussian-family.md) · [Contents](index.md) · [75. UMVU, Shrinkage, and Exact Testing →](75-umvu-shrinkage-and-exact-testing.md)
