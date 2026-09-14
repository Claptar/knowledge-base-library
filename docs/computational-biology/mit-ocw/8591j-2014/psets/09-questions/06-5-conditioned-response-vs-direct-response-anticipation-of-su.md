---
title: '5 Conditioned Response vs. Direct Response: Anticipation of Sugars in E. coli
  (19 points)'
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/09-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 5 Conditioned Response vs. Direct Response: Anticipation of Sugars in E. coli (19 points)

**Source:** `psets/09-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

E. coli can anticipate the future availability of maltose based on the appearance of lactose. Now consider the two signals _S_ 1 (lactose) and _S_ 2 (maltose), separated by a time Δ _t_ where _S_ 2 gives rise to a response _R_ 2 , in this case _R_ 2 is some protein necessary for the use of maltose as a nutrient. \e have two strains, one only responds directly to _S_ 2 to achieve _R_ 2 (direct response, D�), the other one anticipates _R_ 2 by upregulating genes associated with _R_ 2 after the appearance of _S_ 1 (conditioned response, C�). \e will identify the conditions when conditioned response is superior to direct response. The frst panel of the following fgure shows the response of both systems. The solid line corresponds to C� and the dashed line corresponds to the D�.

4

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 9

- a. [2 points] For both types of responses, what is the response function _Y_ ( _t_ ) (i.e. response level) of each system from time _t_ = 0 until the disappearance of _S_ 2 ? Normalize the functions to the steady state of the system.

- b. [4 points] Expression of protein necessary to process _S_ 2 carries a cost _c_ (a decrease in growth rate), and a beneft _b_ (an increase in growth rate) due to the advantage given by responding to _S_ 2 .

   1. Sketch in the panels the cost and beneft functions of each system. Set each to one if no benefts or cost exists at certain times. Assume that the cost is proportional to the production level and the beneft is proportional to the amount of the protein in a cell.

   2. Calculate the beneft functions _b_ ( _t_ ) and cost functions _c_ ( _t_ ) for the systems given that maximum beneft (i.e. the maximum growth rate without any costs) is 1 + _κ_ and maximum cost (i.e. the minimum growth rate) is 1 _− η_ .

- c. [1 point] The ftness of each species can be written as


where _b_ ( _t_ ) and _c_ ( _t_ ) are beneft and cost functions. \rite down the ftness of C� and D�. Do not evaluate the integrals.

- d. [3 points] \rite down the relative ftness function Δ _FCR−DR_ = _FCR − FDR_ for both coupled and uncoupled appearance of signals (i.e. when _S_ 1 and _S_ 2 appear sequentially vs. when only _S_ 1 appears). The duration of the signal _S_ 1 is _TS_ 1 . Evaluate the integrals for Δ _FCR−DR_ .

- e. [3 points] Let's defne _p_ as the probability that _S_ 2 will occur given _S_ 1 . Combine the functions derived above into a single equation to give the relative ftness Δ _FCR−DR_ in an environment where both coupled and uncoupled appearances may occur.

- f. [3 points] **COMPUTATION** Set _κ_ = 0 _._ 17 and _η_ = 0 _._ 045 . The generation time is set to 1 and the duration of the signal _S_ 1 ( _TS_ 1 ) is 0.25. Explore the phase space of Δ _t_ and _p_ for parameter values that maximize and minimize the relative ftness Δ _FCR−DR_ .

- g. [3 points] **COMPUTATION** Find Δ _t_ that gives the maximum overall ftness. Does it make sense?

5

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 9


<!-- Start of picture text -->
S2<br>S1<br>YST<br>0<br>0 Δt Time<br>Cost<br>1<br>0 Δt Time<br>Benefit<br>1<br>6<br>0 Δt Time<br>R level2<br>Growth rate<br>Growth rate<br><!-- End of picture text -->

MIT OpenCourseWare http://ocw.mit.edu

8.591J / 7.81J / 7.32 Systems Biology Fall 2014

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[← 4 Stochastic Simulations of the Error Threshold (17 points)](05-4-stochastic-simulations-of-the-error-threshold-17-points.md) · [Up: contents](index.md)
