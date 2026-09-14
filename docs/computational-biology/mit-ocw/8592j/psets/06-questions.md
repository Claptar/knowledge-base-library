---
title: 06 questions
source: https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/
source_file: sources/ocw-8592j/psets/06-questions.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 06 questions

**Source:** `psets/06-questions.pdf` from [ocw-8592j](https://ocw.mit.edu/courses/8-592j-statistical-physics-in-biology-spring-2011/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

8.592J–HST.452J: Statistical Physics in Biology

Assignment # 6

Force-Extension Curves

1. Linear polymers: Using optical tweezers, it is now possible to pull on the two ends of a single molecule. (Actually the tweezers pull on latex balls that are attached to the ends of the polymer; a complication that we shall ignore.) In the presence of the force F F pulling on the ends of the polymer, there is an additional energy term


where R<sup>F</sup> = FrN − Fr1 is the end–to–end distance (between the first and N<sup>th</sup> monomers) of the chain.

F

(a) For an ideal polymer, the number of configurations with an end–to–end distance of R is given by the usual Gaussian formula


By integrating the Boltzmann weight over all R<sup>F</sup> , calculate the (Gibbs) partition func­ tion Z(N, F, T ) at a temperature T . Using this result, obtain the mean extension RF = kBT∂ ln Z/∂F along the direction of the force FF .

(b) For other cases in which ΩN does not have a simple form (such as for self-avoiding polymers), it is still possible to obtain the linear response of the polymer to small force. To F F F this end, expand the Boltzmann weight exp F · R/kBT to second order in F , and hence ( ) show that


where (R<sup>2</sup> )0 is the mean end–to–end squared d istance of the polymer in the absence of the force.

(c) Dimensional analysis suggests that quite generally the extension–force curve for polymers should have the form


The left hand side is a dimens ionless extension; on the right hand side a dimensionless combination involving the force appears as the argument of an unknown function Φ. At large forces F , the polymer becomes stretched such that Rf ∝ N. For self-avoiding polymers J(R<sup>2</sup> )0 ≈ aN<sup>ν</sup> with ν ≈ 0.59. Use these facts to deduce a non-linear behavior RF ∝ F<sup>λ</sup> for the extension at large force, and give the value of the exponent λ. *****

F

2. Denaturing DNA by force: Obtain the phase diagram of DNA pulled by a force F , by generalizing the Poland–Scheraga model as follows:

1

(a) By integrating over the position vectors, show that the (Gibbs) partition function of DNA of length N can be decomposed into products of contributions from double-stranded rods and single stranded bubbles, as


(b) Treat the double stranded segments as rigid rods of fixed length aℓ. By integrating over all orientations in three dimensions show that


where w = e<sup>−βε</sup> , and ε is the energy gain of forming the double strand.

(c) Treat the double stranded loop as two random walks of length ℓ connected at the two end points. Integrating over all separations of the two end points show that


(d) Examine the problem in a (grand canonical) ensemble with variable DNA lengths N, additionally weighted by a factor of z<sup>N</sup> . Give the expressions for the (Laplace) transformed B<sup>˜</sup> (z) and R<sup>˜</sup> (z) in this ensemble in terms of the (Bose) sums fm<sup>+</sup> (x) = L∞ℓ=1 x<sup>ℓ</sup> /ℓ<sup>m</sup> . (e) Show that the strands become fully separated at a critical point s atisfying R ˜ = B<sup>˜−1</sup> = (sζ3/2r−1, where ζ3/2 ≡ f3+/2<sup>(1) ≈2.612.</sup>

(f) For s = 1, plot the phase diagram of the model in the coordinates (w/g<sup>2</sup> ) and (βFa).

*****

3. Over-stretching DNA: In standard (B–from) DNA the basepairs stack in spiral fashion at separation of 3.4<sup>˚</sup> A. As indicated in the following figure [from S. B. Smith, Y. Cui, C. Busta­ mante, Science 271, 795 (1996), and http://alice.berkeley.edu/˜ steve/DNAstr.html], pulling on DNA with optical tweezers causes it to greatly stretch at forces of around 65±5pN.

(a) One interpretation is that this represents a transition to a new structure of over-stretched DNA, in which the separation of bases has increased to 5.8<sup>˚</sup> A. As a very simple model of this putative state consider DNA as a one dimensional chain in which each unit can either be in the regular form of size 3.4<sup>˚</sup> A, or in the stretched form of size 5.8<sup>˚</sup> A. Assume that an energy U is required to change the regular form to the stretched form. For this part of the problem ignore the three dimensional orientations of each segment, and assume that the state of each element is independent of its neighbors. Calculate the length L(F, T ) for this model when pulled by a force F at a temperature T .

(b) Compare the result from part (a) to the experimental figure, and thus estimate the parameter U from the data in the above model from experiments. Is the width of the transition region in F consistent with the assumptions of the model.

2


(c) Now consider a more realistic model in which neighboring elements tend to be in the same state. Would this lead to a sharpening or widening of the transition region in F ? *****

4. Denaturing RNA by force: By pulling on the ends of RNA, the hydrogen bonds can be broken to yield a stretched polymer. Let us model the partially denatured state as a sequence of linear segments with no hydrogen bonds and ‘blobs’ which are hydrogen bonded (opposite to the case of DNA). Assume that the force carrying backbone of the molecule is made up of the linear segments, and that the RNA blobs carry no force (similar to the loop in problem 2). After integrating over the position vectors, the (Gibbs) partition function of an RNA of length N can be written as


The contributions of linear and blob segments are respectively


(a) Exploit the mathematical similarity to the Poland–Scheraga model to evaluate the grand partition function of the model.

(b) Identify the force Fc at which denaturation starts.

(c) Sketch the fraction of denatured sites as a function of force, clearly indicating the nature of the singularity at Fc.

*****

3

5. (Optional) Pulling RNA: The server on http://bioinfo.ucsd.edu/rna/ (or the pulling server at http://bioserv.mps.ohio-state.edu/rna/) gives force extension curves for RNA based on secondary structure calculations. Use this server to examine force extension curves for: (a) a uniform sequence; (b) an alternating sequence of G and C; (c) an alternating sequence of A and U; (d) an actual RNA sequence. (Choose sequences of roughly the same length.) Comment on the general characteristics of these curves. Does any of them resemble the theoretical result from the previous problem?

*****

4

MIT OpenCourseWare http://ocw.mit.edu

8.592J / HST.452J Statistical Physics in Biology Spring 2011

For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

---

[Up: contents](../index.md)
