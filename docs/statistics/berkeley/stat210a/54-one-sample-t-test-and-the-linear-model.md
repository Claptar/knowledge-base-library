---
title: "54. One-Sample T-Test and the Linear Model"
course: "Berkeley Stat 210A"
chapter: 54
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 54. One-Sample T-Test and the Linear Model

## What this covers

This chapter answers a specific question: given normal data, how do you turn "test whether some
coordinates of the mean are zero" into a statistic with a known, computable null distribution —
and how far does that trick generalize? It builds the $\chi^2$, $t$ and $F$ distributions as the
natural byproduct of rotating a Gaussian vector into a well-chosen orthonormal basis, uses that
rotation to derive the one-sample $t$-test from first principles, and then abstracts the same
argument into the *canonical linear model* and the fully general linear model — of which ordinary
linear regression, the two-sample $t$-test and one-way ANOVA are all instances. It assumes the
multivariate normal distribution and its behaviour under affine maps, exponential families and
UMPU testing, and Basu's theorem, all established earlier in the course.

## The three Gaussian-adjacent distributions

Three distributions keep the calculations below closed-form, and all three arise from a standard
normal vector.

If $Z_1,\dots,Z_d\overset{\text{iid}}{\sim}N(0,1)$, then
$$V=\sum Z_i^2\sim\chi_d^2=\text{Gamma}\!\left(\tfrac d2,2\right),\qquad \mathbb EV=d,\quad
\text{Var}(V)=2d.$$
By the CLT, $(V-d)/\sqrt{2d}\Rightarrow N(0,1)$, so informally $V/d\approx N(1,2/d)\to1$: a
chi-squared variable divided by its degrees of freedom is a noisy estimate of $1$, and the noise
shrinks like $1/\sqrt d$.

If further $Z\sim N(0,\sigma^2)$ and $V\sim\sigma^2\chi_d^2$ independently of $Z$, then
$$\frac{Z}{\sqrt{V/d}}\sim t_d\ \Rightarrow\ N(0,1)\quad\text{as }d\to\infty,$$
which is exactly the "$V/d\to1$" fact applied to the denominator: dividing by an estimate of scale
that has become certain is the same as dividing by the true scale. Likewise, if
$V_1\sim\sigma^2\chi_{d_1}^2$ and $V_2\sim\sigma^2\chi_{d_2}^2$ are independent,
$$\frac{V_1/d_1}{V_2/d_2}\sim F_{d_1,d_2}\ \Rightarrow\ \frac1{d_1}\chi_{d_1}^2\quad\text{as
}d_2\to\infty,$$
by the same argument applied to the denominator alone. Two bridges between the three: if $T\sim
t_d$ then $T^2\sim F_{1,d}$, and if $U\sim\text{Beta}(d_1/2,d_2/2)$ then
$$\frac{U/d_1}{(1-U)/d_2}\sim F_{d_1,d_2}.$$

