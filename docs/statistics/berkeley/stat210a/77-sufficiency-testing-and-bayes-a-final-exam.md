---
title: "77. Sufficiency, Testing, and Bayes: A Final Exam"
course: "Berkeley Stat 210A"
chapter: 77
source: "https://github.com/berkeley-stat210a"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 210A](https://github.com/berkeley-stat210a), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 77. Sufficiency, Testing, and Bayes: A Final Exam

## What this covers

This chapter works through four problems from the Fall 2023 STAT 210A final examination (Prof.
Will Fithian), each a self-contained tour through a technique from earlier in the course:
exponential-family sufficiency and completeness, maximum likelihood asymptotics and a score test
against a non-i.i.d. alternative; hypothesis tests and confidence sets for multivariate normal
means alongside a James–Stein-style combined estimator; Rao–Blackwellization, consistency, the
delta method, and the continuous mapping theorem in a nonparametric two-sample model; and Bayes
point estimation, a minimax lower bound, and a scale-invariant loss function in the uniform scale
family. It assumes exponential families and sufficiency/completeness, the Cramér–Rao bound and
asymptotic normality of the MLE, the delta method, the James–Stein estimator, and Bayes and minimax
risk, all as covered earlier in the course.

## 1. The Laplace scale family: sufficiency, completeness, and a score test against decay

Let $X_1, \dots, X_n$ be i.i.d. draws from the **Laplace scale family**
$$X_i \sim \mathrm{Laplace}(0, \theta) : \quad p_\theta(x) = \frac{1}{2\theta} e^{-|x|/\theta}, \qquad x \in \mathbb{R}, \ \theta > 0.$$
The density is supported on all of $\mathbb{R}$ — this is a genuinely different family from the
Laplace *location* family used elsewhere in the course as a running example, where the unknown
parameter shifts the density rather than scaling it.

**(a) The absolute value is exponential.** For $0 \le a \le b < \infty$,
$$\begin{aligned}
\mathbb{P}(|X_i| \in [a,b]) &= \mathbb{P}(X_i \in [-b,-a]) + \mathbb{P}(X_i \in [a,b]) \\
&= \frac{1}{2}\left(\int_{-b}^{-a} \frac{1}{\theta} e^{x/\theta}\,dx + \int_a^b \frac{1}{\theta} e^{-x/\theta}\,dx\right) \\
&= \int_a^b \frac{1}{\theta} e^{-x/\theta}\,dx = \mathbb{P}(Y \in [a,b]),
\end{aligned}$$
where $Y \sim \mathrm{Exp}(\theta)$: the density folds the negative half-line onto the positive one,
and the two halves' contributions just double the tail. So $|X_i| \sim \mathrm{Exp}(\theta)$.

**(b) A complete sufficient statistic.** The likelihood is
$$p(x) = \left(\frac{1}{2\theta}\right)^n \exp\left\{-\frac{1}{\theta}\sum_i |x_i|\right\},$$
an exponential family with sufficient statistic $T(X) = \sum_i |X_i|$ and natural parameter
$1/\theta$. Because $1/\theta$ ranges over all of $(0,\infty)$ — an open interval, so the family has
full rank — the standard exponential-family fact applies: $T(X)$ is complete, and a complete
sufficient statistic is automatically minimal.

**(c) MLE and its asymptotics.** With $T = \sum_i |X_i|$, the log-likelihood is
$$\ell_n(\theta;X) = -n\log(2\theta) - \frac{1}{\theta}T(X), \qquad \dot\ell_n(\theta;X) = -\frac{n}{\theta} + \frac{T(X)}{\theta^2} = \frac{n}{\theta^2}\left(\frac{T(X)}{n} - \theta\right).$$
The score vanishes at $\hat\theta = T/n = \frac{1}{n}\sum_i |X_i|$, and since the sign of
$\dot\ell_n$ matches the sign of $T/n - \theta$, this is the global maximizer. The Fisher information
is
$$J_n(\theta) = \mathrm{Var}_\theta\!\left(\frac{T(X)}{\theta^2}\right) = n\theta^{-4}\,\mathrm{Var}_\theta(|X_i|) = n\theta^{-2},$$
using $\mathrm{Var}_\theta(|X_i|) = \theta^2$ for the $\mathrm{Exp}(\theta)$ variable from part (a).
Standard MLE theory then gives
$$\sqrt{n}(\hat\theta_n - \theta) \Rightarrow N(0,\theta^2).$$

**(d) Unbiasedness and the Cramér–Rao bound.** Since $\mathbb{E}_\theta|X_i| = \theta$, the average
$T/n$ is unbiased, with variance $\theta^2/n$ (an average of $n$ i.i.d. terms each of variance
$\theta^2$). This is exactly $1/J_n(\theta) = \theta^2/n$: the MLE attains the Cramér–Rao lower
bound here, not just asymptotically but in finite samples.

**(e) A score test against a decaying scale.** Suppose instead we worry the scale is shrinking
geometrically: $X_i \sim \mathrm{Laplace}(0, \theta_0(1-\delta)^i)$ for $i=1,\dots,n$, with
$\theta_0$ known for now, and we want to test $H_0: \delta = 0$ against $H_1: \delta > 0$. The
log-likelihood is
$$\ell_n(\delta;X) = \sum_i \left[-\log(2\theta_0) - i\log(1-\delta) - \frac{|X_i|/\theta_0}{(1-\delta)^i}\right],$$
with derivative
$$\dot\ell_n(\delta;X) = \sum_i\left[\frac{i}{1-\delta} - \frac{i|X_i|/\theta_0}{(1-\delta)^{i+1}}\right].$$
At $\delta = 0$ this is $\dot\ell_n(0;X) = \sum_{i=1}^n i(1 - |X_i|/\theta_0)$, and since
$|X_i|/\theta_0 \sim \mathrm{Exp}(1)$ has variance $1$ under the null, the Fisher information there is
$$J_n(0) = \mathrm{Var}_0(\dot\ell_n(0;X)) = \sum_{i=1}^n i^2 \,\mathrm{Var}(|X_i|/\theta_0) = \sum_{i=1}^n i^2.$$
The normalized score statistic
$$Z = \frac{\sum_{i=1}^n i(1 - |X_i|/\theta_0)}{\left(\sum_{i=1}^n i^2\right)^{-1/2}} \Rightarrow N(0,1)$$
(the exam takes the asymptotic normality of this non-i.i.d. score statistic as given) is compared to
$z_\alpha$ for a one-sided test, since the alternative is one-sided.

**(f) Removing the nuisance parameter (starred).** If $\theta_0$ is also unknown, the score test
above cannot be run directly. The move is to **condition on a statistic that is sufficient for
$\theta_0$ under the null submodel**: here that is $T(X) = \sum_i|X_i|$ (part (b)). Substituting the
plug-in $\hat\theta_0 = T/n$ into the score statistic gives
$$W = \frac{\sum_{i=1}^n i(1 - |X_i|n/T)}{\left(\sum_{i=1}^n i^2\right)^{-1/2}},$$
and rejecting for large $W$ is equivalent, up to an affine transformation, to rejecting for small
values of $\sum_i i|X_i|/T$. Because $W$ is a function of $X/T$ only, its distribution under the null
does not depend on $\theta_0$ at all — it can be found by simulation rather than by an asymptotic
argument, restoring finite-sample control of the Type I error. Concretely, under the null the vector
$D = (|X_1|,\dots,|X_n|)/T$ is $\mathrm{Dirichlet}(\mathbf{1}_n)$ and independent of $T$, so simulating
$D$ (equivalently, simulating $(|X_1|,\dots,|X_n|)$ given $T=t$ as $t \cdot D$) gives the exact
conditional null distribution of the test statistic, from which the cutoff is read off numerically.
This is the general principle of building a **similar test** by conditioning on a sufficient
statistic for the nuisance parameter under the null.

## 2. Multivariate normal means: tests, intervals, and a Stein estimator

Now suppose we observe two independent multivariate normal vectors in $\mathbb{R}^d$, $d \ge 3$:
$$X^{(i)} \sim N_d(\theta^{(i)}, \sigma^2 I_d), \quad i=1,2, \qquad \theta^{(1)},\theta^{(2)} \in \mathbb{R}^d.$$

**(a) Known variance: a $\chi^2$ test.** Set $Y = X^{(2)} - X^{(1)} \sim N_d(\theta^{(2)}-\theta^{(1)}, 2\sigma^2 I_d)$.
Under $H_0: \theta^{(1)} = \theta^{(2)}$,
$$\frac{1}{2\sigma^2}\|Y\|^2 \sim \chi^2_d,$$
so the test rejects when this exceeds the upper-$\alpha$ quantile of $\chi^2_d$.

**(b) Unknown variance, common shift: a one-sample $t$-test.** Suppose now $\sigma^2$ is unknown but
every coordinate is shifted by the same amount, $\theta^{(2)}_j = \theta^{(1)}_j + \delta$. Then
$Y \sim N_d(\delta\mathbf{1}_d, 2\sigma^2 I_d)$, which is exactly the setup of a one-sample $t$-test
on the $d$ "observations" $Y_1,\dots,Y_d$: reject $H_0:\delta=0$ against $\delta \ne 0$ when
$$\frac{|\overline{Y}|}{\sqrt{S^2/d}} > t_{d-1}(\alpha/2),$$
where $\overline{Y} = \frac{1}{d}\sum_j Y_j \sim N(\delta, 2\sigma^2/d)$ and
$S^2 = \frac{1}{d-1}\sum_j(Y_j-\overline{Y})^2 \sim \frac{2\sigma^2}{d-1}\chi^2_{d-1}$, independently
of $\overline{Y}$.

**(c) Inverting the test for a confidence interval.** Testing the point null $\delta=\delta_0$ shifts
the problem to $Y - \delta_0\mathbf{1}_d \sim N_d((\delta-\delta_0)\mathbf{1}_d, 2\sigma^2 I_d)$, and
inverting the rejection region of part (b) gives the interval
$$\overline{Y} \pm \sqrt{S^2/d}\cdot t_{d-1}(\alpha/2).$$

**(d) A Stein estimator built from orthogonal contrasts (starred).** Drop the shift assumption, fix
$\sigma^2=1$, and suppose only that we believe $\theta^{(1)} \approx \theta^{(2)}$ without a strong
prior on how. The trick is to rotate to two **independent** orthogonal contrasts:
$$Z = \frac{X^{(2)}-X^{(1)}}{\sqrt{2}} \sim N_d(\mu, I_d), \qquad W = \frac{X^{(1)}+X^{(2)}}{\sqrt 2} \sim N_d(\nu, I_d),$$
where $\mu = (\theta^{(2)}-\theta^{(1)})/\sqrt2$ and $\nu=(\theta^{(1)}+\theta^{(2)})/\sqrt2$. $Z$ and
$W$ are independent because they are orthogonal linear images of $(X^{(1)},X^{(2)})$. Since we
believe $\theta^{(1)}\approx\theta^{(2)}$, i.e. $\mu \approx 0$, apply a **James–Stein estimator**
to $Z$ but the plain MLE to $W$:
$$\hat\mu = \left(1 - \frac{d-2}{\|Z\|^2}\right)Z, \qquad \hat\nu = W.$$
Undoing the rotation, $\theta^{(2)} = (\mu+\nu)/\sqrt2$ and $\theta^{(1)} = (\nu-\mu)/\sqrt2$, so
$$\hat\theta^{(2)} = \frac{X^{(1)}+X^{(2)}}{2} + \left(1 - \frac{2d-4}{\|X^{(2)}-X^{(1)}\|^2}\right)\frac{X^{(2)}-X^{(1)}}{2}, \qquad
\hat\theta^{(1)} = \frac{X^{(1)}+X^{(2)}}{2} - \left(1 - \frac{2d-4}{\|X^{(2)}-X^{(1)}\|^2}\right)\frac{X^{(2)}-X^{(1)}}{2}.$$
The total MSE for $(\theta^{(1)},\theta^{(2)})$ splits as the sum of the MSEs of $\hat\mu$ and
$\hat\nu$: $\hat\nu = W$ has MSE exactly $d$, and the James–Stein estimator $\hat\mu$ always has MSE
strictly less than $d$ (equal to $2$ exactly when $\mu = 0$, i.e. when $\theta^{(1)}=\theta^{(2)}$).
So the combined estimator has MSE strictly less than $2d$ everywhere, dropping to $d+2$ precisely
where our guess $\theta^{(1)} \approx \theta^{(2)}$ is exactly right.

## 3. A nonparametric two-sample problem: Rao–Blackwellization and asymptotics

Let $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} P$ and, independently, $Y_1,\dots,Y_n \stackrel{\text{i.i.d.}}{\sim} Q$,
real-valued and with no further assumption on $P,Q$. Two facts are given as tools: in the
one-sample nonparametric model the order statistics $S(X) = (X_{(1)},\dots,X_{(n)})$ are complete
sufficient; and if $Z_n \Rightarrow Z$, $W_n \Rightarrow W$ with $Z_n \perp W_n$ for every $n$, then
$(Z_n,W_n) \Rightarrow (Z,W)$ with $Z \perp W$. Here $(S(X),S(Y))$ is (without proof) complete
sufficient for the joint model.

