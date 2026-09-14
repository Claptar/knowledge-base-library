---
title: References
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/recordings/l3-syllabus-transcript.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# References

**Source:** `recordings/l3-syllabus-transcript.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

1. J. Hasty, J. Pradines, M. Dolnik, and J. J. Collins. Noise-based switches and amplifiers for gene expression. _PNAS_ **97** , 2075-2080 (2000).

The goal of this Section is to apply our knowledge of reaction kinetics and equilibrium binding to a real biological problem: the lysis-lysogeny decision of the bacterial phage lambda. The first goal is to derive the kinetic equation **[7]** in Hasty’s paper.

Figure 5 schematically depicts the genetic regulation of the PRM λ promoter. The gene of this promoter, called _cI_ , encodes for a repressor protein, which in turn dimerizes and binds to the DNA as a transcription factor. In this model Hasty _et al._ assume that binding to OR2 enhances transcription whereas binding to OR3 switches off transcription. Note that the wild-type lambda operon has three binding sites.


<!-- Start of picture text -->
K1<br>λ λ<br>λ<br>K2<br>λ<br>λ λ<br>OR2  OR3<br>λ λ<br>OR2  OR3<br>λ λ λ λ<br>OR2  OR3<br><!-- End of picture text -->

**Figure 5.** Possible binding states for the lambda promoter considered by Hasty _et al._ In the unbound state the gene is switched off.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

15


The system of reactions [III.1] reflects the reaction depicted in Fig. 5.  The first four equations are fast reversible reactions since DNA binding and unbinding of the repressors dimers and the dimerization itself occur within seconds, whereas the synthesis (transcription, translation, folding) and degradation (e.g dilution through cell growth) of monomers takes minutes to sometimes an hour. Therefore, the first four reactions are in equilibrium and the steady state concentrations are given in terms of the equilibrium constants. This separation of time scales is an important step in simplifying the model. Since the first four reactions in [III.1] are in equilibrium compared to protein synthesis and degradation, the concentrations of the ‘fast’ variables are (y=[X2]; d=[D]; u=[DX2]; v=[DX2*]; z=[DX2X2]):


Where:


The only slow variable is the concentration of cI monomers x=[X]. The rate of synthesis of repressor monomer is given by:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

16

where po is the concentration of RNA polymerase (assumed to be constant). A basal synthesis rate is modeled by r. In other words the promoter is never fully off, but leaks at a rate r. Now realizing that the total amount of lambda promoter sites dT is conserved:


This, together with [III.2] gives:


Using this result [III.4] becomes:


Now the goal is to ‘clean up’ the ugly looking [III.7]. This is done by normalizing the variables x and t. Since the product K1K2 always appears before x<sup>2</sup> it is logical to introduce a new variable:


Since the units of K1 and K2 are [1/concentration], _~~x~~_ is dimensionless. Using this new variable [III.7] reduces to:


An additional ‘clean-up’ arises when the time is normalized into a dimensionless form:


Using this, gives:


Or,


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– September 2004

17

The dimensionless parameter α is effectively a measure of the synthesis rate of monomer relative to the basal level of expression. The parameter γ reflects the ratio of degradation of monomer relative to the basal level. Matlab code 2 solves the kinetic equation [III.12]. Note that dependent on the initial conditions the system can have different steady state solutions.

**MATLAB Code 2:** Solution of equation [III.12]

**% filename: hasty.m alpha=50; gamma=20; sigma1=1; sigma2=5; options=[]; [t1 y1]=ode23('hastyfunc',[0 10],[0],options,alpha,gamma,sigma1, sigma2); [t2 y2]=ode23('hastyfunc',[0 10],[1],options,alpha,gamma,sigma1, sigma2); plot(t1,y1(:,1),'b',t2,y2(:,1),'r');**

**% filename: hastyfunc.m function dydt = f(t,y,flag,alpha,gamma,sigma1,sigma2) % [x] = y(1) dydt = [alpha*y(1)^2/(1+(1+sigma1)*y(1)^2+sigma2*y(1)^4)gamma*y(1)+1];**

---

[← III A Genetic Switch in Lamba Phage](01-iii-a-genetic-switch-in-lamba-phage.md) · [Up: contents](index.md) · [I.4 Phage lambda and multistability →](03-i-4-phage-lambda-and-multistability.md)
