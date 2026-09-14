---
title: 3 Repeated Prisoner's Dilemma (12 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/09-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 3 Repeated Prisoner's Dilemma (12 points)

**Source:** `psets/09-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The Prisoner's Dilemma is a two­player, two­strategy game, with the payof matrix

||Cooperate|Defect|
|---|---|---|
|Cooperate|�|S|
|Defect|T|P|


where _T > R > P > S_ and _R >_ ( _T_ + _S_ ) _/_ 2 .

Let us consider a repeated Prisoner's Dilemma<sup>2</sup> . Suppose that after each round of game there is a probability _w_ that another round will be played between the two players. Players have a

> 2Chapter 5 of "Evolutionary Dynamics" by Martin Nowak.

2

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 9

good memory and can remember the actions of their opponents in all previous rounds. \hile defection is an evolutionarily stable strategy (ESS) when individuals know they will never meet again, the fnite probability _w_ of repeated interaction may make other strategies evolutionarily stable. Axelrod and Hamilton<sup>3</sup> argued that a strategy called "tit­for­tat" is evolutionarily stable if _w_ is large enough. The tit­for­tat (TFT) strategy is defned as follows:

- Cooperate during the frst interaction,

- Do whatever your opponent did at the previous step of the game.

If two players both play TFT again each other, their payof is


- a. [6 points] Let's follow Axelrod's and Hamilton's derivation of TFT being evolutionarily stable for a large enough _w_ . In order to prove it, you need to know the that if TFT cannot be invaded by either the always defect (ALLD) strategy or the alternation of defection and cooperation (DC), it is evolutionarily stable.

   1. Find a condition for which TFT cannot be invaded by ALLD. For this, compare the payof of two players playing TFT (given by Equation 1) and the payof of ALLD playing against TFT.

   2. Find a condition for which TFT cannot be invaded by DC. (Note: The frst play of DC strategy is to defect.)

\e know that TFT is ESS if and only if it is invasible neither by ALLD nor by DC. Thus if both of the above conditions are satisfed by _w_ , TFT is ESS.

- b. [6 points] Boyd and Lorberbaum questioned the evolutionary stability of TFT. They used a diferent defnition of evolutionary stability. In particular, they showed that TFT can be invaded by a pair of mutants playing diferent strategies. In their discussion, they consid­ ered the following two strategies: 1) the tit­for­two­tats strategy (TFTT), which allows two consecutive defections before retaliating; and 2) the suspicious­tit­for­tat strategy (STFT), which defects on the frst encounter but thereafter plays tit­for­tat.

Compare how TFT and TFTT behave against STFT. Show that TFT is not evolutionarily stable (if two mutants invade it simultaneously, one playing TFTT, the other playing STFT) for large _w_ . \hat is the critical _wc_ ?

---

[← 2 Adaptation in a Sharply Peaked Fitness Landscape (10 points)](03-2-adaptation-in-a-sharply-peaked-fitness-landscape-10-points.md) · [Up: contents](index.md) · [4 Stochastic Simulations of the Error Threshold (17 points) →](05-4-stochastic-simulations-of-the-error-threshold-17-points.md)
