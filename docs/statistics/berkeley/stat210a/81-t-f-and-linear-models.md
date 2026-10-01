---
title: "81. t, F, and Linear Models"
course: "Berkeley Stat 210A"
chapter: 81
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 81. t, F, and Linear Models

## What this covers

This chapter asks a single question in three guises: given normal data, why does testing a
hypothesis about a mean always reduce to comparing a squared "signal" length to a squared "noise"
length, and why are those two lengths always independent of one another? Working out the answer
produces the $t$ and $F$ distributions, and then a single template — the *canonical linear model*
— into which the one-sample $t$-test, the two-sample $t$-test, ordinary regression, and one-way
ANOVA all fit as special cases. It assumes the multivariate normal distribution and its invariance
under affine (in particular orthogonal) maps, the $\chi^2$ distribution as a sum of squared
standard normals, ordinary least squares, and — useful for one aside, not essential — Basu's
theorem and the idea of a complete sufficient statistic.

## The $\chi^2$, $t$, and $F$ distributions

**$\chi^2_d$.** If $X_1,\dots,X_d\sim N(0,1)$ are i.i.d., then $V=\sum_{i=1}^d X_i^2\sim\chi^2_d$.
Since each $X_i^2$ has mean $1$ and variance $2$, $\mathbb E[V]=d$ and $\mathrm{Var}(V)=2d$; and
since $V$ is a sum of $d$ i.i.d. terms, the CLT gives $V\approx N(d,2d)$ once $d$ is reasonably
large.

**$t_d$.** If $Z\sim N(0,1)$ and $V\sim\chi^2_d$ are independent, then
$$T=\frac{Z}{\sqrt{V/d}}\sim t_d.$$
This is the shape every $t$-statistic has: a standardized signal $Z$ divided by the square root of
an independent, unbiased estimate $V/d$ of its own variance. Informally, if $Y\sim N(\mu,1)$ and
$\hat\sigma^2$ is an independent estimate of the variance with $\hat\sigma^2\sim\chi^2_d/d$, then
$(Y-\mu)/\hat\sigma\sim t_d$ — exactly the situation in every example below, with $Y$ replaced by
whatever linear combination of the data carries the parameter being tested.

**$F_{d,d_2}$.** If $V\sim\chi^2_d$ and $V_2\sim\chi^2_{d_2}$ are independent,
$$F_{d,d_2}:=\frac{V/d}{V_2/d_2}.$$
Squaring a $t_d$ variable gives an $F$: if $T\sim t_d$, then
$T^2=\dfrac{Z^2}{V/d}=\dfrac{Z^2/1}{V/d}\sim F_{1,d}$, since $Z^2\sim\chi^2_1$.

**Large-degrees-of-freedom limits.** A $\chi^2_d$ variable is a sum of $d$ i.i.d. $\chi^2_1$ terms,
each with mean $1$, so by the law of large numbers $V/d\to1$ in probability as $d\to\infty$.
Feeding this into the definitions above: the denominator of $T=Z/\sqrt{V/d}$ converges to $1$, so
$t_d\Rightarrow N(0,1)$; and both the numerator and denominator of $F_{d,d_2}$ converge to $1$, so
$F_{d,d_2}\to1$ in probability as $d,d_2\to\infty$. This is why, once the degrees of freedom used
to estimate a variance are large, treating an estimated standard error as if it were the true one
(and using normal rather than $t$ quantiles) barely matters.

**A tool used repeatedly below.** If $Z\sim N_d(\mu,\Sigma)$ then $AZ+b\sim N_d(A\mu+b,A\Sigma A^\top)$
for any matrix $A$ and vector $b$. In particular, if $Q$ is orthogonal ($Q^\top Q=I$) then
$Q^\top Z\sim N_d(Q^\top\mu,\sigma^2I)$ when $\Sigma=\sigma^2I$ — rotating a vector with independent,
equal-variance normal coordinates leaves it with independent, equal-variance normal coordinates.
Everything below is repeated use of this one fact.

## Why signal and noise are independent: the geometric picture

