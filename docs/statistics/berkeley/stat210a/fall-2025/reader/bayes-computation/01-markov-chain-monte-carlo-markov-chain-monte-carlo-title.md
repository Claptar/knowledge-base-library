---
title: Markov Chain Monte Carlo {#markov-chain-monte-carlo .title}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/bayes-computation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Markov Chain Monte Carlo {#markov-chain-monte-carlo .title}

**Source:** [`reader/bayes-computation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/bayes-computation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

<span class="math display">\\$$ \\newcommand{\\cB}{\\mathcal{B}} \\newcommand{\\cF}{\\mathcal{F}} \\newcommand{\\cN}{\\mathcal{N}} \\newcommand{\\cP}{\\mathcal{P}} \\newcommand{\\cX}{\\mathcal{X}} \\newcommand{\\EE}{\\mathbb{E}} \\newcommand{\\PP}{\\mathbb{P}} \\newcommand{\\RR}{\\mathbb{R}} \\newcommand{\\ZZ}{\\mathbb{Z}} \\newcommand{\\td}{\\,\\textrm{d}} \\newcommand{\\simiid}{\\stackrel{\\textrm{i.i.d.}}{\\sim}} \\newcommand{\\simind}{\\stackrel{\\textrm{ind.}}{\\sim}} \\newcommand{\\eqas}{\\stackrel{\\textrm{a.s.}}{=}} \\newcommand{\\eqPas}{\\stackrel{\\cP\\textrm{-a.s.}}{=}} \\newcommand{\\eqmuas}{\\stackrel{\\mu\\textrm{-a.s.}}{=}} \\newcommand{\\eqD}{\\stackrel{D}{=}} \\newcommand{\\indep}{\\perp\\!\\!\\!\\!\\perp} \\DeclareMathOperator\*{\\minz}{minimize\\;} \\DeclareMathOperator\*{\\maxz}{maximize\\;} \\DeclareMathOperator\*{\\argmin}{argmin\\;} \\DeclareMathOperator\*{\\argmax}{argmax\\;} \\newcommand{\\Var}{\\textnormal{Var}} \\newcommand{\\Cov}{\\textnormal{Cov}} \\newcommand{\\Corr}{\\textnormal{Corr}} \\newcommand{\\ep}{\\varepsilon} \\$$</span>

---

[Up: contents](index.md) · [1 Why Bayesian computation is difficult {number="1"} →](02-1-why-bayesian-computation-is-difficult-number-1.md)
