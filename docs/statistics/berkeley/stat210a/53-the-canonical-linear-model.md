---
title: "53. The Canonical Linear Model"
course: "Berkeley Stat 210A Fall 2024"
chapter: 53
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 53. The Canonical Linear Model

## What this covers

This chapter answers one question: given a Gaussian model, what *is* the right test and confidence
interval, and why do the familiar $z$-, $t$-, $\chi^2$- and $F$-statistics all have the shape they do?
It builds all four once, in a stripped-down "canonical" Gaussian model, and then shows that a wide range
of everyday problems — the one-sample and two-sample $t$-tests, testing a single regression coefficient,
one-way ANOVA — are literally the same problem after a change of basis. It assumes the multivariate
normal distribution and how it transforms under linear maps, orthogonal projections, and the earlier use
of Basu's theorem to show a sample mean and sample variance are independent.

## The $\chi^2$, $t$, and $F$ families

Three distributions get built out of independent standard normals and then used everywhere below.

If $Z_1,\dots,Z_d\overset{\mathrm{iid}}\sim N(0,1)$, then $V=\sum_i Z_i^2\sim\chi^2_d$
(equivalently, $\mathrm{Gamma}(d/2,2)$ in shape/scale form), with $\mathbb E V=d$ and
$\mathrm{Var}(V)=2d$. The central limit theorem applied to that sum gives
$(V-d)/\sqrt d\Rightarrow N(0,2)$, or informally $V/d\approx N(1,2/d)$, which collapses to the constant
$1$ as $d\to\infty$ — a law-of-large-numbers statement in more familiar clothing.

If further $Z\sim N(0,1)$ is independent of $V\sim\chi^2_d$, then
$$T=\frac{Z}{\sqrt{V/d}}\sim t_d,$$
Student's $t$ distribution on $d$ degrees of freedom. Since $V/d\to1$, $T\Rightarrow N(0,1)$ as
$d\to\infty$: $t_d$ is a normal distribution fattened to account for not knowing the true scale.

If $V_1\sim\chi^2_{d_1}$ and $V_2\sim\chi^2_{d_2}$ are independent, then
$$F=\frac{V_1/d_1}{V_2/d_2}\sim F_{d_1,d_2},$$
and as $d_2\to\infty$ the denominator concentrates at $1$, so $F_{d_1,d_2}\Rightarrow\chi^2_{d_1}/d_1$.
Squaring a $t$ produces an $F$ with one numerator degree of freedom: if $T\sim t_d$ then
$T^2=Z^2/(V/d)\sim F_{1,d}$, since $Z^2\sim\chi^2_1$.