Take $X\sim N_n(\mu,I_n)$ with $\mu=\alpha e_1$ for some unit vector $e_1$ — e.g. $e_1=\mu/\|\mu\|$
when $\mu\neq0$, so $\alpha=\|\mu\|$. Extend $e_1$ to a complete orthonormal basis $e_1,\dots,e_n$
of $\mathbb R^n$ (Gram–Schmidt). Writing $Q=(e_1\mid\cdots\mid e_n)$, an orthogonal matrix, and
$Z=Q^\top X$, the tool above gives
$$Z=\begin{pmatrix}Z_1\\Z_{2:n}\end{pmatrix}\sim N\!\left(\begin{pmatrix}\alpha\\0\end{pmatrix},I_n\right),$$
so $Z_1\sim N(\alpha,1)$ and $Z_{2:n}\sim N(0,I_{n-1})$. Because $Z$ is jointly Gaussian with a
block-diagonal (here, identity) covariance, $Z_1$ and $Z_{2:n}$ are not merely uncorrelated but
**independent** — this is the only place independence enters, and it is a statement about the
*rotated* coordinates, not about $X$'s original ones. Set $S=\|Z_{2:n}\|$; then $Z_1\perp S$.

<figure>
<svg viewBox="0 0 340 220" role="img" aria-label="A vector X split into its component along the mean direction e1 and an orthogonal residual, with a right angle between them.">
<defs>
<marker id="arrow-tf" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<polygon points="0,0 10,5 0,10" fill="currentColor"/>
</marker>
</defs>
<line x1="40" y1="180" x2="300" y2="180" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow-tf)"/>
<text x="298" y="198" text-anchor="end" font-size="12" fill="currentColor">e&#8321; (signal direction)</text>
<line x1="60" y1="180" x2="190" y2="60" stroke="currentColor" stroke-width="1.5" stroke-dasharray="4 3"/>
<line x1="60" y1="180" x2="190" y2="180" stroke="currentColor" stroke-width="2"/>
<line x1="190" y1="180" x2="190" y2="60" stroke="currentColor" stroke-width="2"/>
<polyline points="180,180 180,170 190,170" fill="none" stroke="currentColor" stroke-width="1"/>
<circle cx="60" cy="180" r="2.5" fill="currentColor"/>
<circle cx="190" cy="180" r="2.5" fill="currentColor"/>
<circle cx="190" cy="60" r="3" fill="currentColor"/>
<text x="52" y="196" font-size="12" fill="currentColor">0</text>
<text x="197" y="58" font-size="12" fill="currentColor">X</text>
<text x="125" y="197" text-anchor="middle" font-size="12" fill="currentColor">Z&#8321;</text>
<text x="197" y="122" font-size="12" fill="currentColor">S = &#8214;Z&#8322;&#8228;&#8345;&#8214;</text>
</svg>
<figcaption>Rotating to a basis with e₁ along the mean splits X into a component Z₁ along e₁ and an
orthogonal remainder of length S, living in the other n−1 directions. Because the rotated
coordinates are still independent normals, the right angle between the two pieces is exactly what
makes Z₁ and S independent, and ‖X‖² = Z₁² + S² splits a chi-squared variable into two independent
chi-squared pieces.</figcaption>
</figure>

Take $e_1=\mathbf1_n/\sqrt n$, so $\mu=\mu\mathbf1_n$ is a constant vector and $\alpha=\sqrt n\,\mu$.
Then $Z_1=\langle X,e_1\rangle=\sqrt n\,\bar X$, and — whichever orthonormal completion
$e_2,\dots,e_n$ of $e_1$ is used — $S^2=\|X\|^2-Z_1^2=\sum_iX_i^2-n\bar X^2=\sum_i(X_i-\bar X)^2$.
So the rotation argument reproves that **the sample mean and the sum of squared deviations of a
normal sample are independent** — a fact already available from Basu's theorem ($\bar X$ is
complete sufficient for $\mu$ when the variance is known, and $\sum(X_i-\bar X)^2$ is ancillary)
but reproved here by a construction general enough to reuse for any "signal direction," not only
the constant one.