Everything below leans on one further fact about the multivariate normal: if $Z\sim N_d(\mu,
\Sigma)$, $A\in\mathbb R^{k\times d}$, $b\in\mathbb R^k$, then $AZ+b\sim N_k(A\mu+b,A\Sigma A')$. In
particular, an **orthogonal** change of basis ($AA'=I$) applied to $N_n(\mu,\sigma^2I_n)$ leaves the
covariance $\sigma^2I_n$ untouched and only moves the mean — the entire mechanism the rest of the
chapter runs on.

## The one-sample $t$-test, by rotating the sample

Take $X_1,\dots,X_n\overset{\text{iid}}{\sim}N(\mu,\sigma^2)$, i.e. $X\sim
N_n(\mu\mathbf1_n,\sigma^2I_n)$, and test $H_0:\mu=0$ against $H_1:\mu\ne0$. The UMPU test rejects
for extreme values of
$$R=\frac{\sqrt n\,\bar X}{\|X\|},$$
literally the (uncentred) correlation of the data vector $X$ with the constant direction
$\mathbf1_n$: it is $\cos\theta$, the cosine of the angle between $X$ and $\mathbf1_n$.

<figure>
<svg viewBox="0 0 320 220" role="img" aria-label="Decomposition of the sample vector X into its projection onto the constant direction and the orthogonal residual">
  <line x1="40" y1="190" x2="300" y2="190" stroke="currentColor" stroke-width="1.5"/>
  <text x="245" y="207" font-size="12" fill="currentColor">1&#8319; direction</text>
  <line x1="40" y1="190" x2="220" y2="55" stroke="currentColor" stroke-width="1.5"/>
  <text x="226" y="52" font-size="12" fill="currentColor">X</text>
  <line x1="220" y1="55" x2="220" y2="190" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="40" y1="190" x2="220" y2="190" stroke="currentColor" stroke-width="2.5"/>
  <text x="95" y="207" font-size="12" fill="currentColor">&#8730;n &#183; X&#772;</text>
  <text x="224" y="123" font-size="12" fill="currentColor">&#8730;((n&#8722;1)S&#178;)</text>
  <path d="M 75 190 A 35 35 0 0 0 68 169" fill="none" stroke="currentColor" stroke-width="1"/>
  <text x="78" y="176" font-size="11" fill="currentColor">&#952;</text>
</svg>
<figcaption>The sample vector X splits into a projection of length √n·X̄ along the constant
direction 1ₙ and a residual of length √((n−1)S²) orthogonal to it. R = cos θ is the uncentred
correlation the test statistic is built from.</figcaption>
</figure>

Equivalently,
$$T=\frac{\sqrt n\,\bar X}{\sqrt{S^2}}=\frac{\|\text{Proj}_{\mathbf1_n}X\|}
{\|\text{Proj}_{\mathbf1_n}^\perp X\|}\cdot\sqrt{n-1}\;\text{sgn}(\bar X)=\frac{R}{\sqrt{1-R^2}},$$
so $R$ and $T$ report the same angle two different ways.

**Change of basis.** To get the null distribution of $T$, rotate rather than compute directly. Let
$Q=(q_1\ \ Q_r)$ be orthogonal, with $q_1=\mathbf1_n/\sqrt n$ and $q_2,\dots,q_n$ completing an
orthonormal basis (Gram–Schmidt). Set $Z=Q'X$. Then $Z_1=q_1'X=\sqrt n\,\bar X$, and
$$\|Q_r'X\|^2=\|Q'X\|^2-\|q_1'X\|^2=\|X\|^2-n\bar X^2=(n-1)S^2\qquad(Q'Q=I_n).$$
Because $Q$ is orthogonal, $Q'X\sim N_n\big(Q'(\mu\mathbf1_n),\sigma^2I_n\big)$, and
$Q'(\mu\mathbf1_n)=\sqrt n\mu\,e_1$ since $q_1$ is exactly the unit vector along $\mathbf1_n$ and
every other $q_j$ is orthogonal to it. So $Z_1\sim N(\sqrt n\mu,\sigma^2)$ and $Z_r=Q_r'X\sim
N_{n-1}(0,\sigma^2I_{n-1})$, and — being jointly Gaussian with block-diagonal covariance —
independent. Hence
$$S^2=\frac1{n-1}\|Z_r\|^2\sim\frac{\sigma^2}{n-1}\chi_{n-1}^2,\qquad S^2\perp\!\!\!\perp Z_1$$
(the independence is exactly what Basu's theorem already gave, since $\bar X$ is complete
sufficient for $\mu$ when $\sigma^2$ is known and $S^2$ is ancillary; the rotation additionally
pins down the *distribution* of $S^2$). Dividing the $N(\sqrt n\mu,\sigma^2)$ variable $Z_1$ by an
independent $\sigma\sqrt{\chi_{n-1}^2/(n-1)}$ is exactly the recipe for a $t$-distribution, so under
$H_0$,
$$T=\frac{\sqrt n\,\bar X}{S}\sim t_{n-1},\qquad T^2=\frac{n\bar X^2}{S^2}\sim F_{1,n-1}.$$

