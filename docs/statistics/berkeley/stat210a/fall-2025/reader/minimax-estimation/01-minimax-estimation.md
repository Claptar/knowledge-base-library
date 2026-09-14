---
title: Minimax Estimation
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/minimax-estimation.html
source_file: sources/berkeley-stat210a/fall-2025/reader/minimax-estimation.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Minimax Estimation

**Source:** [`reader/minimax-estimation.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/minimax-estimation.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

Published

October 5, 2023

<span class="math display">\\$$ \\newcommand{\\cB}{\\mathcal{B}} \\newcommand{\\cF}{\\mathcal{F}} \\newcommand{\\cN}{\\mathcal{N}} \\newcommand{\\cP}{\\mathcal{P}} \\newcommand{\\cX}{\\mathcal{X}} \\newcommand{\\EE}{\\mathbb{E}} \\newcommand{\\PP}{\\mathbb{P}} \\newcommand{\\RR}{\\mathbb{R}} \\newcommand{\\ZZ}{\\mathbb{Z}} \\newcommand{\\td}{\\,\\textrm{d}} \\newcommand{\\simiid}{\\stackrel{\\textrm{i.i.d.}}{\\sim}} \\newcommand{\\simind}{\\stackrel{\\textrm{ind.}}{\\sim}} \\newcommand{\\eqas}{\\stackrel{\\textrm{a.s.}}{=}} \\newcommand{\\eqPas}{\\stackrel{\\cP\\textrm{-a.s.}}{=}} \\newcommand{\\eqmuas}{\\stackrel{\\mu\\textrm{-a.s.}}{=}} \\newcommand{\\eqD}{\\stackrel{D}{=}} \\newcommand{\\indep}{\\perp\\!\\!\\!\\!\\perp} \\DeclareMathOperator\*{\\minz}{minimize\\;} \\DeclareMathOperator\*{\\maxz}{maximize\\;} \\DeclareMathOperator\*{\\argmin}{argmin\\;} \\DeclareMathOperator\*{\\argmax}{argmax\\;} \\newcommand{\\Var}{\\textnormal{Var}} \\newcommand{\\Cov}{\\textnormal{Cov}} \\newcommand{\\Corr}{\\textnormal{Corr}} \\newcommand{\\ep}{\\varepsilon} \\$$</span>

<span class="math inline">\$\\DeclareMathOperator\*{\\minimize}{\\textnormal{minimize}}\$</span>

---

[Up: contents](index.md) · [1 Minimax risk and estimator →](02-1-minimax-risk-and-estimator.md)