**(a) UMVU by Rao–Blackwellization.** For the estimand $g(P,Q) = \mathbb{P}_{X\sim P, Y\sim Q}(X>Y)$,
start from the trivially unbiased $\mathbf{1}\{X_1 > Y_1\}$ and Rao–Blackwellize by conditioning on
the complete sufficient statistic. Conditional on $(S(X),S(Y))$, $X_1$ and $Y_1$ are independent
uniform draws from the two order-statistic sets, so the UMVU estimator is
$$\frac{1}{n^2}\sum_{i,j=1}^n \mathbf{1}\{X_i > Y_j\}$$
(a close relative of the Mann–Whitney statistic). Two natural-looking alternatives fail:
$\frac{1}{n}\sum_i \mathbf{1}\{X_i>Y_i\}$ is unbiased but is *not* a function of the sufficient
statistic, so by Lehmann–Scheffé it cannot be the UMVU estimator; and $\frac{1}{n}\sum_i \mathbf{1}\{X_{(i)}>Y_{(i)}\}$
(pairing the ordered samples) is not even unbiased. The correct estimator can equally well be
written with ordered values, $\frac{1}{n^2}\sum_{i,j}\mathbf{1}\{X_{(i)}>Y_{(j)}\}$, as long as all
$n^2$ pairs appear once.