**The decomposition this buys.** Because $\mathbf1_n$ and $\mathbf1_n^\perp$ are orthogonal, under
$H_0$
$$n\bar X^2\sim\sigma^2\chi_1^2,\qquad (n-1)S^2\sim\sigma^2\chi_{n-1}^2,\qquad
\|X\|^2=n\bar X^2+(n-1)S^2\sim\sigma^2\chi_n^2,$$
and the pieces combine so that
$$\frac{n\bar X^2}{\|X\|^2}=R^2\sim\text{Beta}\!\left(\frac12,\frac{n-1}2\right),\quad\text{independent
of }\|X\|^2.$$

## From one sample to many directions: the canonical linear model

The one-sample argument only used two facts about $\mathbf1_n$: it is one particular direction, and
rotating exposes it. Nothing stops the same argument from testing several directions at once, or
from separating out nuisance directions that are not under test. That abstraction is the
**canonical linear model**: split the coordinates of a rotated Gaussian vector
$$Z=\begin{pmatrix}Z_0\\Z_1\\Z_r\end{pmatrix}\begin{matrix}d_0\\d_1=d-d_0\\d_r=n-d\end{matrix}\sim
N_n\!\left(\begin{pmatrix}\mu_0\\\mu_1\\0\end{pmatrix},\sigma^2I_n\right),$$
and test $H_0:\mu_1=0$ vs. $H_1:\mu_1\ne0$ (one-sided if $d_1=1$). $Z_0$ carries $d_0$ nuisance
directions with unknown mean $\mu_0$, $Z_1$ carries the $d_1$ directions under test, and $Z_r$ is
pure noise — mean zero regardless of $H_0$ or $H_1$ — which is exactly what makes it usable to
estimate $\sigma^2$. This is again an exponential family,
$$p(z)\propto\exp\left\{\frac{\mu_1}{\sigma^2}{}'Z_1+\frac{\mu_0}{\sigma^2}{}'Z_0-
\frac1{2\sigma^2}\|Z\|^2\right\},$$
and the four combinations of "$\sigma^2$ known or not" and "$d_1=1$ or not" reproduce the four
Gaussian-adjacent distributions:

| | $\sigma^2$ known | $\sigma^2$ unknown |
|---|---|---|
| $d_1=1$ | $z$-test: $Z_1/\sigma\sim N(0,1)$ | $t$-test: $Z_1/\hat\sigma\sim t_{n-d}$ |
| $d_1\ge1$ | $\chi^2$-test: $\|Z_1\|^2/\sigma^2\sim\chi_{d_1}^2$ | $F$-test: $\dfrac{\|Z_1\|^2/d_1}{\hat\sigma^2}\sim F_{d_1,n-d}$ |

(In the $d_1\ge1$, $\sigma^2$-known row, rejecting for large $\|Z_1\|$ is the natural rule only
if there is no reason to prefer one direction of $\mu_1$ over another; an anisotropic prior on
$\mu_1$ would weight the coordinates of $Z_1$ differently before combining them.)

In every case $Z_0,Z_1,Z_r$ are mutually independent (jointly Gaussian, block-diagonal covariance),
so testing "conditional on $Z_0$" is the same as testing unconditionally with $Z_1$ alone — the
nuisance directions drop out entirely once isolated by rotation. When $\sigma^2$ is unknown, the
residual block supplies the estimate
$$\hat\sigma^2=\frac{\|Z_r\|^2}{n-d}\sim\frac{\sigma^2}{n-d}\chi_{n-d}^2,\qquad
\mathbb E\hat\sigma^2=\sigma^2,\quad\text{Var}(\hat\sigma^2)=\frac{2\sigma^4}{n-d},$$
independent of $Z_1$ for the same block-diagonal reason. Replacing $\sigma$ by $\hat\sigma$ in the
known-variance statistics is exactly what turns $N(0,1)$ into $t_{n-d}$ and $\chi_{d_1}^2$ into a
rescaled $F_{d_1,n-d}$ — matching the large-degrees-of-freedom limits already noted for $t$ and $F$.

