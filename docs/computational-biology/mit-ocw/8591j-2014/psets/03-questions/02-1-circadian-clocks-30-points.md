---
title: 1 Circadian Clocks (30 points)
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/
source_file: sources/ocw-8591j-2014/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 1 Circadian Clocks (30 points)

**Source:** `psets/03-questions.pdf` from [ocw-8591j-2014](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

Several protein expression levels in plant and animal cells go through a daily cycle, driven by exposure to sunlight during the day and darkness at night. However, even in complete darkness, these expression levels oscillate with an intrinsic period of about 24 hours. The systems which drive these oscillations are known as circadian clocks. At the heart of most of these systems is a pair of transcriptionally regulated proteins: an activator (X) and an inhibitor (Y). In this problem set, we will see how such a simple system can be made to generate oscillations. \e consider two possible system architectures (arrows represent activation, blunt ends represent inhibition):


Problem by Alexander van Oudenaarden. OCW 8.591J Systems Biology, Fall 2004, Problem Set 3, Problem 1.

The corresponding dynamical equations are (using _x_ = [ _X_ ] and _y_ = [ _Y_ ] ):


- a. Identify the parameters corresponding to basal transcription rate, maximal transcription rate, and degradation rate.

- b. \e have assumed the following: for both (A) and (B), the X promoter is inactivated by the binding of a single molecule of Y, and the Y promoter is activated by the binding of a single molecule of X. In addition, for (B), the X promoter is activated by the cooperative binding of two molecules of X. The various fractions that appear in the equations represent the activity of promoters. Explain what each of these fractions means in the context of gene regulation.

- c. Normalization of units. Assume that _A_ 2 _» x_ . Redefne variables and show that by choosing units properly the previous equations can be written in the form

1

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 3


(B)


From now on we will work with the simplifed equations, dropping the bars on the variable and paramter symbols. These equations are of the general form


Let ( _x_ 0 _, y_ 0) be a fxed point of the system ( _f_ ( _x_ 0 _, y_ 0) = 0 _, g_ ( _x_ 0 _, y_ 0) = 0 ) and recall that if we defne


fxed points of this two dimensional system are stable if and only if _Tr_ ( _A_ ) _<_ 0 and _Det_ ( _A_ ) _>_ 0 .

d. **COMPUTATION** For systems (A) and (B) separately, assume _vx_ = 0 _._ 1 , _vy_ = 0 _._ 0 , _kx_ = 4 _._ 0 , _ky_ = 2 _._ 0 and _γx_ = 10 and plot the nullclines _f_ ( _x, y_ ) = 0 and _g_ ( _x, y_ ) = 0 on the y vs. x phase plane. Draw the vector feld indicating the direction of motion in diferent regions of the plane and, based on the graphs, comment on the stability of the fxed point.

e. For system (A), prove that the system will always converge to a stable fxed point.

f. For system (B),

1. Assume _vx_ = 0 _._ 1 , _vy_ = 0 _._ 0 , _kx_ = 4 _._ 0 , _ky_ = 2 _._ 0 and let _γx_ be a variable parameter. Find the fxed point of the system. If this fxed point becomes unstable oscillations will arise. By numerically analyzing _Tr_ ( _A_ ) and _Det_ ( _A_ ) as a function of _γx_ write down the conditions on _γx_ under which the system is oscillatory. \hat does this condition mean in terms of the timescale of X and Y?

2. **COMPUTATION** Solve the equations numerically using the parameters given in (f1). Choose two diferent values of _γx_ , in one case the system shows sustained oscillations, while in the other case the system approaches a stable fxed point.

2

Systems Biology <u>(7.32/7.81J/8.591J)</u>

Problem Set 3

3. **COMPUTATION** By varying _γx_ , we can tune the period of the oscillator. How much does the amplitude of oscillations change? \hat would you expect in the case of a repressilator? Interprete your results and comment on the tunability<sup>1</sup> of an oscillator.

4. System (B) is a network motif found in many biological oscillatory systems (Uri Alon's book, Chapter 6.5). Look up in the literature for an example.

---

[← Problem Set 3](01-problem-set-3.md) · [Up: contents](index.md) · [2 Deterministic scale-free networks2 (15 points) →](03-2-deterministic-scale-free-networks2-15-points.md)
