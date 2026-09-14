---
title: 2 cAMP system (28 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/07-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 2 cAMP system (28 points)

**Source:** `psets/07-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Dictyostelium amoebae are free living cells with a remarkable twist: under the stress of starvation, large numbers of amoebae are able to collect together to form a single multi-cellular organism (Fig. 1). The entire process begins when starving amoebae emit pulses of the chemoattractant cAMP, inducing the surrounding cells to move in their direction and to secrete cAMP themselves. This process generates outgoing spiral waves of cAMP which direct the entire population towards the original source (Fig. 2). We will try to understand the origin of and the response to these cAMP waves.

Dictyostelium life cycle removed due to copyright restrictions. Please see http://www.dictyostelium.com/devcyc.gif.

© The Royal Society. All rights reserved. This content is excluded from our Creative Commons license. For more © fro information, see http://ocw.mit.edu/help/faq-fair-use/.

Problem 2 courtesy of Alexander van Oudenaarden. Used with permission.

## 2.1 Chemical kinetics of cAMP signaling (6 points)

Two species of cAMP receptors exist in the Dictyostelium cell membrane: an `activator' _A_ , and an `inhibitor' _I_ , both of which act on a third protein _R_ . When bound to cAMP, a pair of _A_ molecules catalyzes the conversion of _R_ to an active form _R_<sup>_∗_</sup> , and a pair of _I_ molecules catalyzes the reverse reaction (Fig. 3).

1

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 7

a. The initial binding of cAMP, _C_ , to its receptors is described by:


Write down equations describing the time evolution of [ _AC_ ] and [ _IC_ ] . Assume that [ _AC_ ] _≪_ [ _Atot_ ] , and [ _IC_ ] _≪_ [ _Itot_ ] ; let _a_ be proportional to [ _AC_ ] , _i_ to [ _IC_ ] , and _c_ to [ _C_ ] . By making a convenient choice of units, show that these equations can be written in the form


b. The reactions involving activation and inactivation of R reach a rapid equilibrium:


The _a_<sup>2</sup> and _i_<sup>2</sup> terms arise because it takes two molecules of _AC_ or _IC_ to catalyze these conversion reactions. Setting _β_ = _kR_<sup>_−_</sup> +<sup>,ndanexpressionfortherapidequilibriumvalueof</sup> _kR r_ = [ _R_<sup>_∗_</sup> ] in terms of _a_ , _i_ , and [ _Rtot_ ] .


© source unknown. All rights reserved. This content is excluded from our Creative Commons license. For more information, see http://ocw.mit.edu/help/faq-fair-use/.

## 2.2 Positive feedback and oscillations (12 points)

The molecule _R_ is an enzyme known as adenylate cyclase, which in its active form catalyzes the conversion of ATP into cAMP in the cytoplasm. The presence of extracellular cAMP thus stimulates the synthesis of intracellular cAMP, which in turn is secreted into the environment, creating a positive feedback loop (Fig. 3). Let _c_ 1 = [cAM _Pin_ ]; let the rate of cytoplasmic cAMP synthesis be _k_ 1 _r_ ; and let the rate constant for its secretion be _k_ 0 . _cAMP_ is continuously degraded by phosphodiesterase enzymes both inside and outside the cell, with rate constants _γ_ 1 and _γ_ 0 , respectively. The entire network is described by the following equations:


- a. Assuming that the concentrations _c_ 1 and _a_ reach rapid equilibrium, reduce the four equations in (1) and (2) to two equations for the slow variables _c_ and _i_ . Show explicitly the choice of units required to produce the simplied form shown in (3). What is the value of k?


2

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 7

- b. When Dictyostelium is grown in liquid medium, extracellular cAMP is well stirred, making its concentration uniform over space. However, under such conditions, the cAMP concentration is known to oscillate over time. Find the conditions on _k_ and _β_ so that the system is oscillatory (we are talking about limit cycle oscillations here).

- c. **COMPUTATION** On a graph of _i_ vs. _c_ , plot the nullclines and simulate the time evolution of the system for an oscillatory case.

- d. Suppose the system only required a single molecule of _AC_ or _IC_ in order to catalyze the _R_ conversion reactions. Comment on the behavior of the system in this case.

## 2.3 **COMPUTATION** Diusion and cAMP waves (10 points)

When cells are grown on a plate, cAMP diusion is slow, and the extracellular cAMP concentration is no longer uniform. Consider a plate on which there exists a uniformly distributed population of cells. Each cell senses cAMP in its environment, and secretes fresh cAMP in response. This new batch of cAMP is able to reach neighboring cells, stimulating them to synthesize more cAMP, and so on. The situation is similar to one in which a number of radio transmitter towers (cells) are used to detect, amplify, and re-broadcast a weak radio signal (cAMP). The cAMP concentration now varies over space as well as time. For simplicity, we will analyze a 1-dimensional case, with cells uniformly distributed along a line. We can assume that the cells have xed positions over the timescales considered, because their chemotaxis is relatively slow. This system obeys the equations


In this problem you will have to develop a numerical code for simulating these equations<sup>1</sup> . The system is assumed to extend from _x_ = _−_ 1 to _x_ = +1 , with no ow at the boundaries. As for the initial conditions, consider a pulse of cAMP centered in the origin, that goes to zero towards the boundaries and that has a typical width _σ_ (try to use a smooth but localized function); assume an uniform initial concentration of inhibitor _io_ .

- a. Use the following parameters: _β_ = 4 , _k_ = 0 _._ 5 , _D_ = 10<sup>_−_7</sup> , _σ_ = 0 _._ 1 , and _io_ = 0 _._ 1 . Run the simulation to see the emergence of cAMP waves emanating from the origin. Plot a typical cAMP prole, indicating the direction of motion of the waves.

- b. Run the simulation again, this time with a k value which produces a non-oscillating system. Describe the typical cAMP prole once the transients have died out. Can cells nd the initial source of cAMP based on this type of prole?

- c. A simple concentration gradient would allow cells to nd the cAMP source. Why do you think Dictyostelium uses waves of cAMP rather than a gradient in order to trigger cell aggregation?

## Feedback (+1 Extra Credit)

> 1Page 76-78 of the supplementary notes by Alexander van Oudenaarden under Reaction-Diusion models in the materials section.

3

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 1 Design principles (22 points)](02-1-design-principles-22-points.md) · [Up: contents](index.md)