## Confidence sets, by inverting the test

The same four statistics test $H_0:\mu_1=\mu_1^\circ$ for any fixed $\mu_1^\circ$, not only $0$:
recentre,
$$\begin{pmatrix}Z_0\\Z_1-\mu_1^\circ\\Z_r\end{pmatrix}\sim
N_n\!\left(\begin{pmatrix}\mu_0\\\mu_1-\mu_1^\circ\\0\end{pmatrix},\sigma^2I_n\right),$$
and run the test on $Z_1-\mu_1^\circ$ in place of $Z_1$. Collecting the $\mu_1^\circ$ that are
*not* rejected gives a confidence set for $\mu_1$ at whatever level the test controls:

- $d_1=1$, $\sigma^2$ known: $(Z_1-\mu_1)/\sigma\sim N(0,1)$, giving $Z_1\pm\sigma z_{\alpha/2}$.
- $d_1=1$, $\sigma^2$ unknown: $(Z_1-\mu_1)/\hat\sigma\sim t_{n-d}$, giving $Z_1\pm\hat\sigma\,
  t_{n-d}(\alpha/2)$.
- $d_1\ge1$, $\sigma^2$ known: $\|Z_1-\mu_1\|/\sigma$ has an upper-$\alpha$ quantile
  $c_{\chi^2}(\alpha)$ from the $\chi^2$-test, giving the ball $Z_1+\sigma\sqrt{c_{\chi^2}(\alpha)}
  \,B_1(0)$, where $B_1(0)=\{x:\|x\|\le1\}$.
- $d_1\ge1$, $\sigma^2$ unknown: likewise a ball of radius $\hat\sigma\sqrt{c_F(\alpha)}$ from the
  upper-$\alpha$ quantile of $F$.

A single test recipe produces both a $p$-value and a confidence region: the interval or ball is
just "every null hypothesis the data doesn't reject."

## The general linear model: any subspace hypothesis is canonical after rotation

The canonical model looks special because the mean is aligned with coordinate axes by assumption.
In practice a linear hypothesis is about an arbitrary subspace of $\mathbb R^n$, and rotation always
removes the difference. Observe $Y\sim N_n(\theta,\sigma^2I_n)$ and test
$$\theta\in\Theta_0\quad\text{vs.}\quad\theta\in\Theta\setminus\Theta_0,$$
where $\Theta_0\subseteq\Theta$ are subspaces of $\mathbb R^n$ with $\dim\Theta_0=d_0$,
$\dim\Theta=d=d_0+d_1$. Pick an orthonormal basis $Q=[Q_0\ Q_1\ Q_r]$ with $Q_0$ spanning
$\Theta_0$, $Q_1$ spanning $\Theta\cap\Theta_0^\perp$ (the directions inside the model that
$\Theta_0$ doesn't reach), and $Q_r$ spanning $\mathbb R^n\cap\Theta^\perp$ (the directions outside
the model entirely — pure noise). Because $Q$ is orthogonal it does to $\theta$ and to $\sigma^2I_n$
exactly what the rotation did in the one-sample case:
$$Z=Q'Y\sim N_n\!\left(\begin{pmatrix}Q_0'\theta\\Q_1'\theta\\0\end{pmatrix},\sigma^2I_n\right),
\qquad H_0:Q_1'\theta=0,$$
which is the canonical linear model verbatim, with $\mu_0=Q_0'\theta$, $\mu_1=Q_1'\theta$. Whichever
of the $z$/$\chi^2$/$t$/$F$ tests applies now applies here.

## Worked example: linear regression

