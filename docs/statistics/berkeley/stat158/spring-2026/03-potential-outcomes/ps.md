---
title: Ps
source: https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/03-potential-outcomes/ps.html
source_file: sources/berkeley-stat158/spring-2026/03-potential-outcomes/ps.html
licence: unresolved
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Ps

**Source:** [`03-potential-outcomes/ps.html`](https://github.com/berkeley-stat158/spring-2026/blob/3863c023585286c55df692b83ee6cd5c56dbe822/03-potential-outcomes/ps.html) · **Licence:** unresolved · Converted 2026-09-14 from `.html` (good)

1.  **Estimation under Imbalance**. Consider the setting where we seek to estimate the Average Treatment Effect (ATE) using as our estimator the observed difference in the mean responses in the two groups, <span class="math inline">\$\\overline{Y}\_1 - \\overline{Y}\_0\$</span>. Let <span class="math inline">\$D\_i\$</span> track whether unit <span class="math inline">\$i\$</span> receives the treatment (1) or the control (0) and let the set of indices in the treatment and control groups be be <span class="math inline">\$g1\$</span> and <span class="math inline">\$g0\$</span> respectively. Also let <span class="math inline">\$n\_1\$</span> and <span class="math inline">\$n\_0\$</span> be the number of units in each group.

    So far, we’ve analyzed the case where <span class="math inline">\$n\_1 = n\_2\$</span>, a case where the groups are *balanced*. What happens to the estimator when the groups are *unbalanced*?

    Determine whether or not the estimator is biased when <span class="math inline">\$n\_1\$</span> is twice the size of <span class="math inline">\$n\_0\$</span>. Units are assigned to groups by randomly shuffling the list of their unique identifiers and assigning the first <span class="math inline">\$n\_1\$</span> to the treatment and the remaining to the control. If the estimator is biased, suggest an alternative bias-corrected estimator.

---

[Up: contents](../index.md)
