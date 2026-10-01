---
title: "107. Multiple Frequencies and Change-of-Slope Models"
course: "Berkeley Stat 153"
chapter: 107
source: "https://github.com/berkeley-stat153"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the material of [Berkeley Stat 153](https://github.com/berkeley-stat153), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 107. Multiple Frequencies and Change-of-Slope Models

## What this covers

This chapter works out two nonlinear regression models built on the same machinery: a parameter
that enters the mean function nonlinearly (a frequency, or a time breakpoint), profiled out against
a residual-sum-of-squares function, with everything else handled by ordinary linear regression. It
assumes the single-frequency sinusoidal model, its RSS and posterior formula, and the periodogram
shortcut for computing RSS quickly — all recapped here from an earlier lecture (referred to in the
source as "Lecture 7," not itself part of this material) — together with the Bayesian machinery for
plain linear regression (the posterior for $\beta$ and $\sigma$ given a fixed design matrix,
referred to here as "Problem 4 in Homework 1," also not supplied). The two models covered are
sinusoidal regression with several frequencies at once, and the change-of-slope ("broken-stick")
model for a trend with a kink in it.

## The shared recipe

Every model in this chapter has the same shape: a mean function that is linear in most of its
parameters but nonlinear in a low-dimensional parameter $\theta$ (a frequency, or a pair of
frequencies, or a breakpoint). Write it as
$$y = X_\theta \beta + \epsilon, \qquad \epsilon_t \overset{\text{i.i.d}}{\sim} N(0,\sigma^2),$$
where $X_\theta$ is a design matrix that depends on $\theta$. If $\theta$ were known, this would be
ordinary linear regression. The device for handling the unknown $\theta$ is to profile out $\beta$:
$$RSS(\theta) := \min_\beta \|y - X_\theta \beta\|^2 = \|y - X_\theta \hat\beta_\theta\|^2, \qquad
\hat\beta_\theta = (X_\theta^T X_\theta)^{-1} X_\theta^T y.$$
The maximum likelihood estimate of $\theta$ minimizes $RSS(\theta)$; in practice this is done by
evaluating $RSS$ over a grid of candidate $\theta$ values and taking the arg-min. For Bayesian
uncertainty quantification, with a flat prior on $\theta$ and the usual improper flat priors on
$\beta$ and $\log\sigma$, the posterior of $\theta$ works out to
$$\pi(\theta \mid \text{data}) \propto \left(\frac{1}{RSS(\theta)}\right)^{(n-p)/2} |X_\theta^T X_\theta|^{-1/2},$$
where $p$ is the number of columns of $X_\theta$ (the dimension of $\beta$). This single formula is
what appears, with different $p$, in every model below: $p=3$ for one sinusoid or one breakpoint,
$p=5$ for two sinusoids, $p=4$ for two breakpoints. The two sections that follow apply it to a
frequency parameter and then to a time-breakpoint parameter.

## Recap: one sinusoid and the periodogram shortcut

For data $y_0,\dots,y_{n-1}$ (Python indexing, from 0), the single-frequency sinusoidal model is
$$y_t = \beta_0 + \beta_1\cos(2\pi f t) + \beta_2 \sin(2\pi f t) + \epsilon_t, \qquad f \in [0, 0.5].$$
Here $\theta = f$ and $X_f$ has columns $1, \cos(2\pi f t), \sin(2\pi f t)$. Evaluating $RSS(f)$ and
the posterior over $f$ requires discretizing $f$ to a finite set, and there are two ways to do this:
a dense grid on $(0, 0.5)$, or the **Fourier frequencies** $j/n$. Restricting to Fourier frequencies
buys a large computational shortcut: with the DFT of the data,
$$b_j = \sum_{t=0}^{n-1} y_t \exp\!\left(-\frac{2\pi i jt}{n}\right), \qquad j = 0,\dots,n-1$$
(computed in $O(n\log n)$ by the FFT) and the periodogram $I(j/n) := |b_j|^2/n$, the RSS at a
Fourier frequency reduces to
$$RSS(j/n) = \sum_{t=0}^{n-1}(y_t - \bar y)^2 - 2I(j/n).$$
Minimizing $RSS(j/n)$ over $j$ is therefore the same as maximizing the periodogram. The reason the
formula is this clean is that at a Fourier frequency in $(0, 0.5)$,
$$X_f^T X_f = \begin{pmatrix} n & 0 & 0 \\ 0 & n/2 & 0 \\ 0 & 0 & n/2 \end{pmatrix},$$
a fixed, $f$-independent matrix, so $|X_f^T X_f|^{-1/2} = (n^3/8)^{-1/2}$ can be absorbed into the
constant of proportionality in the posterior:
$$\pi(j/n \mid \text{data}) \propto \left(\frac{1}{RSS(j/n)}\right)^{(n-3)/2} I\{0 < j/n < 0.5\}.$$
Restricting to Fourier frequencies is purely a computational convenience — there is no statistical
reason to prefer them, and doing so can lose real information (the lecture flags the sunspots
dataset as an example where this matters, without working it out further here).

## Adding a second frequency

The natural extension fits two sinusoids at once:
$$y_t = \beta_0 + \beta_1\cos(2\pi f_1 t) + \beta_2\sin(2\pi f_1 t) + \beta_3\cos(2\pi f_2 t) + \beta_4\sin(2\pi f_2 t) + \epsilon_t.$$
Now $\theta = (f_1, f_2)$, $p = 5$, and
$$RSS(f_1,f_2) = \min_{\beta_0,\dots,\beta_4} \sum_{t=0}^{n-1}\big(y_t - \beta_0 - \beta_1\cos(2\pi f_1 t) - \beta_2\sin(2\pi f_1 t) - \beta_3\cos(2\pi f_2 t) - \beta_4\sin(2\pi f_2 t)\big)^2,$$
with posterior $\propto (1/RSS(f_1,f_2))^{(n-5)/2}|X_{f_1,f_2}^TX_{f_1,f_2}|^{-1/2}$. In general this
means minimizing over a *joint* grid in $(f_1,f_2)$ — a two-dimensional search. But if $f_1, f_2$
are restricted to distinct Fourier frequencies in $(0, 0.5)$, the same kind of simplification as
before occurs:
$$RSS(f_1,f_2) = \sum_{t=0}^{n-1}(y_t-\bar y)^2 - 2I(f_1) - 2I(f_2). \tag{4}$$
So the two frequencies that minimize $RSS(f_1,f_2)$ are exactly the top two maximizers of the
periodogram — no joint search needed, just reading off the two tallest peaks.

<figure>
<svg viewBox="0 0 320 200" role="img" aria-label="A periodogram with two dominant peaks marking the best-fitting pair of frequencies">
  <line x1="30" y1="170" x2="300" y2="170" stroke="currentColor" stroke-width="1"/>
  <text x="304" y="174" font-size="12" fill="currentColor">f</text>
  <text x="18" y="26" font-size="12" fill="currentColor">I(f)</text>
  <polyline points="30,165 50,160 70,168 90,155 100,40 110,150 130,160 150,165 170,158 190,162 200,20 210,155 230,168 250,160 270,165 300,168" fill="none" stroke="currentColor" stroke-width="1.5"/>
  <line x1="100" y1="40" x2="100" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="3 2"/>
  <line x1="200" y1="20" x2="200" y2="170" stroke="currentColor" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="100" y="185" text-anchor="middle" font-size="12" fill="currentColor">f₁</text>
  <text x="200" y="185" text-anchor="middle" font-size="12" fill="currentColor">f₂</text>
</svg>
<figcaption>Because Fourier-frequency sinusoids are orthogonal, adding a frequency to the fit lowers
RSS by exactly $2I(f)$ for that frequency alone — so the best-fitting pair is simply the two tallest
peaks of the periodogram.</figcaption>
</figure>

### Why the frequencies decouple: orthogonality of sinusoids

Equation (4) is a consequence of the columns of $X_{f_1,f_2}$ being orthogonal at Fourier
frequencies, and it is worth seeing why, since it is the fact that lets the joint search collapse.

Work with complex sinusoids first. For $0 \le j \le n-1$, define the vector
$$u^j = \big(1, e^{2\pi i j/n}, e^{2\pi i \cdot 2j/n}, \dots, e^{2\pi i (n-1)j/n}\big)^T,$$
i.e. $e^{2\pi i f t}$ at $f = j/n$ evaluated at $t = 0,\dots,n-1$. Two facts fall out immediately:
$u^0$ is the all-ones vector, and $u^j = \overline{u^{n-j}}$ for $1 \le j \le n-1$. The key property
is orthogonality: for $0 \le j \ne k \le n-1$ (using the complex inner product
$\langle a,b\rangle = \sum_t a_t \bar b_t$),
$$\langle u^j, u^k\rangle = \sum_{t=0}^{n-1} \exp\!\Big(2\pi i \frac{j-k}{n}t\Big) = \frac{1 - \exp(2\pi i(j-k))}{1-\exp(2\pi i (j-k)/n)} = 0,$$
since the numerator is $1 - 1 = 0$ (as $j - k$ is an integer) while the denominator is nonzero for
$j \ne k \pmod n$. Setting $j = k$ in the same geometric-sum calculation gives
$\langle u^j, u^j\rangle = \|u^j\|^2 = n$.

This carries over to the real sinusoids that actually appear in the design matrix. For a Fourier
frequency $0 < j/n < 1/2$, define
$$c^j = \big(1,\cos(2\pi j/n), \dots, \cos(2\pi(n-1)j/n)\big)^T, \qquad
s^j = \big(0, \sin(2\pi j/n), \dots, \sin(2\pi(n-1)j/n)\big)^T,$$
the evaluations of $\cos(2\pi ft)$ and $\sin(2\pi ft)$ at $f = j/n$. (At the boundary $j=0$,
$c^0$ is all-ones and $s^0$ is zero; at $j = n/2$, when $n$ is even, $c^{n/2}=(1,-1,1,-1,\dots)$ and
$s^{n/2}=0$.) These relate to the complex vectors by
$$c^j = \frac{u^j + u^{n-j}}{2}, \qquad s^j = \frac{u^j - u^{n-j}}{2i}.$$
Fix two distinct Fourier frequencies $j/n, k/n \in (0,1/2)$. Expanding $\langle c^j, c^k\rangle$
into four inner products of $u$'s, every term vanishes: $j \ne k$ kills $\langle u^j,u^k\rangle$
and $\langle u^{n-j},u^{n-k}\rangle$, and $j/n, k/n < 1/2$ means $j+k<n$, so $n-j\ne k$ and
$n-k\ne j$, killing the cross terms too. Hence $\langle c^j,c^k\rangle = 0$, and the same expansion
shows $\langle c^j, s^j\rangle = \frac{1}{4i}(\langle u^j,u^j\rangle - \langle u^{n-j},u^{n-j}\rangle) = \frac{1}{4i}(n-n)=0$,
and likewise for the other cross terms. Also
$$\langle c^j,c^j\rangle = \tfrac14\big(\langle u^j,u^j\rangle + \langle u^j,u^{n-j}\rangle + \langle u^{n-j},u^j\rangle + \langle u^{n-j},u^{n-j}\rangle\big) = \tfrac14(n+0+0+n) = n/2,$$
and similarly $\langle s^j,s^j\rangle = n/2$.

Now $X_{f_1,f_2}$ (with $f_1=j/n$, $f_2=k/n$) has columns $c^0, c^j, s^j, c^k, s^k$, so by the
orthogonality just shown,
$$X_{f_1,f_2}^T X_{f_1,f_2} = \mathrm{diag}(n,\, n/2,\, n/2,\, n/2,\, n/2).$$
From here the argument proceeds exactly as in the single-frequency case (an earlier lecture, not
reproduced here) to yield (4): the RSS reduction from adding a frequency is $2I(f)$ for that
frequency alone, independent of any other frequency present, because the corresponding columns of
the design matrix are orthogonal.

### Three or more frequencies

The same argument extends to any number of distinct Fourier frequencies. For three distinct
frequencies $f_1, f_2, f_3$ in $(0,1/2)$,
$$RSS(f_1,f_2,f_3) = \sum_{t=0}^{n-1}(y_t-\bar y)^2 - 2I(f_1) - 2I(f_2) - 2I(f_3),$$
so the best-fitting triple of Fourier frequencies is just the top three periodogram peaks. If the
frequencies are *not* restricted to the Fourier grid, this shortcut is unavailable and a genuine
joint minimization of $RSS(f_1,\dots,f_k)$ is needed — harder, but potentially a substantially
better fit depending on the data.

## A model with a bend: change of slope

The same profiling-and-posterior recipe applies to models that are nonlinear for a completely
different reason: a trend line with a kink in it. The **change-of-slope** (or **broken-stick**)
model is
$$y_t = \beta_0 + \beta_1 t + \beta_2\,\mathrm{ReLU}(t-c) + \epsilon_t, \qquad \epsilon_t \overset{\text{i.i.d}}{\sim} N(0,\sigma^2),$$
where $\mathrm{ReLU}(t-c) = (t-c)_+ = (t-c)I\{t>c\} = \max(t-c,0)$ is the ramp (positive-part)
function. Before time $c$ the slope is $\beta_1$; after $c$ it becomes $\beta_1+\beta_2$ — hence
"broken stick."

<figure>
<svg viewBox="0 0 340 200" role="img" aria-label="A broken-stick regression line with a single change of slope at time c">
  <line x1="30" y1="180" x2="320" y2="180" stroke="currentColor" stroke-width="1"/>
  <text x="325" y="184" font-size="12" fill="currentColor">t</text>
  <line x1="30" y1="150" x2="170" y2="95" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="95" x2="310" y2="25" stroke="currentColor" stroke-width="2"/>
  <line x1="170" y1="95" x2="170" y2="180" stroke="currentColor" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="170" y="194" text-anchor="middle" font-size="12" fill="currentColor">c</text>
  <text x="70" y="120" font-size="12" fill="currentColor">slope β₁</text>
  <text x="215" y="50" font-size="12" fill="currentColor">slope β₁+β₂</text>
</svg>
<figcaption>The change-of-slope model: slope β₁ up to the unknown breakpoint c, then β₁+β₂
afterward — the ReLU(t−c) term is what puts the kink in the line.</figcaption>
</figure>

If $c$ were known, (1) is ordinary linear regression $y = X_c\beta + \epsilon$ with
$$X_c = \begin{pmatrix} 1 & 1 & \mathrm{ReLU}(1-c) \\ 1 & 2 & \mathrm{ReLU}(2-c) \\ \vdots & \vdots & \vdots \\ 1 & n & \mathrm{ReLU}(n-c)\end{pmatrix}.$$
Here $\theta = c$, $p = 3$, and the same profiled RSS applies:
$$RSS(c) = \min_{\beta_0,\beta_1,\beta_2} \sum_{t=1}^n \big(y_t - \beta_0 - \beta_1 t - \beta_2\,\mathrm{ReLU}(t-c)\big)^2.$$
Since $c$ only takes the values $1,\dots,n$, its MLE is found by brute-force enumeration
(`np.argmin` over $RSS(c)$ for $c=1,\dots,n$), rather than by a continuous grid. Given $\hat c$, the
remaining parameters follow exactly as in linear regression:
$$\hat\beta = (\hat\beta_0,\hat\beta_1,\hat\beta_2)^T = (X_{\hat c}^T X_{\hat c})^{-1}X_{\hat c}^T y,
\qquad \hat\sigma = \sqrt{RSS(\hat c)/(n-3)}.$$

## Bayesian uncertainty for the breakpoint

For uncertainty quantification, use the same flat priors as in linear regression for
$\beta_0,\beta_1,\beta_2,\log\sigma$ (i.i.d. $\mathrm{unif}(-C,C)$ for large $C$), and a uniform
prior on $c$ — but not over all of $\{1,\dots,n\}$. The endpoints are degenerate:

- At $c=1$, $\mathrm{ReLU}(t-1) = t-1$ for every $t=1,\dots,n$, so the nonlinear term is absorbed
  into the linear terms: $\beta_0+\beta_1 t+\beta_2(t-1) = (\beta_0-\beta_2)+(\beta_1+\beta_2)t$.
  The model collapses to a plain linear trend — it is no longer a broken stick.
- At $c=n$, $\mathrm{ReLU}(t-n) = 0$ for every $t=1,\dots,n$ (since $t<n$ always), so the term has
  no effect at all.

So the meaningful range is $c \in \{2,\dots,n-1\}$, and the prior is taken as
$c \sim \mathrm{uniform}\{2,\dots,n-1\}$. Following the general recipe, the posterior of $c$ is
$$\pi(c\mid\text{data}) \propto \left(\frac{1}{RSS(c)}\right)^{(n-3)/2}|X_c^TX_c|^{-1/2}\, I\{c=2,\dots,n-1\},$$
i.e. the discrete pmf
$$\pi(c\mid\text{data}) = \frac{\big(1/RSS(c)\big)^{(n-3)/2}|X_c^TX_c|^{-1/2}}{\sum_{c'=2}^{n-1}\big(1/RSS(c')\big)^{(n-3)/2}|X_{c'}^TX_{c'}|^{-1/2}}, \qquad c=2,\dots,n-1.$$
Conditional on $c$, the model is once again plain linear regression, so the usual linear-regression
posteriors apply (this step is quoted from a homework result, "Problem 4 in Homework 1," not
reproduced in this lecture):
$$\frac{RSS(c)}{\sigma^2}\ \Big|\ \text{data}, c \ \sim\ \chi^2_{n-3}, \qquad
\beta \mid \text{data}, c, \sigma \ \sim\ N_3\big(\hat\beta_c,\ \sigma^2(X_c^TX_c)^{-1}\big),
\qquad \hat\beta_c = (X_c^TX_c)^{-1}X_c^Ty.$$

