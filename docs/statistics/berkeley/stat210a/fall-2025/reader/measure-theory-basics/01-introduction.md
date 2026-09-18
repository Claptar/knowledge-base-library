---
title: Introduction
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/measure-theory-basics.html
source_file: sources/berkeley-stat210a/fall-2025/reader/measure-theory-basics.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-18'
---

> **Converted source.** [`reader/measure-theory-basics.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/reader/measure-theory-basics.html) — berkeley-stat210a · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.html`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Introduction

## Measure Theory Basics {#measure-theory-basics .title}

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

### Measure theory: a rigorous grounding for probability {.anchored anchor-id="measure-theory-a-rigorous-grounding-for-probability"}

**Measure theory** is an area of mathematics concerned with measuring the “size” of subsets of a certain set. Soon after it was developed in the the early twentieth century, the great Soviet mathematician Kolmogorov realized it could be applied to give a rigorous grounding to probability theory, it was a major advance in understanding and resolving certain [paradoxes](https://en.wikipedia.org/wiki/Bertrand_paradox_(probability)) in probability theory. David Aldous gives a nice [discussion](https://www.stat.berkeley.edu/~aldous/Real_World/kolmogorov.html) of this history.

This is **not** a course on measure-theoretic probability and we will not rigorously develop the subject. However, it will be useful to draw on some of the **basics** of measure theory, to simplify our notation throughout the course and to clarify certain concepts around integration and conditioning. [Homework 0](https://www.stat.berkeley.edu/~wfithian/courses/stat210a/hw0.pdf) illustrates some of the interesting aspects of measure theory and why it is useful.

---

[Up: contents](index.md) · [Measures →](02-measures.md)
