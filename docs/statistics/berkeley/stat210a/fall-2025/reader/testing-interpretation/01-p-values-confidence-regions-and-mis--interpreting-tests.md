---
title: p-values, confidence regions, and (mis-)interpreting Tests
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/testing-interpretation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/testing-interpretation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/testing-interpretation.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# p-values, confidence regions, and (mis-)interpreting Tests

1.  [Course Reader](../introduction/index.md)
2.  [p-values, confidence regions, and (mis-)interpreting Tests](index.md)

## p-values, confidence regions, and (mis-)interpreting Tests {#p-values-confidence-regions-and-mis-interpreting-tests .title}

$$
\newcommand{\cB}{\mathcal{B}}
\newcommand{\cF}{\mathcal{F}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cP}{\mathcal{P}}
\newcommand{\cX}{\mathcal{X}}
\newcommand{\EE}{\mathbb{E}}
\newcommand{\PP}{\mathbb{P}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\td}{\,\textrm{d}}
\newcommand{\simiid}{\stackrel{\textrm{i.i.d.}}{\sim}}
\newcommand{\simind}{\stackrel{\textrm{ind.}}{\sim}}
\newcommand{\eqas}{\stackrel{\textrm{a.s.}}{=}}
\newcommand{\eqPas}{\stackrel{\cP\textrm{-a.s.}}{=}}
\newcommand{\eqmuas}{\stackrel{\mu\textrm{-a.s.}}{=}}
\newcommand{\eqD}{\stackrel{D}{=}}
\newcommand{\indep}{\perp\!\!\!\!\perp}
\DeclareMathOperator*{\minz}{minimize\;}
\DeclareMathOperator*{\maxz}{maximize\;}
\DeclareMathOperator*{\argmin}{argmin\;}
\DeclareMathOperator*{\argmax}{argmax\;}
\newcommand{\Var}{\textnormal{Var}}
\newcommand{\Cov}{\textnormal{Cov}}
\newcommand{\Corr}{\textnormal{Corr}}
\newcommand{\ep}{\varepsilon}
$$

As we have previously defined hypothesis tests, they are characterized by dichotomous accept/reject decisions after choosing a null hypothesis, a test statistic, and a critical threshold. Sometimes we really do need to make a dichotomous decision (for example, the FDA really has to decide whether to approve a drug or not), but this is rare in practice. If our test statistic is large enough to reject $H_0:\;\theta=0$ at the $\alpha = 0.05$ level, we would usually still be interested in questions like:

- Would we have rejected $H_0$ at a stricter $\alpha$ level, like $\alpha = 0.01$ or $\alpha = 0.005$?

- Have we established that $\theta$ is far from zero, or only that it isn’t exactly zero?

These questions can be answered by $p$-values and confidence regions, which enrich our dichotomous decision by respectively telling us about the outcome for other $\alpha$ values we could have used, and for other null hypotheses we could have tested.

---

[Up: contents](index.md) · [p-Values →](02-p-values.md)