Everything below is repeated use of one fact about the multivariate normal: if $Z\sim N_d(\mu,\Sigma)$,
$A\in\mathbb R^{k\times d}$, $b\in\mathbb R^k$, then $AZ+b\sim N_k(A\mu+b,A\Sigma A')$. In particular, an
*orthogonal* transformation ($AA'=I$) of an isotropic Gaussian ($\Sigma=\sigma^2I$) is again isotropic
with the same $\sigma^2$ — only the mean vector moves, and the coordinates of $AZ$ stay independent.

## Deriving the one-sample $t$-test by a change of basis

Take the most familiar testing problem, $X_1,\dots,X_n\overset{\mathrm{iid}}\sim N(\mu,\sigma^2)$,
written as $X\sim N_n(\mu\mathbf1_n,\sigma^2I_n)$ with $\mathbf1_n=(1,\dots,1)'$, and rederive the
one-sample $t$-test as "rotate until the mean vector has only one nonzero entry."

Build an orthonormal matrix $Q=(q_1\ Q_r)$ with $q_1=\mathbf1_n/\sqrt n$, and $q_2,\dots,q_n$ any
orthonormal basis completing $q_1$ to a basis of $\mathbb R^n$ (Gram–Schmidt, say — by the rotational
symmetry above, the particular choice cannot matter). Rotate the data, $Z=Q'X$. Because $Q$ is
orthogonal, $Z$ is still Gaussian with covariance $\sigma^2I_n$, with mean $Q'(\mu\mathbf1_n)=
\mu\,Q'\mathbf1_n$; the first entry of $Q'\mathbf1_n$ is $q_1'\mathbf1_n=\sqrt n$ and every other entry is
$q_j'\mathbf1_n=0$, since each $q_j$, $j\ge2$, was built orthogonal to $q_1=\mathbf1_n/\sqrt n$ and hence
to $\mathbf1_n$ itself. So
$$Z=\binom{Z_1}{Z_r}=\binom{q_1'X}{Q_r'X}\sim N_n\left(\binom{\sqrt n\mu}{0},\ \sigma^2I_n\right),$$
i.e. $Z_1=\sqrt n\bar X\sim N(\sqrt n\mu,\sigma^2)$, and $Z_r\sim N_{n-1}(0,\sigma^2I_{n-1})$ is
independent of $Z_1$ — coordinates of an isotropic Gaussian are always independent, which is the same
conclusion Basu's theorem gave earlier for $\bar X$ and $S^2$, reached a different way.

The length of $Z_r$ is exactly the sample variance. Since $Q$ is orthogonal, $\|Z\|^2=\|X\|^2$, so
$$\|Z_r\|^2=\|X\|^2-Z_1^2=\|X\|^2-n\bar X^2=\sum_i(X_i-\bar X)^2=(n-1)S^2,$$
hence $S^2=\|Z_r\|^2/(n-1)\sim\dfrac{\sigma^2}{n-1}\chi^2_{n-1}$, independent of $Z_1$.

### The geometric picture

$Z_1=q_1'X$ is nothing but the length of the projection of $X$ onto the line spanned by $\mathbf1_n$, and
$Z_r=Q_r'X$ is the projection onto the $(n-1)$-dimensional orthogonal complement — drawn below as a
single axis, which is legitimate because only its length $\|Z_r\|$ ever enters the argument.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="The data vector X split into its projection onto the mean direction and its projection onto the orthogonal complement">
  <defs>
    <marker id="tArrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1" stroke-opacity="0.5"/>
  <text x="240" y="198" font-size="12" fill="currentColor">direction of 1</text>
  <line x1="40" y1="180" x2="220" y2="180" stroke="currentColor" stroke-width="2" marker-end="url(#tArrow)"/>
  <text x="128" y="173" text-anchor="middle" font-size="12" fill="currentColor">Z1</text>
  <line x1="220" y1="180" x2="220" y2="55" stroke="currentColor" stroke-width="2" marker-end="url(#tArrow)"/>
  <text x="232" y="120" font-size="12" fill="currentColor">|Zr|</text>
  <line x1="40" y1="180" x2="220" y2="55" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="100" y="110" text-anchor="middle" font-size="12" fill="currentColor">X</text>
  <path d="M 208 180 L 208 168 L 220 168" fill="none" stroke="currentColor" stroke-width="1"/>
</svg>
<figcaption>The data vector $X$ splits into a component $Z_1$ along the special direction spanned by
$\mathbf1_n$ — whether that component is large is exactly the one-sample question — and a component of
length $\|Z_r\|$ in the orthogonal complement, which does not depend on the mean at all and calibrates
the noise level. $T^2$ compares the squared lengths of these two legs.</figcaption>
</figure>

So testing $H_0:\mu=0$ against large $|\bar X|$ is asking whether $X$ points appreciably along the
special direction $\mathbf1_n$, relative to how far it typically strays in the $n-1$ directions that
carry no signal:
$$T^2=\frac{n\bar X^2}{S^2}=\frac{\|\mathrm{Proj}_{\mathbf1_n}X\|^2}{\frac1{n-1}\|\mathrm{Proj}^\perp_{\mathbf1_n}X\|^2}\ \overset{H_0}\sim\ F_{1,n-1}.$$

The same decomposition gives the $\chi^2$/Beta bookkeeping that reappears in the $F$-test below. Under
$H_0$, $Z_1$ and $Z_r$ are independent, so $n\bar X^2=Z_1^2\sim\sigma^2\chi^2_1=\mathrm{Gamma}(1/2,2\sigma^2)$
and $(n-1)S^2\sim\sigma^2\chi^2_{n-1}=\mathrm{Gamma}((n-1)/2,2\sigma^2)$ are independent Gammas sharing a
scale, so their sum is again Gamma, $\|X\|^2=n\bar X^2+(n-1)S^2\sim\sigma^2\chi^2_n$, and (a standard fact
about independent Gammas with a common scale) the *proportion*
$$\frac{n\bar X^2}{\|X\|^2}\sim\mathrm{Beta}\!\left(\tfrac12,\tfrac{n-1}2\right)$$
is independent of the total $\|X\|^2$. This is where the $F$ distribution's link to the Beta distribution
comes from: if $U\sim\mathrm{Beta}(d_1/2,d_2/2)$ then $\dfrac{U/d_1}{(1-U)/d_2}\sim F_{d_1,d_2}$, and
taking $U=n\bar X^2/\|X\|^2$ here recovers $T^2\sim F_{1,n-1}$.

## The canonical linear model

Strip the one-sample problem to its geometric essence and it becomes a template for every Gaussian
testing problem below. Partition $Z\in\mathbb R^n$ into three blocks of sizes $d_0$, $d_1=d-d_0$, and
$d_r=n-d$,
$$Z=\begin{pmatrix}Z_0\\Z_1\\Z_r\end{pmatrix}\sim N_n\!\left(\begin{pmatrix}\mu_0\\\mu_1\\0\end{pmatrix},\ \sigma^2I_n\right),\qquad \mu_0\in\mathbb R^{d_0},\ \mu_1\in\mathbb R^{d_1},$$
and test $H_0:\mu_1=0$ against $H_1:\mu_1\neq0$ (one-sided if $d_1=1$). Read the three blocks as: $Z_0$
carries nuisance mean parameters that are free under both hypotheses, $Z_1$ carries the coordinates
actually being tested, and $Z_r$ is pure noise — its mean is exactly zero regardless of $\mu_0,\mu_1$, so
it carries no information about $H_0$ and exists only to be used as a yardstick for $\sigma$. Up to the
normalizing constant this is an exponential family with natural parameters $\mu_1/\sigma^2$ and
$\mu_0/\sigma^2$:
$$p(z)\ \propto\ \exp\left(\frac{\mu_1}{\sigma^2}{}'z_1+\frac{\mu_0}{\sigma^2}{}'z_0-\frac1{2\sigma^2}\|z\|^2\right).$$

Four tests fall out, according to whether $\sigma^2$ is known and whether $d_1=1$ or $d_1\ge1$:

- **$\sigma^2$ known, $d_1=1$ — the $z$-test.** Coordinates of an isotropic Gaussian are independent, so
  $Z_0\perp\!\!\!\perp Z_1$ and conditioning on $Z_0$ changes nothing: reject for large $|Z_1|$, using
  $$Z_1/\sigma\ \overset{H_0}\sim\ N(0,1).$$
- **$\sigma^2$ known, $d_1\ge1$ — the $\chi^2$-test.** The natural statistic is the Euclidean length
  $\|Z_1\|$: with no information favoring one direction of departure over another, every direction in
  the $d_1$-dimensional space is equally suspicious (an *anisotropic* prior belief about which directions
  $\mu_1$ is likely to move in would call for a differently weighted statistic instead). Reject for large
  $\|Z_1\|$, using
  $$\|Z_1\|^2/\sigma^2\ \overset{H_0}\sim\ \chi^2_{d_1}.$$
- **$\sigma^2$ unknown, $d_1=1$ — the $t$-test.** $Z_1/\sigma$ can no longer be computed, so $\sigma$
  must be estimated — but only from data carrying no information about $\mu_1$, which is exactly what
  $Z_r$ is. Since $\mathbb E\|Z_r\|^2=(n-d)\sigma^2$ regardless of $\mu_0,\mu_1$, and $Z_r$ is independent
  of $Z_1$, substituting $\hat\sigma=\sqrt{\|Z_r\|^2/(n-d)}$ for $\sigma$ in the $z$-statistic gives an
  honest pivot:
  $$\frac{Z_1}{\sqrt{\|Z_r\|^2/(n-d)}}\ \overset{H_0}\sim\ t_{n-d}.$$
- **$\sigma^2$ unknown, $d_1\ge1$ — the $F$-test.** The same substitution in the $\chi^2$-statistic gives
  $$\frac{\|Z_1\|^2/d_1}{\|Z_r\|^2/(n-d)}\ \overset{H_0}\sim\ F_{d_1,n-d}.$$

Here $n-d$ — what is left over after fitting $d$ mean parameters to $n$ observations — is called the
**residual degrees of freedom**, and $\hat\sigma^2=\|Z_r\|^2/(n-d)$ is the associated unbiased estimator
of $\sigma^2$: $\mathbb E\hat\sigma^2=\sigma^2$ and $\mathrm{Var}(\hat\sigma^2)=2\sigma^4/(n-d)$, both
immediate from $\|Z_r\|^2\sim\sigma^2\chi^2_{n-d}$.

The four statistics are literally one statistic, with $\sigma$ replaced by $\hat\sigma$ whenever it is
not known:

| | $\sigma^2$ known | $\sigma^2$ unknown |
|---|---|---|
| $d_1=1$ | $z=Z_1/\sigma$ | $t=Z_1/\hat\sigma$ |
| $d_1\ge1$ | $\chi^2=\|Z_1\|^2/\sigma^2$ | $F=(\|Z_1\|^2/d_1)/\hat\sigma^2$ |

## Confidence sets in the canonical model

The same four tests invert into confidence sets for $\mu_1$ — testing $H_0:\mu_1=\mu_1^\circ$ for a
general $\mu_1^\circ$, not just $0$. This needs one extra step, since $\mu_1$ is not itself the natural
parameter of the family: recentre by $\mu_1^\circ$. The vector $(Z_0,\ Z_1-\mu_1^\circ,\ Z_r)$ has exactly
the canonical distribution with $\mu_1$ replaced by $\mu_1-\mu_1^\circ$, so all four tests above apply
verbatim with $Z_1-\mu_1^\circ$ standing in for $Z_1$. Inverting each test — keep $\mu_1^\circ$ in the
confidence set exactly when the test does not reject it at the observed data — gives:

- $d_1=1$, $\sigma$ known: $(Z_1-\mu_1)/\sigma\sim N(0,1)$ inverts to the interval
  $Z_1\pm\sigma z_{\alpha/2}$.
- $d_1=1$, $\sigma$ unknown: $(Z_1-\mu_1)/\hat\sigma\sim t_{n-d}$ inverts to
  $Z_1\pm\hat\sigma\,t_{n-d}(\alpha/2)$.
- $d_1\ge1$, $\sigma$ known: $\|Z_1-\mu_1\|^2/\sigma^2\sim\chi^2_{d_1}$ inverts to the ball
  $\{\mu_1:\|\mu_1-Z_1\|\le\sigma\sqrt{c_{\chi^2}(\alpha)}\}$, where $c_{\chi^2}(\alpha)$ is the
  upper-$\alpha$ quantile of $\chi^2_{d_1}$.
- $d_1\ge1$, $\sigma$ unknown: the analogous ball $\{\mu_1:\|\mu_1-Z_1\|\le\hat\sigma\sqrt{c_F(\alpha)}\}$,
  using the upper-$\alpha$ quantile of $F_{d_1,n-d}$.

For $d_1=1$ these are the ordinary two-sided intervals; for $d_1\ge2$ they are balls in the (rotated)
coordinates of $\mu_1$.

## The general linear model

Every subspace-versus-subspace testing problem for a Gaussian mean reduces to the canonical model by the
same rotation trick used above for the one-sample $t$-test, now with one more block. Observe
$Y\sim N_n(\theta,\sigma^2I_n)$ and test $\theta\in\Theta_0$ against $\theta\in\Theta\setminus\Theta_0$,
where $\Theta_0\subseteq\Theta$ are subspaces of $\mathbb R^n$ with $\dim\Theta_0=d_0$ and
$\dim\Theta=d=d_0+d_1$. Choose an orthonormal basis adapted to this nesting: $Q_0$ spanning $\Theta_0$
itself, $Q_1$ spanning what $\Theta$ adds to $\Theta_0$ (the part of $\Theta$ orthogonal to $\Theta_0$),
and $Q_r$ spanning what is left of $\mathbb R^n$ once $\Theta$ is used up. Rotating,
$$Z=Q'Y\sim N_n\left(\begin{pmatrix}Q_0'\theta\\Q_1'\theta\\0\end{pmatrix},\ \sigma^2I_n\right),$$
where the last block is exactly zero because $\theta\in\Theta$ is orthogonal to everything in
$\Theta^\perp$. This is precisely the canonical model with $\mu_0=Q_0'\theta$, $\mu_1=Q_1'\theta$, and
$H_0:\theta\in\Theta_0$ has become $H_0:Q_1'\theta=0$ — run whichever of the $z$-, $\chi^2$-, $t$- or
$F$-test fits $d_1$ and whether $\sigma^2$ is known.

## Worked examples

### Linear regression

Fixed covariates $x_i\in\mathbb R^d$, $Y_i=x_i'\beta+\varepsilon_i$,
$\varepsilon_i\overset{\mathrm{iid}}\sim N(0,\sigma^2)$; stacking rows $x_i'$ into $X\in\mathbb
R^{n\times d}$ with columns $X_1,\dots,X_d$ gives $Y\sim N_n(X\beta,\sigma^2I_n)$. Assuming $X$ has full
column rank, the mean is confined to the $d$-dimensional subspace $\Theta=\mathrm{span}(X_1,\dots,X_d)$.
Testing that the first $d_1$ coefficients vanish, $H_0:\beta_1=\cdots=\beta_{d_1}=0$, is testing
$\theta\in\Theta_0=\mathrm{span}(X_{d_1+1},\dots,X_d)$ (or $\theta=0$ if every coefficient is tested).

The ordinary least-squares estimator $\hat\beta_{\mathrm{OLS}}=\arg\min_\beta\|Y-X\beta\|^2=(X'X)^{-1}X'Y$
is exactly the projection of $Y$ onto $\Theta$, so $\|Z_r\|^2=\|Y-X\hat\beta_{\mathrm{OLS}}\|^2=
\sum_i(Y_i-x_i'\hat\beta)^2$ is the **residual sum of squares**, $\mathrm{RSS}$. Projecting instead onto
the smaller subspace $\Theta_0$ gives the (necessarily larger) **null residual sum of squares**,
$\mathrm{RSS}_0=\|Z_1\|^2+\|Z_r\|^2$ — so $\|Z_1\|^2=\mathrm{RSS}_0-\mathrm{RSS}$ is exactly the extra fit
gained by letting the tested coefficients back into the model, and the $F$-test becomes
$$F=\frac{(\mathrm{RSS}_0-\mathrm{RSS})/(d-d_0)}{\mathrm{RSS}/(n-d)}.$$

**A single coefficient.** To isolate $\beta_1$ alone ($d_1=1$), first *partial out* the remaining
regressors: with $X_0=(X_2,\dots,X_d)$, let
$$X_{1\perp}=X_1-\mathrm{Proj}_{\Theta_0}(X_1)=X_1-X_0(X_0'X_0)^{-1}X_0'X_1$$
be what is left of $X_1$ once its overlap with the other columns is removed. Reparametrizing
$\theta=X\beta$ as $\theta=X_{1\perp}\beta_1+X_0\delta$, the two pieces are now orthogonal
($X_{1\perp}'X_0=0$ by construction), so — exactly as in the canonical model — the least-squares
estimates decouple:
$$\hat\beta_1=\frac{X_{1\perp}'Y}{\|X_{1\perp}\|^2},\qquad
\widehat{\mathrm{s.e.}}(\hat\beta_1)=\frac{\hat\sigma}{\|X_{1\perp}\|},$$
and the familiar regression-table $t$-statistic for a single coefficient is nothing but the canonical
$t$-statistic in the direction $q_1=X_{1\perp}/\|X_{1\perp}\|$:
$$t=\frac{\hat\beta_1}{\widehat{\mathrm{s.e.}}(\hat\beta_1)}\ \overset{H_0}\sim\ t_{n-d}.$$

### The two-sample $t$-test

$Y_1,\dots,Y_m\overset{\mathrm{iid}}\sim N(\mu,\sigma^2)$ and
$Y_{m+1},\dots,Y_{m+n}\overset{\mathrm{iid}}\sim N(\nu,\sigma^2)$, same unknown $\sigma^2$. The mean
vector lies in the two-dimensional subspace
$\Theta=\mathrm{span}\big((\mathbf1_m,-\mathbf1_n),\ \mathbf1_{m+n}\big)$, and $H_0:\mu=\nu$ says
$\theta\in\Theta_0=\mathrm{span}(\mathbf1_{m+n})$, so $d_0=1$, $d=2$, $d_r=m+n-2$. Orthogonalizing
$(\mathbf1_m,-\mathbf1_n)$ against $\mathbf1_{m+n}$ gives, up to scale, the contrast with $1/m$ on the
first block and $-1/n$ on the second, and the resulting canonical $t$-statistic is the familiar
pooled-variance two-sample statistic:
$$t=\frac{\bar Y_1-\bar Y_2}{\hat\sigma\sqrt{1/m+1/n}}\ \overset{H_0}\sim\ t_{m+n-2}.$$

### One-way ANOVA (fixed effects)

$Y_{k,i}\overset{\mathrm{ind.}}\sim N(\mu_k,\sigma^2)$ for $k=1,\dots,m$ groups of $n$ observations each,
testing $H_0:\mu_1=\cdots=\mu_m$. With group means $\bar Y_k$ and grand mean $\bar Y$, the full model has
$d=m$ free means and the null has $d_0=1$ (one common mean), so $d_r=m(n-1)$. Writing out the two
residual sums of squares,
$$\mathrm{RSS}=\sum_{k,i}(Y_{k,i}-\bar Y_k)^2=\|Y\|^2-n\sum_k\bar Y_k^2,\qquad
\mathrm{RSS}_0=\sum_{k,i}(Y_{k,i}-\bar Y)^2=\|Y\|^2-mn\bar Y^2,$$
the gain from letting the groups have separate means is
$$\mathrm{RSS}_0-\mathrm{RSS}=n\sum_k(\bar Y_k-\bar Y)^2,$$
and the $F$-statistic is the classic ratio of between-group to within-group variance:
$$F=\frac{\dfrac{n}{m-1}\sum_k(\bar Y_k-\bar Y)^2}{\dfrac1{m(n-1)}\sum_{k,i}(Y_{k,i}-\bar Y_k)^2}
=\frac{\text{between-group variance}}{\text{within-group variance}}.$$

## Sources

Everything in this chapter comes from the handwritten lecture notes for Berkeley STAT 210A, lecture 18
(dated 10/26 on the outline page), reconstructed by a model from a scanned PDF with no text layer — the
conversion itself flags every equation as unverified, so all display equations here were checked for
internal consistency (e.g. the $F$–Beta relation, the RSS identities) rather than taken on faith:

- `statistics/berkeley/stat210a/fall-2024/handwritten/lecture18-F24/01-outline.md` — the $\chi^2$, $t$,
  $F$ definitions and limiting relations, the one-sample $t$-test change-of-basis derivation, its
  geometric interpretation, and the Beta–$F$ relation.
- `statistics/berkeley/stat210a/fall-2024/handwritten/lecture18-F24/02-canonical-linear-model.md` — the
  canonical linear model, its four tests ($z$, $\chi^2$, $t$, $F$) and their comparison table, the
  confidence-set inversions, and the general linear model.
- `statistics/berkeley/stat210a/fall-2024/handwritten/lecture18-F24/03-ex-linear-regression.md` — the
  linear regression, two-sample $t$-test, and one-way ANOVA examples.

No slide deck, transcript, or problem set was supplied for this lecture — only these handwritten notes.
The notes remark, in passing, that the independence of $Z_1$ and $S^2$ in the one-sample derivation is
"already known, from Basu" — referring to an earlier lecture's use of Basu's theorem (completeness of the
sample mean plus ancillarity of the sample variance) that is not itself contained in this material.

---

[← 52. Multiparameter Exp. Families](52-multiparameter-exp-families.md) · [Contents](index.md) · [54. One-Sample T-Test and the Linear Model →](54-one-sample-t-test-and-the-linear-model.md)
