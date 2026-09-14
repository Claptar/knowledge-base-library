---
title: 03 questions
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/psets/03-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 03 questions

**Source:** `psets/03-questions.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**Systems Biology**

**7.81/8.591/9.531**

# **Problem Set 3 Due in class**

**Assigned: 10.19.04 Due: 11.02.04**

Several protein expression levels in plant and animal cells go through a daily cycle, driven by exposure to sunlight during the day and darkness at night. However, even in complete darkness, these expression levels oscillate with an intrinsic period of about 24 hours. The systems which drive these oscillations are known as _circadian clocks_ . At the heart of most of these systems is a pair of transcriptionally regulated proteins: an activator ( _X_ ) and an inhibitor ( _Y_ ). In this problem set, we will see how such a simple system can be made to generate oscillations. We consider two possible system architectures (arrows represent activation, blunt ends represent inhibition):


<!-- Start of picture text -->
(A)    (B)<br>X  Y  X  Y<br><!-- End of picture text -->

The corresponding dynamical equations are (using _x_ = [ _X_ ]  and _y_ = [ _Y_ ]):


   1. Biochemical interpretation of dynamical equations

- (10) _a._ Identify the parameters corresponding to basal transcription rate, maximal transcription rate, and degradation rate.

- (10) _b._ We have assumed the following: for both (A) and (B), the _X_ promoter is inactivated by the binding of a single molecule of _Y_ , and the _Y_ promoter is activated by the binding of a single molecule of _X_ . In addition, for (B), the _X_ promoter is activated by the cooperative binding of two molecules of _X_ . The various fractions that appear in the dynamical equations represent the fractions of promoters that are active under these conditions. Give a biochemical interpretation of each of these fractions.

   2. Normalization of units. Assume that _A2_ >> _x_ . Define new time and concentration units so that _<u>t</u>_ = γ _yt_ , _<u>x</u>_ = _x_ / _A_ 3 , and _<u>y</u>_ = _y_ / _A_ 1 . The dynamical equations can then be written in the following form:


1

FA04

**Systems Biology**

**7.81/8.591/9.531**

- (10) _a._ Calculate the values of the new (barred) parameters in terms of the old parameters.

   - _b._ Discuss whether these equations can be further simplifed by normalization of units.

(10) _b._ Discuss whether these equations can be further simplifed by normalization of units. From now on we will work with the simplified equations, dropping the bars on our variable and parameter symbols. These equations are of the general form


_Choose one of the following two problems._

   3. Global dynamics. Assume the following parameter values: _vx_ = 0.1; _vy_ = 0.0; _kx_ = 4.0; _ky_ = 2.0; γ _x_ = 10.0. Do this problem for systems (A) and (B) separately.

- (30) _a._ On a graph of _y_ vs. _x_ , plot the nullclines _f_ ( _x,y_ ) = 0 and _g_ ( _x,y_ ) = 0. You should find that the nullclines intersect only once, dividing the graph into four regions. For each of these regions, draw a few arrows indicating the direction of motion (e.g. if _dx/dt_ < 0 and _dy/dt_ > 0, the arrows point NW). Comment on the stability of the fixed point.

- (30) _b._ Write a MATLAB program to solve the dynamical equations upto _t_ = 20.0. Plot the output on a graph along with the nullclines. You should find that system (A) does not oscillate, while system (B) does. It turns out that autoactivation by _X_ is crucial to the generation of oscillations. Problem 4 examines the reasons why this is so.

   4. Stability analysis. Let { _x0_ , _y_ 0} be a fixed point of the system (so that _f_ ( _x0_ , _y0_ ) = 0, _g_ ( _x0_ , _y0_ ) = 0). Define the matrix


Recall that the fixed point is stable if and only if Tr _A_ < 0 and Det _A_ > 0.

- (20) _a._ For system (A), prove that the system will always converge to a stable fixed point.

- (20) _b._ For system (B), assume the following parameter values: _vx_ = 0.1; _vy_ = 0.0; _kx_ = 4.0; _ky_ = 2.0. Let γ _x_ be a free parameter.

Find the fixed point of the system numerically. The matrix _A_ evaluated at the fixed point should be a function of γ _x_ alone. Oscillations will arise whenever this fixed point becomes unstable. Write down the conditions on γ _x_ under which the system is oscillatory. (This transition from a stable to an oscillatory system is known as a Hopf bifurcation.)

- (20) _c._ For system (B), write a MATLAB program to solve the dynamical equations using the parameters given in part _b_ . Do this for two values of γ _x_ , one of which gives an oscillatory system, and the other a stable one. On the same graphs plot out the nullclines _f_ ( _x,y_ ) = 0 and _g_ ( _x,y_ ) = 0.

- (0) _d._ CHALLENGE. In the limit γ _x_ >> 1, estimate the period of system oscillations.

2

FA04

---

[Up: contents](../index.md)