Take $Y_i=x_i'\beta+\varepsilon_i$ with fixed $x_i\in\mathbb R^d$ and
$\varepsilon_i\overset{\text{iid}}{\sim}N(0,\sigma^2)$, i.e. $Y\sim N_n(X\beta,\sigma^2I_n)$ for the
design matrix $X$ with columns $X_1,\dots,X_d$ (assumed full column rank). The model space is
$\Theta=\text{Span}(X_1,\dots,X_d)$, and testing $H_0:\beta_1=\dots=\beta_{d_1}=0$ is testing
$\theta\in\Theta_0=\text{Span}(X_{d_1+1},\dots,X_d)$ (or $\theta=0$ if $d_1=d$). Rotating into
$Q_0,Q_1,Q_r$ as above gives
$$F\text{-stat}=\frac{\|Q_1'Y\|^2/d_1}{\|Q_r'Y\|^2/(n-d)},\qquad
t\text{-stat}=\frac{q_1'Y}{\sqrt{\|Q_r'Y\|^2/(n-d)}}\quad(d_1=1).$$

These become the familiar regression quantities once translated back. The least-squares estimate
$\hat\beta_{\text{OLS}}=\text{argmin}_\beta\|Y-X\beta\|^2=(X'X)^{-1}X'Y$ is exactly the orthogonal
projection of $Y$ onto $\Theta$, so
$$\|Q_r'Y\|^2=\|Y-\text{Proj}_\Theta Y\|^2=\sum_i\big(y_i-x_i'\hat\beta_{\text{OLS}}\big)^2=
\text{RSS},$$
with $n-d$ the **residual degrees of freedom**, and
$$\|Q_1'Y\|^2+\|Q_r'Y\|^2=\|\text{Proj}_{\Theta_0}^\perp Y\|^2=\text{RSS}_0\quad(\text{RSS of the
smaller, null model}),$$
so the $F$-statistic is the familiar comparison of nested models,
$$F=\frac{(\text{RSS}_0-\text{RSS})/(d-d_0)}{\text{RSS}/(n-d)}.$$

