---
title: p-values, confidence regions, and (mis-)interpreting Tests
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# p-values, confidence regions, and (mis-)interpreting Tests

**Source:** [`reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

<span class="math display">\\$$ \\newcommand{\\cB}{\\mathcal{B}} \\newcommand{\\cF}{\\mathcal{F}} \\newcommand{\\cN}{\\mathcal{N}} \\newcommand{\\cP}{\\mathcal{P}} \\newcommand{\\cX}{\\mathcal{X}} \\newcommand{\\EE}{\\mathbb{E}} \\newcommand{\\PP}{\\mathbb{P}} \\newcommand{\\RR}{\\mathbb{R}} \\newcommand{\\ZZ}{\\mathbb{Z}} \\newcommand{\\td}{\\,\\textrm{d}} \\newcommand{\\simiid}{\\stackrel{\\textrm{i.i.d.}}{\\sim}} \\newcommand{\\simind}{\\stackrel{\\textrm{ind.}}{\\sim}} \\newcommand{\\eqas}{\\stackrel{\\textrm{a.s.}}{=}} \\newcommand{\\eqPas}{\\stackrel{\\cP\\textrm{-a.s.}}{=}} \\newcommand{\\eqmuas}{\\stackrel{\\mu\\textrm{-a.s.}}{=}} \\newcommand{\\eqD}{\\stackrel{D}{=}} \\newcommand{\\indep}{\\perp\\!\\!\\!\\!\\perp} \\DeclareMathOperator\*{\\minz}{minimize\\;} \\DeclareMathOperator\*{\\maxz}{maximize\\;} \\DeclareMathOperator\*{\\argmin}{argmin\\;} \\DeclareMathOperator\*{\\argmax}{argmax\\;} \\newcommand{\\Var}{\\textnormal{Var}} \\newcommand{\\Cov}{\\textnormal{Cov}} \\newcommand{\\Corr}{\\textnormal{Corr}} \\newcommand{\\ep}{\\varepsilon} \\$$</span>

As we have previously defined hypothesis tests, they are characterized by dichotomous accept/reject decisions after choosing a null hypothesis, a test statistic, and a critical threshold. Sometimes we really do need to make a dichotomous decision (for example, the FDA really has to decide whether to approve a drug or not), but this is rare in practice. If our test statistic is large enough to reject <span class="math inline">\$H\_0:\\;\\theta=0\$</span> at the <span class="math inline">\$\\alpha = 0.05\$</span> level, we would usually still be interested in questions like:

- Would we have rejected <span class="math inline">\$H\_0\$</span> at a stricter <span class="math inline">\$\\alpha\$</span> level, like <span class="math inline">\$\\alpha = 0.01\$</span> or <span class="math inline">\$\\alpha = 0.005\$</span>?

- Have we established that <span class="math inline">\$\\theta\$</span> is far from zero, or only that it isn’t exactly zero?

These questions can be answered by <span class="math inline">\$p\$</span>-values and confidence regions, which enrich our dichotomous decision by respectively telling us about the outcome for other <span class="math inline">\$\\alpha\$</span> values we could have used, and for other null hypotheses we could have tested.

---

[Up: contents](index.md) · [p-Values →](02-p-values.md)
