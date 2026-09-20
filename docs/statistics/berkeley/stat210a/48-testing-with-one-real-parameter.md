---
title: "48. Testing with one real parameter"
course: "Berkeley Stat 210A Fall 2024"
chapter: 48
source: "https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html"
licence: "CC BY 4.0"
written: "2026-09-20"
---

> **Lecture notes.** Written from the slides and recording of this lecture of [Berkeley Stat 210A Fall 2024](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/recitation.html), licensed CC BY 4.0. These are notes, not a transcript: the material has been reorganised and rewritten. This adaptation carries the same licence, and the original is linked above.

# 48. Testing with one real parameter

## What this covers

The lecture's own outline for this session has three parts — one-sided tests, two-sided tests,
and UMP unbiased tests — but the surviving material only reaches the first, and even that breaks
off mid-example. This chapter is therefore short on purpose: it covers the single question the
notes actually answer, which is what to do when testing a one-sided hypothesis about a real
parameter and no uniformly most powerful (UMP) test exists. It assumes the Neyman–Pearson
framework from earlier in the course — power functions, test size, and what "UMP" means for a
simple-versus-simple test — and builds the **score test** as the natural substitute.

## Why a one-sided hypothesis can defeat UMP

Take a family $\mathcal{P}=\{P_\theta:\theta\in\Theta\subseteq\mathbb{R}\}$ indexed by a single
real parameter, fix $\theta_0\in\Theta$, and consider the **one-sided hypothesis**
$$
H_0:\theta\le\theta_0 \qquad\text{vs.}\qquad H_1:\theta>\theta_0 .
$$
Both sides are composite: $H_0$ covers a whole ray of parameter values, and so does $H_1$.

For a single alternative $\theta_1>\theta_0$, Neyman–Pearson gives the most powerful test of
$\theta_0$ against $\theta_1$: reject when the likelihood ratio $p_{\theta_1}(X)/p_{\theta_0}(X)$
is large. The trouble is that this rejection region can change shape as $\theta_1$ moves — the
notes record this plainly as "LRT may vary for different $\theta_1$ values." If the region that is
best against one alternative is not the region that is best against another, no single test can be
most powerful against every point of $H_1$ at once, and in general **no UMP test exists** for the
one-sided problem.

## Local alternatives and the score test

The fix the notes take is to stop trying to be optimal against a fixed, distant alternative and
instead ask what happens against an alternative that sits just barely inside $H_1$: for $n$ large,
prioritize $\theta_1=\theta_0+\varepsilon$ and let $\varepsilon\downarrow0$.

Write $\ell(\theta;x)=\log p_\theta(x)$ for the log-likelihood and
$\dot\ell(\theta;x)=\partial_\theta\,\ell(\theta;x)$ for its derivative in $\theta$ — the **score**.
The log likelihood ratio between the local alternative and the null point is, by a first-order
Taylor expansion in $\varepsilon$ around $\varepsilon=0$,
$$
\log LR(X)=\log\frac{p_{\theta_0+\varepsilon}(X)}{p_{\theta_0}(X)}=\ell(\theta_0+\varepsilon;X)-\ell(\theta_0;X)\approx \varepsilon\,\dot\ell(\theta_0;X).
$$
Since $\varepsilon>0$ is fixed and small, ranking outcomes $X$ by $\log LR(X)$ agrees, to first
order, with ranking them by $\dot\ell(\theta_0;X)$ alone — the $\varepsilon$ is just a positive
scale factor. So the Neyman–Pearson rejection region for the local alternative, "reject for large
$\log LR$", collapses in the limit $\varepsilon\downarrow0$ to "reject for large score at
$\theta_0$." That is the argument for using the **score at $\theta_0$** as the test statistic
regardless of which nearby $\theta_1$ one had in mind — this is the construction usually called the
score test:
$$
\phi(X)=\mathbf{1}\{\dot\ell(\theta_0;X)\ge c_\alpha\}.
$$