**A single coefficient, explicitly.** When $d_1=1$, write $X_0=(X_2\ \cdots\ X_d)$ and orthogonalize
$X_1$ against the rest:
$$X_{1\perp}=X_1-\text{Proj}_{\Theta_0}(X_1)=X_1-X_0(X_0'X_0)^{-1}X_0'X_1=X_1-X_0\gamma,$$
i.e. the part of $X_1$ the other regressors cannot predict. Reparametrizing $\theta=X\beta$ as
$\theta=X_{1\perp}\beta_1+X_0\delta$ (with $\delta=\beta_{-1}+\gamma\beta_1$) makes the two blocks of
columns orthogonal, so the normal equations decouple and
$$\hat\beta_1=\frac{X_{1\perp}'Y}{\|X_{1\perp}\|^2},\qquad
\widehat{\text{s.e.}}(\hat\beta_1)=\frac{\hat\sigma}{\|X_{1\perp}\|},\qquad
t=\frac{\hat\beta_1}{\widehat{\text{s.e.}}(\hat\beta_1)}.$$
The standard error of a single coefficient is governed entirely by $\|X_{1\perp}\|$: how much of
$X_1$'s variation is left over once the other predictors have explained what they can of it. A
regressor nearly collinear with the rest has small $\|X_{1\perp}\|$ and hence a large standard
error — the algebraic content of "multicollinearity inflates variance."

## Worked example: two-sample $t$-test (equal variance)

$Y_1,\dots,Y_m\overset{\text{iid}}{\sim}N(\mu,\sigma^2)$ and
$Y_{m+1},\dots,Y_{m+n}\overset{\text{iid}}{\sim}N(\nu,\sigma^2)$. As $\mu,\nu$ vary, the mean vector
$\theta=(\mu\mathbf1_m,\nu\mathbf1_n)$ ranges over
$\text{Span}\big((\mathbf1_m,-\mathbf1_n),\ \mathbf1_{m+n}\big)$ — a "grand mean" direction and a
"group contrast" direction — with $H_0:\mu=\nu$ exactly the grand-mean-only subspace
$\text{Span}(\mathbf1_{m+n})$, so $d_0=1$, $d=2$, $d_r=m+n-2$. Orthogonalizing the contrast
direction against $\mathbf1_{m+n}$ and normalizing gives the rejection rule
$$\frac{\frac1m\sum_{i\le m}Y_i-\frac1n\sum_{i>m}Y_i}
{\sqrt{\frac1m+\frac1n}\cdot\sqrt{\text{RSS}/(m+n-2)}}=\frac{\bar Y_1-\bar
Y_2}{\hat\sigma\sqrt{\frac1m+\frac1n}},$$
the pooled two-sample $t$-statistic, as an instance of the $t$-test in the general linear model,
with the pooled variance estimate $\hat\sigma^2=\text{RSS}/(m+n-2)$ playing the role of $\hat\sigma^2$
from the residual block.

## Worked example: one-way ANOVA (fixed effects)

$Y_{k,i}\overset{\text{ind.}}{\sim}\mu_k+\varepsilon_{k,i}$,
$\varepsilon_{k,i}\overset{\text{iid}}{\sim}N(0,\sigma^2)$, for $k=1,\dots,m$ groups of $n$
observations each, testing $H_0:\mu_1=\dots=\mu_m$. With $\bar Y_k$ the group means and $\bar Y$ the
grand mean, $d_0=1$, $d=m$, $d_r=m(n-1)$, and
$$\text{RSS}=\sum_{k,i}(Y_{k,i}-\bar Y_k)^2,\qquad \text{RSS}_0=\sum_{k,i}(Y_{k,i}-\bar Y)^2,\qquad
\text{RSS}_0-\text{RSS}=n\sum_k(\bar Y_k-\bar Y)^2,$$
so the $F$-statistic is the ratio everyone calls "between-group variance over within-group
variance":
$$F=\frac{\frac1{m-1}\,n\sum_k(\bar Y_k-\bar Y)^2}{\frac1{m(n-1)}\sum_{k,i}(Y_{k,i}-\bar Y_k)^2}.$$
It is the $F$-test of the general linear model applied to the subspace of vectors constant within
each group ($\Theta$, dimension $m$) against the subspace of vectors constant overall ($\Theta_0$,
dimension $1$) — no new machinery, only a new choice of $\Theta$ and $\Theta_0$.

## Sources

All from the Berkeley STAT 210A lecture on the one-sample $t$-test through the general linear model
("lecture18-linearmodel"), reconstructed by a model from handwritten lecture pages with no usable
text layer — every displayed equation in these files is flagged unverified by the conversion. The
same lecture recurs, essentially unchanged, across three offerings of the course:

- fall-2024: `handwritten/lecture18-linearmodel/01-one-sample-t-test.md`,
  `02-canonical-linear-model.md`, `03-ex-linear-regression.md`
- fall-2025: `handwritten/lecture18-linearmodel/01-outline.md`,
  `02-canonical-linear-model.md`, `03-ex-linear-regression.md`
- fall-2026: `handwritten/lecture18-linearmodel/01-outline.md`,
  `02-canonical-linear-model.md`, `03-ex-linear-regression.md`

This chapter follows the fall-2024 version, which is textually the same as the other two years
(one arithmetic detail — the informal CLT approximation $V/d\approx N(1,2/d)$ — is taken from the
fall-2025/2026 wording, since the fall-2024 file transcribes the variance differently). No slides,
transcript or problem set were supplied for this lecture; the vector diagram is redrawn from the
fall-2024 file's own description of its projection sketch. Basu's theorem and UMPU testing, invoked
in the notes as prior results ("we already knew, from Basu"), are earlier course material not
contained in these files.

---

[← 53. The Canonical Linear Model](53-the-canonical-linear-model.md) · [Contents](index.md) · [55. Convergence and the Delta Method (part 2) →](55-convergence-and-the-delta-method-part-2.md)