## Sampling the posterior

To visualize this uncertainty, draw posterior samples and plot the resulting fitted curves against
the data:

1. Draw $c^{(1)},\dots,c^{(N)}$ with replacement from $\{2,\dots,n-1\}$, weighted by the posterior
   pmf $\pi(c\mid\text{data})$ (e.g. the `choice` method of `np.random.default_rng()`).
2. For each $j=1,\dots,N$, with $c=c^{(j)}$ fixed:
   a. Compute $RSS(c)$ and $\hat\beta_c$ by ordinary linear regression with design matrix $X_c$.
   b. Draw $\chi^2 \sim \chi^2_{n-3}$ and set $\sigma^{(j)} = \sqrt{RSS(c)/\chi^2}$.
   c. Draw $\beta^{(j)} \sim N\big(\hat\beta_c, (\sigma^{(j)})^2(X_c^TX_c)^{-1}\big)$.

Each posterior sample $(c^{(j)},\beta^{(j)})$ gives a fitted curve
$t \mapsto \beta_0^{(j)}+\beta_1^{(j)}t+\beta_2^{(j)}\mathrm{ReLU}(t-c^{(j)})$, and plotting these
together with the data — together with vertical lines at each $c^{(j)}$ — shows both the spread in
the fitted shape and the uncertainty in where the breakpoint sits. Approximate 95% credible
intervals for each parameter come from the 2.5th and 97.5th percentiles of its posterior samples.