**(b) Consistency via the continuous mapping theorem.** With $\mu=\mathbb{E}_P X$, $\nu=\mathbb{E}_Q Y > 0$,
$\sigma^2 = \mathrm{Var}_P(X)$, $\tau^2=\mathrm{Var}_Q(Y)$ finite and positive, the law of large
numbers gives $\overline X \to \mu$, $\overline Y \to \nu$ in probability, and
$f(x,y)=(x/y)^2$ is continuous everywhere except at $y=0$ — which $\overline Y$ avoids in the
limit — so $T(X,Y) = (\overline X/\overline Y)^2 \to \theta = (\mu/\nu)^2$ in probability by the
continuous mapping theorem.

**(c) Asymptotic normality via the delta method.** The joint CLT gives
$$\sqrt n\left(\binom{\overline X_n}{\overline Y_n} - \binom{\mu}{\nu}\right) \Rightarrow N_2(0,D), \qquad D = \begin{pmatrix}\sigma^2 & 0\\ 0 & \tau^2\end{pmatrix}.$$
The gradient of $f(x,y)=(x/y)^2$ at $(\mu,\nu)$ (with $\nu\ne0$) is
$\nabla f(\mu,\nu) = (2\mu/\nu^2,\, -2\mu^2/\nu^3)$, so the delta method gives
$$\sqrt n(T-\theta) \Rightarrow N(0,\omega^2), \qquad \omega^2 = \nabla f(\mu,\nu)'D\nabla f(\mu,\nu) = 4\left(\frac{\mu^2\sigma^2}{\nu^4}+\frac{\mu^4\tau^2}{\nu^6}\right) = \frac{4}{\nu^2}\left(\theta\sigma^2+\theta^2\tau^2\right).$$

