---
title: Deductive vs inductive reasoning
source: https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/introduction.html
source_file: sources/berkeley-stat210a/fall-2025/units/reader/introduction.html
licence: CC BY 4.0
route: pandoc-html
fidelity: good
converted: '2026-09-14'
---

# Deductive vs inductive reasoning

**Source:** [`units/reader/introduction.html`](https://github.com/berkeley-stat210a/fall-2025/blob/5eb849a4924c34eb73e098cdfc812ffa8d806501/units/reader/introduction.html) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.html` (good)

#### Deductive reasoning {.anchored anchor-id="deductive-reasoning"}

Most mathematics courses are entirely concerned with **deductive reasoning**: drawing conclusions that follow logically from premises. For example:

1.  All real, symmetric matrices have real eigenvalues.

2.  <span class="math inline">\$A\$</span> is a real, symmetric matrix.

3.  *Therefore,* <span class="math inline">\$A\$</span> has real eigenvalues.

Deductive reasoning comes up in everyday life, for example

1.  No one in my daughter’s preschool class has a nut allergy.

2.  Zoe is in my daughter’s preschool class.

3.  *Therefore*, Zoe is not allergic to peanuts.

This type of argument is *risk-free* in the sense that, as long as the premises are true, the conclusions must hold. Of course, the premises could be false: I might be confusing my neighbor Zoe with a different Zoe who is in my daughter’s class. But that is the only way my conclusion could be wrong.

Deductive arguments can involve statements about probability:

1.  This die has six faces labeled 1, 2, 3, 4, 5, and 6.
2.  If I roll it, it is equally likely to land on any face.
3.  *Therefore,* the chance of rolling a 4 is exactly 1/6.

A probability course like **Stat 205A** is about statements like this.

#### Inductive reasoning {.anchored anchor-id="inductive-reasoning"}

Statistics, on the other hand, is the mathematical science of **inductive reasoning**: reasoning from observations to make general claims about the world. Unlike deductive reasoning, such arguments are inherently *risky*: the conclusions we draw can be false even when the premises are correct.

Caution

Note that **inductive proofs** in mathematics are not an example of inductive reasoning as we mean it here. Inductive proofs are really examples of deductive reasoning because they provide a logically valid argument (i.e. the inductive step) for extending the conclusion to the entire class of objects under study.

For example:

1.  I ate a blueberry from the free sample tray at the supermarket.
2.  It was ripe and delicious.
3.  *Therefore*, if I buy a carton of blueberries, they will *probably* be ripe and delicious.

Here we have added the weasel word “probably” not to convey a rigorous quantitative statement about probability, but just to informally convey some uncertainty about the conclusion.

This example would be more persuasive if we had taken a sample randomly from the carton we planned on buying:

1.  I ate five blueberries at random from the carton I intended to buy.
2.  They were all ripe and delicious.
3.  *Therefore*, if I buy the carton, the rest of the blueberries will *probably* be ripe and delicious.

Of course, we could still always be wrong: maybe there were only five good blueberries in the whole carton and we just happened to take those. But that is not very likely.

Scientists very often reason inductively. For example:

1.  Water at 1atm of pressure has been observed to boil at 100°C every time it has been measured in the laboratory.

2.  *Therefore,* water at 1atm of pressure *probably* always boils at 100°C.

Inductive reasoning is the basis of all of the empirical sciences.

We can also make inductive statements about probability:

1.  I flipped this penny 1000 times and got 502 heads.

2.  *Therefore*, it *probably* has about a 50% chance of landing heads.

For now, we’ll assume we know what it means for a penny to have a 50% chance of landing heads; something like: it’s physical properties give it an equal chance of landing heads or tails (and a negligible chance of landing on its side or flying off into space). Generally, there is some controversy among different camps of philosophers and statisticians about what probability means, but not too much when it comes to coin flips. We’ll discuss this more later in the semester.

---

[← About Stat 210A](02-about-stat-210a.md) · [Up: contents](index.md) · [The problem of induction →](04-the-problem-of-induction.md)
