---
title: The problem of induction {.anchored anchor-id="the-problem-of-induction"}
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/introduction.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/introduction.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# The problem of induction {.anchored anchor-id="the-problem-of-induction"}

**Source:** [`units/reader/introduction.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/introduction.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

#### Hume’s problem of induction {.anchored anchor-id="humes-problem-of-induction"}

Unfortunately, inductive reasoning is not *valid* in the sense meant by logicians or mathematicians. It doesn’t matter how many times I’ve seen real symmetric matrices that had real eigenvalues. Without a proof, I can’t make the general claim. There are entertaining examples of patterns being unexpectedly violated in math, such as the [Borwein Integral](https://en.wikipedia.org/wiki/Borwein_integral):

<span class="math display">\\$$ \\begin{aligned} \\int\_0^\\infty \\frac{\\sin x}{x}\\,dx &= \\frac{\\pi}{2}\\\\\[10pt$$ \\int\_0^\\infty \\frac{\\sin x}{x}\\, \\frac{\\sin(x/3)}{x/3}\\,dx &= \\frac{\\pi}{2}\\\\$$10pt$$ \\int\_0^\\infty \\frac{\\sin x}{x}\\, \\frac{\\sin(x/3)}{x/3}\\, \\frac{\\sin(x/5)}{x/5}\\,dx &= \\frac{\\pi}{2}\\\\$$10pt$$ &\\vdots\\\\$$10pt$$ \\int\_0^\\infty \\frac{\\sin x}{x}\\, \\frac{\\sin(x/3)}{x/3}\\,\\cdots\\, \\frac{\\sin(x/13)}{x/13}\\,dx &= \\frac{\\pi}{2}\\\\$$10pt$$ \\int\_0^\\infty \\frac{\\sin x}{x}\\, \\frac{\\sin(x/3)}{x/3}\\,\\cdots\\, \\frac{\\sin(x/15)}{x/15}\\,dx &= \\frac{\\pi}{2} - 2.31 \\times 10^{-11}. \\end{aligned} \\\]</span>

Bertrand Russell also warned about how inductive inference can go awry in real life:

> Domestic animals expect food when they see the person who usually feeds them. We know that all these rather crude expectations of uniformity are liable to be misleading. The man who has fed the chicken every day throughout its life at last wrings its neck instead, showing that more refined views as to the uniformity of nature would have been useful to the chicken.

David Hume’s work *A Treatise of Human Nature* (1739) first proposed the **problem of induction**, namely that inductive reasoning presumes — seemingly without justification — that yet-to-be-observed cases will be similar to observed cases. This presumption is sometimes called the **uniformity principle**, and it is difficult to see how we can justify it. We can’t justify it through a direct logical argument, because it’s not logically justified. We could justify it by past experience — for example, at a low enough level, physical properties of the world generally seem to be uniform across space and time — but that argument is circular! Just because the future has been like the past in the past, doesn’t mean that it will be like the past in the future.

Hume allowed that people have to reason inductively all the time, but he called it a “custom” or “habit” and challenged philosophers to justify it. Now almost 300 years later, there does not seem to have been a fully satisfactory answer; most philosophers of science (like Karl Popper, for example) admit that inductive reasoning is fallible, but think there are reasonable ways for scientists to deal with this.

#### Statistical evasions of the problem of induction {.anchored anchor-id="statistical-evasions-of-the-problem-of-induction"}

We seem to be in trouble if we are trying to build a mathematical science of inductive reasoning, when the first thing we know about induction is that it is not mathematically valid. Statisticians have two main ways of evading this problem, which lead to the two main mathematical frameworks for statistical inference:

**Evasion 1: Bayesian reasoning**. Bayesians respond to Hume that, whatever our *a priori* beliefs are about the world, we at least know how to update them in the light of experience using the mathematics of conditional probability. Our prior beliefs may not ultimately be justified, but there is only one rational way to update them (note this is somewhat disputed). We may hope that after enough experience they will “wash out” and observers with different prior beliefs will eventually converge in their beliefs after seeing enough data. We will study Bayesian statistics in a few weeks.

**Evasion 2: Inductive behavior (frequentist statistics)**. Another way of evading the problem is to design methods for inference whose fallibility can be quantified. As long as certain assumptions hold concerning the conditions under which the data were collected, we may be able to come up with methods that we can mathematically prove give correct conclusions with high probability.

---

[← Deductive vs inductive reasoning {.anchored anchor-id="deductive-vs-inductive-reasoning"}](03-deductive-vs-inductive-reasoning-anchored-anchor-id-deductiv.md) · [Up: contents](index.md) · [Introduction Part 05 — →](05-introduction-part-05.md)