The same scheme extends to posterior *predictive* samples for a future observation $y_{t^*}$: run
steps 1–2 as above, and add
$$\text{(d)} \quad y_{t^*}^{(j)} \sim N\Big(\beta_0^{(j)}+\beta_1^{(j)}t^*+\beta_2^{(j)}\mathrm{ReLU}(t^*-c^{(j)}),\ (\sigma^{(j)})^2\Big).$$

## More than one breakpoint

Two breakpoints give
$$y_t = \beta_0+\beta_1 t + \beta_2\,\mathrm{ReLU}(t-c_1) + \beta_3\,\mathrm{ReLU}(t-c_2)+\epsilon_t,$$
i.e. $y = X_c\beta+\epsilon$ with $c=(c_1,c_2)$ and $X_c$ having columns $1, t, \mathrm{ReLU}(t-c_1),
\mathrm{ReLU}(t-c_2)$. Now $\theta=(c_1,c_2)$, $p=4$, and $RSS(c) = \min_\beta\|y-X_c\beta\|^2$ is
minimized over the grid of pairs $c_1,c_2 \in \{1,\dots,n\}$ — an $O(n^2)$ search instead of $O(n)$.
The posterior of $c$ is, by the same recipe,
$$\pi(c\mid\text{data}) \propto \left(\frac{1}{RSS(c)}\right)^{(n-4)/2}|X_c^TX_c|^{-1/2}.$$
In general, with $k$ breakpoints,
$$y_t = \beta_0+\beta_1t+\sum_{j=1}^k\beta_{j+1}\,\mathrm{ReLU}(t-c_j)+\epsilon_t,$$
and estimation and inference proceed exactly as before, with $X_c$ extended by one ReLU column per
breakpoint. The obstacle is computational: a grid search over $k$ breakpoints costs $O(n^k)$, which
the lecture notes becomes expensive once $k\ge4$.