<figure>
<svg viewBox="0 0 360 170" role="img" aria-label="A theta axis split at theta0 into H0 and H1, with a local alternative theta0 plus epsilon shrinking toward theta0">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="currentColor"/>
    </marker>
  </defs>
  <rect x="40" y="90" width="140" height="20" fill="currentColor" fill-opacity="0.15"/>
  <line x1="40" y1="100" x2="320" y2="100" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="180" y1="90" x2="180" y2="110" stroke="currentColor" stroke-width="1.5"/>
  <text x="180" y="128" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8320;</text>
  <text x="108" y="78" text-anchor="middle" font-size="12" fill="currentColor">H&#8320;: &#952; &#8804; &#952;&#8320;</text>
  <text x="255" y="78" text-anchor="middle" font-size="12" fill="currentColor">H&#8321;: &#952; &#62; &#952;&#8320;</text>
  <circle cx="230" cy="100" r="3" fill="currentColor"/>
  <text x="230" y="145" text-anchor="middle" font-size="12" fill="currentColor">&#952;&#8320;+&#949;</text>
  <line x1="222" y1="132" x2="188" y2="132" stroke="currentColor" stroke-width="1.5" marker-end="url(#arrow)"/>
  <text x="205" y="160" text-anchor="middle" font-size="12" fill="currentColor">&#949; &#8595; 0</text>
</svg>
<figcaption>The local-alternative argument: instead of fixing one point of $H_1$, push the
alternative $\theta_0+\varepsilon$ toward the boundary $\theta_0$ and see what the optimal
rejection region converges to.</figcaption>
</figure>

## Checking the size against a composite null

Because $H_0:\theta\le\theta_0$ is composite, it is not enough to tune $c_\alpha$ so that
$P_{\theta_0}(\phi(X)=1)=\alpha$ at the boundary point alone. Validity as a level-$\alpha$ test
requires the power function
$$
\beta_\phi(\theta)=P_\theta(\phi(X)=1)
$$
to satisfy $\beta_\phi(\theta)\le\alpha$ for **every** $\theta\le\theta_0$, not just at $\theta_0$
itself. The notes flag this explicitly as a step that has to be checked in any application of the
score test — they state the requirement but do not carry out the check.

## The Laplace example, as far as the source goes

The notes open a worked example and then stop: let $X_1,\dots,X_n\overset{iid}{\sim}\frac12
e^{-|x-\theta|}$, the Laplace (double-exponential) distribution with location parameter $\theta$,
and consider testing $H_0:\theta\le\theta_0$ against $H_1:\theta>\theta_0$ — presumably to work out
the score $\dot\ell(\theta_0;X)$ for this family and see what the resulting test looks like. The
source breaks off mid-sentence at this point, so no score function, test statistic, or size
calculation for the Laplace case survives in the material available here.

## Sources

- All of the above is from the handwritten lecture note
  `statistics/berkeley/stat210a/fall-2024/handwritten/lecture15-testonepar.md` (converted from
  `handwritten/lecture15-testonepar.pdf`, licensed CC BY 4.0). The note itself was reconstructed by
  a model from a PDF with no text layer, and its own banner marks the prose as paraphrase and every
  equation as unverified — treat the equations here with the same caution.
- The note's own outline lists three parts: one-sided tests in general, two-sided tests, and UMP
  unbiased tests. Only the first is present in the material supplied for this chapter; two-sided
  tests and UMP unbiased tests are named in the outline but their content is not in the source and
  is not covered here.
- The worked example (testing a location parameter for the Laplace distribution) is stated in the
  source but not completed — the note cuts off after posing the hypotheses, before deriving the
  score or the test.
- Background taken as already known — the Neyman–Pearson lemma, power functions, size, and what a
  UMP test is for a simple hypothesis — was not supplied with this chapter and is assumed from
  earlier in the course.

---

[← 47. One-Sided Tests in General](47-one-sided-tests-in-general.md) · [Contents](index.md) · [49. $p$-Values and Confidence Sets →](49-p-values-and-confidence-sets.md)
