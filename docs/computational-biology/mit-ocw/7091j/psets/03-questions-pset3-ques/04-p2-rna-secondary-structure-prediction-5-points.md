---
title: P2. RNA secondary structure prediction (5 points).
source: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
source_file: sources/ocw-7091j/psets/03-questions-pset3-ques.pdf
licence: CC BY-NC-SA 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# P2. RNA secondary structure prediction (5 points).

**Source:** `psets/03-questions-pset3-ques.pdf` from [ocw-7091j](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) · **Licence:** CC BY-NC-SA 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

**(A -  3 points)** Use the Nussinov algorithm to find the secondary structure that maximizes the number of Watson-Crick base-pairs in the following RNA sequence (show your work):

# CGAGUCGGAGUC


**(B – 2 points)** Run this sequence through the mfold RNA folding server (default parameters) at: http://mfold.rit.albany.edu/?q=mfold/RNA-Folding-Form

Examine the top two structures it produces by looking at the “pdf”s under “View Individual Structures:”. Notice that they don’t match the structure predicted by the Nussinov algorithm. Examining the examples of real RNA secondary structures shown in lecture (slides 12, 32, 39 of Lecture 11), generate a hypothesis for which criteria used by the mfold algorithm to describe RNA thermodynamics prevents this algorithm from predicting the structure returned by the Nussinov algorithm in part (A). Test your hypothesis by strategically inserting adenosines at locations (e.g. in loops, between stems, across from bulges) necessary in the sequence above and finding the minimum number that must be inserted so that the top mfold-predicted structure has pairs between the same bases as in your Nussinov base pair-maximization structure.

**<mark>(A – 1 point)</mark>** <mark>Go to the Protein Data Bank (http://www.rcsb.org/pdb/home/home.do) and search for the protein we’ll be working with – 1YY8. What is this molecule? By looking at the “3D View” tab of this protein, what is the predominant secondary structure (α-helix or β-sheet)?</mark>

**<mark>(B – 1 point)</mark>** <mark>In order to open and edit the pyRosetta</mark> _ <mark>1YY8.py file, you will need to use a text editor on Athena’s Dialup Service, which doesn’t register commands from the mouse. If you’re familiar with emacs or vim, these are great options, otherwise we recommend nano, a friendly text editor that can be navigated with the arrow keys. Open the file for editing by typing:</mark>

<mark>nano pyRosetta_1YY8.py</mark>

<mark>You can scroll with the arrow keys, and additional commands are shown at the bottom of the Terminal, where ^ is the Control key. Once you’ve made any changes, to exit and save, type “Control + x” followed by “y” and then Enter to signify yes, you want to save your changes.</mark>

<mark>Look over how the code for part</mark> _ <mark>b() loads the PDB file 1YY8.clean.pdb (which has been cleaned to remove non-atomic annotation information) and prints out the protein’s angles and energy score. Then run the script from the command line with python pyRosetta</mark> _ <mark>1YY8.py (note that it may take up a couple of minutes to load the module the first time you run it; it will also print out many lines of initialization warnings before printing out what is in the code). What is the energy of the structure, and what categories are the primary contributors (weighted score) for and against the total energy? (describe the categories in words as on the lecture slides, not just the shortened names that appear)</mark>

**(C – 1 point)** <mark>In the code for part</mark> _ <mark>c(), Monte-Carlo side-chain packing is implemented. At the indicated region, add code to print out the post-packed energy score. At the bottom of the script, uncomment part</mark> _ <mark>c() and run the script. What is the energy of the structure after packing, and which two categories have decreased the most compared to part (b)? (describe the categories in words as on the lecture slides, not just the shortened names that appear)</mark>

**(D – 1 point)** The 1YY8.rotated.pdb structure is the same as 1YY8.clean.pdb, except that one residue’s phi or psi angle has been changed. Fill in the code for <mark>part</mark> _ <mark>d() to load the rotated structure and perform side-chain packing on it, printing out the energy of the structure before and after side-chain packing. What is the energy before and after? Why is the post-side-chain packing energy not the same as that of part (c)?</mark>

**(E – 1 point)** Add code to <mark>part</mark> _ <mark>e() to determine which angle (phi or psi, as well as which residue number this angle belongs to) is changed in the rotated structure. Which residue/angle is it?</mark>

**(F – 1 point)** Using the residue and angle you determined in part (e), add code to <mark>part</mark> _ <mark>f() to determine the energy of the structure with that angle changed to each of the possible angles [-180,-179,….,180]. Which of these angles has the lowest energy, and does this agree with the corresponding angle in the original structure from part (b)?</mark>

<mark>Add each of these energies to the energies</mark> _ <mark>of</mark> _ <mark>angle list, and then modify set</mark> _ <mark>title to include the residue and angle that you changed. If you’ve done this correctly, an energy</mark> _ <mark>vs</mark> _ <mark>angle.pdf plot will be written to the directory where the script is. If you’re at an Athena workstation, you can view this PDF directly (Home Folder > pyRosetta_materials); if you’ve ssh’ed into Athena from a Terminal on your local computer, you can copy this PDF to your local computer and then open it in your computer’s PDF viewer with the following commands using scp (secure copy):</mark>

<mark><in a new Terminal on your computer, cd into your local computer’s directory where you want to download the PDF></mark>

<mark>scp <your Kerberos username>@athena.dialup.mit.edu:~/pyRosetta_materials/e</mark> nergy_vs_angle.pdf .

---

[← P1. Gibbs Sampler (10 Points).](03-p1-gibbs-sampler-10-points.md) · [Up: contents](index.md) · [P4. Queuing theory/connections (4 points). →](05-p4-queuing-theory-connections-4-points.md)