**(d) The degenerate case $\mu=\nu=0$.** Here $Z=\sqrt n(\overline X_n,\overline Y_n) \Rightarrow N_2(0,D)$
directly (no further scaling needed), and the continuous mapping theorem still applies to
$T=(Z_1/Z_2)^2$ even though $f$ is discontinuous at $Z_2=0$: the relevant, slightly more general
form of the theorem only needs the set of discontinuities to have measure zero under the *limiting*
law, which is true here since $N_2(0,D)$ puts no mass on $\{z_2=0\}$ — unlike in part (b), where the
argument instead leaned on convergence in probability to a fixed point away from the discontinuity.
Writing $Z_1=\sigma U$, $Z_2=\tau V$ with $U,V$ independent standard normal,
$$T = (Z_1/Z_2)^2 = \frac{\sigma^2}{\tau^2}\cdot\frac{U^2}{V^2} \Rightarrow \frac{\sigma^2}{\tau^2}F_{1,1}.$$
A reader uneasy about invoking the relaxed continuous mapping theorem can get the same conclusion
more carefully by truncating, $T_B(X,Y) = \min(T,B)$: since $f(x,y)=\min((x/y)^2,B)$ *is* continuous
everywhere, $T_B \Rightarrow \min(\sigma^2F_{1,1}/\tau^2, B)$ for every $B$, and letting $B\to\infty$
shows the cdf of $T$ converges everywhere to the (continuous) limiting cdf.