Under $H_0:\mu=0$ (so $\alpha=0$), this gives an exact split of a $\chi^2_n$ into two independent
pieces:
$$\|X\|^2=n\bar X^2+\sum_{i=1}^n(X_i-\bar X)^2,\qquad n\bar X^2\sim\chi^2_1,\quad
\sum_{i=1}^n(X_i-\bar X)^2\sim\chi^2_{n-1},$$
independent of each other, consistent with $\chi^2_1+\chi^2_{n-1}=\chi^2_n$ in distribution.

This split also gives the Beta–$F$ correspondence used below. If $V_1\sim\chi^2_a$ and
$V_2\sim\chi^2_b$ are independent, write $U=V_1/(V_1+V_2)$; a standard fact about independent gamma
variables with a common scale is that $U\sim\mathrm{Beta}(a/2,b/2)$, independent of $V_1+V_2$.
Since $V_1/V_2=U/(1-U)$,
$$F_{a,b}=\frac{V_1/a}{V_2/b}=\frac ba\cdot\frac U{1-U}.$$
Taking $a=1$, $b=n-1$, $V_1=n\bar X^2$, $V_2=\sum(X_i-\bar X)^2$ recovers the one-sample $t$-statistic:
with $\hat\sigma^2=\sum(X_i-\bar X)^2/(n-1)$,
$$t^2=\left(\frac{\bar X}{\hat\sigma/\sqrt n}\right)^2=\frac{n\bar X^2}{\hat\sigma^2}
=(n-1)\frac{n\bar X^2}{\sum(X_i-\bar X)^2}=(n-1)\frac{V_1}{V_2}=F_{1,n-1},$$
exactly the general fact "$T^2\sim F_{1,d}$" from the previous section, instantiated with $d=n-1$.

## The canonical linear model

Every example below reduces, after a change of basis, to the following abstract problem. Let
$$Z=\begin{pmatrix}Z_0\\Z_1\end{pmatrix}\sim N\!\left(\begin{pmatrix}\mu\\0\end{pmatrix},\sigma^2I_d\right),
\qquad d=d_0+d_1,\ \mu\in\mathbb R^{d_0},$$
and test $H_0:\mu=0$ against $H_1:\mu\neq0$ (or a one-sided alternative, if $d_0=1$ and only
departures in one direction matter). Writing $z=(z_0,z_1)$, the density
$$f(z)=\frac1{(2\pi\sigma^2)^{d/2}}\exp\left(-\frac{\|z_1\|^2+\|z_0-\mu\|^2}{2\sigma^2}\right)$$
is an exponential family in $(\mu,\sigma^2)$, with $(Z_0,\|Z_1\|^2)$ sufficient.

**$\sigma^2$ known.** Conditioning on $Z_1$ costs nothing, since $Z_0\sim N(\mu,\sigma^2I_{d_0})$
regardless of $Z_1$. Reject for large $\|Z_0\|^2$ (a $\chi^2$-test); if $d_0=1$, reject for large
$|Z_0|$, or for large $Z_0$ alone if the alternative is one-sided.

**$\sigma^2$ unknown.** Now $\|Z_1\|^2$ is the natural estimate of the nuisance parameter:
$\mathbb E[\|Z_1\|^2/d_1]=\sigma^2$ and $\mathrm{Var}(\|Z_1\|^2/d_1)=2\sigma^4/d_1$, and — by the
rotation argument above, applied block by block — $Z_1$ is independent of $Z_0$. Under $H_0$,
$\|Z_0\|^2/\sigma^2\sim\chi^2_{d_0}$ and $\|Z_1\|^2/\sigma^2\sim\chi^2_{d_1}$ are independent, so the
unknown $\sigma^2$ cancels from their ratio:
$$F=\frac{\|Z_0\|^2/d_0}{\|Z_1\|^2/d_1}\sim F_{d_0,d_1}\quad\text{under }H_0.$$
Reject for large $F$ (an $F$-test, used when $d_0>1$); when $d_0=1$, the signed version
$$T=\frac{Z_0}{\sqrt{\|Z_1\|^2/d_1}}\sim t_{d_1}$$
is available and can be used one-sided if needed.

