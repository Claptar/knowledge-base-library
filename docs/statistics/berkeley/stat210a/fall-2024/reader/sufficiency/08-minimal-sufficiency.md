---
title: Minimal sufficiency
source: https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/sufficiency.qmd
source_file: sources/berkeley-stat210a/fall-2024/reader/sufficiency.qmd
licence: CC BY 4.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# Minimal sufficiency

**Source:** [`reader/sufficiency.qmd`](https://github.com/berkeley-stat210a/fall-2024/blob/812543bde50398a54db3044bf8ba7120189a4dfa/reader/sufficiency.qmd) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.qmd` (lossless)

Consider again the example with $X_1,\ldots,X_n \simiid N(\theta,1)$. We have shown that $\sum_i X_i$ is sufficient. It follows that $\overline{X} = \frac{1}{n}\sum_i X_i$ is also sufficient. But we have also shown that the vector of order statistics $S(X) = (X_{(1)}, \ldots, X_{(n)})$ is another sufficient statistic. Finally, the full data set $X$ is always a sufficient statistic, by definition.

While these are indeed all sufficient statistics, some of them represent more significant compressions of the data than others. We can see this from the fact that $\sum_i X_i$ and $\overline{X}$ are recoverable from each other, and can also be recovered from either $S(X)$ or $X$ itself, but $S(X)$ cannot be recovered from $\sum_i X_i$ or $\overline{X}$. The full data $X$ cannot be recovered from any of the other three, but any of the other three can be recovered from it. Among these statistics, the first two represent the greatest reduction of the data, and $X$ represents no reduction at all, while $S(X)$ sits in the middle.

Any statistic from which a sufficient statistic can be recovered is immediately a sufficient statistic:

**Proposition:** If $T(X)$ is sufficient and $T(X) = f(S(X))$ then $S(X)$ is also sufficient.

*Proof:* By the factorization theorem we can find densities with $$
p_\theta(x) = g_\theta(T(x))h(x) = (g_\theta \circ f)(S(x)) h(x),
$$ showing that $S(X)$ is sufficient as well.

We say that a sufficient statistic is **minimal** if it can be recovered from any other sufficient statistic. That is, $T(X)$ is **minimal sufficient** if

1.  $T(X)$ is sufficient, and

2.  For any other sufficient statistic $S(X)$, we have $T(X) = f(S(X))$ for some $f$ (almost surely in $\cP$).

We would like to be able to recognize minimal sufficient statistics when we can. For a model $\cP$ with densities $p_\theta$, we can say that two data sets $x,y\in \cX$ are *equivalent* (with respect to statistical inference in $\cP$) if $p_\theta(x)/p_\theta(y)$ does not depend on $\theta$. We can write $x \equiv_{\cP} y$ if this is the case.

Note that, for any sufficient statistic $T(X)$, values that map to the same output value $t$ must be equivalent: if $T(x)=T(y)=t$, we have $$
\frac{p_\theta(x)}{p_\theta(y)} = \frac{\PP_\theta(X = x \text{ and } T(X) = t)}{\PP_\theta(X = y \text{ and } T(X) = t)} = \frac{\PP(X = x \mid T(X) = t)}{\PP(X = y \mid T(X) = t)},
$$ which does not depend on $\theta$ by sufficiency of $T(X)$.\footnote{this is really true up to almost sure equality.} Thus, for *any* sufficient statistic we have $T(x) = T(y) \Rightarrow x \equiv_{\cP} y$: the function $T$ is only allowed to collapse values that are equivalent to each other. For a *minimal sufficient statistic*, this implication goes both ways since $T$ collapses the sample space as much as possible. That is,

**Proposition:** Assume $\cP$ has densities $p_\theta(x)$, and $T(X)$ is any statistic. If we have $$x \equiv_{\cP} y \iff T(x) = T(y),$$ then $T(X)$ is minimal sufficient.

*Proof (discrete* $\cX$): First, we show $T(X)$ is sufficient. For any $x$ with $T(x) = t$, we have

$$
\PP_\theta(X = x \mid T(X) = t) = \frac{p_\theta(x)}{\sum_{z: T(z) = t} p_\theta(z)} = \frac{1}{\sum_{z:\; T(z) = t} p_\theta(z)/p_\theta(x)},
$$ which does not depend on $\theta$ because all of the values $z$ that we sum over in the denominator map to the same $t$, and are therefore equivalent to $x$ by assumption.

Next, assume $S(X)$ is any other sufficient statistic. If $S(x) = S(y) = s$, then $x \equiv_{\cP} y$, by the argument above the theorem, and consequently $T(x) = T(y)$ by assumption. Then we can set $f(s) = T(x)$. For any other value $z$ with $S(z) = s$, we must also have $x \equiv_{\cP} z$ so $T(z) = T(x) = f(S(z))$. Since $s$ was arbitrary, we have the result.

---

[← Sufficient statistics under i.i.d. sampling](07-sufficient-statistics-under-i-i-d-sampling.md) · [Up: contents](index.md)