## 4. Bayes estimation for the uniform scale family

Let $X \sim \mathrm{Unif}[0,\theta]$, with mean $\theta/2$ and variance $\theta^2/12$. Recall the
$\mathrm{Pareto}(x_0,\alpha)$ density $p_{x_0,\alpha}(x) = \alpha x_0^\alpha/x^{\alpha+1}$ for
$x \ge x_0$.

**(a) A conjugate Pareto prior.** With prior $\lambda(\theta) \propto \theta^{-(\alpha+1)}\mathbf{1}\{\theta\ge\theta_0\}$
and likelihood $p_\theta(x) = \theta^{-1}\mathbf{1}\{x\le\theta\}$, the posterior is
$$\lambda(\theta\mid x) \propto \theta^{-(\alpha+2)}\mathbf{1}\{\theta\ge\theta_0\}\mathbf{1}\{\theta\ge x\} = \theta^{-(\alpha+2)}\mathbf{1}\{\theta \ge \max(x,\theta_0)\} \propto \mathrm{Pareto}(\max(x,\theta_0),\,\alpha+1).$$
Under squared error loss the Bayes estimator is the posterior mean,
$\hat\theta = (1+1/\alpha)\max(\theta_0, X)$.

The reason this is worth doing carefully is a genuine trap: both the uniform and the Pareto family
have parameter-dependent support, so the two indicator functions cannot be dropped the way they
usually can when a family's support is fixed. Writing the posterior as $\mathrm{Pareto}(\theta_0,\alpha+1)$
— ignoring the data-dependent floor — gives a distribution that doesn't depend on $x$ at all, which
should immediately look wrong: the data must move the posterior.

**(b) A polynomial prior.** With $\lambda(\theta) = 2\theta\,\mathbf{1}\{0\le\theta\le1\}$, the
posterior is
$$\lambda(\theta\mid x) \propto 2\theta\cdot\mathbf{1}\{\theta\le1\}\cdot\theta^{-1}\mathbf{1}\{x\le\theta\} = 2\cdot\mathbf{1}\{x\le\theta\le1\} \propto \mathrm{Unif}[x,1]$$
(again, a wrong answer here — $\mathrm{Unif}[0,1]$, forgetting that the data truncates the support
from below — is the same trap as in part (a)). The Bayes estimator is $(1+X)/2$, with
$$\mathrm{MSE}(\theta) = \left(\frac{1}{2}-\frac{3\theta}{4}\right)^2 + \frac{\theta^2}{48} = \frac{7}{12}\theta^2 - \frac{3}{4}\theta + \frac{1}{4},$$
and integrating against the prior gives the Bayes risk
$$\int_0^1 2\theta\left(\frac{7}{12}\theta^2-\frac{3}{4}\theta+\frac{1}{4}\right)d\theta = \frac{7}{24}-\frac{1}{2}+\frac{1}{4} = \frac{1}{24}.$$