**A nuisance mean elsewhere.** If instead $Z\sim N(\mu,\sigma^2I_d)$ with $\mu$ arbitrary — not
necessarily zero on the $Z_1$ block — write $Z_0\sim N_{d_0}(\mu_0,\sigma^2I_{d_0})$,
$Z_1\sim N_{d_1}(\mu_1,\sigma^2I_{d_1})$. Everything above still holds with $Z_1-\mu_1$ in place of
$Z_1$, since $Z_1-\mu_1\sim N(0,\sigma^2I_{d_1})$, independent of $Z_0$. In particular
$\hat\sigma:=\sqrt{\|Z_1-\mu_1\|^2/d_1}$ is the natural estimate of $\sigma$ itself (not of
$\sigma^2$ times something else), and inverting the $t$- and $F$-statistics above gives, at level
$1-\alpha$:

- a confidence interval $\mu_0\in Z_0\pm t_{d_1,1-\alpha/2}\,\hat\sigma$;
- a confidence ellipsoid $\|\mu_0-Z_0\|^2\le\dfrac{d_0}{d_1}\|Z_1-\mu_1\|^2\,F_{d_0,d_1,1-\alpha}$;
- a prediction interval for one further, independent draw $Z_{\text{new}}\sim N(\mu_0,\sigma^2)$
  from the same block (taking $d_0=1$): since $Z_{\text{new}}-Z_0$ has variance $2\sigma^2$ and is
  independent of $Z_1$, $(Z_{\text{new}}-Z_0)/(\hat\sigma\sqrt2)\sim t_{d_1}$, so
  $Z_{\text{new}}\in Z_0\pm t_{d_1,1-\alpha/2}\,\hat\sigma\sqrt2$ — wider than the confidence
  interval for $\mu_0$ itself, because it must also cover the new observation's own noise, not just
  the uncertainty in $Z_0$.

## The general linear model

Now let $Y\sim N(X\beta,\sigma^2I_n)$ ($\sigma^2$ known or unknown), and suppose the hypothesis to
be tested is $\beta\in\Theta_0$ vs. $\beta\in\Theta_1$, where $\Theta_0\subset\Theta_1$ are
subspaces of $\mathbb R^p$ with $\dim\Theta_0=d_0$, $\dim\Theta_1=d=d_0+d_1$. The trick is always
the same: rotate into the canonical picture above.

Since $X\beta$ ranges over a subspace of $\mathbb R^n$ as $\beta$ does, choose an orthonormal basis
$Q=(Q_0\mid Q_1\mid Q_2)$ of $\mathbb R^n$ adapted to the nested subspaces: $Q_0$ (dimension $d_0$)
spans $\Theta_0$'s image, $Q_1$ (dimension $d_1$) spans the rest of $\Theta_1$'s image, and $Q_2$
(dimension $n-d$) spans what's left of $\mathbb R^n$ entirely outside $\Theta_1$'s image.
Rotating,
$$Z=Q^\top Y\sim N_n(Q^\top X\beta,\sigma^2I_n),$$
and by construction $Q_2^\top X\beta=0$ always — that direction lies outside $\Theta_1$'s image
regardless of $\beta$ — while $H_0$ says exactly that the $Q_1$-block of the mean also vanishes:
$H_0:Q_1^\top X\beta=0$.

Watch the relabeling relative to the canonical model just above: there, the tested block was
called $Z_0$, with dimension $d_0$, and everything else was the noise block $Z_1$, of dimension
$d_1=d-d_0$. Here the same role — zero under $H_0$, free under $H_1$ — is played by $Z_1$, of
dimension $d_1$; the genuine, hypothesis-independent noise is the extra block $Z_2$, of dimension
$n-d$, which the canonical model didn't need because there $\Theta_1$ was taken to be the whole
ambient space. Once the rotation is made, run whichever test fits: an $F$-test comparing $\|Z_1\|^2$
to $\|Z_2\|^2$ if $d_1>1$, or a $t$-test if $d_1=1$.

### Example: linear regression

