---
title: 11 outline
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/11-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 11 outline

**Source:** `lecture-outlines/11-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

A second study describes the development of a genetic oscillator based on the combination of positive and negative feedback:

M. R. Atkinson, M. A. Savageau, J. T. Myers, and A. J. Ninfa. _Cell_ **113** , 597-607

(2003)

In this lecture we will derive the stability diagram in Fig. 1B. In the model odd subscripts are used for mRNA whereas even subscripts are used for proteins. For example, the translation of mRNA is modeled as:


where _kp_ is the translation rate constant and β2 is the decay rate constant of the protein X2.


the form:


Analogously the system of equations describing the genetic circuit in Fig.1A is:


**[VII.19]**

The functions f1, f3, and f5 describe the transcriptional regulation and are defined by triphasic functions. For the stability analysis only the first four equations are relevant since no feedback occurs after x4. As described in the Supplementary information of the paper:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

39


In the case of a single fixed point, this point occurs at x1=x2=x3=x4=1. The matrix A is now defined as:


The eigenvalues of this matrix are found by solving:


This leads to the characteristic equation in the form:


Solving for the λ’s is difficult. However there is a convenient mathematical condition, called the Routh-Hurwitz criterion that allows you to determine the stability without explicitly calculating the eigenvalues. The Routh-Hurwitz criterion states that a system is stable (real part of all eigenvalues is negative) if all coefficients [VII.23] are positive and all elements in the first column of the Routh-Hurwitz matrix are positive. This matrix is constructed as follows:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

40

The matrix has n+1 (in our case 5) rows:


where


The Routh-Hurwitz stability criterion states that the number of roots with positive real parts is equal to the number of sign changes of coefficients in the first column of the matrix. Let’s apply this criterion to our problem. First we have to make sure that all coefficient ai are positive. ao and a1 are always positive, a4 is positive if:


This is the line with the negative slope in the stability diagram (Fig. 1B). a2 is positive if: β1β2 + β1β3 + β1β4 + β2β3 + β2β4 + β3β4 > _g_ 12β1β2 **[VII.27]**

If β1≈β3 and β2≈β4 this is satisfied when g12 < 4. Similarly, a3 is positive if

β1β2β3 + β1β2β4 + β2β3β4 + β1β3β4 > _g_ 12(β1β2β3 + β1β2β4 ) **[VII.28]**

If β1≈β3 and β2≈β4 this is satisfied when g12 < 2. Therefore the conditions for positive ai are:


The next step is to calculate b1, c1, and d1. Substitution in [VII.25] yields d1=b2=a4>0 because of [VII.26]. b1 >0 is equivalent to:

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

41


Rewriting gives:


The first term is larger than the last term in [VII.31] cancel if g12<4 which is already satisfied by [VII.29]. The remaining is:


The left sum has in total 12 terms whereas the right has four. So as long as g12<3, b1>0. The last condition to prove is: c1>0.


Substitution of [VII.25] gives:


The easiest way to solve this is graphically. The values for the degradation constants are: β1 = β3 = β5 = 20.8 + 0.696/ _td_ hr<sup>-1</sup> and β2 = β4 = β6 = 0.696/ _td_ hr<sup>-1</sup> . Figure 12 shows the stability region (also see MATLAB code 6).

# **MATLAB code 6: Routh-Hurwitz criterion:**

**clear; close; g1=0:0.1:4; t_D=0.5; b1=20.8+0.696/t_D; b2=0.696/t_D; b3=20.8+0.696/t_D; b4=0.696/t_D; a0=1; a1=(b1+b2+b3+b4); a2=(b1*b2+b1*b3+b1*b4+b2*b3+b2*b4+b3*b4)-g1*b1*b2; a3=b1*b2*b3+b1*b2*b4+b2*b3*b4+b1*b3*b4-g1*b1*b2*b3-g1*b1*b2*b4; y1=1-(a1*a2.*a3-a3.*a3)./(a1*a1*b1*b2*b3*b4); y2=1-g1; plot(g1,y1,'b',g1,y2,'r'); axis([0 4 -20 2]); grid on; xlabel('g12'); ylabel('g14g32');**

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

42


**Figure 12** . Stability analysis of synthetic oscillator of Atkinson et al.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– October 2004

43

---

[Up: contents](../index.md)
