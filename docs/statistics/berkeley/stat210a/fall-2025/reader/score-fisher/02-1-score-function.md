---
title: 1 Score Function
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html
source_file: sources/berkeley-stat210a/fall-2025/reader/score-fisher.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# 1 Score Function

**Source:** [`reader/score-fisher.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/score-fisher.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

In this section we introduce the score function and Fisher information, two concepts that are central in asymptotic statistics. We

Assume a family <span class="math inline">\$\\cP\$</span> has densities <span class="math inline">\$p\_\\theta\$</span> with respect to a measure <span class="math inline">\$\\mu\$</span>, for <span class="math inline">\$\\theta \\in \\Theta \\subseteq \\RR^d\$</span>. Assume additionally that these densities have common support: that <span class="math inline">\$\\{x: p\_\\theta(x) &gt; 0\\}\$</span> is the same for all <span class="math inline">\$\\theta\$</span> (since we can truncate the sample space to this common support, we could just as well assume <span class="math inline">\$p\_\\theta(x) &gt; 0\$</span> for all <span class="math inline">\$x\$</span> and <span class="math inline">\$\\theta\$</span>).

**Definition:** The *Score function* is defined as <span class="math inline">\$S\_{\\theta}(X) = \\nabla \\ell(\\theta;X)\$</span>, a random vector of dimension <span class="math inline">\$d\$</span>.

We can think of the score function <span class="math inline">\$S\_{\\theta\_0}(X)\$</span> at a given value <span class="math inline">\$\\theta\_0\$</span> as a kind of “local” sufficient statistic that we could use to distinguish between <span class="math inline">\$\\theta\$</span> values in a small neighorhood of <span class="math inline">\$\\theta\_0\$</span>.

To see why, recall that the log-likelihood <span class="math inline">\$\\ell(\\theta;X) = \\log p\_\\theta(X)\$</span>, thought of as a random function with argument <span class="math inline">\$\\theta\$</span>, is a minimal sufficient statistic for <span class="math inline">\$X\$</span>, up to a vertical shift.

Wait! Didn’t we say a statistic can’t be a function of <span class="math inline">\$\\theta\$</span>?

Yes, but what we meant by this is, more precisely, is that a statistic can be calculated from the data, by an analyst who doesn’t know what is the *true* value of <span class="math inline">\$\\theta\$</span> that governed the sampling distribution of the data <span class="math inline">\$X\$</span>.

The trouble is that there is a bit of notational ambiguity when we write <span class="math inline">\$\\ell(\\theta;X)\$</span>. If we want to be a bit more precise, what we mean here is <span class="math inline">\$\\ell(\\cdot; X)\$</span>, which is realized in the space of functions from <span class="math inline">\$\\theta\$</span> to <span class="math inline">\$\\mathbb{R}\$</span>. If the analyst observes <span class="math inline">\$X\$</span> they can plot a graph of this whole likelihood function; that graph is the statistic.

On the other hand, suppose that instead we interpret <span class="math inline">\$\\ell(\\theta;X)\$</span> as the function *evaluated at* the true value <span class="math inline">\$\\theta\$</span>, i.e. in more pedantic notation <span class="math inline">\$\\left.\\ell(\\cdot; X)\\right\|\_{\\text{true } \\theta}\$</span>. Then, this would *not* be a statistic because the analyst can’t calculate it without knowing which is the true value.

A third possibility is that we could be evaluating \$()

For any fixed reference point <span class="math inline">\$\\theta\_0 \\in \\Theta\$</span>, we can subtract <span class="math inline">\$\\ell(\\theta\_0; X)\$</span> to obtain the minimal sufficient statistic <span class="math inline">\$\\ell(\\theta; X) - \\ell(\\theta\_0; X)\$</span>. Then, for a nearby value <span class="math inline">\$\\theta = \\theta\_0 + \\eta\$</span>, with <span class="math inline">\$\\eta\$</span> small, we have <span class="math display">\\$$ \\ell(\\theta\_0 + \\eta; X) - \\ell(\\theta\_0; X) \\approx \\eta'S\_{\\theta\_0}(X), \\$$</span> so the statistic <span class="math inline">\$S\_{\\theta\_0}(X)\$</span> would approximately capture all of the information in a “local” model <span class="math inline">\$\\{P\_{\\theta\_0+\\eta}: \\eta \\text{ small}\\} \\subseteq \\cP\$</span>.

Is the score a statistic?

It depends. Sometimes the reference point <span class="math inline">\$\\theta\_0\$</span> is generic, or it might be specified by the analyst without knowing whether it is the true value of <span class="math inline">\$\\theta\$</span>; for example, we could be testing the null hypothesis <span class="math inline">\$H\_0:\\;\\theta = \\theta\_0\$</span>, without knowing whether the null is true. In that case, it is a statistic (and we’ll often call it a “score statistic”).

On the other hand, for many theoretical calculations, including most of the calculations in this section, we will be specifically interested in <span class="math inline">\$S\_\\theta(X)\$</span> for the *true* value of <span class="math inline">\$\\theta\$</span> that is govering the sampling distribution <span class="math inline">\$P\_\\theta\$</span> of the data. In that case, the score is *not* a statistic.

When we study asymptotic statistics, local models like these will be natural objects of study, because a large data set will commonly allow us to rule out most <span class="math inline">\$\\theta\$</span> values and only focus on values in a small neighborhood of the true parameter.

Or, writing it a different way, we have <span class="math display">\\$$ p\_{\\theta\_0+\\eta}(x) = e^{\\ell(\\theta\_0 + \\eta; x)} \\approx e^{\\eta'\\nabla \\ell(\\theta\_0;x)}p\_{\\theta\_0}(x). \\$$</span>

This evokes some analogies between the score in a generic parametric family and the sufficient statistic in an exponential family. We’ll begin by looking at differential identities.

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [2 Differential Identities and the Fisher Information →](03-2-differential-identities-and-the-fisher-information.md)