Let $Y_i=X_i^\top\beta+\varepsilon_i$, $\varepsilon_i\sim N(0,\sigma^2)$ i.i.d., i.e.
$Y\sim N_n(X\beta,\sigma^2I_n)$ with $X\in\mathbb R^{n\times p}$ of full column rank. Here
$\Theta_1=\mathbb R^p$ (its image is $\mathrm{span}(X_1,\dots,X_p)$, dimension $d=p$), and the
hypothesis is $H_0:\beta=(\beta_0^\top,0^\top)^\top$ — the last $d_1$ coordinates of $\beta$ are
zero — so $\Theta_0=\mathrm{span}(X_1,\dots,X_q)$ with $q=p-d_1=d_0$.

Least squares gives $\hat\beta=\arg\min_\beta\|Y-X\beta\|^2=(X^\top X)^{-1}X^\top Y$,
$\hat Y=X\hat\beta$, and the residual sum of squares $\mathrm{RSS}=\|Y-\hat Y\|^2$. Fitting the
restricted model (only $X_1,\dots,X_q$) gives $\mathrm{RSS}_0$; fitting the full model gives
$\mathrm{RSS}_1$. Because $\Theta_0\subset\Theta_1\subset\mathbb R^n$, the restricted fit $\hat
Y_0$ (projection onto $\Theta_0$'s image) is also the projection of the full fit $\hat Y$ onto that
same subspace — projections onto nested subspaces compose — so $Y-\hat Y_0$, $\hat Y-\hat Y_0$, and
$Y-\hat Y$ form a right triangle:
$$\mathrm{RSS}_0=\|Y-\hat Y_0\|^2=\|Y-\hat Y\|^2+\|\hat Y-\hat Y_0\|^2=\mathrm{RSS}_1+\|\hat Y-\hat Y_0\|^2.$$
The middle term, $\|\hat Y-\hat Y_0\|^2=\mathrm{RSS}_0-\mathrm{RSS}_1$, is exactly $\|Z_1\|^2$ in
the rotated coordinates — the squared length of the piece the extra $d_1$ regressors add — and
$\mathrm{RSS}_1=\|Z_2\|^2$ is the squared length of the part of $Y$ genuinely outside the model.
The two are independent, being orthogonal blocks of the same rotated Gaussian vector, giving
$$F=\frac{(\mathrm{RSS}_0-\mathrm{RSS}_1)/d_1}{\mathrm{RSS}_1/(n-d)}\sim F_{d_1,n-d}\quad\text{under }H_0,$$
where $n-d$ is the *residual degrees of freedom*.

When only a single coefficient is tested ($d_1=1$, say $\beta_q=0$), there's a more computational
route to the same statistic. Write $X=(X_0\mid X_1)$ and residualize the tested column against the
rest: $X_1^\perp=X_1-\mathrm{Proj}_{X_0}X_1$. Then $X\beta=X_0\beta_0+X_1^\perp\beta_1$ is an
equivalent, now-orthogonal reparametrization, and the least-squares coefficient on the residualized
column,
$$\hat\beta_1=(X_1^{\perp\top}X_1^\perp)^{-1}X_1^{\perp\top}Y,$$
is the same number the full regression gives for that coefficient (the Frisch–Waugh–Lovell fact:
regressing $Y$ on $X_1^\perp$ alone, after removing $X_0$ from both $Y$ and $X_1$, recovers the
multiple-regression coefficient). Its estimated variance is
$\widehat{\mathrm{Var}}(\hat\beta_1)=\hat\sigma^2(X_1^{\perp\top}X_1^\perp)^{-1}$ with
$\hat\sigma^2=\mathrm{RSS}_1/(n-d)$, and
$$t=\frac{\hat\beta_1}{\mathrm{SE}(\hat\beta_1)}\sim t_{n-d}.$$

### Example: two-sample $t$-test (equal variances)

Let $Y_1,\dots,Y_n\sim N(\mu_1,\sigma^2)$ and $Y_{n+1},\dots,Y_{n+m}\sim N(\mu_2,\sigma^2)$, all
independent, stacked into $Y=(Y_1,\dots,Y_{n+m})^\top$ with mean constant at $\mu_1$ on the first
block and $\mu_2$ on the second. The model space is
$\Theta=\mathrm{span}\big(\mathbf1_{n+m},\,(\mathbf1_n^\top,0^\top)^\top\big)$, dimension $d=2$;
$H_0:\mu_1=\mu_2$ gives $\Theta_0=\mathrm{span}(\mathbf1_{n+m})$, dimension $d_0=1$, so $d_1=1$ and
the noise dimension is $n-d=n+m-2$.

Applying the same residualizing trick — orthogonalize the group indicator against the intercept
$\mathbf1_{n+m}$ — collapses this to the one-coefficient regression case above and reproduces the
familiar pooled two-sample $t$-statistic
$$t=\frac{\bar Y_1-\bar Y_2}{\hat\sigma\sqrt{\frac1n+\frac1m}}\sim t_{n+m-2},\qquad
\hat\sigma^2=\frac{\sum_{i=1}^n(Y_i-\bar Y_1)^2+\sum_{i=1}^m(Y_i-\bar Y_2)^2}{n+m-2}.$$
The $n+m-2$ degrees of freedom are exactly the $n-d$ of the general formula: two dimensions of the
$(n+m)$-dimensional space — one per group mean — are used up fitting the model, leaving $n+m-2$ to
estimate $\sigma^2$.

### Example: one-way ANOVA

Let $Y_{ki}\sim N(\mu_k,\sigma^2)$ for groups $k=1,\dots,m$ and observations $i=1,\dots,n$ per
group, and test $H_0:\mu_1=\cdots=\mu_m$. Reparametrizing as $Y_{ki}=\mu+\alpha_k+\varepsilon_{ki}$
with $\sum_k\alpha_k=0$ makes the group effects $\alpha_k$ identifiable and orthogonal to the grand
mean $\mu$; with $\bar Y_{k\cdot}=\frac1n\sum_iY_{ki}$ the group means and
$\bar Y=\frac1{mn}\sum_k\sum_iY_{ki}$ the grand mean, this is again an instance of the general
linear model — $\Theta_0=\mathrm{span}(\mathbf1)$ (dimension $1$) inside $\Theta_1=\mathrm{span}$
of the group indicators (dimension $m$) inside $\mathbb R^{mn}$ — so the same three-way orthogonal
split as in the regression example applies, this time comparing a *between-group* sum of squares
to a *within-group* sum of squares. **The supplied source material breaks off at exactly this
point**, right after defining $\bar Y_{k\cdot}$ and $\bar Y$, before writing out the sums of
squares or the resulting $F$-statistic explicitly.

## Sources

- All of this chapter comes from the "Testing linear hypotheses" reader of Berkeley STAT210A, in
  text that is identical across two conversions supplied for this chapter: the fall-2024 and
  fall-2026 `reader/testing-linear.qmd` (`01-t-and-f-distributions.md`, `02-canonical-linear-model.md`,
  `03-general-linear-model.md`) and the fall-2025 `reader/testing-linear.html` (`01-1-t-and-f-distributions.md`,
  `02-2-canonical-linear-model.md`, `03-3-general-linear-model.md`, duplicated verbatim under
  `units/reader/`). No slides, transcript, or exercises were supplied for this chapter.
- The source itself is truncated mid-sentence at the end of the one-way ANOVA example (it stops at
  "$\bar Y=\frac1{mn}\dots$"); the ANOVA $F$-statistic is not given in the supplied material and is
  not completed here.
- A few small inconsistencies in the raw reader — a scale factor on $n\bar X^2$'s stated Gamma
  distribution that breaks the additivity used two lines later, a stray extra factor of $\sigma$ in
  the canonical-model confidence interval and prediction interval, and a dimensional mismatch in
  "$H_0:Q_1'\beta=0$" — have been resolved here to match the surrounding derivation; in each case
  the fix is forced by a fact stated a few lines earlier in the same source (e.g. $\mathbb
  E[\|Z_1\|^2/d_1]=\sigma^2$ already identifies $\sqrt{\|Z_1-\mu_1\|^2/d_1}$ as the estimate of
  $\sigma$ itself, with nothing further to multiply it by).

---

[← 80. p-Values](80-p-values.md) · [Contents](index.md) · [82. Nuisance Parameters →](82-nuisance-parameters.md)
