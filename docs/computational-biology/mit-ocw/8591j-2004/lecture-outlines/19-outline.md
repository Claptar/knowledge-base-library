---
title: 19 outline
source: https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/
source_file: sources/ocw-8591j-2004/lecture-outlines/19-outline.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 19 outline

**Source:** `lecture-outlines/19-outline.pdf` from [ocw-8591j-2004](https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2004/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

# **IX Models for eukaryotic gradient sensing**

The first model on gradient sensing we discussed was developed by Narang _et al._ :

A. Narang, K. K. Subramanian, and D. L. Lauffenburger. A mathematical model for chemoattractant gradient sensing based on receptor-regulated membrane phospholipid signaling dynamics. _Ann. of Biomed. Eng._ **29** , 677-691 (2001).

Let use the reduced scheme in Fig. 2b of Narang’s paper as a starting point. The model describes the time evolution of four concentrations: the active receptors (r10), the membrane phosphoinositides (p), the cytosolic inositol (i), and the phosphoinositides in the endoplasmic reticulum (ps). For the receptors Narang et al. use a very similar approach as discussed for bacterial chemotaxis (Fig. 3, Narang’s paper). For Dictyostelium chemotaxis it is assumed that only the non-phosphorylated receptors are involved in the pathway. The total concentration of sensitive (non-phosphorylated) receptors is therefore:


The first subscript indicates if a ligand is bound (1) or not bound (0) to the receptor. The second subscript reflects the phosphorylation state: phosphorylated (1) or not phosphorylated (0). The asterix indicates that the receptor is complexed to the deactivating (Ed) or activating enzyme (Ea).

The kinetic equation for rs is:


where Dr is diffusion coefficient of the receptor in the membrane and R is the cell radius. In this model any chemical gradients in the cell’s cytoplasm are ignored and only gradients in the membrane are considered. In the model it is assumed that dephosphorylation is independent of ligand concentration (k01=k11). Note that this is conceptually identical to Barkai’s model for perfect adaptation (demethylation is independent of ligand concentration, keff4 is independent of ligand). It is also assumed

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

50

that the system reaches a quasi-steady state for the ligand binding, and the enzymes Ea and Ed that remove and add the phosphates. Ea activates the receptor by phosphorylation and Ed deactivates the receptor by dephosphorylation. Only activate receptors are involved in the signaling pathway. Therefore:


Kl and K10 are dissociation constants for the ligand-receptor binding and Ed-receptor binding. Ea is binding its substrates with a high affinity (K01,K11 << 1) and Ea is assumed to operate at saturation. Again this is conceptually identical to the assumption that CheR is operating at saturation for bacterial chemotaxis. Therefore:


ea,t is the total concentration of Ea. Substituting [IX.1], [IX.3] and [IX.4] in [IX.2] gives:


This is equation (1) in Narang’s paper. Equations (2)-(4) describe the time evolution of the three other variables:


cp and ci are basal synthesis rates of P and I synthesis respectively. P and I decay according to first order kinetics with rate constants kp and ki. The receptor mediated synthesis of P is cooperative (nH=2) and autocatalytic. Note that the approximation kfr10p<sup>2</sup> ps is only valid for low concentrations of p and ps. P is removed from the

membrane at a rate krpi. It is clear from [IX.6] that the total amount of phosphoinositides (p+ps) is conserved. The factor s in the last equation of [IX.6] denotes the membrane

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

51

length per area. This factor is required since the synthesis and removal of P is based on the length of the plasma membrane. The system of equations [IX.5]-[IX.6] are reactiondiffusion equations similar to the equations discussed in Section XIII. The role of activator is played by P whereas I acts as an inhibitor. Note that the inhibitor diffuses much faster than the membrane bound activators (Dp<<Di).

Narang uses periodic boundary conditions for all four variables of the form:


where x={r10,p,ps,i}. The homogeneous solutions are depicted with the superscript -. For a uniform simulation with ligand concentration l<sup>-</sup> , the steady-state values for the homogeneous solutions are:


Assuming the cell has reach steady state for a uniform stimulus l<sup>-</sup> , now the ligand profile is instantaneously changed to l(θ). We assume that immediately after this change r00, r10, and r<sup>*</sup> 10<sup>equilibrate but r</sup> s<sup>, p, p</sup> s<sup>and i remain unchanged since these reaction are much</sup> slower. The total amount of active receptors is:


Therefore, immediately after the change from uniform the gradient stimulation r10 changes to:


The initial conditions are therefore:


7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

52

This is basically all we have to know to solve the model. Narang adds one more step to obtain dimensionless equations.

7.81/8.591/9.531 Systems Biology – A. van Oudenaarden – MIT– November 2004

53

---

[Up: contents](../index.md)