## Sources

- **Sinusoidal models: recap, multiple frequencies, orthogonality proof.** UC Berkeley STAT 153,
  Fall 2025, "Lecture Nine" (Aditya Guntuboyina, September 26, 2025): sections 1 ("Recap: previous
  two lectures"), 2 ("Sinusoidal Models with more frequencies," including §2.1–2.4 on orthogonality
  and the multi-frequency RSS decomposition), and 3 ("Other Nonlinear Models," the two-breakpoint
  change-of-slope extension). Converted from a PDF with no text layer; the source itself flags every
  equation as unverified.
- **Change-of-slope model, Bayesian uncertainty, posterior sampling.** UC Berkeley STAT 153, Spring
  2025, "Lecture Nine" (Aditya Guntuboyina, February 18, 2025): sections 1 ("Change of Slope
  Model"), 3 ("Uncertainty Quantification for $c,\beta_0,\beta_1,\beta_2,\sigma$"), 4 ("Posterior
  Sampling for Uncertainty Quantification"), and 5 ("More Changes of Slope"). Same caveat on
  fidelity as above.
- **Referred to but not supplied**: "Lecture 7" of the course (the derivation of the single-frequency
  RSS-to-periodogram identity and the final step of the multi-frequency orthogonality proof), "Homework
  One, Problem 4" (the linear-regression result behind the $\chi^2_{n-3}$ posterior for $\sigma$), and
  "Homework Two" (further worked examples of nonlinear regression models, mentioned but not given).

---

[← 106. Mean, Variance, and Spectrum Models](106-mean-variance-and-spectrum-models.md) · [Contents](index.md) · [108. Introduction to Time Series (part 1) →](108-introduction-to-time-series-part-1.md)