**(c) The minimax risk is infinite (starred).** To see this, rescale part (b): take the prior
$\frac{2\theta}{B^2}\mathbf{1}\{0\le\theta\le B\}$ for $B>0$. Writing $Y=X/B$, $\zeta=\theta/B$
reduces this exactly to part (b)'s problem, so its Bayes estimator is $(X+B)/2$ and its Bayes risk
scales by $B^2$:
$$\mathbb{E}\big[((X+B)/2-\theta)^2\big] = B^2\,\mathbb{E}\big[((Y+1)/2-\zeta)^2\big] = \frac{B^2}{24}.$$
Since the Bayes risk of *any* prior lower-bounds the minimax risk, and $B^2/24 \to \infty$ as
$B\to\infty$, the minimax risk for squared error loss on this problem must be infinite. This is the
general pattern for showing a minimax risk is unbounded: exhibit a family of priors whose Bayes
risks diverge.

**(d) A scale-invariant loss.** Under squared *relative* error loss $L(\hat\theta,\theta) = ((\hat\theta-\theta)/\theta)^2$,
restrict to linear estimators $aX$. The risk is
$$R(\theta) = \frac{1}{\theta^2}\Big[(a\,\mathbb{E}_\theta X-\theta)^2 + a^2\mathrm{Var}_\theta(X)\Big] = \left(\frac a2-1\right)^2+\frac{a^2}{12} = \frac{a^2}{3}-a+1,$$
which is a constant function of $a$ alone — the $\theta$-dependence cancels entirely, because
relative error loss combined with a pure scale family makes the risk scale-invariant. Minimizing
over $a$ gives $a=3/2$, with constant risk $1/4$ for every $\theta$.

## Exercises

**1. Laplace scale family.** With $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} \mathrm{Laplace}(0,\theta)$,
$p_\theta(x) = \frac{1}{2\theta}e^{-|x|/\theta}$ on $\mathbb{R}$:

(a) Show $|X_i| \sim \mathrm{Exp}(\theta)$.
(b) Find a minimal sufficient statistic for the model. Is it complete?
(c) Find the MLE for $\theta$ and its asymptotic distribution.
(d) Show the estimator from (c) is unbiased. Does it attain the Cramér–Rao lower bound?
(e) Now suppose $X_i \sim \mathrm{Laplace}(0,\theta_0(1-\delta)^i)$ for $i=1,\dots,n$, with $\theta_0$
known. Propose a score test of $H_0:\delta=0$ against $H_1:\delta>0$, with an explicit statistic and
an asymptotic cutoff.
(f) *(Starred.)* Now suppose $\theta_0$ is also unknown. Modify the test from (e) so that it has
finite-sample control of the Type I error rate, explaining how you would find the cutoff without
knowing $\theta_0$.

**2. Multivariate normal means.** Let $X^{(i)} \stackrel{\text{ind.}}{\sim} N_d(\theta^{(i)},\sigma^2 I_d)$
for $i=1,2$, $d\ge3$.

(a) With $\sigma^2$ known, propose a test of $H_0:\theta^{(1)}=\theta^{(2)}$ against
$\theta^{(1)}\ne\theta^{(2)}$, with a cutoff in terms of a $\chi^2$ quantile.
(b) With $\sigma^2$ unknown and $\theta^{(2)}_j=\theta^{(1)}_j+\delta$ for all $j$ (a common shift),
propose a finite-sample test of $H_0:\delta=0$ against $\delta\ne0$.
(c) Under the same assumptions, give a confidence interval for $\delta$.
(d) *(Starred.)* With $\theta^{(1)},\theta^{(2)}$ unrestricted and $\sigma^2=1$, and a belief that
$\theta^{(1)}\approx\theta^{(2)}$ without further information, propose an estimator of
$(\theta^{(1)},\theta^{(2)})$ with MSE less than $2d$ everywhere, but MSE $d+2$ whenever
$\theta^{(1)}=\theta^{(2)}$.

**3. A nonparametric two-sample problem.** Let $X_1,\dots,X_n \stackrel{\text{i.i.d.}}{\sim} P$ and,
independently, $Y_1,\dots,Y_n \stackrel{\text{i.i.d.}}{\sim} Q$, both real-valued, with
$(S(X),S(Y))$ complete sufficient for the joint model.

(a) Find the UMVU estimator of $g(P,Q)=\mathbb{P}_{X\sim P,Y\sim Q}(X>Y)$ and justify its optimality.
(b) With $\mu=\mathbb{E}_PX$, $\nu=\mathbb{E}_QY>0$, $\sigma^2=\mathrm{Var}_P(X)$,
$\tau^2=\mathrm{Var}_Q(Y)$ finite and positive, show $T(X,Y)=(\overline X/\overline Y)^2$ is
consistent for $\theta=(\mu/\nu)^2$.
(c) Give the asymptotic distribution of $T$, appropriately normalized, with parameters expressed in
terms of $\mu,\nu,\sigma^2,\tau^2,\theta$.
(d) *(Starred.)* If $\mu=\nu=0$, give the (appropriately normalized, if necessary) asymptotic
distribution of $T$, and justify the argument.

**4. Bayes estimation for the uniform scale family.** Let $X\sim\mathrm{Unif}[0,\theta]$. Assume
squared error loss for parts (a)–(c).

(a) Show $\theta\sim\mathrm{Pareto}(\theta_0,\alpha)$ is conjugate, and find the posterior and Bayes
estimator.
(b) Repeat for the prior $\lambda(\theta)=2\theta\,\mathbf{1}\{0\le\theta\le1\}$: find the Bayes
estimator and the Bayes risk.
(c) *(Starred.)* Is the minimax risk for this problem finite? Prove it is infinite, or exhibit a
finite upper bound. (Hint: consider a version of the problem with $\theta$ bounded above by some
$B>0$.)
(d) Under squared relative error loss $L(\hat\theta,\theta)=((\hat\theta-\theta)/\theta)^2$, find the
best estimator of the form $aX$ ($a>0$): the minimizing $a$ and the resulting risk as a function of
$\theta$.

## Sources

All of this chapter is drawn from the Fall 2023 STAT 210A (UC Berkeley, Prof. Will Fithian) final
examination question booklet, which is a combined problem-and-solution document (the exam booklet
itself, converted together with its solutions):

- Title page and exam instructions: `01-final-examination-question-booklet.md`
- Problem 1, Laplace location family: `02-1-laplace-location-family-24-points-4-points-part.md`
- Problem 2, multivariate normal means: `03-2-multivariate-normal-means-20-points-5-points-part.md`
- Problem 3, nonparametric two-sample problem: `04-3-nonparametric-two-sample-problem-20-points-5-points-part.md`
- Problem 4, Bayes estimation for the uniform scale family: `05-4-bayes-estimation-for-uniform-scale-family-20-points-5-poin.md`

all under `docs/statistics/berkeley/stat210a/fall-2024/old-exams/solution2023/` in the
knowledge-base-library repository. Byte-identical copies of the same booklet, differing only in
which course-instance directory they are filed under, also appear under the `fall-2025`,
`fall-2025/units`, and `fall-2026` `old-exams/solution2023/` directories; only the `fall-2024` copy
is cited above.

The source markdown carries its own provenance note worth repeating here: it was reconstructed by a
model from a PDF with no extractable text layer, the prose is a paraphrase in places, and **every
equation in it is unverified against the original PDF**. This chapter reorganizes and explains that
material but does not independently re-derive or check it against the source PDF; treat the
mathematics here with the same caveat the source itself carries.

No slides or lecture transcript were supplied for this chapter — the entire input is the exam
booklet listed above.

---

[← 76. Regression with Correlated Errors](76-regression-with-correlated-errors.md) · [Contents](index.md) · [78. Sufficiency and Minimal Sufficiency (part 2) →](78-sufficiency-and-minimal-sufficiency-part-2.md)
